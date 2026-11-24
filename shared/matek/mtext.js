/* ───────────────────────────────────────────────────────────────
   shared/matek/mtext.js — MatText + MatQ: matematikai szöveg a vásznon és pontos törtszámolás
   Betöltés a lesson.js UTÁN:  <script src="../../shared/matek/mtext.js"></script>

   A jelölés ugyanaz, mint a .md-ben (leckek/README.md, tools/build_lesson.py fejléce); az elemző
   (MatText.parse) a Python build Mx osztályának tükörképe – a közös próbaesetek a
   tools/tests/mx-cases.js-ben vannak, a böngészős próba: tools/tests/mtext.html.

   MatText.parse(s, o)          → fa. o: {frac: true (alap: 3/4 álló tört), chem: false, math: false
                                  (az egész s képlet, mint a `…` belseje), big: false (képlet: sor)}
       v1.1 (2026-11-24) – mértékegység a képletben ÁLLÓ (ISO 80000), a változó dőlt marad. Egységnek csak a
       SZÁM UTÁN álló egységjel számít: `5 cm`, `9,81 m/s^2`, `3 * 10^8 m/s`, `20 °C`, `72 km/h`, `5 N*m`;
       egybetűs egység (m, s, g, l, h, N, J, W, V, A, K) csak szóközzel: `5 m` = 5 méter, `5m` = 5 · m (változó);
       szám nélkül mindig változó: `F = m * a`, `v = s / t`. Mindig álló: °C, °F. Explicit álló szöveg a képletben:
       "…" (pl. `"max" + x`). A t (tonna) és az a (ár) szándékosan nem egység (idő, változó). Az egységlista a
       build UNITS-a (tools/build_lesson.py) – a kettő együtt változzon (próbák: tools/tests/mx-cases.js).
       A fa: 'szöveg' · ['i', 'x'] · ['sup', fa] · ['sub', fa] · ['frac', számláló, nevező] ·
             ['sqrt', fa] · ['mx', fa]  (`…` képletszakasz)
   MatText.draw(L, s, x, y, o)  kiírja s-t (szöveg VAGY kész fa). o mint az L.tx-nél:
                                  s (px, alap 30), w, f (alap F.M = JetBrains Mono), c, a ('left'|'center'|'right'),
                                  b ('alphabetic'|'middle'|'top'), k (md-kulcs), max (szélesség, fölötte
                                  kicsinyít), qa; továbbá vf (változók betűje, alap Fraunces dőlt),
                                  frac/chem/math (mint a parse-nál). → {x, y, w, h} (a teljes doboz)
                                  A darabokat L.tx írja ki, a k kulccsal – a QA és a review mód látja őket.
   MatText.measure(L, s, o)     → {w, h, asc, desc} rajzolás nélkül
   MatText.frac(L, n, d, x, y, o)   álló tört; o.whole (vegyes szám egész része), o.sign ('−' / '+')
   MatText.num(v, d, {plus})    '−3,25' · '+3' (U.fmt + előjel)
   MatText.check(L, key, expected, eps = 1e-9)   ha az L.dat(key) értéke (v, frac → n/d) ≠ expected,
                                  piros hibasávot tesz ki (#lesson-error) – a QA „HIBASÁV”-ként jelzi. → true/false
   MatText.evalExpr(fa, vars)   egy expr típusú adat fája (L.dat(k).tree) → szám (eval nélkül)
   MatText.css                  a panel tört-, gyök- és képletstílusa; betöltéskor bekerül a <head>-be

   MatQ(n, d = 1)               pontos tört (egész számláló/nevező, mindig egyszerűsítve, nevező > 0)
       .add(q) .sub(q) .mul(q) .div(q) .neg() .inv() .cmp(q) (−1/0/1) .eq(q)   (q: MatQ vagy szám)
       .v (lebegőpontos) · .n .d · .str() '3/4' · .str('mixed') '1 1/5' · .dec(k) '0,75' (k tizedesre
       kerekítve; k nélkül pontos, vagy periódusnál {pre: '0,1', rep: '6', s: '0,1(6)'})
   MatQ.from(datum)             L.dat(k) (frac / number / ratio) → MatQ;  MatQ.parse('2 1/3')
   MatQ.gcd(a, b) · MatQ.lcm(a, b) · MatQ.evalExpr(fa, vars) → MatQ (√ és tört kitevő: hiba)

   Betűk: a fontokból hiányzó jeleket (π, ≤, ∈ …) a shared/lesson.css unicode-range szabályai
   ugyanazon a családnéven pótolják – ehhez itt nem kell semmi; a QA glifellenőrzése jelzi, ha mégis
   hiányzik valami. Méretek: a tört számlálója/nevezője az alapméret 0,8-szorosa, a kitevő/index
   0,65-szöröse – kitevős szöveg alapja ≥ 34 px, törté ≥ 28 px, hogy a QA 22 px-es küszöbét tartsa.
   ─────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  // ── elemző (a tools/build_lesson.py Mx osztályának tükörképe) ──
  const LET = 'A-Za-zÀ-ÖØ-öø-žΑ-Ωα-ω';
  const IS_LET = new RegExp('^[' + LET + ']$'), IS_WORD = new RegExp('^[' + LET + '0-9_]$');
  // képletben a görög kisbetű változó → dőlt (mint a latin); a nagybetű (Δ, Σ, Ω) és a π álló
  const GREEK = /^[Α-Ωα-ωϑϕϵ]$/, isVar = (t) => IS_LET.test(t) && !/^[Α-Ωπ]$/.test(t) || /^[ϑϕϵ]$/.test(t);
  const ELEMENTS = new Set(('H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se ' +
    'Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb ' +
    'Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg ' +
    'Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og').split(' '));
  const CHEM_EXCEPT = new Set(['B1', 'B2', 'B3', 'B5', 'B6', 'B7', 'B9', 'B12', 'C3', 'C4', 'K2', 'V1', 'V2', 'U2', 'A3', 'A4', 'A5',
    'PM10', 'PM2', 'N1', 'S1', 'S2']);
  const MATH_OPS = [['<=>', '⇔'], ['|->', '↦'], ['<=', '≤'], ['>=', '≥'], ['!=', '≠'], ['~=', '≈'], ['->', '→'], ['=>', '⇒'], ['+-', '±']];
  const FUNCS = new Set(['sin', 'cos', 'tg', 'ctg', 'tan', 'cot', 'log', 'lg', 'ln', 'lim', 'max', 'min', 'sgn', 'lnko', 'lkkt', 'mod', 'exp', 'abs']);
  const NAMED = { pi: 'π', inf: '∞', NN: 'ℕ', ZZ: 'ℤ', QQ: 'ℚ', RR: 'ℝ' };
  const SUB_IN = { '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9' };
  const SUP_IN = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '−' };
  const at = (re, s, i) => { re.lastIndex = i; const m = re.exec(s); return m && m.index === i ? m : null; };
  const R = (src) => new RegExp(src, 'y');
  const FRAC_RE = R('(\\d+)/(\\d+)(?![0-9/]|,\\d)'), EXP_RE = R('\\^([−-]?)(\\d+(?:,\\d+)?|[A-Za-zα-ω])');
  const CHARGE_RE = R('\\^(\\d*[+\\-−])(?![\\w(])'), CHEM_RE = R('(?:[A-Z][a-z]?\\d*|\\((?:[A-Z][a-z]?\\d*)+\\)\\d*)+');
  const SUBRUN = R('\\d+|[' + LET + ']+'), SQRT_TOK = R('\\d+(?:,\\d+)?|[A-Za-zα-ω]'), WORD = R('[A-Za-zÀ-ÖØ-öø-ž]+');
  const SUBD = R('[₀₁₂₃₄₅₆₇₈₉]+'), SUPD = R('[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+'), BIGSLASH = R('\\s*/\\s*\\('), PRIMES = R('[′″‴]+');
  // mértékegység a képletben (v1.1): álló, ha SZÁM UTÁN áll (lásd a fejlécet; a build UNITS-ának tükörképe)
  const UNITS = new Set(('nm µm mm cm dm m km mg g dkg kg s ms h perc l ml cl dl hl N kN J kJ MJ W kW MW Wh kWh Pa kPa hPa MPa ' +
    'bar V mV kV A mA K Hz kHz MHz mol cal kcal ha lx dB').split(' '));
  const UNIT_WORD = R('[µμ]?[A-Za-z]+');
  function afterNumber(out) {      // számra végződik-e a kimenet (szöveg számjeggyel a végén, vagy szám^kitevő)?
    let k = out.length - 1;
    if (k >= 0 && typeof out[k] === 'string') { if (out[k].trim()) return /\d\s*$/.test(out[k]); k--; }
    return k > 0 && out[k][0] === 'sup' && out[k][1].every((x) => typeof x === 'string') && typeof out[k - 1] === 'string' && /\d$/.test(out[k - 1]);
  }

  function matchClose(s, i) {
    let depth = 0;
    for (let j = i; j < s.length; j++) {
      if (s[j] === '\\') continue;
      if (s[j] === '(') depth++; else if (s[j] === ')') { depth--; if (depth === 0) return j; }
    }
    return -1;
  }
  function splitTop(s) {
    let depth = 0;
    for (let j = 0; j < s.length; j++) {
      const c = s[j];
      if (c === '(' || c === '[') depth++; else if (c === ')' || c === ']') depth--;
      else if (c === '/' && depth === 0 && (j === 0 || s[j - 1] !== '\\')) return [s.slice(0, j), s.slice(j + 1)];
    }
    return null;
  }
  function push(out, x) {
    if (typeof x === 'string') { if (!x) return; if (out.length && typeof out[out.length - 1] === 'string') { out[out.length - 1] += x; return; } }
    out.push(x);
  }
  const isUpper = (c) => c >= 'A' && c <= 'Z';
  const isDigit = (c) => c >= '0' && c <= '9';

  function Parser(frac, chem) { this.frac = frac; this.chem = chem; this.errors = []; }
  Parser.prototype.seq = function (s, math, big) {
    const out = [], n = s.length; let i = 0, unitEnd = -1;
    while (i < n) {
      const c = s[i], prev = i ? s[i - 1] : '';
      let m;
      if (c === '\\' && i + 1 < n) { push(out, s[i + 1]); i += 2; continue; }
      if (c === '`') {
        let j = s.indexOf('`', i + 1);
        while (j > 0 && s[j - 1] === '\\') j = s.indexOf('`', j + 1);
        if (j < 0) { this.errors.push('lezáratlan `'); push(out, s.slice(i + 1)); break; }
        out.push(['mx', this.seq(s.slice(i + 1, j), true, false)]); i = j + 1; continue;
      }
      if (s.startsWith('[[', i)) {
        const j = s.indexOf(']]', i + 2), parts = j > 0 ? splitTop(s.slice(i + 2, j)) : null;
        if (j < 0 || !parts) { this.errors.push('[[…]]'); push(out, j > 0 ? s.slice(i, j + 2) : s.slice(i)); i = j > 0 ? j + 2 : n; continue; }
        out.push(['frac', this.seq(parts[0].trim(), true, false), this.seq(parts[1].trim(), true, false)]); i = j + 2; continue;
      }
      if (c === '^' && out.length) {
        if (s.startsWith('^(', i)) { const j = matchClose(s, i + 1); if (j > 0) { out.push(['sup', this.seq(s.slice(i + 2, j), math, false)]); i = j + 1; continue; } }
        if ((m = at(CHARGE_RE, s, i))) { out.push(['sup', [m[1].replace('-', '−')]]); i += m[0].length; continue; }
        if ((m = at(EXP_RE, s, i))) {
          const inner = m[1] ? ['−'] : [];
          if (math && isVar(m[2])) inner.push(['i', m[2]]); else push(inner, m[2]);
          out.push(['sup', inner]); if (i === unitEnd) unitEnd = i + m[0].length; i += m[0].length; continue;
        }
      }
      if (c === '_' && i + 1 < n && (IS_LET.test(prev) || math && (isDigit(prev) || prev === ')'))) {
        if (s[i + 1] === '(') { const j = matchClose(s, i + 1); if (j > 0) { out.push(['sub', this.seq(s.slice(i + 2, j), math, false)]); i = j + 1; continue; } }
        if ((m = at(SUBRUN, s, i + 1))) {
          const t = m[0];
          out.push(['sub', math && t.length === 1 && isVar(t) ? [['i', t]] : [t]]); i = i + 1 + t.length; continue;
        }
      }
      if ((math || this.frac) && (c === '√' || math && s.startsWith('gyök(', i))) {
        const k = i + (c === '√' ? 1 : 4);
        if (k < n && s[k] === '(') { const j = matchClose(s, k); if (j > 0) { out.push(['sqrt', this.seq(s.slice(k + 1, j), true, false)]); i = j + 1; continue; } }
        if (c === '√' && (m = at(SQRT_TOK, s, k))) { out.push(['sqrt', math && isVar(m[0]) ? [['i', m[0]]] : [m[0]]]); i = k + m[0].length; continue; }
      }
      if ((math || this.frac) && isDigit(c) && !(IS_WORD.test(prev) || (prev && ',./'.includes(prev)))) {
        m = at(FRAC_RE, s, i);
        if (m && !(i + m[0].length < n && IS_LET.test(s[i + m[0].length]))) {
          const a = m[1], b = m[2];
          if (out.length && typeof out[out.length - 1] === 'string') {
            const last = out[out.length - 1];
            if (/(?:^|[^\w,])(\d+) $/.test(last) && +a < +b) out[out.length - 1] = last.slice(0, -1);
          }
          out.push(['frac', [a], [b]]); i += m[0].length; continue;
        }
      }
      if (this.chem && !math) {
        if ((isUpper(c) || c === '(') && !(IS_WORD.test(prev) || prev === '\\')) {
          m = at(CHEM_RE, s, i);
          if (m && /\d/.test(m[0]) && !(i + m[0].length < n && /[a-záéíóöőúüű0-9]/.test(s[i + m[0].length]))) {
            const f = m[0], syms = f.match(/[A-Z][a-z]?/g) || [];
            if (!CHEM_EXCEPT.has(f) && syms.every((x) => ELEMENTS.has(x)) && (f.match(/\(/g) || []).length === (f.match(/\)/g) || []).length) {
              for (const p of f.matchAll(/([A-Z][a-z]?|[()])(\d*)/g)) { push(out, p[1]); if (p[2]) out.push(['sub', [p[2]]]); }
              i += f.length; continue;
            }
          }
        }
        if (SUB_IN[c] && out.length) { m = at(SUBD, s, i); out.push(['sub', [[...m[0]].map((x) => SUB_IN[x]).join('')]]); i += m[0].length; continue; }
        if (SUP_IN[c] && out.length) {
          m = at(SUPD, s, i);
          if (/[⁺⁻]/.test(m[0])) { out.push(['sup', [[...m[0]].map((x) => SUP_IN[x]).join('')]]); i += m[0].length; continue; }
        }
        if (s.startsWith('->', i)) { push(out, '→'); i += 2; continue; }
      }
      if (math) {
        const op = MATH_OPS.find(([a]) => s.startsWith(a, i));
        if (op) { push(out, op[1]); i += op[0].length; continue; }
        if (c === '*') {
          if (out.length && typeof out[out.length - 1] === 'string') out[out.length - 1] = out[out.length - 1].replace(/ +$/, '');
          push(out, ' · '); i++; while (i < n && s[i] === ' ') i++; continue;
        }
        if (c === '-') { push(out, '−'); i++; continue; }
        if (c === '(') {
          const j = matchClose(s, i);
          if (j < 0) { this.errors.push('páratlan zárójel'); push(out, '('); i++; continue; }
          const inner = this.seq(s.slice(i + 1, j), true, big);
          if (big && (m = at(BIGSLASH, s, j + 1))) {
            const k = j + m[0].length, j2 = matchClose(s, k);
            if (j2 > 0) { out.push(['frac', inner, this.seq(s.slice(k + 1, j2), true, big)]); i = j2 + 1; continue; }
          }
          push(out, '('); for (const x of inner) push(out, x); push(out, ')'); i = j + 1; continue;
        }
        if (c === ')') { this.errors.push('páratlan zárójel'); push(out, ')'); i++; continue; }
        if (c === '"') { const j = s.indexOf('"', i + 1); if (j > 0) { push(out, s.slice(i + 1, j)); i = unitEnd = j + 1; continue; } }
        if (c === '°' && (s[i + 1] === 'C' || s[i + 1] === 'F') && !(i + 2 < n && IS_WORD.test(s[i + 2]))) { push(out, s.slice(i, i + 2)); i = unitEnd = i + 2; continue; }
        if ((m = at(UNIT_WORD, s, i)) && UNITS.has(m[0].replace('μ', 'µ')) && !(i + m[0].length < n && (IS_WORD.test(s[i + m[0].length]) || '′″‴('.includes(s[i + m[0].length])))) {
          const w = m[0], cont = unitEnd >= 0 && ['/', '·', '*'].includes(s.slice(unitEnd, i).trim());
          if (cont || afterNumber(out) && (w.length > 1 || prev === ' ')) { push(out, w.replace('μ', 'µ')); i = unitEnd = i + w.length; continue; }
        }
        if (GREEK.test(c)) {
          if (!isVar(c)) { push(out, c); i++; continue; }
          const pr = at(PRIMES, s, i + 1), t = c + (pr ? pr[0] : '');
          out.push(['i', t]); i += t.length; continue;
        }
        if ((m = at(WORD, s, i))) {
          const w = m[0];
          if (NAMED[w]) push(out, NAMED[w]);
          else if (!/^[A-Za-z]+$/.test(w) || FUNCS.has(w)) push(out, w);
          else { const pr = at(PRIMES, s, i + w.length); out.push(['i', w + (pr ? pr[0] : '')]); i += pr ? pr[0].length : 0; }
          i += w.length; continue;
        }
      }
      push(out, c); i++;
    }
    return out;
  };

  function parse(s, o = {}) {
    if (Array.isArray(s)) return s;
    const p = new Parser(o.frac !== false, !!o.chem);
    const t = o.math ? p.seq(String(s), true, !!o.big) : p.seq(String(s), false, false);
    parse.errors = p.errors;
    return t;
  }

  // ── elrendezés és rajz ──
  const FD = () => (window.Lesson && Lesson.FONTS.D) || 'Fraunces';
  const FM = () => (window.Lesson && Lesson.FONTS.M) || '"JetBrains Mono"';

  // → {w, asc, desc, items: [{t: 'tx', s, dx, dy, o} | {t: 'ln', x0, x1, dy, lw} | {t: 'rad', dx, dy, w, h, lw}]}
  function layout(L, nodes, sz, o, math) {
    let x = 0, asc = sz * .74, desc = sz * .24;
    const items = [];
    const font = (italic) => italic ? { s: sz, f: o.vf || FD(), i: true, w: o.vw || 400 } : { s: sz, f: o.f || FM(), w: o.w || 500, ls: o.ls };
    const add = (box, dy = 0) => {
      for (const it of box.items) items.push(Object.assign({}, it, { dx: it.dx + x, dy: (it.dy || 0) + dy }));
      asc = Math.max(asc, box.asc - dy); desc = Math.max(desc, box.desc + dy); x += box.w;
    };
    for (const nd of nodes) {
      if (typeof nd === 'string' || nd[0] === 'i') {
        const s = typeof nd === 'string' ? nd : nd[1], fo = font(nd[0] === 'i' && typeof nd !== 'string');
        const w = L.measure(s, fo).w;
        items.push({ t: 'tx', s, dx: x, dy: 0, o: fo });
        x += w + (fo.i ? sz * .04 : 0);
        continue;
      }
      const k = nd[0];
      if (k === 'mx') { add(layout(L, nd[1], sz, o, true)); continue; }
      if (k === 'sup' || k === 'sub') {
        const b = layout(L, nd[1], sz * .65, o, math);
        add(b, k === 'sup' ? -sz * .42 : sz * .2); x += sz * .04; continue;
      }
      if (k === 'frac') {
        const fs = sz * .8, nb = layout(L, nd[1], fs, o, true), db = layout(L, nd[2], fs, o, true);
        const pad = sz * .1, w = Math.max(nb.w, db.w) + pad * 2, axis = -sz * .3, gap = Math.max(4, sz * .14), lw = Math.max(2, sz * .07);
        const nDy = axis - gap - nb.desc, dDy = axis + gap + db.asc;
        const box = { w: w + sz * .12, asc: -(nDy - nb.asc), desc: dDy + db.desc, items: [] };
        for (const it of nb.items) box.items.push(Object.assign({}, it, { dx: it.dx + sz * .06 + (w - nb.w) / 2, dy: (it.dy || 0) + nDy }));
        for (const it of db.items) box.items.push(Object.assign({}, it, { dx: it.dx + sz * .06 + (w - db.w) / 2, dy: (it.dy || 0) + dDy }));
        box.items.push({ t: 'ln', dx: sz * .06, x1: w, dy: axis, lw });
        add(box); continue;
      }
      if (k === 'sqrt') {
        const b = layout(L, nd[1], sz, o, true), lw = Math.max(2, sz * .07), rw = sz * .55, top = b.asc + sz * .12;
        const box = { w: rw + b.w + sz * .1, asc: top + lw, desc: b.desc, items: [{ t: 'rad', dx: 0, dy: 0, w: rw, top, bot: b.desc * .6, lw, len: b.w + sz * .1 }] };
        for (const it of b.items) box.items.push(Object.assign({}, it, { dx: it.dx + rw + sz * .05 }));
        add(box); continue;
      }
    }
    return { w: x, asc, desc, items };
  }

  function prep(L, s, o) {
    const tree = parse(s, o);
    let sz = o.s || 30, b = layout(L, tree, sz, o, !!o.math);
    if (o.max && b.w > o.max) { sz = sz * o.max / b.w; b = layout(L, tree, sz, o, !!o.math); }
    return b;
  }

  function measure(L, s, o = {}) { const b = prep(L, s, o); return { w: b.w, h: b.asc + b.desc, asc: b.asc, desc: b.desc }; }

  function draw(L, s, x, y, o = {}) {
    const b = prep(L, s, o), c = L.ctx, a = o.a || 'left', bl = o.b || 'alphabetic';
    const x0 = a === 'center' ? x - b.w / 2 : a === 'right' ? x - b.w : x;
    const base = bl === 'middle' ? y + (b.asc - b.desc) / 2 : bl === 'top' ? y + b.asc : bl === 'bottom' ? y - b.desc : y;
    const col = o.c || L.ink || '#1c2440';
    for (const it of b.items) {
      if (it.t === 'tx') {
        L.tx(it.s, x0 + it.dx, base + it.dy, Object.assign({}, it.o, { c: col, a: 'left', b: 'alphabetic', k: o.k, qa: o.qa }));
      } else if (it.t === 'ln') {
        c.save(); c.strokeStyle = col; c.lineWidth = it.lw; c.lineCap = 'round';
        c.beginPath(); c.moveTo(x0 + it.dx, base + it.dy); c.lineTo(x0 + it.dx + it.x1, base + it.dy); c.stroke(); c.restore();
      } else if (it.t === 'rad') {
        const X = x0 + it.dx, Y = base + it.dy;
        c.save(); c.strokeStyle = col; c.lineWidth = it.lw; c.lineJoin = 'round'; c.lineCap = 'round';
        c.beginPath(); c.moveTo(X, Y - it.top * .45); c.lineTo(X + it.w * .25, Y - it.top * .55); c.lineTo(X + it.w * .55, Y + it.bot);
        c.lineTo(X + it.w * .95, Y - it.top); c.lineTo(X + it.w + it.len, Y - it.top); c.stroke(); c.restore();
      }
    }
    return { x: x0, y: base - b.asc, w: b.w, h: b.asc + b.desc };
  }

  function frac(L, n, d, x, y, o = {}) {
    const t = [];
    if (o.sign) t.push(o.sign === '-' ? '−' : o.sign);
    if (o.whole) t.push(String(o.whole));
    t.push(['frac', [String(n)], [String(d)]]);
    return draw(L, t, x, y, o);
  }

  function fmtNum(v, d = 0, opt = {}) {
    const U = window.Lesson && Lesson.U;
    const s = U ? U.fmt(v, d) : (v < 0 ? '−' : '') + Math.abs(v).toFixed(d).replace('.', ',');
    return opt.plus && v > 0 ? '+' + s : s;
  }

  function showError(L, msg) {
    console.error(msg);
    let e = document.getElementById('lesson-error');
    if (!e) { e = document.createElement('div'); e.id = 'lesson-error'; (L.stage || document.body).append(e); }
    if (!e.textContent.includes(msg)) e.textContent += (e.textContent ? '\n' : '') + msg;
  }

  function check(L, key, expected, eps = 1e-9) {
    const d = L.dat(key);
    let v = d.v;
    if (d.t === 'frac') v = (d.neg ? -1 : 1) * (d.w + d.n / d.d);
    const ev = expected instanceof Q ? expected.v : +expected;
    if (!(Math.abs(v - ev) <= eps * Math.max(1, Math.abs(ev)))) {
      showError(L, `Ellenőrzés: a .md „${key}” adata ${L.val(key)}, a lecke számolása szerint ${expected instanceof Q ? expected.str() : fmtNum(ev, 4).replace(/,?0+$/, '')}. Javítsd a .md-t (vagy jelezd a hibát).`);
      return false;
    }
    return true;
  }

  // ── MatQ: pontos tört ──
  const gcd = (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; };
  const lcm = (a, b) => Math.abs(a / gcd(a, b) * b);
  function Q(n, d = 1) {
    if (!(this instanceof Q)) return new Q(n, d);
    if (n instanceof Q) { this.n = n.n; this.d = n.d; return; }
    if (!Number.isInteger(n) || !Number.isInteger(d)) { const q = Q.fromNumber(n / d); n = q.n; d = q.d; }
    if (d === 0) throw new Error('MatQ: a nevező 0');
    if (d < 0) { n = -n; d = -d; }
    const g = gcd(n, d) || 1; this.n = n / g; this.d = d / g;
  }
  const toQ = (q) => q instanceof Q ? q : Q.fromNumber(q);
  Q.fromNumber = (x) => {
    if (Number.isInteger(x)) return new Q(x, 1);
    const s = String(x); if (/e/i.test(s)) throw new Error('MatQ: túl kicsi/nagy szám: ' + s);
    const [i, f = ''] = s.split('.'), d = Math.pow(10, f.length);
    return new Q(Math.round(x * d), d);
  };
  Q.prototype = {
    get v() { return this.n / this.d; },
    add(q) { q = toQ(q); return new Q(this.n * q.d + q.n * this.d, this.d * q.d); },
    sub(q) { q = toQ(q); return new Q(this.n * q.d - q.n * this.d, this.d * q.d); },
    mul(q) { q = toQ(q); return new Q(this.n * q.n, this.d * q.d); },
    div(q) { q = toQ(q); if (!q.n) throw new Error('MatQ: osztás 0-val'); return new Q(this.n * q.d, this.d * q.n); },
    neg() { return new Q(-this.n, this.d); },
    inv() { return new Q(this.d, this.n); },
    cmp(q) { q = toQ(q); const a = this.n * q.d, b = q.n * this.d; return a < b ? -1 : a > b ? 1 : 0; },
    eq(q) { return this.cmp(q) === 0; },
    str(mode) {
      const neg = this.n < 0, n = Math.abs(this.n), sg = neg ? '−' : '';
      if (this.d === 1) return sg + n;
      if (mode === 'mixed' && n > this.d) return sg + Math.floor(n / this.d) + ' ' + (n % this.d) + '/' + this.d;
      return sg + n + '/' + this.d;
    },
    dec(k) {
      const neg = this.n < 0, n = Math.abs(this.n), d = this.d, sg = neg ? '−' : '';
      if (k != null) return fmtNum(this.v, k);
      let ip = Math.floor(n / d), r = n % d, digs = ''; const seen = new Map();
      while (r && !seen.has(r) && digs.length < 60) { seen.set(r, digs.length); r *= 10; digs += Math.floor(r / d); r %= d; }
      const I = sg + fmtNum(ip, 0);
      if (!r) return digs ? I + ',' + digs : I;
      const p = seen.get(r), pre = I + ',' + digs.slice(0, p), rep = digs.slice(p);
      return { pre, rep, s: pre + '(' + rep + ')' };
    },
    toString() { return this.str(); },
  };
  Q.gcd = gcd; Q.lcm = lcm;
  Q.parse = (s) => {
    const m = String(s).trim().match(/^([−\-+]?)\s*(?:(\d+)\s+)?(\d+)\s*\/\s*(\d+)$/);
    if (m) { const q = new Q(+(m[2] || 0) * +m[4] + +m[3], +m[4]); return m[1] === '−' || m[1] === '-' ? q.neg() : q; }
    const x = Number(String(s).trim().replace('−', '-').replace(/\s/g, '').replace(',', '.'));
    if (!isFinite(x)) throw new Error('MatQ.parse: ' + s);
    return Q.fromNumber(x);
  };
  Q.from = (d) => {
    if (!d) throw new Error('MatQ.from: nincs adat');
    if (d.t === 'frac') { const q = new Q(d.w * d.d + d.n, d.d); return d.neg ? q.neg() : q; }
    if (d.t === 'ratio') return Q.fromNumber(d.a).div(d.b);
    return Q.fromNumber(d.v);
  };

  // ── expr-fa kiértékelése (eval nélkül) ──
  function evalWith(e, vars, ops) {
    if (typeof e === 'number') return ops.num(e);
    if (typeof e === 'string') { if (!(e in vars)) throw new Error('evalExpr: nincs értéke: ' + e); return ops.num(vars[e]); }
    const [op, a, b] = e, A = () => evalWith(a, vars, ops), B = () => evalWith(b, vars, ops);
    switch (op) {
      case '()': return A();
      case 'neg': return ops.neg(A());
      case 'pos': return A();
      case 'abs': return ops.abs(A());
      case '√': return ops.sqrt(A());
      case '+': return ops.add(A(), B());
      case '−': return ops.sub(A(), B());
      case '·': case 'imp': return ops.mul(A(), B());
      case ':': case '/': return ops.div(A(), B());
      case '^': return ops.pow(A(), B());
      case '=': case '<': case '>': case '≤': case '≥': case '≠': return ops.rel(op, A(), B());
      default: throw new Error('evalExpr: ismeretlen művelet ' + op);
    }
  }
  const FLOAT = {
    num: (x) => +x, neg: (x) => -x, abs: Math.abs, sqrt: Math.sqrt, add: (x, y) => x + y, sub: (x, y) => x - y,
    mul: (x, y) => x * y, div: (x, y) => x / y, pow: Math.pow,
    rel: (op, x, y) => ({ '=': Math.abs(x - y) < 1e-9, '<': x < y, '>': x > y, '≤': x <= y + 1e-9, '≥': x >= y - 1e-9, '≠': Math.abs(x - y) >= 1e-9 })[op],
  };
  const EXACT = {
    num: (x) => x instanceof Q ? x : Q.fromNumber(x), neg: (x) => x.neg(), abs: (x) => x.n < 0 ? x.neg() : x,
    sqrt: () => { throw new Error('MatQ.evalExpr: √ nem pontos'); }, add: (x, y) => x.add(y), sub: (x, y) => x.sub(y),
    mul: (x, y) => x.mul(y), div: (x, y) => x.div(y),
    pow: (x, y) => { if (y.d !== 1) throw new Error('MatQ.evalExpr: tört kitevő'); let r = new Q(1), k = Math.abs(y.n); while (k--) r = r.mul(x); return y.n < 0 ? r.inv() : r; },
    rel: (op, x, y) => { const c = x.cmp(y); return ({ '=': c === 0, '<': c < 0, '>': c > 0, '≤': c <= 0, '≥': c >= 0, '≠': c !== 0 })[op]; },
  };
  Q.evalExpr = (tree, vars = {}) => evalWith(tree, vars, EXACT);

  const css = `
.lp-text .frac, .lp-title .frac, .big-fx .frac { display: inline-flex; flex-direction: column; vertical-align: middle;
  text-align: center; font-size: .82em; line-height: 1.08; margin: 0 .1em; }
.frac .fn { border-bottom: max(2px, .07em) solid currentColor; padding: 0 .12em .04em; }
.frac .fd { padding: .04em .12em 0; }
.frac .fs, .rt .rp { display: none; }
.big-fx .frac { font-size: .78em; }
.rt { white-space: nowrap; }
.rt .rad { border-top: max(2px, .06em) solid currentColor; padding: .02em .06em 0 .04em; margin-left: .02em; }
.lp-text .mx, .lp-title .mx { font-family: Fraunces, serif; white-space: nowrap; }
.mx i { font-style: italic; padding-right: .04em; }
.lp-text sup, .lp-text sub, .lp-title sup, .lp-title sub, .big-fx sup, .big-fx sub { font-size: .68em; line-height: 0; }`;
  if (typeof document !== 'undefined' && !document.getElementById('mtext-css')) {
    const st = document.createElement('style'); st.id = 'mtext-css'; st.textContent = css;
    (document.head || document.documentElement).append(st);
  }

  const MatText = { parse, layout, measure, draw, frac, num: fmtNum, check, css, evalExpr: (tree, vars = {}) => evalWith(tree, vars, FLOAT) };
  const root = typeof window !== 'undefined' ? window : globalThis;
  root.MatText = MatText; root.MatQ = Q;
})();
