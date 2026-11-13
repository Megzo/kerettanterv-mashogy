#!/usr/bin/env python3
"""Térképadatok a történelemleckékhez: Natural Earth (közkincs) → shared/tort/map-*.js

    python3 -I tools/build_mapdata.py --download   # letölti a forrásokat a sources/naturalearth/ alá (+ manifest.json)
    python3 -I tools/build_mapdata.py              # a letöltött GeoJSON-okból megírja a shared/tort/map-*.js fájlokat

Forrás: Natural Earth (naturalearthdata.com), a hivatalos GitHub-tükörből
(github.com/nvkelso/natural-earth-vector, geojson/). Közkincs; a „Made with Natural Earth” feltüntetése
kérés, nem kötelezettség. A letöltött fájlok megbízhatatlan bemenetek: a sources/ alatt vannak,
.gitignore-on; ezért fut a szkript -I kapcsolóval, és csak JSON-t olvas belőlük.

Kimenet (formátum: shared/tort/README.md):
  map-karpat.js        Kárpát-medence, 9–30° K, 42–51° É, 1:10m (+ európai kiegészítő folyók/tavak), q = 1000
  map-mediterran.js    Földközi-tenger + Közel-Kelet, 10° Ny – 50° K, 20–56° É, 1:50m, q = 100
  map-vilag.js         a Föld, 1:110m szárazföld + nagy tavak, q = 100
  map-orszaghatarok.js mai országhatárok (szárazföldi határvonalak), 12° Ny – 50° K, 20–60° É, 1:50m, q = 100

Lépések: kivágás a téglalapra (sokszög: Sutherland–Hodgman, vonal: Liang–Barsky), egyszerűsítés
(Douglas–Peucker, tűrés fokban), kis szigetek/tavak elhagyása, kvantálás (fok × q egész), az
azonos nevű folyószakaszok összefűzése, delta-kódolás. Csak a Python standard könyvtárát használja.
"""
import datetime
import hashlib
import json
import math
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "sources" / "naturalearth"
OUT = ROOT / "shared" / "tort"
BASE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/"
FILES = ["ne_10m_land", "ne_10m_rivers_lake_centerlines", "ne_10m_rivers_europe", "ne_10m_lakes",
         "ne_10m_lakes_europe", "ne_10m_geography_regions_polys", "ne_50m_land", "ne_50m_rivers_lake_centerlines",
         "ne_50m_lakes", "ne_50m_admin_0_boundary_lines_land", "ne_110m_land", "ne_110m_lakes"]

# ── magyar nevek (a Natural Earth névmezője → magyar). Ami nincs itt, annak a name_hu / angol neve marad.
HU = {
    "Danube": "Duna", "Donau": "Duna", "Tisa": "Tisza", "Tisza": "Tisza", "Sava": "Száva", "Drau": "Dráva",
    "Drava": "Dráva", "Mur": "Mura", "Mures": "Maros", "Olt": "Olt", "Prut": "Prut", "Dniester": "Dnyeszter",
    "Vistula": "Visztula", "Oder": "Odera", "Elbe": "Elba", "Sio": "Sió", "Soroksari Duna": "Ráckevei-Duna",
    "Ferenc Csatorna": "Ferenc-csatorna", "Inn": "Inn", "Po": "Pó", "Adige": "Adige", "Rhein": "Rajna",
    "Rhin": "Rajna", "Rhine": "Rajna", "Drina": "Drina", "Bug": "Bug", "Southern Bug": "Déli-Bug",
    "Ialomita": "Jalomica", "Evros": "Marica", "Maritsa": "Marica", "Tevere": "Tevere", "Vltava": "Moldva",
    "Warta": "Warta", "Main": "Majna", "Weser": "Weser", "Ticino": "Ticino", "Mincio": "Mincio",
    "Strymnas": "Sztruma", "Drin": "Drin", "Bojana": "Bojana", "Bratul Chillia": "Kilia-ág",
    "Bratul Sulina": "Szulina-ág", "Bratul Sfintu Gheorghe": "Szent György-ág", "Borcea": "Borcea-ág",
    "Nile": "Nílus", "Rosetta Branch": "Rosette-ág", "Damietta Branch": "Damietta-ág", "Jordan": "Jordán",
    "Al Furat": "Eufrátesz", "Firat": "Eufrátesz", "Euphrates": "Eufrátesz", "Tigris": "Tigris", "Dicle": "Tigris",
    "Shatt al Arab": "Satt el-Arab", "Dnipro": "Dnyeper", "Dnepre": "Dnyeper", "Don": "Don", "Volga": "Volga",
    "Kama": "Káma", "Daugava": "Daugava", "Rhône": "Rhône", "Ebro": "Ebro", "Tajo": "Tajo", "Tejo": "Tajo",
    "Duero": "Duero", "Seine": "Szajna", "Loire": "Loire", "Garonne": "Garonne", "Thames": "Temze",
    "Suez Canal": "Szuezi-csatorna", "Ismailiya Canal": "Iszmáilijai-csatorna", "Gharraf Canal": "Garráf-csatorna",
    "Lek": "Lek", "Nederrijn": "Alsó-Rajna", "Waal": "Waal", "Ariège": "Ariège",
    # európai kiegészítő réteg: name_hu javítások
    "Crisul Alb": "Körös", "Slana": "Sajó", "Hornád": "Hernád", "Ipel": "Ipoly", "Raab": "Rába",
}
# A Natural Earth néhány névtelen szakasza (rivernum / ne_id szerint) – csak a biztosan azonosítottak
UNNAMED = {("cl10", 330): "Tisza", ("cl10", 624): "Duna", ("eu", 1159107823): "Nyitra",
           ("eu", 1159119905): "Berettyó", ("eu", 1159120099): "Hortobágy", ("eu", 1159111147): "Küküllő"}
# 1:10m: a „Mur” vonal a torkolat (Legrád) után a Dráva alsó szakaszát is tartalmazza → ott kettévágjuk
SPLITS = {"Mura": ((16.857, 46.302), "Dráva")}
MODERN = {"Tisza-tó", "Nasszer-tó", "Kremencsuk-víztározó", "Kakhovka-víztározó", "Kujbisevi-víztározó",
          "Szuezi-csatorna", "Iszmáilijai-csatorna", "Garráf-csatorna", "Ferenc-csatorna"}
REGION_HU = {"APPENINEK": "Appenninek", "ÉSZAK-EURÓPAI-SÍKSÁG": "Észak-európai-síkság",
             "SZAHARAI-ATLASZ": "Szaharai-Atlasz", "MAGAS-ATLASZ": "Magas-Atlasz", "AHAGGAR-HEGYSÉG": "Ahaggar",
             "HIDZSÁZ-HEGYSÉG": "Hidzsáz-hegység", "ASIR-HEGYSÉG": "Aszír-hegység", "ELBURZ-HEGYSÉG": "Elburz",
             "NYUGATI SIVATAG": "Nyugati-sivatag", "KÖZÉP-OROSZ FELFÖLD": "Közép-orosz-hátság", "SZÁHIL": "Száhel",
             "Sztyepp övezete Ukrajnában": "Pontusi sztyepp", "Toros-hegység": "Taurusz-hegység",
             "Catena Costiera": "Calabriai-hegység", "Cord. Cantábrica": "Kantábriai-hegység",
             "KUH RUD-HEGYSÉG": "Kuhrud-hegység", "Plat. du Tademaït": "Tademait-fennsík",
             "Tátra": "Északnyugati-Kárpátok"}


# ─────────────────────────────────────────────── letöltés
def download():
    SRC.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()
    ua = {"User-Agent": "Mozilla/5.0 (mapdata-downloader)"}
    with urllib.request.urlopen(urllib.request.Request(BASE + "VERSION", headers=ua), timeout=60) as r:
        version = r.read().decode("utf-8", "replace").strip()[:40]
    files = []
    for f in FILES:
        url = f"{BASE}geojson/{f}.geojson"
        print("letöltés:", url)
        with urllib.request.urlopen(urllib.request.Request(url, headers=ua), timeout=300) as r:
            raw = r.read()
        (SRC / f"{f}.geojson").write_bytes(raw)
        files.append({"file": f"{f}.geojson", "url": url, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
    manifest = {"source": "Natural Earth (public domain) — https://www.naturalearthdata.com/",
                "mirror": "https://github.com/nvkelso/natural-earth-vector", "version": version,
                "downloaded": today, "licence": "public domain (credit appreciated: Made with Natural Earth)",
                "files": files}
    (SRC / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ {len(files)} fájl, Natural Earth {version} → {SRC.relative_to(ROOT)}/")


# ─────────────────────────────────────────────── geometria
def load(name):
    p = SRC / f"{name}.geojson"
    if not p.exists():
        sys.exit(f"hiányzik: {p.relative_to(ROOT)} — futtasd: python3 -I tools/build_mapdata.py --download")
    return json.loads(p.read_text(encoding="utf-8"))["features"]


def props(f):
    return {k.lower(): v for k, v in (f.get("properties") or {}).items()}


def rings_of(geom):
    t, c = geom["type"], geom["coordinates"]
    if t == "Polygon":
        return [r for r in c]
    if t == "MultiPolygon":
        return [r for poly in c for r in poly]
    return []


def lines_of(geom):
    t, c = geom["type"], geom["coordinates"]
    return [c] if t == "LineString" else (list(c) if t == "MultiLineString" else [])


def bbox_of(pts):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def overlaps(b, box):
    return not (b[2] < box[0] or b[0] > box[2] or b[3] < box[1] or b[1] > box[3])


def clip_ring(ring, box):
    """Sutherland–Hodgman: zárt sokszög vágása tengelypárhuzamos téglalapra. A vágóél mentén
    keletkező szakaszok pontosan a téglalap szélén vannak (a rajzoló ezeket kihagyhatja körvonalnál)."""
    x0, y0, x1, y1 = box
    pts = [tuple(p[:2]) for p in ring]
    if pts and pts[0] == pts[-1]:
        pts = pts[:-1]
    edges = [(lambda p: p[0] >= x0, lambda a, b: (x0, a[1] + (b[1] - a[1]) * (x0 - a[0]) / (b[0] - a[0]))),
             (lambda p: p[0] <= x1, lambda a, b: (x1, a[1] + (b[1] - a[1]) * (x1 - a[0]) / (b[0] - a[0]))),
             (lambda p: p[1] >= y0, lambda a, b: (a[0] + (b[0] - a[0]) * (y0 - a[1]) / (b[1] - a[1]), y0)),
             (lambda p: p[1] <= y1, lambda a, b: (a[0] + (b[0] - a[0]) * (y1 - a[1]) / (b[1] - a[1]), y1))]
    for inside, cut in edges:
        if not pts:
            break
        out, prev = [], pts[-1]
        for cur in pts:
            if inside(cur):
                if not inside(prev):
                    out.append(cut(prev, cur))
                out.append(cur)
            elif inside(prev):
                out.append(cut(prev, cur))
            prev = cur
        pts = out
    return pts


def clip_line(line, box):
    """Liang–Barsky szakaszonként; a téglalapon kívüli részek mentén darabokra bont."""
    x0, y0, x1, y1 = box
    runs, cur = [], []
    for a, b in zip(line, line[1:]):
        ax, ay, bx, by = a[0], a[1], b[0], b[1]
        dx, dy = bx - ax, by - ay
        t0, t1, ok = 0.0, 1.0, True
        for p, q in ((-dx, ax - x0), (dx, x1 - ax), (-dy, ay - y0), (dy, y1 - ay)):
            if p == 0:
                if q < 0:
                    ok = False; break
            else:
                t = q / p
                if p < 0:
                    if t > t1: ok = False; break
                    t0 = max(t0, t)
                else:
                    if t < t0: ok = False; break
                    t1 = min(t1, t)
        if not ok:
            if cur: runs.append(cur); cur = []
            continue
        pa, pb = (ax + t0 * dx, ay + t0 * dy), (ax + t1 * dx, ay + t1 * dy)
        if not cur:
            cur = [pa]
        elif cur[-1] != pa:
            runs.append(cur); cur = [pa]
        cur.append(pb)
        if t1 < 1:
            runs.append(cur); cur = []
    if cur:
        runs.append(cur)
    return [r for r in runs if len(r) > 1]


def dp(pts, tol):
    """Douglas–Peucker (iteratív) nyitott vonalra; a két végpont megmarad."""
    n = len(pts)
    if n < 3:
        return list(pts)
    keep = [False] * n
    keep[0] = keep[-1] = True
    stack, t2 = [(0, n - 1)], tol * tol
    while stack:
        i, j = stack.pop()
        ax, ay = pts[i]; bx, by = pts[j]
        dx, dy = bx - ax, by - ay
        L2 = dx * dx + dy * dy
        best, bi = -1.0, -1
        for k in range(i + 1, j):
            px, py = pts[k]
            if L2 == 0:
                d = (px - ax) ** 2 + (py - ay) ** 2
            else:
                t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
                d = (px - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2
            if d > best:
                best, bi = d, k
        if best > t2:
            keep[bi] = True
            stack += [(i, bi), (bi, j)]
    return [p for p, k in zip(pts, keep) if k]


def dp_ring(pts, tol):
    if len(pts) < 4:
        return pts
    far = max(range(len(pts)), key=lambda k: (pts[k][0] - pts[0][0]) ** 2 + (pts[k][1] - pts[0][1]) ** 2)
    a = dp(pts[:far + 1], tol)
    b = dp(pts[far:] + [pts[0]], tol)
    return a[:-1] + b[:-1]


def densify_edges(pts, box, step=1.0):
    """A vágókeretre eső (egyenes, egy szélességi körön / hosszúsági körön futó) éleket 1°-onként
    pontokkal töltjük ki, hogy kúpvetületben a keret íve is ívként jelenjen meg, ne húrként."""
    out, n = [], len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        out.append(a)
        same = (a[1] == b[1] and a[1] in (box[1], box[3])) or (a[0] == b[0] and a[0] in (box[0], box[2]))
        if same:
            k = int(max(abs(b[0] - a[0]), abs(b[1] - a[1])) / step)
            out += [(a[0] + (b[0] - a[0]) * j / (k + 1), a[1] + (b[1] - a[1]) * j / (k + 1)) for j in range(1, k + 1)]
    return out


def inside(pt, rings):
    x, y, c = pt[0], pt[1], False
    for r in rings:
        for (ax, ay), (bx, by) in zip(r, r[1:] + r[:1]):
            if (ay > y) != (by > y) and x < ax + (bx - ax) * (y - ay) / (by - ay):
                c = not c
    return c


def label_point(rings):
    """Címkepont a sokszög belsejében: rácspontok közül a peremtől legtávolabbi (közelítő „pole of
    inaccessibility”) – egy ív alakú hegységnél (Kárpátok) ez a hegyvonulaton van, nem a medencében."""
    big = max(rings, key=area)
    x0, y0, x1, y1 = bbox_of(big)
    k = math.cos(math.radians((y0 + y1) / 2))
    segs = [(a, b) for r in rings for a, b in zip(r, r[1:] + r[:1])]

    def edge_dist(px, py):
        best = 1e18
        for (ax, ay), (bx, by) in segs:
            ax, bx, qx = ax * k, bx * k, px * k
            dx, dy = bx - ax, by - ay
            L2 = dx * dx + dy * dy or 1e-18
            t = max(0.0, min(1.0, ((qx - ax) * dx + (py - ay) * dy) / L2))
            best = min(best, (qx - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2)
        return best

    best, bp = -1, ((x0 + x1) / 2, (y0 + y1) / 2)
    N = 28
    for i in range(N + 1):
        for j in range(N + 1):
            p = (x0 + (x1 - x0) * i / N, y0 + (y1 - y0) * j / N)
            if inside(p, rings):
                d = edge_dist(*p)
                if d > best:
                    best, bp = d, p
    return [round(bp[0], 2), round(bp[1], 2)]


def area(pts):
    return abs(sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))) / 2


def quant(pts, q, ring=False):
    out = []
    for x, y in pts:
        p = (round(x * q), round(y * q))
        if not out or out[-1] != p:
            out.append(p)
    if ring and len(out) > 1 and out[0] == out[-1]:
        out.pop()
    return out


def delta(pts):
    flat, px, py = [], 0, 0
    for i, (x, y) in enumerate(pts):
        flat += [x, y] if i == 0 else [x - px, y - py]
        px, py = x, y
    return flat


def polys(geoms, box, tol, q, min_area):
    out = []
    for g in geoms:
        for r in rings_of(g):
            if len(r) < 4 or not overlaps(bbox_of(r), box):
                continue
            c = clip_ring(r, box)
            if len(c) < 3 or area(c) < min_area:
                continue
            s = quant(densify_edges(dp_ring(c, tol), box), q, ring=True)
            if len(s) >= 3 and area([(x / q, y / q) for x, y in s]) >= min_area:
                out.append(s)
    return out


def merge_lines(lines, snap=0):
    """Kvantált vonaldarabok összefűzése, ahol egyik vége a másik elejére (vagy végére) esik
    (snap: ennyi kvantumon belüli végpontokat azonosnak veszünk – pl. a Danube/Donau szakaszhatár)."""
    lines = [list(l) for l in lines if len(l) > 1]
    if snap:
        ends = []
        for l in lines:
            for idx in (0, -1):
                p = l[idx]
                for e in ends:
                    if abs(e[0] - p[0]) <= snap and abs(e[1] - p[1]) <= snap:
                        l[idx] = e; break
                else:
                    ends.append(p)
    changed = True
    while changed:
        changed = False
        ends = {}
        for i, l in enumerate(lines):
            ends.setdefault(l[0], []).append(i)
            ends.setdefault(l[-1], []).append(i)
        used, out = set(), []
        for i, l in enumerate(lines):
            if i in used:
                continue
            used.add(i)
            cur = l
            grown = True
            while grown:
                grown = False
                for j in ends.get(cur[-1], []):
                    if j not in used:
                        m = lines[j]
                        cur = cur + (m[1:] if m[0] == cur[-1] else m[::-1][1:])
                        used.add(j); grown = changed = True; break
                if grown:
                    continue
                for j in ends.get(cur[0], []):
                    if j not in used:
                        m = lines[j]
                        cur = (m[:-1] if m[-1] == cur[0] else m[::-1][:-1]) + cur
                        used.add(j); grown = changed = True; break
            out.append(cur)
        lines = out
    return lines


def split_line(line, at):
    """A vonal kettévágása az 'at' ponthoz legközelebbi csúcsnál → (eleje, vége)."""
    k = min(range(len(line)), key=lambda i: (line[i][0] - at[0]) ** 2 + (line[i][1] - at[1]) ** 2)
    return line[:k + 1], line[k:]


# ─────────────────────────────────────────────── rétegek
def river_name(p, tag):
    raw = p.get("name")
    if raw is None:
        key = (tag, p.get("ne_id") if tag == "eu" else p.get("rivernum"))
        return UNNAMED.get(key, ""), ""
    en = p.get("name_en") or raw
    return HU.get(raw) or HU.get(en) or p.get("name_hu") or en, en


def rivers(sources, box, tol, q, max_rank=99):
    groups = {}
    for feats, tag in sources:
        for f in feats:
            if not f.get("geometry"):
                continue
            p = props(f)
            if (p.get("scalerank") or 0) > max_rank:
                continue
            n, en = river_name(p, tag)
            lc = p.get("featurecla") == "Lake Centerline"
            if lc:
                n = "\x01" + n          # külön tétel: a tavon átfutó középvonal (lc: 1)
            for line in lines_of(f["geometry"]):
                if len(line) < 2 or not overlaps(bbox_of(line), box):
                    continue
                parts = [line]
                if n in SPLITS:
                    a, b = split_line(line, SPLITS[n][0])
                    # a torkolat felőli (keletebbre végződő) rész a másik folyó
                    head, tail = (a, b) if a[0][0] < b[-1][0] else (b, a)
                    parts = []
                    for seg, nm in ((head, n), (tail, SPLITS[n][1])):
                        for c in clip_line(seg, box):
                            g = groups.setdefault(nm, {"en": en if nm == n else "", "r": 99, "p": []})
                            g["p"].append(c)
                            g["r"] = min(g["r"], int(p.get("scalerank") or 0))
                    continue
                for c in clip_line(line, box):
                    g = groups.setdefault(n if n else f"#{id(f)}", {"en": en, "r": 99, "p": []})
                    g["p"].append(c)
                    g["r"] = min(g["r"], int(p.get("scalerank") or 0))
    out = []
    for n, g in groups.items():
        lines = merge_lines([quant(dp(l, tol), q) for l in g["p"]], snap=max(1, round(0.01 * q)))
        lines = [l for l in lines if len(l) > 1]
        if not lines:
            continue
        lc = n.startswith("\x01")
        n = n.lstrip("\x01")
        item = {"n": "" if n.startswith("#") else n}
        if g["en"] and g["en"] != item["n"]:
            item["en"] = g["en"]
        item["r"] = g["r"] if g["r"] < 99 else 10
        if item["n"] in MODERN:
            item["modern"] = 1
        if lc:
            item["lc"] = 1
        item["p"] = [delta(l) for l in lines]
        out.append(item)
    out.sort(key=lambda it: (it["r"], it["n"] == "", it["n"], it.get("lc", 0)))
    return out


def lakes(sources, box, tol, q, min_area):
    out, seen = [], set()
    for feats in sources:
        for f in feats:
            if not f.get("geometry"):
                continue
            p = props(f)
            n = p.get("name_hu") or p.get("name_en") or p.get("name") or ""
            n = REGION_HU.get(n, n)
            ps = polys([f["geometry"]], box, tol, q, min_area)
            if not ps:
                continue
            key = (n, tuple(ps[0][0]))
            if key in seen:
                continue
            seen.add(key)
            item = {"n": n}
            if p.get("name_en") and p["name_en"] != n:
                item["en"] = p["name_en"]
            if p.get("featurecla") == "Reservoir" or n in MODERN:
                item["modern"] = 1
            item["p"] = [delta(r) for r in ps]
            out.append(item)
    # azonos nevű tavak (pl. a Holt-tenger két medencéje) egy tételbe
    merged = {}
    for it in out:
        if it["n"] and it["n"] in merged:
            merged[it["n"]]["p"] += it["p"]
        else:
            merged[it["n"] or f"#{len(merged)}"] = it
    return list(merged.values())


def regions(feats, box, tol, q, classes):
    """classes: {Natural Earth featurecla: legnagyobb megengedett scalerank}."""
    out = []
    for f in feats:
        if not f.get("geometry"):
            continue
        p = props(f)
        if p.get("featurecla") not in classes or (p.get("scalerank") or 0) > classes[p.get("featurecla")]:
            continue
        rs = [r for r in rings_of(f["geometry"])]
        b = bbox_of([pt for r in rs for pt in r])
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        if not (box[0] <= cx <= box[2] and box[1] <= cy <= box[3]):
            continue
        ps = polys([f["geometry"]], box, tol, q, 0)
        if not ps:
            continue
        n = p.get("name_hu") or p.get("name_en") or p.get("name")
        n = REGION_HU.get(n, n)
        item = {"n": n, "en": p.get("name_en") or p.get("name"), "t": p.get("featurecla"), "r": int(p.get("scalerank") or 0),
                "c": [round(v * q) for v in label_point([[(x / q, y / q) for x, y in r] for r in ps])],
                "p": [delta(r) for r in ps]}
        out.append(item)
    out.sort(key=lambda it: (it["r"], it["n"]))
    return out


def write_js(name, var, header, data):
    body = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    path = OUT / name
    path.write_text(f"/* {header.strip()}\n*/\nwindow.{var}=" + body + ";\n", encoding="utf-8")
    n_pts = sum(len(r) // 2 for layer in ("land",) for r in data.get(layer, []))
    print(f"✓ {name}: {path.stat().st_size / 1024:.0f} KB (szárazföld {len(data.get('land', []))} sokszög, {n_pts} pont)")


HEADER = """{title}
   Forrás: Natural Earth {scale} ({layers}), közkincs – naturalearthdata.com („Made with Natural Earth”).
   Generálta: tools/build_mapdata.py (a forrásfájlok URL-je és SHA-256-ja: sources/naturalearth/manifest.json).
   Kivágat: {ext}. Egyszerűsítés: Douglas–Peucker, {tol}° tűrés.
   KÓDOLÁS: minden koordináta egész szám = fok × q (q = {q}), [hosszúság, szélesség] párokban, keletre és
   északra pozitív. Egy vonal / gyűrű lapos tömb: [x0, y0, dx1, dy1, dx2, dy2, …] – az első pont abszolút, a
   többi az előzőhöz képesti különbség (delta). Gyűrűk: zárt, az utolsó pont nem ismétli az elsőt; kitöltés
   'evenodd' szabállyal (a lyukak külön gyűrűk). A kivágat szélére eső élek a vágásból jönnek, nem partvonalak.
   Dekódolás és vetületek: shared/tort/proj.js (TortProj.unpack). Leírás: shared/tort/README.md.
   Mezők: land: [gyűrű]; lakes: [{{n: név, en, modern?: 1, p: [gyűrű]}}]; rivers: [{{n: magyar név ('' =
   névtelen), en, r: Natural Earth rang (kisebb = fontosabb), modern?: 1 (csatorna, víztározó), lc?: 1 (a
   folyó középvonala egy tavon át – csak akkor rajzold, ha a tavat nem), p: [vonal]}}];
   regions: [{{n, en, t: típus, r, c: [x, y] címkepont, p: [gyűrű]}}]; lines: [vonal]."""


def main(argv):
    if "--download" in argv:
        download()
        return 0
    OUT.mkdir(parents=True, exist_ok=True)

    # ── Kárpát-medence, 1:10m
    box, q, tol = (9.0, 42.0, 30.0, 51.0), 1000, 0.003
    cl10, eu = load("ne_10m_rivers_lake_centerlines"), load("ne_10m_rivers_europe")
    data = {"name": "Kárpát-medence", "q": q, "bbox": [round(v * q) for v in box], "scale": "10m",
            "land": [delta(r) for r in polys([f["geometry"] for f in load("ne_10m_land")], box, tol, q, 0.004)],
            "lakes": lakes([load("ne_10m_lakes"), load("ne_10m_lakes_europe")], box, 0.0015, q, 0.0015),
            "rivers": rivers([(cl10, "cl10"), (eu, "eu")], box, tol, q),
            "regions": regions(load("ne_10m_geography_regions_polys"), box, 0.03, q,
                               {"Range/mtn": 5, "Plain": 5, "Plateau": 5, "Delta": 5, "Basin": 5, "Lowland": 5})}
    write_js("map-karpat.js", "TORT_MAP_KARPAT", HEADER.format(
        title="Kárpát-medence – térképadat a történelemleckékhez (window.TORT_MAP_KARPAT)", scale="1:10m",
        layers="land, lakes + lakes_europe, rivers_lake_centerlines + rivers_europe, geography_regions_polys",
        ext="9–30° K, 42–51° É", tol=tol, q=q), data)

    # ── Földközi-tenger és Közel-Kelet, 1:50m
    box, q, tol = (-10.0, 20.0, 50.0, 56.0), 100, 0.012
    data = {"name": "Földközi-tenger és Közel-Kelet", "q": q, "bbox": [round(v * q) for v in box], "scale": "50m",
            "land": [delta(r) for r in polys([f["geometry"] for f in load("ne_50m_land")], box, tol, q, 0.01)],
            "lakes": lakes([load("ne_50m_lakes")], box, 0.01, q, 0.003),
            "rivers": rivers([(load("ne_50m_rivers_lake_centerlines"), "cl50")], box, tol, q),
            "regions": regions(load("ne_10m_geography_regions_polys"), box, 0.12, q,
                               {"Range/mtn": 4, "Delta": 4, "Desert": 3, "Pen/cape": 3, "Geoarea": 3, "Plateau": 3,
                                "Plain": 2, "Lowland": 3})}
    write_js("map-mediterran.js", "TORT_MAP_MEDITERRAN", HEADER.format(
        title="Földközi-tenger és Közel-Kelet – térképadat a történelemleckékhez (window.TORT_MAP_MEDITERRAN)",
        scale="1:50m (tájnevek: 1:10m)", layers="land, lakes, rivers_lake_centerlines; geography_regions_polys",
        ext="10° Ny – 50° K, 20–56° É", tol=tol, q=q), data)

    # ── Világ, 1:110m
    box, q, tol = (-180.0, -90.0, 180.0, 90.0), 100, 0.05
    data = {"name": "Világ", "q": q, "bbox": [round(v * q) for v in box], "scale": "110m",
            "land": [delta(r) for r in polys([f["geometry"] for f in load("ne_110m_land")], box, tol, q, 0.3)],
            "lakes": lakes([load("ne_110m_lakes")], box, 0.08, q, 0.5)}
    write_js("map-vilag.js", "TORT_MAP_VILAG", HEADER.format(
        title="A Föld szárazföldjei – térképadat a földgömbhöz (window.TORT_MAP_VILAG)", scale="1:110m",
        layers="land, lakes", ext="az egész Föld", tol=tol, q=q), data)

    # ── mai országhatárok, 1:50m
    box, q, tol = (-12.0, 20.0, 50.0, 60.0), 100, 0.015
    lines = []
    for f in load("ne_50m_admin_0_boundary_lines_land"):
        for line in lines_of(f["geometry"]):
            for c in clip_line(line, box):
                lines.append(quant(dp(c, tol), q))
    data = {"name": "Mai országhatárok", "q": q, "bbox": [round(v * q) for v in box], "scale": "50m",
            "lines": [delta(l) for l in merge_lines(lines) if len(l) > 1]}
    write_js("map-orszaghatarok.js", "TORT_MAP_HATAROK", HEADER.format(
        title="MAI országhatárok – halvány tájékozódási réteg (window.TORT_MAP_HATAROK). Történeti határ NEM!",
        scale="1:50m", layers="admin_0_boundary_lines_land", ext="12° Ny – 50° K, 20–60° É", tol=tol, q=q), data)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
