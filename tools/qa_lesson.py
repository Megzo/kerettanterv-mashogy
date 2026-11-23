#!/usr/bin/env python3
"""Automatikus QA egy leckéhez: képernyőkép minden lépésről + JS-hibák + kilógó / átfedő szövegek.

    python3 tools/qa_lesson.py leckek/fizika-7-8/01-suruseg.html [opciók]

  --at T1,T2     ezekben a lépésidőkben (mp) fotóz; alap: a lépés `settle` ideje (vagy 8 mp)
                 pl. --at 1,settle  → egy korai és egy nyugalmi kép lépésenként
  --steps 1,3    csak ezek a lépések (1-től)
  --back         visszafelé léptetést is fotóz (N+1. lépésről vissza N-re) → NN-vissza.png
  --review N     review módban fotózza az N. lépést, egérrel egy feliraton és egy bekezdésen
  --half         960×540-es képek (gyorsabb átnézéshez); alap: 1920×1080
  --out DIR      kimeneti mappa; alap: build/qa/<lecke>/
  --det          determinizmus-próba: minden lépést kétszer fotóz ugyanannál az L.st-nél (közte oda-vissza
                 léptet), rögzített képkockaidővel (50 ms); eltérésnél ✗ és NN-det-a/b.png
  --states       ha a lecke megadja: window.__qaStates = {3: [{name: 'min', set(L) {…}}, …]} (kulcs: lépés
                 1-től) → minden állapotot is lefotóz (03-min.png) és ellenőriz
  --poke JSON    minden fotózott lépésnél meghívja a lecke L.poke(obj) függvényét (pl. '{"a": -2}')
  --data         kiírja az L.dat értékeit (évvel, frissítendő/előrejelzés/modell/becslés jelzővel) → data.json

Mindig fut (visszafelé kompatibilisen; a „!” sorok figyelmeztetések, a kilépési kódot nem rontják):
  · glifellenőrzés: a vászon- és panelszöveg minden karaktere benne van-e a shared/lesson.css
    @font-face unicode-range-eiben (különben rendszerfontra esik vissza, gépenként eltérő szélességgel);
  · enter() futásideje: figyelmeztetés 300 ms felett;
  · ha a lecke ad L.checks() függvényt (→ [{name, ok, got, want}]), minden képnél lefut; ok: false → ✗;
  · matematikaleckében ("math": true) a vászonfeliratokon: tizedespont, kötőjel-mínusz, *, ' (figyelmeztetés).

Ellenőrzés: konzol- és oldalhibák; a panel szövegdoboza túlcsordul-e; panel-elemek kilógnak-e;
a vásznon (L.tx-szel írt) feliratok: a panel alá lógnak-e (x > 1360), kilógnak-e a színpadról,
kisebbek-e 22 px-nél, átfedik-e egymást; hiányzó tartalomkulcs (⟨kulcs⟩).
A motor a dt-t 0,05 s-ra vágja, ezért a késői állapotokhoz a QA közvetlenül állítja az L.st-t.
"""
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent

CHECK_JS = r"""() => {
  const L = window.__lesson, out = [];
  const P = document.getElementById('lesson-panel'), pr = P.getBoundingClientRect(), sc = L.scale;
  const txt = P.querySelector('.lp-text');
  if (txt.scrollHeight > txt.clientHeight + 2) out.push(`PANEL: a szöveg nem fér el (${Math.round(txt.scrollHeight)} > ${Math.round(txt.clientHeight)} px)`);
  const ctr = P.querySelector('.lp-controls').getBoundingClientRect(), nav = P.querySelector('.lp-nav').getBoundingClientRect();
  if (ctr.height && ctr.bottom > nav.top + 1) out.push('PANEL: a vezérlők a navigációba lógnak');
  for (const e of P.querySelectorAll('*')) {
    const r = e.getBoundingClientRect(); if (!r.width) continue;
    if (r.right > pr.right + 1 || r.left < pr.left - 1) out.push(`PANEL: kilóg oldalt: <${e.tagName.toLowerCase()} class="${e.className}"> „${(e.textContent || '').trim().slice(0, 30)}”`);
    const cs = getComputedStyle(e);
    if ((cs.overflow !== 'visible' || e.tagName === 'BUTTON') && e.scrollWidth > e.clientWidth + 2 && e.clientWidth) out.push(`PANEL: vízszintes túlcsordulás: „${(e.textContent || '').trim().slice(0, 30)}”`);
  }
  if (document.getElementById('lesson-error')) out.push('HIBASÁV: ' + document.getElementById('lesson-error').textContent);
  const ms = L.marks.filter((m) => m.a > .3);
  for (const m of ms) {
    const nm = `„${m.s.slice(0, 28)}”`;
    if (m.s.includes('⟨')) out.push(`HIÁNYZÓ KULCS: ${nm}`);
    if (m.x + m.w > L.VW + 4 && m.x < 1380 + 516) out.push(`VÁSZON: a panel alá lóg (x→${Math.round(m.x + m.w)}): ${nm}`);
    if (m.x < -1 || m.y < -1 || m.y + m.h > 1081 || m.x + m.w > 1921) out.push(`VÁSZON: kilóg a színpadról: ${nm}`);
    if (m.px < 21.5) out.push(`VÁSZON: ${m.px.toFixed(1)} px < 22 px: ${nm}`);
  }
  const q = ms.filter((m) => m.qa);
  for (let i = 0; i < q.length; i++) for (let j = i + 1; j < q.length; j++) {
    const a = q[i], b = q[j];
    const w = Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x), h = Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y);
    if (w > 2 && h > 2 && w * h > .12 * Math.min(a.w * a.h, b.w * b.h)) out.push(`VÁSZON: átfedés „${a.s.slice(0, 22)}” × „${b.s.slice(0, 22)}”`);
  }
  return { problems: [...new Set(out)], marks: L.marks.length };
}"""


GLYPH_JS = r"""() => {
  const L = window.__lesson, P = document.getElementById('lesson-panel'), out = [];
  const w = document.createTreeWalker(P, NodeFilter.SHOW_TEXT);
  for (let n = w.nextNode(); n; n = w.nextNode()) {
    const t = n.textContent.trim(); if (!t || !n.parentElement || n.parentElement.closest('[hidden]')) continue;
    out.push([getComputedStyle(n.parentElement).fontFamily.split(',')[0].replace(/["']/g, '').trim(), t]);
  }
  return { marks: L.marks.filter((m) => m.a > .3).map((m) => m.s), panel: out };
}"""

CHECKS_JS = r"""() => {
  const L = window.__lesson;
  if (typeof L.checks !== 'function') return [];
  try { return (L.checks() || []).filter((c) => !c.ok).map((c) => `ELLENŐRZÉS ✗ ${c.name}` +
    (c.got !== undefined ? `: ${JSON.stringify(c.got)} ≠ várt ${JSON.stringify(c.want)}` : '')); }
  catch (e) { return ['ELLENŐRZÉS: L.checks() hibát dobott: ' + e]; }
}"""

GO_JS = "(i) => { const t0 = performance.now(); window.__lesson.go(i, true); return performance.now() - t0; }"

DET_INIT = r"""(() => {          // rögzített képkockaidő: a QA lépteti (window.__qaTick)
  let q = [], t = 1000;
  window.requestAnimationFrame = (cb) => { q.push(cb); return q.length; };
  window.__qaTick = (n = 1) => { for (let k = 0; k < n; k++) { t += 50; const cbs = q; q = []; cbs.forEach((cb) => cb(t)); } };
  window.__qaGrab = () => { const c = window.__lesson.canvas; return c.getContext('2d').getImageData(0, 0, c.width, c.height).data; };
})()"""

DET_JS = r"""([i, j, settle]) => {
  const L = window.__lesson, T = window.__qaTick;
  const at = () => { L.st = settle; L.t = 100; L.sp = L.step; T(1); };
  L.go(i, true); T(2); at(); const a = window.__qaGrab();
  L.go(j, true); T(6); L.go(i, true); T(2); at(); const b = window.__qaGrab();
  let diff = 0; for (let k = 0; k < a.length; k += 4) if (Math.abs(a[k] - b[k]) + Math.abs(a[k + 1] - b[k + 1]) + Math.abs(a[k + 2] - b[k + 2]) > 12) diff++;
  return [diff, a.length / 4];
}"""

MATH_MARK = [(re.compile(r"\d\.\d"), "tizedespont (3,14 a magyar írásmód)"),
             (re.compile(r"(?:^|\s)-\d|\d\s-\s\d"), "kötőjel-mínusz (−)"),
             (re.compile(r"\d\s*\*\s*\d"), "* szorzásjel (·)"), (re.compile(r"\d'"), "aposztróf szögperc (′)")]


def font_coverage():
    """shared/lesson.css → {család: [(tól, ig), …]} az @font-face unicode-range-ekből."""
    css = (ROOT / "shared" / "lesson.css").read_text(encoding="utf-8")
    cov = {}
    for blk in re.findall(r"@font-face\s*\{(.*?)\}", css, re.S):
        fam = re.search(r"font-family:\s*[\"']?([^;\"']+)", blk)
        ur = re.search(r"unicode-range:\s*([^;]+)", blk)
        if not fam:
            continue
        rngs = cov.setdefault(fam.group(1).strip(), [])
        for part in (ur.group(1).split(",") if ur else ["U+0-10FFFF"]):
            a, _, b = part.strip()[2:].partition("-")
            if "?" in a:
                a, b = a.replace("?", "0"), a.replace("?", "F")
            rngs.append((int(a, 16), int(b or a, 16)))
    return cov


def missing_glyphs(text, rngs):
    return sorted({ch for ch in text if not ch.isspace() and ord(ch) >= 32 and not any(a <= ord(ch) <= b for a, b in rngs)})


def main(argv):
    opts, args, i = {}, [], 0
    while i < len(argv):
        a = argv[i]
        if a in ("--at", "--steps", "--review", "--out", "--poke"):
            opts[a] = argv[i + 1]; i += 2
        elif a.startswith("--"):
            opts[a] = True; i += 1
        else:
            args.append(a); i += 1
    if not args:
        print(__doc__); return 2
    html = pathlib.Path(args[0])
    if html.suffix == ".md":
        html = html.with_suffix(".html")
    html = html.resolve()
    md, cjs = html.with_suffix(".md"), html.with_suffix(".content.js")
    if md.exists() and (not cjs.exists() or cjs.stat().st_mtime < md.stat().st_mtime):
        print(f"FIGYELEM: a {cjs.name} régebbi a .md-nél — futtasd: python3 tools/build_lesson.py {md.name}")
    out = pathlib.Path(opts.get("--out") or ROOT / "build" / "qa" / html.stem)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.png"):
        old.unlink()
    total, nwarn = 0, 0
    cov = font_coverage()
    allr = [r for rs in cov.values() for r in rs]
    is_math = bool(re.search(r'"math"\s*:\s*true', html.read_text(encoding="utf-8")))
    poke = json.loads(opts["--poke"]) if "--poke" in opts else None
    seen_glyph = set()

    def extra(pg, glyph=True):
        """Figyelmeztetések (glif, matematikai írásmód) + L.checks() hibái."""
        warns = []
        if glyph:
            g = pg.evaluate(GLYPH_JS)
            for s_ in g["marks"]:
                miss = [c for c in missing_glyphs(s_, allr) if c not in seen_glyph]
                if miss:
                    seen_glyph.update(miss)
                    warns.append(f"GLIF: nincs a fontokban: {' '.join(miss)} ({', '.join(f'U+{ord(c):04X}' for c in miss)}) – „{s_[:28]}”")
                if is_math:
                    for rx, msg in MATH_MARK:
                        if rx.search(s_):
                            warns.append(f"ÍRÁSMÓD: {msg} – „{s_[:28]}”")
            for fam, t in g["panel"]:
                miss = [c for c in missing_glyphs(t, cov.get(fam, allr)) if (fam, c) not in seen_glyph]
                if miss:
                    seen_glyph.update((fam, c) for c in miss)
                    warns.append(f"GLIF (panel, {fam}): nincs a fontban: {' '.join(miss)} – „{t[:28]}”")
        return warns, pg.evaluate(CHECKS_JS)

    def report(head, probs, warns, limit=12):
        print(head + ("✓" if not probs else f"✗ {len(probs)}") + (f"  ! {len(warns)}" if warns else ""))
        for m in probs[:limit]:
            print("     · " + m)
        if len(probs) > limit:
            print(f"     · … és még {len(probs) - limit}")
        for m in warns[:limit]:
            print("     ! " + m)

    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=.5 if "--half" in opts else 1)
        errs = []
        pg.on("pageerror", lambda e: errs.append("JS-HIBA: " + str(e).split("\n")[0]))
        pg.on("console", lambda m: errs.append("KONZOL: " + m.text) if m.type == "error" else None)

        def open_(query=""):
            pg.goto(html.as_uri() + query)
            pg.wait_for_function("window.__lesson && window.__lesson.started", timeout=15000)
            pg.wait_for_timeout(300)

        def shoot(i, t, name):
            if t is not None:
                pg.evaluate(f"(() => {{ const L = window.__lesson; L.st = {t}; L.sp = L.step; }})()")
            pg.wait_for_timeout(250)
            pg.screenshot(path=str(out / name))
            return pg.evaluate(CHECK_JS)

        open_()
        steps = pg.evaluate("window.__lesson.steps.map((s) => ({ title: s.title.replace(/<[^>]+>/g, ''), settle: s.settle || 8 }))")
        n = len(steps)
        idx = range(n) if "--steps" not in opts else [int(s) - 1 for s in opts["--steps"].split(",")]
        ats = (opts.get("--at") or "settle").split(",")
        if "--data" in opts:
            D = pg.evaluate("window.__lesson.content ? window.__lesson.content.data : {}")
            (out / "data.json").write_text(json.dumps(D, ensure_ascii=False, indent=1), encoding="utf-8")
            print("adatok (L.dat):")
            for k, d in D.items():
                val = d.get("s") or (str(d.get("v")) + (" " + d["u"] if d.get("u") else ""))
                flags = [f for f, on in (("becslés", d.get("est")), (f"{d.get('yr')}-es adat" if d.get("yr") else "", d.get("yr")),
                                          ("frissítendő", d.get("upd")), ("előrejelzés", d.get("proj")), ("modell", d.get("model"))) if on]
                print(f"   {k}: {val}" + (f"  [{', '.join(flags)}]" if flags else ""))
        states = pg.evaluate("(() => { const s = window.__qaStates || {}; const o = {}; for (const k in s) o[k] = s[k].map((x) => x.name); return o; })()") \
            if "--states" in opts else {}
        for i in idx:
            for k, at in enumerate(ats):
                errs.clear()
                ms = pg.evaluate(GO_JS, i); pg.wait_for_timeout(900)
                if poke is not None:
                    pg.evaluate("(o) => { const L = window.__lesson; if (typeof L.poke !== 'function') throw new Error('a lecke nem ad L.poke()-ot'); L.poke(o); }", poke)
                t = steps[i]["settle"] if at == "settle" else float(at)
                name = f"{i + 1:02d}" + (f"-{at}" if len(ats) > 1 else "") + ".png"
                r = shoot(i, t, name)
                warns, chk = extra(pg)
                if ms > 300:
                    warns.append(f"enter(): {ms:.0f} ms (> 300 ms – iskolai gépen lassú lehet; számolj előre kevesebbet, vagy init()-ben)")
                probs = errs + r["problems"] + chk
                total += len(probs); nwarn += len(warns)
                report(f"{i + 1:02d} {steps[i]['title'][:44]:<44} t={t:<4g} feliratok:{r['marks']:>3}  ", probs, warns)
            for sn, nm in enumerate(states.get(str(i + 1), [])):
                errs.clear()
                pg.evaluate(GO_JS, i); pg.wait_for_timeout(300)
                pg.evaluate(f"(() => {{ const L = window.__lesson; window.__qaStates[{i + 1}][{sn}].set(L); }})()")
                pg.wait_for_timeout(300)
                r = shoot(i, steps[i]["settle"], f"{i + 1:02d}-{nm}.png")
                warns, chk = extra(pg)
                probs = errs + r["problems"] + chk
                total += len(probs); nwarn += len(warns)
                report(f"{i + 1:02d} állapot „{nm}”{'':<20} ", probs, warns)
        if "--back" in opts:
            for i in [j for j in idx if j < n - 1]:
                errs.clear()
                pg.evaluate(f"window.__lesson.go({i + 1}, true)"); pg.wait_for_timeout(400)
                pg.evaluate("window.__lesson.prev()"); pg.wait_for_timeout(900)
                r = shoot(i, None, f"{i + 1:02d}-vissza.png")
                probs = errs + r["problems"]; total += len(probs)
                st = pg.evaluate("window.__lesson.st")
                print(f"{i + 1:02d} vissza ({i + 2}→{i + 1}), L.st={st:.1f}  " + ("✓" if not probs else f"✗ {len(probs)}"))
                for m in probs[:8]:
                    print("     · " + m)
        if "--review" in opts:
            s = int(opts["--review"]) - 1
            open_(f"?review#{s + 1}")
            pg.evaluate("(() => { const L = window.__lesson; L.st = (L.steps[L.step].settle || 8); })()"); pg.wait_for_timeout(300)
            m = pg.evaluate("(() => { const m = window.__lesson.marks.find((m) => m.k && m.a > .5); return m && [m.x + m.w / 2, m.y + m.h / 2]; })()")
            if m:
                pg.mouse.move(m[0], m[1]); pg.wait_for_timeout(250)
                pg.screenshot(path=str(out / f"review-{s + 1:02d}-felirat.png"))
            r = pg.evaluate("(() => { const e = document.querySelector('.lp-text [data-src]'); if (!e) return null; const r = e.getBoundingClientRect(); return [r.x + 20, r.y + r.height / 2]; })()")
            if r:
                pg.mouse.move(r[0], r[1]); pg.wait_for_timeout(250)
                pg.screenshot(path=str(out / f"review-{s + 1:02d}-panel.png"))
            print(f"review: {s + 1}. lépés → review-{s + 1:02d}-*.png")
        if "--det" in opts:
            ctx2 = b.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=.5)
            ctx2.add_init_script(DET_INIT)
            pd = ctx2.new_page()
            derr = []
            pd.on("pageerror", lambda e: derr.append("JS-HIBA: " + str(e).split("\n")[0]))
            pd.goto(html.as_uri())
            pd.wait_for_function("window.__lesson && window.__lesson.started", timeout=15000)
            pd.evaluate("document.fonts.ready.then(() => 1)"); pd.wait_for_timeout(500)
            pd.evaluate("window.__qaTick(3)")
            for i in idx:
                derr.clear()
                j = i + 1 if i < n - 1 else max(0, i - 1)
                diff, tot = pd.evaluate(DET_JS, [i, j, steps[i]["settle"]])
                probs = list(derr)
                if diff / tot > 0.0005:
                    probs.append(f"DETERMINIZMUS: ugyanannál az L.st-nél a két kép {diff} képpontban ({100 * diff / tot:.2f} %) eltér "
                                 "(seed nélküli Math.random, valós idő, képkockánként halmozott állapot?)")
                    for tag, jj in (("a", None), ("b", j)):
                        if jj is not None:
                            pd.evaluate("([j, i]) => { window.__lesson.go(j, true); window.__qaTick(6); window.__lesson.go(i, true); window.__qaTick(2); }", [jj, i])
                        else:
                            pd.evaluate("(i) => { window.__lesson.go(i, true); window.__qaTick(2); }", i)
                        pd.evaluate(f"(() => {{ const L = window.__lesson; L.st = {steps[i]['settle']}; L.t = 100; L.sp = L.step; window.__qaTick(1); }})()")
                        pd.screenshot(path=str(out / f"{i + 1:02d}-det-{tag}.png"))
                total += len(probs)
                report(f"{i + 1:02d} determinizmus (L.st={steps[i]['settle']:g}, {j + 1}. lépésen át)  ", probs, [])
            ctx2.close()
        b.close()
    if nwarn:
        print(f"! {nwarn} figyelmeztetés (glif / enter() / írásmód) – nézd át, de nem hiba")
    print(f"{'✓ nincs hiba' if not total else f'✗ {total} probléma'} · képek: {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
