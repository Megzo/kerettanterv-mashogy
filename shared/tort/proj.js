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
   TortProj.view(proj, {lon, lat, s, x, y})
                               képernyő-leképezés: a (lon, lat) pont a képernyő (x, y) pontjára esik, s = px / Föld-sugár.
                               → {pt(lon, lat) → [sx, sy, látható], inv(sx, sy) → [lon, lat], kmPx: px/km, …}
                               Kameramozgás: két view-paraméter között interpolálj (lon, lat lineárisan, s logaritmikusan).
   TortProj.fit(proj, [lonMin, latMin, lonMax, latMax], [x, y, w, h], pad?)
                               → {lon, lat, s, x, y}: a view-paraméter, amellyel a fokos téglalap kitölti a képernyő-téglalapot.
   TortProj.trace(ctx, V, pts, {close, edge, ortho})
                               moveTo/lineTo útvonal (beginPath/fill/stroke a hívóé). close: gyűrű.
                               edge: [lonMin, latMin, lonMax, latMax] – az erre a keretre eső (vágásból származó) éleket
                               kihagyja → partvonal-körvonalhoz. ortho: 'fill' (a hátoldali pontok a gömb peremére
                               kerülnek; a teljesen hátoldali gyűrű kimarad) vagy 'stroke' (a hátoldali szakaszok
                               kimaradnak). Gömbön a kitöltés közelítő: a peremen átnyúló kontinens széle a perem mentén
                               fut – kivetítve jól néz ki, de ne számolj vele területet.
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

  function view(proj, v) {
    const c = proj.fwd(v.lon, v.lat), s = v.s, X = v.x, Y = v.y;
    const out = [0, 0, true];
    return {
      proj, lon: v.lon, lat: v.lat, s, x: X, y: Y, kmPx: s / R_KM,
      pt(lon, lat) {
        const p = proj.fwd(lon, lat);
        out[0] = X + (p[0] - c[0]) * s; out[1] = Y - (p[1] - c[1]) * s; out[2] = p.length < 3 || p[2] >= 0;
        return out;                       // FIGYELEM: ugyanaz a tömb minden hívásnál – másold, ha eltárolod
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

  function trace(ctx, V, pts, o) {
    o = o || {};
    const e = o.edge, eps = 1e-6, n = pts.length / 2, ort = V.proj.kind === 'ortho' && o.ortho;
    const onEdge = (ax, ay, bx, by) => e && ((Math.abs(ax - bx) < eps && (Math.abs(ax - e[0]) < eps || Math.abs(ax - e[2]) < eps)) ||
                                             (Math.abs(ay - by) < eps && (Math.abs(ay - e[1]) < eps || Math.abs(ay - e[3]) < eps)));
    if (ort) {                 // teljesen a hátoldalon lévő gyűrű kimarad (különben a peremre vetítve az egész korongot kitöltené)
      let any = false;
      for (let i = 0; i < n && !any; i++) any = V.pt(pts[2 * i], pts[2 * i + 1])[2];
      if (!any) return;
    }
    let pen = false;
    const last = o.close ? n : n - 1;
    for (let i = 0; i <= last; i++) {
      const k = (i % n) * 2, lon = pts[k], lat = pts[k + 1];
      let p = V.pt(lon, lat);
      if (ort && !p[2]) {
        if (ort === 'stroke') { pen = false; continue; }
        const dx = p[0] - V.x, dy = p[1] - V.y, r = Math.hypot(dx, dy) || 1;   // a perem a látható és a hátoldal határa
        p = [V.x + dx / r * V.s, V.y + dy / r * V.s];
      }
      if (i > 0 && e) {
        const j = ((i - 1) % n) * 2;
        if (onEdge(pts[j], pts[j + 1], lon, lat)) pen = false;
      }
      if (!pen || (o.close && i === 0)) { ctx.moveTo(p[0], p[1]); pen = true; } else ctx.lineTo(p[0], p[1]);
    }
    if (o.close && !e && !ort) ctx.closePath();
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

  window.TortProj = { decode, unpack, lcc, ortho, view, fit, trace, gc, dist };
})();
