# `shared/tort/` – közös térképadat a történelemleckékhez

Offline, dupla kattintással betölthető adatfájlok (sima `<script src>`, nincs fetch) és egy kis
vetület-segéd. **A térképmotor (kamera, rétegek, címkézés, nyilak) nincs itt**: azt az első
térképes lecke építi meg leckén belül, és csak átnézés után kerül ide (`leckek/SZERZODES.md`,
Történelem-kiegészítés).

| fájl | globális változó | kivágat | forrás | méret |
|---|---|---|---|---|
| `map-karpat.js` | `TORT_MAP_KARPAT` | 9–30° K, 42–51° É | NE 1:10m + európai kiegészítő folyók/tavak, q = 1000 | ~86 KB |
| `map-mediterran.js` | `TORT_MAP_MEDITERRAN` | 10° Ny – 50° K, 20–56° É | NE 1:50m (tájnevek 1:10m), q = 100 | ~49 KB |
| `map-vilag.js` | `TORT_MAP_VILAG` | az egész Föld | NE 1:110m szárazföld + nagy tavak, q = 100 | ~39 KB |
| `map-orszaghatarok.js` | `TORT_MAP_HATAROK` | 12° Ny – 50° K, 20–60° É | NE 1:50m mai szárazföldi országhatárok, q = 100 | ~16 KB |
| `map-europa.js` | `TORT_MAP_EUROPA` | 25° Ny – 60° K, 30–72° É | NE 1:50m szárazföld, tavak, folyók, q = 100 (`tools/build_tortmap.py`) | ~67 KB |
| `map-torthatar.js` | `TORT_HATAR` | Európa + volt SZU, É. Afrika, Közel-Kelet (25° Ny – 180° K, 30–82° É) | **történeti határok**, vázlatos: NE 1:10m admin-1 + kézi vágás, topologikus ívek, q = 1000 | ~380 KB |
| `proj.js` | `TortProj` | – | vetületek (Lambert, ortografikus, Equal Earth), dekódolás, útvonal-rajzolás | ~14 KB |

## Formátum

Minden koordináta **egész szám = fok × q** (a `q` a fájlban van), `[hosszúság, szélesség]`
sorrendben, keletre és északra pozitív. Egy vonal vagy gyűrű lapos tömb, **delta-kódolva**:
`[x0, y0, dx1, dy1, dx2, dy2, …]` – az első pont abszolút, a többi az előzőhöz képest.
Gyűrű: zárt (az utolsó pont nem ismétli az elsőt), kitöltés `'evenodd'` szabállyal (a tavak és
a Kaszpi-tenger lyukak). Dekódolás: `TortProj.unpack(M)` → fokos `Float64Array`-ek.

```
{ name, q, bbox: [x0, y0, x1, y1] (× q), scale: '10m' | '50m' | '110m',
  land:    [gyűrű],                                 // szárazföld, a kivágatra vágva
  lakes:   [{n, en?, modern?: 1, p: [gyűrű]}],     // n: magyar név (Natural Earth name_hu), '' = névtelen
  rivers:  [{n, en?, r, modern?: 1, lc?: 1, p: [vonal]}],
  regions: [{n, en, t, r, c: [x, y], p: [gyűrű]}],  // tájak, hegységek (durva foltok!)
  lines:   [vonal] }                                // csak map-orszaghatarok.js
```

- `rivers[].n` magyar név (a `tools/build_mapdata.py` táblázatából; ami nincs benne, annak a
  Natural Earth `name_hu` / angol neve). `r`: Natural Earth rang, kisebb = fontosabb (vonalvastagsághoz,
  szűréshez). Egy folyó több tételben is lehet (pl. a Nílus az Asszuáni-gát tava alatt és fölött).
- `lc: 1` – a folyó középvonala egy tavon át (Nílus a Nasszer-tavon, Zala–Sió a Balatonon). Csak
  akkor rajzold, ha a tavat nem.
- `modern: 1` – mai mű: víztározó (Nasszer-tó, Tisza-tó, dnyeperi tározók), csatorna
  (Szuezi-, Ferenc-csatorna). Ókori/középkori térképen hagyd el, és a tó helyén rajzold a folyót.
- A folyók és partok a **mai** állapotot mutatják. A szabályozás előtti Tisza, a mocsarak
  (Sárrét, Ecsedi-láp, Hanság) nincsenek benne – ahol számít, a lecke rajzol „vázlatos” réteget
  (terv.md 4. fejezet, 13. pont).
- `regions[]`: Natural Earth „geography regions” – kézzel rajzolt, **durva** foltok (a Kárpátok
  folt az Erdélyi-medencét is lefedi). Névcímkéhez (`c`: belső címkepont) és halvány árnyaláshoz
  jó, domborzatnak nem. A Mátra, Bükk, Bakony stb. nincs benne: azt a lecke `.md`-je adja meg
  koordinátával. `t`: `Range/mtn`, `Plain`, `Plateau`, `Delta`, `Desert`, `Pen/cape`, `Geoarea`, `Lowland`.
- A kivágat szélére eső élek a vágásból jönnek: körvonalnál hagyd ki őket (`trace` `edge` opció).
- `map-orszaghatarok.js` **mai** határ: csak halvány, kikapcsolható, „mai határok” feliratú
  tájékozódási réteg lehet. Történeti határ soha.

## Történeti határok (`map-torthatar.js`, `window.TORT_HATAR`)

**Minden csoport vázlatos.** A Natural Earth 1:10m mai közigazgatási egységeiből (megye, kerület, tartomány,
vajdaság) épül; ahol egy történeti határ mai egységen fut át, ott kézi vágóvonal osztja ketté
(`tools/build_tortmap.py`, `CUTS` – minden töréspont mellett a helységnév, melyik oldalra került). A `notes[csoport]`
mondja meg, miben tér el a valóságtól; a lecke **ezt a jelleget közölje** (pl. „vázlatos határ” felirat a
forrássávban). A területet és a népességet a lecke a `.md` `### Adatok` részéből mutassa, **soha ne a sokszögből**
(a `qa` mező csak ellenőrzés).

```
{ id: 'torthatar', q: 1000, ver, src, lic, url, asOf, generated, vazlatos: true,
  bbox:  [x0, y0, x1, y1] (× q)               // a kivágat; az erre eső ívek vágásból jönnek, nem határok
  arcs:  [lapos delta-tömb]                    // közös ívek: [x0, y0, dx1, dy1, …] (fok × q)
  units: [{id, n, cc, set: 'karpat'|'europa', c: [lon, lat], r: [[ívhivatkozás, …], …]}],
  groups: {kulcs: [egység-id, …] | {alkulcs: [egység-id, …]}},
  points: {fiume: [lon, lat], …},             // pontként kezelt helyek (Fiume corpus separatum, Danzig, Berlin …)
  notes:  {csoport: 'vázlatos: …'},
  qa:     {'csoport' | 'csoport.alkulcs': [számolt km², közismert km² | null, eltérés % | null]} }
```

- **Ívhivatkozás:** `i ≥ 0` → `arcs[i]` előre, `i < 0` → `arcs[~i]` (= `arcs[−i−1]`) visszafelé. Egy gyűrű az ívek
  egymás utáni összefűzése; minden következő ív első pontja azonos az előző utolsójával (elhagyandó), a gyűrű zárt.
- **Körüljárás:** külső gyűrű az óramutatóval ellentétes (a lon/lat síkon), lyuk (Budapest Pest megyében, Berlin
  Brandenburgban, Minszk …) azzal egyező → kitöltés **`'nonzero'`** szabállyal. Egy csoport összes egységét **egy
  útvonalban** töltsd ki: a szomszédos egységek ugyanazt az ívet használják, ezért nincs rés és nincs csík a varraton.
- **Csoport körvonala:** a csoporton belül pontosan egyszer használt ívek (a kétszer használtak belső határok).
  A `bbox`-ra eső ívek (Oroszország keleti, Afrika és a Közel-Kelet déli vágóéle) nem határok: `trace(…, {edge})`.
- **Egységek:** `set: 'karpat'` – HU (20 megye, a megyei jogú városok a megyében), SK, RO, RS, HR, SI, AT,
  Kárpátalja: 0,0016° tűréssel, megyetérképhez is jó. `set: 'europa'` – a többi ország egyesítve, külön egység csak
  ott, ahol történeti határ fut (pl. `PL-SL.a`, `BY-MI.pl`, `CZ-JM.sd`, `LT-KL`): 0,018° tűrés, **kontinens-léptékre**
  (Kárpát-medencei közelképen a lengyel/ukrán határ szögletes). Berlin finomabb (a szektorhatár közelképhez).
  `n`: magyar név, `cc`: mai ország (ISO 3166-1), `c`: címkepont. A vágott darabok azonosítója `<mai egység>.<jel>`.
- A partvonal az admin-1 adatból jön: `map-europa.js` / `map-karpat.js` szárazföldje fölé rajzolva kis eltérés
  lehet a parton – kontinens-léptéken nem látszik; közelképen a csoportot a szárazföldre vágd (`ctx.clip()`), vagy
  rajzold a csoportot partvonalnak.

Referencia-dekóder (a próbaoldal ezzel rajzolt):

```js
const H = window.TORT_HATAR, P = TortProj;
const ARCS = H.arcs.map(a => P.decode(a, H.q)), U = {};
for (const u of H.units) U[u.id] = u;
function ring(refs) {                                   // ívhivatkozások → Float64Array [lon, lat, …]
  const out = [];
  for (const r of refs) {
    const a = ARCS[r >= 0 ? r : ~r], n = a.length / 2;
    for (let k = out.length ? 1 : 0; k < n; k++) { const i = r >= 0 ? k : n - 1 - k; out.push(a[2 * i], a[2 * i + 1]); }
  }
  if (out.length > 4 && out[0] === out[out.length - 2] && out[1] === out[out.length - 1]) out.length -= 2;
  return Float64Array.from(out);
}
const RINGS = {}; for (const u of H.units) RINGS[u.id] = u.r.map(ring);         // egyszer, init-ben
function fillGroup(c, V, ids) {                          // ids: H.groups.mo1920 vagy H.groups.eu1914.DE
  c.beginPath(); for (const id of ids) for (const r of RINGS[id]) P.trace(c, V, r, { close: true });
  c.fill('nonzero');
}
function strokeGroup(c, V, ids) {                        // körvonal: a csoportban egyszer használt ívek
  const cnt = new Map();
  for (const id of ids) for (const rr of U[id].r) for (const r of rr) { const a = r >= 0 ? r : ~r; cnt.set(a, (cnt.get(a) || 0) + 1); }
  c.beginPath(); for (const [a, n] of cnt) if (n === 1) P.trace(c, V, ARCS[a], { edge: H.bbox.map(v => v / H.q) });
  c.stroke();
}
```

(A 07-es lecke `TortTerr` modulja erre épül; ha elkészül, azt használd.)

### Csoportkulcsok

| kulcs | tartalom |
|---|---|
| `mo1914`, `hsz1914`, `mo1914hsz` | Magyar Királyság 1914 Horvát-Szlavónország nélkül / Horvát-Szlavónország / a kettő együtt |
| `mo1920`, `mo1938`, `mo1939`, `mo1940`, `mo1941`, `mo1947` | az ország területe az adott évben (1920 = a pozsonyi hídfővel; 1947 = mai) |
| `felvidek`, `karpatalja`, `erdely`, `delvidek`, `orvidek`, `arva-szepes` | az 1920-ban elcsatolt részek (mai egységekből) |
| `trianon1920` | `HU, CS, RO, SHS, AT, PL` – a megosztás egy térképen (Fiume pont: `points.fiume`) |
| `bd1`, `karpatalja1939`, `szlovakia1939`, `bd2`, `delvidek1941`, `pozsonyi-hidfo1947` | a revízió lépései és az 1947-es hídfő |
| `zonak1944` | `I, II, III, IV, V, VI, BP` (+ `I-II`, `V-VI`) – a deportálási zónák, vázlatos |
| `eu1914` | Európa 1914: `DE, AH-AT, AH-HU, AH-BH, RU, FR, UK, IT, RO, BG, SRB, MNE, GR, OT` (Oszmán Bir.), `PE`, `AR` … + gyarmatok (`FR-gyarmat` …); **összesítő / részhalmaz** kulcsok: `AH` (= AH-AT + AH-HU + AH-BH), `RU-FI`, `RU-PL` (az `RU` részei) |
| `de1871` | = `eu1914.DE` (Német Császárság) |
| `eu1923` | Európa 1923–37: `DE, SAAR, DANZIG, PL, CS, AT, HU, RO, YU, IT, SU, LT, …` + mandátumok |
| `eu1938` | építőkockák 1938–39-re: `DE1937, AT, SUDETEN, ZAOLZIE, CS-1938, PROTEKTORATUS, SK1939, MEMEL, DANZIG, AL, PL, HU-1938, BD1, KARPATALJA1939` (átfedők: rétegenként rajzold) |
| `eu1942` | 1942. november, annektált / közigazgatási állapot: `DE, DE-PROT, DE-GG, FR-AL, SK, HU, RO, RO-TRANSZNISZTRIA, BG, IT, NDH, SRB, GR, FR, FR-occ, FR-COR, SU, FI, …` (a frontvonal nem egységhatár – a lecke rajzolja) |
| `eu1949`, `eu1989` | `NSZK, NDK, SAAR` (csak 1949), `Berlin-Ny, Berlin-K, Berlin-US, Berlin-GB, Berlin-FR, PL, CS, HU, SU, YU, …` (a Berlin-szektorok a `Berlin-Ny` részei) |
| `szu1991` | a 15 utódállam: `RU, UA, BY, MD, LT, LV, EE, GE, AM, AZ, KZ, UZ, TM, KG, TJ` |
| `mai0` | **mai** országok (ISO-kód szerint) – csak tájékozódás, történeti határ soha |
| `mai1` | **mai** megyék / körzetek a Kárpát-medencében, a vágott darabjaikkal (14. lecke) |

A teljes térképek (`eu1914`, `eu1923`, `eu1942`, `eu1949`, `eu1989`) az összesítő kulcsok nélkül minden egységet
pontosan egyszer fednek le (a build ellenőrzi). Ami nem állam (gyarmat, mandátum), azt a kulcs neve jelzi.

### Ismert pontatlanságok (a `notes` mező részletesen)

- A határ mai egységhatáron fut, ahol a mai egység és a történeti határ egybeesik – ez sokszor csak közelítés:
  Erdély = 16 mai megye (Orsova környéke hiányzik), Vajdaság-körzetek a Bácska–Bánságra, a Szerémség része a
  Belgrádhoz tartozó Zimony nélkül, Horvátország dalmát megyéi, a Saar-vidék 1920-as északi határa, Litvánia
  Vilnius-vidéke (= mai Vilnius megye), Besszarábia (= Moldova + Budzsák).
- Kézi vágóvonalak (vázlatos, helységnevek közé húzva): bécsi döntések (`bd1` +9 %, mert a falusor nem
  rekonstruálható), kelet-szlovákiai sáv 1939, pozsonyi hídfő, árvai és szepesi falvak, baranyai háromszög (Dráva),
  Szerémség (Duna), Tisza (az Észak-bánsági körzet nyugati része – Magyarkanizsa, Zenta, Ada – a Bácskához),
  német–orosz és osztrák–orosz határ 1914, lengyel korridor és Felső-Szilézia 1922, Danzig, Kelet-Poroszország,
  rigai határ 1921, Szudéta-vidék, Zaolzie, francia demarkációs vonal 1940, Észak-Schleswig, Memel-vidék,
  Budzsák, Nesztosz (Nyugat-Trákia), Saar 1920, Berlin szektorai.
- `zonak1944`: megyékből összerakva; Sopron (V. zóna) Győr-Moson-Sopronban, Sátoraljaújhely (I.) Borsodban maradt –
  **történész ellenőrizze**. A Bánság 1941-ben német katonai közigazgatás – nincs a `delvidek1941`-ben.
- Nem szerepel: Eupen-Malmedy, Hlučín-vidék, Petsamo, Karéliai-földszoros (külön), a trieszti szabad terület, Görögország
  megszállási zónái, a szovjet front – ezeket a lecke vázlatos réteggel rajzolja, ha kell.

### Terület-ellenőrzés (gömbi terület a végleges, egyszerűsített sokszögből)

| csoport | számolt km² | közismert km² | eltérés |
|---|---:|---:|---:|
| `mo1914hsz` | 318 379 | 325 411 | −2,2 % |
| `mo1914` | 278 963 | 282 870 | −1,4 % |
| `hsz1914` | 39 417 | 42 541 | −7,3 % |
| `mo1920` (hídfővel) | 93 019 | 92 952 | +0,1 % |
| `mo1947` | 92 951 | 93 030 | −0,1 % |
| `trianon1920.CS` | 61 174 | 61 646 | −0,8 % |
| `trianon1920.RO` = `erdely` | 100 204 | 102 813 | −2,5 % |
| `trianon1920.SHS` (Horvátországgal) | 59 389 | 63 370 | −6,3 % |
| `delvidek` (Horvátország nélkül) | 19 973 | 20 829 | −4,1 % |
| `trianon1920.AT` = `orvidek` | 3 971 | 4 020 | −1,2 % |
| `trianon1920.PL` = `arva-szepes` | 622 | 589 | +5,5 % |
| `bd1` | 13 054 | 11 927 | +9,4 % |
| `karpatalja1939` | 11 262 | 12 061 | −6,6 % |
| `szlovakia1939` | 1 589 | 1 697 | −6,4 % |
| `bd2` | 42 955 | 43 104 | −0,3 % |
| `delvidek1941` | 11 490 | 11 475 | +0,1 % |
| `mo1941` | 173 368 | 171 753 | +0,9 % |
| `pozsonyi-hidfo1947` | 68 | 65 | +4,8 % |
| `eu1914.DE` / `AH` / `FR` / `IT` | 539 838 / 680 410 / 532 377 / 289 345 | 540 858 / 676 615 / 536 464 / 286 682 | −0,2 / +0,6 / −0,8 / +0,9 % |
| `eu1923.PL` / `CS` / `RO` / `YU` / `AT` | 391 755 / 139 674 / 295 430 / 246 096 / 83 758 | 388 634 / 140 446 / 295 049 / 248 987 / 83 868 | +0,8 / −0,5 / +0,1 / −1,2 / −0,1 % |
| `eu1923.DANZIG` / `SAAR` | 1 878 / 1 995 | 1 966 / 1 912 | −4,5 / +4,3 % |
| `eu1938.SUDETEN` / `ZAOLZIE` / `PROTEKTORATUS` / `SK1939` / `MEMEL` | 27 590 / 806 / 50 104 / 35 270 / 2 824 | 28 680 / 869 / 49 363 / 38 055 / 2 848 | −3,8 / −7,3 / +1,5 / −7,3 / −0,9 % |
| `eu1949.NSZK` / `NDK` / `Berlin-Ny` / `Berlin-K` | 244 816 / 107 630 / 482 / 404 | 245 300 / 107 900 / 480 / 403 | −0,2 / −0,3 / +0,5 / +0,2 % |

Közismert értékek: KSH (1910, 1920, 1941), a döntések korabeli adatai (hu.wikipedia: Első / Második bécsi döntés,
Magyar–szlovák kis háború: 1 697 km², 78 település), az európai államokra a kerekített lexikoni adatok. Minden
eltérés 10 % alatt; a teljes lista (`eu1914.RO`, `BG`, `SRB`, `GR` …) a `qa` mezőben és a build kimenetén.

## Vetület-segéd (`proj.js`)

A teljes API a fájl tetején. Röviden: `lcc({lon0, lat0, lat1, lat2})` Lambert-féle szögtartó
kúpvetület, `ortho({lon0, lat0})` ortografikus gömb, `equalEarth({lon0})` egyenlő területű világvetület,
`outline(ctx, V)` a vetület körvonala (gömbkorong / Equal Earth-perem); `view(proj, {lon, lat, s, x, y})`
képernyőre képez (s = px / Föld-sugár; kamera-animációhoz két view-paraméter között
interpolálj, `s`-t logaritmikusan), `fit(proj, bbox, rect)` kitöltő nézetet számol,
`trace(ctx, V, pts, opts)` útvonalat rajzol, `gc()` főkör, `dist()` km.

**Equal Earth** (`equalEarth({lon0})`, egyenlő területű világvetület – tematikus térképhez, ahol a terület
számít; a földrajzi adatok: `shared/foldrajz/`). A teljes világ kitöltő nézete:
`fit(proj, [lon0 − 180, −90, lon0 + 180, 90], rect)` (a bbox a középmeridiánhoz igazodjon). A térkép széle a
`lon0 ± 180°` délkör: a `trace` a varraton átnyúló gyűrűt mindkét oldalon megrajzolja, ezért rajzolás előtt
vágj a térkép körvonalára (`outline`); a nyitott vonalat a varratnál megszakítja. Az `edge` opcióval hívott
`trace` a régi (varrat-kezelés nélküli) úton fut.

```js
const pr = P.equalEarth({ lon0: 10 }), V = P.view(pr, P.fit(pr, [-170, -90, 190, 90], [20, 40, 1320, 1000]));
c.save(); c.beginPath(); P.outline(c, V); c.fillStyle = '#dbe9f3'; c.fill(); c.clip();   // óceán + vágás
for (const k of FOLD_ORSZAGOK.countries) { c.beginPath(); for (const r of k.p) P.trace(c, V, P.decode(r, 100), { close: true }); c.fill('evenodd'); }
c.restore();
```

`outline(ctx, V)` gömbön (`ortho`) a korong útvonala. Visszafelé kompatibilis bővítés: a meglévő vetületek
és a `trace` viselkedése nem változott.

Ajánlott paraméterek: Kárpát-medence `{lon0: 19.5, lat0: 47, lat1: 45, lat2: 49}`; Földközi-tenger
`{lon0: 20, lat0: 38, lat1: 30, lat2: 46}`; Egyiptom `{lon0: 31, lat0: 27, lat1: 23, lat2: 31}`.

```html
<script src="../../shared/tort/proj.js"></script>
<script src="../../shared/tort/map-karpat.js"></script>
<script>
const P = TortProj, M = P.unpack(window.TORT_MAP_KARPAT);           // egyszer, init-ben
const proj = P.lcc({ lon0: 19.5, lat0: 47, lat1: 45, lat2: 49 });
const V = P.view(proj, P.fit(proj, [15.5, 44.5, 25.5, 49.5], [40, 40, 1280, 1000]));
c.beginPath(); for (const r of M.land) P.trace(c, V, r, { close: true });
c.fillStyle = '#f3ead8'; c.fill('evenodd');                          // szárazföld
c.beginPath(); for (const r of M.land) P.trace(c, V, r, { close: true, edge: M.bbox });
c.strokeStyle = '#1b5a94'; c.lineWidth = 2; c.stroke();                // partvonal (a vágóél nélkül)
for (const f of M.rivers) if (!f.lc && !f.modern && f.r <= 8) {
  c.beginPath(); for (const l of f.p) P.trace(c, V, l);
  c.lineWidth = f.r <= 2 ? 3 : 1.8; c.stroke();
}
const buda = V.pt(19.04, 47.50);                                       // [x, y, látható] – friss tömb (v1.1), eltárolható
</script>
```

Gömbön (`ortho`) a kitöltéshez `{close: true, ortho: 'fill'}`, a körvonalhoz `{ortho: 'stroke'}`;
előtte rajzold meg a korongot (`P.outline(ctx, V)` vagy `ctx.arc(V.cx, V.cy, V.s, …)`). A `'fill'` (v1.1, 2026-11-24 óta)
valódi horizontvágás: a gyűrűt a látható félgömbre vágja, és a perem mentén ívvel zárja (mint a d3-geo `clipCircle`),
így a horizonton átnyúló nagy sokszögek (időzónasávok, Antarktisz) sem festenek hamis csíkot, és a kimenet
páros–páratlan találatvizsgálatra is jó. A `'stroke'` a peremet átlépő szakaszt a peremig húzza. Teljesítmény: a teljes
`map-karpat.js` (kb. 12 ezer pont) képkockánkénti újravetítése néhány ms; ha kamera nem mozog,
rajzold egyszer egy háttér-vászonra.

## Forrás, licenc, újragenerálás

**Natural Earth** (naturalearthdata.com), a hivatalos GitHub-tükörből (`nvkelso/natural-earth-vector`,
`geojson/`). **Közkincs (public domain)**; a „Made with Natural Earth” feltüntetése kérés, nem
kötelezettség – a leckék stáblistájában / `.md` megjegyzésében érdemes. A letöltött fájlok URL-je,
mérete, SHA-256-ja és dátuma: `sources/naturalearth/manifest.json` (maguk a GeoJSON-ok
`.gitignore`-on vannak).

```bash
python3 -I tools/build_mapdata.py --download   # forrás letöltése + manifest.json
python3 -I tools/build_mapdata.py              # shared/tort/map-*.js újragenerálása
```

A magyar folyónevek, a névtelen szakaszok azonosítása és a „mai mű” jelölés a szkript elején,
táblázatban van – ott javítsd, ne a generált fájlban.

`map-europa.js` és `map-torthatar.js`: `tools/build_tortmap.py` (csak standard könyvtár; a geometria-segédeket a
`build_mapdata.py`-ból veszi). Forrás: a fenti Natural Earth-fájlok + `ne_10m_admin_1_states_provinces`
(`sources/foldrajz/naturalearth/manifest.json`). A szkript `--download` kapcsolója a hiányzó fájlokat a manifestben
rögzített URL-ről tölti le, és SHA-256-tal ellenőrzi. A kézi vágóvonalak saját rekonstrukciók (a döntések,
szerződések szövegében megnevezett települések és folyók alapján) – **saját munka**; javítani a
`CUTS` táblázatban kell, majd újragenerálni.

```bash
python3 -I tools/build_tortmap.py --download   # hiányzó forrás letöltése (a manifest szerint)
python3 -I tools/build_tortmap.py              # shared/tort/map-europa.js + map-torthatar.js (a területtáblát kiírja)
```
