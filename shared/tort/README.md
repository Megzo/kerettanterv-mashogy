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
| `proj.js` | `TortProj` | – | vetületek, dekódolás, útvonal-rajzolás | ~10 KB |

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

## Vetület-segéd (`proj.js`)

A teljes API a fájl tetején. Röviden: `lcc({lon0, lat0, lat1, lat2})` Lambert-féle szögtartó
kúpvetület, `ortho({lon0, lat0})` ortografikus gömb; `view(proj, {lon, lat, s, x, y})`
képernyőre képez (s = px / Föld-sugár; kamera-animációhoz két view-paraméter között
interpolálj, `s`-t logaritmikusan), `fit(proj, bbox, rect)` kitöltő nézetet számol,
`trace(ctx, V, pts, opts)` útvonalat rajzol, `gc()` főkör, `dist()` km.

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
const buda = V.pt(19.04, 47.50);                                       // [x, y, látható] – másold, ha eltárolod
</script>
```

Gömbön (`ortho`) a kitöltéshez `{close: true, ortho: 'fill'}`, a körvonalhoz `{ortho: 'stroke'}`;
előtte rajzold meg a korongot (`ctx.arc(V.x, V.y, V.s, …)`). Teljesítmény: a teljes
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
