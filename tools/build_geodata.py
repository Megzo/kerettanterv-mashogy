#!/usr/bin/env python3
"""Földrajzi adatfájlok a Földrajz 9–10. leckékhez → shared/foldrajz/*.js

    python3 -I tools/build_geodata.py --download [forrás …]   # letöltés a sources/foldrajz/<forrás>/ alá (+ manifest.json)
    python3 -I tools/build_geodata.py [fájl …]                 # a letöltött nyers adatokból megírja a shared/foldrajz/*.js-t

Források (a --download után a forrás neve szűkít, pl. `--download usgs etopo`):
  naturalearth  Natural Earth (közkincs): országok 1:110m, Kazahsztán 1:50m, admin-1 1:10m (megyék), időzónák 1:10m
  usgs          USGS ComCat FDSN (közkincs, USA szövetségi): M ≥ 6,0 földrengések 1975–2024, CSV
  noaavolc      NOAA NCEI Volcano Location Database (közkincs, USA szövetségi), JSON-API
  pb2002        PB2002 lemezhatár-modell (Bird 2003), a fraxen/tectonicplates GeoJSON-tükörből – ODC-BY 1.0
  etopo         NOAA ETOPO 2022 (15″), az ERD ERDDAP-szerveréről, szelvényenként egy sor / oszlop, CSV
  wpp2024       ENSZ World Population Prospects 2024, CSV (gz) – CC BY 3.0 IGO
  worldbank     Világbank WDI, API v2 (JSON) – CC BY 4.0

A letöltött fájlok megbízhatatlan bemenetek: a sources/ alatt vannak (.gitignore-on, csak a manifest.json kerül a
repóba), a szkript -I kapcsolóval fut, és csak JSON-t / CSV-t olvas belőlük (gzip a standard könyvtárral).
Kimenet és formátum: shared/foldrajz/README.md. Csak a Python standard könyvtárát használja.
A geometria-segédek (vágás, egyszerűsítés, kvantálás, delta) a tools/build_mapdata.py-ból jönnek.
"""
import csv
import datetime
import gzip
import hashlib
import io
import json
import math
import pathlib
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_mapdata as bm  # noqa: E402  (geometria-segédek: clip_ring, dp, dp_ring, quant, delta, area, …)

SRC = ROOT / "sources" / "foldrajz"
OUT = ROOT / "shared" / "foldrajz"
UA = {"User-Agent": "Mozilla/5.0 (geodata-downloader)"}
TODAY = datetime.date.today().isoformat()

NE_BASE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/"
NE_FILES = ["ne_110m_admin_0_countries", "ne_50m_admin_0_countries", "ne_10m_admin_1_states_provinces",
            "ne_10m_time_zones"]
USGS_URL = ("https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=1975-01-01&endtime=2025-01-01"
            "&minmagnitude=6&eventtype=earthquake&orderby=time-asc&limit=20000")
VOLC_URL = "https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/volcanolocs?page={}"
PB_BASE = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/"
PB_FILES = ["GeoJSON/PB2002_steps.json", "GeoJSON/PB2002_plates.json", "LICENSE.md", "README.md"]
ERDDAP = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ETOPO_2022_v1_15s"
WPP_BASE = "https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/CSV_FILES/"
WPP_FILES = ["WPP2024_PopulationByAge5GroupSex_Medium.csv.gz", "WPP2024_TotalPopulationBySex.csv.gz",
             "WPP2024_Demographic_Indicators_Medium.csv.gz"]
WB_API = "https://api.worldbank.org/v2/"

# ── domborzati szelvények: (azonosító, magyar cím, tengely, rögzített fok, kezdet, vég, mintavétel km-ben)
#    tengely 'lat': szélességi kör mentén (nyugat → kelet), 'lon': délkör mentén (dél → észak)
PROFILES = [
    ("japan", "Japán-árok – a Koreai-félsziget keleti pereme, Japán-tenger, Honsú, Csendes-óceán (é. sz. 38,3°, a 2011-es Tóhoku-rengés szélessége)",
     "lat", 38.3, 128.0, 150.0, 2.0),
    ("andok", "Andok – Csendes-óceán, Perui–chilei-árok, Altiplano, Chaco (d. sz. 20°)", "lat", -20.0, -80.0, -55.0, 2.0),
    ("atlanti", "Atlanti-óceán – Florida, Közép-atlanti-hátság, Marokkó (é. sz. 30°)", "lat", 30.0, -82.0, -8.0, 4.0),
    ("himalaja", "Himalája – Gangesz-síkság, Mount Everest, Tibeti-fennsík, Tarim-medence (k. h. 86,925°)",
     "lon", 86.925, 22.0, 40.0, 1.0),
    ("alfold-bukk", "Alföld – Bükk (k. h. 20,5°: Tisza-vidék, Mátraalja, Bükk-fennsík)", "lon", 20.5, 46.5, 48.3, 0.25),
]

# ── WPP 2024: korfa-országok (ISO3 → magyar név). A brief (10) négy országot + a világot kéri; az ötödik Kína
#    (az egykepolitika és a gyors öregedés miatt „harmadik sors” a korfán) – a koordinátor döntése nélkül választva.
WPP_LOCS = {"WLD": ("World", "Világ"), "NGA": ("Nigeria", "Nigéria"), "IND": ("India", "India"),
            "CHN": ("China", "Kína"), "JPN": ("Japan", "Japán"), "HUN": ("Hungary", "Magyarország")}

# ── Világbank WDI mutatók: rövid kulcs → (kód, magyar név, egység, tárolási szorzó)
WDI = {
    "gdpPpp": ("NY.GDP.PCAP.PP.KD", "egy főre jutó GDP, vásárlóerő-paritáson (állandó 2021-es nemzetközi dollár)", "$", 1),
    "gdpUsd": ("NY.GDP.PCAP.CD", "egy főre jutó GDP, folyó áron (USD)", "$", 1),
    "gniAtlas": ("NY.GNP.PCAP.CD", "egy főre jutó GNI, Atlas-módszer (folyó USD)", "$", 1),
    "gniPpp": ("NY.GNP.PCAP.PP.CD", "egy főre jutó GNI, vásárlóerő-paritáson (folyó nemzetközi dollár)", "$", 1),
    "le": ("SP.DYN.LE00.IN", "születéskor várható élettartam (év)", "év", 10),
    "pop": ("SP.POP.TOTL", "népesség (fő)", "ezer fő", 0.001),
    "empAgr": ("SL.AGR.EMPL.ZS", "foglalkoztatás: mezőgazdaság (a foglalkoztatottak %-a, ILO-becslés)", "%", 10),
    "empInd": ("SL.IND.EMPL.ZS", "foglalkoztatás: ipar (a foglalkoztatottak %-a, ILO-becslés)", "%", 10),
    "empSrv": ("SL.SRV.EMPL.ZS", "foglalkoztatás: szolgáltatás (a foglalkoztatottak %-a, ILO-becslés)", "%", 10),
}
WDI_AGG = {"WLD": "Világ", "EUU": "Európai Unió"}   # a Világbank-aggregátumok közül csak ezek


# ─────────────────────────────────────────────── letöltés
def get(url, timeout=600):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def save(folder, name, url, raw, files):
    (folder / name).parent.mkdir(parents=True, exist_ok=True)
    (folder / name).write_bytes(raw)
    files.append({"file": name, "url": url, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
    print(f"  {name}: {len(raw) / 1024:.0f} KB")


def manifest(folder, files, **meta):
    m = dict(meta, downloaded=TODAY, files=files)
    (folder / "manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ {folder.relative_to(ROOT)}/manifest.json ({len(files)} fájl)")


def dl_naturalearth():
    d, files = SRC / "naturalearth", []
    d.mkdir(parents=True, exist_ok=True)
    version = get(NE_BASE + "VERSION").decode("utf-8", "replace").strip()[:40]
    for f in NE_FILES:
        url = f"{NE_BASE}geojson/{f}.geojson"
        save(d, f + ".geojson", url, get(url), files)
    manifest(d, files, source="Natural Earth — https://www.naturalearthdata.com/",
             mirror="https://github.com/nvkelso/natural-earth-vector", version=version,
             licence="public domain (credit appreciated: Made with Natural Earth)")


def dl_usgs():
    d, files = SRC / "usgs", []
    d.mkdir(parents=True, exist_ok=True)
    save(d, "comcat_m6_1975-2024.csv", USGS_URL, get(USGS_URL), files)
    manifest(d, files, source="USGS Earthquake Hazards Program, ANSS Comprehensive Earthquake Catalog (ComCat)",
             service="https://earthquake.usgs.gov/fdsnws/event/1/",
             licence="public domain (U.S. federal government work)")


def dl_noaavolc():
    d, files = SRC / "noaavolc", []
    d.mkdir(parents=True, exist_ok=True)
    page, pages = 1, 1
    while page <= pages:
        url = VOLC_URL.format(page)
        raw = get(url)
        pages = min(int(json.loads(raw)["totalPages"]), 50)
        save(d, f"volcanolocs_p{page}.json", url, raw, files)
        page += 1
    manifest(d, files, source="NOAA NCEI / WDS, Global Volcano Locations Database",
             info="https://www.ngdc.noaa.gov/hazard/volcano.shtml", doi="10.7289/V5TB14V7",
             licence="public domain (U.S. federal government work); cite NCEI/WDS")


def dl_pb2002():
    d, files = SRC / "pb2002", []
    d.mkdir(parents=True, exist_ok=True)
    commit = json.loads(get("https://api.github.com/repos/fraxen/tectonicplates/commits?per_page=1"))[0]
    for f in PB_FILES:
        url = PB_BASE + f
        save(d, f.split("/")[-1], url, get(url), files)
    manifest(d, files, source="PB2002 — P. Bird (2003): An updated digital model of plate boundaries. "
             "Geochem. Geophys. Geosyst. 4(3), 1027, doi:10.1029/2001GC000252",
             mirror="https://github.com/fraxen/tectonicplates (H. Ahlenius, Nordpil; GeoJSON: csterling)",
             commit=commit.get("sha"), commit_date=commit.get("commit", {}).get("committer", {}).get("date"),
             licence="Open Data Commons Attribution License (ODC-BY) 1.0 — http://opendatacommons.org/licenses/by/1.0/")


ETOPO_SERVERS = [  # (ERDDAP-adatkészlet, változó, verzió) – az első, amelyik válaszol; a manifest rögzíti, melyik lett
    ("https://coastwatch.pfeg.noaa.gov/erddap/griddap/ETOPO_2022_v1_15s", "z",
     "NOAA NCEI ETOPO 2022 15 Arc-Second Global Relief Model (surface), doi:10.25921/fd45-gt74"),
    ("https://pae-paha.pacioos.hawaii.edu/erddap/griddap/etopo1_ice", "z",
     "NOAA NGDC ETOPO1 1 Arc-Minute Global Relief Model, Ice Surface (2009), doi:10.7289/V5C8276M"),
]


def dl_etopo():
    import time
    d, files = SRC / "etopo", []
    d.mkdir(parents=True, exist_ok=True)
    used = set()
    for pid, _t, axis, fix, a, b, _s in PROFILES:
        raw = None
        for base, var, ver in ETOPO_SERVERS:
            q = f"{var}[({fix})][({a}):1:({b})]" if axis == "lat" else f"{var}[({a}):1:({b})][({fix})]"
            url = base + ".csv?" + urllib.parse.quote(q, safe="():,")
            for attempt in range(3):
                try:
                    raw = get(url)
                    break
                except Exception as e:  # noqa: BLE001  (503 „temporary problem” az ERD-szerveren gyakori)
                    print(f"  {base.rsplit('/', 1)[-1]}: {e} – újra ({attempt + 1}/3)")
                    time.sleep(15)
            if raw:
                break
        if not raw:
            sys.exit(f"ETOPO: egyik szerver sem válaszolt ({pid})")
        save(d, f"szelveny-{pid}.csv", url, raw, files)
        files[-1]["dataset"] = ver
        used.add(ver)
    manifest(d, files, source="; ".join(sorted(used)), servers=[s[0] for s in ETOPO_SERVERS],
             licence="public domain (U.S. federal government work); "
             "ERDDAP: 'may be used and redistributed for free but is not intended for legal use'")


def dl_wpp():
    d, files = SRC / "wpp2024", []
    d.mkdir(parents=True, exist_ok=True)
    for f in WPP_FILES:
        save(d, f, WPP_BASE + f, get(WPP_BASE + f, timeout=900), files)
    manifest(d, files, source="United Nations, Department of Economic and Social Affairs, Population Division (2024). "
             "World Population Prospects 2024", info="https://population.un.org/wpp/",
             licence="Creative Commons Attribution 3.0 IGO (CC BY 3.0 IGO)")


def dl_worldbank():
    d, files = SRC / "worldbank", []
    d.mkdir(parents=True, exist_ok=True)
    url = WB_API + "country?format=json&per_page=400"
    save(d, "countries.json", url, get(url), files)
    for key, (code, *_r) in WDI.items():
        url = f"{WB_API}country/all/indicator/{code}?format=json&per_page=20000&date=1960:{int(TODAY[:4])}"
        raw = get(url)
        meta = json.loads(raw)[0]
        if int(meta.get("pages", 1)) > 1:
            sys.exit(f"{code}: több oldal ({meta}) – növeld a per_page-et")
        save(d, f"{code}.json", url, raw, files)
    manifest(d, files, source="World Bank, World Development Indicators (WDI), API v2",
             info="https://datacatalog.worldbank.org/search/dataset/0037712",
             licence="Creative Commons Attribution 4.0 (CC BY 4.0); some indicators: third-party (ILO, UN) via WDI")


DOWNLOADS = {"naturalearth": dl_naturalearth, "usgs": dl_usgs, "noaavolc": dl_noaavolc, "pb2002": dl_pb2002,
             "etopo": dl_etopo, "wpp2024": dl_wpp, "worldbank": dl_worldbank}


# ─────────────────────────────────────────────── közös: beolvasás, fejléc, kiírás
def man(src):
    p = SRC / src / "manifest.json"
    if not p.exists():
        sys.exit(f"hiányzik: {p.relative_to(ROOT)} — futtasd: python3 -I tools/build_geodata.py --download {src}")
    return json.loads(p.read_text(encoding="utf-8"))


def raw_path(src, name):
    p = SRC / src / name
    if not p.exists():
        sys.exit(f"hiányzik: {p.relative_to(ROOT)} — futtasd: python3 -I tools/build_geodata.py --download {src}")
    return p


def load_json(src, name):
    return json.loads(raw_path(src, name).read_text(encoding="utf-8"))


def load_csv_gz(src, name, keep):
    """Soronként olvasott gzip-CSV; csak azok a sorok, amelyekre keep(row) igaz (a WPP-fájlok több száz MB-osak)."""
    with gzip.open(raw_path(src, name), "rt", encoding="utf-8-sig", newline="") as g:
        return [r for r in csv.DictReader(g) if keep(r)]


def ne(name):
    return load_json("naturalearth", name + ".geojson")["features"]


def meta(fid, ver, src, lic, url, as_of):
    return {"id": fid, "ver": ver, "src": src, "lic": lic, "url": url, "asOf": as_of, "generated": TODAY}


def write_js(fname, var, m, desc, data, registry=None):
    """Kimenet: /* fejléc */ + window.VAR = {id, ver, src, lic, url, asOf, generated, …adat}.
    registry: ha meg van adva, window.VAR = window.VAR || {}; window.VAR[registry] = {…} (több fájl egy névtérben)."""
    head = (f"{desc.strip()}\n   Forrás: {m['src']}\n   Verzió: {m['ver']} · Licenc: {m['lic']}\n   URL: {m['url']}\n"
            f"   Letöltve: {m['asOf']} · Generálva: {m['generated']} (tools/build_geodata.py; a nyers fájlok URL-je és "
            f"SHA-256-ja: sources/foldrajz/<forrás>/manifest.json)\n   Formátum: shared/foldrajz/README.md")
    head = head.replace("*/", "* /")   # a megjegyzés nem zárulhat le idő előtt
    body = json.dumps(dict(m, **data), ensure_ascii=False, separators=(",", ":"))
    if registry:
        js = f"window.{var}=window.{var}||{{}};window.{var}[{json.dumps(registry)}]={body};\n"
    else:
        js = f"window.{var}={body};\n"
    path = OUT / fname
    path.write_text(f"/* {head}\n*/\n" + js, encoding="utf-8")
    kb = path.stat().st_size / 1024
    print(f"✓ {fname}: {kb:.0f} KB")
    if kb > 400:
        print(f"  FIGYELEM: {fname} > 400 KB")


def d1(vals):
    """1D delta-kódolás egészekre: [v0, v1 − v0, v2 − v1, …]."""
    out, prev = [], 0
    for v in vals:
        out.append(v - prev)
        prev = v
    return out


def rings(geom):
    return bm.rings_of(geom) if geom else []


def polys_of(geom):
    if not geom:
        return []
    return [geom["coordinates"]] if geom["type"] == "Polygon" else list(geom["coordinates"])


WORLD = (-180.0, -90.0, 180.0, 90.0)


def topo_simplify(groups, tol):
    """Topológiamegőrző egyszerűsítés: groups = [[gyűrű, …], …] (gyűrű: [(lon, lat), …], zárás nélkül).
    A szomszédos sokszögek közös határszakaszai (ívei) egyszer, azonosan egyszerűsödnek, így nem keletkezik rés
    vagy átfedés. Csomópont: ahol a pontot tartalmazó gyűrűk halmaza megváltozik."""
    key = lambda p: (round(p[0], 7), round(p[1], 7))
    owners = {}
    allr = [(gi, ri, [tuple(pt[:2]) for pt in r]) for gi, g in enumerate(groups) for ri, r in enumerate(g)]
    for idx, (_gi, _ri, r) in enumerate(allr):
        for pt in r:
            owners.setdefault(key(pt), set()).add(idx)
    cache, out = {}, [[None] * len(g) for g in groups]
    for idx, (gi, ri, r) in enumerate(allr):
        n = len(r)
        if n < 4:
            out[gi][ri] = r
            continue
        # a szomszéd(ok) halmaza pontonként; ahol csak ez a gyűrű birtokolja a pontot (a szomszéd ott nem tartalmaz
        # csúcsot), az előző szomszédot örökli – így a nem tökéletes topológia sem aprózza fel az íveket
        oth = [frozenset(owners[key(pt)] - {idx}) for pt in r]
        if any(oth):
            k0 = next(i for i in range(n) if oth[i])
            for i in range(k0 + 1, k0 + n):
                if not oth[i % n]:
                    oth[i % n] = oth[(i - 1) % n]
        junc = [i for i in range(n) if len(oth[i]) > 1 or oth[i] != oth[i - 1]]
        if not junc:
            out[gi][ri] = bm.dp_ring(r, tol)
            continue
        res = []
        for a, b in zip(junc, junc[1:] + [junc[0] + n]):
            arc = [r[k % n] for k in range(a, b + 1)]
            fk, rk = tuple(key(p) for p in arc), tuple(key(p) for p in reversed(arc))
            if fk in cache:
                sarc = cache[fk]
            elif rk in cache:
                sarc = list(reversed(cache[rk]))
            else:
                sarc = bm.dp(arc, tol)
                cache[fk] = sarc
            res += sarc[:-1]
        out[gi][ri] = res
    return out


def densify(r, seg):
    """A seg foknál hosszabb éleket (pl. a tengeri időzónák délkör menti, pólustól pólusig tartó éleit) közbülső
    pontokkal tölti ki – gömbön (ortho) enélkül a hátoldalra futó hosszú él rossz helyen metszené a peremet."""
    out, n = [], len(r)
    for i in range(n):
        a, b = r[i], r[(i + 1) % n]
        out.append(a)
        k = int(max(abs(b[0] - a[0]), abs(b[1] - a[1])) / seg)
        if k and abs(b[0] - a[0]) < 180:
            out += [(a[0] + (b[0] - a[0]) * j / (k + 1), a[1] + (b[1] - a[1]) * j / (k + 1)) for j in range(1, k + 1)]
    return out


def pack_rings(rs, q, min_area=0.0, seg=2.0):
    """Gyűrűk → kvantált, delta-kódolt lapos tömbök (a túl kicsik / elfajulók kimaradnak); a seg foknál hosszabb
    élek kitöltve (densify)."""
    res = []
    for r in rs:
        if seg:
            r = densify(list(r), seg)
        s = bm.quant(r, q, ring=True)
        if len(s) >= 3 and bm.area([(x / q, y / q) for x, y in s]) >= min_area:
            res.append(bm.delta(s))
    return res


def edge_union(ring_lists):
    """Szomszédos (közös csúcsokon érintkező) sokszögek egyesítése: a kétszer szereplő élek kiesnek, a maradék
    élekből gyűrűk fűződnek. ring_lists: [[gyűrű, …], …]. → gyűrűk listája (külső + lyukak)."""
    key = lambda p: (round(p[0], 7), round(p[1], 7))
    cnt, edges = {}, []
    for rs in ring_lists:
        for r in rs:
            pts = [key(p) for p in r]
            if pts[0] == pts[-1]:
                pts = pts[:-1]
            for a, b in zip(pts, pts[1:] + pts[:1]):
                if a == b:
                    continue
                edges.append((a, b))
                u = (a, b) if a < b else (b, a)
                cnt[u] = cnt.get(u, 0) + 1
    nxt = {}
    for a, b in edges:
        if cnt[(a, b) if a < b else (b, a)] == 1:
            nxt.setdefault(a, []).append(b)
    out = []
    while nxt:
        start = next(iter(nxt))
        ring, cur = [start], start
        while True:
            b = nxt[cur].pop()
            if not nxt[cur]:
                del nxt[cur]
            if b == start:
                break
            ring.append(b)
            cur = b
            if cur not in nxt:
                break
        out.append(ring)
    return out


def ne_version():
    return man("naturalearth").get("version", "?")


# ─────────────────────────────────────────────── országok (Natural Earth 1:110m)
# Vitatott / nem általánosan elismert területek (dis: 1 → a lecke szaggatott körvonallal rajzolja). A Natural Earth
# alapértelmezett („de facto”) nézetét követjük; a TYPE mező (Disputed / Indeterminate) erre nem jó, ezért kézi lista.
DISPUTED = {"ESH": "Nyugat-Szahara – Marokkó ellenőrzi és igényli, a Szahravi Arab Demokratikus Köztársaság is igényli",
            "PSE": "Palesztina – részben elismert állam, a határai vitatottak",
            "CYN": "Észak-Ciprus – csak Törökország ismeri el",
            "SOL": "Szomáliföld – nemzetközileg el nem ismert, Szomália része",
            "XKX": "Koszovó – részben elismert állam",
            "TWN": "Tajvan – a Kínai Népköztársaság igényli, részben elismert",
            "FLK": "Falkland-szigetek – brit tengerentúli terület, Argentína igényli"}
# Az Európai Unió tagállamai (2020. február 1. óta 27; 2026-ban ellenőrizve: nem változott)
EU27 = set("AUT BEL BGR HRV CYP CZE DNK EST FIN FRA DEU GRC HUN IRL ITA LVA LTU LUX MLT NLD POL PRT ROU SVK SVN ESP "
           "SWE".split())
# Natural Earth kód → a Világbank WDI kódja (ahol eltér)
ISO_FIX = {"KOS": "XKX"}
# a Natural Earth name_hu mezőjének javításai (ISO3 → magyar név)
NAME_HU_FIX = {"ESH": "Nyugat-Szahara", "SOL": "Szomáliföld", "CYN": "Észak-Ciprus", "XKX": "Koszovó",
               "USA": "Amerikai Egyesült Államok", "GBR": "Egyesült Királyság", "COD": "Kongói Demokratikus Köztársaság",
               "COG": "Kongói Köztársaság", "CIV": "Elefántcsontpart", "CZE": "Csehország", "MKD": "Észak-Macedónia",
               "SWZ": "Eswatini", "TLS": "Kelet-Timor", "MMR": "Mianmar", "KOR": "Dél-Korea", "PRK": "Észak-Korea", "TWN": "Tajvan"}


def iso3(p):
    for k in ("ISO_A3", "ISO_A3_EH", "ADM0_A3"):
        v = p.get(k)
        if v and v != "-99":
            return ISO_FIX.get(v, v)
    return None


def hu_names():
    """ISO3 → magyar név a Natural Earth 1:50m országrétegből (az több kis országot tartalmaz, mint az 1:110m)."""
    out = {}
    for f in ne("ne_50m_admin_0_countries"):
        p = f["properties"]
        k = iso3(p)
        if k and k not in out:
            out[k] = NAME_HU_FIX.get(k) or p.get("NAME_HU") or p.get("NAME")
    out.update(NAME_HU_FIX)
    return out


def build_orszagok():
    m = man("naturalearth")
    q, items = 100, []
    feats = ne("ne_110m_admin_0_countries")
    for f in feats:
        p = f["properties"]
        k = iso3(p)
        rs = [[tuple(pt[:2]) for pt in r[:-1]] for r in rings(f["geometry"])]
        it = {"iso": k, "n": NAME_HU_FIX.get(k) or p.get("NAME_HU") or p["NAME"], "en": p["NAME"],
              "lp": [round(p["LABEL_X"] * q), round(p["LABEL_Y"] * q)], "cont": p.get("CONTINENT")}
        if k in EU27:
            it["eu"] = 1
        if k in DISPUTED:
            it["dis"] = 1
        it["p"] = pack_rings(rs, q)
        items.append(it)
    items.sort(key=lambda it: it["iso"])
    dup = [k for k in {it["iso"] for it in items} if sum(1 for it in items if it["iso"] == k) > 1]
    if dup:
        sys.exit(f"orszagok: ismétlődő kód: {dup}")
    eu_missing = sorted(EU27 - {it["iso"] for it in items})
    data = {"q": q, "scale": "110m", "disputed": DISPUTED, "euMissing": eu_missing, "countries": items}
    write_js("orszagok.js", "FOLD_ORSZAGOK",
             meta("orszagok", f"Natural Earth {ne_version()}, ne_110m_admin_0_countries",
                  "Natural Earth – Admin 0 Countries 1:110m (naturalearthdata.com, „Made with Natural Earth”)",
                  "közkincs (public domain)", "https://www.naturalearthdata.com/", m["downloaded"]),
             f"""Országok 1:110m – tematikus térképhez (FoldChoro), buborék- és országpontokhoz (window.FOLD_ORSZAGOK)
   {len(items)} ország / terület; kulcs: iso (ISO 3166-1 alpha-3, a Világbank kódjával egyezően; Koszovó XKX, Észak-Ciprus
   CYN, Szomáliföld SOL). A Natural Earth »de facto« határait mutatja. Vitatott: dis: 1 (lista: disputed).
   Az 1:110m-es rétegből hiányzó kis EU-tagállamok: {', '.join(eu_missing) or '–'} (pontként a WDI-ből / a .md-ből).""",
             data)
    return {it["iso"]: it for it in items}


# ─────────────────────────────────────────────── megyék (Natural Earth admin-1 1:10m, Magyarország)
MJV = {"Sopron": "Győr-Moson-Sopron", "Győr": "Győr-Moson-Sopron", "Szeged": "Csongrád-Csanád",
       "Hódmezővásárhely": "Csongrád-Csanád", "Salgótarján": "Nógrád", "Szolnok": "Jász-Nagykun-Szolnok", "Érd": "Pest",
       "Eger": "Heves", "Miskolc": "Borsod-Abaúj-Zemplén", "Dunaújváros": "Fejér", "Székesfehérvár": "Fejér",
       "Kecskemét": "Bács-Kiskun", "Tatabánya": "Komárom-Esztergom", "Szombathely": "Vas", "Zalaegerszeg": "Zala",
       "Nagykanizsa": "Zala", "Veszprém": "Veszprém", "Kaposvár": "Somogy", "Pécs": "Baranya", "Szekszárd": "Tolna",
       "Békéscsaba": "Békés", "Debrecen": "Hajdú-Bihar", "Nyíregyháza": "Szabolcs-Szatmár-Bereg"}
SEAT = {"Baranya": "Pécs", "Bács-Kiskun": "Kecskemét", "Békés": "Békéscsaba", "Borsod-Abaúj-Zemplén": "Miskolc",
        "Csongrád-Csanád": "Szeged", "Fejér": "Székesfehérvár", "Győr-Moson-Sopron": "Győr", "Hajdú-Bihar": "Debrecen",
        "Heves": "Eger", "Jász-Nagykun-Szolnok": "Szolnok", "Komárom-Esztergom": "Tatabánya", "Nógrád": "Salgótarján",
        "Pest": "Budapest", "Somogy": "Kaposvár", "Szabolcs-Szatmár-Bereg": "Nyíregyháza", "Tolna": "Szekszárd",
        "Vas": "Szombathely", "Veszprém": "Veszprém", "Zala": "Zalaegerszeg", "Budapest": "Budapest"}


def build_megyek():
    m = man("naturalearth")
    q = 1000
    feats = [f for f in ne("ne_10m_admin_1_states_provinces") if f["properties"].get("adm0_a3") == "HUN"]
    counties, cities = {}, {}
    for f in feats:
        p = f["properties"]
        n = p.get("name_hu") or p["name"]
        t = p.get("type_en")
        rs = [[tuple(pt[:2]) for pt in r] for r in rings(f["geometry"])]
        if t == "Urban county":
            cities[n] = rs
        else:
            counties[n] = {"rs": rs, "iso": p.get("iso_3166_2"), "en": p["name"], "nuts2": p.get("region")}
    if len(counties) != 20 or set(MJV) != set(cities):
        sys.exit(f"megyek: váratlan szerkezet: {len(counties)} megye/főváros, megyei jogú városok: {sorted(cities)}")
    groups, names = [], sorted(counties, key=lambda n: (n != "Budapest", n))
    for n in names:
        parts = [counties[n]["rs"]] + [cities[c] for c, cn in MJV.items() if cn == n]
        u = edge_union(parts)
        groups.append(u)
    items = []
    for n, rs in zip(names, groups):
        outer = [r for r in rs if bm.area(r) > 1e-4]
        items.append({"n": n, "iso": counties[n]["iso"], "seat": SEAT[n], "nuts2": counties[n]["nuts2"],
                      "lp": [round(v * q) for v in bm.label_point(outer)], "p": pack_rings(rs, q)})
    # az ország körvonala: az összes megye egyesítése
    border = edge_union(groups)
    data = {"q": q, "scale": "10m", "counties": items, "border": pack_rings(border, q, 1e-4)}
    nring = {it["n"]: len(it["p"]) for it in items}
    write_js("megyek.js", "FOLD_MEGYEK",
             meta("megyek", f"Natural Earth {ne_version()}, ne_10m_admin_1_states_provinces (HUN)",
                  "Natural Earth – Admin 1 States, Provinces 1:10m, Magyarország (naturalearthdata.com)",
                  "közkincs (public domain)", "https://www.naturalearthdata.com/", m["downloaded"]),
             f"""Magyarország 19 megyéje és Budapest, 1:10m (window.FOLD_MEGYEK)
   A Natural Earth a 23 megyei jogú várost külön egységként adja; itt a megyéjükbe olvasztva (közös élek elhagyásával),
   hogy a KSH megyei adataival (19 megye + Budapest) egyezzen. Egyszerűsítés nincs (a közös határok pontosan
   illeszkednek). Gyűrűk száma: {nring}. border: az országhatár (a megyék egyesítése).""",
             data)


# ─────────────────────────────────────────────── időzónák (Natural Earth 1:10m + javítótábla)
# A Natural Earth időzóna-rétege 2012-es állapotú (pl. Oroszország akkor egész évben „nyári” időt használt). A javítások
# a mai (2026) NORMÁLIDŐT (téli időt) adják; nyári időszámítást a réteg nem modellez. Forrás: IANA tz database (tzdata,
# közkincs), a változások napja zárójelben. A javító sokszögek a Natural Earth 1:50m ország- vagy 1:10m admin-1
# rétegéből jönnek, és a zónarétegre rajzolandók (fixes) – találatvizsgálatnál előbb a fixes-t nézd.
TZ_COUNTRY_FIX = {  # ADM0_A3 (Natural Earth 1:50m) → (perc, mióta, megjegyzés)
    "KAZ": (300, "2024-03-01", "Kazahsztán egyetlen zónára (UTC+5) tért át"),
    "TUR": (180, "2016-09-07", "Törökország állandó UTC+3"),
    "VEN": (-240, "2016-05-01", "Venezuela UTC−4:30 → UTC−4"),
    "SDN": (120, "2017-11-01", "Szudán UTC+3 → UTC+2"),
    "SDS": (120, "2021-02-01", "Dél-Szudán UTC+3 → UTC+2"),
    "MAR": (60, "2018-10-28", "Marokkó állandó UTC+1 (ramadánkor UTC+0)"),
    "SAH": (60, "2018-10-28", "Nyugat-Szahara: a marokkói időt követi (vitatott terület)"),
    "NAM": (120, "2017-10-24", "Namíbia egész évben UTC+2"),
    "PRY": (-180, "2024-10-14", "Paraguay állandó UTC−3"),
    "JOR": (180, "2022-10-28", "Jordánia állandó UTC+3"),
    "SYR": (180, "2022-10-28", "Szíria állandó UTC+3"),
    "GRL": (-120, "2023-03-25", "Grönland nagy része UTC−2 (egyszerűsítés: Pituffik UTC−4, Danmarkshavn UTC+0 nincs külön)"),
    "NFK": (660, "2015-10-04", "Norfolk-sziget UTC+11:30 → UTC+11"),
}
TZ_ADMIN1_FIX = {  # ISO 3166-2 (Natural Earth admin-1) → (perc, mióta, megjegyzés)
    "MX-ROO": (-300, "2015-02-01", "Quintana Roo UTC−5"),
    "MX-CHH": (-360, "2022-10-30", "Chihuahua UTC−6 (egyszerűsítés: a határmenti községek UTC−7)"),
    "CA-YT": (-420, "2020-11-01", "Yukon állandó UTC−7"),
    "BR-AC": (-300, "2013-11-10", "Acre UTC−5"),
    "CL-MA": (-180, "2016-05-15", "Magallanes állandó UTC−3"),
}
# Oroszország (2014. október 26. óta, a 2016-os és 2020-as regionális változásokkal). Szaha (Jakutföld) egyszerűsítve
# egészében UTC+9 (keleti járásai valójában UTC+10 és UTC+11). A Krím és Szevasztopol: de facto moszkvai idő 2014 óta,
# vitatott terület (dis: 1).
RU_TZ = {2: "KGD", 3: "AD ARK BEL BRY CE CU SPE DA IN IVA KB KL KLU KC KR KIR KO KOS KDA KRS LEN LIP ME MO MOW MOS MUR "
                   "NEN NIZ SE NGR ORL PNZ PSK ROS RYA SMO STA TAM TA TUL TVE VLA VGG VLG VOR YAR",
         4: "AST SAM SAR UD ULY", 5: "BA CHE KGN KHM ORE PER SVE TYU YAN", 6: "OMS", 7: "ALT AL KEM KK KYA NVS TOM TY",
         8: "BU IRK", 9: "AMU SA ZAB", 10: "KHA PRI YEV", 11: "MAG SAK", 12: "KAM CHU"}
RU_DISPUTED = {"UA-43": "Krím", "UA-40": "Szevasztopol"}


def utc_label(minutes):
    sign = "+" if minutes >= 0 else "−"
    h, mm = divmod(abs(minutes), 60)
    return f"UTC{sign}{h}" + (f":{mm:02d}" if mm else "")


def build_idozonak():
    m = man("naturalearth")
    q, tol, amin = 100, 0.15, 0.05
    zones = {}
    for f in ne("ne_10m_time_zones"):
        p = f["properties"]
        mins = round(float(p["zone"]) * 60)
        z = zones.setdefault(mins, {"rs": [], "places": []})
        z["rs"] += [[tuple(pt[:2]) for pt in r[:-1]] for r in rings(f["geometry"])]
        if p.get("places") and p["places"] not in z["places"]:
            z["places"].append(p["places"])
    keys = sorted(zones)
    simp = topo_simplify([zones[k]["rs"] for k in keys], tol)
    zitems = []
    for k, rs in zip(keys, simp):
        zitems.append({"m": k, "n": utc_label(k), "places": "; ".join(zones[k]["places"])[:300],
                       "p": pack_rings(rs, q, amin)})
    # javítások
    fixes = []
    c50 = {f["properties"]["ADM0_A3"]: f for f in ne("ne_50m_admin_0_countries")}
    for code, (mins, since, note) in TZ_COUNTRY_FIX.items():
        if code not in c50:
            sys.exit(f"idozonak: nincs ilyen ország az 1:50m rétegben: {code}")
        f = c50[code]
        rs = [[tuple(pt[:2]) for pt in r[:-1]] for r in rings(f["geometry"])]
        it = {"k": code, "nm": NAME_HU_FIX.get(code) or f["properties"].get("NAME_HU") or f["properties"]["NAME"],
              "m": mins, "n": utc_label(mins), "since": since, "note": note,
              "p": pack_rings([bm.dp_ring(r, tol) for r in rs], q, amin)}
        if code == "SAH":
            it["dis"] = 1
        fixes.append(it)
    ru_code = {f"RU-{c}": h * 60 for h, cs in RU_TZ.items() for c in cs.split()}
    a1 = [f for f in ne("ne_10m_admin_1_states_provinces")
          if f["properties"].get("iso_3166_2") in ru_code or f["properties"].get("iso_3166_2") in TZ_ADMIN1_FIX
          or f["properties"].get("iso_3166_2") in RU_DISPUTED]
    seen = {f["properties"]["iso_3166_2"] for f in a1}
    miss = sorted((set(ru_code) | set(TZ_ADMIN1_FIX) | set(RU_DISPUTED)) - seen)
    if miss:
        sys.exit(f"idozonak: hiányzó admin-1 egységek: {miss}")
    ru = [f for f in a1 if f["properties"]["iso_3166_2"] in ru_code or f["properties"]["iso_3166_2"] in RU_DISPUTED]
    ru_simp = topo_simplify([[[tuple(pt[:2]) for pt in r[:-1]] for r in rings(f["geometry"])] for f in ru], tol)
    for f, rs in zip(ru, ru_simp):
        p = f["properties"]
        c = p["iso_3166_2"]
        mins = ru_code.get(c, 180)
        it = {"k": c, "nm": p.get("name_hu") or p["name"], "m": mins, "n": utc_label(mins), "since": "2014-10-26",
              "note": "Oroszország", "p": pack_rings(rs, q, amin)}
        if c in RU_DISPUTED:
            it["dis"] = 1
            it["note"] = "de facto moszkvai idő 2014 óta – vitatott terület"
        if c in ("RU-AST", "RU-SAR", "RU-ULY", "RU-NVS", "RU-ALT", "RU-AL", "RU-TOM", "RU-ZAB", "RU-MAG", "RU-SAK"):
            it["since"] = "2016"
        if c == "RU-VGG":
            it["since"] = "2020-12-27"
        if c == "RU-SA":
            it["note"] = "egyszerűsítés: Szaha keleti járásai UTC+10 / UTC+11"
        fixes.append(it)
    for f in a1:
        c = f["properties"]["iso_3166_2"]
        if c in TZ_ADMIN1_FIX:
            mins, since, note = TZ_ADMIN1_FIX[c]
            rs = [[tuple(pt[:2]) for pt in r[:-1]] for r in rings(f["geometry"])]
            fixes.append({"k": c, "nm": f["properties"].get("name_hu") or f["properties"]["name"], "m": mins,
                          "n": utc_label(mins), "since": since, "note": note,
                          "p": pack_rings([bm.dp_ring(r, tol) for r in rs], q, amin)})
    data = {"q": q, "scale": "10m", "zones": zitems, "fixes": fixes}
    write_js("idozonak.js", "FOLD_IDOZONAK",
             meta("idozonak", f"Natural Earth {ne_version()}, ne_10m_time_zones (2012-es állapot) + javítótábla (2026)",
                  "Natural Earth – Time Zones 1:10m (naturalearthdata.com); javítások: IANA tz database (közkincs), "
                  "Natural Earth 1:50m országok és 1:10m admin-1 sokszögeivel",
                  "közkincs (public domain)", "https://www.naturalearthdata.com/", m["downloaded"]),
             f"""Időzónák – normálidő (téli idő), eltérés UTC-től percben (window.FOLD_IDOZONAK)
   zones: a Natural Earth zónái (a tengereken a 15°-os tengeri zónák), ELAVULT, 2012-es állapot.
   fixes: {len(fixes)} javító sokszög (ország / admin-1), a zónák FÖLÉ rajzolandó; találatvizsgálatnál előbb ezt nézd.
   Nyári időszámítás nincs a rétegben (a lecke `.md`-je adja meg). Egyszerűsítés: topológiamegőrző Douglas–Peucker,
   {tol}° tűrés.""",
             data)


# ─────────────────────────────────────────────── lemezhatárok (PB2002, Bird 2003) – ODC-BY 1.0
PB_TYPE = {"OSR": "d", "CRB": "d", "SUB": "s", "CCB": "c", "OCB": "c", "OTF": "t", "CTF": "t"}
PB_CLASS = {"OSR": "óceáni szétnyíló hátság", "CRB": "kontinentális hasadék (rift)", "SUB": "alábukási öv",
            "CCB": "kontinentális összetartó határ (ütközés)", "OCB": "óceáni összetartó határ",
            "OTF": "óceáni transzform vető", "CTF": "kontinentális transzform vető"}
PB_TYPES_HU = {"d": "szétnyíló (divergens)", "s": "alábukó (szubdukció)", "c": "ütköző / egyéb összetartó",
               "t": "elcsúszó (transzform)"}
# A kerettanterv 9 nagy lemeze (9–10. évf., topográfia) → a PB2002 lemezkódjai
BIG9 = {"Afrikai-lemez": ["AF", "SO"], "Antarktiszi-lemez": ["AN"], "Ausztrál–Indiai-lemez": ["IN", "AU"],
        "Csendes-óceáni-lemez": ["PA"], "Dél-amerikai-lemez": ["SA"], "Észak-amerikai-lemez": ["NA"],
        "Eurázsiai-lemez": ["EU"], "Fülöp-lemez": ["PS"], "Nasca-lemez": ["NZ"]}
PLATE_HU = {"AF": "Afrikai (Núbiai) lemez", "SO": "Szomáliai lemez", "AN": "Antarktiszi-lemez", "IN": "Indiai-lemez",
            "AU": "Ausztrál-lemez", "PA": "Csendes-óceáni-lemez", "SA": "Dél-amerikai-lemez", "NA": "Észak-amerikai-lemez",
            "EU": "Eurázsiai-lemez", "PS": "Fülöp-lemez", "NZ": "Nasca-lemez", "AR": "Arab-lemez", "CA": "Karibi-lemez",
            "CO": "Kókusz-lemez", "JF": "Juan de Fuca-lemez", "SC": "Scotia-lemez", "AT": "Anatóliai-lemez",
            "AS": "Égei-lemez", "SU": "Szunda-lemez", "YA": "Jangce-lemez", "AM": "Amúr-lemez", "OK": "Ohotszki-lemez",
            "RI": "Rivera-lemez", "MA": "Mariana-lemez", "ON": "Okinava-lemez", "BU": "Burmai-lemez", "CL": "Karolina-lemez",
            "ND": "Észak-andoki-lemez", "PM": "Panama-lemez", "AP": "Altiplano-lemez", "TO": "Tonga-lemez",
            "KE": "Kermadec-lemez", "NH": "Új-hebridai-lemez", "SW": "Sandwich-lemez", "GP": "Galápagos-lemez",
            "EA": "Húsvét-lemez", "JZ": "Juan Fernández-lemez"}


def build_lemezhatarok():
    m = man("pb2002")
    q = 100
    steps = load_json("pb2002", "PB2002_steps.json")["features"]
    # 1) egymást követő, azonos határú és osztályú lépések összefűzése vonalakká
    runs, cur, key0 = [], None, None
    for f in steps:
        p = f["properties"]
        k = (p["PLATEBOUND"], p["STEPCLASS"])
        pts = [tuple(c[:2]) for c in f["geometry"]["coordinates"]]
        if cur and k == key0 and abs(cur["pts"][-1][0] - pts[0][0]) < 1e-6 and abs(cur["pts"][-1][1] - pts[0][1]) < 1e-6:
            cur["pts"] += pts[1:]
            cur["st"].append(p)
        else:
            cur = {"k": k, "pts": list(pts), "st": [p]}
            runs.append(cur)
            key0 = k
    grp = {}
    for r in runs:
        b, cls = r["k"]
        g = grp.setdefault((b, PB_TYPE[cls]), {"L": 0.0, "vd": 0.0, "vr": 0.0, "cls": {}, "p": []})
        for st in r["st"]:
            g["L"] += st["STEPLENGTH"]
            g["vd"] += st["VELOCITYDI"] * st["STEPLENGTH"]
            g["vr"] += st["VELOCITYRI"] * st["STEPLENGTH"]
            g["cls"][cls] = g["cls"].get(cls, 0) + st["STEPLENGTH"]
        ql = bm.quant(bm.dp(r["pts"], 0.05), q)
        if len(ql) >= 2:
            g["p"].append(ql)
    lines = []
    for (b, t), g in sorted(grp.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        if not g["p"]:
            continue
        L = g["L"] or 1
        lines.append({"b": b, "t": t, "c": max(g["cls"], key=g["cls"].get), "km": round(L),
                      "vd": round(g["vd"] / L), "vr": round(g["vr"] / L),
                      "p": [bm.delta(l) for l in bm.merge_lines(g["p"])]})
    # 2) sebesség-mintapontok kb. 500 km-enként (nyilakhoz): hely, a határ iránya, relatív sebesség
    vel = {"lon": [], "lat": [], "az": [], "v": [], "vaz": [], "vd": [], "vr": [], "t": []}
    acc = 1e9
    for f in steps:
        p = f["properties"]
        acc += p["STEPLENGTH"]
        if acc < 500:
            continue
        acc = 0
        lon = (p["STARTLONG"] + p["FINALLONG"]) / 2 if abs(p["STARTLONG"] - p["FINALLONG"]) < 180 else p["STARTLONG"]
        for k, v in (("lon", round(lon * q)), ("lat", round((p["STARTLAT"] + p["FINALLAT"]) / 2 * q)),
                     ("az", round(p["AZIMUTHCEN"])), ("v", round(p["VELOCITYLE"])), ("vaz", round(p["VELOCITYAZ"])),
                     ("vd", round(p["VELOCITYDI"])), ("vr", round(p["VELOCITYRI"])), ("t", PB_TYPE[p["STEPCLASS"]])):
            vel[k].append(v)
    # 3) lemezek (54 sokszög, 52 lemez), topológiamegőrző egyszerűsítéssel
    pf = load_json("pb2002", "PB2002_plates.json")["features"]
    groups = [[[tuple(pt[:2]) for pt in r[:-1]] for r in rings(f["geometry"])] for f in pf]
    simp = topo_simplify(groups, 0.08)
    big = {c: g for g, cs in BIG9.items() for c in cs}
    plates = {}
    for f, rs in zip(pf, simp):
        p = f["properties"]
        c = p["Code"]
        it = plates.setdefault(c, {"code": c, "n": PLATE_HU.get(c, p["PlateName"] + "-lemez"), "en": p["PlateName"],
                                   "p": []})
        if c in big:
            it["g"] = big[c]
        it["p"] += pack_rings(rs, q, 0.01)
    for c, it in plates.items():
        rs = [list(zip(*[iter(TortDecode(r, q))] * 2)) for r in it["p"]]
        it["lp"] = [round(v * q) for v in bm.label_point(rs)]
    data = {"q": q, "types": PB_TYPES_HU, "classes": PB_CLASS, "big9": BIG9, "lines": lines,
            "vel": {k: (d1(v) if k in ("lon", "lat") else v) for k, v in vel.items()},
            "plates": sorted(plates.values(), key=lambda it: (it.get("g") is None, it["code"]))}
    write_js("lemezhatarok.js", "FOLD_LEMEZHATAROK",
             meta("lemezhatarok", f"PB2002 (Bird 2003), fraxen/tectonicplates @{(m.get('commit') or '')[:7]}",
                  "P. Bird (2003): An updated digital model of plate boundaries. Geochemistry, Geophysics, Geosystems "
                  "4(3), 1027, doi:10.1029/2001GC000252 – GeoJSON: H. Ahlenius (Nordpil), csterling; "
                  "github.com/fraxen/tectonicplates",
                  "Open Data Commons Attribution License (ODC-BY) 1.0 – a forrás megjelölése kötelező",
                  "https://github.com/fraxen/tectonicplates", m["downloaded"]),
             f"""Kőzetlemezek és lemezhatárok – PB2002 modell (window.FOLD_LEMEZHATAROK)
   FORRÁSMEGJELÖLÉS KÖTELEZŐ (ODC-BY 1.0): „Lemezhatárok: P. Bird (2003), PB2002; GeoJSON: Hugo Ahlenius, Nordpil”.
   lines: {len(lines)} tétel – lemezpáronként (b: „AF-AN”) és típusonként (t: d / s / c / t) a határ vonalai
   (p: [vonal, …], Douglas–Peucker 0,05°); c: a tétel hossz szerint leggyakoribb PB2002-lépésosztálya, km: hossz,
   vd: átlagos szétnyílási sebesség mm/év (negatív = közeledés), vr: átlagos jobbos elcsúszás mm/év.
   vel: {len(vel['t'])} mintapont kb. 500 km-enként (lon, lat delta-kódolva, × q), az: a határ iránya (fok),
   v / vaz: relatív sebesség mm/év és iránya (fok), vd, vr, t. plates: 52 lemez, g: a kerettanterv 9 nagy lemeze.""",
             data)


def TortDecode(flat, q):
    out, x, y = [], 0, 0
    for i in range(0, len(flat), 2):
        x += flat[i]; y += flat[i + 1]
        out += [x / q, y / q]
    return out


# ─────────────────────────────────────────────── földrengések (USGS ComCat)
def build_rengesek():
    m = man("usgs")
    q = 100
    rows = list(csv.DictReader(io.StringIO(raw_path("usgs", "comcat_m6_1975-2024.csv").read_text(encoding="utf-8"))))
    rows = [r for r in rows if r.get("type") == "earthquake" and r.get("mag") and float(r["mag"]) >= 6.0]
    rows.sort(key=lambda r: r["time"])
    ep = datetime.date(1975, 1, 1)
    cols = {"day": [], "lon": [], "lat": [], "dep": [], "mag": []}
    for r in rows:
        t = datetime.date.fromisoformat(r["time"][:10])
        cols["day"].append((t - ep).days)
        cols["lon"].append(round(float(r["longitude"]) * q))
        cols["lat"].append(round(float(r["latitude"]) * q))
        cols["dep"].append(max(0, round(float(r["depth"] or 0))))
        cols["mag"].append(round(float(r["mag"]) * 10))
    big = [(r["time"][:10], float(r["mag"]), r["place"]) for r in rows if float(r["mag"]) >= 8.5]
    data = {"q": q, "epoch": "1975-01-01", "n": len(rows), "minMag": 6.0, "range": ["1975-01-01", "2024-12-31"],
            "day": d1(cols["day"]), "lon": cols["lon"], "lat": cols["lat"], "dep": cols["dep"], "mag": cols["mag"]}
    write_js("rengesek.js", "FOLD_RENGESEK",
             meta("rengesek", f"USGS ComCat, lekérdezve {m['downloaded']}",
                  "U.S. Geological Survey, Earthquake Hazards Program – ANSS Comprehensive Earthquake Catalog (ComCat), "
                  "FDSN Event Web Service", "közkincs (USA szövetségi kormányzati mű)", USGS_URL, m["downloaded"]),
             f"""Földrengések, M ≥ 6,0, 1975–2024 – {len(rows)} esemény időrendben (window.FOLD_RENGESEK)
   Oszloponként (az i. elem az i. rengés): day: napok 1975-01-01 óta, DELTA-kódolva (futó összeg); lon, lat: fok × q
   (q = {q}); dep: fészekmélység km; mag: magnitúdó × 10 (a ComCat preferált magnitúdója, típusa vegyes: Mw, Ms, mb).
   M ≥ 8,5: {'; '.join(f'{d} M{mg:.1f}' for d, mg, _p in big)}.""",
             data)


# ─────────────────────────────────────────────── vulkánok (NOAA NCEI)
VOLC_TYPE = [("rv", "rétegvulkán", ["Stratovolcano", "Stratovolcanoes", "Stratovolcano(es)"]),
             ("pv", "pajzsvulkán", ["Shield volcano", "Shield", "Shield volcanoes", "Pyroclastic shield"]),
             ("ov", "összetett vulkán", ["Complex volcano", "Compound volcano", "Somma volcano", "Volcanic complex"]),
             ("ka", "kaldera", ["Caldera"]),
             ("kk", "salak- és tufakúp", ["Cinder cone", "Cinder cones", "Scoria cone", "Scoria cones", "Pyroclastic cone",
                                          "Pyroclastic cones", "Lava cone", "Cone", "Pumice cone", "Tuff cone", "Tuff rings"]),
             ("ld", "lávadóm", ["Lava dome", "Lava domes"]),
             ("ta", "tenger alatti vulkán", ["Submarine volcano", "Submarine", "Submarine volcanoes", "Submarine volcano?"]),
             ("vm", "vulkánmező", ["Volcanic field"]),
             ("hv", "hasadékvulkán", ["Fissure vent", "Fissure vents", "Crater rows"]),
             ("ma", "maar, robbanásos kráter", ["Maar", "Maars", "Explosion crater"]),
             ("eg", "egyéb / ismeretlen", [])]
VOLC_LAST = ["", "1964 vagy később", "1900–1963", "1800–1899", "1700–1799", "1500–1699", "i. sz. 1–1499",
             "i. e. (holocén)", "kormeghatározás nélkül, valószínűleg holocén", "bizonytalan / ismeretlen"]


def build_vulkanok():
    m = man("noaavolc")
    q = 100
    items = []
    for fe in m["files"]:
        items += load_json("noaavolc", fe["file"])["items"]
    tmap = {raw: i for i, (_c, _n, raws) in enumerate(VOLC_TYPE) for raw in raws}
    out = {"lon": [], "lat": [], "el": [], "t": [], "le": [], "n": []}
    skipped = 0
    for it in sorted(items, key=lambda x: (x.get("longitude") or 0)):
        if (it.get("morphology") == "Not Volcanic" or it.get("timeErupt") == "Q"
                or (it.get("status") or "").startswith("Pleistocene") or it.get("latitude") is None):
            skipped += 1
            continue
        te = it.get("timeErupt") or ""
        le = int(te[1]) if len(te) == 2 and te[0] == "D" and te[1].isdigit() else (8 if te.startswith("U") and te != "Unknown" else 9)
        out["lon"].append(round(float(it["longitude"]) * q))
        out["lat"].append(round(float(it["latitude"]) * q))
        out["el"].append(int(it["elevation"]) if it.get("elevation") is not None else None)
        out["t"].append(tmap.get(it.get("morphology"), len(VOLC_TYPE) - 1))
        out["le"].append(le)
        out["n"].append(it.get("name") or "")
    data = {"q": q, "types": [[c, n] for c, n, _r in VOLC_TYPE], "last": VOLC_LAST, "n": len(out["n"]),
            "lon": d1(out["lon"]), "lat": out["lat"], "el": out["el"], "t": out["t"], "le": out["le"], "names": out["n"]}
    write_js("vulkanok.js", "FOLD_VULKANOK",
             meta("vulkanok", f"NOAA NCEI Volcano Location Database, lekérdezve {m['downloaded']}",
                  "NOAA National Centers for Environmental Information (NCEI) / World Data Service: Global Volcano "
                  "Locations Database, doi:10.7289/V5TB14V7 (a helyek nagyrészt a Smithsonian Global Volcanism Program "
                  "katalógusára épülnek)", "közkincs (USA szövetségi kormányzati mű; forrásmegjelölés kérés)",
                  "https://www.ngdc.noaa.gov/hazard/volcano.shtml", m["downloaded"]),
             f"""Holocén vulkánok helye, típusa és utolsó kitörése – {len(out['n'])} vulkán, hosszúság szerint (window.FOLD_VULKANOK)
   Oszloponként: lon (fok × q, DELTA-kódolva), lat (fok × q), el: csúcsmagasság m (negatív: tenger alatt; null: nincs
   adat), t: típus indexe a types-ban, le: utolsó kitörés kódja a last-ban (1–7: a GVP D1–D7 osztályai), names: angol
   név. Kihagyva {skipped} tétel (nem vulkáni, pleisztocén). A Kárpát-medence vulkánjai (pl. Csomád) nincsenek a
   holocén listán – ha kell, a lecke `.md`-je adja meg.""",
             data)


# ─────────────────────────────────────────────── domborzati szelvények (ETOPO)
def build_szelvenyek():
    m = man("etopo")
    byfile = {f["file"]: f for f in m["files"]}
    for pid, title, axis, fix, a, b, step_km in PROFILES:
        fe = byfile.get(f"szelveny-{pid}.csv")
        if not fe:
            print(f"  kihagyva: szelveny-{pid} (nincs letöltve)")
            continue
        text = raw_path("etopo", fe["file"]).read_text(encoding="utf-8")
        rows = list(csv.reader(io.StringIO(text)))[2:]
        pts = sorted((float(r[1]) if axis == "lat" else float(r[0]), float(r[2])) for r in rows if len(r) >= 3 and r[2] not in ("", "NaN"))
        km_deg = 111.195 * (math.cos(math.radians(fix)) if axis == "lat" else 1.0)
        step = step_km / km_deg
        n = int(round((b - a) / step))
        z = []
        j = 0
        for i in range(n + 1):
            lo, hi = a + (i - 0.5) * step, a + (i + 0.5) * step
            while j < len(pts) and pts[j][0] < lo:
                j += 1
            k, acc = j, []
            while k < len(pts) and pts[k][0] < hi:
                acc.append(pts[k][1]); k += 1
            if not acc:   # üres cella (a rács a szelvény végén fél cellával eltolva kezdődik): a legközelebbi minta
                c = a + i * step
                acc = [min(pts, key=lambda t: abs(t[0] - c))[1]]
            z.append(round(sum(acc) / len(acc)))
        ver = fe.get("dataset", m.get("source", "ETOPO"))
        data = {"t": title, "axis": axis, "fix": fix, "from": a, "to": b, "step": round(step, 6), "km": step_km,
                "n": len(z), "zmin": min(z), "zmax": max(z), "z": d1(z)}
        along = "szélességi kör (nyugat → kelet)" if axis == "lat" else "délkör (dél → észak)"
        write_js(f"szelveny-{pid}.js", "FOLD_SZELVENY",
                 meta(f"szelveny-{pid}", ver.split(",")[0], ver, "közkincs (USA szövetségi kormányzati mű)",
                      fe["url"].split(".csv?")[0], m["downloaded"]),
                 f"""Domborzati / batimetriai szelvény: {title} (window.FOLD_SZELVENY['{pid}'])
   A szelvény egy {along} mentén fut, {a}° → {b}°, {step_km} km-enként (= {step:.5f}°) a cella-átlag magassága
   méterben (tengerszint felett +, alatt −). z: DELTA-kódolva (futó összeg). i. pont helye: from + i × step fok.
   Legmélyebb / legmagasabb pont a mintavétel után: {min(z)} m / {max(z)} m (a valódi szélsőérték ennél nagyobb lehet).""",
                 data, registry=pid)


# ─────────────────────────────────────────────── korfa (ENSZ WPP 2024)
WPP_LOCID = {"WLD": 900, "NGA": 566, "IND": 356, "CHN": 156, "JPN": 392, "HUN": 348}


def build_korfa():
    m = man("wpp2024")
    ids = {str(v): k for k, v in WPP_LOCID.items()}
    years = list(range(1950, 2101, 5))
    ages = [f"{a}–{a + 4}" for a in range(0, 100, 5)] + ["100+"]
    age_csv = [f"{a}-{a + 4}" for a in range(0, 100, 5)] + ["100+"]
    rows = load_csv_gz("wpp2024", "WPP2024_PopulationByAge5GroupSex_Medium.csv.gz",
                       lambda r: r["LocID"] in ids and r["Variant"] == "Medium" and int(r["Time"]) % 5 == 0)
    pyr = {k: {"m": [None] * (len(years) * len(ages)), "f": [None] * (len(years) * len(ages))} for k in WPP_LOCID}
    for r in rows:
        k, y = ids[r["LocID"]], int(r["Time"])
        if y not in years or r["AgeGrp"] not in age_csv:
            continue
        i = years.index(y) * len(ages) + age_csv.index(r["AgeGrp"])
        pyr[k]["m"][i] = round(float(r["PopMale"]) * 10)
        pyr[k]["f"][i] = round(float(r["PopFemale"]) * 10)
    for k, d in pyr.items():
        if None in d["m"] or None in d["f"]:
            sys.exit(f"korfa: hiányos adat: {k}")
    tot = {k: {} for k in WPP_LOCID}
    for r in load_csv_gz("wpp2024", "WPP2024_TotalPopulationBySex.csv.gz",
                         lambda r: r["LocID"] in ids and r["Variant"] in ("Medium", "Low", "High")):
        tot[ids[r["LocID"]]].setdefault(r["Variant"], {})[int(r["Time"])] = round(float(r["PopTotal"]))
    totals = {}
    for k, vs in tot.items():
        o = {}
        for var, key in (("Medium", "med"), ("Low", "low"), ("High", "high")):
            ys = sorted(vs.get(var, {}))
            if var != "Medium":
                ys = [y for y in ys if y >= 2024]
            o[key] = {"y0": ys[0], "v": d1([vs[var][y] for y in ys])}
        totals[k] = o
    IND = {"cbr": ("CBR", 10, "születési arány, ezrelék"), "cdr": ("CDR", 10, "halálozási arány, ezrelék"),
           "tfr": ("TFR", 100, "teljes termékenységi arány (gyermek / nő)"),
           "lex": ("LEx", 10, "születéskor várható élettartam, év"), "imr": ("IMR", 10, "csecsemőhalandóság, ezrelék"),
           "births": ("Births", 10, "élveszületések, ezer fő"), "deaths": ("Deaths", 10, "halálozások, ezer fő"),
           "mig": ("CNMR", 10, "nettó vándorlási arány, ezrelék"), "gr": ("PopGrowthRate", 100, "népességnövekedés, %/év"),
           "med": ("MedianAgePop", 10, "mediánéletkor, év")}
    ind = {k: {"y0": 1950} for k in WPP_LOCID}
    rows = load_csv_gz("wpp2024", "WPP2024_Demographic_Indicators_Medium.csv.gz",
                       lambda r: r["LocID"] in ids and r["Variant"] == "Medium" and int(r["Time"]) <= 2100)
    rows.sort(key=lambda r: int(r["Time"]))
    for key, (col, f, _n) in IND.items():
        for k in WPP_LOCID:
            raw = [r[col] for r in rows if ids[r["LocID"]] == k]
            if len(raw) != 151:
                sys.exit(f"korfa: {k} {col}: {len(raw)} év")
            if all(v.strip() == "" for v in raw):
                ind[k][key] = None          # nincs értelmezve (pl. a világ nettó vándorlása)
                continue
            ind[k][key] = d1([round(float(v) * f) for v in raw])
    data = {"unit": "ezer fő", "k": 10, "years": years, "ages": ages, "estLast": 2023,
            "locs": {k: {"n": WPP_LOCS[k][1], "en": WPP_LOCS[k][0]} for k in WPP_LOCID},
            "pyr": pyr, "tot": totals, "indMeta": {k: [v[0], v[1], v[2]] for k, v in IND.items()}, "ind": ind}
    write_js("korfa-wpp2024.js", "FOLD_KORFA",
             meta("korfa-wpp2024", "World Population Prospects 2024",
                  "United Nations, Department of Economic and Social Affairs, Population Division (2024): World Population "
                  "Prospects 2024", "CC BY 3.0 IGO – a forrás megjelölése kötelező", "https://population.un.org/wpp/",
                  m["downloaded"]),
             f"""Korfák és népesedési mutatók – ENSZ WPP 2024 (window.FOLD_KORFA)
   Helyek: {', '.join(f'{k} {v[1]}' for k, v in WPP_LOCS.items())}. Az 1950–2023 közötti érték becslés, 2024-től
   ELŐREJELZÉS (estLast = 2023). Népesség július 1-jén.
   pyr[hely].m / .f: férfiak / nők, ezer fő × 10 (k = 10), évenként (years: 1950–2100, 5 évente) a 21 korcsoport
   (ages: 0–4 … 100+): az i. év j. korcsoportja: [i × 21 + j]. Közepes változat.
   tot[hely].med / .low / .high: a teljes népesség évenként, ezer fő, {{y0, v: DELTA-kódolva}} – közepes (1950–2100),
   alsó és felső változat (2024–2100).
   ind[hely][mutató]: évenkénti mutatók 1950–2100 (y0 = 1950), DELTA-kódolva, a tárolt érték = mutató × szorzó
   (indMeta: [WPP-oszlop, szorzó, magyar név]). Közepes változat.""",
             data)


# ─────────────────────────────────────────────── fejlettség (Világbank WDI)
def build_wdi(countries110):
    m = man("worldbank")
    meta_c = load_json("worldbank", "countries.json")[1]
    econ = {c["id"]: c for c in meta_c if c["region"]["value"].strip() != "Aggregates"}
    keep = set(econ) | set(WDI_AGG)
    hu = hu_names()
    ystart, last = 1960, 0
    series = {}
    lastupd = {}
    for key, (code, _n, _u, _k) in WDI.items():
        d = load_json("worldbank", f"{code}.json")
        lastupd[key] = d[0].get("lastupdated")
        for r in d[1] or []:
            iso = r.get("countryiso3code")
            if iso in keep and r.get("value") is not None:
                y = int(r["date"])
                series.setdefault(key, {}).setdefault(iso, {})[y] = r["value"]
                last = max(last, y)
    years = last - ystart + 1
    codes = sorted(keep, key=lambda c: (c in WDI_AGG, c))
    out = {}
    for key, (code, _n, _u, k) in WDI.items():
        col = []
        for iso in codes:
            vs = series.get(key, {}).get(iso)
            if not vs:
                col.append(None)
                continue
            ys = [ystart + i for i in range(years)]
            arr = [round(vs[y] * k) if y in vs else None for y in ys]
            while arr and arr[-1] is None:
                arr.pop()
            first = next(i for i, v in enumerate(arr) if v is not None)
            enc, prev = [first], 0
            for v in arr[first:]:
                if v is None:
                    enc.append(None)
                else:
                    enc.append(v - prev)
                    prev = v
            col.append(enc)
        out[key] = col
    clist = []
    for iso in codes:
        if iso in WDI_AGG:
            clist.append({"iso": iso, "n": WDI_AGG[iso], "en": iso, "agg": 1})
            continue
        c = econ[iso]
        it = {"iso": iso, "n": hu.get(iso) or c["name"], "en": c["name"], "reg": c["region"]["id"],
              "inc": c["incomeLevel"]["id"]}
        if iso in EU27:
            it["eu"] = 1
        if iso not in countries110:
            it["map"] = 0
            if c.get("longitude"):
                it["pt"] = [round(float(c["longitude"]), 2), round(float(c["latitude"]), 2)]
        clist.append(it)
    regions = {c["region"]["id"]: c["region"]["value"].strip() for c in econ.values()}
    REG_HU = {"EAS": "Kelet-Ázsia és a csendes-óceáni térség", "ECS": "Európa és Közép-Ázsia",
              "LCN": "Latin-Amerika és a Karib-térség", "MEA": "Közel-Kelet és Észak-Afrika (+ Afganisztán, Pakisztán)",
              "NAC": "Észak-Amerika", "SAS": "Dél-Ázsia", "SSF": "Szubszaharai Afrika"}
    INC_HU = {"HIC": "magas jövedelmű", "UMC": "felső-közepes jövedelmű", "LMC": "alsó-közepes jövedelmű",
              "LIC": "alacsony jövedelmű", "INX": "nincs besorolva"}
    data = {"y0": ystart, "y1": last, "ind": {k: {"code": v[0], "n": v[1], "u": v[2], "k": v[3], "upd": lastupd[k]}
                                              for k, v in WDI.items()},
            "regions": {k: REG_HU.get(k, v) for k, v in regions.items()},
            "income": INC_HU, "countries": clist, "d": out}
    write_js("fejlettseg-wdi.js", "FOLD_WDI",
             meta("fejlettseg-wdi", f"World Development Indicators, API v2 (frissítve: {max(v for v in lastupd.values() if v)})",
                  "World Bank – World Development Indicators (WDI); a foglalkoztatási adatok az ILO modellbecslései",
                  "CC BY 4.0 – a forrás megjelölése kötelező", "https://data.worldbank.org/", m["downloaded"]),
             f"""Fejlettségi mutatók országonként, {ystart}–{last} – Világbank WDI (window.FOLD_WDI)
   countries[i]: iso (Világbank-kód = ISO3), n: magyar név, reg: régió, inc: jövedelmi csoport (a LETÖLTÉSKORI besorolás,
   évente változik), eu: EU-tag, map: 0 = nincs az orszagok.js 1:110m-es térképén (pt: [lon, lat] a fővárosé),
   agg: 1 = aggregátum (WLD világ, EUU Európai Unió).
   d[mutató][i]: az i. ország idősora: null (nincs adat) vagy [o, v0, d1, d2, …]: o = az első adatév indexe (év = y0 + o),
   utána DELTA-kódolt értékek; egy null érték = hiányzó év (a futó összeg nem változik). Tárolt = érték × k
   (ind[mutató].k). Megjegyzés: a GDP/fő PPP 1990-től, a foglalkoztatás 1991-től van.""",
             data)


BUILDS = ["orszagok", "megyek", "idozonak", "lemezhatarok", "rengesek", "vulkanok", "szelveny", "korfa", "wdi"]


def main(argv):
    if "--download" in argv:
        names = [a for a in argv if not a.startswith("-")] or list(DOWNLOADS)
        for n in names:
            print("letöltés:", n)
            DOWNLOADS[n]()
        return 0
    want = [a for a in argv if not a.startswith("-")] or BUILDS
    OUT.mkdir(parents=True, exist_ok=True)
    for b in want:
        if b == "orszagok":
            build_orszagok()
        elif b == "megyek":
            build_megyek()
        elif b == "idozonak":
            build_idozonak()
        elif b == "lemezhatarok":
            build_lemezhatarok()
        elif b == "rengesek":
            build_rengesek()
        elif b == "vulkanok":
            build_vulkanok()
        elif b == "szelveny":
            build_szelvenyek()
        elif b == "korfa":
            build_korfa()
        elif b == "wdi":
            build_wdi({iso3(f["properties"]) for f in ne("ne_110m_admin_0_countries")})
        else:
            sys.exit(f"ismeretlen kimenet: {b} (lehetséges: {', '.join(BUILDS)})")
    total = sum(f.stat().st_size for f in OUT.glob("*.js"))
    print(f"összesen: {total / 1024:.0f} KB ({len(list(OUT.glob('*.js')))} fájl)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
