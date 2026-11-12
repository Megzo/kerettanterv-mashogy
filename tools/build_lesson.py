#!/usr/bin/env python3
"""Lecke-tartalom build: <lecke>.md  →  <lecke>.content.js  (window.LESSON_CONTENT = {...})

    python3 tools/build_lesson.py leckek/fizika-7-8/01-suruseg.md
    python3 tools/build_lesson.py --all          # minden leckek/**/NN-*.md, amelynek van .html párja
    python3 tools/build_lesson.py --check …      # csak ellenőriz, nem ír

A .md formátumát a leckek/README.md írja le. A lecke HTML-je egy
<script type="application/json" id="lesson-spec"> blokkban deklarálja, mit vár:
    {"steps": 9,
     "labels": {"kulcs": 40, "másik": null},      # felirat → max. hossz (null: alapértelmezés)
     "data":   {"kulcs": {"unit": "g/cm³", "min": 0.1, "max": 25}}}   # vagy csak "g/cm³"
A build hibával (1-es kilépési kód, sorszámmal) áll le, ha hiányzó vagy fölösleges kulcs van,
egy felirat túl hosszú, egy szám nem értelmezhető / rossz a mértékegysége / tartományon kívül esik.
Figyelmeztet, ha egy lépés panelszövege 55 szónál hosszabb.
Csak a Python standard könyvtárát használja.
"""
import html as H
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_LABEL_MAX = 32
MAX_WORDS = 55
UNIT_ALIASES = {"cm3": "cm³", "m3": "m³", "dm3": "dm³", "mm3": "mm³", "g/cm3": "g/cm³", "kg/m3": "kg/m³",
                "kg/dm3": "kg/dm³", "fok": "°", "°c": "°C", "C°": "°C"}
NUM_RE = re.compile(r"^([−\-+]?)(\d{1,3}(?:[   ]\d{3})+|\d+)(?:,(\d+))?(?=\s|$|%|°)\s*(.*)$")


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
    v = float(re.sub(r"[   ]", "", intp) + ("." + frac if frac else ""))
    if sign in "−-" and sign:
        v = -v
    return v, norm_unit(unit), len(frac or "")


def inline(text, line, P, data_fmt):
    """Tanárbarát jelölés → HTML. **félkövér**, *dőlt*, ==színnel kiemelt==, {adatkulcs} → az adat értéke."""
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
    s = re.sub(r"\x00PH(\d+)\x00", lambda m: H.escape(data_fmt[list(data_fmt)[int(m.group(1))]]), s)
    if re.search(r"\*|==", s):
        P.warn(line, "lezáratlan * vagy == jelölés a szövegben.")
    return s


def plain(s):
    return re.sub(r"\*\*|==|(?<!\w)\*|\*(?!\w)", "", s)


def fmt_value(v, d, u):
    s = f"{abs(v):.{d}f}".split(".")
    i = s[0]
    if len(i) > 4:
        i = re.sub(r"\B(?=(\d{3})+(?!\d))", " ", i)
    out = ("−" if v < 0 else "") + i + ("," + s[1] if len(s) > 1 else "")
    return out + ((u if u == "°" else " " + u) if u else "")   # szögfok: 15° (szóköz nélkül); 20 °C


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
    return {"steps": spec.get("steps"), "labels": labels, "data": data}


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


def build(md_path, check_only=False):
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
        r = parse_number(v, n, P)
        if not r:
            data_fmt[k] = v      # a hibát már jeleztük; a {hivatkozás} ne okozzon újabbat
            continue
        val, unit, d = r
        want = spec["data"][k]
        if norm_unit(want.get("unit", "")) != unit:
            P.err(n, f"„{k}”: a mértékegység „{want.get('unit', '')}” legyen, nem „{unit}”.")
        if "min" in want and val < want["min"] or "max" in want and val > want["max"]:
            P.err(n, f"„{k}” = {v}: kívül esik az értelmes tartományon ({want.get('min', '…')} – {want.get('max', '…')}).")
        data[k] = {"v": val, "u": unit, "d": d}
        data_fmt[k] = fmt_value(val, d, unit)
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
            u = spec["data"][k].get("unit", "")
            P.err(0, f"hiányzó adat: „- {k}: … {u}” (### Adatok alá)")

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
        if words > MAX_WORDS:
            P.warn(s["line"], f"a(z) „{s['title']}” lépés panelszövege {words} szó (ajánlott ≤ {MAX_WORDS}).")
        steps.append({"title": inline(s["title"], s["line"], P, data_fmt), "html": "".join(parts), "line": s["line"], "words": words})

    if P.errors or check_only:
        return P
    meta = doc["meta"]
    content = {
        "source": md_path.name, "title": doc["title"], "titleLine": doc["titleLine"],
        "meta": {"subject": meta.get("tantárgy", ""), "grade": meta.get("évfolyam", ""), "topic": meta.get("témakör", "")},
        "steps": steps, "labels": labels, "data": data, "src": src,
    }
    out = md_path.with_suffix(".content.js")
    out.write_text(f"/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: {md_path.name}\n"
                   f"   Újragenerálás: python3 tools/build_lesson.py {md_path.relative_to(ROOT).as_posix() if md_path.is_relative_to(ROOT) else md_path.name} */\n"
                   "window.LESSON_CONTENT = " + json.dumps(content, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    P.out = out
    return P


def main(argv):
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
