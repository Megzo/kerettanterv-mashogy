#!/usr/bin/env python3
"""A letöltött kerettanterv-dokumentumokból (DOCX) egységes Markdown.

Bemenet:  sources/oktatas.hu_2020_nat/manifest.json + a DOCX/DOC fájlok
Köztes:   build/raw/*.md       (pandoc → GFM, változtatás nélkül)
Kimenet:  kerettanterv/<tantárgy>/<sáv>.md, _bevezeto-*.md, README.md,
          temakorok.csv, temakorok.json, ellenorzes.txt

A szöveget nem írjuk át: csak a tagolást egységesítjük (témakör = ##, a témakörön
belüli fejezetek = ###), és eltávolítjuk a pandoc-maradványokat (span-ek,
„<!-- end list -->”, listán belüli „>”).

Futtatás (a projekt gyökeréből):  python3 -I tools/build_kerettanterv.py
"""
import csv
import difflib
import html
import json
import pathlib
import re
import subprocess
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "sources" / "oktatas.hu_2020_nat"
RAW = ROOT / "build" / "raw"
OUT = ROOT / "kerettanterv"

# fájlnév → (tantárgy megjelenített neve, mappa-slug)
SUBJECT = {
    "Magyar_nyelv_es_irodalom": ("Magyar nyelv és irodalom", "magyar-nyelv-es-irodalom"),
    "magyar_nyelv_es_irodalom": ("Magyar nyelv és irodalom", "magyar-nyelv-es-irodalom"),
    "Matematika": ("Matematika", "matematika"),
    "Specialis_Matematika": ("Speciális matematika tagozat", "matematika-specialis"),
    "Etika": ("Etika", "etika"),
    "Kornyezetismeret": ("Környezetismeret", "kornyezetismeret"),
    "elo_idegen_nyelv": ("Élő idegen nyelv (első)", "idegen-nyelv-elso"),
    "masodik_elo_idegen_nyelv": ("Második élő idegen nyelv", "idegen-nyelv-masodik"),
    "Latin_nyelv": ("Latin nyelv", "latin-nyelv"),
    "Enek-zene": ("Ének-zene", "enek-zene"),
    "Vizualis_kultura": ("Vizuális kultúra", "vizualis-kultura"),
    "Technika_es_tervezes": ("Technika és tervezés", "technika-es-tervezes"),
    "Digitalis_kultura": ("Digitális kultúra", "digitalis-kultura"),
    "Testneveles": ("Testnevelés", "testneveles"),
    "Tortenelem": ("Történelem", "tortenelem"),
    "Allampolgari_ismeretek": ("Állampolgári ismeretek", "allampolgari-ismeretek"),
    "Hon_es_nepismeret": ("Hon- és népismeret", "hon-es-nepismeret"),
    "Termeszettudomany": ("Természettudomány", "termeszettudomany"),
    "Kemia": ("Kémia", "kemia"),
    "Fizika": ("Fizika", "fizika"),
    "fizika": ("Fizika", "fizika"),
    "Biologia": ("Biológia", "biologia"),
    "Foldrajz": ("Földrajz", "foldrajz"),
    "Drama_es_szinhaz": ("Dráma és színház", "drama-es-szinhaz"),
    "Mozgokepkultura_es_mediaismeret": ("Mozgóképkultúra és médiaismeret", "mozgokepkultura-es-mediaismeret"),
    "kozossegi_neveles": ("Közösségi nevelés (osztályfőnöki)", "kozossegi-neveles"),
}

SCHOOL = {
    "altisk_1-4": ("általános iskola", ""),
    "altisk_5-8": ("általános iskola", ""),
    "gimn_9-12": ("gimnázium (4 évfolyamos)", ""),
    "gimn6_7-12": ("gimnázium (6 évfolyamos)", "-hatosztalyos"),
}

# A témakörön belüli fejezetcímek egységes alakja.
SECTIONS = [
    (r"tanulási eredmények", "Tanulási eredmények"),
    (r"fejlesztési feladatok és ismeretek", "Fejlesztési feladatok és ismeretek"),
    (r"(kulcs)?fogalmak", "Fogalmak"),
    (r"javasolt tevékenységek", "Javasolt tevékenységek"),
]

DASH = "–"


def subject_of(name):
    for k in sorted(SUBJECT, key=len, reverse=True):
        if name.startswith(k):
            return SUBJECT[k]
    raise SystemExit(f"ismeretlen tantárgy: {name}")


def convert(path):
    """DOCX/DOC → nyers Markdown (gyorsítótárazva build/raw alá)."""
    RAW.mkdir(parents=True, exist_ok=True)
    out = RAW / f"{path.parent.name}__{path.stem}.md"
    if not out.exists() or out.stat().st_mtime < path.stat().st_mtime:
        if path.suffix == ".docx":
            subprocess.run(["pandoc", str(path), "-t", "gfm", "--wrap=none", "-o", str(out)], check=True)
        else:  # régi .doc: csak nyers szöveg
            txt = subprocess.run(["antiword", "-m", "UTF-8.txt", "-w", "0", str(path)],
                                 check=True, capture_output=True, text=True).stdout
            out.write_text(txt, encoding="utf-8")
    return out.read_text(encoding="utf-8")


def clean(line):
    line = re.sub(r"</?span[^>]*>", "", line)
    line = re.sub(r"^(\s*-\s+)>\s?", r"\1", line)          # „  - > szöveg”
    line = re.sub(r"^(\s+)>\s?", r"\1", line)               # behúzott „> szöveg”
    line = line.replace("****", "")
    return line.rstrip()


def plain(line):
    s = re.sub(r"<[^>]+>", "", line)
    s = html.unescape(s)
    s = re.sub(r"^\s*#+\s*", "", s)
    s = s.replace("**", "").replace("\\", "")
    s = re.sub(r"(?<!\w)\*|\*(?!\w)", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


RE_TOPIC = re.compile(r"^témakör(?: neve)?\s*:\s*(.*)$", re.I)
RE_HOURS = re.compile(r"^javasolt (?:minimum )?óraszám\s*\*?:?\*?\s*(.*)$", re.I)
RE_BAND = re.compile(
    r"^(?:(?P<mod>[A-ZÁÉÍÓÖŐÚÜŰ][^–\d]{2,40}?)\s*–\s*)?(?:a\s+|az\s+)?(?:(?:hat évfolyamos|hatosztályos) gimnázium\s+)?"
    r"(?P<a>\d{1,2})\.?(?:\s*[–-]\s*(?P<b>\d{1,2})\.)?\s*évfolyam(?:ok|a)?(?:\s+számára)?:?$", re.I)


# Egy dokumentumon belüli párhuzamos változatok: nyelvek, modulok.
RE_VARIANT = re.compile(r"^(?:élő idegen nyelv:\s*(?P<lang>angol|német)|(?P<modul>modul „(?P<ml>[a-d])”)\s*:\s*(?P<mname>.+))$", re.I)


def variant_label(m):
    if m.group("lang"):
        return m.group("lang").capitalize()
    return f"Modul „{m.group('ml').upper()}”: {m.group('mname').strip()}"


def mod_slug(mod):
    if not mod:
        return ""
    m = re.match(r"Modul „([A-D])”", mod)
    if m:
        return "-modul-" + m.group(1).lower()
    a = unicodedata.normalize("NFKD", mod).encode("ascii", "ignore").decode().lower()
    return "-" + re.sub(r"[^a-z0-9]+", "-", a).strip("-")


def band_str(m):
    a, b = m.group("a"), m.group("b")
    return f"{a}{DASH}{b}" if b else a


def section_label(p):
    q = p.rstrip(":").strip().lower()
    for pat, label in SECTIONS:
        if re.fullmatch(pat, q):
            return label
    return None


def is_table_line(line):
    s = line.lstrip()
    return s.startswith("|") or s.startswith("<")


def parse_overview_tables(lines):
    """Az áttekintő táblázatok sorai: [(sorindex, [(név, óraszám-szöveg), ...])]."""
    tables = []
    i = 0
    n = len(lines)
    while i < n:
        s = lines[i].lstrip()
        if s.startswith("|"):
            j = i
            rows = []
            while j < n and lines[j].lstrip().startswith("|"):
                cells = [plain(c) for c in lines[j].strip().strip("|").split("|")]
                rows.append(cells)
                j += 1
            tables.append((i, rows))
            i = j
            continue
        if s.startswith("<table"):
            j = i
            buf = []
            while j < n and "</table>" not in lines[j]:
                buf.append(lines[j])
                j += 1
            buf.append(lines[j] if j < n else "")
            t = "\n".join(buf)
            rows = []
            for tr in re.findall(r"<tr.*?</tr>", t, re.S):
                cells = [plain(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, re.S)]
                rows.append(cells)
            tables.append((i, rows))
            i = j + 1
            continue
        i += 1
    out = []
    for idx, rows in tables:
        hdr_i = None
        for k, r in enumerate(rows[:3]):
            if any(re.fullmatch(r"(kerettantervi )?témakör(ök)?( neve| megnevezése)?|tematikai egység", c, re.I) for c in r) and \
               any("óraszám" in c.lower() for c in r):
                hdr_i = k
                break
        if hdr_i is None:
            continue
        hdr = rows[hdr_i]
        ni = next(k for k, c in enumerate(hdr) if re.fullmatch(r"(kerettantervi )?témakör(ök)?( neve| megnevezése)?|tematikai egység", c, re.I))
        hi = next(k for k, c in enumerate(hdr) if "óraszám" in c.lower())
        items = []
        for r in rows[hdr_i + 1:]:
            if len(r) <= max(ni, hi):
                continue
            name, hrs = r[ni], r[hi]
            if not name or re.match(r"^-+$", name):
                continue
            if re.search(r"összes|szabadon|^óraszám|^összesen", name, re.I):
                continue
            items.append((name, hrs))
        if items:
            out.append((idx, items))
    return out


def norm_name(s):
    s = re.sub(r"\(\s*[\d,\s]+\)\s*$", "", s)  # „(2, 4)” Nat-hivatkozás a táblázatban
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[^\w]+", " ", s).strip()
    return s


def parse_doc(text, default_band):
    lines = [clean(l) for l in text.split("\n")]
    lines = [l for l in lines if l.strip() != "<!-- end list -->"]

    # 1) jelölők
    bands = []    # (sorindex, sáv, modul)
    topics = []   # sorindex
    variants = [] # (sorindex, címke)
    for i, l in enumerate(lines):
        if is_table_line(l):
            continue
        p = plain(l)
        if not p:
            continue
        mv = RE_VARIANT.match(p)
        if mv and len(p) < 120:
            variants.append((i, variant_label(mv)))
            continue
        m = RE_BAND.match(p)
        if m and len(p) < 70:
            bands.append((i, band_str(m), (m.group("mod") or "").strip()))
            continue
        if RE_TOPIC.match(p):
            topics.append(i)

    # 2) témakörök
    def band_at(i):
        cur = (default_band, "")
        var = ""
        for vi, v in variants:
            if vi < i:
                var = v
        for bi, b, mod in bands:
            if bi < i:
                cur = (b, mod)
        return (cur[0], cur[1] or var)

    def next_boundary(i):
        cands = [t for t in topics if t > i] + [b for b, _, _ in bands if b > i] + \
                [v for v, _ in variants if v > i] + [len(lines)]
        return min(cands)

    result = []
    for ti in topics:
        p = plain(lines[ti])
        title = RE_TOPIC.match(p).group(1).strip()
        k = ti + 1
        if not title:  # a cím a következő nem üres sorban
            while k < len(lines) and not plain(lines[k]):
                k += 1
            title = plain(lines[k]) if k < len(lines) else ""
            k += 1
        end = next_boundary(ti)
        body = lines[k:end]
        hours = ""
        out_body = []
        for l in body:
            pl = plain(l)
            mh = RE_HOURS.match(pl)
            if mh and not hours and not is_table_line(l):
                hours = mh.group(1).strip()
                continue
            out_body.append(l)
        band, mod = band_at(ti)
        result.append({"line": ti, "band": band, "module": mod, "title": title,
                       "hours_raw": hours, "body": tidy_body(out_body)})

    # 3) sávok bevezetője: a sávjelölő és az első témakör (vagy következő sáv) közötti szöveg
    first_marker = min([t for t in topics] + [b for b, _, _ in bands] + [v for v, _ in variants] + [len(lines)])
    intro = "\n".join(lines[:first_marker]).strip()
    for vi, v in variants:  # a változatok (nyelv, modul) saját bevezetője a _bevezeto fájlba
        txt = "\n".join(lines[vi + 1:next_boundary(vi)]).strip()
        intro += f"\n\n## {v}\n\n{txt}"
    band_intros = {}
    for bi, b, mod in bands:
        end = next_boundary(bi)
        txt = "\n".join(lines[bi + 1:end]).strip()
        key = (b, mod)
        band_intros[key] = (band_intros.get(key, "") + "\n\n" + txt).strip()

    # 4) áttekintő táblázatok, sávhoz rendelve
    overview = {}
    for idx, items in parse_overview_tables(lines):
        nxt = [t for t in topics if t > idx]   # a táblázat az utána következő témakörök sávjához tartozik
        key = band_at(nxt[0]) if nxt else band_at(idx)
        overview.setdefault(key, []).append(items)

    return {"intro": intro, "band_intros": band_intros, "topics": result,
            "overview": overview, "bands": bands}


def tidy_body(lines):
    """A témakör belsejének egységesítése: ismert fejezetcímek → ###, más fejléc → félkövér."""
    out = []
    prev_label = None
    for l in lines:
        p = plain(l)
        lab = section_label(p) if p and not is_table_line(l) and len(p) < 60 else None
        if lab:
            out.append(f"### {lab}")
            prev_label = lab
            continue
        if re.match(r"^\s*#+\s", l):  # a pandoc által fejléccé tett bekezdés
            l = re.sub(r"^\s*#+\s*", "", l)
            if prev_label != "Fogalmak":
                l = f"**{l}**" if "**" not in l else l
        out.append(l)
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip()
    return txt


def hours_int(s):
    m = re.match(r"^\**\s*(\d+)\s*(?:(?:tan)?óra|$)", s.replace("*", "").strip())
    return int(m.group(1)) if m else None


def band_slug(b):
    return b.replace(DASH, "-")


def main():
    man = json.loads((SRC / "manifest.json").read_text(encoding="utf-8"))
    report = []
    rows = []          # összesítő (CSV/JSON)
    summary = {}       # (tantárgy, sáv-fájl) → adatok a README-hez
    OUT.mkdir(exist_ok=True)

    for f in man["files"]:
        path = SRC / f["file"]
        name = path.stem
        subj, slug = subject_of(name)
        school, suffix = SCHOOL[f["band"]]
        mband = re.search(r"(\d{1,2})\.?(?:\s*[–-]\s*(\d{1,2}))?\.\s*évfolyam", f["title"])
        if mband:
            doc_band = f"{mband.group(1)}{DASH}{mband.group(2)}" if mband.group(2) else mband.group(1)
        else:
            doc_band = f["band"].split("_")[1].replace("-", DASH)
        text = convert(path)
        d = OUT / slug
        d.mkdir(exist_ok=True)
        src_line = (f"> **Forrás:** [{f['title']}]({f['url']}) – Oktatási Hivatal, "
                    f"[NAT 2020 kerettantervek]({man['source_index']}) · letöltve: {man['downloaded']}  \n"
                    f"> **Iskolatípus:** {school} · **Eredeti fájl:** `sources/oktatas.hu_2020_nat/{f['file']}`  \n"
                    f"> Gépi konverzió: a szöveg a forrásé, csak a tagolás egységesített.")

        if path.suffix == ".doc":
            fn = d / f"{band_slug(doc_band)}{suffix}.md"
            fn.write_text(f"# {subj} · {doc_band}. évfolyam\n\n{src_line}\n\n"
                          f"> ⚠ Régi .doc formátum, régi típusú „tematikai egység” szerkezet – "
                          f"csak nyers szövegként konvertálva.\n\n```text\n{text.strip()}\n```\n",
                          encoding="utf-8")
            report.append(f"[NYERS] {f['file']}: .doc, csak nyers szöveg")
            summary[(subj, fn.name)] = {"subject": subj, "slug": slug, "file": fn.name, "school": school,
                                         "band": doc_band, "n": None, "hours": None, "table_n": None,
                                         "table_hours": None, "status": "nyers szöveg (.doc)"}
            continue

        doc = parse_doc(text, doc_band)
        intro_fn = d / f"_bevezeto-{band_slug(doc_band)}{suffix}.md"
        intro_fn.write_text(f"# {subj} – bevezető ({doc_band}. évfolyam)\n\n{src_line}\n\n{doc['intro']}\n",
                            encoding="utf-8")

        # sávonként csoportosítás (a modul – pl. „Biológia – 11. évfolyam” – külön fájl)
        groups = {}
        for t in doc["topics"]:
            groups.setdefault((t["band"], t["module"]), []).append(t)
        if not groups:
            report.append(f"[HIBA] {f['file']}: egyetlen témakört sem találtam")
        for (band, mod), topics in groups.items():
            fn = d / f"{band_slug(band)}{mod_slug(mod)}{suffix}.md"
            title = f"{subj} · {band}. évfolyam" + (f" · {mod}" if mod else "")
            parts = [f"# {title}", "", src_line, ""]
            parts += ["## Témakörök áttekintése", "", "| # | Témakör | Javasolt óraszám |", "|---|---|---|"]
            total = 0
            for k, t in enumerate(topics, 1):
                h = hours_int(t["hours_raw"])
                total += h or 0
                parts.append(f"| {k} | {t['title'].replace('|', '/')} | {t['hours_raw'] or '–'} |")
            parts.append(f"| | **Összesen** | **{total} óra** |")
            parts.append("")
            bi = doc["band_intros"].get((band, mod), "")
            if bi:
                parts += ["## A sáv bevezetője (a forrásból)", "", bi, ""]
            for k, t in enumerate(topics, 1):
                parts += [f"## {k}. {t['title']}", "", f"**Javasolt óraszám:** {t['hours_raw'] or '–'}", "", t["body"], ""]
                rows.append({"tantargy": subj, "iskolatipus": school, "sav": band, "modul": mod,
                             "sorszam": k, "temakor": t["title"], "javasolt_oraszam": hours_int(t["hours_raw"]),
                             "oraszam_szoveg": t["hours_raw"], "fajl": f"{slug}/{fn.name}",
                             "forras": f["url"]})
            fn.write_text(re.sub(r"\n{3,}", "\n\n", "\n".join(parts)).strip() + "\n", encoding="utf-8")

            # ellenőrzés az áttekintő táblázattal
            names = [norm_name(t["title"]) for t in topics]

            def check(ov):
                tnames = [norm_name(n) for n, _ in ov]
                missing = [n for n, _ in ov if not difflib.get_close_matches(norm_name(n), names, 1, 0.75)]
                extra = [t["title"] for t in topics if not difflib.get_close_matches(norm_name(t["title"]), tnames, 1, 0.75)]
                t_hours = sum(hours_int(h + " óra") or 0 for _, h in ov)
                if missing or extra or len(ov) != len(topics):
                    st = f"eltérés: táblázat {len(ov)} / szöveg {len(topics)}"
                elif t_hours != total:
                    st = f"óraszám-eltérés: táblázat {t_hours} / szöveg {total}"
                else:
                    st = "OK"
                return (st != "OK", len(missing) + len(extra)), st, missing, extra, t_hours, ov

            # ha több (alternatív) táblázat van, a legjobban egyezőt vesszük
            tables = doc["overview"].get((band, mod), [])
            if tables:
                _, status, missing, extra, t_hours, ov = min((check(t) for t in tables), key=lambda r: r[0])
                if len(tables) > 1:
                    status += f" ({len(tables)} táblázat közül a legjobb)"
            else:
                status, missing, extra, t_hours, ov = "nincs áttekintő táblázat", [], [], 0, []
            no_h = [t["title"] for t in topics if hours_int(t["hours_raw"]) is None]
            report.append(f"[{'OK' if status.startswith('OK') else 'NÉZD'}] {f['file']} → {slug}/{fn.name}: "
                          f"{len(topics)} témakör, {total} óra; {status}")
            for n in missing:
                report.append(f"      táblázatban van, szövegben nincs: {n}")
            for n in extra:
                report.append(f"      szövegben van, táblázatban nincs: {n}")
            for n in no_h:
                report.append(f"      nem egész óraszám: {n}")
            summary[(subj, fn.name)] = {"subject": subj, "slug": slug, "file": fn.name, "school": school,
                                         "band": band + (f" ({mod})" if mod else ""), "n": len(topics),
                                         "hours": total, "table_n": len(ov) if ov else None,
                                         "table_hours": t_hours if ov else None, "status": status}

    # összesítők
    with open(OUT / "temakorok.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    (OUT / "temakorok.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "ellenorzes.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
    write_readme(man, summary, rows)
    print("\n".join(report))
    print(f"\n{len(rows)} témakör, {len(summary)} sáv-fájl → {OUT}")


def write_readme(man, summary, rows):
    order = ["általános iskola", "gimnázium (4 évfolyamos)", "gimnázium (6 évfolyamos)"]
    L = ["# Kerettantervek (NAT 2020) – Markdown", "",
         f"- **Forrás:** Oktatási Hivatal – [A 2020-as NAT-hoz illeszkedő tartalmi szabályozók]({man['source_index']})",
         f"- **Letöltve:** {man['downloaded']} · az eredeti fájlok: `sources/oktatas.hu_2020_nat/` (`manifest.json`: URL + SHA-256)",
         "- **Hatály:** a kerettantervek 2020. szeptember 1-jétől felmenő rendszerben (1., 5., 9., ill. a 6 évfolyamos "
         "gimnáziumok 7. évfolyamán) bevezetett Nat 2020-hoz tartoznak (OH tájékoztató). A 8 évfolyamos gimnáziumoknak "
         "nincs külön kerettanterve (az 5–8. és 9–12. évfolyamosakat használják); a technikum a gimnáziumi kerettanterveket használja.",
         "- **Nem része:** szakképző iskola, felnőttoktatás, nemzetiségi, SNI- és két tanítási nyelvű kerettantervek, "
         "a „7. melléklet” szerinti választható kerettantervek.",
         "- **Konverzió:** `tools/build_kerettanterv.py` (pandoc). A szöveg a forrásé; a tagolás egységesített. "
         "Ellenőrzési napló: [`ellenorzes.txt`](ellenorzes.txt).", "",
         f"Összesen **{len(rows)} témakör**. A „táblázat” oszlop a dokumentum saját áttekintő táblázata, "
         "ezzel vetettük össze a szövegből kinyert témaköröket.", "",
         "### Az ellenőrzés eltéréseinek tipikus okai", "",
         "Az eltérések többsége **a forrásdokumentumon belüli** (táblázat ≠ részletes szöveg), nem konverziós hiba:", "",
         "- A táblázatban olyan sor van, amihez nincs kifejtett témakör: „Évente két mélységelvű téma” (történelem), "
         "„Rendszerező összefoglalás” (matematika 11–12.), „Ismétlés, felkészülés az érettségire”, „Téli tevékenységek” (technika C modul).",
         "- A témakör címe a táblázatban és a szövegben kicsit más (pl. „A dualizmus kori Magyarország” ↔ „A dualizmus kora”), "
         "vagy egy táblázatsor a szövegben két témakörre bomlik (földrajz 7–8.: Európa / Európán kívüli kontinensek).",
         "- Óraszám: hiányzó vagy eltérő érték a táblázatban (pl. fizika 9–10. hat évf.: üres cella), "
         "változatonként megadott óraszám (dráma: „A változat: 3 óra, B változat: 1 óra”; ének-zene: osztályonként), "
         "vagy nem számszerű (gyógytestnevelés).",
         "- **Magyar nyelv és irodalom:** hierarchikus szerkezet (nagy témakör → szerzők/művek saját óraszámmal); "
         "a résztémák a témakör szövegében megvannak, de az áttekintő táblázat sorai nem feleltethetők meg 1:1-ben. "
         "Ezt a tárgyat érdemes külön átnézni.",
         "- Latin nyelv, mozgóképkultúra: régi .doc, régi típusú szerkezet – csak nyers szövegként.", ""]
    for sch in order:
        items = sorted([v for v in summary.values() if v["school"] == sch], key=lambda v: (v["subject"], v["file"]))
        if not items:
            continue
        L += [f"## {sch[0].upper() + sch[1:]}", "", "| Tantárgy | Sáv | Témakör | Óraszám | Táblázat | Ellenőrzés |",
              "|---|---|---|---|---|---|"]
        for v in items:
            tab = f"{v['table_n']} / {v['table_hours']} óra" if v["table_n"] else "–"
            L.append(f"| {v['subject']} | [{v['band']}]({v['slug']}/{v['file']}) | {v['n'] if v['n'] is not None else '–'} | "
                     f"{v['hours'] if v['hours'] is not None else '–'} | {tab} | {v['status']} |")
        L.append("")
    (OUT / "README.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
