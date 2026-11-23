# `shared/foldrajz/` – földrajzi adatfájlok a Földrajz 9–10. leckékhez

Offline, dupla kattintással betölthető adatfájlok (sima `<script src>`, nincs fetch). Mindet a
`tools/build_geodata.py` generálja – **kézzel ne javítsd**, a javítótáblák a szkriptben vannak.
A rajzoló modulok (FoldChoro, FoldSection, FoldChart…) nincsenek itt: azokat a leckék építik meg
(terv: `pilot/foldrajz-9-10/terv.md`, 4. fejezet). Vetületek és dekódolás: `shared/tort/proj.js`
(`TortProj`, Equal Earth is).

| fájl | globális változó | tartalom | forrás · licenc | lecke | méret |
|---|---|---|---|---|---|
| `orszagok.js` | `FOLD_ORSZAGOK` | 177 ország / terület 1:110m, ISO3, magyar név, címkepont, EU-tagság, vitatott jelölés | Natural Earth · közkincs | 11, 12, 13, 15 | ~92 KB |
| `megyek.js` | `FOLD_MEGYEK` | 19 megye + Budapest 1:10m, megyeszékhely, címkepont, országhatár | Natural Earth admin-1 · közkincs | 13 | ~24 KB |
| `idozonak.js` | `FOLD_IDOZONAK` | időzónák (normálidő, perc) + 103 javító sokszög a mai állapothoz | Natural Earth + IANA tz · közkincs | 01 | ~142 KB |
| `lemezhatarok.js` | `FOLD_LEMEZHATAROK` | lemezhatárok 4 típusban, sebességminták, 52 lemez (a tanterv 9 nagy lemeze jelölve) | PB2002 (Bird 2003) · **ODC-BY 1.0** | 02, 03 | ~120 KB |
| `rengesek.js` | `FOLD_RENGESEK` | 6992 földrengés, M ≥ 6,0, 1975–2024: dátum, hely, mélység, magnitúdó | USGS ComCat · közkincs | 02, 03 | ~135 KB |
| `vulkanok.js` | `FOLD_VULKANOK` | 1603 holocén vulkán: hely, magasság, típus, utolsó kitörés, név | NOAA NCEI · közkincs | 02, 03 | ~49 KB |
| `szelveny-*.js` | `FOLD_SZELVENY[id]` | domborzati szelvények: `japan`, `andok`, `atlanti`, `himalaja`, `alfold-bukk` | NOAA ETOPO 2022 · közkincs | 02, 03, 06, 08 | 3–8 KB/db |
| `korfa-wpp2024.js` | `FOLD_KORFA` | korfák 1950–2100 (5 évente), össznépesség 3 változatban, 10 népesedési mutató évente; világ + 5 ország | ENSZ WPP 2024 · **CC BY 3.0 IGO** | 10 | ~86 KB |
| `fejlettseg-wdi.js` | `FOLD_WDI` | 9 mutató (GDP/fő PPP és USD, GNI/fő Atlas és PPP, várható élettartam, népesség, foglalkoztatás 3 szektorban), 217 ország + világ + EU, 1960–2025 | Világbank WDI · **CC BY 4.0** | 11, 13 | ~305 KB |

Összesen kb. 0,98 MB. **Nem készült el:** `aramlasok.js` (tengeráramlások – saját „vázlatos” rajz, a 09-es
lecke gyártásakor kerül a lecke `.md`-jébe koordinátákkal, hogy a tanár átnézhesse) és az opcionális
`szel-jan-jul.js` (NCEP/NCAR szélmező – csak netCDF-ben érhető el, a stdlib-es feldolgozás nem éri meg
egyetlen lépésért; a 05-ös lecke analitikus „vázlatos” áramlásmezőt rajzol).

## Közös fejléc

Minden fájl egy `/* … */` megjegyzéssel kezdődik (tartalom, forrás, verzió, licenc, URL, letöltés és
generálás napja, a mezők leírása), az objektum első kulcsai pedig mindig:

```
{ id, ver, src, lic, url, asOf, generated, …adat }
```

`id` = a fájlnév `.js` nélkül (ezzel hivatkozik a `.md` `dataset` kulcsa, terv B5), `ver` a forrás
verziója, `src` a forrásmegjelölés (ezt írja ki a lecke forrássora), `lic` a licenc, `asOf` a letöltés
napja, `generated` a generálásé. A szelvények egy névtérben vannak:
`window.FOLD_SZELVENY = window.FOLD_SZELVENY || {}; FOLD_SZELVENY['japan'] = {…}`.

## Kódolás

- **Geometria** – mint a `shared/tort/` fájlokban: egész szám = fok × `q`, `[lon, lat]` párok, lapos tömb,
  **delta-kódolva** (az első pont abszolút, a többi az előzőhöz képest). Gyűrű: zárt, az utolsó pont nem
  ismétli az elsőt, kitöltés `'evenodd'`. Dekódolás: `TortProj.decode(p, M.q)` → `Float64Array`. A hosszú
  (> 2°) élek közbülső pontokkal ki vannak töltve, hogy gömbön (ortho) se metsszék rossz helyen a peremet.
- **1D delta** – ahol a leírás „DELTA-kódolva” jelzi (pl. `FOLD_RENGESEK.day`, `FOLD_VULKANOK.lon`,
  szelvények `z`, korfa-idősorok): futó összeg.
  ```js
  const d1 = (a) => { let v = 0; return a.map((x) => (v += x)); };
  ```
- **WDI-idősor** (`FOLD_WDI.d[mutató][i]`): `null` (nincs adat) vagy `[o, v0, d1, …]` – `o` az első adatév
  indexe, utána delta-értékek, a közbeeső `null` hiányzó év (a futó összeg nem változik). Tárolt = érték × `k`.
  ```js
  function wdi(W, key, i) {           // → [érték | null] W.y0..W.y1
    const s = W.d[key][i], k = W.ind[key].k, out = new Array(W.y1 - W.y0 + 1).fill(null);
    if (!s) return out;
    let v = 0;
    for (let j = 1; j < s.length; j++) if (s[j] !== null) { v += s[j]; out[s[0] + j - 1] = v / k; }
    return out;
  }
  ```

## Fájlonként

**`orszagok.js`** – `countries: [{iso, n, en, lp: [x, y] × q, cont, eu?: 1, dis?: 1, p: [gyűrű]}]`, `q = 100`.
Az `iso` a Világbank kódjával egyezik (ISO 3166-1 alpha-3; Koszovó `XKX`), így a WDI-hez közvetlenül
kapcsolható. A Natural Earth **de facto** határait mutatja (Krím Ukrajnánál, Nyugat-Szahara külön).
Az 1:110m-ben nincs benne Málta és a legtöbb kis szigetország: ezeket a `FOLD_WDI` `map: 0, pt: [lon, lat]`
mezője jelöli (pontként rajzolhatók). **Vitatott területek** (`dis: 1`, szaggatott körvonal, `disputed`
mező indoklással): Nyugat-Szahara (ESH), Palesztina (PSE), Észak-Ciprus (CYN), Szomáliföld (SOL),
Koszovó (XKX), Tajvan (TWN), Falkland-szigetek (FLK). A Kasmír-, Aksai Chin- és hasonló határviták a
Natural Earth de facto vonalát követik, külön nincsenek jelölve – ha a lecke ilyet mutat, a `.md` jelezze.

**`megyek.js`** – `counties: [{n, iso (HU-xx), seat, nuts2 (angol régiónév), lp, p}]`, `border`, `q = 1000`.
A Natural Earth a 23 megyei jogú várost külön egységként adja; a szkript a megyéjükbe olvasztja (közös élek
elhagyásával), így 19 megye + Budapest marad, a KSH megyei adataival egyezően. **Pontosság:** 1:10m
(a határpontok kb. 2–3 km-enként) – országos tematikus térképhez elég, településszintű nagyításhoz nem.
Pest megyének két gyűrűje van (a Budapest-lyuk). Egyszerűsítés nincs, a szomszédos megyék pontosan illeszkednek.

**`idozonak.js`** – `zones: [{m (perc), n ('UTC+5:30'), places, p}]` és `fixes: [{k, nm, m, n, since, note,
dis?, p}]`, `q = 100`. **A Natural Earth időzóna-rétege 2012-es állapotú** (Oroszország akkor egész évben
„nyári” időn volt, Törökország UTC+2, Venezuela UTC−4:30…). A mai **normálidőt** a `fixes` adja: a zónák
FÖLÉ rajzolandó javító sokszögek (Natural Earth 1:50m országok, illetve 1:10m admin-1 egységek), a változás
napjával (IANA tz database). Javítva: Kazahsztán (2024: egységesen UTC+5), Törökország, Venezuela, Szudán,
Dél-Szudán, Marokkó, Nyugat-Szahara (vitatott), Namíbia, Paraguay (2024), Jordánia, Szíria, Grönland,
Norfolk-sziget, Quintana Roo, Chihuahua, Yukon, Acre, Magallanes és Oroszország 81 szubjektuma
(2014-es visszaállás, 2016-os és 2020-as regionális változások); a Krím és Szevasztopol de facto moszkvai
idővel, `dis: 1` jelöléssel. **Egyszerűsítések:** Szaha egészében UTC+9 (keleti járásai UTC+10/+11),
Grönland egészében UTC−2, Chihuahua határmenti községei (UTC−7) nincsenek külön; nyári időszámítás nincs a
rétegben. Találatvizsgálatnál (melyik zónára kattintott?) előbb a `fixes`-t nézd. A tengereken a 15°-os
tengeri zónák.

**`lemezhatarok.js`** – **Forrásmegjelölés kötelező (ODC-BY 1.0):** „Lemezhatárok: P. Bird (2003), An updated
digital model of plate boundaries, *Geochem. Geophys. Geosyst.* 4(3), 1027, doi:10.1029/2001GC000252;
GeoJSON: Hugo Ahlenius, Nordpil (github.com/fraxen/tectonicplates).” A letöltött tükör licencfájlja
(`LICENSE.md`) ODC-BY 1.0-t ír, szigorúbb feltételt nem találtunk.
- `lines: [{b, t, c, km, vd, vr, p: [vonal]}]` – lemezpáronként és típusonként. `t`: `d` szétnyíló (OSR, CRB),
  `s` alábukó (SUB), `c` ütköző / egyéb összetartó (CCB, OCB), `t` elcsúszó (OTF, CTF); `c`: a leggyakoribb
  PB2002-osztály (`classes` magyarul). `b`: a két lemez kódja; alábukásnál a PB2002 jelölése szerint `/` vagy
  `\` választja el (az irányt Bird 2003 írja le – a leckében ne ebből olvasd ki, melyik bukik alá). `vd`:
  átlagos szétnyílás mm/év (negatív = közeledés), `vr`: jobbos elcsúszás mm/év.
- `vel: {lon, lat (DELTA, × q), az, v, vaz, vd, vr, t}` – 491 mintapont kb. 500 km-enként a nyilakhoz:
  `az` a határ iránya, `v`/`vaz` a relatív sebesség (mm/év) és iránya.
- `plates: [{code, n, en, g?, lp, p}]` – 52 lemez; `g` = a kerettanterv 9 nagy lemeze közül melyikhez tartozik
  (`big9`): az Afrikai-lemez = Núbiai + Szomáliai, az Ausztrál–Indiai-lemez = Indiai + Ausztrál (a tanterv
  szerint egyben; a panel jegyezze meg, hogy a PB2002 kettéválasztja).
- Ellenőrzés: alábukó határok átlaga −53 mm/év, szétnyílók +36 mm/év (közeledés, ill. távolodás – helyes előjel).

**`rengesek.js`** – oszloponként (`n` = 6992): `day` (napok 1975-01-01 óta, DELTA), `lon`, `lat` (× 100),
`dep` (km), `mag` (× 10). Mélységi osztályok a lecke dolga (szokásos: sekély < 70 km, közepes 70–300 km,
mély > 300 km). A magnitúdó a ComCat preferált értéke, típusa vegyes (Mw, Ms, mb).

**`vulkanok.js`** – oszloponként (`n` = 1603, hosszúság szerint): `lon` (DELTA, × 100), `lat`, `el` (m, `null` =
nincs adat), `t` (típusindex a `types`-ban: rétegvulkán, pajzsvulkán, összetett vulkán, kaldera, salak- és
tufakúp, lávadóm, tenger alatti, vulkánmező, hasadékvulkán, maar, egyéb), `le` (utolsó kitörés: 1 = 1964 vagy
később … 7 = i. e., 8 = kormeghatározás nélkül, 9 = bizonytalan), `names` (angol név: Etna, Vesuvius,
St. Helens, Popocatepetl…). A NOAA-adatbázis helyei nagyrészt a Smithsonian GVP katalógusára épülnek; a GVP
saját adatát licenc-bizonytalanság miatt nem használtuk. A Csomád nincs a listán.

**`szelveny-*.js`** – `{t, axis ('lat' | 'lon'), fix, from, to, step (fok), km, n, zmin, zmax, z (DELTA, m)}`.
Az i. pont: `from + i × step` fok. A szelvények **szélességi kör (ny → k) vagy délkör (d → é) mentén**
futnak, nem főkörön (rövid szakaszon a különbség elhanyagolható). Minden pont egy `km` széles cella átlaga,
ezért a csúcsok és árkok laposabbak a valóságosnál (Everest-cella 8457 m, Japán-árok −7436 m) – a lecke a
valódi értéket a `.md`-ből írja ki. Helyek: Japán-árok é. sz. 38,3° (k. h. 128–150°), Andok d. sz. 20°
(ny. h. 80–55°), Atlanti-óceán é. sz. 30° (ny. h. 82–8°), Himalája k. h. 86,925° (é. sz. 22–40°, az Everesten
át), Alföld–Bükk k. h. 20,5° (é. sz. 46,5–48,3°). Új szelvény: a `PROFILES` táblázat a szkriptben.

**`korfa-wpp2024.js`** – helyek (`locs`): WLD világ, NGA Nigéria, IND India, CHN Kína, JPN Japán, HUN
Magyarország (az ötödik ország, Kína, saját választás: a brief négyet nevez meg). `pyr[hely].m/.f`: ezer fő × 10,
`[év-index × 21 + korcsoport]`, `years` 1950–2100 5 évente, `ages` 0–4 … 100+. 2024-től **előrejelzés**
(`estLast: 2023`). `tot[hely].med/.low/.high`: teljes népesség ezer főben, `{y0, v (DELTA)}`; a közepes
1950–2100, az alsó és felső 2024–2100. `ind[hely][kulcs]`: évenkénti mutató 1950–2100 (DELTA, × szorzó, lásd
`indMeta`): `cbr`, `cdr`, `tfr`, `lex`, `imr`, `births`, `deaths`, `mig`, `gr`, `med`. A világ nettó vándorlása
`null`. Ellenőrzés: világ 2024: 8 161 973 ezer fő, csúcs 10 289 millió (közepes); Magyarország 1954: 222,7 ezer
élveszületés.

**`fejlettseg-wdi.js`** – `countries[i]: {iso, n, en, reg, inc, eu?, map?: 0, pt?, agg?}`, `d[mutató][i]`,
`ind[mutató]: {code, n, u, k, upd}`, `regions`, `income` (magyarul). Az `inc` a letöltéskori jövedelmi
besorolás (évente változik, `.md`-ben évvel). A GDP/fő PPP csak 1990-től, a foglalkoztatás 1991-től van;
1960–1989-re csak a folyó áras USD-mutatók. **Feltűnő forrásérték:** a Közép-afrikai Köztársaság várható
élettartama 2019-ben 31,5, 2022-ben 18,8 év (a WPP 2024 válságbecslése, a WDI is ezt közli) – buborékdiagramon
kiugrik; a lecke ne ezt az évet válassza kiemelésnek, vagy jelezze.

## Forrás, licenc, újragenerálás

| forrás | mappa (`sources/foldrajz/`) | licenc | megjelölés a leckében |
|---|---|---|---|
| Natural Earth (`nvkelso/natural-earth-vector`) | `naturalearth/` | közkincs | „Made with Natural Earth” (kérés) |
| USGS ComCat (FDSN) | `usgs/` | közkincs (USA szövetségi) | „USGS ComCat” |
| NOAA NCEI Volcano Locations | `noaavolc/` | közkincs (USA szövetségi) | „NOAA NCEI / WDS” |
| PB2002 (Bird 2003), `fraxen/tectonicplates` | `pb2002/` | **ODC-BY 1.0** | **kötelező**, lásd fent |
| NOAA ETOPO 2022 (ERDDAP: coastwatch.pfeg.noaa.gov) | `etopo/` | közkincs | „NOAA ETOPO 2022” |
| ENSZ World Population Prospects 2024 | `wpp2024/` | **CC BY 3.0 IGO** | **kötelező**: „ENSZ WPP 2024” |
| Világbank WDI (API v2) | `worldbank/` | **CC BY 4.0** | **kötelező**: „Világbank, WDI” |

A nyers fájlok `.gitignore`-on vannak; a mappánkénti `manifest.json` (URL, méret, SHA-256, letöltés napja,
licenc) a repóba kerül. A letöltött fájlok megbízhatatlan bemenetek: a szkript `-I` kapcsolóval fut, nem a
`sources/` alatt van, és csak JSON-t / CSV-t (gzip) olvas.

```bash
python3 -I tools/build_geodata.py --download            # minden forrás (kb. 150 MB, a WPP és a NE admin-1 a nagy)
python3 -I tools/build_geodata.py --download usgs etopo  # csak ezek
python3 -I tools/build_geodata.py                        # minden shared/foldrajz/*.js újragenerálása
python3 -I tools/build_geodata.py korfa wdi              # csak ezek (orszagok megyek idozonak lemezhatarok
                                                         #  rengesek vulkanok szelveny korfa wdi)
```

Az ETOPO-letöltés az ERD ERDDAP-szerverét kérdezi (gyakori a 503 „temporary problem” – a szkript
háromszor próbálkozik, utána az ETOPO1-re (PacIOOS ERDDAP) vált, és ezt a manifest és a fejléc `ver` mezője
rögzíti). Frissítéskor (új WDI- vagy WPP-kiadás) a `ver`/`asOf` változik: nézd át a leckék `.md`-jének
`dataset` sorát és a „frissítendő” jelölésű számokat.
