#!/usr/bin/env python3
"""Matematikai / természettudományos jelek a leckék webfontjaiba (shared/fonts/*-math.woff2 stb.).

A meglévő latin + latin-ext részhalmazok (Google Fonts) nem tartalmazzák a ≤ ≥ ≈ √ π ∞ ∈ ⇌ ⁻ ₂ ⅓ …
jeleket. Ez a szkript a hivatalos forrásból (google/fonts repó, rögzített commit) letöltött teljes
fontokból részhalmazt vág, és a shared/lesson.css-ben UGYANAZON a családnéven (Fraunces,
Bricolage Grotesque, JetBrains Mono) további @font-face szabályokat generál `unicode-range`-dzsel.
Így a DOM és a vászon (ctx.font) is ugyanazt a családot használja, a leckék kódja változatlan.

Rétegek családonként (egy jel az első rétegből jön, amelyikben megvan; a meglévő latin /
latin-ext fájlokban már meglévő jelekhez nem nyúlunk):
  Fraunces       → Fraunces (teljes upstream, opsz 14) → STIX Two Text (görög, indexek, törtek)
                   → Noto Sans Math (műveleti jelek, nyilak, halmazjelek) → Noto Sans (betű-alsóindexek)
  Bricolage      → Bricolage Grotesque (teljes upstream, opsz 14, wdth 100) → Noto Sans → Noto Sans Math
  JetBrains Mono → JetBrains Mono (teljes upstream) → Noto Sans → Noto Sans Math
A tartalékfontokat `size-adjust` igazítja a fő családhoz (betűk: x-magasság, műveleti jelek:
nagybetű-magasság). Különlegesség: a JetBrains Mono mínuszjele (U+2212) ugyanaz a rajz, mint a
kötőjelé – itt a nagykötőjel (en dash) rajzát kapja, ami olyan széles, mint a + vízszintes szára.

Futtatás (a projekt gyökeréből; kell: fonttools + brotli, pl. venv-ben):
    python -m venv /tmp/fontvenv && /tmp/fontvenv/bin/pip install fonttools brotli
    /tmp/fontvenv/bin/python -I tools/build_fonts.py --download   # letöltés + manifest.json
    /tmp/fontvenv/bin/python -I tools/build_fonts.py              # hash-ellenőrzés + részhalmazolás + CSS
A letöltött fájlok (sources/fonts/, megbízhatatlan adat) gitignore-on vannak; csak a
sources/fonts/manifest.json (URL + SHA-256) kerül a repóba.
"""
import datetime
import hashlib
import io
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "sources" / "fonts"
OUT = ROOT / "shared" / "fonts"
CSS = ROOT / "shared" / "lesson.css"
BEGIN = "/* ── BEGIN generált: tools/build_fonts.py (matematikai jelek) – kézzel ne szerkeszd ── */"
END = "/* ── END generált: tools/build_fonts.py ── */"

# google/fonts repó, rögzített commit (reprodukálható letöltés)
COMMIT = "06bfe0d62a98375cb09c942fa18e68bd32cff057"
RAW = f"https://raw.githubusercontent.com/google/fonts/{COMMIT}/ofl/"
FILES = [
    "fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf", "fraunces/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf", "fraunces/OFL.txt",
    "bricolagegrotesque/BricolageGrotesque[opsz,wdth,wght].ttf", "bricolagegrotesque/OFL.txt",
    "jetbrainsmono/JetBrainsMono[wght].ttf", "jetbrainsmono/OFL.txt",
    "stixtwotext/STIXTwoText[wght].ttf", "stixtwotext/STIXTwoText-Italic[wght].ttf", "stixtwotext/OFL.txt",
    "notosans/NotoSans[wdth,wght].ttf", "notosans/OFL.txt",
    "notosansmath/NotoSansMath-Regular.ttf", "notosansmath/OFL.txt",
]

# A lefedendő jelkészlet (kódpont-tartományok)
TARGET_RANGES = [
    (0x00AC, 0x00AC), (0x00B0, 0x00B3), (0x00B5, 0x00B5), (0x00B7, 0x00B7), (0x00B9, 0x00B9),
    (0x00BC, 0x00BE), (0x00D7, 0x00D7), (0x00F7, 0x00F7),
    (0x0391, 0x03A1), (0x03A3, 0x03A9), (0x03B1, 0x03C9), (0x03D1, 0x03D1), (0x03D5, 0x03D5),
    (0x03F5, 0x03F5),                                            # görög (ϑ ϕ ϵ változatokkal)
    (0x2016, 0x2016), (0x2026, 0x2026), (0x2030, 0x2034), (0x2044, 0x2044),   # ‖ … ‰ ‱ ′ ″ ‴ ⁄
    (0x2070, 0x2071), (0x2074, 0x208E), (0x2090, 0x209C),        # felső és alsó indexek
    (0x2102, 0x2103), (0x2109, 0x2109), (0x2113, 0x2113), (0x2115, 0x2115), (0x211A, 0x211A),
    (0x211D, 0x211D), (0x2124, 0x2124), (0x2126, 0x2126), (0x212B, 0x212B),   # ℂ ℃ ℉ ℓ ℕ ℚ ℝ ℤ Ω Å
    (0x2150, 0x215E), (0x2189, 0x2189),                          # törtek
    (0x2190, 0x21FF),                                            # nyilak
    (0x2200, 0x22FF),                                            # matematikai műveleti jelek
    (0x2300, 0x2300), (0x2308, 0x230B),                          # ⌀ ⌈ ⌉ ⌊ ⌋
    (0x25A0, 0x25A1), (0x25B2, 0x25B3), (0x25B6, 0x25B6), (0x25C0, 0x25C0), (0x25CB, 0x25CB),
    (0x25CF, 0x25CF), (0x25E6, 0x25E6),                          # ■ □ ▲ △ ▶ ◀ ○ ● ◦
    (0x27C2, 0x27C2), (0x27F5, 0x27FF),                          # ⟂, hosszú nyilak
]
TARGET = sorted({c for a, b in TARGET_RANGES for c in range(a, b + 1)})

# Kimeneti fájlok: forrás, rögzített tengelyek (a wght változó marad), metrika a size-adjusthoz
OUTPUTS = {
    "fraunces-math":            ("fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf", {"opsz": 14, "SOFT": 0, "WONK": 0}),
    "fraunces-math-italic":     ("fraunces/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf", {"opsz": 14, "SOFT": 0, "WONK": 0}),
    "bricolage-grotesque-math": ("bricolagegrotesque/BricolageGrotesque[opsz,wdth,wght].ttf", {"opsz": 14, "wdth": 100}),
    "jetbrains-mono-math":      ("jetbrainsmono/JetBrainsMono[wght].ttf", {}),
    "stix-two-text-ext":        ("stixtwotext/STIXTwoText[wght].ttf", {}),
    "stix-two-text-ext-italic": ("stixtwotext/STIXTwoText-Italic[wght].ttf", {}),
    "noto-sans-ext":            ("notosans/NotoSans[wdth,wght].ttf", {"wdth": 100}),
    "noto-sans-math":           ("notosansmath/NotoSansMath-Regular.ttf", {}),
}
# Felső / alsó indexek egy fontból (a Fraunces-ből csak ⁰¹²³⁴ van, a vegyes forrás feltűnő: 10⁻³)
SUPSUB = {0x00B2, 0x00B3, 0x00B9} | set(range(0x2070, 0x209D))
# Családok: a meglévő (nem bántott) fájlok + rétegek: (kimenet, size-adjust alapja x / cap / None,
# kényszerített kódpontok – ezeket akkor is ez a réteg adja, ha a meglévő fájlban / korábbi rétegben megvannak)
FAMILIES = [
    ("Fraunces", "normal", "100 900", ["fraunces-latin", "fraunces-latin-ext"],
     [("fraunces-math", None, ()), ("stix-two-text-ext", "x", SUPSUB), ("noto-sans-math", "cap", ()), ("noto-sans-ext", "x", ())]),
    ("Fraunces", "italic", "100 900", ["fraunces-latin-italic", "fraunces-latin-ext-italic"],
     [("fraunces-math-italic", None, ()), ("stix-two-text-ext-italic", "x", SUPSUB), ("noto-sans-math", "cap", ()), ("noto-sans-ext", "x", ())]),
    ("Bricolage Grotesque", "normal", "200 800", ["bricolage-grotesque-latin", "bricolage-grotesque-latin-ext"],
     [("bricolage-grotesque-math", None, ()), ("noto-sans-ext", "x", ()), ("noto-sans-math", "cap", ())]),
    ("JetBrains Mono", "normal", "100 800", ["jetbrains-mono-latin", "jetbrains-mono-latin-ext"],
     [("jetbrains-mono-math", None, {0x2212}), ("noto-sans-ext", "x", ()), ("noto-sans-math", "cap", ())]),
]
MINUS_FIX = {"jetbrains-mono-math": "endash"}   # U+2212 → ennek a glifának a rajza
# Index-előjelek (⁺⁻⁼⁽⁾ ₊₋₌₍₎) a font saját + − = ( ) jeleiből, kicsinyített összetett glifaként,
# a ⁴ / ₄ ↔ 4 arányával és helyzetével. (A Bricolage-ből hiányoznak – a Noto Sans-é kisebb és
# máshol ül –, a JetBrains Mono ⁺-ja pedig a számjegyeknél jóval lejjebb ül: Na⁺.)
SYNTH_FROM = {0x207A: 0x2B, 0x207B: 0x2212, 0x207C: 0x3D, 0x207D: 0x28, 0x207E: 0x29,
              0x208A: 0x2B, 0x208B: 0x2212, 0x208C: 0x3D, 0x208D: 0x28, 0x208E: 0x29}
SYNTH = {"jetbrains-mono-math", "bricolage-grotesque-math"}


def synth_scripts(font):
    """Index-előjelek hozzáadása a fonthoz (cmap + glyf + hmtx + gvar); a HVAR-t eldobjuk, az
    előrelépés-változást a gvar fantompontjai adják."""
    from fontTools.ttLib.tables._g_l_y_f import Glyph, GlyphComponent
    from fontTools.pens.boundsPen import BoundsPen
    cmap, glyf, hmtx, gs = font.getBestCmap(), font["glyf"], font["hmtx"], font.getGlyphSet()

    def bounds(g):
        p = BoundsPen(gs); gs[g].draw(p); return p.bounds

    order = list(font.getGlyphOrder())
    for cp, base_cp in SYNTH_FROM.items():
        ref, ref_base = (0x2074, 0x34) if cp < 0x2080 else (0x2084, 0x34)
        rb, bb = bounds(cmap[ref]), bounds(cmap[ref_base])
        sc = (rb[3] - rb[1]) / (bb[3] - bb[1])
        dy = rb[1] - sc * bb[1]
        base = cmap[base_cp]
        adv_ref, adv_rbase, adv_base = hmtx[cmap[ref]][0], hmtx[cmap[ref_base]][0], hmtx[base][0]
        adv = round(sc * adv_base + (adv_ref - sc * adv_rbase))
        comp = GlyphComponent()
        comp.glyphName, comp.flags = base, 0
        comp.x, comp.y = round((adv - sc * adv_base) / 2), round(dy)
        comp.transform = [[sc, 0], [0, sc]]
        g = Glyph(); g.numberOfContours = -1; g.components = [comp]
        name = f"uni{cp:04X}.synth"
        order.append(name)
        font.setGlyphOrder(order)
        glyf.glyphOrder = order
        glyf.glyphs[name] = g
        g.recalcBounds(glyf)
        hmtx[name] = (adv, g.xMin)
        if "gvar" in font:
            font["gvar"].variations[name] = []
        for t in font["cmap"].tables:
            if t.isUnicode():
                t.cmap[cp] = name
    for tag in ("HVAR",):
        if tag in font:
            del font[tag]


def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def download():
    SRC.mkdir(parents=True, exist_ok=True)
    files = []
    for rel in FILES:
        url = RAW + urllib.parse.quote(rel)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (font-downloader)"})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        dst = SRC / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        files.append({"file": rel, "url": url, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        print(f"  {rel}  {len(data):>9} B")
    man = {"source": "https://github.com/google/fonts (ofl/)", "commit": COMMIT,
           "downloaded": datetime.date.today().isoformat(), "license": "SIL Open Font License 1.1",
           "files": files}
    (SRC / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def verify():
    man = json.loads((SRC / "manifest.json").read_text(encoding="utf-8"))
    bad = [f["file"] for f in man["files"] if not (SRC / f["file"]).exists() or sha256(SRC / f["file"]) != f["sha256"]]
    if bad:
        sys.exit("HIBA: hiányzó vagy eltérő hash-ű forrásfájl (futtasd --download-dal): " + ", ".join(bad))


def ranges(cps):
    out, cps = [], sorted(cps)
    i = 0
    while i < len(cps):
        j = i
        while j + 1 < len(cps) and cps[j + 1] == cps[j] + 1:
            j += 1
        out.append(f"U+{cps[i]:04X}" + (f"-{cps[j]:04X}" if j > i else ""))
        i = j + 1
    return ", ".join(out)


def main(argv):
    from fontTools.ttLib import TTFont
    from fontTools import subset
    from fontTools.varLib import instancer

    if "--download" in argv:
        download()
    verify()

    cmaps, metrics = {}, {}
    for name, (rel, _) in OUTPUTS.items():
        f = TTFont(SRC / rel, lazy=True)
        cmaps[name] = f.getBestCmap()
        upm = f["head"].unitsPerEm
        metrics[name] = {"x": f["OS/2"].sxHeight / upm, "cap": f["OS/2"].sCapHeight / upm}
        if name in SYNTH:
            cmaps[name] = {**cmaps[name], **{c: "synth" for c in SYNTH_FROM}}

    need = {name: set() for name in OUTPUTS}          # fájl → kódpontok (az összes család uniója)
    faces, report = [], []
    for fam, style, weight, base, layers in FAMILIES:
        have = set()
        for b in base:
            have |= set(TTFont(OUT / f"{b}.woff2", lazy=True).getBestCmap())
        forced = set().union(*[set(f) for _, _, f in layers])
        left = [c for c in TARGET if c not in have and c not in forced]
        base_m = metrics[layers[0][0]]
        for name, adj, force in layers:
            got = sorted({c for c in left if c in cmaps[name]} | {c for c in force if c in cmaps[name]})
            if not got:
                continue
            need[name] |= set(got)
            left = [c for c in left if c not in cmaps[name]]
            sa = f" size-adjust: {100 * base_m[adj] / metrics[name][adj]:.1f}%;" if adj else ""
            faces.append(f'@font-face {{ font-family: "{fam}"; font-style: {style}; font-weight: {weight}; '
                         f'font-display: block;{sa}\n  src: url("fonts/{name}.woff2") format("woff2");\n'
                         f'  unicode-range: {ranges(got)}; }}')
        report.append(f"{fam} {style}: hiányzik még {len(left)} jel: " + "".join(chr(c) for c in left))

    total = 0
    for name, cps in need.items():
        if not cps:
            continue
        rel, pin = OUTPUTS[name]
        font = TTFont(SRC / rel)
        if pin:
            font = instancer.instantiateVariableFont(font, pin)
        if "gvar" in font:   # a lusta gvar-szótárból hiányozhat glifa (Noto Sans) → kifejtjük
            gv = font["gvar"]
            gv.variations = {g: gv.variations.get(g, []) for g in font.getGlyphOrder()}
        if name in MINUS_FIX:
            for t in font["cmap"].tables:
                if t.isUnicode():
                    t.cmap[0x2212] = MINUS_FIX[name]
        if name in SYNTH:
            synth_scripts(font)
        opt = subset.Options()
        opt.flavor = "woff2"
        opt.hinting = False
        opt.desubroutinize = True
        opt.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]
        opt.drop_tables += ["MATH", "STAT"]
        opt.layout_features = ["kern", "mark", "mkmk", "ccmp", "locl"]
        sub = subset.Subsetter(opt)
        sub.populate(unicodes=sorted(cps))
        sub.subset(font)
        buf = io.BytesIO()
        font.flavor = "woff2"
        font.save(buf)
        (OUT / f"{name}.woff2").write_bytes(buf.getvalue())
        total += len(buf.getvalue())
        print(f"  {name}.woff2  {len(cps):>4} jel  {len(buf.getvalue()):>7} B")
    print(f"  összesen {total} B")
    for r in report:
        print("  " + r)

    css = CSS.read_text(encoding="utf-8")
    block = BEGIN + "\n" + "\n".join(faces) + "\n" + END
    if BEGIN in css:
        css = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda m: block, css, flags=re.S)
    else:  # első futás: a meglévő @font-face szabályok után
        last = [m.end() for m in re.finditer(r"@font-face \{.*?\}\n", css, flags=re.S)][-1]
        css = css[:last] + block + "\n" + css[last:]
    CSS.write_text(css, encoding="utf-8")
    print(f"  {CSS.relative_to(ROOT)} frissítve ({len(faces)} @font-face)")


if __name__ == "__main__":
    main(sys.argv[1:])
