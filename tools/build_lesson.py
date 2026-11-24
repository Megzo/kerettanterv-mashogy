#!/usr/bin/env python3
"""Lecke-tartalom build: <lecke>.md  →  <lecke>.content.js  (window.LESSON_CONTENT = {...})

    python3 tools/build_lesson.py leckek/fizika-7-8/01-suruseg.md
    python3 tools/build_lesson.py --all          # minden leckek/**/NN-*.md, amelynek van .html párja
    python3 tools/build_lesson.py --check …      # csak ellenőriz, nem ír
    python3 tools/build_lesson.py --selftest     # a tools/tests/ próbafájljain teszteli a buildet
    python3 tools/build_lesson.py --stale [ÉV]   # a „frissítendő” adatok, amelyek éve < ÉV − 2 (alap: idei év)

A .md formátumát a leckek/README.md írja le. A lecke HTML-je egy
<script type="application/json" id="lesson-spec"> blokkban deklarálja, mit vár:
    {"steps": 9,
     "maxWords": 45,                              # opcionális: panelszöveg-korlát lépésenként (alap: 55)
     "math": true,  /  "chem": true,              # opcionális: tantárgyi jelölés (lásd lent)
     "sources": true,                             # opcionális: minden adat mellé <!-- forrás: … --> kell
     "review": ["elsősegély"],                    # opcionális: <!-- Szakmai ellenőrzés: … --> blokk kell
     "labels": {"kulcs": 40, "másik": null},      # felirat → max. hossz (null: alapértelmezés)
     "data":   {"kulcs": {"unit": "g/cm³", "min": 0.1, "max": 25}},   # vagy csak "g/cm³"
     # magyar (opcionális): ### Idézet sorai – kulcs → szabály, vagy csoport (a kulcs eleje + szóköz: „jv 1/1” → „jv”)
     "quotes": {"jv 1/1": {"syll": 12, "cut": 6}},  "quoteSets": {"jv": {"syll": 12, "cut": 6, "lines": 24}},
     "yVowel": ["Teleky"],                        # ezekben a szavakban az y magánhangzó (alap: nem)
     "rel": {"people": ["Gergely", "Éva"], "units": ["I", "II", "III", "IV", "V"]},   # a rel adattípushoz
     "interpretive": true}                        # figyelmeztet, ha nincs „> értelmezés:” doboz és nyitott kérdés
A build hibával (1-es kilépési kód, sorszámmal) áll le, ha hiányzó vagy fölösleges kulcs van,
egy felirat túl hosszú, egy szám nem értelmezhető / rossz a mértékegysége / tartományon kívül esik.
Figyelmeztet, ha egy lépés panelszövege a korlátnál (alap: 55 szó) hosszabb.

Adattípusok (a spec "data" bejegyzésének "type" mezője; alap: "number"):
  number  „0,92 g/cm³” → {"v": 0.92, "u": "g/cm³", "d": 2}
          Szorzószó (ezer / millió / milliárd / billió = 10¹²) bármely egységgel: „25 ezer fő”,
          „480 millió”, „4,5 millió/µl” → v = 25000 …; ha a spec egysége maga „millió km”, a szó az
          egység része marad (visszafelé kompatibilis). A „trillió” szóra figyelmeztet.
          Egység közvetlenül a szám után: „70/perc” (u = "/perc"). Szög: „45° 30′” → v = 45,5 (spec "°").
          Spec-kapcsolók: "int": true (egész), "sign": true (a „+3” előjele megmarad, s = "+3"),
          "dim": "hosszúság" | "terület" | "térfogat" | "tömeg" | "idő" | "szög" (rövid nevek: hossz)
          → a családból bármely egység írható; kimenet + "base" (alapegységben) és "bu" (m, m², l,
          kg, s, °); a min/max ekkor az alapegységre vonatkozik, az "int" viszont a MEGADOTT egységben
          ellenőriz („5 cm” egész, „2,5 cm” nem).
  year    „Kr. e. 753”, „i. e. 753”, „Kr. u. 476”, „i. sz. 476”, „1241” (0. év nincs → hiba)
          → {"t": "year", "v": -753, "a": -752, "s": "Kr. e. 753"}
          v = előjeles történeti év (Kr. e. 753 = −753, 0 nincs); a = csillagászati év (Kr. e. 1 = 0,
          Kr. e. 753 = −752) – két esemény között eltelt évek: b.a − a.a (Kr. e. 776 → Kr. e. 753: 23).
          A spec min/max a v-re vonatkozik.
  date    „1848. március 15.”, „1848. március”, „Kr. e. 44. március 15.”
          → {"t": "date", "v": 1848, "ymd": [1848, 3, 15], "a": 1848.20…, "s": "1848. március 15."}
          ymd[2] null, ha csak hónap van; a = csillagászati év + az évből eltelt rész (idővonalhoz);
          a napot a hónap hosszához méri (február 29.: 1582 előtt Julián, utána Gergely-naptár).
  coord   „47,50° É, 19,04° K” (É/D, K/Ny; „47° 30′ É” is) → {"t": "coord", "lat": 47.5, "lon": 19.04,
          "s": "…"}; a spec "box": [lonmin, latmin, lonmax, latmax] ellenőrzi, hogy a térképen van-e.
  range   „50–70 ezer fő”, „25–28”, „60–100/perc” → {"t": "range", "lo": 50000, "hi": 70000, "v": 60000,
          "u": "fő", "d": 0, "s": "50–70 ezer fő"}; min/max a lo-ra és a hi-ra is.
          Spec "dim" (mint a number-nél): „2–5 mm”, „60–90 µm” – a családból bármely egység; kimenet
          + "blo", "bhi" (alapegységben), "base" (a közepük), "bu"; a min/max ekkor az alapegységre vonatkozik.
  ago     (mély idő) „3,8 milliárd éve”, „66 millió éve”, „7–6 millió éve” → {"t": "ago", "v": 3.8e9,
          ["lo", "hi"], "s"}; v = évek száma a jelen előtt; min/max években. „Kr. e.” itt hiba (→ year).
  ratio   „5474 : 1850”, „3 : 1”, „3 : 4 : 5” → {"t": "ratio", "a": 5474, "b": 1850, "v": a/b,
          ["p": [3, 4, 5]], "s": "5474 : 1850"} (a kettőspont körül nem törő szóköz: nem törik sort)
  frac    „3/4”, „2 1/3”, „−5/8”, „7/4” → {"t": "frac", "n": 1, "d": 3, "w": 2, "neg": false,
          "v": 2.333…, "red": true, "s": "2 1/3"}; spec: "maxDen", "proper", "reduced" (6/8 → hiba).
  list    „2; 3; 5; 5; 5”, „−1,2; 0,9; 5,4 °C” (pontosvessző!) → {"t": "list", "v": [...], "u", "d", "s"};
          spec: "len": 12 vagy [min, max], "int", min/max elemenként.
  series  (x → y párok) „0 °C: 13,3 · 20 °C: 31,6” → {"t": "series", "x": [...], "y": [...], "ux", "uy",
          "s"}; spec: "ux" (x egysége), "unit" (y egysége), "len", min/max (y), "xmin"/"xmax";
          x szigorúan nő.
  point   „(2; −1,5)”, „A(2; −3)” → {"t": "point", "x": 2, "y": -1.5, ["name"], "s"}; spec "box":
          [xmin, ymin, xmax, ymax], "int".
  expr    „x^2 − 4x + 3”, „2 + 3 · 4”, „3x + 4 = 19” → {"t": "expr", "s", "tok": [...], "tree": [...]}
          ellenőrzött kifejezésfa (spec "vars": ["x"] – alap; csak ezek a betűk). A fa: szám, "x",
          [op, a, b] – op: + − · : / ^ imp (2x) = < > ≤ ≥ ≠; [neg, a] [() a] [abs a] [√ a].
          Tört-literál: egész/egész (utána nem ^) egyetlen levél, erősebben köt, mint a · : (1/3 · 3/4 →
          [·, [/, 1, 3], [/, 3, 4]]; 2 : 1/4 → [:, 2, [/, 1, 4]]) – mint a MatExpr v1.1; tizedesnél
          (1,5/3) és kitevőnél (1/2^3) a / közönséges osztás marad.
          A JS a fát eval nélkül értékeli ki (shared/matek/mtext.js: MatText.evalExpr, MatQ.evalExpr).
  formula „H₂O”, „H2O”, „SO4^2-”, „Ca(OH)₂” → {"t": "formula", "s": "H₂O", "atoms": {"H": 2, "O": 1},
          "charge": 0}; spec "atoms" / "charge" (ha megadja, egyeznie kell).
  equation „CH₄ + 2 O₂ → CO₂ + 2 H₂O” (vagy ->) → {"t": "equation", "s", "lhs": [{"k", "f", "atoms",
          "charge"}], "rhs": [...]}; atom- és töltésmérleg, a nyíl kötelező.
  utc     „UTC+5:30”, „UTC−5”, „UTC” → {"t": "utc", "min": 330, "s": "UTC+5:30"}
  dataset „ENSZ WPP 2024” + spec {"id": "korfa-wpp2024"} → a shared/foldrajz/<id>.js (vagy spec "path")
          léteznie kell, a fejléc "id"-je egyezzen, és a .md szövegének évszámai (2024) a fejléc
          "src"/"ver" mezőjében is szerepeljenek (a szöveg maga a forrássor rövid neve).
          → {"t": "dataset", "id", "src", "ver", "s"}
Magyar nyelv és irodalom (szöveges adat; a „kb.”/„(2025)” jelzők itt nincsenek – a "s" a normalizált alak):
  metrum  „— ∪ ∪ | — ∪ ∪ | — ×” (- – _ = —, u ◡ ⏑ = ∪, x = ×; | versláb, || metszet) → {"t": "meter", "feet": [["—", "∪",
          "∪"], …], "n": szótagszám, "cz": [a metszet előtti verslábak száma], "s"}; spec "line": idézetkulcs → a szótagszám
          egyezzen (hiba), és hosszú magánhangzó (á é í ó ő ú ű) ne álljon ∪ helyen (figyelmeztetés); "feet": N.
  rhyme   „aabb” (x = rímtelen; rövidebb képlet versszakonként ismétlődik) + spec "quotes": csoport vagy "lines": [kulcsok]
          → {"t": "rhyme", "p": [betű soronként], "keys": [...], "s"}; figyelmeztet, ha egy rímpár sorvégi magánhangzója
          eltér (a hosszúság nem számít: o = ó).
  morph   „kert + ész (képző) + ek (jel) + nek (rag)”, „virág (tő) + cserép (tő) + ben (rag)”, „-ban/-ben (rag)” →
          {"t": "morph", "s": "kertészeknek", "parts": [{"s": "kert", "k": "tő"}, …, ["alt": ["ban", "ben"]]]};
          fajta: tő képző jel rag kötőhangzó előtag (az első elem alapból tő). Hiba: rag után jel/képző; figyelmeztet:
          jel után képző, hangrend-eltérés (kivétel: <!-- ingadozó --> a sorban).
  pron    „kútba [kúdba]” → {"t": "pron", "w": "kútba", "p": "kúdba", "s"}; szögletes zárójel nélkül hiba.
  rel     „Gergely – Éva: szerelem (I–V)” → {"t": "rel", "a", "b", "kind", ["from", "to", "fi", "ti"], "s"}; kind: barát
          ellenség család szerelem szolgál vezet; a szereplők / egységek a spec "rel" listáiból (fi, ti: index), lista
          nélkül római vagy arab szám (fi, ti: az értéke).
### Idézet blokk (bármely ## alatt): „- kulcs: verssor”, a sorban | = sormetszet (a megjelenített szövegből eltűnik;
  szó szerinti |: \\|). Előtte kötelező: <!-- idézet: <szerző>: <mű> (<év>), <hely> · szöveg: <kiadás> · szerző † <év> · közkincs -->
  (népköltészet: „gyűjtő † <év>”; jogszabály: † nélkül). Hiba, ha † + 70 ≥ az idei év. Szótagszám = a magánhangzók száma;
  eltérés (syll, cut) hiba, kivéve <!-- szótagszám: N, … --> / <!-- eltérés: … --> a sor végén (figyelmeztetés).
  Kimenet: content.quotes = {kulcs: {"s", "syl", "v": [a szótagmagok indexei s-ben], ["cut": [szótag a | előtt],
  "ci": [karakterhely]], "ref": a forrás indexe}}, content.quoteSrc = [a forrásmegjegyzések]; a JS: L.quote(k), L.quoteDat(k).
> értelmezés: … → <p class="interp"> „Egy lehetséges olvasat” fejléccel (shared/lesson.css); beleszámít a szókorlátba.
Becslésjelző minden típuson: „kb. …”, „~ …”, „≈ …”, „… (becslés)”, évszámnál „… körül” is
  → "est": true, és "s" „kb. ”-vel kezdődik ("s0": ugyanez a jelző nélkül).
Az adat éve és állapota (zárójeles utótag, vesszővel): „8,2 milliárd fő (2025, frissítendő)”,
  „(előrejelzés)”, „(modell)”, „(2030, előrejelzés)” → "yr": 2025, "upd": true, "proj": true,
  "model": true; a "s" a jelölők nélkül.
Az új típusoknál (és becslésnél, szorzószónál) a "s" a magyarul formázott alak; ezt kapja a
panelszöveg {kulcs} hivatkozása és az L.val(k). A régi, sima számok kimenete változatlan.

Jelölés a szövegben (panel, lépéscím, felirat) – a részletek a leckek/README.md-ben:
  minden leckében: `…` képletszakasz (1 szó), x^2 / 10^-3 / 2^(n+1) / Na^+ / SO4^2- (felső index),
     F_fel, x_1, H_2O (alsó index: számjegyek VAGY betűk), [[x/2]] álló tört, {1; 2; 3} halmaz
     (nem adatkulcs, mert van benne „;”), \\{ \\} \\/ \\^ \\_ \\` szó szerint.
  a `…` képletben: * → ·, - → −, <= >= != ~= → ≤ ≥ ≠ ≈, -> |-> => <=> → ↦ ⇒ ⇔, +- → ±,
     pi inf → π ∞, NN ZZ QQ RR → ℕ ℤ ℚ ℝ, √(…) / gyök(…), a latin betűk és a görög kisbetűk
     dőltek (sin, lg…, a π és a görög nagybetűk – Δ, Σ, Ω – állók). Mértékegység SZÁM UTÁN álló (ISO 80000):
     `9,81 m/s^2`, `5 cm`, `3 * 10^8 m/s`, `20 °C`; egybetűs (m, s, g…) csak szóközzel (`5m` = 5 · m);
     szám nélkül változó (`F = m * a`); "…" közti szöveg álló. A panelen a képlet szóközei nem törők
     (csak relációjel után törhet), a `képlet:` sor is egyben marad.
  "math": true – 3/4 álló tört, 2 1/3 vegyes szám, √(…) a szövegben is; a `képlet:` sor egésze
     képlet, (a) / (b) emeletes tört; figyelmeztet: 3*4, 5 - 3, 3.14, 30', (3, 2), cm2.
  "chem": true – H2O, CO2, Ca(OH)2 → alsó index; ₂ ⁺ (Unicode) → <sub>/<sup>; -> → →.
     Feliratban Unicode-ra alakít (H₂O, Na^+ → Na⁺, SO4^2- → SO₄²⁻); minden átalakítást „info:” sorban kiír.
  a # cím (sima szöveg: panel + böngészőfül) – minden leckében: `képlet`, x^2, Na^+, √(…) → Unicode
     (x², Na⁺, √2); "chem": H2O → H₂O; amit Unicode-dal nem lehet (F_fel), az jelöléssel marad; „info:” sor.
A fa és a HTML-alak a shared/matek/mtext.js MatText.parse-ával közös (próbák: tools/tests/mx-cases.js).
Csak a Python standard könyvtárát használja.
"""
import datetime
import html as H
import json
import math
import pathlib
import re
import sys
import tempfile
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_LABEL_MAX = 32
MAX_WORDS = 55
UNIT_ALIASES = {"cm3": "cm³", "m3": "m³", "dm3": "dm³", "mm3": "mm³", "g/cm3": "g/cm³", "kg/m3": "kg/m³",
                "kg/dm3": "kg/dm³", "fok": "°", "°c": "°C", "C°": "°C"}
NUM_RE = re.compile(r"^([−\-+]?)(\d{1,3}(?:[ \u00a0\u202f]\d{3})+|\d+)(?:,(\d+))?(?=\s|$|%|°|/|′|')\s*(.*)$")
TYPES = ("number", "year", "date", "coord", "range", "ago", "ratio", "frac", "list", "series", "point", "expr",
         "formula", "equation", "utc", "dataset", "metrum", "rhyme", "morph", "pron", "rel")
HU_TYPES = {"metrum", "rhyme", "morph", "pron", "rel"}     # magyar: nem szám, nincs becslés-/évjelző
NB = "\u00a0"                                   # nem törő szóköz: „Kr. e. 753” ne törjön sort
MONTHS = ["január", "február", "március", "április", "május", "június", "július", "augusztus",
          "szeptember", "október", "november", "december"]
MULT = {"ezer": 1e3, "millió": 1e6, "milliárd": 1e9, "billió": 1e12, "trillió": 1e18}
INT = r"\d{1,3}(?:[ \u00a0\u202f]\d{3})+|\d+"
NUM = rf"(?:{INT})(?:,\d+)?"
EST_PRE = re.compile(r"^(?:kb\.|kb\s|cca\.|~|≈)\s*", re.I)
EST_POST = re.compile(r"\s*\((?:becslés|becsült)\)$", re.I)
ERA = r"(?:(Kr\.\s*e\.|i\.\s*e\.)|(Kr\.\s*u\.|i\.\s*sz\.))"
YEAR_RE = re.compile(rf"^{ERA}?\s*({INT})(\s+körül)?$", re.I)
DATE_RE = re.compile(rf"^{ERA}?\s*({INT})\.\s+([a-zéáíóöőúüű]+)(?:\s+(\d{{1,2}})\.)?$", re.I)
COORD_PART = re.compile(r"(\d{1,3}(?:,\d+)?)\s*°(?:\s*(\d{1,2}(?:,\d+)?)\s*[′'])?\s*(É|D|K|Ny)\b")
RANGE_RE = re.compile(rf"^((?:{INT})(?:,\d+)?)\s*([–\-])\s*((?:{INT})(?:,\d+)?)(?=\s|$|%|/)\s*(.*)$")
AGO_RE = re.compile(rf"^({NUM})(?:\s*([–\-])\s*({NUM}))?\s+(?:(ezer|millió|milliárd)\s+)?éve$")
# mértékegység-családok: egység → szorzó az alapegységre
DIMS = {
    "hosszúság": ("m", {"nm": 1e-9, "µm": 1e-6, "mm": 1e-3, "cm": 1e-2, "dm": 0.1, "m": 1, "km": 1e3}),
    "terület": ("m²", {"mm²": 1e-6, "cm²": 1e-4, "dm²": 1e-2, "m²": 1, "a": 100, "ha": 1e4, "km²": 1e6}),
    "térfogat": ("l", {"µl": 1e-6, "mm³": 1e-6, "ml": 1e-3, "cm³": 1e-3, "cl": 1e-2, "dl": 0.1, "l": 1, "dm³": 1,
                       "hl": 100, "m³": 1000, "km³": 1e12}),
    "tömeg": ("kg", {"µg": 1e-9, "mg": 1e-6, "g": 1e-3, "dkg": 1e-2, "kg": 1, "t": 1e3}),
    "idő": ("s", {"ms": 1e-3, "s": 1, "perc": 60, "min": 60, "óra": 3600, "h": 3600, "nap": 86400,
                  "hét": 604800, "év": 31557600}),
    "szög": ("°", {"°": 1, "′": 1 / 60}),
}
DIM_ALIAS = {"hossz": "hosszúság", "térf": "térfogat"}
DIM_UNIT_ALIASES = {"cm2": "cm²", "m2": "m²", "dm2": "dm²", "mm2": "mm²", "km2": "km²", "L": "l", "liter": "l",
                    "km3": "km³", "um": "µm", "μm": "µm", "μl": "µl", "μg": "µg", "ul": "µl"}
TAG_WORDS = {"frissítendő": "upd", "előrejelzés": "proj", "modell": "model", "becslés": "est", "becsült": "est"}


class Problems:
    def __init__(self, path):
        self.path, self.errors, self.warnings, self.infos = path, [], [], []

    def err(self, line, msg):
        self.errors.append(f"{self.path.name}{f':{line}' if line else ''}: HIBA: {msg}")

    def warn(self, line, msg):
        m = f"{self.path.name}{f':{line}' if line else ''}: figyelem: {msg}"
        if m not in self.warnings:
            self.warnings.append(m)

    def info(self, line, msg):
        self.infos.append(f"{self.path.name}{f':{line}' if line else ''}: info: {msg}")


def norm_unit(u):
    u = u.strip()
    return UNIT_ALIASES.get(u, UNIT_ALIASES.get(u.lower(), u))


def to_float(intp, frac):
    return float(re.sub(r"[ \u00a0\u202f]", "", intp) + ("." + frac if frac else ""))


def clean(v):
    """Szorzás utáni lebegőpontos zaj eltüntetése: 8,2 · 10⁹ = 8200000000.0, nem 8199999999.999999."""
    return float(f"{v:.12g}")


def num_of(t):
    """'3,25' / '19 300' → float (előjel nélkül)."""
    i, _, f = t.partition(",")
    return to_float(i, f or None)


def parse_number(raw, line, P):
    """'0,92 g/cm³' → (0.92, 'g/cm³', 2). Magyar tizedesvessző, valódi mínusz, szóközös ezres tagolás."""
    s = raw.strip()
    if re.match(r"^[−\-+]?\d+\.\d", s):
        P.err(line, f"„{s}”: tizedesvesszőt használj, ne pontot (pl. 0,92).")
        return None
    m = NUM_RE.match(s)
    if not m:
        P.err(line, f"„{s}”: nem értelmezhető szám (formátum: 0,92 g/cm³ · 19 300 g · −4 °C).")
        return None
    sign, intp, frac, unit = m.groups()
    if sign == "-":
        P.warn(line, f"„{s}”: kötőjel helyett valódi mínuszjelet (−) írj.")
    v = to_float(intp, frac)
    if sign in "−-" and sign:
        v = -v
    return v, norm_unit(unit), len(frac or "")


def fmt_num(v, d):
    s = f"{abs(v):.{d}f}".split(".")
    i = s[0]
    if len(i) > 4:
        i = re.sub(r"\B(?=(\d{3})+(?!\d))", "\u202f", i)
    return ("−" if v < 0 else "") + i + ("," + s[1] if len(s) > 1 else "")


def unit_sep(u):
    """Szám és egység között: 20 °C, de 15° és 70/perc (szóköz nélkül)."""
    return "" if not u or u in ("°", "′") or u.startswith("/") else NB


def fmt_value(v, d, u):
    return fmt_num(v, d) + ((u if u == "°" else NB + u) if u else "")   # szögfok: 15° (szóköz nélkül); 20 °C


def split_est(s):
    """Becslésjelző leválasztása: 'kb. 50–70 ezer fő' → ('50–70 ezer fő', True)."""
    s, est = s.strip(), False
    m = EST_PRE.match(s)
    if m:
        s, est = s[m.end():].strip(), True
    m = EST_POST.search(s)
    if m:
        s, est = s[:m.start()].strip(), True
    return s, est


def split_tags(s):
    """Záró zárójeles jelölők: '8,2 milliárd fő (2025, frissítendő)' → ('8,2 milliárd fő', {'yr': 2025, 'upd': True}).
    Csak akkor, ha a zárójelben minden elem ismert jelölő (évszám vagy TAG_WORDS)."""
    m = re.search(r"\s*\(([^()]*)\)$", s)
    if not m:
        return s, {}
    tags = {}
    for part in (p.strip().lower() for p in m.group(1).split(",")):
        if re.fullmatch(r"\d{4}", part) and "yr" not in tags:
            tags["yr"] = int(part)
        elif part in TAG_WORDS:
            tags[TAG_WORDS[part]] = True
        else:
            return s, {}
    return s[:m.start()].strip(), tags


def split_mult(rest, want_unit, line=None, P=None):
    """('ezer fő', 'fő') → (1000, 'ezer', 'fő'); ('millió/µl', '/µl') → (1e6, 'millió', '/µl').
    Ha a teljes maradék maga az elvárt egység, nincs szorzó."""
    u = norm_unit(rest)
    if u == norm_unit(want_unit):
        return 1, "", u
    m = re.match(r"^(\S+?)(?:\s+|(?=/)|$)(.*)$", rest.strip())
    w, tail = (m.group(1), m.group(2)) if m else ("", "")
    if w in MULT:
        if w == "trillió" and P:
            P.warn(line, "„trillió” = 10¹⁸ – angol forrásból (trillion = 10¹² = billió) szinte mindig hibás; ellenőrizd.")
        return MULT[w], w, norm_unit(tail)
    return 1, "", u


def year_str(v, bc_style, ad_style):
    n = fmt_num(abs(v), 0)
    if v < 0:
        return (bc_style or "Kr. e.").replace(" ", NB) + NB + n
    return (ad_style.replace(" ", NB) + NB + n) if ad_style else n


def era_styles(bc, ad):
    norm = lambda e: re.sub(r"\.\s*", ". ", e.strip()).strip()   # 'Kr.e.' → 'Kr. e.'
    return (norm(bc).replace("I.", "i.").replace("KR.", "Kr.") if bc else None,
            norm(ad).replace("I.", "i.").replace("KR.", "Kr.") if ad else None)


def parse_year(s, line, P, k):
    if re.match(r"^[−\-]\s*\d", s):
        P.err(line, f"„{k}” = {s}: időszámításunk előtti évet „Kr. e. {s.lstrip('−-').strip()}” alakban írj.")
        return None
    if re.search(r"\béve\b", s):
        P.err(line, f"„{k}” = {s}: ez évszám-adat; az „… éve” (pl. 66 millió éve) a mély idő („ago”) típusa.")
        return None
    m = YEAR_RE.match(s)
    if not m:
        P.err(line, f"„{k}” = {s}: nem értelmezhető évszám (formátum: Kr. e. 753 · Kr. u. 476 · 1241).")
        return None
    bc, ad, num, korul = m.groups()
    n = int(re.sub(r"\D", "", num))
    if n == 0:
        P.err(line, f"„{k}” = {s}: 0. év nincs (Kr. e. 1 után rögtön Kr. u. 1 következik).")
        return None
    bc, ad = era_styles(bc, ad)
    v = -n if bc else n
    return {"t": "year", "v": v, "a": v + 1 if v < 0 else v}, year_str(v, bc, ad), bool(korul)


def is_leap(a):             # a: csillagászati év; 1582 előtt Julián, utána Gergely-naptár
    return a % 4 == 0 if a < 1583 else (a % 4 == 0 and a % 100 != 0 or a % 400 == 0)


def parse_date(s, line, P, k):
    m = DATE_RE.match(s)
    if not m:
        P.err(line, f"„{k}” = {s}: nem értelmezhető dátum (formátum: 1848. március 15. · 1848. március).")
        return None
    bc, ad, num, mon, day = m.groups()
    n = int(re.sub(r"\D", "", num))
    if n == 0:
        P.err(line, f"„{k}” = {s}: 0. év nincs.")
        return None
    if mon.lower() not in MONTHS:
        P.err(line, f"„{k}” = {s}: ismeretlen hónap „{mon}” (január … december, kisbetűvel, kiírva).")
        return None
    bc, ad = era_styles(bc, ad)
    v = -n if bc else n
    a = v + 1 if v < 0 else v
    mi = MONTHS.index(mon.lower()) + 1
    mlen = [31, 29 if is_leap(a) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = int(day) if day else None
    if d is not None and not 1 <= d <= mlen[mi - 1]:
        P.err(line, f"„{k}” = {s}: {MONTHS[mi - 1]} {d}. nem létező nap.")
        return None
    doy = sum(mlen[:mi - 1]) + ((d - 0.5) if d else mlen[mi - 1] / 2)
    frac = round(doy / sum(mlen), 4)
    text = year_str(v, bc, ad) + ". " + MONTHS[mi - 1] + (f" {d}." if d else "")
    return {"t": "date", "v": v, "ymd": [v, mi, d], "a": round(a + frac, 4)}, text, False


def parse_coord(s, line, P, k, want):
    parts = list(COORD_PART.finditer(s))
    rest = COORD_PART.sub("", s).strip(" ,;")
    if len(parts) != 2 or rest:
        P.err(line, f"„{k}” = {s}: nem értelmezhető koordináta (formátum: 47,50° É, 19,04° K).")
        return None
    lat = lon = None
    for p in parts:
        deg, mins, hemi = p.groups()
        x = to_float(*(deg.split(",") + [None])[:2])
        if mins:
            mm = to_float(*(mins.split(",") + [None])[:2])
            if mm >= 60:
                P.err(line, f"„{k}” = {s}: a szögperc 60-nál kisebb legyen.")
                return None
            x += mm / 60
        if hemi in ("É", "D"):
            lat = (x if hemi == "É" else -x) if lat is None else "dup"
        else:
            lon = (x if hemi == "K" else -x) if lon is None else "dup"
    if lat in (None, "dup") or lon in (None, "dup"):
        P.err(line, f"„{k}” = {s}: egy szélesség (É/D) és egy hosszúság (K/Ny) kell.")
        return None
    if abs(lat) > 90 or abs(lon) > 180:
        P.err(line, f"„{k}” = {s}: a szélesség legfeljebb 90°, a hosszúság legfeljebb 180° lehet.")
        return None
    box = want.get("box")
    if box and not (box[0] <= lon <= box[2] and box[1] <= lat <= box[3]):
        P.err(line, f"„{k}” = {s}: kívül esik a lecke térképén ({box[1]}–{box[3]}° É, {box[0]}–{box[2]}° K). "
                    "Elcserélted az É/K jelet?")
        return None
    text = ", ".join(re.sub(r"\s+", " ", p.group(0)).replace("° ", "°" + NB) for p in parts)
    return {"t": "coord", "lat": round(lat, 6), "lon": round(lon, 6)}, text, False


def parse_range(s, line, P, k, want):
    m = RANGE_RE.match(s)
    if not m:
        P.err(line, f"„{k}” = {s}: nem értelmezhető tartomány (formátum: 50–70 ezer fő · 25–28).")
        return None
    a, dash, b, rest = m.groups()
    if dash == "-":
        P.warn(line, f"„{k}” = {s}: kötőjel helyett nagygondolatjelet (–) írj a tartományba.")
    (ai, _, af), (bi, _, bf) = a.partition(","), b.partition(",")
    lo, hi, d = to_float(ai, af), to_float(bi, bf), max(len(af), len(bf))
    dim = want.get("dim")
    if dim:                                   # mértékegység-család: „2–5 mm”, „60–90 µm” → + blo, bhi, base, bu
        dim = DIM_ALIAS.get(dim, dim)
        if dim not in DIMS:
            P.err(line, f"„{k}”: ismeretlen dim „{dim}” (lehet: {', '.join(DIMS)}).")
            return None
        bu, fam = DIMS[dim]
        mult, mw, unit = split_mult(rest, "", line, P)
        unit = DIM_UNIT_ALIASES.get(unit, unit)
        if unit not in fam:
            P.err(line, f"„{k}” = {s}: {dim} mértékegysége kell ({', '.join(fam)}), nem „{unit}”.")
            return None
    else:
        mult, mw, unit = split_mult(rest, want.get("unit", ""), line, P)
        if unit != norm_unit(want.get("unit", "")):
            P.err(line, f"„{k}”: a mértékegység „{want.get('unit', '')}” legyen, nem „{unit}”.")
            return None
    if lo >= hi:
        P.err(line, f"„{k}” = {s}: a tartomány alsó értéke kisebb legyen a felsőnél.")
        return None
    text = fmt_num(lo, len(af)) + "–" + fmt_num(hi, len(bf))
    if mw:
        text += NB + mw + (("" if unit.startswith("/") else NB) + unit if unit else "")
    elif unit:
        text += unit_sep(unit) + unit
    lo, hi = clean(lo * mult), clean(hi * mult)
    d = max(0, d - int(round(math.log10(mult))))
    item = {"t": "range", "lo": lo, "hi": hi, "v": (lo + hi) / 2, "u": unit, "d": d}
    if dim:
        item.update(blo=clean(lo * fam[unit]), bhi=clean(hi * fam[unit]), bu=bu)
        item["base"] = clean((item["blo"] + item["bhi"]) / 2)
    return item, text, False


# ── új adattípusok ─────────────────────────────────────────────────────────────────────────

def parse_number_item(s, n, P, k, want):
    """number típus → (item, text) vagy None."""
    r = parse_number(s, n, P)
    if not r:
        return None
    val, unit, d = r
    raw_sign = s.strip()[:1]
    wu = norm_unit(want.get("unit", ""))
    extra = {}
    text = None
    # szög: 45° 30′
    m = re.fullmatch(r"°\s*(\d{1,2}(?:,\d+)?)\s*([′'])", unit)
    if wu == "°" and (m or unit in ("′", "'")):
        if (m and m.group(2) == "'") or unit == "'":
            P.warn(n, f"„{k}”: szögpercnek ′ jelet írj, ne aposztrófot (45° 30′).")
        if m:
            mins = num_of(m.group(1))
            if mins >= 60:
                P.err(n, f"„{k}” = {s}: a szögperc 60-nál kisebb legyen.")
                return None
            text = fmt_num(val, d) + "°" + NB + m.group(1) + "′"
            val = val + (mins if val >= 0 else -mins) / 60
        else:
            text = fmt_num(val, d) + "′"
            val = val / 60
        unit, d, extra["s"] = "°", max(d, 2), text
    dim = want.get("dim")
    if dim:
        dim = DIM_ALIAS.get(dim, dim)
        if dim not in DIMS:
            P.err(n, f"„{k}”: ismeretlen dim „{dim}” (lehet: {', '.join(DIMS)}).")
            return None
        bu, fam = DIMS[dim]
        u2 = DIM_UNIT_ALIASES.get(unit, unit)
        if u2 not in fam:
            P.err(n, f"„{k}” = {s}: {dim} mértékegysége kell ({', '.join(fam)}), nem „{unit}”.")
            return None
        item = {"v": val, "u": u2, "d": d, "base": val * fam[u2], "bu": bu}
        text = text or (fmt_num(val, d) + unit_sep(u2) + u2)
        item["s"] = text
        chk = item["base"]
        ichk = val                            # int: a megadott egységben („5 cm” egész), nem az alapegységben
    else:
        mult, mw, unit2 = (1, "", unit)
        if unit != wu:
            mult, mw, unit2 = split_mult(unit, want.get("unit", ""), n, P)
        if unit2 != wu:
            P.err(n, f"„{k}”: a mértékegység „{want.get('unit', '')}” legyen, nem „{unit}”.")
        item = {"v": clean(val * mult), "u": unit2, "d": max(0, d - int(round(math.log10(mult))))}
        if text is None:
            text = fmt_value(val, d, unit) if not unit.startswith("/") else fmt_num(val, d) + unit
        if mw:
            item["s"] = text = fmt_num(val, d) + NB + mw + (("" if unit2.startswith("/") else NB) + unit2 if unit2 else "")
        if "s" in extra:
            item["s"] = extra["s"]
        if unit.startswith("/") and not mw:
            item["s"] = text
        chk = ichk = item["v"]
    if want.get("int") and abs(ichk - round(ichk)) > 1e-9:
        P.err(n, f"„{k}” = {s}: egész szám kell.")
    if want.get("sign"):
        if raw_sign == "+" and val > 0:
            text = "+" + text
        item["s"] = text
    return item, text, chk


def parse_ago(s, line, P, k, want):
    if re.search(r"Kr\.|i\.\s*e\.|i\.\s*sz\.", s):
        P.err(line, f"„{k}” = {s}: a mély idő „… éve” alakú (pl. 66 millió éve); „Kr. e.” évszámhoz year típus kell.")
        return None
    m = AGO_RE.match(s)
    if not m:
        P.err(line, f"„{k}” = {s}: nem értelmezhető (formátum: 3,8 milliárd éve · 66 millió éve · 7–6 millió éve).")
        return None
    a, dash, b, mw = m.groups()
    if dash == "-":
        P.warn(line, f"„{k}” = {s}: kötőjel helyett nagygondolatjelet (–) írj a tartományba.")
    mult = MULT[mw] if mw else 1
    text = fmt_num(num_of(a), len(a.partition(",")[2])) + "".join(
        ["–" + fmt_num(num_of(b), len(b.partition(",")[2]))] if b else []) + (NB + mw if mw else "") + NB + "éve"
    va = clean(num_of(a) * mult)
    item = {"t": "ago", "v": va}
    if b:
        vb = clean(num_of(b) * mult)
        if va == vb:
            P.err(line, f"„{k}” = {s}: a tartomány két vége egyforma.")
            return None
        item.update(lo=min(va, vb), hi=max(va, vb), v=(va + vb) / 2)
    return item, text, False


def parse_ratio(s, line, P, k, want):
    parts = [p.strip() for p in s.split(":")]
    if len(parts) < 2 or not all(re.fullmatch(NUM, p) for p in parts):
        P.err(line, f"„{k}” = {s}: nem értelmezhető arány (formátum: 3 : 1 · 5474 : 1850 · 16 : 9).")
        return None
    vals = [num_of(p) for p in parts]
    if any(v == 0 for v in vals[1:]):
        P.err(line, f"„{k}” = {s}: az arány tagja nem lehet 0.")
        return None
    item = {"t": "ratio", "a": vals[0], "b": vals[1], "v": vals[0] / vals[1]}
    if len(vals) > 2:
        item["p"] = vals
    return item, (NB + ":" + NB).join(fmt_num(v, len(p.partition(",")[2])) for v, p in zip(vals, parts)), False   # „105 : 100” nem törik


def parse_frac(s, line, P, k, want):
    if re.fullmatch(rf"{NUM}\s*:\s*{NUM}", s):
        P.err(line, f"„{k}” = {s}: ez arány – törtet így írj: 3/4 (arányhoz a lecke ratio típust használjon).")
        return None
    m = re.fullmatch(r"([−\-+]?)\s*(?:(\d+)\s+)?(\d+)\s*/\s*(\d+)", s)
    if not m:
        P.err(line, f"„{k}” = {s}: nem értelmezhető tört (formátum: 3/4 · 2 1/3 · −5/8).")
        return None
    sign, w, a, b = m.groups()
    if sign == "-":
        P.warn(line, f"„{k}” = {s}: kötőjel helyett valódi mínuszjelet (−) írj.")
    w, a, b = int(w or 0), int(a), int(b)
    if b == 0:
        P.err(line, f"„{k}” = {s}: a nevező nem lehet 0.")
        return None
    if w and a >= b:
        P.err(line, f"„{k}” = {s}: vegyes számban a tört része valódi tört legyen (számláló < nevező).")
        return None
    if want.get("maxDen") and b > want["maxDen"]:
        P.err(line, f"„{k}” = {s}: a nevező legfeljebb {want['maxDen']} lehet.")
    if want.get("proper") and (w or a >= b):
        P.err(line, f"„{k}” = {s}: valódi tört kell (a számláló kisebb a nevezőnél).")
    g = math.gcd(a, b)
    if want.get("reduced") and g > 1:
        P.err(line, f"„{k}” = {s}: nem egyszerűsített alak ({a}/{b} → {a // g}/{b // g}?).")
    neg = sign in ("−", "-")
    v = (w + a / b) * (-1 if neg else 1)
    text = ("−" if neg else "") + (f"{w} " if w else "") + f"{a}/{b}"
    return {"t": "frac", "n": a, "d": b, "w": w, "neg": neg, "v": v, "red": g == 1}, text, False


def parse_list(s, line, P, k, want):
    if ";" not in s and re.search(r"\d,\s+[−\-]?\d", s):
        P.err(line, f"„{k}” = {s}: az elemeket pontosvesszővel válaszd el (a vessző tizedesvessző): 2; 3; 5.")
        return None
    parts = [p.strip() for p in s.split(";")]
    if any(not p for p in parts):
        P.err(line, f"„{k}” = {s}: üres elem a listában.")
        return None
    vals, units, ds = [], [], []
    for p in parts:
        r = parse_number(p, line, P)
        if not r:
            return None
        vals.append(r[0]); units.append(r[1]); ds.append(r[2])
    wu = norm_unit(want.get("unit", ""))
    given = [u for u in units if u]
    if given and (len(set(given)) > 1 or not (len(given) == len(units) or len(given) == 1 and units[-1])):
        P.err(line, f"„{k}” = {s}: a mértékegységet egyszer, a lista végére írd (−1,2; 0,9; 5,4 °C).")
        return None
    unit = given[0] if given else ""
    if unit != wu:
        P.err(line, f"„{k}”: a mértékegység „{want.get('unit', '')}” legyen, nem „{unit}”.")
        return None
    ln = want.get("len")
    if ln is not None:
        lo, hi = (ln, ln) if isinstance(ln, int) else ln
        if not lo <= len(vals) <= hi:
            P.err(line, f"„{k}”: {len(vals)} elem van, " + (f"{lo} kell." if lo == hi else f"{lo}–{hi} kell."))
    if want.get("int") and any(abs(v - round(v)) > 1e-9 for v in vals):
        P.err(line, f"„{k}” = {s}: minden elem egész szám legyen.")
    text = "; ".join(fmt_num(v, d) for v, d in zip(vals, ds)) + (unit_sep(unit) + unit if unit else "")
    return {"t": "list", "v": vals, "u": unit, "d": max(ds)}, text, False


def parse_series(s, line, P, k, want):
    pairs = [p.strip() for p in re.split(r"\s*[·;]\s*", s) if p.strip()]
    xs, ys, txt, dx, dy = [], [], [], 0, 0
    ux, uy = norm_unit(want.get("ux", "")), norm_unit(want.get("unit", ""))
    for p in pairs:
        a, sep, b = p.partition(":")
        if not sep:
            P.err(line, f"„{k}”: „{p}” – a párokat „x: y” alakban, „·” jellel elválasztva írd (0 °C: 13,3 · 20 °C: 31,6).")
            return None
        ra, rb = parse_number(a, line, P), parse_number(b, line, P)
        if not ra or not rb:
            return None
        if ra[1] != ux:
            P.err(line, f"„{k}”: az x mértékegysége „{ux}” legyen, nem „{ra[1]}”.")
            return None
        if rb[1] and rb[1] != uy:
            P.err(line, f"„{k}”: az y mértékegysége „{uy}” legyen, nem „{rb[1]}”.")
            return None
        xs.append(ra[0]); ys.append(rb[0]); dx, dy = max(dx, ra[2]), max(dy, rb[2])
        txt.append(fmt_num(ra[0], ra[2]) + unit_sep(ux) + ux + ": " + fmt_num(rb[0], rb[2]))
    if any(b <= a for a, b in zip(xs, xs[1:])):
        P.err(line, f"„{k}”: az x értékei szigorúan növekedjenek.")
        return None
    ln = want.get("len")
    if ln is not None:
        lo, hi = (ln, ln) if isinstance(ln, int) else ln
        if not lo <= len(xs) <= hi:
            P.err(line, f"„{k}”: {len(xs)} pár van, " + (f"{lo} kell." if lo == hi else f"{lo}–{hi} kell."))
    if "xmin" in want and xs[0] < want["xmin"] or "xmax" in want and xs[-1] > want["xmax"]:
        P.err(line, f"„{k}”: az x kívül esik a tartományon ({want.get('xmin', '…')} – {want.get('xmax', '…')}).")
    return {"t": "series", "x": xs, "y": ys, "ux": ux, "uy": uy, "dx": dx, "dy": dy}, " · ".join(txt), False


def parse_point(s, line, P, k, want):
    m = re.fullmatch(r"([A-Z][′']*)?\s*\(\s*([^;()]+?)\s*;\s*([^;()]+?)\s*\)", s)
    if not m:
        hint = " A koordinátákat pontosvesszővel válaszd el (a vessző tizedesvessző)." if "," in s else ""
        P.err(line, f"„{k}” = {s}: nem értelmezhető pont (formátum: (2; −1,5) · A(3; −2)).{hint}")
        return None
    name, a, b = m.groups()
    ra, rb = parse_number(a, line, P), parse_number(b, line, P)
    if not ra or not rb:
        return None
    if ra[1] or rb[1]:
        P.err(line, f"„{k}” = {s}: a pont koordinátái mértékegység nélküli számok.")
        return None
    x, y = ra[0], rb[0]
    box = want.get("box")
    if box and not (box[0] <= x <= box[2] and box[1] <= y <= box[3]):
        P.err(line, f"„{k}” = {s}: kívül esik a lecke koordináta-rendszerén (x: {box[0]}…{box[2]}, y: {box[1]}…{box[3]}).")
        return None
    if want.get("int") and (x != int(x) or y != int(y)):
        P.err(line, f"„{k}” = {s}: egész koordináták kellenek.")
    item = {"t": "point", "x": x, "y": y}
    if name:
        item["name"] = name.replace("'", "′")
    return item, (item.get("name", "")) + f"({fmt_num(x, ra[2])}; {fmt_num(y, rb[2])})", False


def parse_utc(s, line, P, k, want):
    m = re.fullmatch(r"UTC\s*(?:([+−\-±])\s*(\d{1,2})(?::(\d{2}))?)?", s)
    if not m:
        P.err(line, f"„{k}” = {s}: nem értelmezhető időzóna (formátum: UTC+1 · UTC+5:30 · UTC−5 · UTC).")
        return None
    sign, h, mi = m.groups()
    if sign == "-":
        P.warn(line, f"„{k}” = {s}: kötőjel helyett valódi mínuszjelet (−) írj: UTC−5.")
    h, mi = int(h or 0), int(mi or 0)
    if mi not in (0, 15, 30, 45) or h > 14 or (h == 14 and mi):
        P.err(line, f"„{k}” = {s}: az eltérés −12:00 és +14:00 között, negyedórás lépésben lehet.")
        return None
    tot = (h * 60 + mi) * (-1 if sign in ("−", "-") else 1)
    if not sign:
        text = "UTC"
    else:
        text = "UTC" + ("±" if sign == "±" else "−" if tot < 0 else "+") + str(h) + (f":{mi:02d}" if mi else "")
    return {"t": "utc", "min": tot}, text, False


def dataset_header(path):
    head = path.read_text(encoding="utf-8", errors="replace")[:6000]
    out = {}
    for f in ("id", "ver", "src"):
        m = re.search(rf"[\"']?\b{f}[\"']?\s*:\s*[\"']([^\"'\n]+)[\"']", head)
        if m:
            out[f] = m.group(1).strip()
    return out


def parse_dataset(s, line, P, k, want):
    did = want.get("id")
    if not did:
        P.err(line, f"„{k}”: a dataset típusnál a spec-ben „id” kell (pl. \"id\": \"korfa-wpp2024\").")
        return None
    path = ROOT / (want.get("path") or f"shared/foldrajz/{did}.js")
    if not path.exists():
        P.err(line, f"„{k}”: nincs ilyen adatfájl: {path.relative_to(ROOT).as_posix()}")
        return None
    hd = dataset_header(path)
    norm = lambda t: re.sub(r"\s+", " ", t.strip())
    if hd.get("id") and hd["id"] != did:
        P.err(line, f"„{k}”: az adatfájl azonosítója „{hd['id']}”, a spec-ben „{did}”.")
    # a .md szövege a forrássor rövid neve („ENSZ WPP 2024”); a benne álló évszám(ok) a fájl fejlécében
    # (src/ver) is szerepeljen – így egy adatfrissítés után a .md elavult évszáma kiderül
    head = " ".join(hd.get(f, "") for f in ("src", "ver"))
    miss = [y for y in re.findall(r"\b(?:19|20)\d\d\b", s) if y not in head]
    if head.strip() and miss:
        P.err(line, f"„{k}” = {s}: a(z) {', '.join(miss)} nem szerepel az adatfájl fejlécében "
                    f"(verzió: {hd.get('ver') or '–'}) – frissítsd a .md-t.")
        return None
    item = {"t": "dataset", "id": did}
    item.update({f: hd[f] for f in ("src", "ver") if f in hd})
    return item, norm(s), False


# ── kémiai képlet és egyenlet ──
def chem_formula(f):
    """'Ca(OH)2', 'SO4^2-', 'H₂O', 'Mg²⁺' → (atoms, charge, unicode, html) vagy hibaüzenet (str)."""
    f = f.strip()
    m = re.search("[⁰¹²³⁴⁵⁶⁷⁸⁹]*[⁺⁻]$", f)
    if m:
        f = f[:m.start()] + "^" + m.group(0).translate(SUP_IN)
    f = f.translate(SUB_IN)
    body, _, ch = f.partition("^")
    charge = 0
    if ch:
        mm = re.fullmatch(r"(\d*)([+\-−])", ch)
        if not mm:
            return f"„{f}”: a töltést így írd: Na^+ · SO4^2- (vagy Na⁺, SO₄²⁻)"
        charge = int(mm.group(1) or 1) * (1 if mm.group(2) == "+" else -1)
    stack, i, uni, htm = [{}], 0, "", ""
    while i < len(body):
        c = body[i]
        if c == "(":
            stack.append({}); uni += c; htm += c; i += 1; continue
        mm = re.match(r"\)(\d*)|([A-Z][a-z]?)(\d*)", body[i:])
        if not mm:
            return f"„{f}”: váratlan jel „{c}” a képletben"
        if mm.group(0).startswith(")"):
            if len(stack) < 2:
                return f"„{f}”: páratlan zárójel"
            num = int(mm.group(1) or 1)
            top = stack.pop()
            for a, n in top.items():
                stack[-1][a] = stack[-1].get(a, 0) + n * num
            uni += ")" + (mm.group(1) or "").translate(SUB_OUT)
            htm += ")" + (f"<sub>{mm.group(1)}</sub>" if mm.group(1) else "")
        else:
            sym, num = mm.group(2), mm.group(3)
            if sym not in ELEMENTS:
                return f"„{f}”: ismeretlen vegyjel „{sym}”"
            stack[-1][sym] = stack[-1].get(sym, 0) + int(num or 1)
            uni += sym + num.translate(SUB_OUT)
            htm += sym + (f"<sub>{num}</sub>" if num else "")
        i += len(mm.group(0))
    if len(stack) != 1 or not stack[0]:
        return f"„{f}”: " + ("páratlan zárójel" if len(stack) != 1 else "üres képlet")
    if charge:
        q = (str(abs(charge)) if abs(charge) > 1 else "") + ("+" if charge > 0 else "−")
        uni += q.translate(SUP_OUT)
        htm += f"<sup>{q}</sup>"
    return stack[0], charge, uni, htm


def parse_formula(s, line, P, k, want):
    r = chem_formula(s)
    if isinstance(r, str):
        P.err(line, f"„{k}”: {r}.")
        return None
    atoms, charge, uni, htm = r
    if "atoms" in want and atoms != want["atoms"]:
        P.err(line, f"„{k}” = {s}: a lecke {fmt_atoms(want['atoms'])} összetételt vár, ez {fmt_atoms(atoms)}.")
    if "charge" in want and charge != want["charge"]:
        P.err(line, f"„{k}” = {s}: a lecke {want['charge']} töltést vár, ez {charge}.")
    return {"t": "formula", "atoms": atoms, "charge": charge, "_html": htm}, uni, False


def fmt_atoms(a):
    return ", ".join(f"{n} {e}" for e, n in a.items())


def parse_equation(s, line, P, k, want):
    sides = re.split(r"\s*(?:→|->)\s*", s)
    if len(sides) != 2:
        P.err(line, f"„{k}” = {s}: " + ("pontosan egy nyíl (→ vagy ->) kell a két oldal közé."
                                       if len(sides) > 2 or not re.search("⇌|<->|=", s) else
                                       "a reakcióegyenletben nyíl áll (→ vagy ->), nem = vagy ⇌."))
        return None
    out, tot, uni, htm = {}, [{}, {}], [], []
    for si, side in enumerate(sides):
        terms = []
        for t in re.split(r"\s+\+\s+", side.strip()):
            m = re.fullmatch(r"(\d+)?\s*(\S+)", t.strip())
            if not m:
                P.err(line, f"„{k}”: nem értelmezhető tag: „{t}”.")
                return None
            kf = int(m.group(1) or 1)
            r = chem_formula(m.group(2))
            if isinstance(r, str):
                P.err(line, f"„{k}”: {r}.")
                return None
            atoms, charge, u, h = r
            terms.append({"k": kf, "f": u, "atoms": atoms, "charge": charge})
            for a, n in atoms.items():
                tot[si][a] = tot[si].get(a, 0) + n * kf
            tot[si]["±"] = tot[si].get("±", 0) + charge * kf
            uni.append((f"{kf} " if kf > 1 else "") + u)
            htm.append((f"{kf} " if kf > 1 else "") + h)
        out["lhs" if si == 0 else "rhs"] = terms
        uni.append("→"); htm.append("→")
    uni.pop(); htm.pop()
    nl = len(out["lhs"])
    text = " + ".join(uni[:nl]) + " → " + " + ".join(uni[nl + 1:])
    html_ = " + ".join(htm[:nl]) + " → " + " + ".join(htm[nl + 1:])
    bad = []
    for a in list(dict.fromkeys(list(tot[0]) + list(tot[1]))):
        if a != "±" and tot[0].get(a, 0) != tot[1].get(a, 0):
            bad.append(f"bal oldalon {tot[0].get(a, 0)} {a}, jobb oldalon {tot[1].get(a, 0)} {a}")
    if tot[0].get("±", 0) != tot[1].get("±", 0):
        bad.append(f"a töltés bal oldalon {tot[0].get('±', 0):+d}, jobb oldalon {tot[1].get('±', 0):+d}")
    if bad:
        P.err(line, f"„{k}” = {s}: nincs kiegyenlítve: " + "; ".join(bad) + ".")
        return None
    return {"t": "equation", **out, "_html": html_}, text, False


# ── kifejezés (expr) ──
EXPR_TOK = re.compile(r"\s*(?:(\d+(?:,\d+)?)|(<=>|<=|>=|!=|[=<>≤≥≠])|([+\-−·*×:/^()|√])|([A-Za-z])|(\S))")
REL = {"<=": "≤", ">=": "≥", "!=": "≠"}


def parse_expr_tree(src, vars_):
    """→ (fa, tokenek) vagy hibaüzenet (str)."""
    toks, pos = [], 0
    while pos < len(src):
        m = EXPR_TOK.match(src, pos)
        if not m or m.end() == pos:
            break
        pos = m.end()
        num, rel, op, var, bad = m.groups()
        if bad:
            return f"ismeretlen jel „{bad}” a kifejezésben"
        if num:
            toks.append(("n", num))
        elif rel:
            toks.append(("r", REL.get(rel, rel)))
        elif op:
            toks.append(("o", {"-": "−", "*": "·", "×": "·"}.get(op, op)))
        else:
            if var not in vars_:
                return f"„{var}” betű nem szerepel a lecke változói között ({', '.join(vars_) or 'nincs'})"
            toks.append(("v", var))
    if not toks:
        return "üres kifejezés"
    i = 0

    def peek():
        return toks[i] if i < len(toks) else (None, None)

    def eat():
        nonlocal i
        i += 1
        return toks[i - 1]

    def num(t):
        return int(t) if "," not in t else float(t.replace(",", "."))

    def atom():
        t, v = peek()
        if t == "n":
            eat()
            # tört-literál: egész/egész (utána nem ^) → egyetlen levél, erősebben köt, mint a · : (1/3 · 3/4 →
            # [·, [/, 1, 3], [/, 3, 4]]; 2 : 1/4 → [:, 2, [/, 1, 4]]) – mint a MatExpr v1.1 (matematika-5-6/04)
            d, nx = (toks[i + 1] if i + 1 < len(toks) else None), (toks[i + 2] if i + 2 < len(toks) else None)
            if peek()[1] == "/" and d and d[0] == "n" and "," not in v and "," not in d[1] and not (nx and nx[1] == "^"):
                eat(); eat(); return ["/", num(v), num(d[1])]
            return num(v)
        if t == "v":
            eat(); return v
        if v == "(":
            eat(); e = summ()
            if peek()[1] != ")":
                raise ValueError("páratlan zárójel: hiányzik egy „)”")
            eat(); return ["()", e]
        if v == "|":
            eat(); e = summ()
            if peek()[1] != "|":
                raise ValueError("lezáratlan abszolútérték-jel |")
            eat(); return ["abs", e]
        if v == "√":
            eat(); return ["√", atom()]
        if t is None:
            raise ValueError("a kifejezés hiányosan végződik")
        raise ValueError(f"két műveleti jel egymás után („{v}”)" if t == "o" else f"váratlan „{v}”")

    def power():
        a = atom()
        if peek()[1] == "^":
            eat(); return ["^", a, unary()]
        return a

    def unary():
        t, v = peek()
        if t == "o" and v in "+−":
            eat(); return ["neg" if v == "−" else "pos", unary()]
        return power()

    def term():
        a = unary()
        while True:
            t, v = peek()
            if t == "o" and v in "·:/":
                eat(); a = [v, a, unary()]
            elif t == "v" or v in ("(", "√"):
                a = ["imp", a, unary()]
            elif t == "n":
                raise ValueError("hiányzó műveleti jel két szám között")
            else:
                return a

    def summ():
        a = term()
        while peek()[0] == "o" and peek()[1] in "+−":
            v = eat()[1]
            a = [v, a, term()]
        return a

    try:
        e = summ()
        if peek()[0] == "r":
            r = eat()[1]
            e = [r, e, summ()]
            if peek()[0] == "r":
                raise ValueError("csak egy reláció (=, <, ≤ …) állhat a kifejezésben")
        if i < len(toks):
            raise ValueError(f"váratlan „{toks[i][1]}”" + (" (páratlan zárójel)" if toks[i][1] == ")" else ""))
    except ValueError as ex:
        return str(ex)
    return e, [v for _, v in toks]


def expr_str(e):
    if isinstance(e, (int, float)):
        return fmt_num(e, len(repr(e).partition(".")[2]) if isinstance(e, float) else 0)
    if isinstance(e, str):
        return e
    op = e[0]
    if op == "()":
        return "(" + expr_str(e[1]) + ")"
    if op == "abs":
        return "|" + expr_str(e[1]) + "|"
    if op == "√":
        return "√" + expr_str(e[1])
    if op == "neg":
        return "−" + expr_str(e[1])
    if op == "pos":
        return "+" + expr_str(e[1])
    if op == "^":
        b, bs = e[2], expr_str(e[2])
        simple = isinstance(b, (int, str)) or b[0] == "()" or b[0] == "neg" and isinstance(b[1], (int, str))
        return expr_str(e[1]) + "^" + (bs if simple else "(" + bs + ")")
    if op == "imp":
        return expr_str(e[1]) + expr_str(e[2])
    if op == "/":
        return expr_str(e[1]) + "/" + expr_str(e[2])
    return expr_str(e[1]) + f" {op} " + expr_str(e[2])


def parse_expr(s, line, P, k, want, ctx):
    if ctx.get("math"):
        if "*" in s:
            P.warn(line, f"„{k}”: szorzásjelnek ·-ot írj (3 · 4), ne *-ot.")
        if re.search(r"(?:^|[\s(])-(?=\s*[\w(])|\s-\s", s):
            P.warn(line, f"„{k}”: kötőjel helyett valódi mínuszjelet (−) írj.")
    r = parse_expr_tree(s, want.get("vars", ["x"]))
    if isinstance(r, str):
        P.err(line, f"„{k}” = {s}: {r}.")
        return None
    tree, tok = r
    text = expr_str(tree)
    mxp = Mx(frac=True)
    return {"t": "expr", "tok": tok, "tree": tree,
            "_html": '<span class="mx">' + nobreak(mx_html(mxp.math(text))) + "</span>"}, text, False


# ── Magyar nyelv és irodalom: idézet, verssor, szóelem, ejtés, szereplőkapcsolat ──────────────────
# Szándékosan egyszerű, kiszámítható szabályok: a build nem elemez verset és nem ragoz. A szótagszám a
# magánhangzók száma (megbízható); a rímképletet, a metrumot és a szóelemzést a .md adja meg kézzel, a
# build csak az egyszerű, biztos ellentmondásokat jelzi (lásd a leckek/README.md „Magyar” szakaszát).
HU_VOWELS = set("aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ" + "õûôëäÕÛÔËÄ")     # + régi nyomdai alakok (õ, û = ő, ű)
HU_LONG = set("áéíóőúűÁÉÍÓŐÚŰ" + "õûôÕÛÔ")
HU_LETTERS = re.compile(r"[^\W\d_]+")
RHYME_NORM = str.maketrans("íóúőűõûôÍÓÚŐŰÕÛÔ", "iouööööö" + "IOUÖÖÖÖÖ")   # a rímben a hosszúság (i/í, o/ó…) nem számít
MORPH_KINDS = ("tő", "képző", "jel", "rag", "kötőhangzó", "előtag")
MORPH_RANK = {"képző": 1, "jel": 2, "rag": 3}
INVARIANT_SUFFIX = {"ért", "ként", "nként", "kor", "ig", "é", "ék", "éi", "né", "i", "ni", "nyi", "képp", "képpen"}
REL_KINDS = ("barát", "ellenség", "család", "szerelem", "szolgál", "vezet")
METER_SYM = {"—": "—", "–": "—", "-": "—", "_": "—", "∪": "∪", "u": "∪", "U": "∪", "◡": "∪", "⏑": "∪", "˘": "∪",
             "×": "×", "x": "×", "X": "×"}
ROMAN = re.compile(r"^(?=[IVXLC])(C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
QUOTE_SRC = re.compile(r"^\s*idézet\s*:", re.I)
DEATH_RE = re.compile(r"(?:(szerző|gyűjtő|lejegyző|fordító|kiadó|szerkesztő|átdolgozó)\s*)?†\s*(?:kb\.\s*|~\s*)?(\d{3,4})", re.I)


def hu_vowels(s, yv=frozenset()):
    """A szótagmagok (magánhangzók) indexei s-ben. Az y csak akkor magánhangzó, ha a szó (kisbetűvel) a spec
    "yVowel" listájában van, és nem egy gy/ly/ny/ty betű része (pl. Teleky: 3 szótag; Kölcsey: 2)."""
    out = []
    for m in HU_LETTERS.finditer(s):
        w, y_ok = m.group(0), m.group(0).lower() in yv
        for j, ch in enumerate(w):
            if ch in HU_VOWELS or y_ok and ch in "yY" and not (j and w[j - 1] in "glntGLNT"):
                out.append(m.start() + j)
    return out


def roman_val(s):
    m = ROMAN.match(s)
    if not m or not s:
        return None
    v, vals = 0, {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    for i, ch in enumerate(s):
        x = vals[ch]
        v += -x if i + 1 < len(s) and vals[s[i + 1]] > x else x
    return v


def harmony(w):
    """Hangrend a toldalék-illeszkedéshez: 'mély' | 'magas' | None (nem dönthető el biztosan → nincs figyelmeztetés).
    Csak e/é/i/í: magas (de csak i/í: None – híd, nyíl); az utolsó nem semleges magánhangzó dönt (kávé, papír:
    mély; sofőr: magas); mély + záró e (hotel, október): ingadozó → None."""
    vs = [c for c in w.lower() if c in HU_VOWELS]
    if not vs:
        return None
    nn = [c for c in vs if c not in "eéií"]
    if not nn:
        return "magas" if any(c in "eé" for c in vs) else None
    if nn[-1] in "öőüűõûô":
        return "magas"
    if vs[-1] == "e" and vs[-1] != nn[-1]:
        return None
    return "mély"


def suffix_harmony(s):
    if s in INVARIANT_SUFFIX:
        return None
    vs = [c for c in s.lower() if c in HU_VOWELS]
    if any(c in "aáoóuú" for c in vs):
        return "mély"
    if any(c in "öőüűeéõûô" for c in vs):
        return "magas"
    return None


def parse_metrum(s, line, P, k, want, ctx):
    """„— ∪ ∪ | — ∪ ∪ | — — | — — | — ∪ ∪ | — ×” → {t: meter, feet: [[—, ∪, ∪], …], n, cz, s}.
    Jelek: — (vagy - – _) hosszú, ∪ (vagy u ◡ ⏑) rövid, × (vagy x) közömbös; | versláb-határ, || sormetszet."""
    feet, cur, cz, i = [], [], [], 0
    while i < len(s):
        ch = s[i]
        if ch.isspace():
            i += 1; continue
        if ch == "|":
            dbl = s[i:i + 2] == "||"
            if cur:
                feet.append(cur); cur = []
            elif not feet:
                P.err(line, f"„{k}” = {s}: a sor nem kezdődhet |-vel."); return None
            if dbl:
                cz.append(len(feet))
            i += 2 if dbl else 1; continue
        if ch not in METER_SYM:
            P.err(line, f"„{k}” = {s}: ismeretlen jel „{ch}” (lehet: — hosszú, ∪ rövid, × közömbös, | versláb, || metszet)."); return None
        cur.append(METER_SYM[ch]); i += 1
    if cur:
        feet.append(cur)
    flat = [x for f in feet for x in f]
    if not flat:
        P.err(line, f"„{k}”: üres metrum."); return None
    if "feet" in want and len(feet) != want["feet"]:
        P.err(line, f"„{k}” = {s}: {len(feet)} versláb, {want['feet']} kell.")
    text = " || ".join(" | ".join(" ".join(f) for f in feet[a:b]) for a, b in zip([0] + cz, cz + [len(feet)]))
    qk = want.get("line")
    q = ctx.get("quotes", {}).get(qk) if qk else None
    if qk and q is None:
        P.err(line, f"„{k}”: a spec „line” sora („{qk}”) nincs az ### Idézet alatt.")
    if q is not None:
        if len(flat) != q["syl"]:
            P.err(line, f"„{k}”: a metrum {len(flat)} szótagos, a(z) „{qk}” sor {q['syl']} szótagos.")
        else:
            for j, (sym, vi) in enumerate(zip(flat, q["v"])):
                if sym == "∪" and q["s"][vi] in HU_LONG:
                    P.warn(line, f"„{k}”: a(z) {j + 1}. szótag ({q['s'][vi]}) hosszú magánhangzó, a metrum rövidnek (∪) jelöli.")
    return {"t": "meter", "feet": feet, "n": len(flat), "cz": cz}, text, False


def parse_rhyme(s, line, P, k, want, ctx):
    """„aabb” (a spec "quotes": idézetcsoport vagy "lines": [kulcsok]) → {t: rhyme, p: [betű soronként], keys, s}.
    Rövidebb képlet ciklikusan ismétlődik (versszakonként); x = rímtelen sor. Csak figyelmeztet, ha a rímpár
    sorvégi magánhangzója eltér (a hosszúság nem számít)."""
    pat = re.sub(r"\s+", "", s)
    if not re.fullmatch(r"[a-z]+", pat):
        P.err(line, f"„{k}” = {s}: a rímképlet kisbetűkből álljon (pl. aabb, abab; x = rímtelen sor)."); return None
    qs = ctx.get("quotes", {})
    if "lines" in want:
        keys = list(want["lines"])
    elif "quotes" in want:
        g = want["quotes"]
        keys = [q for q in qs if q == g or q.startswith(g + " ")]
    else:
        P.err(line, f"„{k}”: a rímképlet specjében „quotes” (idézetcsoport) vagy „lines” kell."); return None
    miss = [q for q in keys if q not in qs]
    if miss or not keys:
        P.err(line, f"„{k}”: nincs ilyen idézetsor: {', '.join(miss) or want.get('quotes')}."); return None
    if len(keys) % len(pat):
        P.err(line, f"„{k}” = {s}: {len(pat)} betűs képlet, de {len(keys)} sor van (a sorok száma legyen a többszöröse)."); return None
    p = [pat[j % len(pat)] for j in range(len(keys))]
    for j0 in range(0, len(keys), len(pat)):           # versszakonként: ugyanaz a betű = ugyanaz a sorvégi magánhangzó
        grp = {}
        for j in range(j0, j0 + len(pat)):
            q = qs[keys[j]]
            if p[j] != "x" and q["v"]:
                grp.setdefault(p[j], []).append((q["s"][q["v"][-1]].lower().translate(RHYME_NORM), keys[j]))
        for letter, vs in grp.items():
            if len({v for v, _ in vs}) > 1:
                P.warn(line, f"„{k}”: a(z) „{letter}” rím sorvégei nem csengenek egybe: " +
                       ", ".join(f"{kk} ({(HU_LETTERS.findall(qs[kk]['s']) or ['?'])[-1]})" for _, kk in vs) + " – ellenőrizd a képletet.")
    return {"t": "rhyme", "p": p, "keys": keys}, pat, False


def parse_morph(s, line, P, k, want, ctx):
    """„kert + ész (képző) + ek (jel) + nek (rag)” → {t: morph, s: 'kertészeknek', parts: [{s, k}, …]};
    „-ban/-ben (rag)” → változatlista: parts[0].alt = ['ban', 'ben']. A fajta zárt listából; az első elem
    alapból tő. Hibát ad, ha rag után jel vagy képző jön; figyelmeztet a hangrend-eltérésre (<!-- ingadozó -->)."""
    raw_parts = [x.strip() for x in re.split(r"\s*\+\s*", s)]
    parts = []
    for j, rp in enumerate(raw_parts):
        m = re.fullmatch(r"(-?[^\s()]+?)\s*(?:\(([^()]*)\))?", rp)
        if not m or not m.group(1).strip("-"):
            P.err(line, f"„{k}” = {s}: nem értelmezhető szóelem „{rp}” (formátum: kert + ész (képző) + ek (jel))."); return None
        form, kind = m.group(1), (m.group(2) or "").strip()
        if kind and kind not in MORPH_KINDS:
            P.err(line, f"„{k}”: ismeretlen szóelem-fajta „{kind}” (lehet: {', '.join(MORPH_KINDS)})."); return None
        if not kind:
            if j:
                P.err(line, f"„{k}”: a(z) „{form}” fajtáját írd mögé zárójelben ({', '.join(MORPH_KINDS)})."); return None
            kind = "tő"
        alt = [a.strip().lstrip("-") for a in form.split("/")]
        if any(not re.fullmatch(r"[^\W\d_]+", a) for a in alt):
            P.err(line, f"„{k}”: a(z) „{form}” szóelemben csak betű állhat (változat: -ban/-ben)."); return None
        part = {"s": "/".join(alt), "k": kind}
        if len(alt) > 1:
            part["alt"] = alt
        parts.append(part)
    if len(parts) > 1 and any("alt" in p for p in parts):
        P.err(line, f"„{k}”: szóban a toldalék megvalósult alakját írd (kert + ben (rag)); a változatlistát (-ban/-ben) "
                    "külön adatként add meg."); return None
    if len(parts) > 1 and parts[0]["k"] not in ("tő", "előtag"):
        P.err(line, f"„{k}” = {s}: a szó tővel (vagy előtaggal) kezdődjön."); return None
    flex = any(re.search(r"\bingadozó\b", t) for t in ctx.get("cmt", {}).get(line, []))
    rank, base = 0, ""
    for p in parts:
        if p["k"] in ("tő", "előtag"):
            rank, base = 0, p["s"]; continue
        r = MORPH_RANK.get(p["k"], rank)
        if rank == 3 and r < 3:
            P.err(line, f"„{k}” = {s}: rag után nem jöhet {p['k']} („{p['s']}”).")
        elif rank == 2 and r == 1:
            P.warn(line, f"„{k}” = {s}: jel után képző („{p['s']}”)? Ellenőrizd a sorrendet.")
        rank = max(rank, r)
        if p["k"] == "kötőhangzó" and not (len(p["s"]) == 1 and p["s"] in HU_VOWELS):
            P.warn(line, f"„{k}”: a kötőhangzó egyetlen magánhangzó (a, e, o, ö), nem „{p['s']}”.")
        hb, hs = harmony(base), suffix_harmony(p["s"])
        if hb and hs and hb != hs and not flex and len(parts) > 1:
            P.warn(line, f"„{k}”: a(z) „{p['s']}” ({p['k']}) {hs} hangrendű, a(z) „{base}” {hb} – illeszkedik? "
                         "(ha a szó ingadozó vagy kivétel, írd a sor végére: <!-- ingadozó -->)")
        base += p["s"]
    if len(parts) > 1:
        text = "".join(p["s"] for p in parts)
    elif parts[0]["k"] in ("tő", "előtag"):
        text = parts[0]["s"]
    else:                                              # önálló toldalék: -ban/-ben, -ság
        text = "/".join("-" + a for a in parts[0].get("alt", [parts[0]["s"]]))
    return {"t": "morph", "parts": parts}, text, False


IPA_LIKE = re.compile(r"[ːˈˌəɛɔøœʏɑɒæɪʊʃʒɲɟçŋθðɡχʁɾɫʔ]")


def parse_pron(s, line, P, k, want, ctx):
    """„kútba [kúdba]” → {t: pron, w: 'kútba', p: 'kúdba', s: 'kútba [kúdba]'}: írás + ejtés a betűk szerint."""
    m = re.fullmatch(r"(.+?)\s*\[([^\[\]]+)\]", s)
    if not m:
        P.err(line, f"„{k}” = {s}: az ejtést szögletes zárójelbe írd az írott alak után: kútba [kúdba]."); return None
    w, p = m.group(1).strip(), m.group(2).strip()
    if w == p:
        P.warn(line, f"„{k}”: az írás és az ejtés azonos ({w}) – szándékos?")
    if IPA_LIKE.search(p):
        P.warn(line, f"„{k}”: az ejtést a magyar betűk szerint írd, IPA-jelek nélkül ({p}).")
    return {"t": "pron", "w": w, "p": p}, f"{w} [{p}]", False


def parse_rel(s, line, P, k, want, ctx):
    """„Gergely – Éva: szerelem (I–V)” → {t: rel, a, b, kind, from, to, fi, ti, s}. A fajta zárt listából; a
    szereplők és az egységek a spec "rel": {"people": […], "units": […]} listájából (ha megadja)."""
    m = re.fullmatch(r"(.+?)\s+([–—-])\s+(.+?)\s*:\s*([^\s()]+)\s*(?:\(([^()]*)\))?", s)
    if not m:
        P.err(line, f"„{k}” = {s}: formátum: Gergely – Éva: szerelem (I–V)."); return None
    a, dash, b, kind, span = (x.strip() if x else x for x in m.groups())
    if dash == "-":
        P.warn(line, f"„{k}”: a két szereplő közé nagykötőjel (–) kell, szóközökkel.")
    if kind not in REL_KINDS:
        P.err(line, f"„{k}”: ismeretlen kapcsolat „{kind}” (lehet: {', '.join(REL_KINDS)})."); return None
    if a == b:
        P.err(line, f"„{k}”: a két szereplő ugyanaz ({a})."); return None
    rel = ctx.get("rel", {})
    people, units = want.get("people", rel.get("people")), want.get("units", rel.get("units"))
    if people is not None:
        for x in (a, b):
            if x not in people:
                P.err(line, f"„{k}”: ismeretlen szereplő „{x}” (a lecke szereplői: {', '.join(people)})."); return None
    item = {"t": "rel", "a": a, "b": b, "kind": kind}
    text = f"{a} – {b}: {kind}"
    if span:
        ends = [x.strip() for x in re.split(r"\s*[–—]\s*", span)]
        if len(ends) == 1 and units is None and re.fullmatch(r"[IVXLC]+-[IVXLC]+", span):
            ends = span.split("-")
            P.warn(line, f"„{k}”: a tartományba nagykötőjel (–) kell: {ends[0]}–{ends[1]}.")
        if len(ends) > 2 or not all(ends):
            P.err(line, f"„{k}” = {s}: az időszak formátuma (I–V) vagy (III)."); return None
        fr, to = ends[0], ends[-1]
        if units is not None:
            bad = [x for x in (fr, to) if x not in units]
            if bad:
                P.err(line, f"„{k}”: ismeretlen egység „{bad[0]}” (a lecke egységei: {', '.join(map(str, units))})."); return None
            fi, ti = units.index(fr), units.index(to)
        else:
            fi, ti = (roman_val(fr) if roman_val(fr) else int(fr) if fr.isdigit() else None), \
                     (roman_val(to) if roman_val(to) else int(to) if to.isdigit() else None)
            if fi is None or ti is None:
                P.err(line, f"„{k}”: „{span}”: római vagy arab szám kell, vagy add meg a spec „rel.units” listáját."); return None
        if fi > ti:
            P.err(line, f"„{k}” = {s}: az időszak eleje ({fr}) a vége ({to}) után van."); return None
        item.update({"from": fr, "to": to, "fi": fi, "ti": ti})
        text += f" ({fr}–{to})" if fr != to else f" ({fr})"
    return item, text, False


def quote_source(t, P, line, year):
    """A <!-- idézet: … --> forrásmegjegyzés ellenőrzése (szerzői jog: a † év + 70 < az idei év)."""
    t = re.sub(r"\s+", " ", t).strip()
    body = QUOTE_SRC.sub("", t).strip()
    folk, law = bool(re.search(r"népköltészet", body, re.I)), bool(re.search(r"jogszabály", body, re.I))
    if not re.search(r"\bszöveg\s*:", body, re.I):
        P.err(line, "az idézet forrásmegjegyzéséből hiányzik a kiadás: „· szöveg: <kiadás / MEK-szám / URL>”.")
    if re.search(r"\bvédett\b", body, re.I):
        P.err(line, "védett szöveget nem idézhetsz szó szerint – legfeljebb a címét és saját szavas összefoglalót.")
    deaths = [(role.lower() if role else "", int(y)) for role, y in DEATH_RE.findall(body)]
    if not deaths and not law and not folk:
        P.err(line, "az idézet forrásmegjegyzéséből hiányzik a szerző halálának éve: „· szerző † 1849”"
                    " (népköltészetnél „népköltészet · gyűjtő † 1898”, jogszabálynál „jogszabály”).")
    if folk and not any(r in ("gyűjtő", "lejegyző", "kiadó", "szerkesztő") for r, _ in deaths):
        P.err(line, "népköltészetnél a közkincs gyűjtés/kiadás kell: „· gyűjtő † <év>” (pl. Arany László † 1898).")
    for role, y in deaths:
        if y + 70 >= year:
            P.err(line, f"{role or 'szerző'} † {y}: a szöveg védett ({y + 71}. január 1-jétől közkincs) – szó szerint nem "
                        "idézhető, legfeljebb a cím és saját szavas összefoglaló (Szjt. 31. §).")
    return body


def build_quotes(md_path, doc, spec, P, ctx):
    """### Idézet blokkok → content.quotes {kulcs: {s, syl, v, cut, ci, ref}} + content.quoteSrc [forrás]."""
    lines = doc["_lines"]
    com = md_comments(md_path)
    year = datetime.date.today().year
    yv = frozenset(w.lower() for w in spec["yVowel"])
    rules, sets = spec["quotes"], spec["quoteSets"]
    quotes, srcs = {}, []
    for blk in doc["quoteBlocks"]:
        lo = blk["line"] - 1
        while lo >= 1 and not lines[lo - 1].strip():
            lo -= 1
        hi = blk["keys"][0][1] if blk["keys"] else blk["line"] + 1
        cand = [(ln, t) for ln, t in com if lo < ln < hi and QUOTE_SRC.match(t)]
        if not cand:
            P.err(blk["line"], "az ### Idézet előtt kötelező a forrásmegjegyzés: <!-- idézet: <szerző>: <mű> (<év>), <hely> · "
                               "szöveg: <kiadás> · szerző † <év> · közkincs -->")
            ref = None
        else:
            srcs.append(quote_source(cand[-1][1], P, cand[-1][0], year))
            ref = len(srcs) - 1
        pos = {}
        for k, n in blk["keys"]:
            raw = doc["items"][k][1]
            if not raw:
                P.err(n, f"„{k}”: üres idézetsor."); continue
            grp = max((g for g in sets if k == g or k.startswith(g + " ")), key=len, default=None)
            if k not in rules and grp is None:
                P.err(n, f"„{k}”: fölösleges idézet — a lecke nem használja (a spec „quotes” / „quoteSets” listájában nincs)."); continue
            rule = dict(sets.get(grp) or {}, **(rules.get(k) or {}))
            j = pos[grp] = pos.get(grp, -1) + 1
            pieces = re.split(r"(?<!\\)\|", raw)
            text, ci = "", []
            for i, pc in enumerate(pieces):
                pc = pc.replace("\\|", "|")
                if i:
                    gap = text.endswith(" ") or pc.startswith(" ")
                    text = text.rstrip() + (" " if gap else "")
                    ci.append(len(text))
                    pc = pc.lstrip()
                text += pc
            text = text.strip()
            v = hu_vowels(text, yv)
            cut = [sum(1 for x in v if x < c) for c in ci]
            notes = ctx["cmt"].get(n, [])
            dev = [t for t in notes if re.match(r"\s*(szótagszám|eltérés)\s*:", t, re.I)]
            want_syl = rule.get("syll")
            if isinstance(want_syl, list):
                want_syl = want_syl[j % len(want_syl)] if want_syl else None
            if want_syl is not None and len(v) != want_syl:
                said = [int(m.group(1)) for t in dev for m in [re.match(r"\s*szótagszám\s*:\s*(\d+)", t, re.I)] if m]
                if said and said[0] != len(v):
                    P.err(n, f"„{k}”: a megjegyzés szerint {said[0]} szótag, a build {len(v)}-et számolt (magánhangzók: "
                             f"{' '.join(text[x] for x in v)}).")
                elif dev:
                    P.warn(n, f"„{k}”: {len(v)} szótag ({want_syl} helyett) – a megjegyzés szerint szándékos/forráshű.")
                else:
                    P.err(n, f"„{k}”: {len(v)} szótag, {want_syl} kellene (magánhangzók: {' '.join(text[x] for x in v)}). "
                             "Ha a forrásban is így van: <!-- szótagszám: N, a forrásban is --> a sor végére.")
            want_cut = rule.get("cut")
            if want_cut is not None and ci:
                wc = want_cut if isinstance(want_cut, list) else [want_cut]
                if cut != wc:
                    (P.warn if dev else P.err)(n, f"„{k}”: a sormetszet (|) {', '.join(map(str, cut))}. szótag után van, "
                                                  f"{', '.join(map(str, wc))} kellene" + (" – a megjegyzés szerint szándékos." if dev else
                                                  " (ha szándékos: <!-- eltérés: … -->)."))
            q = {"s": text, "syl": len(v), "v": v}
            if ci:
                q.update({"cut": cut, "ci": ci})
            if ref is not None:
                q["ref"] = ref
            quotes[k] = q
    for k in rules:
        if k not in quotes and k not in doc["items"]:
            P.err(0, f"hiányzó idézet: „- {k}: …” (### Idézet alá)")
    for g, r in sets.items():
        n_ = sum(1 for k in quotes if k == g or k.startswith(g + " "))
        if "lines" in r and n_ != r["lines"]:
            P.err(0, f"a(z) „{g}” idézetcsoportban {n_} sor van, a lecke {r['lines']}-et vár.")
        elif not n_ and not any(k == g or k.startswith(g + " ") for k in doc["items"]):
            P.err(0, f"hiányzó idézetcsoport: „- {g} …: …” (### Idézet alá)")
    return quotes, srcs


def parse_datum(k, raw, n, want, P, ctx=None):
    """Egy ### Adatok sor értéke → (adat-dict, formázott szöveg, panel-HTML vagy None) vagy None."""
    ctx = ctx or {}
    typ = want.get("type", "number")
    if typ not in TYPES:
        return None              # a spec hibáját a read_spec már jelezte
    if typ in HU_TYPES:          # szöveges adat: a „kb.”, „(2025)” jelzők itt nem értelmezhetők
        fn = {"metrum": parse_metrum, "rhyme": parse_rhyme, "morph": parse_morph, "pron": parse_pron, "rel": parse_rel}[typ]
        r = fn(raw.strip(), n, P, k, want, ctx)
        if not r:
            return None
        item, text, _ = r
        item["s"] = text
        return item, text, None
    s0, tags = split_tags(raw.strip())
    s, est = split_est(s0)
    est = est or tags.pop("est", False)
    chk = None
    html_ = None
    if typ == "number":
        r = parse_number_item(s, n, P, k, want)
        if not r:
            return None
        item, text, chk = r
    elif typ == "year":
        r = parse_year(s, n, P, k)
        if not r:
            return None
        item, text, korul = r
        est = est or korul
    else:
        fn = {"date": lambda: parse_date(s, n, P, k), "coord": lambda: parse_coord(s, n, P, k, want),
              "range": lambda: parse_range(s, n, P, k, want), "ago": lambda: parse_ago(s, n, P, k, want),
              "ratio": lambda: parse_ratio(s, n, P, k, want), "frac": lambda: parse_frac(s, n, P, k, want),
              "list": lambda: parse_list(s, n, P, k, want), "series": lambda: parse_series(s, n, P, k, want),
              "point": lambda: parse_point(s, n, P, k, want), "utc": lambda: parse_utc(s, n, P, k, want),
              "dataset": lambda: parse_dataset(s, n, P, k, want),
              "formula": lambda: parse_formula(s, n, P, k, want),
              "equation": lambda: parse_equation(s, n, P, k, want),
              "expr": lambda: parse_expr(s, n, P, k, want, ctx)}[typ]
        r = fn()
        if not r:
            return None
        item, text, _ = r
        html_ = item.pop("_html", None)
    if typ in ("number", "year", "range", "ago", "ratio", "frac", "list", "series"):
        if typ == "number":
            lo = hi = chk
        elif typ == "range" and "blo" in item:          # dim: a min/max az alapegységre vonatkozik
            lo, hi = item["blo"], item["bhi"]
        elif typ in ("range", "ago") and "lo" in item:
            lo, hi = item["lo"], item["hi"]
        elif typ in ("list", "series"):
            lo, hi = min(item["v" if typ == "list" else "y"]), max(item["v" if typ == "list" else "y"])
        elif typ == "ratio":
            lo = hi = item["v"]
        else:
            lo = hi = item["v"]
        if "min" in want and lo < want["min"] or "max" in want and hi > want["max"]:
            P.err(n, f"„{k}” = {raw}: kívül esik az értelmes tartományon ({want.get('min', '…')} – {want.get('max', '…')}).")
    if typ == "frac" and html_ is None:
        html_ = mx_html(Mx(frac=True).text(text))
    if est:
        item["est"] = True
        item["s0"] = text
        text = "kb." + NB + text
        if html_:
            html_ = "kb." + NB + html_
    for t in ("yr", "upd", "proj", "model"):
        if t in tags:
            item[t] = tags[t]
    if tags.get("upd") and "yr" not in tags:
        P.warn(n, f"„{k}”: a „frissítendő” adat mellé írd az évét is: „(2025, frissítendő)”.")
    if typ != "number" or est:
        item["s"] = text
    if typ == "number" and tags and "s" not in item:
        item["s"] = text
    return item, item.get("s", text), html_


# ── Jelölés (matematika, kémia, minden tárgy) ─────────────────────────────────────────────
# A jelölés-elemző egy kis fát ad, ugyanazt, mint a shared/matek/mtext.js MatText.parse-a
# (közös próbaesetek: tools/tests/mx-cases.js). A fa csomópontjai:
#   "szöveg" · ["i", "x"] dőlt változó · ["sup", [...]] · ["sub", [...]] · ["frac", [számláló], [nevező]]
#   ["sqrt", [...]] · ["mx", [...]] képletszakasz (`…`)
SUB_IN = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
SUP_IN = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "0123456789+−")
SUB_OUT = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP_OUT = str.maketrans("0123456789+−-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻")
ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se
  Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb
  Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg
  Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og""".split())
# kémiai módban sem képlet (vitamin, hegy, papírméret…); a „\” előtag is letiltja: \B12
CHEM_EXCEPT = {"B1", "B2", "B3", "B5", "B6", "B7", "B9", "B12", "C3", "C4", "K2", "V1", "V2", "U2", "A3", "A4", "A5",
               "PM10", "PM2", "N1", "S1", "S2"}
MATH_OPS = [("<=>", "⇔"), ("|->", "↦"), ("<=", "≤"), (">=", "≥"), ("!=", "≠"), ("~=", "≈"), ("->", "→"),
            ("=>", "⇒"), ("+-", "±")]
FUNCS = {"sin", "cos", "tg", "ctg", "tan", "cot", "log", "lg", "ln", "lim", "max", "min", "sgn", "lnko", "lkkt",
         "mod", "exp", "abs"}
NAMED = {"pi": "π", "inf": "∞", "NN": "ℕ", "ZZ": "ℤ", "QQ": "ℚ", "RR": "ℝ"}
LET = "A-Za-zÀ-ÖØ-öø-žΑ-Ωα-ω"
IS_LET = re.compile(f"[{LET}]")
IS_WORD = re.compile(f"[{LET}0-9_]")
CHEM_RE = re.compile(r"(?:[A-Z][a-z]?\d*|\((?:[A-Z][a-z]?\d*)+\)\d*)+")
CHEM_PART = re.compile(r"([A-Z][a-z]?|[()])(\d*)")
FRAC_RE = re.compile(r"(\d+)/(\d+)(?![0-9/]|,\d)")
EXP_RE = re.compile(r"\^([−-]?)(\d+(?:,\d+)?|[A-Za-zα-ω])")
CHARGE_RE = re.compile(r"\^(\d*[+\-−])(?![\w(])")
# képletben a görög kisbetű változó → dőlt (mint a latin); a nagybetű (Δ, Σ, Ω) és a π álló
GREEK = re.compile("[Α-Ωα-ωϑϕϵ]")
MATH_WORD = re.compile("[A-Za-zÀ-ÖØ-öø-ž]+")
PRIMES = re.compile("[′″‴]*")  # a változó vesszője vele együtt dőlt: γ′, f″
# Mértékegység a képletben (ISO 80000: álló betű). Csak SZÁM UTÁN álló egység számít egységnek – a betű különben
# változó (m: tömeg, s: út, V: térfogat …). Egybetűs egység csak szóközzel: „5 m”, „2m” = 2 · m; többbetűs
# szóköz nélkül is: „5cm”. Szám = számjegyre végződő szöveg, vagy hatvány (3 · 10^8 m/s). Az egység után
# „/” vagy „·” és egy újabb egység folytatja (m/s, km/h, N·m), a kitevő is (m^2, m/s^2). °C, °F mindig álló.
# Explicit jelölés: "…" a képletben – az idézőjelek közti szöveg álló marad ("cm", "max").
# Szándékosan nincs benne: t (tonna – idő), a (ár – változó).
UNITS = set("""nm µm mm cm dm m km mg g dkg kg s ms h perc l ml cl dl hl N kN J kJ MJ W kW MW Wh kWh Pa kPa hPa MPa
  bar V mV kV A mA K Hz kHz MHz mol cal kcal ha lx dB""".split())
UNIT_WORD = re.compile("[µμ]?[A-Za-z]+")


def is_var(t):
    """Egy betűs változó: latin vagy görög kisbetű (nem π) → dőlt."""
    return bool(IS_LET.fullmatch(t) and not re.fullmatch("[Α-Ωπ]", t) or re.fullmatch("[ϑϕϵ]", t))


def match_close(s, i, op="(", cl=")"):
    """s[i] == op → a párja indexe, vagy -1."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "\\":
            continue
        if s[j] == op:
            depth += 1
        elif s[j] == cl:
            depth -= 1
            if depth == 0:
                return j
    return -1


def split_top(s, ch="/"):
    """Az első, zárójelen kívüli ch mentén kettévág (None, ha nincs)."""
    depth = 0
    for j, c in enumerate(s):
        if c in "([":
            depth += 1
        elif c in ")]":
            depth -= 1
        elif c == ch and depth == 0 and (j == 0 or s[j - 1] != "\\"):
            return s[:j], s[j + 1:]
    return None


class Mx:
    """Jelölés-elemző. frac: a 3/4 számjegyes tört állóvá válik (matematikalecke);
    chem: H2O, Na^+, -> és a Unicode-indexek kémiai jelölése (kémialecke)."""

    def __init__(self, frac=False, chem=False):
        self.frac, self.chem = frac, chem
        self.errors, self.conv = [], []

    @staticmethod
    def push(out, x):
        if isinstance(x, str):
            if not x:
                return
            if out and isinstance(out[-1], str):
                out[-1] += x
                return
        out.append(x)

    def text(self, s):
        return self.seq(s, math=False)

    def math(self, s, big=False):
        return self.seq(s, math=True, big=big)

    @staticmethod
    def after_number(out):
        """Számra végződik-e az eddigi kimenet (szöveg számjeggyel a végén, vagy szám^kitevő)?"""
        k = len(out) - 1
        if k >= 0 and isinstance(out[k], str):
            if out[k].strip():
                return bool(re.search(r"\d\s*$", out[k]))
            k -= 1                                     # 10^8 után álló szóköz
        return (k > 0 and out[k][0] == "sup" and all(isinstance(x, str) for x in out[k][1])
                and isinstance(out[k - 1], str) and bool(re.search(r"\d$", out[k - 1])))

    def seq(self, s, math, big=False):
        out, i, n = [], 0, len(s)
        P = self.push
        unit_end = -1                  # az utolsó mértékegység vége (a folytatáshoz: m/s, m^2)
        while i < n:
            c = s[i]
            prev = s[i - 1] if i else ""
            if c == "\\" and i + 1 < n:
                P(out, s[i + 1]); i += 2; continue
            if c == "`":
                j = s.find("`", i + 1)
                while j > 0 and s[j - 1] == "\\":
                    j = s.find("`", j + 1)
                if j < 0:
                    self.errors.append("lezáratlan ` (a képletszakasz végéről hiányzik a ` jel)")
                    P(out, s[i + 1:]); break
                out.append(["mx", self.math(s[i + 1:j])]); i = j + 1; continue
            if s.startswith("[[", i):
                j = s.find("]]", i + 2)
                parts = split_top(s[i + 2:j]) if j > 0 else None
                if j < 0 or not parts:
                    self.errors.append("[[…]]: " + ("hiányzik a ]]" if j < 0 else "hiányzik a törtvonal (/), pl. [[x/2]]"))
                    P(out, s[i:j + 2] if j > 0 else s[i:]); i = j + 2 if j > 0 else n; continue
                out.append(["frac", self.math(parts[0].strip()), self.math(parts[1].strip())]); i = j + 2; continue
            if c == "^" and out:
                if s.startswith("^(", i):
                    j = match_close(s, i + 1)
                    if j > 0:
                        out.append(["sup", self.seq(s[i + 2:j], math)]); i = j + 1; continue
                m = CHARGE_RE.match(s, i)
                if m:
                    out.append(["sup", [m.group(1).replace("-", "−")]]); i = m.end(); continue
                m = EXP_RE.match(s, i)
                if m:
                    sign, tok = m.groups()
                    inner = ["−"] if sign else []
                    if math and is_var(tok):
                        inner.append(["i", tok])
                    else:
                        self.push(inner, tok)
                    out.append(["sup", inner])
                    if i == unit_end:
                        unit_end = m.end()
                    i = m.end(); continue
            if c == "_" and i + 1 < n and (IS_LET.match(prev) or math and (prev.isdigit() or prev == ")")):
                if s[i + 1] == "(":
                    j = match_close(s, i + 1)
                    if j > 0:
                        out.append(["sub", self.seq(s[i + 2:j], math)]); i = j + 1; continue
                m = re.compile(r"\d+|[" + LET + r"]+").match(s, i + 1)
                if m:
                    t = m.group(0)
                    out.append(["sub", [["i", t]] if math and len(t) == 1 and is_var(t) else [t]])
                    i = m.end(); continue
            if (math or self.frac) and (c == "√" or math and s.startswith("gyök(", i)):
                k = i + (1 if c == "√" else 4)
                if k < n and s[k] == "(":
                    j = match_close(s, k)
                    if j > 0:
                        out.append(["sqrt", self.seq(s[k + 1:j], True)]); i = j + 1; continue
                m = re.compile(r"\d+(?:,\d+)?|[A-Za-zα-ω]").match(s, k) if c == "√" else None
                if m:
                    t = m.group(0)
                    out.append(["sqrt", [["i", t]] if math and is_var(t) else [t]]); i = m.end(); continue
            if (math or self.frac) and c.isdigit() and not (IS_WORD.match(prev) or prev and prev in ",./"):
                m = FRAC_RE.match(s, i)
                if m and not (i + len(m.group(0)) < n and IS_LET.match(s[i + len(m.group(0))])):
                    a, b = m.groups()
                    if out and isinstance(out[-1], str):
                        mm = re.search(r"(?:^|[^\w,])(\d+) $", out[-1])
                        if mm and int(a) < int(b):
                            out[-1] = out[-1][:-1]
                    out.append(["frac", [a], [b]]); i = m.end(); continue
            if self.chem and not math:
                if (c.isupper() or c == "(") and not (IS_WORD.match(prev) or prev == "\\"):
                    m = CHEM_RE.match(s, i)
                    if m and re.search(r"\d", m.group(0)) and not (m.end() < n and re.match(r"[a-záéíóöőúüű0-9]", s[m.end()])):
                        f = m.group(0)
                        syms = re.findall(r"[A-Z][a-z]?", f)
                        if f not in CHEM_EXCEPT and all(x in ELEMENTS for x in syms) and f.count("(") == f.count(")"):
                            for sym, num in CHEM_PART.findall(f):
                                P(out, sym)
                                if num:
                                    out.append(["sub", [num]])
                            self.conv.append(f)
                            i = m.end(); continue
                if c in "₀₁₂₃₄₅₆₇₈₉" and out:
                    m = re.compile("[₀₁₂₃₄₅₆₇₈₉]+").match(s, i)
                    out.append(["sub", [m.group(0).translate(SUB_IN)]]); i = m.end(); continue
                if c in "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻" and out:
                    m = re.compile("[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+").match(s, i)
                    if re.search("[⁺⁻]", m.group(0)):
                        out.append(["sup", [m.group(0).translate(SUP_IN)]]); i = m.end(); continue
                if s.startswith("->", i):
                    P(out, "→"); self.conv.append("->"); i += 2; continue
            if math:
                op = next((b for a, b in MATH_OPS if s.startswith(a, i)), None)
                if op:
                    P(out, op); i += len(next(a for a, b in MATH_OPS if b == op)); continue
                if c == "*":
                    if out and isinstance(out[-1], str):
                        out[-1] = out[-1].rstrip(" ")
                    P(out, " · "); i += 1
                    while i < n and s[i] == " ":
                        i += 1
                    continue
                if c == "-":
                    P(out, "−"); i += 1; continue
                if c == "(":
                    j = match_close(s, i)
                    if j < 0:
                        self.errors.append("páratlan zárójel a képletben: hiányzik egy „)”")
                        P(out, "("); i += 1; continue
                    inner = self.seq(s[i + 1:j], True, big)
                    m = re.compile(r"\s*/\s*\(").match(s, j + 1) if big else None
                    if m:
                        k = m.end() - 1
                        j2 = match_close(s, k)
                        if j2 > 0:
                            out.append(["frac", inner, self.seq(s[k + 1:j2], True, big)]); i = j2 + 1; continue
                    P(out, "(")
                    for x in inner:
                        P(out, x)
                    P(out, ")"); i = j + 1; continue
                if c == ")":
                    self.errors.append("páratlan zárójel a képletben: fölösleges „)”")
                    P(out, ")"); i += 1; continue
                if c == '"':
                    j = s.find('"', i + 1)
                    if j > 0:
                        P(out, s[i + 1:j]); i = unit_end = j + 1; continue
                if c == "°" and s[i + 1:i + 2] in ("C", "F") and not (i + 2 < n and IS_WORD.match(s[i + 2])):
                    P(out, s[i:i + 2]); i = unit_end = i + 2; continue
                m = UNIT_WORD.match(s, i)
                if m and m.group(0).replace("μ", "µ") in UNITS and not (m.end() < n and (IS_WORD.match(s[m.end()]) or s[m.end()] in "′″‴(")):
                    w = m.group(0)
                    cont = unit_end >= 0 and s[unit_end:i].strip() in ("/", "·", "*")
                    if cont or self.after_number(out) and (len(w) > 1 or prev == " "):
                        P(out, w.replace("μ", "µ")); i = unit_end = m.end(); continue
                if GREEK.fullmatch(c):
                    if not is_var(c):
                        P(out, c); i += 1; continue
                    t = c + PRIMES.match(s, i + 1).group(0)
                    out.append(["i", t]); i += len(t); continue
                m = MATH_WORD.match(s, i)
                if m:
                    w = m.group(0)
                    if w in NAMED:
                        P(out, NAMED[w])
                    elif not re.fullmatch(r"[A-Za-z]+", w) or w in FUNCS:
                        P(out, w)
                    else:
                        w += PRIMES.match(s, m.end()).group(0)
                        out.append(["i", w])
                    i = m.start() + len(w); continue
            P(out, c); i += 1
        return out


def mx_html(nodes, esc=True):
    e = (lambda t: H.escape(t, quote=False)) if esc else (lambda t: t)
    out = []
    for x in nodes:
        if isinstance(x, str):
            out.append(e(x)); continue
        t = x[0]
        if t == "i":
            out.append(f"<i>{e(x[1])}</i>")
        elif t in ("sup", "sub"):
            out.append(f"<{t}>{mx_html(x[1], esc)}</{t}>")
        elif t == "frac":
            out.append(f'<span class="frac"><span class="fn">{mx_html(x[1], esc)}</span><span class="fs">/</span>'
                       f'<span class="fd">{mx_html(x[2], esc)}</span></span>')
        elif t == "sqrt":
            inner = mx_html(x[1], esc)
            if vis_len(x[1]) > 1:
                inner = '<span class="rp">(</span>' + inner + '<span class="rp">)</span>'
            out.append(f'<span class="rt">√<span class="rad">{inner}</span></span>')
        elif t == "mx":
            out.append(f'<span class="mx">{nobreak(mx_html(x[1], esc))}</span>')
    return "".join(out)


REL_BREAK = re.compile(r"(?<![=≤≥≠≈⇒⇔→↦])(?<!&lt;)(?<!&gt;) ")


def nobreak(h):
    """Képlet a panelen: a szóközök nem törő szóközzé válnak (a képlet egyben marad), kivéve a relációjel
    (= < > ≤ ≥ ≠ ≈ ⇒ ⇔ → ↦) utánit – egy túl hosszú képlet ott törhet (mint a nyomdai szedésben).
    Csak a HTML-tageken kívüli szöveget érinti."""
    parts = re.split(r"(<[^>]+>)", h)
    for i in range(0, len(parts), 2):
        parts[i] = REL_BREAK.sub(NB, parts[i])
    return "".join(parts)


def vis_len(nodes):
    """Látható hossz (karakterben, közelítő): a tört max(számláló, nevező) + 1."""
    n = 0
    for x in nodes:
        if isinstance(x, str):
            n += len(x)
        elif x[0] == "i":
            n += len(x[1])
        elif x[0] == "frac":
            n += max(vis_len(x[1]), vis_len(x[2])) + 1
        elif x[0] == "sqrt":
            n += 1 + vis_len(x[1])
        else:
            n += vis_len(x[1])
    return n


def mx_unicode(nodes):
    """Fa → Unicode-szöveg (kémiai feliratokhoz: H₂O, Na⁺); None, ha nem írható át."""
    out = []
    for x in nodes:
        if isinstance(x, str):
            out.append(x)
        elif x[0] == "i":
            out.append(x[1])
        elif x[0] in ("sub", "sup") and all(isinstance(y, str) for y in x[1]):
            t = "".join(x[1])
            if not re.fullmatch(r"[0-9]+" if x[0] == "sub" else r"[0-9+−-]+", t):
                return None
            out.append(t.translate(SUB_OUT if x[0] == "sub" else SUP_OUT))
        elif x[0] == "mx":
            r = mx_unicode(x[1])
            if r is None:
                return None
            out.append(r)
        else:
            return None
    return "".join(out)


SUP_ALL = str.maketrans("0123456789+−-=()ni", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿⁱ")
SUB_ALL = str.maketrans("0123456789+−-=()", "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎")


def mx_plain(nodes):
    """Fa → sima szöveg (címhez, ahol nincs HTML): x², H₂O, Na⁺, √2, 3/4. Ami Unicode-dal nem írható
    (pl. betűs index: F_fel), az a .md-jelöléssel marad (F_fel, x^(n+1))."""
    out = []
    for x in nodes:
        if isinstance(x, str):
            out.append(x); continue
        t = x[0]
        if t == "i":
            out.append(x[1])
        elif t in ("sup", "sub"):
            inner = mx_plain(x[1])
            ok = re.fullmatch(r"[0-9+−\-=()ni]+" if t == "sup" else r"[0-9+−\-=()]+", inner)
            if ok:
                out.append(inner.translate(SUP_ALL if t == "sup" else SUB_ALL))
            else:
                mark = "^" if t == "sup" else "_"
                out.append(mark + (inner if re.fullmatch(r"\w+", inner) else "(" + inner + ")"))
        elif t == "frac":
            if out and out[-1][-1:].isdigit():
                out.append(" ")                   # vegyes szám: 2 1/3 (a fa a szóközt elnyeli)
            out.append(mx_plain(x[1]) + "/" + mx_plain(x[2]))
        elif t == "sqrt":
            inner = mx_plain(x[1])
            out.append("√" + (inner if vis_len(x[1]) <= 1 or re.fullmatch(r"[\w,]+", inner) else "(" + inner + ")"))
        elif t == "mx":
            out.append(mx_plain(x[1]))
    return "".join(out)


def has_script(nodes):
    """Van-e a fában felső/alsó index (bármilyen mélységben)."""
    return any(not isinstance(x, str) and (x[0] in ("sup", "sub") or has_script(x[1] if x[0] != "frac" else x[1] + x[2]))
               for x in nodes if not isinstance(x, str) and x[0] != "i")


def plain_title(title, line, P, ctx):
    """A # cím jelölése → sima Unicode-szöveg (a cím a panelen és a böngészőfülön textContent).
    Képlet `…`, x^2, Na^+, √(…) minden leckében; "chem": H2O → H₂O; "math": 3/4 marad 3/4."""
    if not title or not re.search(r"[`^_√]|->|[A-Z][a-z]?\d", title):
        return title
    mp = Mx(frac=bool(ctx.get("math")), chem=bool(ctx.get("chem")))
    t = mx_plain(mp.text(title))
    for e in mp.errors:
        P.err(line, f"cím: {e}")
    if t != title:
        P.info(line, f"cím: {title} → {t}")
    return t


MATH_WARN = [
    (re.compile(r"\d\s*[*×]\s*\d|\d\s+x\s+\d"), "szorzásjelnek ·-ot írj (3 · 4), vagy tedd a képletet ` ` közé."),
    (re.compile(r"÷"), "osztásjelnek :-ot írj (12 : 3)."),
    (re.compile(r"(?:^|[\s(])-(?=\s*\d)|\s-\s"), "kötőjel helyett valódi mínuszjelet (−) írj, vagy tedd a képletet ` ` közé."),
    (re.compile(r"\d\.\d"), "tizedespont? A magyar írásmód tizedesvessző (3,14)."),
    (re.compile(r"\d'"), "szögpercnek ′ jelet írj (30′), ne aposztrófot."),
    (re.compile(r"\(\s*[−\-]?\d+(?:,\d+)?\s*,\s+[−\-]?\d"), "pont koordinátáit pontosvesszővel válaszd el: P(3; −2)."),
    (re.compile(r"(?<![\w^])(?:mm|cm|dm|m|km)\^?[23]\b"), "mértékegység kitevővel: m², cm³ (nem m2, cm^2)."),
]


def inline(text, line, P, data_fmt, ctx=None, fx=False):
    """Tanárbarát jelölés → HTML. **félkövér**, *dőlt*, ==színnel kiemelt==, F_fel → alsó index, {adatkulcs} → az adat
    értéke, `képlet`, x^2, [[a/b]], {1; 2; 3} halmaz; matematika- és kémialeckében a tantárgyi jelölés is."""
    ctx = ctx or {}
    math_, chem = ctx.get("math"), ctx.get("chem")
    data_html = ctx.get("html", {})
    keys = list(data_fmt)
    s = text.replace("\\{", "\x01").replace("\\}", "\x02")

    def sub_ph(m):
        k = m.group(1).strip()
        if k in data_fmt:
            return "\x00" + chr(0xE000 + keys.index(k)) + "\x00"
        if ";" in k or not k:                 # halmaz: {1; 2; 3}, { }
            return "\x01" + m.group(1) + "\x02"
        P.err(line, f"{{{k}}}: nincs ilyen adat az ### Adatok listákban." +
              (" (Halmazt pontosvesszővel írj: {1; 2; 3}.)" if math_ else ""))
        return k
    s = re.sub(r"\{([^{}]*)\}", sub_ph, s)
    store = []

    def put(h):
        store.append(h)
        return "\x03" + chr(0xE000 + len(store) - 1) + "\x03"

    def sub_mx(src, big=False):
        mp = Mx(frac=math_)
        tree = mp.math(src, big)
        for e in mp.errors:
            P.err(line, e)
        return put('<span class="mx">' + nobreak(mx_html(tree)) + "</span>")
    if fx and math_:
        s = sub_mx(s, big=True)
    else:
        if math_:
            for rx, msg in MATH_WARN:
                if rx.search(re.sub(r"(?<!\\)`(?:\\`|[^`])*`", " ", s)):
                    P.warn(line, msg)
        s = re.sub(r"(?<!\\)`((?:\\`|[^`])*)`", lambda m: sub_mx(m.group(1)), s)
        if chem:
            s = s.replace("->", "→")
        if re.search(r"(?<!\\)`", s):
            P.err(line, "lezáratlan ` (a képletszakasz végéről hiányzik a ` jel).")
    s = H.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", s)
    s = re.sub(r"==(.+?)==", r'<span class="key">\1</span>', s)
    # tantárgyi jelölés a sima szövegen (a HTML-tagek érintetlenek): alsó/felső index, tört, kémiai képlet
    mp = Mx(frac=math_, chem=chem)
    parts = re.split(r"(<[^>]+>)", s)
    for i in range(0, len(parts), 2):
        if parts[i]:
            parts[i] = mx_html(mp.text(parts[i]), esc=False)
    s = "".join(parts)
    for e in mp.errors:
        P.err(line, e)
    for f in dict.fromkeys(mp.conv):
        if f != "->" and f not in ctx.setdefault("seen", set()):
            ctx["seen"].add(f)
            P.info(line, f"{f} → {mx_unicode(Mx(chem=True).text(f))}")
    s = re.sub("\x03(.)\x03", lambda m: store[ord(m.group(1)) - 0xE000], s)
    s = re.sub("\x00(.)\x00", lambda m: data_html.get(keys[ord(m.group(1)) - 0xE000]) or
               H.escape(data_fmt[keys[ord(m.group(1)) - 0xE000]]), s)
    s = s.replace("\x01", "{").replace("\x02", "}")
    if re.search(r"\*|==", s):
        P.warn(line, "lezáratlan * vagy == jelölés a szövegben.")
    return s


def plain(s):
    return re.sub(r"\*\*|==|(?<!\w)\*|\*(?!\w)", "", s)


def count_words(t, ctx, fx=False):
    """Panelszöveg szavai. Képletszakasz (`…`) = 1 szó; matematikában a tört és a hatvány is 1 szó,
    a `képlet:` sor matematika- és kémialeckében 3 szó."""
    if fx and (ctx.get("math") or ctx.get("chem")):
        return 3
    t = re.sub(r"(?<!\\)`(?:\\`|[^`])*`", "X", t)
    t = re.sub(r"\[\[.*?\]\]", "X", t)
    if ctx.get("math"):
        t = re.sub(r"(?<![\w,])\d+(?: \d+)?/\d+", "X", t)
        t = re.sub(r"[\w)]+\^(?:\([^)]*\)|[−\-]?\w+)", "X", t)
    return len(re.findall(r"[\wÀ-ž]+(?:[-–][\wÀ-ž]+)*", plain(re.sub(r"\{[^{}]+\}", "X", t))))


def read_spec(html_path, P):
    if not html_path.exists():
        P.err(0, f"nincs párja: {html_path.name} (a .md mellett azonos nevű .html kell)")
        return None
    m = re.search(r'<script[^>]*id="lesson-spec"[^>]*>(.*?)</script>', html_path.read_text(encoding="utf-8"), re.S)
    if not m:
        P.err(0, f"{html_path.name}: nincs <script type=\"application/json\" id=\"lesson-spec\"> blokk")
        return None
    try:
        spec = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        P.err(0, f"{html_path.name}: a lesson-spec nem érvényes JSON: {e}")
        return None
    labels = spec.get("labels", {})
    if isinstance(labels, list):
        labels = {k: None for k in labels}
    data = {k: (v if isinstance(v, dict) else {"unit": v}) for k, v in spec.get("data", {}).items()}
    for k, v in data.items():
        if v.get("type", "number") not in TYPES:
            P.err(0, f"{html_path.name}: „{k}”: ismeretlen adattípus „{v.get('type')}” (lehet: {', '.join(TYPES)}).")
    mw = spec.get("maxWords", MAX_WORDS)
    if not isinstance(mw, int) or mw < 1:
        P.err(0, f"{html_path.name}: a maxWords pozitív egész szám legyen."); mw = MAX_WORDS
    if spec.get("math") and spec.get("chem"):
        P.err(0, f"{html_path.name}: a \"math\" és a \"chem\" közül legfeljebb az egyik lehet true.")
    rv = spec.get("review", [])
    if not isinstance(rv, list):
        P.err(0, f"{html_path.name}: a \"review\" lista legyen, pl. [\"elsősegély\"]."); rv = []
    hu = {}
    for key, kind in (("quotes", dict), ("quoteSets", dict), ("yVowel", list), ("rel", dict)):
        v = spec.get(key, kind())
        if isinstance(v, list) and key == "quotes":
            v = {k: {} for k in v}
        if not isinstance(v, kind):
            P.err(0, f"{html_path.name}: a \"{key}\" {'lista' if kind is list else 'objektum'} legyen."); v = kind()
        hu[key] = v
    return {"steps": spec.get("steps"), "labels": labels, "data": data, "maxWords": mw,
            "math": bool(spec.get("math")), "chem": bool(spec.get("chem")),
            "sources": bool(spec.get("sources")), "review": rv, "interpretive": bool(spec.get("interpretive")), **hu}


def parse_md(path, P):
    lines = path.read_text(encoding="utf-8").split("\n")
    # HTML-megjegyzések (<!-- … -->) kiszűrése, a sorszámok megtartásával
    in_c = False
    for i, l in enumerate(lines):
        out, rest = "", l
        while rest:
            if in_c:
                j = rest.find("-->")
                if j < 0:
                    rest = ""
                else:
                    rest, in_c = rest[j + 3:], False
            else:
                j = rest.find("<!--")
                if j < 0:
                    out, rest = out + rest, ""
                else:
                    out, rest, in_c = out + rest[:j], rest[j + 4:], True
        lines[i] = out.rstrip()

    doc = {"title": None, "titleLine": 0, "meta": {}, "steps": [], "items": {}, "bareNotes": [], "quoteBlocks": [],
           "_lines": lines}
    sec = None          # None | 'common' | step dict
    sub = None          # None | 'labels' | 'data'
    para = []           # [(line, text)]

    def flush():
        nonlocal para
        if para and isinstance(sec, dict):
            sec["blocks"].append(("p", para[0][0], " ".join(t for _, t in para)))
        para = []

    for n, raw in enumerate(lines, 1):
        l = raw.strip()
        if not l:
            flush(); continue
        if l.startswith("# ") and not l.startswith("## "):
            if doc["title"]:
                P.err(n, "csak egy „# Cím” sor lehet.")
            doc["title"], doc["titleLine"] = l[2:].strip(), n
            continue
        if doc["title"] is None:
            P.err(n, "a fájl első sora a „# Cím” legyen.")
            doc["title"] = "?"
        if l.startswith("## "):
            flush(); sub = None
            h = l[3:].strip()
            if re.match(r"(?i)^közös\b", h):
                sec = "common"; continue
            m = re.match(r"^(\d+)\.\s+(.+)$", h)
            if not m:
                P.err(n, f"„## {h}”: lépéscím formátuma „## 3. Cím”, vagy „## Közös”.")
                sec = None; continue
            num = int(m.group(1))
            if num != len(doc["steps"]) + 1:
                P.err(n, f"a lépések sorszáma {len(doc['steps']) + 1} kellene legyen, nem {num}.")
            sec = {"title": m.group(2).strip(), "line": n, "blocks": []}
            doc["steps"].append(sec)
            continue
        if l.startswith("### "):
            flush()
            h = l[4:].strip().lower()
            if sec is None:
                P.err(n, "a ### szakasz egy ## lépés vagy a ## Közös alá tartozik.")
            sub = {"feliratok": "labels", "adatok": "data", "idézet": "quotes"}.get(h)
            if not sub:
                P.err(n, f"„### {l[4:].strip()}”: ismeretlen szakasz (lehet: ### Feliratok, ### Adatok, ### Idézet).")
            if sub == "quotes":
                doc["quoteBlocks"].append({"line": n, "keys": []})
            continue
        if sec is None and not doc["steps"] and not doc["meta"] and ":" in l:
            for part in re.split(r"\s+·\s+", l):
                k, _, v = part.partition(":")
                doc["meta"][k.strip().lower()] = v.strip()
            doc["metaLine"] = n
            continue
        if sub:
            m = re.match(r"^[-*]\s+([^:]+?)\s*:\s*(.*)$", l)
            if not m:
                P.err(n, f"a {({'labels': 'Feliratok', 'data': 'Adatok'}.get(sub, 'Idézet'))} alatt minden sor „- kulcs: érték” alakú legyen.")
                continue
            k, v = m.group(1).strip(), m.group(2).strip()
            if k in doc["items"]:
                P.err(n, f"„{k}” kulcs kétszer szerepel (először: {doc['items'][k][2]}. sor).")
                continue
            doc["items"][k] = (sub, v, n)
            if sub == "quotes":
                doc["quoteBlocks"][-1]["keys"].append((k, n))
            continue
        if sec == "common" or sec is None:
            P.err(n, "ide csak ### Feliratok / ### Adatok / ### Idézet kerülhet, folyó szöveg nem.")
            continue
        if l.startswith(">"):
            flush()
            if re.match(r"(?i)^>\s*értelmezés\s*:", l):
                sec["blocks"].append(("interp", n, re.sub(r"(?i)^>\s*értelmezés\s*:\s*", "", l))); continue
            if not re.match(r"(?i)^>\s*megjegyzés\s*:", l):
                doc["bareNotes"].append(n)
            t = re.sub(r"^>\s*(megjegyzés\s*:)?\s*", "", l, flags=re.I)
            sec["blocks"].append(("note", n, t)); continue
        if re.match(r"(?i)^képlet\s*:", l):
            flush(); sec["blocks"].append(("fx", n, l.split(":", 1)[1].strip())); continue
        if re.match(r"^[-*]\s+", l):
            flush(); sec["blocks"].append(("li", n, re.sub(r"^[-*]\s+", "", l))); continue
        para.append((n, l))
    flush()
    return doc


def md_comments(path):
    """[(kezdősor, szöveg)] a .md HTML-megjegyzéseiről."""
    text = path.read_text(encoding="utf-8")
    return [(text.count("\n", 0, m.start()) + 1, m.group(1)) for m in re.finditer(r"<!--(.*?)-->", text, re.S)]


def check_sources(md_path, doc, P):
    """"sources": true – minden adat mellett <!-- forrás: … --> (utána, ugyanabban a sorban, vagy blokkszinten
    <!-- forrás (az alábbiakra): … --> a szakasz elején)."""
    raw = md_path.read_text(encoding="utf-8").split("\n")
    com = md_comments(md_path)
    src_at = {ln for ln, t in com if re.match(r"\s*forrás\b", t, re.I)}
    block_at = {ln for ln, t in com if re.match(r"\s*forrás\s*\(az alábbiakra\)", t, re.I)}
    for k, (kind, v, n) in doc["items"].items():
        if kind != "data":
            continue
        ok = n in src_at
        j = n                                     # a következő nem üres sor egy forrás-megjegyzés?
        while not ok and j < len(raw) and not raw[j].strip():
            j += 1
        if not ok and j < len(raw) and (j + 1) in src_at and raw[j].lstrip().startswith("<!--"):
            ok = True
        j = n - 1                                 # blokkszintű megjegyzés a szakasz elején
        while not ok and j >= 1 and not raw[j - 1].lstrip().startswith("#"):
            if j in block_at:
                ok = True
            j -= 1
        if not ok:
            P.warn(n, f"„{k}”: hiányzik a forrás – írd utána: <!-- forrás: <hivatkozás>, lekérdezve: ÉÉÉÉ-HH-NN -->"
                      " (közismert adatnál: <!-- forrás: közismert -->).")


def build(md_path, check_only=False, out_dir=None):
    md_path = md_path.resolve()
    P = Problems(md_path)
    spec = read_spec(md_path.with_suffix(".html"), P)
    doc = parse_md(md_path, P)
    if spec is None:
        return P
    ctx = {"math": spec["math"], "chem": spec["chem"], "html": {}, "rel": spec["rel"]}
    quotes, quote_src = {}, []
    if doc["quoteBlocks"] or spec["quotes"] or spec["quoteSets"] or any(
            v.get("type") in HU_TYPES for v in spec["data"].values()):
        ctx["cmt"] = {}
        for ln, t in md_comments(md_path):
            ctx["cmt"].setdefault(ln, []).append(t)
        quotes, quote_src = build_quotes(md_path, doc, spec, P, ctx)     # 0) idézetek (a metrum/rím adat hivatkozik rájuk)
        ctx["quotes"] = quotes

    for k in ("tantárgy", "évfolyam", "témakör"):
        if k not in doc["meta"]:
            P.err(doc.get("metaLine", 2), f"a metaadat-sorból hiányzik: „{k}: …” (pl. tantárgy: Fizika · évfolyam: 7–8. · témakör: …)")

    labels, data, src, data_fmt = {}, {}, {}, {}
    # 1) adatok (először, hogy a {hivatkozások} feloldhatók legyenek)
    for k, (kind, v, n) in doc["items"].items():
        if kind != "data":
            continue
        src[k] = n
        if k not in spec["data"]:
            P.err(n, f"„{k}”: fölösleges adat — a lecke nem használja" + (" (felirat lenne?)" if k in spec["labels"] else "") + ".")
            continue
        r = parse_datum(k, v, n, spec["data"][k], P, ctx)
        if not r:
            data_fmt[k] = v      # a hibát már jeleztük; a {hivatkozás} ne okozzon újabbat
            continue
        data[k], data_fmt[k], h = r
        if h:
            ctx["html"][k] = h
    # 2) feliratok
    for k, (kind, v, n) in doc["items"].items():
        if kind != "labels":
            continue
        src[k] = n
        if k not in spec["labels"]:
            P.err(n, f"„{k}”: fölösleges felirat — a lecke nem használja" + (" (adat lenne?)" if k in spec["data"] else "") + ".")
            continue
        if not v:
            P.err(n, f"„{k}”: üres felirat."); continue

        def lab_ref(m):
            kk = m.group(1).strip()
            if kk in data_fmt:
                return data_fmt[kk]
            if ";" in kk or not kk:
                return m.group(0)
            P.err(n, f"{{{m.group(1)}}}: nincs ilyen adat.")
            return m.group(0)
        text = re.sub(r"\{([^{}]*)\}", lab_ref, v.replace("\\{", "\x01").replace("\\}", "\x02"))
        text = text.replace("\x01", "{").replace("\x02", "}")
        mp = Mx(frac=spec["math"], chem=spec["chem"])
        tree = mp.text(text)
        for e in mp.errors:
            P.err(n, f"„{k}”: {e}")
        if spec["chem"] and (mp.conv or has_script(tree)):     # Na^+, SO4^2-, ₂ is (nem csak a H2O-szerű képlet)
            u = mx_unicode(tree)
            if u is not None:
                for f in dict.fromkeys(mp.conv):
                    if f != "->":
                        P.info(n, f"{f} → {mx_unicode(Mx(chem=True).text(f))}")
                if not mp.conv and u != text:
                    P.info(n, f"„{k}”: {text} → {u}")
                text = u
        if spec["chem"] and re.search(r"egyenlet$", k) and "→" not in text:
            P.warn(n, f"„{k}”: az egyenletben nyíl kell (→ vagy ->), pl. „metán + oxigén → szén-dioxid + víz”.")
        mx = spec["labels"][k] or DEFAULT_LABEL_MAX
        ln = vis_len(tree) if not (spec["chem"] and text != v) else len(text)
        if ln > mx:
            P.err(n, f"„{k}”: a felirat {ln} karakter, legfeljebb {mx} lehet (a vásznon nem férne el).")
        if re.search(r"\d\.\d", text):
            P.warn(n, f"„{k}”: tizedespont? A magyar írásmód tizedesvessző (3,14).")
        labels[k] = text
    for k in quotes:
        src[k] = doc["items"][k][2]
    for k in spec["labels"]:
        if k not in labels and k not in doc["items"]:
            P.err(0, f"hiányzó felirat: „- {k}: …” (### Feliratok alá)")
    for k in spec["data"]:
        if k not in data and k not in doc["items"]:
            w = spec["data"][k]
            hint = {"year": "Kr. e. 753", "date": "1848. március 15.", "coord": "47,50° É, 19,04° K",
                    "range": "50–70 ezer " + w.get("unit", ""), "ago": "66 millió éve", "ratio": "3 : 1",
                    "frac": "3/4", "list": "2; 3; 5 " + w.get("unit", ""), "point": "(2; −1,5)",
                    "series": "0 " + w.get("ux", "") + ": 13,3 · 20 " + w.get("ux", "") + ": 31,6",
                    "expr": "x^2 − 4x + 3", "formula": "H₂O", "equation": "CH₄ + 2 O₂ → CO₂ + 2 H₂O",
                    "utc": "UTC+1", "dataset": "<a forrás neve>", "metrum": "— ∪ ∪ | — ∪ ∪ | — ×", "rhyme": "aabb",
                    "morph": "kert + ész (képző) + ek (jel) + nek (rag)", "pron": "kútba [kúdba]",
                    "rel": "Gergely – Éva: szerelem (I–V)"}.get(w.get("type"), "… " + w.get("unit", ""))
            P.err(0, f"hiányzó adat: „- {k}: {hint.strip()}” (### Adatok alá)")
    if spec["sources"]:
        check_sources(md_path, doc, P)
    if spec["review"] and not any(re.match(r"\s*Szakmai ellenőrzés\s*:", t) for _, t in md_comments(md_path)):
        P.warn(0, f"a lecke szakmai lektorálást kér ({', '.join(spec['review'])}): hiányzik a "
                  "<!-- Szakmai ellenőrzés: <szerep>, <dátum>, <ajánlás verziója> --> blokk (név nélkül).")
    if spec["math"]:
        for n in doc["bareNotes"]:
            P.warn(n, "a „>” sor megjegyzésdoboz – egyenlőtlenséggel ne kezdj sort (írd ` ` közé: `x > 3`), "
                      "megjegyzésnél írd ki: „> megjegyzés: …”.")

    # 3) lépések
    if spec["steps"] is not None and len(doc["steps"]) != spec["steps"]:
        P.err(0, f"a lecke {spec['steps']} lépést vár, a .md-ben {len(doc['steps'])} van.")
    steps = []
    for s in doc["steps"]:
        parts, words, ul = [], 0, []
        for kind, n, t in s["blocks"]:
            words += count_words(t, ctx, kind == "fx")
            h = inline(t, n, P, data_fmt, ctx, fx=kind == "fx")
            if kind == "li":
                ul.append(f'<li data-src="{n}">{h}</li>'); continue
            if ul:
                parts.append("<ul>" + "".join(ul) + "</ul>"); ul = []
            cls = {"note": ' class="note"', "fx": ' class="big-fx"', "interp": ' class="interp"'}.get(kind, "")
            if kind == "fx":
                h = nobreak(h)                 # a képlet: sor egyben marad (csak relációjel után törhet)
            if kind == "interp":               # „> értelmezés: …” – egy lehetséges olvasat (magyar irodalom)
                h = '<span class="interp-h">Egy lehetséges olvasat</span>' + h
            parts.append(f'<p{cls} data-src="{n}">{h}</p>')
        if ul:
            parts.append("<ul>" + "".join(ul) + "</ul>")
        if not parts:
            P.warn(s["line"], f"a(z) „{s['title']}” lépésnek nincs panelszövege.")
        if words > spec["maxWords"]:
            P.warn(s["line"], f"a(z) „{s['title']}” lépés panelszövege {words} szó (ajánlott ≤ {spec['maxWords']}).")
        steps.append({"title": inline(s["title"], s["line"], P, data_fmt, ctx), "html": "".join(parts), "line": s["line"], "words": words})

    if spec["interpretive"] and not any(kind == "interp" for s in doc["steps"] for kind, _, _ in s["blocks"]) and not any(
            s["blocks"] and re.search(r"\?[”»\"')\]]*$", s["blocks"][-1][2].rstrip()) for s in doc["steps"]):
        P.warn(0, "értelmező lecke (\"interpretive\"): legyen benne legalább egy „> értelmezés: …” doboz vagy egy "
                  "kérdéssel végződő lépés (nyitott kérdés).")
    title = plain_title(doc["title"], doc["titleLine"], P, ctx)
    if P.errors or check_only:
        P.content = {"data": data, "labels": labels, "steps": steps, "title": title}
        if quotes:
            P.content["quotes"] = quotes
        return P
    meta = doc["meta"]
    content = {
        "source": md_path.name, "title": title, "titleLine": doc["titleLine"],
        "meta": {"subject": meta.get("tantárgy", ""), "grade": meta.get("évfolyam", ""), "topic": meta.get("témakör", "")},
        "steps": steps, "labels": labels, "data": data, "src": src,
    }
    if quotes:                           # csak ha van ### Idézet (a régi leckék kimenete változatlan)
        content["quotes"] = quotes
        content["quoteSrc"] = quote_src
    out = (pathlib.Path(out_dir) if out_dir else md_path.parent) / (md_path.stem + ".content.js")
    out.write_text(f"/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: {md_path.name}\n"
                   f"   Újragenerálás: python3 tools/build_lesson.py {md_path.relative_to(ROOT).as_posix() if md_path.is_relative_to(ROOT) else md_path.name} */\n"
                   "window.LESSON_CONTENT = " + json.dumps(content, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    P.out = out
    P.content = content
    return P


def all_lessons():
    return sorted(p for p in (ROOT / "leckek").rglob("*.md") if re.match(r"^\d\d-", p.name) and p.with_suffix(".html").exists())


def stale(files, year):
    """--stale: a „frissítendő” adatok, amelyek éve régebbi, mint year − 2."""
    n = 0
    for f in files:
        P = build(f, check_only=True)
        for k, d in getattr(P, "content", {}).get("data", {}).items():
            if d.get("upd") and d.get("yr", 0) < year - 2:
                n += 1
                rel = f.resolve().relative_to(ROOT).as_posix() if f.resolve().is_relative_to(ROOT) else f.name
                print(f"{rel}: „{k}” = {d.get('s', d.get('v'))} ({d.get('yr', 'év nélkül')}) – frissítendő")
    print(f"{'✓ nincs elavult adat' if not n else f'{n} frissítendő adat'} (határ: {year - 2} előtti)")
    return 0


def mx_cases():
    t = (ROOT / "tools" / "tests" / "mx-cases.js").read_text(encoding="utf-8")
    return json.loads(t[t.index("["):t.rindex("]") + 1])


def selftest():
    """A tools/tests/ próbafájljai: tort-adatok.md (hibátlan, értékek ellenőrzése), tort-hibak.md (várt hibák),
    uj-adatok.md / uj-hibak.md (az új adattípusok), jeloles-mat.md / jeloles-kem.md (jelölés), mx-cases.js,
    magyar-adatok.md / magyar-hibak.md (idézet, verssor, metrum, rím, szóelem, ejtés, kapcsolat, értelmezés)."""
    T = ROOT / "tools" / "tests"
    fails = []

    def check(name, got, want):
        if got != want:
            fails.append(f"{name}: {got!r} ≠ várt {want!r}")

    with tempfile.TemporaryDirectory() as tmp:
        P = build(T / "tort-adatok.md", out_dir=tmp)
        for m in P.errors + P.warnings:
            fails.append("váratlan: " + m)
        D = getattr(P, "content", {}).get("data", {})
        g = lambda k, f: D.get(k, {}).get(f)
        check("olimpia v", g("első olimpia", "v"), -776)
        check("olimpia a", g("első olimpia", "a"), -775)
        check("róma s", g("Róma alapítása", "s"), "Kr.\u00a0e.\u00a0753")
        check("eltelt évek", g("Róma alapítása", "a") - g("első olimpia", "a"), 23)
        check("Kr. e. 1 → Kr. u. 1", g("Kr. u. 1", "a") - g("Kr. e. 1", "a"), 1)
        check("476 s", g("Nyugatrómai Birodalom vége", "s"), "Kr.\u00a0u.\u00a0476")
        check("i. e. stílus", g("i. e. év", "s"), "i.\u00a0e.\u00a0490")
        check("tatárjárás", (g("muhi csata", "v"), g("muhi csata", "s")), (1241, "1241"))
        check("körül → est", (g("piramis", "est"), g("piramis", "s"), g("piramis", "s0")),
              (True, "kb.\u00a0Kr.\u00a0e.\u00a02560", "Kr.\u00a0e.\u00a02560"))
        check("dátum", (g("forradalom", "ymd"), g("forradalom", "s"), g("forradalom", "v")), ([1848, 3, 15], "1848. március 15.", 1848))
        check("dátum a", round(g("forradalom", "a"), 3), round(1848 + (31 + 29 + 14.5) / 366, 3))
        check("hónap", (g("csak hónap", "ymd"), g("csak hónap", "s")), ([1849, 4, None], "1849. április"))
        check("Kr. e. dátum", (g("Caesar halála", "ymd"), g("Caesar halála", "a") < -42), ([-44, 3, 15], True))
        check("koord", (g("Buda", "lat"), g("Buda", "lon"), g("Buda", "s")), (47.5, 19.04, "47,50°\u00a0É, 19,04°\u00a0K"))
        check("koord perc", (round(g("Marathón", "lat"), 4), round(g("Marathón", "lon"), 4)), (38.15, 23.9667))
        check("koord D/Ny", (g("Lisszabon", "lat"), g("Lisszabon", "lon")), (38.72, -9.14))
        check("tartomány", {f: g("sereg", f) for f in ("lo", "hi", "v", "u", "s", "est")},
              {"lo": 50000.0, "hi": 70000.0, "v": 60000.0, "u": "fő", "s": "kb.\u00a050–70\u00a0ezer\u00a0fő", "est": True})
        check("tartomány egység nélkül", (g("napok", "lo"), g("napok", "hi"), g("napok", "s"), g("napok", "u")), (25.0, 28.0, "25–28", ""))
        check("szám becsléssel", (g("lakosság", "v"), g("lakosság", "est"), g("lakosság", "s")), (2000000.0, True, "kb.\u00a02\u00a0millió\u00a0fő"))
        check("sima szám változatlan", D.get("távolság"), {"v": 42.195, "u": "km", "d": 3})
        check("millió km egység", D.get("Nap távolsága"), {"v": 150.0, "u": "millió km", "d": 0})
        html = "".join(s["html"] for s in getattr(P, "content", {}).get("steps", []))
        check("{hivatkozás}", "Kr.\u00a0e.\u00a0753" in H.unescape(html) and "kb.\u00a050–70\u00a0ezer\u00a0fő" in H.unescape(html), True)

        P = build(T / "tort-hibak.md", check_only=True)
        want = ["0. év nincs", "Kr. e. 33", "február 30. nem létező nap", "ismeretlen hónap", "kívül esik a lecke térképén",
                "egy szélesség (É/D) és egy hosszúság", "alsó értéke kisebb", "mértékegység „fő” legyen",
                "nem értelmezhető évszám", "kívül esik az értelmes tartományon", "ismeretlen adattípus"]
        for w in want:
            if not any(w in e for e in P.errors):
                fails.append(f"hiányzó várt hiba: „{w}”")
        if len(P.errors) != len(want):
            fails.append(f"{len(P.errors)} hiba, várt: {len(want)}:\n    " + "\n    ".join(P.errors))
        if not any("szó (ajánlott ≤ 20)" in w for w in P.warnings):
            fails.append("hiányzó figyelmeztetés: maxWords (20)")

        # ── új adattípusok ──
        P = build(T / "uj-adatok.md", out_dir=tmp)
        for m in P.errors + P.warnings:
            fails.append("uj-adatok váratlan: " + m)
        D = getattr(P, "content", {}).get("data", {})
        g = lambda k, f=None: D.get(k, {}) if f is None else D.get(k, {}).get(f)
        check("ago", (g("élet kezdete", "v"), g("élet kezdete", "s")), (3.8e9, "3,8\u00a0milliárd\u00a0éve"))
        check("ago tartomány", (g("emberfélék", "lo"), g("emberfélék", "hi"), g("emberfélék", "s")), (6e6, 7e6, "7–6\u00a0millió\u00a0éve"))
        check("ago becslés", (g("oxigén", "est"), g("oxigén", "s")), (True, "kb.\u00a02,4\u00a0milliárd\u00a0éve"))
        check("ratio", (g("Mendel", "a"), g("Mendel", "b"), round(g("Mendel", "v"), 4), g("Mendel", "s")), (5474, 1850, 2.9589, "5474\u00a0:\u00a01850"))
        check("ratio 3 tag", g("háromszög", "p"), [3, 4, 5])
        check("pulzus /perc", (g("pulzus", "v"), g("pulzus", "u"), g("pulzus", "s")), (70, "/perc", "70/perc"))
        check("tartomány /perc", (g("pulzus tartomány", "lo"), g("pulzus tartomány", "u"), g("pulzus tartomány", "s")), (60, "/perc", "60–100/perc"))
        check("millió/µl", (g("vörösvérsejt", "v"), g("vörösvérsejt", "u"), g("vörösvérsejt", "s")), (4.5e6, "/µl", "4,5\u00a0millió/µl"))
        check("billió", (g("sejtek", "v"), g("sejtek", "s")), (3.8e13, "38\u00a0billió"))
        check("szorzószó egységgel", (g("jég", "v"), g("jég", "u")), (68000, "km²"))
        check("dim", (g("sejt mérete", "base"), g("sejt mérete", "bu"), g("sejt mérete", "s")), (7e-6, "m", "7\u00a0µm"))
        check("dim térfogat", (g("pohár", "base"), g("pohár", "bu")), (0.25, "l"))
        check("range dim", {f: g("sejtméret-tartomány", f) for f in ("lo", "hi", "u", "s", "blo", "bhi", "base", "bu")},
              {"lo": 10.0, "hi": 30.0, "u": "µm", "s": "10–30\u00a0µm", "blo": 1e-5, "bhi": 3e-5, "base": 2e-5, "bu": "m"})
        check("range dim tizedes", (g("hajszál", "blo"), g("hajszál", "bhi"), g("hajszál", "d"), g("hajszál", "s")),
              (5e-5, 1e-4, 2, "0,05–0,1\u00a0mm"))
        check("int", g("lábak", "v"), 94)
        check("sign", g("változás", "s"), "+3")
        check("sign negatív", g("hidegrekord", "s"), "−35\u00a0°C")
        check("szög perc", (g("szög", "v"), g("szög", "s")), (45.5, "45°\u00a030′"))
        check("frac", {f: g("tört", f) for f in ("n", "d", "w", "neg", "red", "s")},
              {"n": 3, "d": 4, "w": 0, "neg": False, "red": True, "s": "3/4"})
        check("frac vegyes", (g("vegyes", "w"), g("vegyes", "n"), g("vegyes", "d"), round(g("vegyes", "v"), 4)), (2, 1, 3, 2.3333))
        check("frac negatív", (g("negatív tört", "neg"), g("negatív tört", "v"), g("negatív tört", "s")), (True, -0.625, "−5/8"))
        check("list", (g("jegyek", "v"), g("jegyek", "s")), ([2, 3, 5, 5, 5], "2; 3; 5; 5; 5"))
        check("list egységgel", (g("havi hőmérséklet", "v")[:3], g("havi hőmérséklet", "u"), len(g("havi hőmérséklet", "v"))),
              ([-1.2, 0.9, 5.4], "°C", 12))
        check("series", (g("oldhatóság", "x"), g("oldhatóság", "y"), g("oldhatóság", "ux")), ([0, 20, 40], [13.3, 31.6, 63.9], "°C"))
        check("point", (g("csúcs", "x"), g("csúcs", "y"), g("csúcs", "s")), (2, -1.5, "(2; −1,5)"))
        check("point névvel", (g("A pont", "name"), g("A pont", "s")), ("A", "A(3; −2)"))
        check("utc", (g("Delhi", "min"), g("Delhi", "s")), (330, "UTC+5:30"))
        check("utc negatív", (g("New York", "min"), g("New York", "s")), (-300, "UTC−5"))
        check("utc 0", (g("London", "min"), g("London", "s")), (0, "UTC"))
        check("év/állapot", {f: g("világ népessége", f) for f in ("yr", "upd", "s", "v")},
              {"yr": 2025, "upd": True, "s": "8,2\u00a0milliárd\u00a0fő", "v": 8.2e9})
        check("előrejelzés", (g("népesség 2050", "proj"), g("népesség 2050", "yr")), (True, 2050))
        check("modell", g("föhn", "model"), True)
        check("expr", (g("függvény", "s"), g("függvény", "tree")),
              ("x^2 − 4x + 3", ["+", ["−", ["^", "x", 2], ["imp", 4, "x"]], 3]))
        check("expr sorrend", g("műveleti sorrend", "tree"), ["+", 2, ["·", 3, 4]])
        check("expr egyenlet", g("egyenlet", "tree"), ["=", ["+", ["imp", 3, "x"], 4], 19])
        check("formula", (g("víz", "s"), g("víz", "atoms"), g("víz", "charge")), ("H₂O", {"H": 2, "O": 1}, 0))
        check("formula ion", (g("szulfátion", "s"), g("szulfátion", "atoms"), g("szulfátion", "charge")), ("SO₄²⁻", {"S": 1, "O": 4}, -2))
        check("formula zárójel", g("oltott mész", "atoms"), {"Ca": 1, "O": 2, "H": 2})
        check("equation", (g("metán égése", "s"), [t["k"] for t in g("metán égése", "rhs")]),
              ("CH₄ + 2 O₂ → CO₂ + 2 H₂O", [1, 2]))
        check("equation ionok", g("csapadék", "s"), "Ag⁺ + Cl⁻ → AgCl")
        html = "".join(s["html"] for s in getattr(P, "content", {}).get("steps", []))
        check("{tört} álló", '<span class="frac"><span class="fn">3</span>' in html, True)
        check("{képlet} index", "H<sub>2</sub>O" in html, True)
        check("{kifejezés}", '<span class="mx"><i>x</i><sup>2</sup>' in html, True)

        P = build(T / "uj-hibak.md", check_only=True)
        want = ["Kr. e.” évszámhoz year", "nem lehet 0", "6/8 → 3/4", "pontosvesszővel", "nincs kiegyenlítve: bal oldalon 2 O, jobb oldalon 4 O",
                "ismeretlen vegyjel „Xy”", "a lecke 1 C, 4 H összetételt vár", "szigorúan növekedjenek", "egész szám kell",
                "két műveleti jel egymás után", "„y” betű nem szerepel", "páratlan zárójel", "kívül esik a lecke koordináta-rendszerén",
                "negyedórás", "nincs ilyen adatfájl", "2022 nem szerepel az adatfájl", "hosszúság mértékegysége kell", "elem van, 12 kell",
                "nem = vagy ⇌", "az „… éve”", "„hossz tartomány” = 2–5 kg: hosszúság mértékegysége kell",
                "„nagy tartomány” = 2–5 m: kívül esik"]
        for w in want:
            if not any(w in e for e in P.errors):
                fails.append(f"uj-hibak: hiányzó várt hiba: „{w}”")
        if len(P.errors) != len(want):
            fails.append(f"uj-hibak: {len(P.errors)} hiba, várt: {len(want)}:\n    " + "\n    ".join(P.errors))
        for w in ["trillió", "frissítendő” adat mellé", "hiányzik a forrás", "Szakmai ellenőrzés"]:
            if not any(w in x for x in P.warnings):
                fails.append(f"uj-hibak: hiányzó figyelmeztetés: „{w}”")

        # ── jelölés ──
        P = build(T / "jeloles-mat.md", out_dir=tmp)
        for m in P.errors:
            fails.append("jeloles-mat váratlan: " + m)
        st = getattr(P, "content", {}).get("steps", [])
        hs = [s["html"] for s in st]
        exp = [
            (0, '<span class="frac"><span class="fn">3</span><span class="fs">/</span><span class="fd">4</span></span>'),
            (0, "3/4 km/h"),                                    # \/ menekítés, km/h érintetlen
            (0, '2<span class="frac"><span class="fn">1</span>'),  # vegyes szám: a szóköz eltűnik
            (0, "2<sup>3</sup>"),
            (0, "{1; 2; 3}"), (0, "{ }"), (0, "{x}"),
            (1, '<span class="mx"><i>x</i><sup>2</sup> − 4<i>x</i> + 3 = 0</span>'),
            (1, '<span class="mx"><i>a</i> · <i>b</i> ≤ <i>c</i></span>'),
            (1, '<span class="mx"><i>f</i>: <i>x</i> ↦ 2<i>x</i> + 1</span>'),
            (1, '<span class="rt">√<span class="rad"><span class="rp">(</span><i>x</i> + 1<span class="rp">)</span></span></span>'),
            (1, "π"), (1, "10<sup>−3</sup>"), (1, "2<sup><i>n</i>+1</sup>"), (1, "<i>D</i><sub><i>f</i></sub>"),
            (1, "<i>x</i><sub>1</sub>"),
            (2, '<p class="big-fx" data-src="'), (2, '<span class="frac"><span class="fn">−<i>b</i> ± '),
            (3, '<span class="frac"><span class="fn"><i>x</i></span><span class="fs">/</span><span class="fd">2</span></span>'),
        ]
        exp = [(i, nobreak(e) if i in (1, 2) and not e.startswith("<p") else e) for i, e in exp]     # a képlet szóközei nem törők (v2)
        for i, e in exp:
            if i >= len(hs) or e not in hs[i]:
                fails.append(f"jeloles-mat {i + 1}. lépés: hiányzik „{e}”\n      {hs[i] if i < len(hs) else '—'}")
        check("képlet: törés csak relációjel után", nobreak("<i>a</i> + 1 = 2 &lt; 3"),
              "<i>a</i>\u00a0+\u00a01\u00a0= 2\u00a0&lt; 3")
        Pq = Problems(T / "x.md")
        check("dim + int a megadott egységben", parse_number_item("5 cm", 1, Pq, "k", {"dim": "hossz", "int": True})[0]["base"], 0.05)
        parse_number_item("2,5 cm", 1, Pq, "k", {"dim": "hossz", "int": True})
        check("dim + int: 2,5 cm hiba", len(Pq.errors), 1)
        check("expr tört-literál", parse_expr_tree("1/3 · 3/4", ["x"])[0], ["·", ["/", 1, 3], ["/", 3, 4]])
        check("expr tört-literál osztás után", parse_expr_tree("2 : 1/4", ["x"])[0], [":", 2, ["/", 1, 4]])
        check("expr tizedes / marad osztás", parse_expr_tree("1,5/3 · 2", ["x"])[0], ["·", ["/", 1.5, 3], 2])
        check("expr tört^ nem literál", parse_expr_tree("1/2^3", ["x"])[0], ["/", 1, ["^", 2, 3]])
        check("képletszakasz = 1 szó", st[1]["words"] if len(st) > 1 else None, 12)
        check("képlet: = 3 szó", st[2]["words"] if len(st) > 2 else None, 5)
        L = getattr(P, "content", {}).get("labels", {})
        check("felirat nyersen marad", L.get("tört felirat"), "3/4 + 1/4 = 1")
        check("cím (matek)", getattr(P, "content", {}).get("title"), "Próba: matematikai jelölés – x² − 1, √2, 2 1/3")
        for w in ["szorzásjelnek", "valódi mínuszjelet", "tizedespont", "szögpercnek", "pontosvesszővel", "kitevővel",
                  "egyenlőtlenséggel ne kezdj"]:
            if not any(w in x for x in P.warnings):
                fails.append(f"jeloles-mat: hiányzó figyelmeztetés: „{w}”")

        P = build(T / "jeloles-kem.md", out_dir=tmp)
        for m in P.errors:
            fails.append("jeloles-kem váratlan: " + m)
        hs = [s["html"] for s in getattr(P, "content", {}).get("steps", [])]
        for e in ["H<sub>2</sub>O", "CO<sub>2</sub>-kibocsátás", "Na<sup>+</sup>-ion", "SO<sub>4</sub><sup>2−</sup>",
                  "Ca(OH)<sub>2</sub>", " → ", "Mg<sup>2+</sup>", "B12", "Cl-atom", "H<sub>2</sub>O (alsó index)"]:
            if not any(e in h for h in hs):
                fails.append(f"jeloles-kem: hiányzik „{e}”\n      " + "\n      ".join(hs))
        L = getattr(P, "content", {}).get("labels", {})
        check("kémiai felirat Unicode", (L.get("víz"), L.get("ion"), L.get("reakció")), ("H₂O", "SO₄²⁻", "CH₄ + 2 O₂ → CO₂ + 2 H₂O"))
        check("kémiai felirat ion (^)", (L.get("kation"), L.get("hidroxidion"), L.get("kalciumion"), L.get("unicode")),
              ("Na⁺", "OH⁻", "Ca²⁺-ion", "Mg²⁺"))
        check("cím (kémia)", getattr(P, "content", {}).get("title"), "Próba: kémiai jelölés – H₂O, Na⁺ és SO₄²⁻")
        if not any("Na^+ → Na⁺" in x for x in P.infos):
            fails.append("jeloles-kem: hiányzó info: Na^+ → Na⁺")
        if not any("H2O → H₂O" in x for x in P.infos):
            fails.append("jeloles-kem: hiányzó info: H2O → H₂O")
        if not any("nyíl kell" in x for x in P.warnings):
            fails.append("jeloles-kem: hiányzó figyelmeztetés: szóegyenlet nyíl nélkül")

        # ── magyar: idézet, verssor, metrum, rím, szóelem, ejtés, szereplőkapcsolat, értelmezés ──
        P = build(T / "magyar-adatok.md", out_dir=tmp)
        for m in P.errors + P.warnings:
            fails.append("magyar-adatok váratlan: " + m)
        C = getattr(P, "content", {})
        Q, D = C.get("quotes", {}), C.get("data", {})
        g = lambda k, f=None: D.get(k, {}) if f is None else D.get(k, {}).get(f)
        q = lambda k, f: Q.get(k, {}).get(f)
        check("idézet: a | eltűnik", q("jv 1/1", "s"), "Tüzesen süt le a nyári nap sugára")
        check("idézet: szótag, metszet", (q("jv 1/1", "syl"), q("jv 1/1", "cut"), q("jv 1/1", "ci")), (12, [6], [17]))
        check("idézet: a metszet karakterhelye", Q.get("jv 1/1", {}).get("s", "")[17:22], "nyári")
        check("idézet: 6 sor, forrás", ([k for k in Q if k.startswith("jv ")], q("jv 1/6", "ref")),
              (["jv 1/1", "jv 1/2", "jv 1/3", "jv 1/4", "jv 1/5", "jv 1/6"], 0))
        check("idézet: szótagmagok", [Q["jv 1/2"]["s"][i] for i in Q.get("jv 1/2", {}).get("v", [])] if "jv 1/2" in Q else None,
              list("Aéeeéőauáoáa"))
        check("idézet: forrássor", (len(C.get("quoteSrc", [])), (C.get("quoteSrc") or [""])[0][:28]), (3, "Petőfi Sándor: János vitéz ("))
        check("idézet: jogszabály († nélkül)", q("kt idézet", "ref"), 2)
        check("idézet: review-sor (src)", C.get("src", {}).get("jv 1/1"), 14)
        check("rím", (g("jv rímképlet", "p"), g("jv rímképlet", "s")), (list("aabbcc"), "aabbcc"))
        check("metrum", (g("huszt 1 metrum", "n"), g("huszt 1 metrum", "feet")[2] if g("huszt 1 metrum") else None,
                         g("huszt 1 metrum", "s")), (15, ["—", "—"], "— ∪ ∪ | — ∪ ∪ | — — | — — | — ∪ ∪ | — ×"))
        check("metrum: - u jelek, || metszet", (g("huszt 2 metrum", "n"), g("huszt 2 metrum", "cz"), g("huszt 2 metrum", "s")),
              (14, [3], "— ∪ ∪ | — ∪ ∪ | — || — ∪ ∪ | — ∪ ∪ | —"))
        check("morph", (g("kertészeknek", "s"), [(x["s"], x["k"]) for x in g("kertészeknek", "parts") or []]),
              ("kertészeknek", [("kert", "tő"), ("ész", "képző"), ("ek", "jel"), ("nek", "rag")]))
        check("morph összetett", [x["k"] for x in g("virágcserépben", "parts") or []], ["tő", "tő", "rag"])
        check("morph kötőhangzó", g("házakban", "s"), "házakban")
        check("morph változatlista", (g("inessivus", "s"), (g("inessivus", "parts") or [{}])[0].get("alt")), ("-ban/-ben", ["ban", "ben"]))
        check("pron", (g("kútba", "w"), g("kútba", "p"), g("kútba", "s")), ("kútba", "kúdba", "kútba [kúdba]"))
        check("rel", {f: g("Gergely és Éva", f) for f in ("a", "b", "kind", "from", "to", "fi", "ti")},
              {"a": "Gergely", "b": "Éva", "kind": "szerelem", "from": "I", "to": "V", "fi": 0, "ti": 4})
        check("rel egy egység", (g("Dobó és Gergely", "from"), g("Dobó és Gergely", "to"), g("Dobó és Gergely", "s")),
              ("IV", "IV", "Dobó – Gergely: vezet (IV)"))
        hs = [s["html"] for s in C.get("steps", [])]
        check("értelmezés-doboz", bool(hs) and '<p class="interp" data-src="10"><span class="interp-h">Egy lehetséges olvasat</span>A tűző'
              in hs[0], True)
        check("{ejtés} a panelen", bool(hs) and "kútba [kúdba]" in hs[0], True)
        check("értelmezés: a szókorlátba számít", C.get("steps", [{}])[0].get("words"), 21)
        check("szótag: Kölcsey (y nem magánhangzó)", len(hu_vowels("Kölcsey Ferenc")), 4)
        check("szótag: yVowel", len(hu_vowels("Teleky Blanka", frozenset({"teleky"}))), 5)
        check("szótag: gy/ny/ly/ty", len(hu_vowels("hogy nyolc folyó tyúk")), 5)
        check("hangrend", [harmony(w) for w in ("ház", "kert", "kávé", "papír", "sofőr", "híd", "hotel", "tök")],
              ["mély", "magas", "mély", "mély", "magas", None, None, "magas"])
        check("római szám", [roman_val(x) for x in ("I", "IV", "IX", "XIV", "IIII", "")], [1, 4, 9, 14, None, None])

        P = build(T / "magyar-hibak.md", check_only=True)
        want = ["„jv csonka”: 9 szótag, 12 kellene", "a megjegyzés szerint 10 szótag", "a sormetszet (|) 5. szótag után",
                "„fölösleges”: fölösleges idézet", "kötelező a forrásmegjegyzés", "szerző † 1989: a szöveg védett",
                "népköltészetnél a közkincs gyűjtés", "hiányzik a kiadás", "hiányzó idézet: „- hiányzó sor",
                "„kiadás nélkül” idézetcsoportban 1 sor van", "5 betűs képlet, de 8 sor", "ismeretlen jel „?”",
                "a metrum 6 szótagos", "rag után nem jöhet jel", "„ész” fajtáját írd", "ismeretlen szóelem-fajta „képzö”",
                "megvalósult alakját", "szögletes zárójelbe", "ismeretlen szereplő „Bornemissza”", "az időszak eleje (IV)",
                "ismeretlen kapcsolat „rokon”", "ismeretlen egység „VI”"]
        for w in want:
            if not any(w in e for e in P.errors):
                fails.append(f"magyar-hibak: hiányzó várt hiba: „{w}”")
        if len(P.errors) != len(want):
            fails.append(f"magyar-hibak: {len(P.errors)} hiba, várt: {len(want)}:\n    " + "\n    ".join(P.errors))
        for w in ["„jv jelzett”: 9 szótag (12 helyett)", "„a” rím sorvégei nem csengenek", "5. szótag (é) hosszú magánhangzó",
                  "„ban” (rag) mély hangrendű, a(z) „kert” magas", "az írás és az ejtés azonos", "értelmező lecke"]:
            if not any(w in x for x in P.warnings):
                fails.append(f"magyar-hibak: hiányzó figyelmeztetés: „{w}”")

    # ── a # cím más tárgyban: Unicode, ahol lehet; a többi változatlan ──
    Pt = Problems(T / "cím")
    for src, want in [("Miért úszik a jég? – a sűrűség", "Miért úszik a jég? – a sűrűség"),
                      ("A `v = s/t` képlet", "A v = s/t képlet"), ("Az F_fel felhajtóerő", "Az F_fel felhajtóerő"),
                      ("10^-3 és x^(n+1)", "10⁻³ és xⁿ⁺¹"), ("A CO2 és a B12", "A CO2 és a B12"), ("Kr. e. 753 – 1848", "Kr. e. 753 – 1848")]:
        check(f"cím „{src}”", plain_title(src, 1, Pt, {}), want)
    check("cím (kémia, B12 nem képlet)", plain_title("A CO2 és a B12", 1, Pt, {"chem": True}), "A CO₂ és a B12")
    check("cím hibátlan", Pt.errors, [])

    # ── közös próbaesetek (a JS MatText.parse ugyanezeket futtatja) ──
    for c in mx_cases():
        mp = Mx(frac=c.get("frac", False), chem=c.get("chem", False))
        got = mp.math(c["src"], c.get("big", False)) if c.get("math") else mp.text(c["src"])
        check(f"mx „{c['src']}”", got, c["tree"])
    for f in fails:
        print("✗", f)
    print("✓ selftest: minden rendben" if not fails else f"✗ selftest: {len(fails)} hiba")
    return 1 if fails else 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--stale" in argv:
        i = argv.index("--stale")
        year = int(argv[i + 1]) if i + 1 < len(argv) and argv[i + 1].isdigit() else datetime.date.today().year
        rest = [a for j, a in enumerate(argv) if not a.startswith("--") and not (j == i + 1 and a.isdigit())]
        return stale([pathlib.Path(a) for a in rest] or all_lessons(), year)
    check = "--check" in argv
    args = [a for a in argv if not a.startswith("--")]
    if "--all" in argv:
        files = all_lessons()
    else:
        files = [pathlib.Path(a) for a in args]
    if not files:
        print(__doc__); return 2
    bad = 0
    for f in files:
        if not f.exists():
            print(f"{f}: nincs ilyen fájl"); bad += 1; continue
        P = build(f, check)
        for m in P.infos + P.warnings + P.errors:
            print(m)
        if P.errors:
            bad += 1
            print(f"✗ {f.name}: {len(P.errors)} hiba — a .content.js NEM frissült.")
        else:
            print(f"✓ {f.name}" + (" (ellenőrizve)" if check else f" → {P.out.name}") + (f", {len(P.warnings)} figyelmeztetés" if P.warnings else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
