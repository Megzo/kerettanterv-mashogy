/* ───────────────────────────────────────────────────────────────
   Kerettanterv – másképp · közös lecke-motor
   (az iskola/ kísérlet motorja, visszafelé kompatibilis bővítésekkel)
   1920×1080 logikai színpad (vászon + DOM réteg), jobb oldalt
   magyarázó panel, lépésenkénti (fejezetes) animáció.

   Használat:
     const L = Lesson.create({
       content: window.LESSON_CONTENT,     // ÚJ: a .md-ből generált tartalom (cím, lépésszövegek, feliratok, adatok)
       subject: 'Fizika', title: '…',      // content nélkül kötelező, content mellett elhagyható
       home: false,                        // ÚJ: false → nincs „← tantárgyak” link (alap: 'index.html')
       steps: [
         { title: '…', text: '<p>…</p>',   // content mellett elhagyható: a .md N. lépéséből jön
           settle: 6,                      // ÚJ (opcionális): ennyi mp után nyugalmi az állapot;
                                           //   visszafelé lépve innen indul, a QA ezt fotózza
           enter(L) {}, leave(L) {},       // opcionális
           controls(L) { L.slider({...}); L.button('…', fn); } // opcionális
         }, …
       ],
       init(L) {},     // egyszer, a betűtípusok betöltése után
       draw(L) {},     // minden képkockán
     });

   A draw(L)-ben elérhető:
     L.ctx   2D kontextus, 1920×1080 logikai koordinátákban (a transzformáció már be van állítva)
     L.W, L.H        1920, 1080
     L.VW            1360 — a szabad vizuális terület szélessége (ettől jobbra a panel takar)
     L.t, L.dt       teljes idő / képkocka-idő másodpercben (dt ≤ 0.05)
     L.step          aktuális lépés indexe (0-tól)
     L.st            az aktuális lépésbe lépés óta eltelt másodperc
     L.sp            simított lépés-index (lebegőpontos, kb. 0.6 s alatt követi L.step-et) — kamerához, áttűnéshez
     L.dir           +1 előre, −1 visszafelé léptünk
     L.prog(a, b)    0..1: hol tart L.st az [a, b] másodperc-intervallumban
     L.layer         DOM réteg a vászon fölött (1920×1080, absolute) — SVG/HTML elemekhez
     L.pointer       {x, y, down, inside} logikai koordinátákban

   ÚJ — tartalom (a .md-ből, lásd leckek/SZERZODES.md):
     L.lab(k)        felirat szövege ('### Feliratok' kulcs → szöveg)
     L.num(k)        adat számértéke ('### Adatok', pl. 0.92)
     L.unit(k)       adat mértékegysége (pl. 'g/cm³')
     L.val(k, d)     adat magyarul formázva egységgel: '0,92 g/cm³' (d: tizedesjegyek, alap: ahogy a .md-ben)
   ÚJ — vászon-szöveg (méréssel; a QA és a review mód ebből tudja, hol van felirat):
     L.tx(s, x, y, o)   kiírja s-t; o = {s: px, w: vastagság, f: család, i: dőlt, a: igazítás, b: alapvonal,
                        c: szín, ls: betűköz, max: max. szélesség (fölötte kicsinyít), k: md-kulcs(ok),
                        qa: false → a QA átfedés-vizsgálata kihagyja}. Visszaad: {w, h, x, y} (doboz).
     L.measure(s, o)    ugyanaz rajzolás nélkül → {w, h}
     L.pill(s, x, y, o) szöveghez méretezett lekerekített doboz + szöveg; o.bg, o.bd (keret), o.pad, o.r
     L.fonts         {D: Fraunces, B: Bricolage Grotesque, M: JetBrains Mono} — o.f értékei
   ÚJ — U.fmt(v, d)  magyar számformátum: tizedesvessző, valódi mínuszjel (−), 10 000 fölött ezres tagolás
   ÚJ — review mód:  ?review az URL-ben vagy a K billentyű → a feliratok és bekezdések fölé mutatva
                     kiírja a Markdown-kulcsot és a sor számát.
   ÚJ — window.__lesson.marks: az utolsó képkocka feliratainak dobozai (a QA olvassa).
   ─────────────────────────────────────────────────────────────── */
(function () {
  'use strict';
  const W = 1920, H = 1080, VW = 1360;
  const FONTS = { D: 'Fraunces', B: '"Bricolage Grotesque"', M: '"JetBrains Mono"' };

  const U = {
    clamp: (v, a = 0, b = 1) => Math.min(b, Math.max(a, v)),
    lerp: (a, b, t) => a + (b - a) * t,
    map: (v, a, b, c, d) => c + (d - c) * U.clamp((v - a) / (b - a)),
    smooth: (t) => { t = U.clamp(t); return t * t * (3 - 2 * t); },
    inOut: (t) => { t = U.clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; },
    out: (t) => 1 - Math.pow(1 - U.clamp(t), 3),
    in: (t) => Math.pow(U.clamp(t), 3),
    outBack: (t) => { t = U.clamp(t); const c = 1.70158; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); },
    outElastic: (t) => { t = U.clamp(t); if (t === 0 || t === 1) return t; return Math.pow(2, -10 * t) * Math.sin((t * 10 - .75) * (2 * Math.PI) / 3) + 1; },
    /* determinisztikus véletlen: const r = U.rng(42); r() → [0,1) */
    rng: (seed) => { let s = seed >>> 0 || 1; return () => { s ^= s << 13; s >>>= 0; s ^= s >> 17; s ^= s << 5; s >>>= 0; return s / 4294967296; }; },
    /* "#rrggbb" + alfa → rgba() */
    rgba: (hex, a = 1) => { const n = parseInt(hex.slice(1), 16); return `rgba(${n >> 16 & 255},${n >> 8 & 255},${n & 255},${a})`; },
    /* két "#rrggbb" szín keverése */
    mix: (h1, h2, t) => { const a = parseInt(h1.slice(1), 16), b = parseInt(h2.slice(1), 16); const c = (s) => Math.round(U.lerp(a >> s & 255, b >> s & 255, U.clamp(t))); return `rgb(${c(16)},${c(8)},${c(0)})`; },
    /* magyar számformátum: U.fmt(-3.14159, 2) → '−3,14'; U.fmt(19300) → '19 300' */
    fmt: (v, d = 0) => {
      const s = Math.abs(v).toFixed(d).split('.'); let i = s[0];
      if (i.length > 4) i = i.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
      return (v < 0 && Math.abs(v) >= Math.pow(10, -d) / 2 ? '−' : '') + i + (s[1] ? ',' + s[1] : '');
    },
    TAU: Math.PI * 2,
  };

  function el(tag, cls, html) { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }

  function create(cfg) {
    const C = cfg.content || null;
    const L = {
      W, H, VW, U, cfg, steps: cfg.steps, step: 0, st: 0, sp: 0, t: 0, dt: 0, dir: 1,
      pointer: { x: 0, y: 0, down: false, inside: false }, scale: 1, fonts: FONTS,
      content: C, marks: [], review: /[?&]review\b/.test(location.search),
    };
    L.prog = (a, b) => U.clamp((L.st - a) / (b - a));
    const errors = [];
    if (cfg.content === undefined && 'content' in cfg) errors.push('Hiányzik a tartalomfájl (…content.js). Futtasd: python3 tools/build_lesson.py <lecke>.md');
    if (C) {
      cfg.title = cfg.title || C.title; cfg.subject = cfg.subject || C.meta.subject;
      if (C.steps.length !== cfg.steps.length) errors.push(`A .md ${C.steps.length} lépést tartalmaz, a lecke ${cfg.steps.length}-et vár. Futtasd újra a build_lesson.py-t.`);
      cfg.steps.forEach((s, i) => { const cs = C.steps[i]; if (!cs) return; if (s.title == null) s.title = cs.title; if (s.text == null) s.text = cs.html; s.src = cs.line; });
    }
    cfg.steps.forEach((s) => { if (s.title == null) s.title = '⟨cím hiányzik⟩'; });

    // ── tartalom-elérés ──
    const missing = new Set();
    const miss = (k) => { if (!missing.has(k)) { missing.add(k); console.error('Hiányzó tartalomkulcs: ' + k); } };
    L.lab = (k) => { const v = C && C.labels[k]; if (v == null) { miss(k); return '⟨' + k + '⟩'; } return v; };
    const dat = (k) => { const v = C && C.data[k]; if (!v) { miss(k); return { v: NaN, u: '', d: 0 }; } return v; };
    L.num = (k) => dat(k).v;
    L.unit = (k) => dat(k).u;
    L.val = (k, d) => { const v = dat(k); return U.fmt(v.v, d == null ? v.d : d) + (v.u ? (v.u === '°' ? '' : ' ') + v.u : ''); };
    const srcOf = (k) => (C && C.src && C.src[k]) || 0;

    // ── DOM váz ──
    document.title = cfg.title + ' — ' + cfg.subject;
    const vp = el('div'); vp.id = 'lesson-viewport';
    const stage = el('div'); stage.id = 'lesson-stage';
    const canvas = el('canvas'); canvas.id = 'lesson-canvas';
    const layer = el('div'); layer.id = 'lesson-layer';
    const panel = el('aside'); panel.id = 'lesson-panel';
    panel.innerHTML = `
      <div class="lp-top"><span class="lp-subject"></span><span class="lp-review-badge" hidden>REVIEW</span><a class="lp-home" href="${cfg.home || 'index.html'}"${cfg.home === false ? ' hidden' : ''}>← tantárgyak</a></div>
      <div class="lp-lesson"></div>
      <div class="lp-rule"></div>
      <div class="lp-body" style="display:flex;flex-direction:column;flex:1 1 auto;min-height:0">
        <div class="lp-count"></div>
        <h2 class="lp-title"></h2>
        <div class="lp-text"></div>
        <div class="lp-controls"></div>
      </div>
      <div class="lp-nav">
        <button class="lp-arrow prev" title="Előző (←)">←</button>
        <button class="lp-arrow replay" title="Lépés újrajátszása (R)">↻</button>
        <div class="lp-dots"></div>
        <button class="lp-arrow next" title="Következő (→)">→</button>
      </div>
      <div class="lp-hint"><kbd>←</kbd> <kbd>→</kbd> léptetés · <kbd>R</kbd> újra · <kbd>F</kbd> teljes képernyő</div>`;
    stage.append(canvas, layer, panel); vp.append(stage); document.body.append(vp);
    panel.querySelector('.lp-subject').textContent = cfg.subject;
    const $lesson = panel.querySelector('.lp-lesson'); $lesson.textContent = cfg.title;
    const $count = panel.querySelector('.lp-count'), $title = panel.querySelector('.lp-title'),
      $text = panel.querySelector('.lp-text'), $controls = panel.querySelector('.lp-controls'),
      $dots = panel.querySelector('.lp-dots'), $prev = panel.querySelector('.prev'), $next = panel.querySelector('.next'),
      $body = panel.querySelector('.lp-body'), $badge = panel.querySelector('.lp-review-badge');
    L.stage = stage; L.canvas = canvas; L.layer = layer; L.panel = panel; L.controlsEl = $controls;
    L.ctx = canvas.getContext('2d');
    L.ink = (getComputedStyle(document.body).getPropertyValue('--ink') || '').trim() || '#1c2440';   // L.tx alapszíne
    if (C) { $lesson.dataset.src = C.titleLine; }
    if (errors.length) { const e = el('div'); e.id = 'lesson-error'; e.textContent = errors.join('\n'); stage.append(e); errors.forEach((m) => console.error(m)); }

    cfg.steps.forEach((s, i) => { const d = el('button', 'lp-dot'); d.title = (i + 1) + '. ' + s.title.replace(/<[^>]+>/g, ''); d.onclick = () => L.go(i); $dots.append(d); });

    // ── vezérlő-segédek (a lépés controls(L) függvényéből hívhatók) ──
    L.slider = ({ label, min = 0, max = 1, step = 0.01, value = 0, format = (v) => v, onInput, k }) => {
      const w = el('div', 'lp-slider'); const lb = el('label', '', label); const out = el('output');
      if (k) lb.dataset.src = srcOf(k), lb.dataset.key = k;
      const inp = el('input'); inp.type = 'range'; inp.min = min; inp.max = max; inp.step = step; inp.value = value;
      const upd = () => { out.textContent = format(+inp.value); };
      inp.addEventListener('input', () => { upd(); onInput && onInput(+inp.value); });
      upd(); w.append(lb, out, inp); $controls.append(w); reviewTags();
      return { el: w, input: inp, set: (v) => { inp.value = v; upd(); } };
    };
    L.button = (label, onClick, k) => {
      let row = $controls.lastElementChild; if (!row || !row.classList.contains('lp-btnrow')) { row = el('div', 'lp-btnrow'); $controls.append(row); }
      const b = el('button', 'lp-btn', label); b.addEventListener('click', () => onClick && onClick(b)); row.append(b);
      if (k) b.dataset.src = srcOf(k), b.dataset.key = k;
      reviewTags(); return b;
    };

    // ── review mód: data-src (sor) / data-key → olvasható címke ──
    function reviewTags() {
      if (!L.review) return;
      const file = (C && C.source) || '';
      panel.querySelectorAll('[data-src]').forEach((e) => {
        const what = e.dataset.key ? 'felirat: ' + e.dataset.key : e === $lesson ? 'cím (# sor)' : e.classList.contains('lp-title') ? 'lépéscím (## sor)' : 'panelszöveg';
        e.dataset.rev = `${what} · ${file} ${e.dataset.src}. sor`;
      });
    }
    const tip = el('div'); tip.id = 'lesson-revtip'; tip.hidden = true; stage.append(tip);
    panel.addEventListener('mouseover', (e) => {
      const t = L.review && e.target.closest && e.target.closest('[data-rev]');
      if (!t) { tip.hidden = true; return; }
      const r = t.getBoundingClientRect(), s0 = stage.getBoundingClientRect(), k = W / s0.width;
      tip.textContent = t.dataset.rev; tip.hidden = false;
      tip.style.left = Math.min((r.left - s0.left) * k, W - tip.offsetWidth - 8) + 'px';
      tip.style.top = Math.max(4, (r.top - s0.top) * k - 36) + 'px';
    });
    panel.addEventListener('mouseleave', () => { tip.hidden = true; });
    L.setReview = (on) => { L.review = !!on; stage.classList.toggle('review', L.review); $badge.hidden = !L.review; reviewTags(); };

    // ── lépésváltás ──
    function render() {
      const s = cfg.steps[L.step], n = cfg.steps.length;
      $count.innerHTML = `<b>${String(L.step + 1).padStart(2, '0')}</b> <span>/ ${String(n).padStart(2, '0')}</span>`;
      $title.innerHTML = s.title; $text.innerHTML = s.text || '';
      if (s.src) $title.dataset.src = s.src; else delete $title.dataset.src;
      $controls.innerHTML = ''; if (s.controls) s.controls(L);
      $body.classList.remove('lp-anim'); void $body.offsetWidth; $body.classList.add('lp-anim');
      [...$dots.children].forEach((d, i) => { d.classList.toggle('cur', i === L.step); d.classList.toggle('done', i < L.step); });
      $prev.disabled = L.step === 0; $next.disabled = L.step === n - 1;
      reviewTags();
      try { history.replaceState(null, '', location.search + '#' + (L.step + 1)); } catch (e) { /* file:// alatt is megy, de biztos ami biztos */ }
    }
    L.go = (i, force) => {
      i = U.clamp(i, 0, cfg.steps.length - 1); if (i === L.step && !force) return;
      const old = cfg.steps[L.step]; if (old && old.leave && L.started) old.leave(L);
      L.dir = i >= L.step ? 1 : -1; L.prevStep = L.step; L.step = i;
      const s = cfg.steps[i];
      L.st = L.dir < 0 && L.started && s.settle ? s.settle : 0;   // visszafelé: a nyugalmi állapotból
      render(); if (s.enter) s.enter(L);
    };
    L.next = () => L.go(L.step + 1); L.prev = () => L.go(L.step - 1);
    L.replay = () => { L.dir = 1; L.go(L.step, true); L.st = 0; };
    $prev.onclick = L.prev; $next.onclick = L.next; panel.querySelector('.replay').onclick = L.replay;

    window.addEventListener('keydown', (e) => {
      if (e.target && /INPUT|TEXTAREA|SELECT/.test(e.target.tagName) && e.target.type !== 'range') return;
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      const k = e.key;
      if (k === 'ArrowRight' || k === 'PageDown' || k === ' ') { e.preventDefault(); L.next(); }
      else if (k === 'ArrowLeft' || k === 'PageUp') { e.preventDefault(); L.prev(); }
      else if (k === 'Home') L.go(0); else if (k === 'End') L.go(cfg.steps.length - 1);
      else if (k === 'r' || k === 'R') L.replay();
      else if (k === 'k' || k === 'K') L.setReview(!L.review);
      else if (k === 'f' || k === 'F') { if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen && document.documentElement.requestFullscreen(); }
      else if (/^[1-9]$/.test(k)) L.go(+k - 1);
      else if (cfg.onKey) cfg.onKey(e, L);
    });

    // ── méretezés (letterbox) + HiDPI vászon ──
    function fit() {
      const s = Math.min(innerWidth / W, innerHeight / H); L.scale = s;
      stage.style.transform = `scale(${s}) translate(-50%, -50%)`;
      const k = U.clamp(s * (window.devicePixelRatio || 1), 1, 2.5);
      const cw = Math.round(W * k), ch = Math.round(H * k);
      if (canvas.width !== cw) { canvas.width = cw; canvas.height = ch; }
      L.k = cw / W;
    }
    window.addEventListener('resize', fit); fit();

    // ── mutató (logikai koordináták) ──
    L.toStage = (e) => { const r = stage.getBoundingClientRect(); return { x: (e.clientX - r.left) / r.width * W, y: (e.clientY - r.top) / r.height * H }; };
    stage.addEventListener('pointermove', (e) => { const p = L.toStage(e); L.pointer.x = p.x; L.pointer.y = p.y; L.pointer.inside = true; });
    stage.addEventListener('pointerdown', (e) => { const p = L.toStage(e); L.pointer.x = p.x; L.pointer.y = p.y; L.pointer.down = true; });
    window.addEventListener('pointerup', () => { L.pointer.down = false; });
    stage.addEventListener('pointerleave', () => { L.pointer.inside = false; });

    // ── vászon-szöveg mérése, feliratdobozok ──
    let cur = [];
    const font = (o) => `${o.i ? 'italic ' : ''}${o.w || 500} ${o.s || 24}px ${o.f || FONTS.B}`;
    L.measure = (s, o = {}) => {
      const c = L.ctx; c.font = font(o); c.letterSpacing = o.ls || '0px';
      const w = c.measureText(String(s)).width; c.letterSpacing = '0px'; return { w, h: (o.s || 24) * 1.0 };
    };
    L.tx = (s, x, y, o = {}) => {
      const c = L.ctx; s = String(s);
      if (o.max) { const m = L.measure(s, o).w; if (m > o.max) o = Object.assign({}, o, { s: (o.s || 24) * o.max / m }); }
      const sz = o.s || 24, a = o.a || 'left', b = o.b || 'alphabetic';
      c.font = font(o); c.textAlign = a; c.textBaseline = b; c.letterSpacing = o.ls || '0px';
      c.fillStyle = o.c || L.ink;
      const w = c.measureText(s).width; c.fillText(s, x, y); c.letterSpacing = '0px';
      const x0 = a === 'center' ? x - w / 2 : a === 'right' || a === 'end' ? x - w : x;
      const asc = sz * .74, desc = sz * .24;
      const y0 = b === 'middle' ? y - (asc + desc) / 2 : b === 'top' || b === 'hanging' ? y : b === 'bottom' ? y - asc - desc : y - asc;
      const box = { x: x0, y: y0, w, h: asc + desc };
      const alpha = c.globalAlpha;
      if (alpha > .04 && s.trim()) {
        const m = c.getTransform(), k = L.k || 1;
        cur.push({ s, k: o.k || null, x: (m.a * box.x + m.c * box.y + m.e) / k, y: (m.b * box.x + m.d * box.y + m.f) / k,
          w: box.w * Math.hypot(m.a, m.b) / k, h: box.h * Math.hypot(m.c, m.d) / k, px: sz * Math.hypot(m.c, m.d) / k, a: alpha, qa: o.qa !== false });
      }
      return box;
    };
    L.pill = (s, x, y, o = {}) => {
      const c = L.ctx, pad = o.pad == null ? 12 : o.pad, sz = o.s || 24, m = L.measure(s, o), a = o.a || 'left';
      const w = m.w + pad * 2, h = sz * 1.3 + pad * .8;
      const x0 = a === 'center' ? x - w / 2 : a === 'right' ? x - w : x, y0 = y - h / 2;
      c.beginPath(); c.roundRect(x0, y0, w, h, o.r == null ? h / 2 : o.r);
      if (o.bg) { c.fillStyle = o.bg; c.fill(); }
      if (o.bd) { c.strokeStyle = o.bd; c.lineWidth = o.bw || 2; c.stroke(); }
      L.tx(s, x0 + pad, y0 + h / 2 + sz * .02, Object.assign({}, o, { a: 'left', b: 'middle' }));
      return { x: x0, y: y0, w, h };
    };

    function drawReview() {
      const c = L.ctx; c.save(); c.globalAlpha = 1; c.setTransform(L.k, 0, 0, L.k, 0, 0);
      let hit = null;
      for (const m of L.marks) {
        c.setLineDash([5, 4]); c.lineWidth = 1.5; c.strokeStyle = m.k ? 'rgba(122,60,194,.6)' : 'rgba(200,40,40,.7)';
        c.strokeRect(m.x - 3, m.y - 3, m.w + 6, m.h + 6);
        const p = L.pointer; if (p.inside && p.x >= m.x - 3 && p.x <= m.x + m.w + 3 && p.y >= m.y - 3 && p.y <= m.y + m.h + 3) hit = m;
      }
      c.setLineDash([]);
      if (hit) {
        const ks = hit.k ? [].concat(hit.k) : [], file = (C && C.source) || '';
        const t = ks.length ? ks.map((k) => `${k} · ${file} ${srcOf(k) || '?'}. sor`).join('   |   ') : 'NINCS KULCS — kódban rögzített szöveg';
        c.font = '600 18px ' + FONTS.M; const w = c.measureText(t).width + 20;
        const x = U.clamp(hit.x, 8, W - w - 8), y = hit.y - 40 < 8 ? hit.y + hit.h + 8 : hit.y - 40;
        c.fillStyle = '#7a3cc2'; c.beginPath(); c.roundRect(x, y, w, 32, 7); c.fill();
        c.fillStyle = '#fff'; c.textAlign = 'left'; c.textBaseline = 'middle'; c.fillText(t, x + 10, y + 17);
      }
      c.restore();
    }

    // ── főciklus ──
    let last = 0;
    function frame(now) {
      const dt = Math.min(0.05, (now - last) / 1000 || 0); last = now;
      L.dt = dt; L.t += dt; L.st += dt;
      L.sp += (L.step - L.sp) * (1 - Math.exp(-dt * 5.5)); if (Math.abs(L.step - L.sp) < 0.0005) L.sp = L.step;
      L.ctx.setTransform(L.k, 0, 0, L.k, 0, 0);
      cur = [];
      if (cfg.draw) cfg.draw(L);
      L.marks = cur;
      if (L.review) drawReview();
      requestAnimationFrame(frame);
    }
    function start() {
      if (cfg.init) cfg.init(L);
      const h = parseInt((location.hash || '').slice(1), 10);
      L.step = -1; L.go(h >= 1 && h <= cfg.steps.length ? h - 1 : 0, true); L.sp = L.step; L.started = true;
      L.setReview(L.review);
      stage.classList.add('ready'); requestAnimationFrame((n) => { last = n; frame(n); });
    }
    const fonts = ['560 40px Fraunces', 'italic 400 40px Fraunces', '400 24px "Bricolage Grotesque"', '700 24px "Bricolage Grotesque"', '500 20px "JetBrains Mono"'];
    const ready = document.fonts && document.fonts.load ? Promise.all(fonts.map((f) => document.fonts.load(f, 'őűÁ'))).catch(() => { }) : Promise.resolve();
    Promise.race([ready, new Promise((r) => setTimeout(r, 2500))]).then(start);

    window.__lesson = L;
    return L;
  }

  window.Lesson = { create, U, W, H, VW, FONTS };
})();
