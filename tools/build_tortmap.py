#!/usr/bin/env python3
"""Történeti határok és Európa-alaptérkép a Történelem 7–8. leckékhez → shared/tort/map-torthatar.js, map-europa.js

    python3 -I tools/build_tortmap.py --download   # a hiányzó Natural Earth fájlok letöltése (SHA-256 a manifestből)
    python3 -I tools/build_tortmap.py              # a két adatfájl újragenerálása

Bemenet (Natural Earth, közkincs; a fájlok .gitignore-on, csak a manifest.json van a repóban):
  sources/foldrajz/naturalearth/ne_10m_admin_1_states_provinces.geojson   (manifest: ugyanott)
  sources/naturalearth/ne_50m_land / _lakes / _rivers_lake_centerlines, ne_10m_rivers_lake_centerlines (manifest: ugyanott)
A letöltött fájlok megbízhatatlan bemenetek: a szkript -I kapcsolóval fut, nem a forrásmappában van, és csak JSON-t
olvas belőlük. Csak a Python standard könyvtárát használja; a geometria-segédek a tools/build_mapdata.py-ból jönnek.

MÓDSZER (map-torthatar.js, window.TORT_HATAR)
  1. Egységek: a Natural Earth 1:10m admin-1 egységei (megye, kerület, tartomány …). A Kárpát-medencében (HU, SK, RO, RS,
     HR, SI, AT, Kárpátalja) egyenként, finom tűréssel; Európában a mai országok egyesítve, és csak ott külön egység egy
     admin-1 egység (vagy azok csoportja), ahol egy történeti határ mai egységhatáron fut.
  2. Kézi vágóvonalak (CUTS, lent): ahol a történeti határ mai egységen fut át (bécsi döntések, a Duna Újvidéknél, a
     Dráva Baranyában, a német–orosz határ 1914, a lengyel korridor, a rigai határ, a Szudéta-vidék, a francia
     demarkációs vonal 1940, Berlin szektorai …). Minden vonal töréspontjai mellett a helységnevek: melyik oldalra
     került. A vonalak SAJÁT, vázlatos rekonstrukciók a döntések / szerződések szövegében megnevezett települések és
     folyók alapján (közkincs jogszabály- és szerződésszövegek, ill. a Wikipédia szócikkeiben közölt településlisták);
     atlaszokat csak egybevetésre használtunk, adatot nem vettünk át. Minden csoport „vázlatos”.
  3. Topológia: a szomszédos egységek közös határa egyetlen közös ív (arc), egyszer egyszerűsítve (Douglas–Peucker,
     a végpontok rögzítve) – ezért nincs rés vagy átfedés a varratokon, és egy csoport körvonala futás közben
     kiszámolható (a csoporton belül kétszer használt ívek kimaradnak).
  4. Ellenőrzés: minden csoport területe gömbi felszínként (km²), a közismert értékkel összevetve (qa mező, README).
     A leckék a területet és a népességet a .md `### Adatok` részéből mutatják, SOHA nem a sokszögből.
Formátum és API: shared/tort/README.md.
"""
import datetime
import hashlib
import json
import math
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_mapdata as bm  # noqa: E402  (clip_ring, dp, dp_ring, quant, delta, area, label_point, inside, rivers, lakes, polys)

NE = ROOT / "sources" / "naturalearth"
FD = ROOT / "sources" / "foldrajz" / "naturalearth"
OUT = ROOT / "shared" / "tort"
TODAY = datetime.date.today().isoformat()
NEEDED = {NE: ["ne_50m_land", "ne_50m_lakes", "ne_50m_rivers_lake_centerlines", "ne_10m_rivers_lake_centerlines"],
          FD: ["ne_10m_admin_1_states_provinces"]}
UA = {"User-Agent": "Mozilla/5.0 (mapdata-downloader)"}


# ─────────────────────────────────────────────── letöltés (a meglévő manifestek URL-je és SHA-256-ja szerint)
def download():
    for folder, names in NEEDED.items():
        man = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
        files = {f["file"]: f for f in man["files"]}
        for n in names:
            f, p = files[n + ".geojson"], folder / (n + ".geojson")
            if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == f["sha256"]:
                print("megvan:", p.relative_to(ROOT))
                continue
            print("letöltés:", f["url"])
            with urllib.request.urlopen(urllib.request.Request(f["url"], headers=UA), timeout=600) as r:
                raw = r.read()
            p.write_bytes(raw)
            h = hashlib.sha256(raw).hexdigest()
            if h != f["sha256"]:
                sys.exit(f"ELTÉRŐ SHA-256: {p.relative_to(ROOT)} ({h}) – a forrás frissült; a manifestet a "
                         f"tools/build_mapdata.py --download / build_geodata.py --download frissíti, ellenőrizd az eredményt")
            print(f"  ✓ {len(raw) / 1024:.0f} KB, SHA-256 egyezik")


def load(folder, name):
    p = folder / (name + ".geojson")
    if not p.exists():
        sys.exit(f"hiányzik: {p.relative_to(ROOT)} — futtasd: python3 -I tools/build_tortmap.py --download")
    return json.loads(p.read_text(encoding="utf-8"))["features"]


# ─────────────────────────────────────────────── egységek: Natural Earth admin-1 → egység-azonosító
R7 = lambda p: (round(p[0], 7), round(p[1], 7))  # noqa: E731
BOX = (-25.0, 30.0, 180.0, 82.0)          # az Európa-rész kivágata (a volt szovjet államok teljes egészükben)
TOL = {"karpat": 0.0016, "europa": 0.018}  # Douglas–Peucker tűrés fokban
MIN_ISLAND = {"karpat": 0.0004, "europa": 0.006}   # fok² – ennél kisebb, csak tengerparttal határos gyűrű kimarad

COUNTRIES = ("DEU POL CZE SVK HUN AUT CHE LIE FRA BEL NLD LUX ITA SMR VAT MLT SVN HRV BIH SRB KOS MNE ALB MKD GRC "
             "BGR ROU MDA UKR BLR LTU LVA EST RUS FIN ALD SWE NOR DNK FRO ISL IRL GBR IMN JEY GGY ESP PRT AND MCO GIB "
             "TUR CYP CYN ESB WSB KAB GEO ARM AZE KAZ UZB TKM KGZ TJK SYR LBN ISR PSX JOR IRQ IRN SAU KWT EGY LBY TUN DZA MAR").split()
KARPAT_CC = {"HUN", "SVK", "ROU", "SRB", "HRV", "SVN", "AUT"}
A2 = {"KOS": "XK", "CYN": "CY", "ESB": "CY", "WSB": "CY", "KAB": "KZ", "PSX": "PS", "ALD": "FI", "FRO": "DK", "IMN": "GB", "JEY": "GB", "GGY": "GB"}
MD_LEFT = {"Camenca", "Grigoriopol", "Stîngă Nistrului", "Transnistria"}   # Dnyeszteren túli (bal parti) egységek
HU_CITY = {"Sopron": "Győr-Moson-Sopron", "Győr": "Győr-Moson-Sopron", "Szeged": "Csongrád-Csanád",
           "Hódmezővásárhely": "Csongrád-Csanád", "Salgótarján": "Nógrád", "Szolnok": "Jász-Nagykun-Szolnok",
           "Érd": "Pest", "Eger": "Heves", "Miskolc": "Borsod-Abaúj-Zemplén", "Dunaújváros": "Fejér",
           "Székesfehérvár": "Fejér", "Kecskemét": "Bács-Kiskun", "Tatabánya": "Komárom-Esztergom", "Szombathely": "Vas",
           "Zalaegerszeg": "Zala", "Nagykanizsa": "Zala", "Veszprém": "Veszprém", "Kaposvár": "Somogy", "Pécs": "Baranya",
           "Szekszárd": "Tolna", "Békéscsaba": "Békés", "Debrecen": "Hajdú-Bihar", "Nyíregyháza": "Szabolcs-Szatmár-Bereg"}

# az egyesített / külön kezelt egységek magyar neve
NAMES = {
    "FR": "Franciaország", "FR-AL": "Elzász-Lotaringia (Bas-Rhin, Haut-Rhin, Moselle)", "FR-COR": "Korzika",
    "IT": "Olaszország", "IT-TAA": "Trentino és Dél-Tirol", "IT-JUL": "Görz és Trieszt (Gorizia, Trieste)",
    "GR": "Görögország", "GR-A": "Kelet-Makedónia és Thrákia", "GR-DOD": "Dodekanészosz",
    "BG": "Bulgária", "BG-DO": "Dél-Dobrudzsa (Dobrics, Szilisztra)", "TR": "Törökország",
    "TR-KARS": "Kars, Ardahan, Artvin, Iğdır", "TR-HAT": "Hatay (Alexandrette)", "LT": "Litvánia",
    "LT-KL": "Klaipėda (Memel-vidék)", "LT-VL": "Vilnius megye", "BY": "Belarusz (Homel, Mahiljov, Minszk város)",
    "UA": "Ukrajna (keleti és középső területek)", "UA-KR": "Krím (Szevasztopollal)", "MD": "Moldova (a Dnyeszteren innen)",
    "MD-TR": "Dnyeszteren túli terület", "RU": "Oroszország", "RU-KGD": "Kalinyingrádi terület", "DK": "Dánia",
    "GB": "Nagy-Britannia", "GB-NIR": "Észak-Írország", "NO": "Norvégia", "FI": "Finnország", "ES": "Spanyolország",
    "PT": "Portugália", "NL": "Hollandia", "SI": "Szlovénia (Stájerország, Krajna, Karintia része)",
    "SI-PM": "Muravidék (Prekmurje)", "SI-LIT": "Szlovén Tengermellék (Goriška, Obalno-kraška, Notranjska)",
    "SI-LJ": "Közép- és Délkelet-Szlovénia (Ljubljana)", "ME": "Montenegró", "ME-BOKA": "Kotori-öböl (Herceg Novi, Kotor, Tivat, Budva)",
    "XK": "Koszovó", "XK-W": "Nyugat-Koszovó (Peć, Đakovica)", "XK-MIT": "Észak-Koszovó (Kosovska Mitrovica)",
    "MK": "Észak-Macedónia", "MK-W": "Nyugat-Macedónia (Polog, Délnyugat)", "CY": "Ciprus", "PS": "Palesztin területek",
    "IL": "Izrael", "CH": "Svájc", "LI": "Liechtenstein", "BE": "Belgium", "LU": "Luxemburg", "SE": "Svédország",
    "IS": "Izland", "IE": "Írország", "EE": "Észtország", "LV": "Lettország", "GE": "Grúzia", "AM": "Örményország",
    "AZ": "Azerbajdzsán", "KZ": "Kazahsztán", "UZ": "Üzbegisztán", "TM": "Türkmenisztán", "KG": "Kirgizisztán",
    "TJ": "Tádzsikisztán", "AL": "Albánia", "BA": "Bosznia-Hercegovina", "AD": "Andorra", "MC": "Monaco",
    "SM": "San Marino", "VA": "Vatikán", "MT": "Málta", "GI": "Gibraltár", "SY": "Szíria", "LB": "Libanon",
    "JO": "Jordánia", "IQ": "Irak", "IR": "Irán", "SA": "Szaúd-Arábia", "KW": "Kuvait", "EG": "Egyiptom",
    "LY": "Líbia", "TN": "Tunézia", "DZ": "Algéria", "MA": "Marokkó",
}


def unit_of(p):
    """Natural Earth admin-1 tulajdonságok → (egység-azonosító, név) vagy None (kimarad)."""
    a3, iso, name, reg = p["adm0_a3"], p["iso_3166_2"], p["name"], p.get("region") or ""
    hu = p.get("name_hu") or name
    if iso in ("UA-43", "UA-40"):                       # a Natural Earth a Krímet orosz ellenőrzésűnek veszi
        return "UA-KR", None
    if a3 == "HUN":
        if p.get("type_en") == "Urban county":
            return "@" + HU_CITY[hu], None                 # a megyéjébe olvad (lent)
        return iso, hu
    if a3 == "HRV" and name == "Brodsko-Posavska" and hu == "Pozsega-Szlavónia":
        return "HR-11", "Pozsega-Szlavónia"                # a Natural Earth-ben hibás ISO-kód (HR-12 kétszer)
    if a3 in ("SVK", "ROU", "SRB", "HRV", "AUT", "DEU", "POL", "CZE"):
        return iso, hu
    if a3 == "SVN":
        if reg in ("Goriška", "Obalno-kraška", "Notranjsko-kraška"):
            return "SI-LIT", None
        if reg in ("Osrednjeslovenska", "Jugovzhodna Slovenija"):
            return "SI-LJ", None
        if reg == "Pomurska":
            return "?SI-POM", None                         # a Mura két partja szerint szétválogatva (lent)
        return "SI", None
    if a3 == "FRA":
        if p.get("type_en") == "Overseas department":
            return None
        return ("FR-AL" if iso in ("FR-57", "FR-67", "FR-68") else "FR-COR" if iso in ("FR-2A", "FR-2B") else "FR"), None
    if a3 == "ITA":
        return ("IT-TAA" if iso in ("IT-TN", "IT-BZ") else "IT-JUL" if iso in ("IT-GO", "IT-TS") else "IT"), None
    if a3 == "GRC":
        return ("GR-A" if iso == "GR-A" else "?GR-L" if iso == "GR-L" else "GR"), None
    if a3 == "BGR":
        return ("BG-DO" if iso in ("BG-08", "BG-19") else "BG"), None
    if a3 == "TUR":
        return ("TR-KARS" if iso in ("TR-36", "TR-75", "TR-08", "TR-76") else "TR-HAT" if iso == "TR-31" else "TR"), None
    if a3 == "LTU":
        return (iso if iso in ("LT-KL", "LT-VL", "LT-TA") else "LT"), None
    if a3 == "BLR":
        return (iso if iso in ("BY-HR", "BY-BR", "BY-MI", "BY-VI") else "BY"), (hu if iso in ("BY-HR", "BY-BR", "BY-MI", "BY-VI") else None)
    if a3 == "UKR":
        keep = ("UA-21", "UA-46", "UA-61", "UA-26", "UA-07", "UA-56", "UA-77", "UA-51")
        return (iso, hu) if iso in keep else ("UA", None)
    if a3 == "MDA":
        return ("MD-TR" if name in MD_LEFT else "MD"), None
    if a3 == "RUS":
        return ("RU-KGD" if iso == "RU-KGD" else "RU"), None
    if a3 == "DNK":
        return ("DK-83", "Dél-Dánia régió (Syddanmark)") if iso == "DK-83" else ("DK", None)
    if a3 == "GBR":
        return ("GB-NIR" if p.get("geonunit") == "Northern Ireland" else "GB"), None
    if a3 == "NOR":
        return None if iso in ("NO-21", "NO-X01~") else ("NO", None)
    if a3 == "ESP":
        return None if reg == "Canary Is." else ("ES", None)
    if a3 == "PRT":
        return None if iso == "PT-20" else ("PT", None)
    if a3 == "NLD":
        return None if iso.startswith("NL-BQ") else ("NL", None)
    if a3 == "MNE":
        return ("ME-BOKA" if name in ("Herceg Novi", "Kotor", "Tivat", "Budva") else "ME"), None
    if a3 == "KOS":
        return ("XK-W" if reg in ("Peć", "Đakovica") else "XK-MIT" if reg == "Kosovska Mitrovica" else "XK"), None
    if a3 == "MKD":
        return ("MK-W" if reg in ("Polog", "Southwestern") else "MK"), None
    if a3 == "ISR":
        return "IL", None
    return A2.get(a3, p.get("iso_a2")), None


# ─────────────────────────────────────────────── kézi vágóvonalak
# Minden vonal [hosszúság, szélesség] töréspontok listája; a vonal két vége a vágandó egységeken KÍVÜL van.
# cut: {egység: (bal oldali darab, jobb oldali darab)} – „bal” a vonal haladási irányához képest. Ha egy egységet a vonal
# nem metsz, egészében a közelebbi oldalra kerül (a szkript kiírja). Az eredmény vázlatos: a töréspontok a megnevezett
# helységek közé esnek, a pontos határ (dűlő, patak) nem rekonstruálható.
CUTS = [
    # ── Első bécsi döntés, 1938. november 2. – nyugatról keletre; a JOBB (déli) oldal Magyarországé. Forrás: a döntő-
    # bírósági határozat és melléklete (a visszacsatolt városok listája: Komárom, Érsekújvár, Léva, Losonc, Rimaszombat,
    # Rozsnyó, Kassa, Ungvár, Munkács, Beregszász), a hu.wikipedia „Első bécsi döntés” szócikk; a vegyes bizottság 1939
    # márciusi cseréi (Alsójattó, Nagycétény, Nagyhind, Kalász ↓HU; Cseklész, Gány, Barakony ↑SK) beépítve.
    ("bd1", [(17.24, 47.97),                 # Magyarország (Rajka–Dunakiliti), innen a Dunán át
             (17.215, 48.06), (17.27, 48.12),    # Pozsonypüspöki ↑ (marad), a Csallóköz nyugati csúcsa ↓
             (17.32, 48.19),                     # Cseklész (Bernolákovo) ↑ (1939-es csere)
             (17.38, 48.25), (17.47, 48.27),     # Szenc ↓
             (17.62, 48.26), (17.75, 48.25),     # Galánta ↓, Szered (Sereď) ↑
             (17.88, 48.23), (18.0, 48.24),      # Vága ↓ (1939), Nyitra ↑
             (18.12, 48.26), (18.24, 48.28),     # Nagycétény ↓ (1939), Nyitra ↑ (alatta)
             (18.34, 48.27), (18.45, 48.26),     # Nagyhind, Kalász ↓, Verebély ↓, Aranyosmarót ↑
             (18.56, 48.27), (18.70, 48.25),     # Léva ↓, Garamszentbenedek ↑
             (18.85, 48.22), (19.0, 48.22),      # Ipolyság ↓, Korpona ↑
             (19.20, 48.27), (19.38, 48.29),     # Kékkő ↓
             (19.55, 48.38), (19.72, 48.38),     # Gács, Losonc ↓
             (19.90, 48.38), (20.05, 48.43),     # Fülek, Rimaszombat ↓, Tiszolc ↑
             (20.22, 48.50), (20.35, 48.58),     # Tornalja ↓, Nagyrőce ↑
             (20.50, 48.69), (20.68, 48.68),     # Rozsnyó ↓, Dobsina ↑
             (20.90, 48.71), (21.10, 48.72),     # Jászó, Szepsi ↓
             (21.26, 48.765), (21.40, 48.70),    # Kassa ↓ (a város északi széle), Eperjes ↑
             (21.60, 48.665), (21.80, 48.655),     # Tőketerebes ↓, Varannó ↑
             (21.95, 48.64), (22.10, 48.66),     # Nagymihály ↑, Nagykapos ↓
             (22.25, 48.66), (22.38, 48.59),     # Ungvár ↓ (a város északi széle)
             (22.52, 48.52), (22.68, 48.47),     # Szerednye ↓, Munkács ↓
             (22.78, 48.42), (22.78, 48.30),     # Szolyva ↑
             (22.78, 48.15), (22.86, 48.00), (22.95, 47.93)],  # Beregszász ↓, Nagyszőlős ↑ – vége Romániában
     {"SK-BL": ("SK-BL", "SK-BL.bd1"), "SK-TA": ("SK-TA", "SK-TA.bd1"), "SK-NI": ("SK-NI", "SK-NI.bd1"),
      "SK-BC": ("SK-BC", "SK-BC.bd1"), "SK-KI": ("SK-KI", "SK-KI.bd1"), "UA-21": ("UA-21", "UA-21.bd1")}),
    # ── A „kis háború” után, 1939. április 4.: kelet-szlovákiai sáv (Szobránc, Ulics, Sztakcsin környéke, 1 697 km²,
    # 78 település – hu.wikipedia „Magyar–szlovák kis háború”). Délről északra; a JOBB (keleti) oldal Magyarországé.
    ("sk1939", [(22.00, 48.62), (21.98, 48.72), (21.96, 48.82), (21.97, 48.90),   # Nagykapos ↑ – Szobránc ↓ – Szinna ↑
                (22.00, 48.98), (22.05, 49.05), (22.10, 49.12), (22.13, 49.22)],  # Sztakcsin ↓ – vége Lengyelországban
     {"SK-KI": ("SK-KI", "SK-KI.k39"), "SK-PV": ("SK-PV", "SK-PV.k39")}),
    # ── A pozsonyi hídfő, 1947. február 10. (párizsi béke, 1. cikk 4. pont): Horvátjárfalu, Oroszvár, Dunacsún.
    # Az osztrák határtól a Dunáig, majd a Dunán le; a JOBB (déli) oldal a hídfő.
    ("hidfo1947", [(17.04, 48.07), (17.10, 48.072), (17.14, 48.083), (17.158, 48.086), (17.18, 48.07),
                   (17.206, 48.061), (17.243, 48.041), (17.257, 48.028), (17.285, 48.024)],
     {"SK-BL": ("SK-BL", "SK-BL.hidfo")}),
    # ── 1920: Lengyelországhoz került árvai (Jabłonka, Lipnica Wielka, Chyżne, Podwilk) és szepesi (Niedzica, Łapsze,
    # Jurgów, Frydman, Kacwin) falvak – összesen 589 km² (KSH 1920). Hurok Szlovákiából Szlovákiába; a JOBB oldal a darab.
    ("arva1920", [(19.47, 49.53), (19.53, 49.585), (19.62, 49.60), (19.72, 49.585), (19.79, 49.53), (19.84, 49.45),
                  (19.835, 49.40), (19.75, 49.34)],
     {"PL-MA": ("PL-MA", "PL-MA.arva")}),
    ("szepes1920", [(20.12, 49.25), (20.10, 49.32), (20.10, 49.40), (20.13, 49.46), (20.20, 49.48), (20.28, 49.46),
                    (20.34, 49.43), (20.36, 49.37)],
     {"PL-MA": ("PL-MA", "PL-MA.szepes")}),
    # ── Második bécsi döntés, 1940. augusztus 30. – nyugatról keletre; a BAL (északi) oldal Magyarországé. Forrás: a
    # döntés melléklete (térkép) és a hu.wikipedia „Második bécsi döntés” szócikk településjegyzéke: Nagyvárad, Élesd,
    # Bánffyhunyad, Kolozsvár, Marosvásárhely, Székelykeresztúr, Székelyudvarhely, Sepsiszentgyörgy, Kovászna ↑HU;
    # Nagyszalonta, Belényes, Torda, Marosludas, Dicsőszentmárton, Segesvár, Kőhalom, Brassó ↓RO.
    ("bd2", [(21.55, 46.93),                    # Magyarország (Kötegyán–Méhkerék)
             (21.72, 46.95), (21.88, 46.98),    # Nagyszalonta ↓, Nagyvárad ↑ (déli széle)
             (22.10, 46.96), (22.30, 46.92),    # Mezőtelegd, Élesd ↑, Belényes ↓
             (22.55, 46.88), (22.80, 46.80),    # Bihar-hegység
             (23.00, 46.76), (23.25, 46.73),    # Bánffyhunyad ↑
             (23.45, 46.70), (23.62, 46.70),    # Kolozsvár ↑ (a város déli széle, Feleki-tető)
             (23.80, 46.66), (23.98, 46.62),    # Torda ↓, Kolozs ↑
             (24.15, 46.56), (24.32, 46.50),    # Marosludas ↓
             (24.45, 46.45), (24.62, 46.41),    # Marosvásárhely ↑, Dicsőszentmárton ↓
             (24.78, 46.35), (24.95, 46.27),    # Erdőszentgyörgy ↑, Segesvár ↓
             (25.10, 46.18), (25.28, 46.10),    # Székelykeresztúr ↑, Kőhalom ↓
             (25.45, 46.00), (25.60, 45.92),    # Homoród, Barót ↑
             (25.75, 45.80), (25.92, 45.76),    # Sepsiszentgyörgy ↑, Prázsmár ↓
             (26.10, 45.72), (26.25, 45.62),    # Kovászna, Zágon ↑, Bodzaforduló ↓
             (26.35, 45.45)],                   # vége az 1940 előtti román–magyar (kárpáti) határon túl
     {"RO-BH": ("RO-BH.bd2", "RO-BH"), "RO-CJ": ("RO-CJ.bd2", "RO-CJ"), "RO-MS": ("RO-MS.bd2", "RO-MS"),
      "RO-BV": ("RO-BV.bd2", "RO-BV")}),      # Szilágy, Hargita (Csík, Udvarhely), Kovászna (Háromszék): egészben észak
    # ── A Dráva Baranyában: a mai magyar–horvát határ Drávától eltérő szakaszától (Drávaszabolcs–Kásád) a Duna
    # torkolatáig a Natural Earth Dráva-vonalán. A BAL (északi) oldal a „baranyai háromszög” (Baranya vármegye része 1918-ig).
    ("drava", "DRAVA", {"HR-14": ("HR-14.bar", "HR-14")}),
    # ── A Duna Újvidéknél: a Dél-bácskai körzet Dunától délre eső része (Pétervárad, Karlóca, Beocsin) a Szerémséghez
    # (1918-ig Horvát-Szlavónország) tartozott. A Natural Earth Duna-vonalán; a JOBB (déli) oldal a szerémségi darab.
    ("duna-ujvidek", "DANUBE_NS", {"RS-06": ("RS-06", "RS-06.srem")}),
    # ── Német–orosz és német–osztrák határ 1914 (a mai Lengyelországban). A cseh határtól a Visztulán és a Przemszán
    # (Mysłowice: a „három császár sarka”) át a Prosnáig, a Gopło-tóig, a Visztuláig és a Drwęcáig. A BAL oldal német.
    ("de-ru-1914", [(18.30, 49.88), (18.45, 49.93), (18.70, 49.96), (18.90, 49.98),      # Pless ↑DE, Bielitz ↓AT
                    (19.08, 50.00), (19.16, 50.04),                                       # Przemsza-torkolat
                    (19.17, 50.14), (19.17, 50.24),                                       # Mysłowice ↑DE, Jaworzno →AT
                    (19.12, 50.33), (19.09, 50.44),                                       # Bytom/Piekary DE, Sosnowiec RU
                    (18.98, 50.53), (18.88, 50.65), (18.80, 50.78),                       # Woźniki DE, Koziegłowy RU
                    (18.68, 50.90), (18.52, 51.00),                                       # Lubliniec DE, Kłobuck RU
                    (18.40, 51.07), (18.25, 51.17), (18.12, 51.33),                       # Praszka RU, Wieruszów RU
                    (18.04, 51.52), (18.02, 51.70), (17.92, 51.85),                       # Grabów RU, Kalisz RU (nyugati széle)
                    (17.80, 52.00), (17.72, 52.15), (17.82, 52.30),                       # Pyzdry RU, Strzałkowo DE / Słupca RU
                    (17.95, 52.44), (18.15, 52.54), (18.30, 52.62),                       # Powidz, Gopło
                    (18.42, 52.75), (18.60, 52.85), (18.75, 52.93),                       # Inowrocław DE, Radziejów RU
                    (18.74, 53.02), (18.95, 53.08), (19.10, 53.13),                       # Drwęca: Toruń DE, Dobrzyń RU, Golub DE
                    (19.30, 53.20), (19.45, 53.24), (19.62, 53.24), (19.80, 53.12)],      # Brodnica DE – vége Mazóviában
     {"PL-SL": ("PL-SL.de14", "PL-SL.x"), "PL-WP": ("PL-WP.de14", "PL-WP.c"), "PL-KP": ("PL-KP.b", "PL-KP.c"),
      "PL-OP": ("PL-OP", "PL-OP.ru")}),
    # ── Osztrák–orosz határ 1914: Mysłowice-től kelet felé, Krakkótól északra, majd a Visztulán a San torkolatáig.
    # A BAL (északi) oldal orosz.
    ("at-ru-1914", [(19.14, 50.245), (19.30, 50.25), (19.45, 50.26), (19.60, 50.22),     # Sławków RU, Jaworzno AT, Olkusz RU
                    (19.80, 50.17), (19.98, 50.12),                                       # Krzeszowice AT, Michałowice (Krakkó É)
                    (20.15, 50.08), (20.30, 50.08), (20.48, 50.16), (20.73, 50.24),       # Visztula: Niepołomice AT
                    (20.90, 50.30), (21.27, 50.42), (21.55, 50.50), (21.78, 50.69),       # Połaniec, Baranów, Sandomierz RU
                    (21.90, 50.80)],
     {"PL-SL.x": ("PL-SL.c", "PL-SL.d"), "PL-MA": ("PL-MA.c", "PL-MA")}),
    # ── Német–lengyel határ 1920/22–1939 (versailles-i béke, felső-sziléziai népszavazás 1921 és a genfi döntés 1922):
    # a Balti-tengertől délre. Északról délre haladva a JOBB (nyugati) oldal német.
    ("de-pl-1922", [(17.97, 54.92), (17.95, 54.80), (17.88, 54.62), (17.80, 54.45),     # Lębork DE, Wejherowo PL
                    (17.68, 54.28), (17.62, 54.12), (17.52, 53.95), (17.43, 53.78),      # Bytów DE, Kościerzyna PL, Chojnice PL
                    (17.40, 53.60), (17.27, 53.45), (17.15, 53.30), (17.05, 53.17),      # Człuchów DE, Złotów DE, Więcbork PL
                    (16.85, 53.05), (16.60, 52.98), (16.35, 52.92), (16.08, 52.84),      # Piła DE, Czarnków PL, Noteć, Krzyż DE
                    (15.90, 52.72), (15.80, 52.58), (15.80, 52.40), (15.88, 52.22),      # Międzychód PL, Zbąszyń PL
                    (15.95, 52.05), (16.15, 51.88), (16.42, 51.76), (16.75, 51.60),      # Wschowa DE, Leszno PL, Rawicz PL
                    (17.10, 51.54), (17.45, 51.53), (17.72, 51.42), (17.88, 51.30),      # Milicz DE, Ostrzeszów PL, Syców DE
                    (17.98, 51.18), (18.20, 51.10), (18.42, 51.00),                       # Kępno PL – a régi orosz határ mentén
                    (18.52, 50.86), (18.55, 50.72), (18.62, 50.58), (18.74, 50.47),      # Olesno DE, Lubliniec PL
                    (18.84, 50.40), (18.90, 50.34), (18.86, 50.29), (18.77, 50.26),      # Tarnowskie Góry PL, Bytom DE, Chorzów PL
                    (18.72, 50.20), (18.60, 50.14), (18.44, 50.08), (18.30, 50.00),      # Gliwice DE, Rybnik PL, Racibórz DE
                    (18.22, 49.92)],
     {"PL-PM": ("PL-PM", "PL-PM.a"), "PL-WP.de14": ("PL-WP.b", "PL-WP.a"), "PL-SL.de14": ("PL-SL.b", "PL-SL.a"),
      "PL-KP.b": ("PL-KP.b", "PL-KP.de22"), "PL-OP": ("PL-OP.pl22", "PL-OP")}),
    # ── Danzig Szabad Város 1920–1939: a Gdynia–Sopot határtól Kartuzy és Tczew között a Visztuláig, a Nagy-Werderen
    # át a Nogatig (Marienburg ↓DE) és a Visztula-lagúnáig. Az óramutató szerint körbe; a BAL oldal Danzig.
    ("danzig", [(18.62, 54.47), (18.555, 54.462), (18.45, 54.42), (18.34, 54.35), (18.31, 54.26), (18.40, 54.16),
                (18.58, 54.11), (18.72, 54.11), (18.82, 54.10), (18.95, 54.06), (19.05, 54.05), (19.15, 54.10),
                (19.25, 54.16), (19.33, 54.26), (19.40, 54.42)],
     {"PL-PM": ("PL-PM.gd", "PL-PM")}),
    # ── Kelet-Poroszország délnyugati határa 1920–1939: a Nogattól a Visztula keleti partján (Marienwerder, Stuhm DE),
    # majd Deutsch Eylau DE / Lubawa PL, Neidenburg DE / Działdowo PL. A BAL oldal német.
    ("ostpr1920", [(19.06, 54.10), (19.03, 54.03), (18.95, 53.95), (18.88, 53.85), (18.86, 53.72), (18.80, 53.60),
                   (18.78, 53.48), (19.05, 53.55), (19.30, 53.59), (19.52, 53.58), (19.68, 53.55), (19.88, 53.49),
                   (20.02, 53.42), (20.16, 53.33), (20.32, 53.28), (20.46, 53.20), (20.50, 53.08)],
     {"PL-PM": ("PL-PM.op", "PL-PM"), "PL-WN": ("PL-WN", "PL-WN.b")}),
    # ── A rigai béke határa 1921–1939 (lengyel–szovjet): a Daugavától délre, Dzisna, Hlybokaje, Dokšycy PL / Polack,
    # Lepel SZ; Radoszkowicze, Rakaw, Stołpce, Nieśwież PL / Zaslaŭje, Dzjarzsinszk, Sluck SZ. Északról délre; a JOBB
    # (nyugati) oldal lengyel. Délebbre a határ nagyjából a mai breszti / homeli és rivnei / zsitomiri területhatár.
    ("riga1921", [(28.10, 56.35), (28.15, 56.05), (28.20, 55.90), (28.35, 55.70), (28.40, 55.45), (28.25, 55.20), (28.15, 54.95),
                  (28.08, 54.72), (27.85, 54.50), (27.55, 54.27), (27.35, 54.12), (27.22, 53.95), (27.10, 53.78),
                  (26.97, 53.58), (26.92, 53.30), (26.86, 53.05), (26.75, 52.80), (26.65, 52.55)],
     {"BY-MI": ("BY-MI", "BY-MI.pl"), "BY-VI": ("BY-VI", "BY-VI.pl")}),
    # ── Szudéta-vidék, 1938. október (müncheni egyezmény, a német–csehszlovák határbizottság november 20-i vonala):
    # Cseh- és Morvaország belsejében az óramutató járásával egyezően körbe; a BAL (külső) oldal német. Német: Břeclav,
    # Mikulov, Znojmo, Slavonice, Český Krumlov, Prachatice, Cheb, Karlovy Vary, Most, Litoměřice, Liberec, Trutnov,
    # Broumov, Králíky, Lanškroun, Svitavy, Šumperk, Bruntál, Opava, Nový Jičín; cseh: Moravské Budějovice, České
    # Budějovice, Klatovy, Domažlice, Plzeň, Rakovník, Louny, Mělník, Mladá Boleslav, Turnov, Náchod, Polička, Olomouc,
    # Hranice, Ostrava.
    ("sudeten", [(16.95, 48.62), (16.95, 48.80), (16.72, 48.90), (16.45, 48.93), (16.20, 48.95), (16.00, 48.97),
                 (15.75, 48.98), (15.48, 49.03), (15.25, 49.05), (15.00, 49.00), (14.85, 48.93), (14.62, 48.90),
                 (14.45, 48.92), (14.28, 48.90), (14.10, 48.96), (13.95, 49.06), (13.72, 49.14), (13.50, 49.21),
                 (13.30, 49.27), (13.10, 49.33), (12.95, 49.37), (12.78, 49.44),       # Domažlice: ki a határig
                 (12.95, 49.56), (13.05, 49.68), (13.14, 49.82), (13.25, 49.97), (13.38, 50.12), (13.55, 50.22),
                 (13.75, 50.32), (13.88, 50.45), (14.05, 50.48), (14.18, 50.45), (14.35, 50.50), (14.55, 50.53),
                 (14.85, 50.55), (15.05, 50.62), (15.30, 50.65), (15.55, 50.60), (15.75, 50.53), (15.98, 50.50),
                 (16.10, 50.47), (16.25, 50.39),                                        # Náchod: ki a határig
                 (16.30, 50.27), (16.40, 50.15), (16.48, 50.02), (16.44, 49.86), (16.38, 49.77), (16.45, 49.64),
                 (16.65, 49.65), (16.86, 49.74), (17.05, 49.72), (17.22, 49.75), (17.38, 49.70), (17.52, 49.71),
                 (17.66, 49.65), (17.85, 49.62), (17.96, 49.56), (18.10, 49.65), (18.20, 49.76), (18.27, 49.86),
                 (18.30, 49.95), (18.33, 50.05)],
     {k: (k + ".sd", k) for k in ("CZ-JM", "CZ-VY", "CZ-JC", "CZ-PL", "CZ-KA", "CZ-US", "CZ-ST", "CZ-LI", "CZ-KR",
                                  "CZ-PA", "CZ-OL", "CZ-MO", "CZ-ZL")}),
    # ── Zaolzie (Teschen-vidék csehszlovák része), 1938. október 2.: Bohumín, Karviná, Orlová, Český Těšín, Třinec,
    # Jablunkov → Lengyelország. Északról délre; a BAL (keleti) oldal lengyel.
    ("zaolzie", [(18.27, 49.97), (18.30, 49.88), (18.40, 49.80), (18.46, 49.72), (18.50, 49.62), (18.60, 49.50),
                 (18.70, 49.40)],
     {"CZ-MO": ("CZ-MO.za", "CZ-MO")}),
    # ── A francia demarkációs vonal 1940. június 22. – 1942. november 11. (compiègne-i fegyverszünet, 2. cikk):
    # a spanyol határtól (Saint-Jean-Pied-de-Port) Mont-de-Marsan, Langon, Libourne, Angoulême, Poitiers, Châtellerault,
    # Loches, Vierzon, Moulins, Chalon-sur-Saône, Dole mentén a svájci határig (Genf). A BAL (északi / nyugati) oldal
    # megszállt.
    ("demarkacio1940", [(-1.25, 42.80), (-1.25, 42.95), (-1.20, 43.15), (-0.85, 43.45), (-0.45, 43.85), (-0.25, 44.50), (-0.15, 44.90),
                        (0.15, 45.40), (0.35, 45.80), (0.60, 46.20), (0.62, 46.60), (0.80, 46.90), (1.10, 47.10),
                        (1.60, 47.20), (2.10, 47.22), (2.60, 46.95), (3.00, 46.75), (3.35, 46.58), (3.90, 46.50),
                        (4.40, 46.65), (4.85, 46.78), (5.20, 46.85), (5.45, 46.95), (5.65, 46.80), (5.85, 46.55),
                        (5.98, 46.35), (6.13, 46.22)],
     {"FR": ("FR.occ", "FR")}),
    # ── Észak-Schleswig 1864–1920 német, 1920-tól (népszavazás) dán: a Kongeå (Ribe ↑ dán) vonala. Nyugatról keletre;
    # a JOBB (déli) oldal Észak-Schleswig.
    ("kongea", [(8.0, 55.47), (8.45, 55.47), (8.70, 55.45), (8.95, 55.46), (9.15, 55.47), (9.35, 55.48), (9.52, 55.47),
                (9.60, 55.45), (9.66, 55.40)],
     {"DK-83": ("DK-83", "DK-SJ")},
     # szigetek: Als és Rømø Észak-Schleswighez, Fyn, Ærø, Langeland, Fanø, Mandø a dán oldalon
     lambda x, y: "R" if (x < 9.0 and y < 55.2) or (9.5 < x < 10.1 and y < 55.1) else "L"),
    # ── A Memel-vidék (Klaipėda-vidék) 1920–1939: a Nemunastól északra, az 1914-es német–orosz határig (Nimmersatt –
    # Laugszargen – Schmalleningken). Nyugatról keletre; a JOBB (déli) oldal a Memel-vidék.
    ("memel", [(20.95, 55.88), (21.07, 55.885), (21.22, 55.86), (21.40, 55.75), (21.55, 55.62), (21.68, 55.50),
               (21.80, 55.40), (21.95, 55.30), (22.15, 55.20), (22.30, 55.12), (22.45, 55.07), (22.50, 54.98)],
     {"LT-KL": ("LT-KL.n", "LT-KL"), "LT-TA": ("LT-TA", "LT-TA.mem")}),
    # ── Budzsák: Besszarábia Odesszai területhez tartozó része (a Dnyeszter-limántól nyugatra). A Dnyeszter mentén
    # délkelet felé; a JOBB (délnyugati) oldal a Budzsák.
    ("budzsak", [(29.80, 46.55), (29.95, 46.60), (30.12, 46.42), (30.25, 46.30), (30.35, 46.15), (30.48, 46.07), (30.60, 45.95), (30.75, 45.85)],
     {"UA-51": ("UA-51", "UA-51.bud")}),
    # ── A Meszta / Nesztosz folyó: nyugatra Kavala és Drama (1913-tól görög), keletre Nyugat-Trákia (Xanthi, Komotini,
    # Alexandrupoli; 1913–1919 bolgár). Északról délre; a BAL (keleti) oldal Nyugat-Trákia.
    ("nesztosz", [(23.95, 41.62), (24.05, 41.42), (24.30, 41.30), (24.55, 41.25), (24.72, 41.18), (24.75, 41.00),
                  (24.80, 40.86), (24.82, 40.70)],
     {"GR-A": ("GR-A.e", "GR-A.w")}),
    # ── A Saar-vidék 1920–1935 (versailles-i béke, 45–50. cikk) a mai Saarlandnál kisebb: az 1946–47-es bővítés
    # (Wadern, Losheim, Nohfelden, Freisen környéke) nélkül. Nyugatról keletre; a JOBB (déli) oldal az 1920-as terület
    # (Merzig, Tholey, St. Wendel benne).
    ("saar1920", [(6.30, 49.45), (6.45, 49.46), (6.60, 49.47), (6.72, 49.48), (6.85, 49.49), (7.00, 49.50),
                  (7.10, 49.51), (7.20, 49.51), (7.40, 49.48)],
     {"DE-SL": ("DE-SL.n", "DE-SL")}),
    # ── Berlin: a szovjet szektor határa (1961–89: a fal nyomvonala) – Pankow/Reinickendorf, Bornholmer Straße,
    # Brandenburgi kapu, Checkpoint Charlie, Oberbaumbrücke, Treptow/Neukölln. Északról délre; a JOBB oldal Nyugat-Berlin.
    ("berlin-fal", [(13.33, 52.70), (13.33, 52.64), (13.37, 52.60), (13.39, 52.555), (13.376, 52.535), (13.377, 52.516),
                    (13.392, 52.507), (13.43, 52.502), (13.45, 52.49), (13.48, 52.46), (13.52, 52.42), (13.53, 52.37)],
     {"DE-BE": ("DE-BE.O", "DE-BE.W")}),
    # Francia szektor (Reinickendorf, Wedding) északon; nyugatról keletre, a BAL oldal francia.
    ("berlin-fr", [(13.05, 52.62), (13.20, 52.585), (13.27, 52.555), (13.32, 52.54), (13.36, 52.535), (13.42, 52.54)],
     {"DE-BE.W": ("DE-BE.FR", "DE-BE.W2")}),
    # Brit szektor (Spandau, Charlottenburg, Tiergarten, Wilmersdorf) és amerikai (Zehlendorf, Steglitz, Schöneberg,
    # Tempelhof, Kreuzberg, Neukölln); nyugatról keletre, a BAL oldal brit.
    ("berlin-gb", [(13.05, 52.46), (13.18, 52.47), (13.25, 52.48), (13.31, 52.485), (13.345, 52.50), (13.37, 52.507),
                   (13.42, 52.515)],
     {"DE-BE.W2": ("DE-BE.GB", "DE-BE.US")}),
]


def river_line(feats, name, x0, x1):
    """A Natural Earth 1:10m folyóvonal x0 ≤ hosszúság ≤ x1 közötti része (a forrás sorrendjében)."""
    for f in feats:
        if (f["properties"].get("name") or "") != name:
            continue
        g = f["geometry"]
        for line in ([g["coordinates"]] if g["type"] == "LineString" else g["coordinates"]):
            pts = [tuple(p[:2]) for p in line if x0 <= p[0] <= x1]
            if len(pts) > 5:
                return pts
    sys.exit(f"nincs folyóvonal: {name}")


def river_cuts(rivers10):
    # Dráva (a Natural Earth-ben a „Mur” vonal folytatása Legrád alatt): a határ 18,283° K-nél válik el a folyótól
    drava = river_line(rivers10, "Mur", 18.29, 18.93)
    drava = [(18.290, 45.776)] + drava[:-1] + [(18.925, 45.553), (18.96, 45.556)]
    # Duna Újvidéknél: a horvát határtól (Ilok) a körzethatárig (19,986° K), mindkét vége a Szerémségben
    duna = river_line(rivers10, "Danube", 19.40, 19.97)
    duna = [(19.385, 45.19), (19.42, 45.25)] + [p for p in duna if p[0] > 19.43] + [(19.99, 45.10)]
    return {"DRAVA": drava, "DANUBE_NS": duna}


# ─────────────────────────────────────────────── geometria: vágás vonallal
def sarea(r):
    return sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(r, r[1:] + r[:1])) / 2


def seg_hit(a, b, c, d):
    """Az ab (gyűrűél) és cd (vágóvonal-szakasz) metszéspontja: (t az ab-n, u a cd-n, pont) vagy None.
    A pontot a kanonikus (rendezett) élirányból számolja, hogy a szomszéd egység ugyanazt a pontot kapja."""
    e0, e1 = (a, b) if a < b else (b, a)
    rx, ry = e1[0] - e0[0], e1[1] - e0[1]
    sx, sy = d[0] - c[0], d[1] - c[1]
    den = rx * sy - ry * sx
    if den == 0:
        return None
    qx, qy = c[0] - e0[0], c[1] - e0[1]
    t = (qx * sy - qy * sx) / den
    u = (qx * ry - qy * rx) / den
    if not (0 < t < 1 and 0 <= u <= 1):
        return None
    p = R7((e0[0] + t * rx, e0[1] + t * ry))
    if p == R7(a) or p == R7(b):
        return None
    ta = t if (a, b) == (e0, e1) else 1 - t
    return ta, u, p


def side_of(line, pt):
    best, s = 1e18, 1
    for c, d in zip(line, line[1:]):
        dx, dy = d[0] - c[0], d[1] - c[1]
        L2 = dx * dx + dy * dy
        t = max(0.0, min(1.0, ((pt[0] - c[0]) * dx + (pt[1] - c[1]) * dy) / L2))
        dist = (pt[0] - c[0] - t * dx) ** 2 + (pt[1] - c[1] - t * dy) ** 2
        if dist < best:
            best, s = dist, (1 if dx * (pt[1] - c[1]) - dy * (pt[0] - c[0]) > 0 else -1)
    return "L" if s > 0 else "R"


def path(ring, i, j):
    n = len(ring)
    out, k = [ring[i]], i
    while k != j:
        k = (k + 1) % n
        out.append(ring[k])
    return out


def cut_unit(rings, line, sidefn=None):
    """rings (külső gyűrűk + lyukak) vágása a line vonallal → ({'L': [...], 'R': [...]}, beszúrt pontok) vagy None,
    ha a vonal nem metszi. A beszúrt pontok: {(élvég1, élvég2) rendezve: [pont, …]} – a szomszéd egységekbe is be kell
    szúrni őket, hogy a közös ívek csúcsai egyezzenek."""
    hits_ring = {}          # (gyűrű, él) → [(t, p)]
    events = []             # (szakasz, u, p)
    patch = {}
    for ri, r in enumerate(rings):
        n = len(r)
        for i in range(n):
            a, b = r[i], r[(i + 1) % n]
            for j, (c, d) in enumerate(zip(line, line[1:])):
                if max(a[0], b[0]) < min(c[0], d[0]) or min(a[0], b[0]) > max(c[0], d[0]) or \
                        max(a[1], b[1]) < min(c[1], d[1]) or min(a[1], b[1]) > max(c[1], d[1]):
                    continue
                h = seg_hit(a, b, c, d)
                if h:
                    t, u, p = h
                    hits_ring.setdefault((ri, i), []).append((t, p))
                    events.append((j, u, p))
                    patch.setdefault((min(a, b), max(a, b)), []).append(p)
    if not events:
        return None, {}
    # a metszéspontok beszúrása a gyűrűkbe
    new = []
    for ri, r in enumerate(rings):
        out = []
        for i, a in enumerate(r):
            out.append(a)
            for _t, p in sorted(hits_ring.get((ri, i), [])):
                out.append(p)
        new.append(out)
    events.sort()
    outer = [r for r in new if not is_hole(r, new)]
    holes = [r for r in new if is_hole(r, new)]
    pieces = [list(r) for r in outer]
    chords = []
    for (j0, _u0, p0), (j1, _u1, p1) in zip(events, events[1:]):
        chord = [p0] + [R7(v) for v in line[j0 + 1:j1 + 1]] + [p1]
        chord = [q for k, q in enumerate(chord) if k == 0 or q != chord[k - 1]]
        mid = ((chord[0][0] + chord[1][0]) / 2, (chord[0][1] + chord[1][1]) / 2)
        if not bm.inside(mid, new):
            continue
        chords.append(chord)
        for k, pc in enumerate(pieces):
            idx = {q: m for m, q in enumerate(pc)}
            if p0 in idx and p1 in idx and bm.inside(mid, [pc]):
                ip, iq = idx[p0], idx[p1]
                inner = chord[1:-1]
                a = path(pc, ip, iq) + list(reversed(inner))
                b = path(pc, iq, ip) + inner
                pieces[k:k + 1] = [a, b]
                break
        else:
            raise RuntimeError(f"a húr nem illeszthető: {p0} → {p1}")
    res = {"L": [], "R": []}
    for pc in pieces:
        s = None
        pos = {q: m for m, q in enumerate(pc)}
        n = len(pc)
        for ch in chords:
            for q0, q1 in zip(ch, ch[1:]):
                if q0 in pos and q1 in pos:
                    if pc[(pos[q0] + 1) % n] == q1:
                        fwd = True
                    elif pc[(pos[q1] + 1) % n] == q0:
                        fwd = False
                    else:
                        continue
                    ccw = sarea(pc) > 0
                    s = "L" if fwd == ccw else "R"
                    break
            if s:
                break
        if s is None:
            cx, cy = sum(x for x, _ in pc) / len(pc), sum(y for _, y in pc) / len(pc)
            s = sidefn(cx, cy) if sidefn else side_of(line, (cx, cy))
        res[s].append(pc)
    for h in holes:
        tgt = next((s for s in "LR" for pc in res[s] if bm.inside(h[0], [pc])), side_of(line, h[0]))
        res[tgt].append(h)
    return res, patch


def is_hole(r, rings):
    """A gyűrű lyuk, ha egy másik gyűrű belsejében van (páratlan mélység)."""
    p = ((r[0][0] + r[1][0]) / 2, (r[0][1] + r[1][1]) / 2)
    depth = sum(1 for o in rings if o is not r and bm.inside(p, [o]))
    return depth % 2 == 1


def apply_patch(units, patch):
    if not patch:
        return
    for u in units.values():
        for ri, r in enumerate(u["rings"]):
            out, n, changed = [], len(r), False
            for i in range(n):
                a, b = r[i], r[(i + 1) % n]
                out.append(a)
                k = (min(a, b), max(a, b))
                if k in patch:
                    ps = sorted(set(patch[k]), key=lambda p: (p[0] - a[0]) ** 2 + (p[1] - a[1]) ** 2)
                    ps = [p for p in ps if p != a and p != b]
                    out += ps
                    changed = changed or bool(ps)
            if changed:
                u["rings"][ri] = out


# ─────────────────────────────────────────────── topológia: közös ívek
def build_arcs(units, q):
    """units: {id: {rings, set}} → (arcs: [delta-kódolt], refs: {id: [[ívindex, …], …]}).
    Ív: a gyűrű olyan maximális élsorozata, amelynek minden éle ugyanazzal a szomszéd gyűrűvel (vagy senkivel) közös."""
    rings = []                          # (egység, gyűrű pontjai)
    for uid, u in units.items():
        for r in u["rings"]:
            r = [p for k, p in enumerate(r) if p != r[k - 1]]
            if len(r) >= 3:
                rings.append((uid, r))
    owner = {}
    for ri, (_uid, r) in enumerate(rings):
        for a, b in zip(r, r[1:] + r[:1]):
            owner[(a, b)] = ri
    arcs, akey, refs, tols = [], {}, {}, []
    nbr_miss = 0
    for ri, (uid, r) in enumerate(rings):
        n = len(r)
        nb = [owner.get((r[(i + 1) % n], r[i]), -1) for i in range(n)]
        nbr_miss += sum(1 for x in nb if x == -1)
        brk = [i for i in range(n) if nb[i] != nb[i - 1]]
        tol = 0.002 if uid.startswith("DE-BE") else TOL[units[uid]["set"]]   # Berlin: a szektorhatár közelképhez
        ring_refs = []
        if not brk:
            m = min(range(n), key=lambda i: r[i])
            pts = r[m:] + r[:m]
            if nb[0] == -1 or sarea(r) > 0:
                seq = pts + [pts[0]]
            else:                     # a szomszéd ugyanezt a kört fordítva járja: kanonikus irány a pozitív
                seq = [pts[0]] + list(reversed(pts[1:])) + [pts[0]]
            segs = [seq] if (nb[0] == -1 or sarea(r) > 0) else [list(reversed(seq))]
            rev_flags = [False] if (nb[0] == -1 or sarea(r) > 0) else [True]
            segs_tol = [(segs[0], rev_flags[0], nb[0])]
        else:
            segs_tol = []
            for a, b in zip(brk, brk[1:] + [brk[0] + n]):
                segs_tol.append(([r[k % n] for k in range(a, b + 1)], False, nb[a % n]))
        for seq, rev, _nbx in segs_tol:
            k = tuple(seq)
            if k in akey:
                idx = akey[k]
                ring_refs.append(~idx if rev else idx)
                tols[idx] = min(tols[idx], tol)
                continue
            rk = tuple(reversed(seq))
            if rk in akey:
                idx = akey[rk]
                ring_refs.append(idx if rev else ~idx)
                tols[idx] = min(tols[idx], tol)
                continue
            akey[k] = len(arcs)
            arcs.append(seq)
            tols.append(tol)
            ring_refs.append(~(len(arcs) - 1) if rev else len(arcs) - 1)
        refs.setdefault(uid, []).append((ring_refs, r))
    # egyszerűsítés (ívenként egyszer) és kvantálás
    enc, dec = [], []
    for seq, tol in zip(arcs, tols):
        closed = seq[0] == seq[-1]
        if closed:
            s = bm.dp_ring(seq[:-1], tol)
            if len(s) < 3:
                s = seq[:-1]
            s = s + [s[0]]
        else:
            s = bm.dp(seq, tol)
        qs = []
        for x, y in s:
            p = (round(x * q), round(y * q))
            if not qs or qs[-1] != p:
                qs.append(p)
        if len(qs) == 1:
            qs.append(qs[0])
        enc.append(bm.delta(qs))
        dec.append([(x / q, y / q) for x, y in qs])
    return enc, dec, refs, nbr_miss


def ring_pts(refs, dec):
    out = []
    for ref in refs:
        a = dec[ref] if ref >= 0 else list(reversed(dec[~ref]))
        out += a if not out else a[1:]
    if len(out) > 1 and out[0] == out[-1]:
        out.pop()
    return out


def sph_area(r):
    """Előjeles gömbi terület km²-ben (Lambert-féle hengeres egyenlő területű vetület trapézszabálya, R = 6371,007 km).
    Pozitív, ha a gyűrű a hosszúság–szélesség síkon az óramutatóval ellentétesen fut."""
    R = 6371.0072
    s = 0.0
    for (l0, f0), (l1, f1) in zip(r, r[1:] + r[:1]):
        s += math.radians(l1 - l0) * (math.sin(math.radians(f0)) + math.sin(math.radians(f1))) / 2
    return -s * R * R      # pozitív: az óramutatóval ellentétes körüljárás (mint a síkbeli sarea)


# ─────────────────────────────────────────────── csoportok
def build_groups(ids):
    has = lambda u: u in ids  # noqa: E731
    pre = lambda *ps: sorted(u for u in ids if any(u == p or u.startswith(p if p.endswith("-") else p + ".") for p in ps))  # noqa: E731
    ro16 = ["RO-AB", "RO-AR", "RO-BH", "RO-BN", "RO-BV", "RO-CJ", "RO-CS", "RO-CV", "RO-HD", "RO-HR", "RO-MM", "RO-MS",
            "RO-SJ", "RO-SB", "RO-SM", "RO-TM"]
    HU = sorted(u for u in ids if u.startswith("HU-"))
    SK = pre("SK-BL", "SK-TA", "SK-NI", "SK-BC", "SK-KI", "SK-PV", "SK-ZI", "SK-TC")
    KA = pre("UA-21")
    ERD = pre(*ro16)
    VAJ = [u for u in pre("RS-01", "RS-02", "RS-03", "RS-04", "RS-05", "RS-06") if u != "RS-06.srem"]
    DELV = VAJ + ["HR-14.bar", "HR-20", "SI-PM"]
    HSZ = pre("HR-01", "HR-02", "HR-03", "HR-04", "HR-05", "HR-06", "HR-07", "HR-10", "HR-11", "HR-12", "HR-16",
              "HR-21") + ["HR-08", "HR-09", "HR-14", "RS-07", "RS-06.srem"]
    ARVA = ["PL-MA.arva", "PL-MA.szepes"]
    MO14 = HU + SK + KA + ERD + DELV + ["AT-1"] + ARVA
    BD1 = sorted(u for u in ids if u.endswith(".bd1"))
    K39 = sorted(u for u in ids if u.endswith(".k39"))
    BD2 = sorted(set(u for u in ids if u.endswith(".bd2")) |
                 {u for u in ("RO-SM", "RO-MM", "RO-SJ", "RO-BN", "RO-HR", "RO-CV") if has(u)})
    DV41 = ["RS-01", "RS-05", "RS-06", "HR-14.bar", "HR-20", "SI-PM"]
    MO20 = HU + ["SK-BL.hidfo"]
    MO41 = MO20 + BD1 + ["UA-21"] + K39 + BD2 + DV41
    g = {
        "mo1914": MO14, "hsz1914": HSZ, "mo1914hsz": MO14 + HSZ,
        "mo1920": MO20, "felvidek": [u for u in SK if u != "SK-BL.hidfo"], "karpatalja": KA, "erdely": ERD,
        "delvidek": DELV, "orvidek": ["AT-1"], "arva-szepes": ARVA,
        "trianon1920": {"HU": MO20, "CS": [u for u in SK if u != "SK-BL.hidfo"] + KA, "RO": ERD, "SHS": DELV + HSZ,
                        "AT": ["AT-1"], "PL": ARVA},
        "bd1": BD1, "karpatalja1939": ["UA-21"], "szlovakia1939": K39, "bd2": BD2, "delvidek1941": DV41,
        "mo1938": MO20 + BD1, "mo1939": MO20 + BD1 + ["UA-21"] + K39, "mo1940": MO20 + BD1 + ["UA-21"] + K39 + BD2,
        "mo1941": MO41, "mo1947": HU, "pozsonyi-hidfo1947": ["SK-BL.hidfo"],
    }
    Z = {
        "I": ["UA-21", "UA-21.bd1", "SK-KI.bd1"] + K39 + ["HU-SZ"],
        "II": BD2,
        "III": ["HU-BZ", "HU-HE", "HU-NO", "HU-KE", "HU-GS", "SK-BL.bd1", "SK-TA.bd1", "SK-NI.bd1", "SK-BC.bd1"],
        "IV": ["HU-BK", "HU-CS", "HU-BE", "HU-HB", "HU-JN", "RS-01", "RS-05", "RS-06"],
        "V": ["HU-VA", "HU-ZA", "HU-SO", "HU-BA", "HU-TO", "HU-VE", "HU-FE", "HR-14.bar", "HR-20", "SI-PM"],
        "VI": ["HU-PE"], "BP": ["HU-BU"],
    }
    Z["I-II"], Z["V-VI"] = Z["I"] + Z["II"], Z["V"] + Z["VI"]
    g["zonak1944"] = Z

    # ── Európa: építőkockák
    DE_L = pre("DE-SH", "DE-HH", "DE-NI", "DE-HB", "DE-NW", "DE-HE", "DE-RP", "DE-BW", "DE-BY", "DE-SL", "DE-MV",
               "DE-BB", "DE-ST", "DE-SN", "DE-TH", "DE-BE")
    PL_DE_ALL = ["PL-ZP", "PL-LB", "PL-DS"]              # 1914 és 1939 között is német
    PL_DE22 = PL_DE_ALL + ["PL-OP", "PL-PM.a", "PL-PM.op", "PL-WN", "PL-WP.a", "PL-SL.a", "PL-KP.de22"]
    PL_DE14 = PL_DE22 + ["PL-OP.pl22", "PL-PM", "PL-PM.gd", "PL-WN.b", "PL-WP.b", "PL-KP.b", "PL-SL.b"]
    PL_RU14 = ["PL-MZ", "PL-LD", "PL-LU", "PL-SK", "PL-PD", "PL-WP.c", "PL-KP.c", "PL-SL.c", "PL-MA.c", "PL-OP.ru"]
    PL_AT14 = ["PL-MA", "PL-SL.d", "PL-PK"]
    GAL = ["UA-46", "UA-61", "UA-26"]
    LTN = ["LT", "LT-KL.n", "LT-TA"]            # Litvánia 1914-ben orosz része (Vilnius-vidék nélkül)
    MEMEL = ["LT-KL", "LT-TA.mem"]
    VOL = ["UA-07", "UA-56"]
    BY_PL = ["BY-HR", "BY-BR", "BY-MI.pl", "BY-VI.pl"]
    BY_SU = ["BY", "BY-MI", "BY-VI"]
    CZ = pre("CZ-")
    SUD = sorted(u for u in CZ if u.endswith(".sd"))
    CZ_REST = [u for u in CZ if not u.endswith(".sd") and u != "CZ-MO.za"]
    AT = pre("AT-")
    SI_ALL = ["SI", "SI-LIT", "SI-LJ", "SI-PM"]
    HR_DALM = ["HR-13", "HR-15", "HR-17", "HR-19"]
    HR_ISL = ["HR-08.cres", "HR-08.isl", "HR-09.isl"]
    HR_ALL = pre("HR-")
    RS_ALL = pre("RS-")
    RS_C = [u for u in RS_ALL if u not in VAJ + ["RS-07", "RS-06.srem"]]   # Szerbia 1914-es (1913 előtti) magja
    RO_OLD = [u for u in pre("RO-") if u not in ERD and u != "RO-SV"]
    MDB = ["MD", "UA-51.bud"]                                             # Besszarábia (vázlatos)
    SU_C = ["RU", "UA", "UA-51", "UA-KR", "MD-TR", "GE", "AM", "AZ", "KZ", "UZ", "TM", "KG", "TJ"]
    FR_M = ["FR", "FR.occ", "FR-COR"]
    UK = ["GB", "GB-NIR", "GI"]
    ME_ALL = ["ME", "ME-BOKA"]
    XK_ALL = ["XK", "XK-W", "XK-MIT"]
    MK_ALL = ["MK", "MK-W"]
    GR_ALL = ["GR", "GR-A.w", "GR-A.e"]
    TR_ALL = ["TR", "TR-KARS", "TR-HAT"]
    MIDEAST = ["SY", "LB", "IL", "PS", "JO", "IQ", "IR", "SA", "KW", "EG", "LY", "TN", "DZ", "MA"]
    small = {k: [k] for k in ("CH", "LI", "BE", "NL", "LU", "SE", "NO", "IS", "ES", "PT", "AD", "MC", "SM", "VA", "MT",
                              "CY", "AL", "BA")}

    g["eu1914"] = dict({
        "DE": DE_L + PL_DE14 + ["FR-AL", "RU-KGD", "DK-SJ"] + MEMEL,
        "AH-AT": AT[:0] + [u for u in AT if u != "AT-1"] + CZ + PL_AT14 + GAL + ["UA-77", "RO-SV", "SI", "SI-LIT", "SI-LJ",
                 "IT-TAA", "IT-JUL", "HR-18"] + HR_DALM + HR_ISL + ["ME-BOKA"],
        "AH-HU": MO14 + HSZ, "AH-BH": ["BA"],
        "RU": SU_C + VOL + BY_PL + BY_SU + MDB + LTN + ["LT-VL", "LV", "EE", "FI"] + PL_RU14 + ["TR-KARS"],
        "RU-FI": ["FI"], "RU-PL": PL_RU14,
        "FR": FR_M, "FR-gyarmat": ["DZ", "TN", "MA"], "UK": UK, "UK-gyarmat": ["CY", "MT", "EG"], "IE": ["IE"],
        "IT": ["IT", "GR-DOD"], "IT-gyarmat": ["LY"], "DK": ["DK", "DK-83"],
        "RO": RO_OLD + ["BG-DO"], "BG": ["BG", "GR-A.e"], "SRB": RS_C + MK_ALL + ["XK", "XK-MIT"],
        "MNE": ["ME", "XK-W"], "GR": ["GR", "GR-A.w"], "OT": ["TR", "TR-HAT", "SY", "LB", "IL", "PS", "JO", "IQ"],
        "PE": ["IR"], "AR": ["SA", "KW"],
    }, **{k: v for k, v in small.items() if k not in ("CY", "MT", "BA")})
    g["eu1914"]["AH"] = g["eu1914"]["AH-AT"] + g["eu1914"]["AH-HU"] + ["BA"]
    g["de1871"] = g["eu1914"]["DE"]

    YU = SI_ALL + HR_ALL + ["BA"] + RS_ALL + ME_ALL + XK_ALL + MK_ALL
    IT20 = ["IT", "IT-TAA", "IT-JUL", "SI-LIT", "HR-18", "HR-08.cres", "GR-DOD"]
    PL21 = (["PL-PM", "PL-WN.b", "PL-WP.b", "PL-KP.b", "PL-SL.b", "PL-OP.pl22"] + PL_RU14 + PL_AT14 + ARVA + GAL + VOL +
            BY_PL + ["LT-VL"])
    DE23 = [u for u in DE_L if u != "DE-SL"] + PL_DE22 + ["RU-KGD"]
    g["eu1923"] = dict({
        "DE": DE23, "SAAR": ["DE-SL"], "DANZIG": ["PL-PM.gd"], "PL": PL21,
        "CS": CZ + [u for u in SK if u != "SK-BL.hidfo"] + KA, "AT": AT, "HU": MO20,
        "RO": pre("RO-") + MDB + ["UA-77", "BG-DO"], "YU": [u for u in YU if u not in IT20],
        "IT": IT20, "BG": ["BG"], "GR": GR_ALL, "TR": ["TR", "TR-KARS"],
        "SU": SU_C + BY_SU + [u for u in ("UA",) if 0],
        "FI": ["FI"], "EE": ["EE"], "LV": ["LV"], "LT": LTN + MEMEL, "DK": ["DK", "DK-83", "DK-SJ"],
        "FR": FR_M + ["FR-AL"], "UK": UK, "IE": ["IE", "GB-NIR"][:1], "FR-mandatum": ["SY", "LB", "TR-HAT"],
        "UK-mandatum": ["IL", "PS", "JO", "IQ"], "EG": ["EG"], "IR": ["IR"], "AR": ["SA", "KW"],
        "IT-gyarmat": ["LY"], "FR-gyarmat": ["DZ", "TN", "MA"],
    }, **{k: v for k, v in small.items() if k != "BA"})
    g["eu1923"]["UK"] = UK
    g["eu1923"]["SU"] = SU_C + BY_SU

    PROT = [u for u in CZ_REST if u != "CZ-MO.za"]
    SK39 = [u for u in SK if u not in BD1 + K39 + ["SK-BL.hidfo"]]
    g["eu1938"] = {   # építőkockák 1938–1939-re (05, 07): mindegyik egy-egy változás darabja
        "DE1937": DE23 + ["DE-SL"], "AT": AT, "SUDETEN": SUD, "ZAOLZIE": ["CZ-MO.za"], "CS-1938": PROT + SK39 + ["UA-21"] + K39,
        "PROTEKTORATUS": PROT, "SK1939": SK39, "MEMEL": MEMEL, "DANZIG": ["PL-PM.gd"], "AL": ["AL"],
        "PL": PL21, "HU-1938": MO20 + BD1, "BD1": BD1, "KARPATALJA1939": ["UA-21"],
    }
    # 1942. november (a legnagyobb kiterjedés): de jure / annektált állapot; a megszállt szovjet területet a lecke a
    # frontvonallal rajzolja (nem egységhatár)
    PL_ANNEX = ["PL-PM", "PL-PM.gd", "PL-WN.b", "PL-WP.b", "PL-WP.c", "PL-KP.b", "PL-KP.c", "PL-SL.b", "PL-SL.c",
                "PL-SL.d", "PL-OP.pl22", "PL-OP.ru", "PL-LD", "PL-PD"]
    GG = ["PL-MZ", "PL-LU", "PL-SK", "PL-MA", "PL-MA.c", "PL-PK"] + ARVA + GAL
    IT42 = IT20 + ["SI-LJ", "HR-08.isl", "HR-13", "HR-15", "HR-17"] + ME_ALL + ["AL", "XK", "XK-W", "MK-W"]
    BG42 = ["BG", "BG-DO", "GR-A.w", "GR-A.e", "MK", "RS-22", "RS-24"]
    NDH = [u for u in HR_ALL if u not in IT42 + ["HR-14.bar", "HR-20"]] + ["BA", "RS-07", "RS-06.srem"]
    SRB42 = [u for u in RS_ALL if u not in DV41 + BG42 + ["RS-07", "RS-06.srem"]] + ["XK-MIT"]
    g["eu1942"] = dict({
        "DE": DE23 + ["DE-SL"] + AT + SUD + MEMEL + PL_ANNEX + ["SI", "CZ-MO.za"],
        "DE-PROT": PROT, "DE-GG": GG, "FR-AL": ["FR-AL"], "LU": ["LU"],
        "SK": SK39, "HU": MO41, "RO": [u for u in pre("RO-") if u not in BD2] + MDB + ["UA-77"],
        "RO-TRANSZNISZTRIA": ["MD-TR", "UA-51"], "BG": BG42, "IT": IT42, "NDH": NDH, "SRB": SRB42, "GR": GR_ALL[:1],
        "FR": ["FR"], "FR-occ": ["FR.occ"], "FR-COR": ["FR-COR"], "DK": ["DK", "DK-83", "DK-SJ"],
        "SU": ["RU", "UA", "UA-KR", "GE", "AM", "AZ", "KZ", "UZ", "TM", "KG", "TJ"] + VOL + BY_PL + BY_SU +
              LTN + ["LT-VL", "LV", "EE"],
        "FI": ["FI"], "UK": UK, "IE": ["IE"], "TR": TR_ALL, "IT-gyarmat": ["LY"], "FR-gyarmat": ["DZ", "TN", "MA"],
        "EG": ["EG"], "UK-mandatum": ["IL", "PS", "JO", "IQ"], "FR-mandatum": ["SY", "LB"], "IR": ["IR"], "AR": ["SA", "KW"],
    }, **{k: v for k, v in small.items() if k not in ("AL", "BA", "LU")})
    BER_W = ["DE-BE.FR", "DE-BE.GB", "DE-BE.US"]
    NSZK = pre("DE-SH", "DE-HH", "DE-NI", "DE-HB", "DE-NW", "DE-HE", "DE-RP", "DE-BW", "DE-BY")
    NDK = pre("DE-MV", "DE-BB", "DE-ST", "DE-SN", "DE-TH")
    PL45 = pre("PL-")
    SU45 = SU_C + BY_SU + BY_PL + VOL + GAL + MDB + ["UA-77", "RU-KGD", "LT-VL", "LV", "EE"] + LTN + MEMEL + KA
    E49 = dict({
        "NSZK": NSZK, "NDK": NDK, "SAAR": pre("DE-SL"), "Berlin-Ny": BER_W, "Berlin-K": ["DE-BE.O"],
        "Berlin-US": ["DE-BE.US"], "Berlin-GB": ["DE-BE.GB"], "Berlin-FR": ["DE-BE.FR"],
        "PL": PL45, "CS": CZ + SK, "HU": HU, "AT": AT, "RO": pre("RO-"), "BG": ["BG", "BG-DO"], "YU": YU + ["HR-18"],
        "IT": ["IT", "IT-TAA", "IT-JUL"], "GR": GR_ALL + ["GR-DOD"], "TR": TR_ALL, "SU": SU45, "FI": ["FI"],
        "DK": ["DK", "DK-83", "DK-SJ"], "FR": FR_M + ["FR-AL"], "UK": UK, "IE": ["IE"],
        "EG": ["EG"], "IL": ["IL"], "PS": ["PS"], "JO": ["JO"], "IQ": ["IQ"], "SY": ["SY"], "LB": ["LB"], "IR": ["IR"],
        "AR": ["SA", "KW"], "LY": ["LY"], "TN": ["TN"], "DZ": ["DZ"], "MA": ["MA"],
    }, **{k: v for k, v in small.items() if k != "BA"})
    E49["YU"] = sorted(set(E49["YU"]))
    g["eu1949"] = E49
    E89 = {k: v for k, v in E49.items() if k != "SAAR"}
    E89["NSZK"] = NSZK + pre("DE-SL")
    g["eu1989"] = E89
    g["szu1991"] = {"RU": ["RU", "RU-KGD"], "UA": ["UA", "UA-51", "UA-51.bud", "UA-KR", "UA-77"] + GAL + VOL + KA,
                    "BY": BY_SU + BY_PL, "MD": ["MD", "MD-TR"], "LT": LTN + MEMEL + ["LT-VL"], "LV": ["LV"],
                    "EE": ["EE"], "GE": ["GE"], "AM": ["AM"], "AZ": ["AZ"], "KZ": ["KZ"], "UZ": ["UZ"], "TM": ["TM"],
                    "KG": ["KG"], "TJ": ["TJ"]}
    # ── mai országok és a Kárpát-medence mai admin-1 egységei (a vágott darabokkal)
    mai0 = {}
    for u in ids:
        mai0.setdefault(ids[u]["cc"], []).append(u)
    g["mai0"] = {k: sorted(v) for k, v in sorted(mai0.items())}
    mai1 = {}
    for u in ids:
        if ids[u]["set"] == "karpat" or u.startswith(("UA-21", "PL-MA.")):
            base = u.split(".")[0]
            if u.startswith("PL-MA."):
                continue
            mai1.setdefault(base, []).append(u)
    g["mai1"] = {k: sorted(v) for k, v in sorted(mai1.items())}
    return g


REF = {   # közismert terület (km²) – csak QA; forrás a README-ben
    "mo1914hsz": 325411, "mo1914": 282870, "hsz1914": 42541, "mo1920": 92952, "felvidek": None, "erdely": 102813,
    "trianon1920.CS": 61646, "trianon1920.RO": 102813, "trianon1920.SHS": 63370, "trianon1920.AT": 4020,
    "trianon1920.PL": 589, "delvidek": 20829, "orvidek": 4020, "arva-szepes": 589, "bd1": 11927,
    "karpatalja1939": 12061, "szlovakia1939": 1697, "bd2": 43104, "delvidek1941": 11475, "mo1941": 171753,
    "pozsonyi-hidfo1947": 65, "mo1947": 93030,
    "eu1914.DE": 540858, "eu1914.AH-AT": 300005, "eu1914.AH-BH": 51199, "eu1914.AH": 676615, "eu1914.IT": 286682,
    "eu1914.FR": 536464, "eu1914.RO": 137903, "eu1914.BG": 114013, "eu1914.SRB": 87300, "eu1914.GR": 120300,
    "eu1923.PL": 388634, "eu1923.CS": 140446, "eu1923.RO": 295049, "eu1923.YU": 248987, "eu1923.AT": 83868,
    "eu1923.DANZIG": 1966, "eu1923.SAAR": 1912, "eu1938.SUDETEN": 28680, "eu1938.ZAOLZIE": 869,
    "eu1938.PROTEKTORATUS": 49363, "eu1938.SK1939": 38055, "eu1938.MEMEL": 2848, "eu1938.DE1937": 470700,
    "eu1949.NSZK": 245300, "eu1949.NDK": 107900, "eu1949.Berlin-Ny": 480, "eu1949.Berlin-K": 403,
}

NOTES = {
    "mo1914": "vázlatos: a Magyar Királyság Horvát-Szlavónország nélkül, mai egységek uniója (HU, SK, Kárpátalja, 16 erdélyi/partiumi/bánsági megye, Vajdaság a Szerémség nélkül, baranyai háromszög, Muraköz, Muravidék, Burgenland, árvai–szepesi falvak); hiányzik Orsova környéke (ma Mehedinți) és a Duna bal parti belgrádi része; Fiume csak pont",
    "hsz1914": "vázlatos: Horvátország a dalmát megyék, az Isztria és a kvarneri szigetek nélkül, a Muraköz és a baranyai háromszög nélkül, + a Szerémség (Sremski körzet és a Dunától délre eső újvidéki rész); hiányzik Zimony (ma Belgrád része), a határ a Lika és Dalmácia között a mai megyehatár",
    "mo1914hsz": "vázlatos: mo1914 + hsz1914 (a Szent Korona országai 1914-ben, Fiume pont)",
    "mo1920": "vázlatos: a mai Magyarország + a pozsonyi hídfő három faluja (1947-ig magyar); nem követi a soproni népszavazást (1921) és az 1922–24-es kiigazításokat (a mai határ már ezek utáni)",
    "felvidek": "vázlatos: a mai Szlovákia (1920-ban Csehszlovákiához); a pozsonyi hídfő 1947-ig magyar, külön darab",
    "karpatalja": "vázlatos: a mai Kárpátaljai terület (Ruszinszkó / Podkarpatská Rus 1920–38)",
    "erdely": "vázlatos: Erdély, Partium és a Bánság romániai része = 16 mai román megye; Orsova környéke hiányzik",
    "delvidek": "vázlatos: Bácska és a Bánság nyugati része (a Vajdaság körzetei a Szerémség nélkül), baranyai háromszög (a Dráva-vonalon vágva), Muraköz (Međimurska), Muravidék (a Mura bal parti szlovén községei); Horvátország nélkül",
    "orvidek": "vázlatos: a mai Burgenland (1921: Sopron és 8 falu népszavazással Magyarországon maradt – a mai határ ezt már tartalmazza)",
    "arva-szepes": "vázlatos: kézi hurok a mai lengyel–szlovák határ mentén (Jabłonka–Podwilk, Niedzica–Łapsze)",
    "trianon1920": "vázlatos: a trianoni békeszerződés szerinti megosztás (HU, CS, RO, SHS Horvátországgal, AT, PL); Fiume (IT) pont",
    "bd1": "vázlatos: első bécsi döntés, 1938. november 2. – kézi vágóvonal a visszacsatolt / maradó városok között (a vegyes bizottság 1939-es cseréivel); a pontos falusor nem rekonstruált",
    "karpatalja1939": "vázlatos: a Kárpátaljai terület a bécsi döntés sávja nélkül (1939. március 15–18.)",
    "szlovakia1939": "vázlatos: a kelet-szlovákiai sáv (1939. április 4.; Szobránc, Sztakcsin, Ulics környéke), kézi vonal",
    "bd2": "vázlatos: második bécsi döntés, 1940. augusztus 30. – kézi vágóvonal Nagyvárad, Kolozsvár, Marosvásárhely, Sepsiszentgyörgy (HU) és Nagyszalonta, Torda, Segesvár, Brassó (RO) között; a mai megyehatárok miatt Kovászna és Hargita szinte egészben",
    "delvidek1941": "vázlatos: Bácska (a Dunáig), baranyai háromszög, Muraköz, Muravidék (1941. április); a Bánság német katonai közigazgatás alá került, nincs benne",
    "mo1941": "vázlatos: az 1941-es országterület (mo1920 + bd1 + Kárpátalja + kelet-szlovákiai sáv + bd2 + Délvidék)",
    "mo1947": "a mai Magyarország (a párizsi béke, 1947 után)",
    "pozsonyi-hidfo1947": "vázlatos: Horvátjárfalu, Oroszvár, Dunacsún – kézi vonal Ligetfalu déli szélén és a Dunán",
    "zonak1944": "a zónák fekvését mutatja, határuk vázlatos: a csendőrkerületek pontos határa nem rekonstruálható mai egységekből; mai megyékből és a fenti darabokból (Braham alapján: I. Kárpátalja és Északkelet-Magyarország [VIII. kassai csendőrkerület], II. Észak-Erdély [IX–X.], III. Észak-Magyarország Kassától a Birodalom határáig, IV. Dél-Magyarország a Dunától keletre, V. Dunántúl, VI. Budapest környéke); eltérések: Sátoraljaújhely (I.) Borsod-Abaúj-Zemplénben, Sopron (V.) Győr-Moson-Sopronban; a BP (Budapest) nem deportált zóna – történész ellenőrizze",
    "eu1914": "vázlatos: Európa 1914 (államok, gyarmatok a kivágatban); hiányzik: Eupen-Malmedy (DE), Hlučín (DE), Petsamo, Orsova; az orosz Lengyelország és Galícia határa a mai vajdaságokon belül kézi vonal; Szerbia, Montenegró, Bulgária 1913-as határa mai egységekből (Sandzsák, Koszovó, Strumica pontatlan); Kars-vidék orosz",
    "de1871": "= eu1914.DE (a Német Császárság 1871–1918), vázlatos; belső államai (Poroszország stb.) nincsenek benne",
    "eu1923": "vázlatos: Európa 1923–1937 (a rigai, trianoni, lausanne-i béke után); Vilnius-vidék = a mai Vilnius megye; Memel 1923-tól litván; Szaar 1920–35 Népszövetség; Karéliai-földszoros (finn) nincs külön",
    "eu1938": "vázlatos építőkockák 1938–1939-re: Anschluss (AT), Szudéta-vidék (kézi körvonal a cseh–morva területen belül), Zaolzie, Protektorátus, Szlovák Állam, Memel, Danzig, Albánia",
    "eu1942": "vázlatos: annektált / közigazgatási állapot 1942 novemberében; a megszállt szovjet területet a lecke a frontvonallal rajzolja; Jugoszlávia felosztása mai egységekből (az olasz Dalmácia a teljes dalmát megyékkel túlbecsült; a bolgár Szerbia-rész = Piroti és Pčinjai körzet; Nagy-Albánia = Koszovó és Nyugat-Macedónia); Görögország megszállási zónái nincsenek szétválasztva",
    "eu1949": "vázlatos: Európa 1949 (NSZK, NDK, Berlin négy szektora kézi vonallal, Szaar-protektorátus); a trieszti szabad terület (1947–54) nincs külön",
    "eu1989": "vázlatos: Európa 1989 (= eu1949, a Saar-vidék 1957-től az NSZK része)",
    "szu1991": "a Szovjetunió 15 utódállama = mai országhatárok (a Krím Ukrajnához)",
    "mai0": "MAI országok (Natural Earth admin-1 uniói; a Krím Ukrajnához); csak tájékozódáshoz, történeti határ NEM",
    "mai1": "MAI admin-1 egységek a Kárpát-medencében (megye, kerület, körzet, tartomány) a vágott darabjaikkal – a 14. lecke megyetérképéhez",
}

POINTS = {"fiume": [14.44, 45.33], "zara": [15.23, 44.12], "danzig": [18.65, 54.35], "memel": [21.13, 55.71],
          "berlin": [13.40, 52.52], "triest": [13.77, 45.65], "nagyvarad": [21.92, 47.06], "kolozsvar": [23.59, 46.77],
          "kassa": [21.26, 48.72], "ungvar": [22.29, 48.62], "ujvidek": [19.84, 45.25], "pozsony": [17.11, 48.15],
          "sopron": [16.59, 47.68]}


MERGED = set()   # a vágásnál szilánkként visszaolvasztott (nem létező) darabok – a csoportokból csendben kimaradnak


def group_area(gr, area_u):
    return sum(area_u[u] for u in gr if u in area_u)


# ─────────────────────────────────────────────── fő folyamat
def build_hatar():
    adm = load(FD, "ne_10m_admin_1_states_provinces")
    rivers10 = load(NE, "ne_10m_rivers_lake_centerlines")
    raw = {}
    mura = river_line(rivers10, "Mur", 15.6, 16.86)
    for f in adm:
        p = f["properties"]
        if p["adm0_a3"] not in COUNTRIES or not f.get("geometry"):
            continue
        res = unit_of(p)
        if res is None:
            continue
        uid, nm = res
        rs = [[R7(pt) for pt in r] for r in bm.rings_of(f["geometry"])]
        rs = [r[:-1] if r[0] == r[-1] else r for r in rs]
        if uid == "?SI-POM":
            outer = max(rs, key=lambda r: abs(sarea(r)))
            cx = sum(x for x, _ in outer) / len(outer)
            cy = sum(y for _, y in outer) / len(outer)
            uid = "SI-PM" if side_of(mura, (cx, cy)) == "L" else "SI"
        if uid.startswith("@"):
            nm_c = uid[1:]
            uid = next(q["iso_3166_2"] for q in (g["properties"] for g in adm)
                       if q["adm0_a3"] == "HUN" and (q.get("name_hu") or q["name"]) == nm_c and q.get("type_en") != "Urban county")
            nm = None
        cc = "UA" if uid == "UA-KR" else A2.get(p["adm0_a3"], p.get("iso_a2"))
        if p["adm0_a3"] == "KOS":
            cc = "XK"
        u = raw.setdefault(uid, {"parts": [], "n": None, "cc": cc})
        u["parts"].append(rs)
        if nm:
            u["n"] = nm
    units = {}
    for uid, u in raw.items():
        rings = bg_union(u["parts"]) if len(u["parts"]) > 1 else u["parts"][0]
        st = "karpat" if (u["cc"] in ("HU", "SK", "RO", "RS", "HR", "SI", "AT") or uid == "UA-21") else "europa"
        units[uid] = {"rings": rings, "n": u["n"] or NAMES.get(uid) or uid, "cc": u["cc"], "set": st}
    # gyűrűk szétválogatása: kvarneri szigetek, Pag, Dodekanészosz
    def split_rings(uid, rules, keep_main=True):
        u = units[uid]
        main = max(u["rings"], key=lambda r: abs(sarea(r)))
        for r in list(u["rings"]):
            if keep_main and r is main:
                continue
            cx = sum(x for x, _ in r) / len(r)
            cy = sum(y for _, y in r) / len(r)
            for tgt, pred in rules:
                if pred(cx, cy):
                    u["rings"].remove(r)
                    if tgt not in units:
                        units[tgt] = {"rings": [], "n": NAMES.get(tgt, tgt), "cc": u["cc"], "set": u["set"]}
                    units[tgt]["rings"].append(r)
                    break
    split_rings("HR-08", [("HR-08.cres", lambda x, y: x < 14.55), ("HR-08.isl", lambda x, y: True)])
    units["HR-08.cres"]["n"], units["HR-08.isl"]["n"] = "Cres és Lošinj", "Krk, Rab és kisebb szigetek"
    split_rings("HR-09", [("HR-09.isl", lambda x, y: True)])
    units["HR-09.isl"]["n"] = "Pag (északi része)"
    split_rings("?GR-L", [("GR-DOD", lambda x, y: x > 26.2), ("GR", lambda x, y: True)], keep_main=False)
    del units["?GR-L"]
    # kivágás
    for uid, u in units.items():
        out = []
        for r in u["rings"]:
            xs = [p[0] for p in r]
            ys = [p[1] for p in r]
            if min(xs) >= BOX[0] and max(xs) <= BOX[2] and min(ys) >= BOX[1] and max(ys) <= BOX[3]:
                out.append(r)
                continue
            c = bm.clip_ring(r, BOX)
            c = [R7(p) for p in c]
            c = [p for k, p in enumerate(c) if p != c[k - 1]]
            if len(c) >= 3 and abs(sarea(c)) > 1e-9:
                out.append(c)
        u["rings"] = out
    units = {k: v for k, v in units.items() if v["rings"]}
    # vágások
    lines = river_cuts(rivers10)
    log = []
    for cut in CUTS:
        name, line, mapping = cut[:3]
        sidefn = cut[3] if len(cut) > 3 else None
        if isinstance(line, str):
            line = lines[line]
        line = [tuple(p) for p in line]
        patch_all = {}
        for uid, (lid, rid) in mapping.items():
            if uid not in units:
                log.append(f"{name}: nincs ilyen egység: {uid}")
                continue
            u = units.pop(uid)
            if bm.inside(line[0], u["rings"]) or bm.inside(line[-1], u["rings"]):
                log.append(f"HIBA {name}: a vonal vége {uid} belsejében van")
            res, patch = cut_unit(u["rings"], line, sidefn)
            if res is None:
                big = max(u["rings"], key=lambda r: abs(sarea(r)))
                s = side_of(line, (sum(x for x, _ in big) / len(big), sum(y for _, y in big) / len(big)))
                tgt = lid if s == "L" else rid
                units[tgt] = dict(u)
                log.append(f"{name}: {uid} nem metszett → egészben {tgt}")
                MERGED.add(rid if tgt == lid else lid)
                continue
            ar = {s: sum(abs(sph_area(r)) for r in res[s]) for s in "LR"}
            for s, o in (("L", "R"), ("R", "L")):
                if res[s] and res[o] and ar[s] < 5:      # a vonal csak súrolja az egységet: szilánk → vissza
                    log.append(f"{name}: {uid} {ar[s]:.1f} km²-es szilánk visszaolvasztva")
                    res[o], res[s] = bg_union([res[o], res[s]]), []
                    MERGED.add(lid if s == "L" else rid)
            for s, tid in (("L", lid), ("R", rid)):
                if res[s]:
                    nu = dict(u, rings=res[s])
                    if tid != uid:
                        nu["n"] = u["n"] + " – " + PIECE_NAMES.get(tid, tid.split(".")[-1])
                    units[tid] = nu
            for k, v in patch.items():
                patch_all.setdefault(k, []).extend(v)
            ar = {s: sum(abs(sph_area(r)) for r in res[s]) for s in "LR"}
            log.append(f"{name}: {uid} → {lid} {ar['L']:.0f} km² | {rid} {ar['R']:.0f} km²")
        apply_patch(units, patch_all)
    for line in log:
        print("  " + line)
    # kis szigetek elhagyása (csak tengerparti gyűrű)
    edge_cnt = {}
    for u in units.values():
        for r in u["rings"]:
            for a, b in zip(r, r[1:] + r[:1]):
                edge_cnt[(a, b)] = 1
    for u in units.values():
        keep = []
        for r in u["rings"]:
            shared = any((b, a) in edge_cnt for a, b in zip(r, r[1:] + r[:1]))
            if not shared and abs(sarea(r)) < MIN_ISLAND[u["set"]] and len(u["rings"]) > 1:
                continue
            keep.append(r)
        u["rings"] = keep
    # topológia
    q = 1000
    order = sorted(units, key=lambda k: (units[k]["set"] != "karpat", k))
    units = {k: units[k] for k in order}
    enc, dec, refs, miss = build_arcs(units, q)
    out_units, area_u = [], {}
    for uid in order:
        u = units[uid]
        rr = refs.get(uid, [])
        rings_out, pts_all, tot = [], [], 0.0
        # lyuk-e: az eredeti gyűrűk egymásba ágyazása
        origs = [r for _refs, r in rr]
        for ring_refs, r in rr:
            hole = is_hole(r, origs)
            pts = ring_pts(ring_refs, dec)
            if len(pts) < 3:
                continue
            a = sph_area(pts)
            if (a > 0) == hole:        # külső: pozitív (az óramutatóval ellentétes), lyuk: negatív
                ring_refs = [~x for x in reversed(ring_refs)]
                pts = list(reversed(pts))
                a = -a
            rings_out.append(ring_refs)
            pts_all.append(pts)
            tot += a
        area_u[uid] = tot
        outer = [p for p in pts_all if sph_area(p) > 0]
        c = bm.label_point(outer if outer else pts_all) if pts_all else [0, 0]
        out_units.append({"id": uid, "n": u["n"], "cc": u["cc"], "set": u["set"], "c": [round(c[0], 2), round(c[1], 2)],
                          "r": rings_out})
    ids = {u["id"]: u for u in out_units}
    groups = build_groups(ids)
    # ellenőrzés: hiányzó egységek, duplikátumok
    qa, missing = {}, set()

    def walk(prefix, gv):
        if isinstance(gv, dict):
            for k, v in gv.items():
                walk(f"{prefix}.{k}", v)
            return
        seen = []
        for x in gv:
            if x not in ids:
                missing.add((prefix, x))
            elif x not in seen:
                seen.append(x)
        gv[:] = seen
        a = group_area(seen, area_u)
        ref = REF.get(prefix)
        qa[prefix] = [round(a), ref, round((a - ref) / ref * 100, 1) if ref else None]
    for k, v in groups.items():
        walk(k, v)
    for gk, x in sorted(missing):
        if x not in MERGED:
            print(f"  FIGYELEM: {gk}: ismeretlen egység {x}")
    # teljességi próba a teljes térképeken
    allids = set(ids)
    for full in ("eu1914", "eu1923", "eu1942", "eu1949", "eu1989"):
        cnt = {}
        for k, v in groups[full].items():
            if full == "eu1914" and k in ("AH", "RU-FI", "RU-PL"):
                continue
            if full == "eu1949" and k in ("Berlin-US", "Berlin-GB", "Berlin-FR"):
                continue
            if full == "eu1989" and k in ("Berlin-US", "Berlin-GB", "Berlin-FR"):
                continue
            for x in v:
                cnt[x] = cnt.get(x, 0) + 1
        dup = sorted(x for x, n in cnt.items() if n > 1)
        unass = sorted(allids - set(cnt))
        print(f"  {full}: {len(cnt)} egység, többször: {dup or '–'}, kimaradt: {unass or '–'}")
    print("  csoportterületek (km², hivatalos, eltérés %):")
    for k, (a, ref, d) in qa.items():
        if ref:
            print(f"    {k:28s} {a:>10,} {ref:>10,} {d:+6.1f} %".replace(",", " "))
    notes = {}
    for k, v in NOTES.items():
        a = qa.get(k)
        num = lambda n: f"{n:,}".replace(",", "\u202f")                                    # noqa: E731
        pct = lambda d: f"{d:+.1f}".replace(".", ",").replace("-", "−") + " %"            # noqa: E731
        extra = f" · a sokszög területe kb. {num(a[0])} km²" if a and not isinstance(groups.get(k), dict) else ""
        if a and a[1]:
            extra += f" (közismert: {num(a[1])} km², eltérés {pct(a[2])})"
        notes[k] = v + extra
    npts = sum(len(a) // 2 for a in enc)
    print(f"  {len(out_units)} egység, {len(enc)} ív, {npts} pont; szomszéd nélküli élek: {miss}")
    meta = {"id": "torthatar", "ver": f"Natural Earth {ne_version()}, ne_10m_admin_1_states_provinces + kézi vágás",
            "src": "Natural Earth – Admin 1 States, Provinces 1:10m (naturalearthdata.com); kézi vágóvonalak: tools/build_tortmap.py",
            "lic": "Natural Earth – közkincs („Made with Natural Earth”); kézi vágás: saját munka", "url": "https://www.naturalearthdata.com/",
            "asOf": ne_date(), "generated": TODAY, "vazlatos": True}
    data = dict(meta, q=q, bbox=[round(v * q) for v in BOX], arcs=enc, units=out_units, groups=groups,
                points=POINTS, notes=notes, qa=qa)
    head = f"""Történeti határok – vázlatos, topologikus egységek a történelemleckékhez (window.TORT_HATAR)
   Forrás: Natural Earth 1:10m admin-1 (közkincs, naturalearthdata.com – „Made with Natural Earth”), mai egységek
   uniója + kézi vágóvonalak (saját munka, töréspontok helységnevekkel: tools/build_tortmap.py, CUTS).
   MINDEN CSOPORT VÁZLATOS – a notes mező mondja meg, miben tér el. A leckék a területet és népességet a .md
   `### Adatok`-ból mutatják, nem a sokszögből (a qa mező csak ellenőrzés).
   Generálta: tools/build_tortmap.py ({TODAY}; a forrásfájlok URL-je és SHA-256-ja: sources/foldrajz/naturalearth/
   manifest.json). Egyszerűsítés: Kárpát-medence {TOL['karpat']}°, Európa {TOL['europa']}° (ívenként, a végpontok rögzítve).
   KÓDOLÁS: q = {q}; arcs[i] delta-kódolt lapos tömb [x0, y0, dx1, dy1, …] (fok × q). Egy egység gyűrűje ívindexek listája:
   i ≥ 0 → arcs[i] előre, i < 0 → arcs[~i] (= arcs[−i−1]) visszafelé; az egymást követő ívek végpontja közös (a
   következő ív első pontja elhagyandó), a gyűrű zárt. Külső gyűrű az óramutatóval ellentétes (lon/lat síkon), lyuk
   azzal egyező → kitöltés 'nonzero' szabállyal (egy csoport egy útvonalban). Körvonal: a csoporton belül egyszer
   használt ívek. Leírás és dekóder: shared/tort/README.md."""
    write(OUT / "map-torthatar.js", "TORT_HATAR", head, data)


PIECE_NAMES = {
    "SK-BL.bd1": "visszacsatolt rész 1938", "SK-TA.bd1": "visszacsatolt rész 1938", "SK-NI.bd1": "visszacsatolt rész 1938",
    "SK-BC.bd1": "visszacsatolt rész 1938", "SK-KI.bd1": "visszacsatolt rész 1938", "UA-21.bd1": "visszacsatolt rész 1938",
    "SK-KI.k39": "1939. áprilisi sáv", "SK-PV.k39": "1939. áprilisi sáv", "SK-BL.hidfo": "pozsonyi hídfő (1947-ig magyar)",
    "PL-MA.arva": "árvai falvak (1920-ig magyar)", "PL-MA.szepes": "szepesi falvak (1920-ig magyar)",
    "HR-14.bar": "baranyai háromszög", "RS-06.srem": "szerémségi rész", "PL-SL.a": "német 1939-ig", "PL-SL.b": "1922-től lengyel",
    "PL-SL.c": "1914-ig orosz", "PL-SL.d": "1918-ig osztrák", "PL-WP.a": "német 1939-ig", "PL-WP.b": "1920-tól lengyel",
    "PL-WP.c": "1914-ig orosz", "PL-KP.b": "1920-tól lengyel", "PL-KP.c": "1914-ig orosz", "PL-KP.de22": "német 1939-ig",
    "PL-PM.a": "német 1939-ig", "PL-PM.gd": "Danzig Szabad Város 1920–39", "PL-PM.op": "Kelet-Poroszország 1920–39",
    "PL-WN.b": "1920-tól lengyel", "PL-MA.c": "1914-ig orosz", "PL-OP.ru": "1914-ig orosz", "PL-OP.pl22": "1922-től lengyel",
    "BY-MI.pl": "lengyel 1921–39", "BY-VI.pl": "lengyel 1921–39", "CZ-MO.za": "Zaolzie", "FR.occ": "megszállt övezet 1940–42",
    "DK-SJ": "Észak-Schleswig", "UA-51.bud": "Budzsák", "GR-A.e": "Nyugat-Trákia", "GR-A.w": "Kavala, Drama",
    "DE-SL.n": "az 1946–47-es bővítés (Wadern, Nohfelden)", "LT-KL.n": "Kretinga, Skuodas (1914-ig orosz)",
    "LT-TA.mem": "Pagėgiai (Memel-vidék)", "DE-BE.O": "szovjet szektor", "DE-BE.W": "nyugati szektorok", "DE-BE.W2": "brit és amerikai szektor",
    "DE-BE.FR": "francia szektor", "DE-BE.GB": "brit szektor", "DE-BE.US": "amerikai szektor",
}
for _k in ("CZ-JM", "CZ-VY", "CZ-JC", "CZ-PL", "CZ-KA", "CZ-US", "CZ-ST", "CZ-LI", "CZ-KR", "CZ-PA", "CZ-OL", "CZ-MO", "CZ-ZL"):
    PIECE_NAMES[_k + ".sd"] = "Szudéta-vidék"
for _k in ("RO-BH", "RO-CJ", "RO-MS", "RO-BV", "RO-AB", "RO-AR"):
    PIECE_NAMES[_k + ".bd2"] = "visszacsatolt rész 1940"
for _k in ("RO-HR", "RO-CV", "RO-SJ"):
    PIECE_NAMES[_k + ".ro"] = "1940-ben román maradt rész"


def bg_union(parts):
    import build_geodata as bg   # noqa: E402  (edge_union)
    return [[R7(p) for p in r] for r in bg.edge_union(parts)]


def ne_version():
    m = json.loads((FD / "manifest.json").read_text(encoding="utf-8"))
    return m.get("version", "?")


def ne_date():
    m = json.loads((FD / "manifest.json").read_text(encoding="utf-8"))
    return m.get("downloaded", "?")


def write(path, var, head, data):
    head = head.replace("*/", "* /")
    body = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    path.write_text(f"/* {head.strip()}\n*/\nwindow.{var}={body};\n", encoding="utf-8")
    kb = path.stat().st_size / 1024
    print(f"✓ {path.relative_to(ROOT)}: {kb:.0f} KB")
    if kb > 400:
        print(f"  FIGYELEM: {path.name} > 400 KB")


def build_europa():
    bm.SRC = NE
    box, q, tol = (-25.0, 30.0, 60.0, 72.0), 100, 0.015
    data = {"name": "Európa", "q": q, "bbox": [round(v * q) for v in box], "scale": "50m",
            "land": [bm.delta(r) for r in bm.polys([f["geometry"] for f in bm.load("ne_50m_land")], box, tol, q, 0.01)],
            "lakes": bm.lakes([bm.load("ne_50m_lakes")], box, 0.012, q, 0.004),
            "rivers": bm.rivers([(bm.load("ne_50m_rivers_lake_centerlines"), "cl50")], box, tol, q)}
    bm.write_js("map-europa.js", "TORT_MAP_EUROPA", bm.HEADER.format(
        title="Európa – alaptérkép a történelemleckékhez, Skandináviával és a Volgáig (window.TORT_MAP_EUROPA)",
        scale="1:50m", layers="land, lakes, rivers_lake_centerlines; generálta: tools/build_tortmap.py",
        ext="25° Ny – 60° K, 30–72° É", tol=tol, q=q).replace("tools/build_mapdata.py", "tools/build_tortmap.py"), data)


def main(argv):
    if "--download" in argv:
        download()
        return 0
    build_europa()
    build_hatar()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
