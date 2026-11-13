#!/usr/bin/env python3
"""Lecke-tartalom build: <lecke>.md  →  <lecke>.content.js  (window.LESSON_CONTENT = {...})

    python3 tools/build_lesson.py leckek/fizika-7-8/01-suruseg.md
    python3 tools/build_lesson.py --all          # minden leckek/**/NN-*.md, amelynek van .html párja
    python3 tools/build_lesson.py --check …      # csak ellenőriz, nem ír
    python3 tools/build_lesson.py --selftest     # a tools/tests/ próbafájljain teszteli a buildet

A .md formátumát a leckek/README.md írja le. A lecke HTML-je egy
<script type="application/json" id="lesson-spec"> blokkban deklarálja, mit vár:
    {"steps": 9,
     "maxWords": 45,                              # opcionális: panelszöveg-korlát lépésenként (alap: 55)
     "labels": {"kulcs": 40, "másik": null},      # felirat → max. hossz (null: alapértelmezés)
     "data":   {"kulcs": {"unit": "g/cm³", "min": 0.1, "max": 25}}}   # vagy csak "g/cm³"
A build hibával (1-es kilépési kód, sorszámmal) áll le, ha hiányzó vagy fölösleges kulcs van,
egy felirat túl hosszú, egy szám nem értelmezhető / rossz a mértékegysége / tartományon kívül esik.
Figyelmeztet, ha egy lépés panelszövege a korlátnál (alap: 55 szó) hosszabb.

Adattípusok (a spec "data" bejegyzésének "type" mezője; alap: "number"):
  number  „0,92 g/cm³” → {"v": 0.92, "u": "g/cm³", "d": 2}
          Szorzószó: ha a spec egysége "fő", a „25 ezer fő” → v = 25000 (ezer / millió / milliárd);
          ha a spec egysége maga „millió km”, a szó az egység része marad (visszafelé kompatibilis).
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
  range   „50–70 ezer fő”, „25–28” → {"t": "range", "lo": 50000, "hi": 70000, "v": 60000, "u": "fő",
          "d": 0, "s": "50–70 ezer fő"}; min/max a lo-ra és a hi-ra is.
Becslésjelző minden típuson: „kb. …”, „~ …”, „≈ …”, „… (becslés)”, évszámnál „… körül” is
  → "est": true, és "s" „kb. ”-vel kezdődik ("s0": ugyanez a jelző nélkül).
Az új típusoknál (és becslésnél, szorzószónál) a "s" a magyarul formázott alak; ezt kapja a
panelszöveg {kulcs} hivatkozása és az L.val(k). A régi, sima számok kimenete változatlan.
Csak a Python standard könyvtárát használja.
"""
import html as H
import json
import math
import pathlib
import re
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_LABEL_MAX = 32
MAX_WORDS = 55
UNIT_ALIASES = {"cm3": "cm³", "m3": "m³", "dm3": "dm³", "mm3": "mm³", "g/cm3": "g/cm³", "kg/m3": "kg/m³",
                "kg/dm3": "kg/dm³", "fok": "°", "°c": "°C", "C°": "°C"}
NUM_RE = re.compile(r"^([−\-+]?)(\d{1,3}(?:[ \u00a0\u202f]\d{3})+|\d+)(?:,(\d+))?(?=\s|$|%|°)\s*(.*)$")
TYPES = ("number", "year", "date", "coord", "range")
NB = " "                                   # nem törő szóköz: „Kr. e. 753” ne törjön sort
MONTHS = ["január", "február", "március", "április", "május", "június", "július", "augusztus",
          "szeptember", "október", "november", "december"]
MULT = {"ezer": 1e3, "millió": 1e6, "milliárd": 1e9}
INT = r"\d{1,3}(?:[ \u00a0\u202f]\d{3})+|\d+"
EST_PRE = re.compile(r"^(?:kb\.|kb\s|cca\.|~|≈)\s*", re.I)
EST_POST = re.compile(r"\s*\((?:becslés|becsült)\)$", re.I)
ERA = r"(?:(Kr\.\s*e\.|i\.\s*e\.)|(Kr\.\s*u\.|i\.\s*sz\.))"
YEAR_RE = re.compile(rf"^{ERA}?\s*({INT})(\s+körül)?$", re.I)
DATE_RE = re.compile(rf"^{ERA}?\s*({INT})\.\s+([a-zéáíóöőúüű]+)(?:\s+(\d{{1,2}})\.)?$", re.I)
COORD_PART = re.compile(r"(\d{1,3}(?:,\d+)?)\s*°(?:\s*(\d{1,2}(?:,\d+)?)\s*[′'])?\s*(É|D|K|Ny)\b")
RANGE_RE = re.compile(rf"^((?:{INT})(?:,\d+)?)\s*([–\-])\s*((?:{INT})(?:,\d+)?)(?=\s|$|%)\s*(.*)$")


class Problems:
    def __init__(self, path):
        self.path, self.errors, self.warnings = path, [], []

    def err(self, line, msg):
        self.errors.append(f"{self.path.name}{f':{line}' if line else ''}: HIBA: {msg}")

    def warn(self, line, msg):
        self.warnings.append(f"{self.path.name}{f':{line}' if line else ''}: figyelem: {msg}")


def norm_unit(u):
    u = u.strip()
    return UNIT_ALIASES.get(u, UNIT_ALIASES.get(u.lower(), u))


def to_float(intp, frac):
    return float(re.sub(r"[ \u00a0\u202f]", "", intp) + ("." + frac if frac else ""))


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


def split_mult(rest, want_unit):
    """('ezer fő', 'fő') → (1000, 'ezer', 'fő'). Ha a teljes maradék maga az elvárt egység, nincs szorzó."""
    u = norm_unit(rest)
    if u == norm_unit(want_unit):
        return 1, "", u
    w, _, tail = rest.strip().partition(" ")
    if w in MULT:
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
    mult, mw, unit = split_mult(rest, want.get("unit", ""))
    if unit != norm_unit(want.get("unit", "")):
        P.err(line, f"„{k}”: a mértékegység „{want.get('unit', '')}” legyen, nem „{unit}”.")
        return None
    if lo >= hi:
        P.err(line, f"„{k}” = {s}: a tartomány alsó értéke kisebb legyen a felsőnél.")
        return None
    text = fmt_num(lo, len(af)) + "–" + fmt_num(hi, len(bf)) + (NB + mw if mw else "") + ((NB + unit) if unit else "")
    lo, hi = lo * mult, hi * mult
    d = max(0, d - int(round(math.log10(mult))))
    return {"t": "range", "lo": lo, "hi": hi, "v": (lo + hi) / 2, "u": unit, "d": d}, text, False


def parse_datum(k, raw, n, want, P):
    """Egy ### Adatok sor értéke → (adat-dict, formázott szöveg) vagy None (a hibát jeleztük)."""
    typ = want.get("type", "number")
    if typ not in TYPES:
        return None              # a spec hibáját a read_spec már jelezte
    s, est = split_est(raw)
    if typ == "number":
        r = parse_number(s, n, P)
        if not r:
            return None
        val, unit, d = r
        mult, mw, unit2 = (1, "", unit)
        if unit != norm_unit(want.get("unit", "")):
            mult, mw, unit2 = split_mult(unit, want.get("unit", ""))
        if unit2 != norm_unit(want.get("unit", "")):
            P.err(n, f"„{k}”: a mértékegység „{want.get('unit', '')}” legyen, nem „{unit}”.")
        item = {"v": val * mult, "u": unit2, "d": max(0, d - int(round(math.log10(mult))))}
        text = fmt_value(val, d, unit)
        if mw:
            item["s"] = text = fmt_num(val, d) + NB + mw + (NB + unit2 if unit2 else "")
    elif typ == "year":
        r = parse_year(s, n, P, k)
        if not r:
            return None
        item, text, korul = r
        est = est or korul
    elif typ == "date":
        r = parse_date(s, n, P, k)
        if not r:
            return None
        item, text, _ = r
    elif typ == "coord":
        r = parse_coord(s, n, P, k, want)
        if not r:
            return None
        item, text, _ = r
    else:
        r = parse_range(s, n, P, k, want)
        if not r:
            return None
        item, text, _ = r
    if typ != "coord":
        lo, hi = (item["lo"], item["hi"]) if typ == "range" else (item["v"], item["v"])
        if "min" in want and lo < want["min"] or "max" in want and hi > want["max"]:
            P.err(n, f"„{k}” = {raw}: kívül esik az értelmes tartományon ({want.get('min', '…')} – {want.get('max', '…')}).")
    if est:
        item["est"] = True
        item["s0"] = text
        text = "kb." + NB + text
    if typ != "number" or est:
        item["s"] = text
    return item, item.get("s", text)


def inline(text, line, P, data_fmt):
    """Tanárbarát jelölés → HTML. **félkövér**, *dőlt*, ==színnel kiemelt==, F_fel → alsó index, {adatkulcs} → az adat értéke."""
    def sub_ph(m):
        k = m.group(1).strip()
        if k not in data_fmt:
            P.err(line, f"{{{k}}}: nincs ilyen adat az ### Adatok listákban.")
            return k
        return "\x00PH" + str(list(data_fmt).index(k)) + "\x00"
    s = re.sub(r"\{([^{}]+)\}", sub_ph, text)
    s = H.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", s)
    s = re.sub(r"==(.+?)==", r'<span class="key">\1</span>', s)
    # alsó index: F_fel → F<sub>fel</sub>, v_0 → v<sub>0</sub> (betű/ρ/Δ után, betűk-számok a végéig)
    s = re.sub(r"([A-Za-zρΔ])_([0-9A-Za-zÁÉÍÓÖŐÚÜŰáéíóöőúüű]+)", r"\1<sub>\2</sub>", s)
    s = re.sub(r"\x00PH(\d+)\x00", lambda m: H.escape(data_fmt[list(data_fmt)[int(m.group(1))]]), s)
    if re.search(r"\*|==", s):
        P.warn(line, "lezáratlan * vagy == jelölés a szövegben.")
    return s


def plain(s):
    return re.sub(r"\*\*|==|(?<!\w)\*|\*(?!\w)", "", s)


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
    return {"steps": spec.get("steps"), "labels": labels, "data": data, "maxWords": mw}


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

    doc = {"title": None, "titleLine": 0, "meta": {}, "steps": [], "items": {}}
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
            sub = {"feliratok": "labels", "adatok": "data"}.get(h)
            if not sub:
                P.err(n, f"„### {l[4:].strip()}”: ismeretlen szakasz (lehet: ### Feliratok, ### Adatok).")
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
                P.err(n, f"a {('Feliratok' if sub == 'labels' else 'Adatok')} alatt minden sor „- kulcs: érték” alakú legyen.")
                continue
            k, v = m.group(1).strip(), m.group(2).strip()
            if k in doc["items"]:
                P.err(n, f"„{k}” kulcs kétszer szerepel (először: {doc['items'][k][2]}. sor).")
                continue
            doc["items"][k] = (sub, v, n)
            continue
        if sec == "common" or sec is None:
            P.err(n, "ide csak ### Feliratok / ### Adatok kerülhet, folyó szöveg nem.")
            continue
        if l.startswith(">"):
            flush()
            t = re.sub(r"^>\s*(megjegyzés\s*:)?\s*", "", l, flags=re.I)
            sec["blocks"].append(("note", n, t)); continue
        if re.match(r"(?i)^képlet\s*:", l):
            flush(); sec["blocks"].append(("fx", n, l.split(":", 1)[1].strip())); continue
        if re.match(r"^[-*]\s+", l):
            flush(); sec["blocks"].append(("li", n, re.sub(r"^[-*]\s+", "", l))); continue
        para.append((n, l))
    flush()
    return doc


def build(md_path, check_only=False, out_dir=None):
    md_path = md_path.resolve()
    P = Problems(md_path)
    spec = read_spec(md_path.with_suffix(".html"), P)
    doc = parse_md(md_path, P)
    if spec is None:
        return P

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
        r = parse_datum(k, v, n, spec["data"][k], P)
        if not r:
            data_fmt[k] = v      # a hibát már jeleztük; a {hivatkozás} ne okozzon újabbat
            continue
        data[k], data_fmt[k] = r
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
        text = re.sub(r"\{([^{}]+)\}", lambda m: data_fmt.get(m.group(1).strip()) or (P.err(n, f"{{{m.group(1)}}}: nincs ilyen adat.") or m.group(0)), v)
        mx = spec["labels"][k] or DEFAULT_LABEL_MAX
        if len(text) > mx:
            P.err(n, f"„{k}”: a felirat {len(text)} karakter, legfeljebb {mx} lehet (a vásznon nem férne el).")
        if re.search(r"\d\.\d", text):
            P.warn(n, f"„{k}”: tizedespont? A magyar írásmód tizedesvessző (3,14).")
        labels[k] = text
    for k in spec["labels"]:
        if k not in labels and k not in doc["items"]:
            P.err(0, f"hiányzó felirat: „- {k}: …” (### Feliratok alá)")
    for k in spec["data"]:
        if k not in data and k not in doc["items"]:
            w = spec["data"][k]
            hint = {"year": "Kr. e. 753", "date": "1848. március 15.", "coord": "47,50° É, 19,04° K",
                    "range": "50–70 ezer " + w.get("unit", "")}.get(w.get("type"), "… " + w.get("unit", ""))
            P.err(0, f"hiányzó adat: „- {k}: {hint.strip()}” (### Adatok alá)")

    # 3) lépések
    if spec["steps"] is not None and len(doc["steps"]) != spec["steps"]:
        P.err(0, f"a lecke {spec['steps']} lépést vár, a .md-ben {len(doc['steps'])} van.")
    steps = []
    for s in doc["steps"]:
        parts, words, ul = [], 0, []
        for kind, n, t in s["blocks"]:
            words += len(re.findall(r"[\wÀ-ž]+(?:[-–][\wÀ-ž]+)*", plain(re.sub(r"\{[^{}]+\}", "X", t))))
            h = inline(t, n, P, data_fmt)
            if kind == "li":
                ul.append(f'<li data-src="{n}">{h}</li>'); continue
            if ul:
                parts.append("<ul>" + "".join(ul) + "</ul>"); ul = []
            cls = {"note": ' class="note"', "fx": ' class="big-fx"'}.get(kind, "")
            parts.append(f'<p{cls} data-src="{n}">{h}</p>')
        if ul:
            parts.append("<ul>" + "".join(ul) + "</ul>")
        if not parts:
            P.warn(s["line"], f"a(z) „{s['title']}” lépésnek nincs panelszövege.")
        if words > spec["maxWords"]:
            P.warn(s["line"], f"a(z) „{s['title']}” lépés panelszövege {words} szó (ajánlott ≤ {spec['maxWords']}).")
        steps.append({"title": inline(s["title"], s["line"], P, data_fmt), "html": "".join(parts), "line": s["line"], "words": words})

    if P.errors or check_only:
        return P
    meta = doc["meta"]
    content = {
        "source": md_path.name, "title": doc["title"], "titleLine": doc["titleLine"],
        "meta": {"subject": meta.get("tantárgy", ""), "grade": meta.get("évfolyam", ""), "topic": meta.get("témakör", "")},
        "steps": steps, "labels": labels, "data": data, "src": src,
    }
    out = (pathlib.Path(out_dir) if out_dir else md_path.parent) / (md_path.stem + ".content.js")
    out.write_text(f"/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: {md_path.name}\n"
                   f"   Újragenerálás: python3 tools/build_lesson.py {md_path.relative_to(ROOT).as_posix() if md_path.is_relative_to(ROOT) else md_path.name} */\n"
                   "window.LESSON_CONTENT = " + json.dumps(content, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    P.out = out
    P.content = content
    return P


def selftest():
    """A tools/tests/ próbafájljai: tort-adatok.md (hibátlan, értékek ellenőrzése), tort-hibak.md (várt hibák)."""
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
        check("róma s", g("Róma alapítása", "s"), "Kr. e. 753")
        check("eltelt évek", g("Róma alapítása", "a") - g("első olimpia", "a"), 23)
        check("Kr. e. 1 → Kr. u. 1", g("Kr. u. 1", "a") - g("Kr. e. 1", "a"), 1)
        check("476 s", g("Nyugatrómai Birodalom vége", "s"), "Kr. u. 476")
        check("i. e. stílus", g("i. e. év", "s"), "i. e. 490")
        check("tatárjárás", (g("muhi csata", "v"), g("muhi csata", "s")), (1241, "1241"))
        check("körül → est", (g("piramis", "est"), g("piramis", "s"), g("piramis", "s0")),
              (True, "kb. Kr. e. 2560", "Kr. e. 2560"))
        check("dátum", (g("forradalom", "ymd"), g("forradalom", "s"), g("forradalom", "v")), ([1848, 3, 15], "1848. március 15.", 1848))
        check("dátum a", round(g("forradalom", "a"), 3), round(1848 + (31 + 29 + 14.5) / 366, 3))
        check("hónap", (g("csak hónap", "ymd"), g("csak hónap", "s")), ([1849, 4, None], "1849. április"))
        check("Kr. e. dátum", (g("Caesar halála", "ymd"), g("Caesar halála", "a") < -42), ([-44, 3, 15], True))
        check("koord", (g("Buda", "lat"), g("Buda", "lon"), g("Buda", "s")), (47.5, 19.04, "47,50° É, 19,04° K"))
        check("koord perc", (round(g("Marathón", "lat"), 4), round(g("Marathón", "lon"), 4)), (38.15, 23.9667))
        check("koord D/Ny", (g("Lisszabon", "lat"), g("Lisszabon", "lon")), (38.72, -9.14))
        check("tartomány", {f: g("sereg", f) for f in ("lo", "hi", "v", "u", "s", "est")},
              {"lo": 50000.0, "hi": 70000.0, "v": 60000.0, "u": "fő", "s": "kb. 50–70 ezer fő", "est": True})
        check("tartomány egység nélkül", (g("napok", "lo"), g("napok", "hi"), g("napok", "s"), g("napok", "u")), (25.0, 28.0, "25–28", ""))
        check("szám becsléssel", (g("lakosság", "v"), g("lakosság", "est"), g("lakosság", "s")), (2000000.0, True, "kb. 2 millió fő"))
        check("sima szám változatlan", D.get("távolság"), {"v": 42.195, "u": "km", "d": 3})
        check("millió km egység", D.get("Nap távolsága"), {"v": 150.0, "u": "millió km", "d": 0})
        html = "".join(s["html"] for s in getattr(P, "content", {}).get("steps", []))
        check("{hivatkozás}", "Kr. e. 753" in H.unescape(html) and "kb. 50–70 ezer fő" in H.unescape(html), True)

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
    for f in fails:
        print("✗", f)
    print("✓ selftest: minden rendben" if not fails else f"✗ selftest: {len(fails)} hiba")
    return 1 if fails else 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    check = "--check" in argv
    args = [a for a in argv if not a.startswith("--")]
    if "--all" in argv:
        files = sorted(p for p in (ROOT / "leckek").rglob("*.md") if re.match(r"^\d\d-", p.name) and p.with_suffix(".html").exists())
    else:
        files = [pathlib.Path(a) for a in args]
    if not files:
        print(__doc__); return 2
    bad = 0
    for f in files:
        if not f.exists():
            print(f"{f}: nincs ilyen fájl"); bad += 1; continue
        P = build(f, check)
        for m in P.warnings + P.errors:
            print(m)
        if P.errors:
            bad += 1
            print(f"✗ {f.name}: {len(P.errors)} hiba — a .content.js NEM frissült.")
        else:
            print(f"✓ {f.name}" + (" (ellenőrizve)" if check else f" → {P.out.name}") + (f", {len(P.warnings)} figyelmeztetés" if P.warnings else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
