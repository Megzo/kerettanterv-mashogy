/* ───────────────────────────────────────────────────────────────
   TortProj – vetületek és dekódolás a shared/tort/map-*.js adatokhoz
   Tiszta függvények, globális állapot nélkül; a rajzolást (stílus, címkék, kamera-animáció)
   a lecke végzi. Leírás és példa: shared/tort/README.md.

   TortProj.unpack(M)          a map-*.js objektumából (pl. window.TORT_MAP_KARPAT) lebegőpontos,
                               fokos koordináták: {land: [Float64Array [lon,lat,lon,lat,…]], lakes: [{n, p: [...]}],
                               rivers: [{n, en, r, p: [...]}], regions: [{n, t, c: [lon,lat], p}], lines, bbox}
                               – egyszer hívd (init), ne képkockánként.
   TortProj.decode(flat, q)    egy delta-kódolt tömb → Float64Array [lon, lat, …] fokban
   TortProj.lcc({lon0, lat0, lat1, lat2})
                               Lambert-féle szögtartó kúpvetület (gömbi): lon0 középmeridián, lat0 a vetület
                               origójának szélessége, lat1/lat2 álló szélességi körök. Pl. Kárpát-medence:
                               {lon0: 19.5, lat0: 47, lat1: 45, lat2: 49}; Földközi-tenger: {lon0: 20, lat0: 38, lat1: 30, lat2: 46}.
   TortProj.ortho({lon0, lat0}) ortografikus földgömb, (lon0, lat0) néz a néző felé. fwd → [x, y, z]; z < 0: hátoldal.
                               Minden vetület: fwd(lon, lat) → [x, y] Föld-sugár egységben (északra +y), inv(x, y) → [lon, lat].
   TortProj.equalEarth({lon0}) Equal Earth egyenlő területű világvetület (Šavrič–Patterson–Jenny 2018), lon0 a
                               középmeridián (alapértelmezés 0). Tematikus (területarányos) világtérképhez. A térkép széle a
                               lon0 ± 180° délkör: a varraton átnyúló gyűrűt a trace mindkét oldalon megrajzolja (a térkép
                               széléig: vágj `TortProj.outline`-nal), a nyitott vonalat a varratnál megszakítja.
   TortProj.outline(ctx, V, n?) a vetület teljes körvonala útvonalként (equalEarth: a térkép pereme, ortho: a korong;
                               beginPath a hívóé) – óceán-kitöltéshez és vágáshoz (ctx.clip()).
   TortProj.view(proj, {lon, lat, s, x, y})
                               képernyő-leképezés: a (lon, lat) pont a képernyő (x, y) pontjára esik, s = px / Föld-sugár.
                               → {pt(lon, lat) → [sx, sy, látható], inv(sx, sy) → [lon, lat], kmPx: px/km,
                                  cx, cy: a vetület origójának képernyőhelye (ortho: a korong középpontja), …}
                               A pt minden hívásra ÚJ tömböt ad (eltárolható; v1.1 előtt ugyanazt a tömböt írta felül).
                               Kameramozgás: két view-paraméter között interpolálj (lon, lat lineárisan, s logaritmikusan).
   TortProj.fit(proj, [lonMin, latMin, lonMax, latMax], [x, y, w, h], pad?)
                               → {lon, lat, s, x, y}: a view-paraméter, amellyel a fokos téglalap kitölti a képernyő-téglalapot.
   TortProj.trace(ctx, V, pts, {close, edge, ortho})
                               moveTo/lineTo útvonal (beginPath/fill/stroke a hívóé). close: gyűrű.
                               edge: [lonMin, latMin, lonMax, latMax] – az erre a keretre eső (vágásból származó) éleket
                               kihagyja → partvonal-körvonalhoz. ortho (csak ortho vetületnél):
                                 'fill'   – a gyűrűt a látható félgömbre vágja (horizontvágás): a látható szakaszokat a
                                            peremen pontosan elvágja, és a perem mentén, ívvel zárja (mint a d3-geo
                                            clipCircle). A gyűrű belseje a lon/lat síkon bezárt tartomány (a körüljárás
                                            irányából). A kimenet csupa zárt, a korongon belüli gyűrű → 'evenodd' kitöltés
                                            és páros–páratlan találatvizsgálat is helyes, vágni sem kell. Teljesen hátoldali
                                            gyűrű: semmi – vagy a teljes korong, ha a belseje a nézőpontot is tartalmazza.
                                 'stroke' – csak a látható rész; a peremet átlépő szakasz a peremig fut (ott megszakad).
                               Az élek főkörívnek számítanak (2–3°-os élekkel bőven pontos).
   Változások: v1.1 (2026-11-24) – ortho 'fill' valódi horizontvágás (előtte a hátoldali pontok a peremre vetültek,
                               ezért a horizonton átnyúló nagy gyűrűk hamis csíkokat festettek, és a találat is hibás
                               volt); 'stroke' a peremig fut; view().pt friss tömböt ad; view().cx/cy; ortho outline a
                               vetület középpontja körül (eddig V.x, V.y – ugyanaz, ha a nézet a vetület középpontja).
   TortProj.gc(lon1, lat1, lon2, lat2, n)
                               főkör (legrövidebb út a gömbön) n+1 ponttal → [[lon, lat], …] (útvonalnyilakhoz, gömbön)
   TortProj.dist(lon1, lat1, lon2, lat2)  távolság km-ben (gömb, R = 6371 km)
   ─────────────────────────────────────────────────────────────── */
(function () {
  'use strict';
  const D = Math.PI / 180, R_KM = 6371;

  function decode(flat, q) {
    const out = new Float64Array(flat.length);
    let x = 0, y = 0;
    for (let i = 0; i < flat.length; i += 2) {
      x += flat[i]; y += flat[i + 1];
      out[i] = x / q; out[i + 1] = y / q;
    }
    return out;
  }

  function unpack(M) {
    const q = M.q, dec = (a) => decode(a, q);
    const feat = (o) => Object.assign({}, o, { p: o.p.map(dec) }, o.c ? { c: [o.c[0] / q, o.c[1] / q] } : {});
    return {
      name: M.name, scale: M.scale, bbox: M.bbox.map((v) => v / q),
      land: (M.land || []).map(dec), lakes: (M.lakes || []).map(feat), rivers: (M.rivers || []).map(feat),
      regions: (M.regions || []).map(feat), lines: (M.lines || []).map(dec),
    };
  }

  const wrap = (d) => ((d + 540) % 360) - 180;

  function lcc(o) {
    const f1 = o.lat1 * D, f2 = o.lat2 * D, f0 = (o.lat0 != null ? o.lat0 : (o.lat1 + o.lat2) / 2) * D;
    const t = (f) => Math.tan(Math.PI / 4 + f / 2);
    const n = Math.abs(o.lat1 - o.lat2) < 1e-9 ? Math.sin(f1) : Math.log(Math.cos(f1) / Math.cos(f2)) / Math.log(t(f2) / t(f1));
    const F = Math.cos(f1) * Math.pow(t(f1), n) / n;
    const rho = (f) => F / Math.pow(t(f), n), rho0 = rho(f0);
    return {
      kind: 'lcc', o,
      fwd(lon, lat) {
        const r = rho(Math.max(-89.9, Math.min(89.9, lat)) * D), th = n * wrap(lon - o.lon0) * D;
        return [r * Math.sin(th), rho0 - r * Math.cos(th)];
      },
      inv(x, y) {
        const dy = rho0 - y, r = Math.sign(n) * Math.hypot(x, dy), th = Math.atan2(x * Math.sign(n), dy * Math.sign(n));
        return [o.lon0 + th / n / D, (2 * Math.atan(Math.pow(F / r, 1 / n)) - Math.PI / 2) / D];
      },
    };
  }

  function ortho(o) {
    const l0 = o.lon0 * D, p0 = o.lat0 * D, sp0 = Math.sin(p0), cp0 = Math.cos(p0);
    return {
      kind: 'ortho', o,
      fwd(lon, lat) {
        const l = lon * D - l0, p = lat * D, cp = Math.cos(p), sp = Math.sin(p), cl = Math.cos(l);
        return [cp * Math.sin(l), cp0 * sp - sp0 * cp * cl, sp0 * sp + cp0 * cp * cl];
      },
      inv(x, y) {
        const r = Math.hypot(x, y);
        if (r > 1) return [NaN, NaN];
        const c = Math.asin(r), sc = Math.sin(c), cc = Math.cos(c);
        if (r < 1e-12) return [o.lon0, o.lat0];
        return [wrap((l0 + Math.atan2(x * sc, r * cp0 * cc - y * sp0 * sc)) / D), Math.asin(cc * sp0 + y * sc * cp0 / r) / D];
      },
    };
  }

  // Equal Earth (B. Šavrič, T. Patterson, B. Jenny, 2018, Int. J. Geogr. Inf. Sci. 33(3)). x, y Föld-sugár egységben.
  const EA1 = 1.340264, EA2 = -0.081106, EA3 = 0.000893, EA4 = 0.003796, EM = Math.sqrt(3) / 2;
  function eeRaw(dl, lat) {          // dl: a középmeridiántól mért hosszúság fokban, NEM tekerve (a varraton túl is)
    const th = Math.asin(EM * Math.sin(Math.max(-90, Math.min(90, lat)) * D)), t2 = th * th, t6 = t2 * t2 * t2;
    return [2 * Math.sqrt(3) * dl * D * Math.cos(th) / (3 * (EA1 + 3 * EA2 * t2 + t6 * (7 * EA3 + 9 * EA4 * t2))),
            th * (EA1 + EA2 * t2 + t6 * (EA3 + EA4 * t2))];
  }
  function equalEarth(o) {
    o = Object.assign({ lon0: 0 }, o || {});
    const rel = (lon) => { let d = lon - o.lon0; while (d > 180) d -= 360; while (d < -180) d += 360; return d; };  // ±180 marad
    return {
      kind: 'equalEarth', o, raw: eeRaw, rel,
      fwd(lon, lat) { return eeRaw(rel(lon), lat); },
      inv(x, y) {
        let th = y / EA1;
        for (let i = 0; i < 12; i++) {
          const t2 = th * th, t6 = t2 * t2 * t2;
          const f = th * (EA1 + EA2 * t2 + t6 * (EA3 + EA4 * t2)) - y, df = EA1 + 3 * EA2 * t2 + t6 * (7 * EA3 + 9 * EA4 * t2);
          const d = f / df; th -= d;
          if (Math.abs(d) < 1e-12) break;
        }
        const t2 = th * th, t6 = t2 * t2 * t2, s = Math.sin(th) / EM;
        if (!(Math.abs(s) <= 1)) return [NaN, NaN];
        const dl = 3 * x * (EA1 + 3 * EA2 * t2 + t6 * (7 * EA3 + 9 * EA4 * t2)) / (2 * Math.sqrt(3) * Math.cos(th)) / D;
        if (Math.abs(dl) > 180 + 1e-9) return [NaN, NaN];
        return [wrap(o.lon0 + dl), Math.asin(s) / D];
      },
    };
  }

  function outline(ctx, V, n) {
    n = n || 90;
    if (V.proj.kind === 'ortho') { const cx = V.cx == null ? V.x : V.cx, cy = V.cy == null ? V.y : V.cy; ctx.moveTo(cx + V.s, cy); ctx.arc(cx, cy, V.s, 0, 2 * Math.PI); return; }
    if (V.proj.kind !== 'equalEarth') return;
    const c = V.proj.fwd(V.lon, V.lat), P = V.proj;
    for (let i = 0; i <= 2 * n + 1; i++) {
      const side = i <= n ? 180 : -180, k = i <= n ? i : 2 * n + 1 - i, lat = -90 + 180 * k / n, p = P.raw(side, lat);
      const sx = V.x + (p[0] - c[0]) * V.s, sy = V.y - (p[1] - c[1]) * V.s;
      if (i === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
    }
    ctx.closePath();
  }

  // Equal Earth: varrat-kezelés. Gyűrű: a hosszúságot folytonosan „letekerjük”, és ha a gyűrű átnyúlik a varraton,
  // ±360°-kal eltolt másolatban is megrajzoljuk (a térképen kívüli részt a hívó vágja le az outline-nal).
  // Nyitott vonal: a varrat-átlépésnél megszakad.
  function traceEE(ctx, V, pts, o) {
    const P = V.proj, c = P.fwd(V.lon, V.lat), n = pts.length / 2;
    if (n < 1) return;
    const scr = (dl, lat) => { const p = P.raw(dl, lat); return [V.x + (p[0] - c[0]) * V.s, V.y - (p[1] - c[1]) * V.s]; };
    if (!o.close) {
      let prev = null;
      for (let i = 0; i < n; i++) {
        const dl = P.rel(pts[2 * i]), p = scr(dl, pts[2 * i + 1]);
        if (prev === null || Math.abs(dl - prev) > 180) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
        prev = dl;
      }
      return;
    }
    const U = new Float64Array(n);
    let lo = Infinity, hi = -Infinity;
    for (let i = 0; i < n; i++) {
      const d = P.rel(pts[2 * i]);
      U[i] = i === 0 ? d : U[i - 1] + (((d - U[i - 1]) % 360) + 540) % 360 - 180;
      lo = Math.min(lo, U[i]); hi = Math.max(hi, U[i]);
    }
    const shifts = [0];
    if (hi > 180 + 1e-9) shifts.push(-360);
    if (lo < -180 - 1e-9) shifts.push(360);
    for (const sh of shifts) {
      for (let i = 0; i < n; i++) {
        const p = scr(U[i] + sh, pts[2 * i + 1]);
        if (i === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
      }
      ctx.closePath();
    }
  }

  function view(proj, v) {
    const c = proj.fwd(v.lon, v.lat), s = v.s, X = v.x, Y = v.y;
    return {
      proj, lon: v.lon, lat: v.lat, s, x: X, y: Y, kmPx: s / R_KM, c0: c[0], c1: c[1], cx: X - c[0] * s, cy: Y + c[1] * s,
      pt(lon, lat) {
        const p = proj.fwd(lon, lat);
        return [X + (p[0] - c[0]) * s, Y - (p[1] - c[1]) * s, p.length < 3 || p[2] >= 0];   // friss tömb (eltárolható)
      },
      inv(sx, sy) { return proj.inv(c[0] + (sx - X) / s, c[1] - (sy - Y) / s); },
    };
  }

  function fit(proj, b, rect, pad) {
    pad = pad == null ? 0 : pad;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (let i = 0; i <= 24; i++) {
      const u = i / 24;
      for (const [lon, lat] of [[b[0] + u * (b[2] - b[0]), b[1]], [b[0] + u * (b[2] - b[0]), b[3]], [b[0], b[1] + u * (b[3] - b[1])], [b[2], b[1] + u * (b[3] - b[1])]]) {
        const p = proj.fwd(lon, lat);
        x0 = Math.min(x0, p[0]); x1 = Math.max(x1, p[0]); y0 = Math.min(y0, p[1]); y1 = Math.max(y1, p[1]);
      }
    }
    const s = Math.min((rect[2] - 2 * pad) / (x1 - x0), (rect[3] - 2 * pad) / (y1 - y0));
    const ll = proj.inv((x0 + x1) / 2, (y0 + y1) / 2);
    return { lon: ll[0], lat: ll[1], s, x: rect[0] + rect[2] / 2, y: rect[1] + rect[3] / 2 };
  }

  const onEdge = (e, ax, ay, bx, by) => (Math.abs(ax - bx) < 1e-6 && (Math.abs(ax - e[0]) < 1e-6 || Math.abs(ax - e[2]) < 1e-6)) ||
                                        (Math.abs(ay - by) < 1e-6 && (Math.abs(ay - e[1]) < 1e-6 || Math.abs(ay - e[3]) < 1e-6));

  function trace(ctx, V, pts, o) {
    o = o || {};
    if (V.proj.kind === 'equalEarth' && !o.edge) return traceEE(ctx, V, pts, o);
    if (V.proj.kind === 'ortho' && o.ortho) return traceOrtho(ctx, V, pts, o);
    const e = o.edge, n = pts.length / 2, P = V.proj, s = V.s, X = V.x, Y = V.y, c0 = V.c0, c1 = V.c1;
    if (n < 1) return;
    let pen = false;
    const last = o.close ? n : n - 1;
    for (let i = 0; i <= last; i++) {
      const k = (i % n) * 2, lon = pts[k], lat = pts[k + 1];
      let sx, sy;
      if (c0 != null) { const p = P.fwd(lon, lat); sx = X + (p[0] - c0) * s; sy = Y - (p[1] - c1) * s; }   // = V.pt, tömb nélkül
      else { const p = V.pt(lon, lat); sx = p[0]; sy = p[1]; }
      if (i > 0 && e) {
        const j = ((i - 1) % n) * 2;
        if (onEdge(e, pts[j], pts[j + 1], lon, lat)) pen = false;
      }
      if (!pen || (o.close && i === 0)) { ctx.moveTo(sx, sy); pen = true; } else ctx.lineTo(sx, sy);
    }
    if (o.close && !e) ctx.closePath();
  }

  /* ── ortho: horizontvágás ──
     A csúcsok a vetület egységgömbjén (x kelet, y észak, z a néző felé); a látható félgömb z ≥ 0. Egy él és a horizont
     metszéspontja a húr z = 0 pontjának normáltja (a főkörív pontosan ott lépi át a peremet). 'fill': a látható láncokat
     (belépés → csúcsok → kilépés) a perem mentén kötjük össze: a kilépési ponttól a gyűrű belseje felé (a lon/lat
     körüljárás iránya: pozitív terület → a belseje balra → az óramutatóval ellentétesen) a legközelebbi belépési pontig. */
  const ringArea = (a, n) => { let s = 0; for (let i = 0, j = n - 1; i < n; j = i++) s += a[2 * j] * a[2 * i + 1] - a[2 * i] * a[2 * j + 1]; return s / 2; };
  function inRingLL(a, n, x, y) {
    let ins = false;
    for (let i = 0, j = n - 1; i < n; j = i++) {
      const xi = a[2 * i], yi = a[2 * i + 1], xj = a[2 * j], yj = a[2 * j + 1];
      if ((yi > y) !== (yj > y) && x < (xj - xi) * (y - yi) / (yj - yi) + xi) ins = !ins;
    }
    return ins;
  }
  let OB = new Float64Array(3 * 2048);
  function traceOrtho(ctx, V, pts, o) {
    const P = V.proj, n = pts.length / 2;
    if (n < 1) return;
    const s = V.s, X0 = V.cx == null ? V.x : V.cx, Y0 = V.cy == null ? V.y : V.cy, e = o.edge, TAU = 2 * Math.PI;
    if (OB.length < 3 * n) OB = new Float64Array(3 * n + 768);
    const A = OB;
    let nv = 0;
    for (let i = 0; i < n; i++) {
      const p = P.fwd(pts[2 * i], pts[2 * i + 1]);
      const z = Math.abs(p[2]) < 1e-12 ? 0 : p[2];       // a pontosan a peremre eső csúcs (pl. pólus) látható
      A[3 * i] = p[0]; A[3 * i + 1] = p[1]; A[3 * i + 2] = z; if (z >= 0) nv++;
    }
    const M = (k) => ctx.moveTo(X0 + A[3 * k] * s, Y0 - A[3 * k + 1] * s), Ln = (k) => ctx.lineTo(X0 + A[3 * k] * s, Y0 - A[3 * k + 1] * s);
    const cut = (j, k) => {             // a (j, k) él peremátlépése → [x, y] az egységkörön
      const zj = A[3 * j + 2], zk = A[3 * k + 2], t = zj / (zj - zk);
      const x = A[3 * j] + (A[3 * k] - A[3 * j]) * t, y = A[3 * j + 1] + (A[3 * k + 1] - A[3 * j + 1]) * t, h = Math.hypot(x, y) || 1;
      return [x / h, y / h];
    };
    if (o.ortho !== 'fill' || !o.close) {          // 'stroke' (vagy nyitott vonal): látható rész, a peremig
      const last = o.close ? n : n - 1;
      let pen = false;
      for (let i = 0; i <= last; i++) {
        const k = i % n, zk = A[3 * k + 2];
        if (i === 0) { if (zk >= 0) { M(k); pen = true; } continue; }
        const j = (i - 1) % n, zj = A[3 * j + 2];
        if (e && onEdge(e, pts[2 * j], pts[2 * j + 1], pts[2 * k], pts[2 * k + 1])) { pen = false; if (zk >= 0) { M(k); pen = true; } continue; }
        if (zj >= 0 && zk >= 0) { if (!pen) M(j); Ln(k); pen = true; }
        else if (zj >= 0) { const q = cut(j, k); if (!pen) M(j); ctx.lineTo(X0 + q[0] * s, Y0 - q[1] * s); pen = false; }
        else if (zk >= 0) { const q = cut(j, k); ctx.moveTo(X0 + q[0] * s, Y0 - q[1] * s); Ln(k); pen = true; }
        else pen = false;
      }
      return;
    }
    const full = () => {                // a teljes korong (120 szögű sokszög – a találat-rögzítő is érti)
      ctx.moveTo(X0 + s, Y0);
      for (let i = 1; i < 120; i++) { const a = TAU * i / 120; ctx.lineTo(X0 + Math.cos(a) * s, Y0 - Math.sin(a) * s); }
      ctx.closePath();
    };
    const lon0 = P.o.lon0, lat0 = P.o.lat0;
    if (nv === 0) { if (inRingLL(pts, n, wrap(lon0), lat0)) full(); return; }
    if (nv === n) {
      M(0); for (let i = 1; i < n; i++) Ln(i); ctx.closePath();
      if (inRingLL(pts, n, wrap(lon0 + 180), -lat0)) full();   // a belseje a hátoldalt is tartalmazza → kifordítva
      return;
    }
    let i0 = 0;
    for (let k = 0; k < n; k++) if (A[3 * ((k + n - 1) % n) + 2] < 0 && A[3 * k + 2] >= 0) { i0 = k; break; }
    const ch = [];
    let cur = null;
    for (let m = 0; m < n; m++) {
      const k = (i0 + m) % n, j = (k + n - 1) % n, zj = A[3 * j + 2], zk = A[3 * k + 2];
      if (zj < 0 && zk >= 0) { const q = cut(j, k); cur = { a0: Math.atan2(q[1], q[0]), p: [q[0], q[1], A[3 * k], A[3 * k + 1]] }; }
      else if (zj >= 0 && zk >= 0) cur.p.push(A[3 * k], A[3 * k + 1]);
      else if (zj >= 0) { const q = cut(j, k); cur.p.push(q[0], q[1]); cur.a1 = Math.atan2(q[1], q[0]); ch.push(cur); cur = null; }
    }
    const dir = ringArea(pts, n) >= 0 ? 1 : -1, used = new Uint8Array(ch.length);
    for (let c0 = 0; c0 < ch.length; c0++) {
      if (used[c0]) continue;
      let c = c0;
      ctx.moveTo(X0 + ch[c].p[0] * s, Y0 - ch[c].p[1] * s);
      for (let guard = 0; guard <= ch.length; guard++) {
        used[c] = 1;
        const p = ch[c].p;
        for (let i = 2; i < p.length; i += 2) ctx.lineTo(X0 + p[i] * s, Y0 - p[i + 1] * s);
        let best = c, bd = Infinity;
        for (let k = 0; k < ch.length; k++) {
          let d = (((dir * (ch[k].a0 - ch[c].a1)) % TAU) + TAU) % TAU;
          if (d > TAU - 1e-9) d = 0;
          if (d < bd) { bd = d; best = k; }
        }
        const m = Math.ceil(bd / (3 * D));                  // perem-ív 3°-onként
        for (let i = 1; i < m; i++) { const a = ch[c].a1 + dir * bd * i / m; ctx.lineTo(X0 + Math.cos(a) * s, Y0 - Math.sin(a) * s); }
        if (best === c0 || used[best]) break;
        c = best;
        ctx.lineTo(X0 + ch[c].p[0] * s, Y0 - ch[c].p[1] * s);
      }
      ctx.closePath();
    }
  }

  function gc(lon1, lat1, lon2, lat2, n) {
    const v = (lon, lat) => [Math.cos(lat * D) * Math.cos(lon * D), Math.cos(lat * D) * Math.sin(lon * D), Math.sin(lat * D)];
    const a = v(lon1, lat1), b = v(lon2, lat2);
    const w = Math.acos(Math.max(-1, Math.min(1, a[0] * b[0] + a[1] * b[1] + a[2] * b[2]))), out = [];
    for (let i = 0; i <= n; i++) {
      const t = i / n, s = Math.sin(w);
      const k1 = s < 1e-12 ? 1 - t : Math.sin((1 - t) * w) / s, k2 = s < 1e-12 ? t : Math.sin(t * w) / s;
      const x = k1 * a[0] + k2 * b[0], y = k1 * a[1] + k2 * b[1], z = k1 * a[2] + k2 * b[2];
      out.push([Math.atan2(y, x) / D, Math.atan2(z, Math.hypot(x, y)) / D]);
    }
    return out;
  }

  function dist(lon1, lat1, lon2, lat2) {
    const h = Math.sin((lat2 - lat1) * D / 2) ** 2 + Math.cos(lat1 * D) * Math.cos(lat2 * D) * Math.sin((lon2 - lon1) * D / 2) ** 2;
    return 2 * R_KM * Math.asin(Math.min(1, Math.sqrt(h)));
  }

  window.TortProj = { decode, unpack, lcc, ortho, equalEarth, outline, view, fit, trace, gc, dist };
})();
