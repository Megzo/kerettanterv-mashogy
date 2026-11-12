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

Ellenőrzés: konzol- és oldalhibák; a panel szövegdoboza túlcsordul-e; panel-elemek kilógnak-e;
a vásznon (L.tx-szel írt) feliratok: a panel alá lógnak-e (x > 1360), kilógnak-e a színpadról,
kisebbek-e 22 px-nél, átfedik-e egymást; hiányzó tartalomkulcs (⟨kulcs⟩).
A motor a dt-t 0,05 s-ra vágja, ezért a késői állapotokhoz a QA közvetlenül állítja az L.st-t.
"""
import pathlib
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


def main(argv):
    opts, args, i = {}, [], 0
    while i < len(argv):
        a = argv[i]
        if a in ("--at", "--steps", "--review", "--out"):
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
    total = 0
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
        for i in idx:
            for k, at in enumerate(ats):
                errs.clear()
                pg.evaluate(f"window.__lesson.go({i}, true)"); pg.wait_for_timeout(900)
                t = steps[i]["settle"] if at == "settle" else float(at)
                name = f"{i + 1:02d}" + (f"-{at}" if len(ats) > 1 else "") + ".png"
                r = shoot(i, t, name)
                probs = errs + r["problems"]
                total += len(probs)
                print(f"{i + 1:02d} {steps[i]['title'][:44]:<44} t={t:<4g} feliratok:{r['marks']:>3}  " + ("✓" if not probs else f"✗ {len(probs)}"))
                for m in probs[:12]:
                    print("     · " + m)
                if len(probs) > 12:
                    print(f"     · … és még {len(probs) - 12}")
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
        b.close()
    print(f"{'✓ nincs hiba' if not total else f'✗ {total} probléma'} · képek: {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
