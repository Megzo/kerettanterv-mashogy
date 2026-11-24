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
                 léptet), rögzített képkockaidővel (50 ms); eltérésnél ✗ és NN-det-a/b.png. Ha a lecke ad
                 idle()-t (Lesson.create({idle})), és az a settle-nél még false (pl. visszalépéskor a settle-től
                 induló kamera), mindkét képnél ugyanannyi képkockát vár tovább (a fejlécben: „+ K képkocka”).
  --states       ha a lecke megadja: window.__qaStates = {3: [{name: 'min', set(L) {…}}, …]} (kulcs: lépés
                 1-től) → minden állapotot is lefotóz (03-min.png) és ellenőriz. Sorrend (v2): a lépésre lép,
                 L.st = settle (vagy az állapot st-je: {name, st: 2.5, set}), lefut a set(L) (set nélkül –
                 {name, st: 1.5} – csak az időt állítja: a lépés egy köztes pillanata), és wait ms (alap
                 250; {wait: 600}) múlva exponál – az L.st-t utána már nem állítja, így az L.st-hez kötött
                 állapot (S.t0 = L.st − 2 → „2 mp-cel az indítás után”) a saját idejét mutatja (± a wait).
                 Figyelmeztet („! ÁLLAPOT”), ha a vászon rögzített képkockaidővel képpontra ugyanaz, mint
                 az állapot nélkül (a set() nem hatott – vagy az állapot a lépés alapképe, pl. a túra vége).
                 A kulcs 1-alapú lépésszám; érvénytelen kulcsra (0, > lépésszám) figyelmeztet.
  --poke JSON    minden fotózott lépésnél meghívja a lecke L.poke(obj) függvényét (pl. '{"a": -2}')
  --data         kiírja az L.dat értékeit (évvel, frissítendő/előrejelzés/modell/becslés jelzővel) → data.json
  --no-jump      kihagyja az ugrópróbát (alapból fut, lásd lent); --jump-only: csak az ugrópróba fut
  --glyphs       glifpróba a magyar és verstani jelekre (magyarleckében alapból fut, lásd lent)

Mindig fut (visszafelé kompatibilisen; a „!” sorok figyelmeztetések, a kilépési kódot nem rontják):
  · idle: ha a lecke ad idle()-t, a settle- és a visszalépés-képek előtt megvárja (max. 5 mp); a --at-tal kért
    köztes képek (--at 1.5) és az állapotképek előtt nem (azok egy mozgás közbeni pillanat fotói);
  · glifellenőrzés: a vászon- és panelszöveg minden karaktere benne van-e a shared/lesson.css
    @font-face unicode-range-eiben (különben rendszerfontra esik vissza, gépenként eltérő szélességgel);
    v2: a vászonfeliratot a saját családja szerint nézi (a motor a marks[].f-ben adja a fontot; régi motornál az
    összes család együtt), és a böngészőben azt is megméri, hogy a fontfájlban tényleg van-e rajz a jelhez (a
    unicode-range csak ígéret: pl. U+2000-206F, de a ‿ nincs benne) – ha nincs, „GLIF … tartalékfontra esik”;
  · magyar- és verstani glifpróba (magyarlecke – content.meta.subject „Magyar…” – vagy --glyphs): ő ű Ő Ű ‚ ’ „ ” – —
    ∪ × [ ] mind a négy fontváltozatban (Fraunces, Fraunces dőlt, Bricolage Grotesque, JetBrains Mono); tájékoztató sor;
  · hangpróba: AudioContext csak felhasználói gesztus (kattintás) után jöhet létre („! HANG”), hangforrás (oszcillátor,
    <audio>) nem indulhat kattintás nélkül, gépi felolvasás (speechSynthesis) nincs – ezek ✗ hibák. A QA nem kattint,
    így minden hang, ami a QA alatt indul, „magától” indult (betöltéskor vagy lépésbelépéskor);
  · enter() futásideje: figyelmeztetés 300 ms felett;
  · ha a lecke ad L.checks() függvényt (→ [{name, ok, got, want}]), minden képnél lefut; ok: false → ✗;
  · matematikaleckében ("math": true) a vászonfeliratokon: tizedespont, kötőjel-mínusz, *, ' (figyelmeztetés);
  · ugrópróba (rögzített képkockaidővel): 1. → utolsó, utolsó → 1., 6 véletlen (seedelt) ugrás számbillentyű-
    szerűen (L.go, áttűnéssel – a köztes jelenetek is rajzolódnak, az enter()-jük nélkül!), és betöltés
    közvetlenül az utolsó lépésre (URL #N); bármely JS-hiba ✗. (Egy draw()-ban dobott hiba a motor
    főciklusát leállítja: a lecke megfagy.)

Ellenőrzés: konzol- és oldalhibák; a panel szövegdoboza túlcsordul-e; panel-elemek kilógnak-e;
a vásznon (L.tx-szel írt) feliratok: a panel alá lógnak-e (x > 1360), kilógnak-e a színpadról,
kisebbek-e 22 px-nél, átfedik-e egymást (forgatott feliratnál a forgatott téglalappal), takarja-e
egy L.pill doboza (bg/bd) egy másik feliratot; hiányzó tartalomkulcs (⟨kulcs⟩).
A motor a dt-t 0,05 s-ra vágja, ezért a késői állapotokhoz a QA közvetlenül állítja az L.st-t.
"""
import json
import pathlib
import re
import sys
import unicodedata

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
  // forgatott felirat (m.q: 4 sarok) → konvex sokszögek metszetének területe; a pill doboza (m.pb / m.pq) is
  const rect = (r) => [[r.x, r.y], [r.x + r.w, r.y], [r.x + r.w, r.y + r.h], [r.x, r.y + r.h]];
  const area = (P) => { let s = 0; for (let i = 0; i < P.length; i++) { const [x1, y1] = P[i], [x2, y2] = P[(i + 1) % P.length]; s += x1 * y2 - x2 * y1; } return Math.abs(s) / 2; };
  const orient = (P) => { let s = 0; for (let i = 0; i < P.length; i++) { const [x1, y1] = P[i], [x2, y2] = P[(i + 1) % P.length]; s += x1 * y2 - x2 * y1; } return s < 0 ? P.slice().reverse() : P; };
  const clipArea = (A, B) => {          // Sutherland–Hodgman: A ∩ B (mindkettő konvex)
    let out = orient(A); B = orient(B);
    for (let i = 0; i < B.length && out.length; i++) {
      const [ax, ay] = B[i], [bx, by] = B[(i + 1) % B.length], inp = out; out = [];
      const side = (p) => (bx - ax) * (p[1] - ay) - (by - ay) * (p[0] - ax);
      for (let j = 0; j < inp.length; j++) {
        const P = inp[j], Q = inp[(j + 1) % inp.length], sp = side(P), sq = side(Q);
        if (sp >= 0) out.push(P);
        if ((sp >= 0) !== (sq >= 0)) { const t = sp / (sp - sq); out.push([P[0] + (Q[0] - P[0]) * t, P[1] + (Q[1] - P[1]) * t]); }
      }
    }
    return out.length > 2 ? area(out) : 0;
  };
  const q = ms.filter((m) => m.qa);
  const hit = (a, b) => {
    if (a.q || b.q) { const A = a.q || rect(a), B = b.q || rect(b); return clipArea(A, B) > Math.max(4, .12 * Math.min(area(A), area(B))); }
    const w = Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x), h = Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y);
    return w > 2 && h > 2 && w * h > .12 * Math.min(a.w * a.h, b.w * b.h);
  };
  for (let i = 0; i < q.length; i++) for (let j = i + 1; j < q.length; j++) {
    const a = q[i], b = q[j];
    if (hit(a, b)) { out.push(`VÁSZON: átfedés „${a.s.slice(0, 22)}” × „${b.s.slice(0, 22)}”`); continue; }
    for (const [p, t] of [[a, b], [b, a]]) {    // a pill doboza takarja a másik feliratot (vagy az a pillre lóg)
      if (!p.pb) continue;
      const T = t.q || rect(t), Pb = p.pq || rect(p.pb), ov = clipArea(T, Pb);
      if (ov > Math.max(4, .12 * area(T))) { out.push(`VÁSZON: a(z) „${p.s.slice(0, 22)}” doboza (pill) takarja: „${t.s.slice(0, 22)}”`); break; }
    }
  }
  return { problems: [...new Set(out)], marks: L.marks.length };
}"""


GLYPH_JS = r"""() => {
  const L = window.__lesson, P = document.getElementById('lesson-panel'), out = [];
  const w = document.createTreeWalker(P, NodeFilter.SHOW_TEXT);
  for (let n = w.nextNode(); n; n = w.nextNode()) {
    const t = n.textContent.trim(); if (!t || !n.parentElement || n.parentElement.closest('[hidden]')) continue;
    const cs = getComputedStyle(n.parentElement);
    out.push([cs.fontFamily.split(',')[0].replace(/["']/g, '').trim(), t, cs.fontStyle !== 'normal']);
  }
  return { marks: L.marks.filter((m) => m.a > .3).map((m) => [m.s, m.f || null]), panel: out };
}"""

CHECKS_JS = r"""() => {
  const L = window.__lesson;
  if (typeof L.checks !== 'function') return [];
  try { return (L.checks() || []).filter((c) => !c.ok).map((c) => `ELLENŐRZÉS ✗ ${c.name}` +
    (c.got !== undefined ? `: ${JSON.stringify(c.got)} ≠ várt ${JSON.stringify(c.want)}` : '')); }
  catch (e) { return ['ELLENŐRZÉS: L.checks() hibát dobott: ' + e]; }
}"""

# hangpróba: a lecke kódja előtt fut; naplózza, ha AudioContext jön létre / hang indul, és volt-e előtte (5 mp-en belül)
# valódi felhasználói bemenet (isTrusted pointerdown / keydown / click). A navigator.userActivation itt nem jó: a
# Playwright evaluate()-je gesztusnak számít. A QA maga nem kattint, így nála minden hang „magától” szól.
AUDIO_INIT = r"""(() => {
  const log = window.__qaAudio = [];
  let last = -1e9;
  for (const t of ['pointerdown', 'keydown', 'click', 'touchend']) window.addEventListener(t, (e) => { if (e.isTrusted) last = performance.now(); }, true);
  const act = () => performance.now() - last < 5000;
  for (const n of ['AudioContext', 'webkitAudioContext']) {
    const C = window[n]; if (typeof C !== 'function') continue;
    const W = function (...a) { log.push({ ev: 'ctx', g: act() }); return new C(...a); };
    W.prototype = C.prototype; Object.setPrototypeOf(W, C); window[n] = W;
  }
  const wrap = (proto, name, ev) => { if (!proto || typeof proto[name] !== 'function') return; const f = proto[name];
    proto[name] = function (...a) { log.push({ ev, g: act() }); return f.apply(this, a); }; };
  if (window.AudioScheduledSourceNode) wrap(AudioScheduledSourceNode.prototype, 'start', 'start');
  if (window.HTMLMediaElement) wrap(HTMLMediaElement.prototype, 'play', 'media');
  if (window.speechSynthesis) wrap(Object.getPrototypeOf(window.speechSynthesis), 'speak', 'tts');
})()"""
AUDIO_JS = "(() => (window.__qaAudio || []).splice(0))()"


def audio_problems(evs):
    """A hangnapló → (hibák, figyelmeztetések). Gesztus közben (g: true) minden megengedett."""
    probs, warns = [], []
    bad = [e["ev"] for e in evs if not e.get("g")]
    if "ctx" in bad:
        warns.append(f"HANG: AudioContext felhasználói kattintás nélkül jött létre ({bad.count('ctx')}×) – csak a ▶ gomb hozza létre")
    if "start" in bad or "media" in bad:
        probs.append(f"HANG: hang indult kattintás nélkül ({bad.count('start') + bad.count('media')}×) – a hang csak kattintásra szólhat")
    if "tts" in bad or any(e["ev"] == "tts" for e in evs):
        probs.append("HANG: gépi felolvasás (speechSynthesis) – nem használható")
    return probs, warns


# glifpróba a böngészőben: van-e rajz a fontfájlban? (ha nincs, a "Fam", monospace és a monospace – és a serif-es pár –
# ugyanazzal a tartalékfonttal rajzol, tehát pontosan ugyanolyan széles)
GLYPH_REAL_JS = r"""async (items) => {
  const c = document.createElement('canvas').getContext('2d'), out = [];
  const w = (f, ch) => { c.font = f; return c.measureText(ch).width; };
  for (const [fam, it, ch] of items) {
    const st = it ? 'italic ' : '';
    try { await document.fonts.load(`${st}40px "${fam}"`, ch); } catch (e) { /* nincs ilyen font */ }
    if (w(`${st}40px "${fam}", monospace`, ch) === w(`${st}40px monospace`, ch) &&
        w(`${st}40px "${fam}", serif`, ch) === w(`${st}40px serif`, ch)) out.push([fam, it, ch]);
  }
  return out;
}"""
HU_PROBE = "őűŐŰ‚’„”–—∪×[]"
HU_FACES = [("Fraunces", False), ("Fraunces", True), ("Bricolage Grotesque", False), ("JetBrains Mono", False)]


def font_of(css_font):
    """'italic 500 24px "JetBrains Mono"' → ('JetBrains Mono', True); ismeretlennél (None, False)."""
    if not css_font:
        return None, False
    m = re.search(r"[\d.]+px(?:/[\d.]+)?\s+(.+)$", css_font)
    fam = m.group(1).split(",")[0].strip().strip("\"'") if m else None
    return fam, bool(re.match(r"\s*(italic|oblique)\b", css_font))


GO_JS = "(i) => { const t0 = performance.now(); window.__lesson.go(i, true); return performance.now() - t0; }"

DET_INIT = r"""(() => {          // rögzített képkockaidő: a QA lépteti (window.__qaTick)
  let q = [], t = 1000;
  window.requestAnimationFrame = (cb) => { q.push(cb); return q.length; };
  window.__qaTick = (n = 1) => { for (let k = 0; k < n; k++) { t += 50; const cbs = q; q = []; cbs.forEach((cb) => cb(t)); } };
  window.__qaGrab = () => { const c = window.__lesson.canvas; return c.getContext('2d').getImageData(0, 0, c.width, c.height).data; };
})()"""

DET_JS = r"""([i, j, settle]) => {
  const L = window.__lesson, T = window.__qaTick;
  // a: i-re lépve; b: j-ről vissza i-re. Mindkettő L.st = settle-nél (L.t = 100). Ha a lecke ad idle()-t
  // (Lesson.create({idle})), és az a settle-nél még false (pl. visszalépéskor a settle-től induló kamera),
  // mindkét kép előtt ugyanannyi (K) képkockát léptet tovább, ahány a lassabbiknak kell – így a kép ugyanannál
  // az L.st-nél és L.t-nél készül, és a nyugalmi állapotot hasonlítja össze.
  const idle = () => typeof L.idle !== 'function' || L.idle();
  const pin = (k) => { L.st = settle; L.t = 100; L.sp = L.step; T(1 + k); };
  const A = (k) => { L.go(i, true); T(2); pin(k); }, B = (k) => { L.go(j, true); T(6); L.go(i, true); T(2); pin(k); };
  const wait = () => { let k = 0; while (k < 100 && !idle()) { T(1); k++; } return k; };
  A(0); const ka = wait(); let a = ka ? null : window.__qaGrab();
  B(0); const kb = wait(); let b = kb ? null : window.__qaGrab();
  const K = Math.max(ka, kb);
  if (K) { A(K); a = window.__qaGrab(); B(K); b = window.__qaGrab(); }
  let diff = 0; for (let k = 0; k < a.length; k += 4) if (Math.abs(a[k] - b[k]) + Math.abs(a[k + 1] - b[k + 1]) + Math.abs(a[k + 2] - b[k + 2]) > 12) diff++;
  return [diff, a.length / 4, K, K >= 100];
}"""

STATE_JS = r"""([i, sn, settle]) => {         // az állapot az exponálás előtt fut: L.st = settle (vagy az állapot st-je), aztán set(L)
  const L = window.__lesson, S = window.__qaStates[i + 1][sn];   // set nélkül ({name, st}) csak az időt állítja
  L.st = S.st != null ? S.st : settle; L.sp = L.step; if (typeof S.set === 'function') S.set(L);
}"""

STATE_EFFECT_JS = r"""([i, sn, settle]) => {   // hatott-e az állapot? rögzített képkockaidővel: kép nélküle és vele, ugyanannál az L.st-nél
  // (set nélküli, csak st-s állapot: a lépés settle-képéhez képest – a „hatás” itt maga az időpont)
  const L = window.__lesson, T = window.__qaTick, S = window.__qaStates[i + 1][sn], hasSet = typeof S.set === 'function';
  const st = (on) => (S.st != null && (on || hasSet) ? S.st : settle);
  const shot = (on) => { L.go(i, true); T(2); L.st = st(on); L.t = 100; L.sp = L.step; if (on && hasSet) S.set(L); T(4); return window.__qaGrab(); };
  const a = shot(false), b = shot(true);
  let diff = 0; for (let k = 0; k < a.length; k += 4) if (a[k] !== b[k] || a[k + 1] !== b[k + 1] || a[k + 2] !== b[k + 2]) diff++;
  return diff;
}"""

IDLE_JS = "(() => { const L = window.__lesson; return typeof L.idle !== 'function' || L.idle(); })()"

JUMP_JS = r"""([a, b]) => {        // a → b ugrás áttűnéssel; a draw()-ban dobott hibát elkapja
  const L = window.__lesson, T = window.__qaTick;
  // kiindulás: a-ra áttűnés nélkül (mint az URL #a), hogy ne ez legyen az első ugrás
  try { L.go(a, true); L.sp = L.step; T(20); } catch (e) { return 'előkészítés (' + (a + 1) + '. lépés, áttűnés nélkül): ' + (e && e.message || e); }
  try { L.go(b); T(30); } catch (e) { return String(e && e.message || e); }
  return null;
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


def drawable(text):
    """A szöveg látható jelei (szóköz, vezérlő- és nulla szélességű jelek nélkül) – a valódi glifpróbához."""
    return {ch for ch in text if not ch.isspace() and unicodedata.category(ch) not in ("Cc", "Cf", "Mn", "Me", "Zs")}


def det_page(b, html, query="", console=False):
    """Rögzített képkockaidős oldal (window.__qaTick) – a --det és az ugrópróba használja."""
    ctx2 = b.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=.5)
    ctx2.add_init_script(DET_INIT)
    pd = ctx2.new_page()
    derr = []
    pd.on("pageerror", lambda e: derr.append("JS-HIBA: " + str(e).split("\n")[0]))
    if console:
        pd.on("console", lambda m: derr.append("KONZOL: " + m.text) if m.type == "error" else None)
    pd.goto(html.as_uri() + query)
    pd.wait_for_function("window.__lesson && window.__lesson.started", timeout=15000)
    pd.evaluate("document.fonts.ready.then(() => 1)")
    return ctx2, pd, derr


def jump_test(b, html, n):
    """Ugrópróba: 1 → utolsó, utolsó → 1, 6 seedelt véletlen ugrás, betöltés #N-re. → hibák száma."""
    import random
    rnd = random.Random(7)
    jumps = [(0, n - 1), (n - 1, 0)] if n > 1 else []
    tries = 0
    while len(jumps) < 8 and n > 2 and tries < 200:
        tries += 1
        a, c = rnd.randrange(n), rnd.randrange(n)
        if abs(a - c) > 1 and (a, c) not in jumps:
            jumps.append((a, c))
    probs = []
    ctx2 = pd = None
    for a, c in jumps:
        if pd is None:
            ctx2, pd, derr = det_page(b, html, console=True)
            pd.wait_for_timeout(200)
            pd.evaluate("window.__qaTick(3)")
        derr.clear()
        try:
            e = pd.evaluate(JUMP_JS, [a, c])
        except Exception as ex:
            e = str(ex).split("\n")[0]
        if e or derr:
            probs.append(f"UGRÁS {a + 1} → {c + 1}: " + (f"JS-HIBA: {e}" if e else derr[0]))
            ctx2.close(); pd = None        # a főciklus leállt → új oldal a következő ugráshoz
    if pd is not None:
        ctx2.close()
    ctx2, pd, derr = det_page(b, html, f"#{n}", console=True)
    try:
        pd.wait_for_timeout(200)
        pd.evaluate("window.__qaTick(30)")
    except Exception as ex:
        derr.append("JS-HIBA: " + str(ex).split("\n")[0])
    if derr:
        probs.append(f"BETÖLTÉS #{n}-re: " + derr[0])
    ctx2.close()
    probs = list(dict.fromkeys(probs))
    print(f"ugrópróba ({len(jumps)} ugrás + #{n}) " + ("✓" if not probs else f"✗ {len(probs)}"))
    for m in probs[:10]:
        print("     · " + m)
    return len(probs)


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

    real = {}                      # (család, dőlt, jel) → van-e rajz a fontfájlban (böngészőben mérve, egyszer)

    def real_missing(pg, triples):
        todo = sorted({x for x in triples if x not in real})
        if todo:
            try:
                gone = {tuple(x) for x in pg.evaluate(GLYPH_REAL_JS, [list(x) for x in todo])}
            except Exception:
                gone = set()
            for x in todo:
                real[x] = x not in gone
        return {x for x in triples if not real.get(x, True)}

    def extra(pg, glyph=True):
        """Figyelmeztetések (glif, matematikai írásmód) + L.checks() hibái."""
        warns = []
        if glyph:
            g = pg.evaluate(GLYPH_JS)
            fonts = []                                  # (szöveg, család, dőlt) a valódi glifpróbához
            for s_, f_ in g["marks"]:
                fam, it = font_of(f_)
                miss = [c for c in missing_glyphs(s_, cov.get(fam, allr)) if (fam, c) not in seen_glyph and c not in seen_glyph]
                if miss:
                    seen_glyph.update((fam, c) for c in miss)
                    warns.append(f"GLIF: nincs a fontokban{f' ({fam})' if fam in cov else ''}: {' '.join(miss)} "
                                 f"({', '.join(f'U+{ord(c):04X}' for c in miss)}) – „{s_[:28]}”")
                if fam in cov:
                    fonts.append((s_, fam, it, "vászon"))
                if is_math:
                    for rx, msg in MATH_MARK:
                        if rx.search(s_):
                            warns.append(f"ÍRÁSMÓD: {msg} – „{s_[:28]}”")
            for fam, t, it in g["panel"]:
                miss = [c for c in missing_glyphs(t, cov.get(fam, allr)) if (fam, c) not in seen_glyph]
                if miss:
                    seen_glyph.update((fam, c) for c in miss)
                    warns.append(f"GLIF (panel, {fam}): nincs a fontban: {' '.join(miss)} – „{t[:28]}”")
                if fam in cov:
                    fonts.append((t, fam, it, "panel"))
            # a unicode-range szerint lefedett jelek: tényleg van-e rajzuk a fontfájlban?
            trip = {(fam, it, c): (s_, where) for s_, fam, it, where in fonts for c in drawable(s_)
                    if not missing_glyphs(c, cov[fam]) and ("real", fam, it, c) not in seen_glyph}
            for fam, it, c in sorted(real_missing(pg, set(trip))):
                seen_glyph.add(("real", fam, it, c))
                s_, where = trip[(fam, it, c)]
                warns.append(f"GLIF ({where}, {fam}{' dőlt' if it else ''}): a(z) {c} (U+{ord(c):04X}) nincs a fontfájlban – "
                             f"tartalékfontra esik – „{s_[:28]}”")
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
        pg.add_init_script(AUDIO_INIT)
        errs = []
        pg.on("pageerror", lambda e: errs.append("JS-HIBA: " + str(e).split("\n")[0]))
        pg.on("console", lambda m: errs.append("KONZOL: " + m.text) if m.type == "error" else None)

        def open_(query=""):
            pg.goto(html.as_uri() + query)
            pg.wait_for_function("window.__lesson && window.__lesson.started", timeout=15000)
            pg.wait_for_timeout(300)

        def wait_idle(limit=5000):
            """Ha a lecke ad idle()-t: vár, amíg true (legfeljebb limit ms) → False, ha nem lett nyugodt."""
            waited = 0
            while waited < limit and not pg.evaluate(IDLE_JS):
                pg.wait_for_timeout(100); waited += 100
            return waited < limit

        def shoot(i, t, name, wait=250, idle=True):
            if t is not None:
                pg.evaluate(f"(() => {{ const L = window.__lesson; L.st = {t}; L.sp = L.step; }})()")
            pg.wait_for_timeout(wait)
            if idle:
                wait_idle()
            pg.screenshot(path=str(out / name))
            return pg.evaluate(CHECK_JS)

        open_()
        steps = pg.evaluate("window.__lesson.steps.map((s) => ({ title: s.title.replace(/<[^>]+>/g, ''), settle: s.settle || 8 }))")
        n = len(steps)
        subject = pg.evaluate("(() => { const C = window.__lesson.content; return (C && C.meta && C.meta.subject) || ''; })()")
        if "--glyphs" in opts or subject.lower().startswith("magyar"):
            gone = real_missing(pg, {(f, it, c) for f, it in HU_FACES for c in HU_PROBE})
            print("glifpróba (magyar, verstani jelek: " + " ".join(HU_PROBE) + "): " + " · ".join(
                f"{f}{' dőlt' if it else ''} " + ("✓" if not [c for c in HU_PROBE if (f, it, c) in gone] else
                                                  "tartalékfont: " + " ".join(c for c in HU_PROBE if (f, it, c) in gone))
                for f, it in HU_FACES))
        a_probs, a_warns = audio_problems(pg.evaluate(AUDIO_JS))
        if a_probs or a_warns:
            report("betöltés (hangpróba)  ", a_probs, a_warns)
            total += len(a_probs); nwarn += len(a_warns)
        idx = range(n) if "--steps" not in opts else [int(s) - 1 for s in opts["--steps"].split(",")]
        ats = (opts.get("--at") or "settle").split(",")
        if "--jump-only" in opts:
            idx = []
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
        state_wait = {(int(k) - 1, sn): w for k, ws in (pg.evaluate(
            "(() => { const s = window.__qaStates || {}; const o = {}; for (const k in s) o[k] = s[k].map((x) => x.wait || 250); return o; })()")
            if states else {}).items() for sn, w in enumerate(ws)}
        no_effect = set()
        bad_keys = [k for k in states if not (k.isdigit() and 1 <= int(k) <= n)]
        if bad_keys:                  # a kulcs 1-alapú lépésszám – a 0 vagy a túl nagy kulcs némán rossz lépésre esne
            print(f"! __qaStates: érvénytelen kulcs(ok): {', '.join(bad_keys)} (1-alapú lépésszám kell, 1–{n}) – kihagyva")
            nwarn += len(bad_keys)
            states = {k: v for k, v in states.items() if k not in bad_keys}
        if states:                    # hatott-e az állapot? (rögzített képkockaidővel, a fotózás előtt)
            ctx3, pd3, _ = det_page(b, html)
            pd3.wait_for_timeout(300); pd3.evaluate("window.__qaTick(3)")
            for k, names in states.items():
                for sn in range(len(names)):
                    i0 = int(k) - 1
                    try:
                        if pd3.evaluate(STATE_EFFECT_JS, [i0, sn, steps[i0]["settle"]]) == 0:
                            no_effect.add((i0, sn))
                    except Exception:
                        pass               # a hibát a fotózás úgyis jelzi
            ctx3.close()
        for i in idx:
            for k, at in enumerate(ats):
                errs.clear()
                pg.evaluate(AUDIO_JS)            # az előző állapotok (__qaStates) hangja nem ehhez a lépéshez tartozik
                ms = pg.evaluate(GO_JS, i); pg.wait_for_timeout(900)
                if poke is not None:
                    pg.evaluate("(o) => { const L = window.__lesson; if (typeof L.poke !== 'function') throw new Error('a lecke nem ad L.poke()-ot'); L.poke(o); }", poke)
                t = steps[i]["settle"] if at == "settle" else float(at)
                name = f"{i + 1:02d}" + (f"-{at}" if len(ats) > 1 else "") + ".png"
                # idle(): csak a nyugalmi (settle) kép várja meg; a --at 1.5 a köztes állapot fotója (különben a várakozás
                # alatt továbbfutna az idő, és a kép a nyugalmat mutatná)
                r = shoot(i, t, name, idle=at == "settle")
                warns, chk = extra(pg)
                if ms > 300:
                    warns.append(f"enter(): {ms:.0f} ms (> 300 ms – iskolai gépen lassú lehet; számolj előre kevesebbet, vagy init()-ben)")
                a_probs, a_warns = audio_problems(pg.evaluate(AUDIO_JS))
                warns += a_warns
                probs = errs + r["problems"] + chk + a_probs
                total += len(probs); nwarn += len(warns)
                report(f"{i + 1:02d} {steps[i]['title'][:44]:<44} t={t:<4g} feliratok:{r['marks']:>3}  ", probs, warns)
            for sn, nm in enumerate(states.get(str(i + 1), [])):
                errs.clear()
                pg.evaluate(GO_JS, i); pg.wait_for_timeout(300)
                # az állapot közvetlenül az exponálás előtt fut (L.st = settle, ill. az állapot st-je), és utána
                # a QA már nem állítja az L.st-t: az L.st-hez kötött állapot (t0 = L.st − 2) is a saját idejét mutatja
                pg.evaluate(STATE_JS, [i, sn, steps[i]["settle"]])
                r = shoot(i, None, f"{i + 1:02d}-{nm}.png", wait=state_wait[(i, sn)], idle=False)
                warns, chk = extra(pg)
                if (i, sn) in no_effect:
                    warns.append("ÁLLAPOT: a vászon képpontra ugyanaz, mint az állapot nélkül – a set() nem hatott? "
                                 "(L.st-hez kötött állapotnál: t0 = L.st − x, vagy adj st-t; ha az állapot a lépés alapképe – pl. a túra "
                                 "vége –, rendben van, de akkor fölösleges)")
                probs = errs + r["problems"] + chk
                total += len(probs); nwarn += len(warns)
                report(f"{i + 1:02d} állapot „{nm}”{'':<20} ", probs, warns)
        if "--back" in opts:
            for i in [j for j in idx if j < n - 1]:
                errs.clear()
                pg.evaluate(f"window.__lesson.go({i + 1}, true)"); pg.wait_for_timeout(400)
                pg.evaluate("window.__lesson.prev()"); pg.wait_for_timeout(650)
                r = shoot(i, None, f"{i + 1:02d}-vissza.png")     # + vár az idle()-re (pl. kamera)
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
        if "--no-jump" not in opts:
            total += jump_test(b, html, n)
        if "--det" in opts:
            ctx2, pd, derr = det_page(b, html)
            pd.wait_for_timeout(500)
            pd.evaluate("window.__qaTick(3)")
            for i in idx:
                derr.clear()
                j = i + 1 if i < n - 1 else max(0, i - 1)
                diff, tot, K, stuck = pd.evaluate(DET_JS, [i, j, steps[i]["settle"]])
                probs = list(derr)
                if stuck:
                    probs.append("IDLE: a lecke idle()-je 5 mp (100 képkocka) után sem lett true")
                if diff / tot > 0.0005:
                    probs.append(f"DETERMINIZMUS: ugyanannál az L.st-nél a két kép {diff} képpontban ({100 * diff / tot:.2f} %) eltér "
                                 "(seed nélküli Math.random, valós idő, képkockánként halmozott állapot?)")
                    for tag, jj in (("a", None), ("b", j)):
                        if jj is not None:
                            pd.evaluate("([j, i]) => { window.__lesson.go(j, true); window.__qaTick(6); window.__lesson.go(i, true); window.__qaTick(2); }", [jj, i])
                        else:
                            pd.evaluate("(i) => { window.__lesson.go(i, true); window.__qaTick(2); }", i)
                        pd.evaluate(f"(() => {{ const L = window.__lesson; L.st = {steps[i]['settle']}; L.t = 100; L.sp = L.step; window.__qaTick({1 + K}); }})()")
                        pd.screenshot(path=str(out / f"{i + 1:02d}-det-{tag}.png"))
                total += len(probs)
                report(f"{i + 1:02d} determinizmus (L.st={steps[i]['settle']:g}{f' + {K} képkocka (idle)' if K else ''}, {j + 1}. lépésen át)  ", probs, [])
            ctx2.close()
        b.close()
    if nwarn:
        print(f"! {nwarn} figyelmeztetés (glif / enter() / írásmód / hang) – nézd át, de nem hiba")
    print(f"{'✓ nincs hiba' if not total else f'✗ {total} probléma'} · képek: {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
