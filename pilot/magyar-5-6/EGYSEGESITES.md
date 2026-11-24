# Magyar 5–6. – modul-egységesítő és javítókör (2026-11-24)

A sorozat 17 leckéjének közös moduljait (MagText, MagMorph, MagVers, MagHang, MagStory) egyeztettük:
minden példány bájtra azonos (md5 a blokk `/* ── MODUL: … ── */` sorától a `/* ── MODUL VÉGE ── */` sor végéig).

## Javítások

### 1. MagText v1.1 – `T.layout` sorszélesség: `maxW`

**Hiba (v1.0):** a `T.layout(tokens, o)` az `o.w`-t egyszerre vette sorszélességnek (`maxW = o.w`) és
betűvastagságnak (`fo(o)` → `w: o.w`). 1000 fölött (`w: 1260`) a font érvénytelen volt (a mérés és a rajz
a korábbi fonttal futott), alatta a vastagság némán átállt (pl. `w: 380` → vékony betű).

**Javítás:** külön `maxW` kulcs a sorszélességhez; a `w` mindenhol (create, layout, tile) a betűvastagság.
A blokk teteje dokumentálja (v1.1-megjegyzés + a `T.layout` API-sora). A blokk mind a 16 MagText-et
használó leckében cserélve (a 11-janos-vitez-utja nem használja).

Átírt hívások (sorszélesség `w` → `maxW`):

| lecke | hívás | változás a képen |
|---|---|---|
| 04-toldalek | 2. lépés: szójelentések (`w: 380`), 4. lépés: mondat (`w: 1260`, érvénytelen font volt) | a jelentések a példány 500-as vastagságával (eddig 380), a mondat 560-assal |
| 05-hasonulas | 4. lépés: szereplőleírás (`w: 330`) | 500-as vastagság (eddig 330) |
| 13-pal-utcai-fiuk | `quote()` segédfüggvény (2., 4., 5., 6., 7. lépés idézetei; `w: 470…1180`), 7. lépés: kérdés (`w: 420`) | az idézetek egységesen a példány 500-as dőltjével (eddig 470–720, a 6. lépésé 1180 → érvénytelen font; ott a forrássor áthelyezve, lásd QA) |

Kerülőutak: a 07-dorlak `sent1()` megjegyzése frissítve (az egysoros mondat szándékosan nem tördel, a
`sent()` kicsinyít, ha nem fér el – ez nem kerülőút többé, hanem döntés). A 06 és a 08 `w` nélkül hív,
saját méretillesztéssel – helyes, nem kellett hozzányúlni.

### 2. MagHang v1.1 – `MagHang.hum` és `o.at`

A 01-kommunikacio leckekódjában élő dúdolás (szótagonként egy zümmögő hang `setTimeout`-tal ütemezve) a
modulba került:

- `MagHang.vowel(o)` / `noise(o)`: új `o.at` (mp) – késleltetett indítás az AudioContext-órán (a `path` ideje
  is ettől számít); a `stop()` a még el nem indult hangokat is leállítja. Az `o.solo` most dokumentált.
- `MagHang.hum(notes, o)` → `{ac0, perf0, T}` | null: `notes = [{t, dur, f0: Hz | [Hz, …], vol}]` (tömb =
  egyenletes csúszás a hang hosszán), alap hangszín `[300, 950, 2350]` Hz. Előbb `stop()`-ot hív.
  `setTimeout` nélkül, pontosan beütemezve.
- A 01 `hum()` most a dallamból jegyzetlistát épít és `MagHang.hum`-ot hív; a `TIMERS` és a `HUMF` megszűnt.
  A kurzor továbbra is `L.st`-ből fut (hang nélkül is).
- Próba (Playwright, oszcillátor-indítás figyelése): a 3. lépés „Dúdold el!” gombja 5 szótagot ütemez
  0,02 / 0,29 / 0,56 / 0,83 / 1,10 mp-re (DS = 0,27), a 6. lépés dúdolása is szól; 0 konzolhiba.

A bővített blokk mind az 5 MagHang-leckében cserélve (01, 02, 03, 05, 10); a többi API változatlan.

### 3. 11-janos-vitez-utja – helynevek halója (4. lépés, valóság-térkép)

A helynév-feliratok (Varsó, Tatárország, a falu, Itália (Róma), Franciaország/Párizs, India/Delhi) átfedték a
szaggatott útvonalat. A lecke `stationLabels()`-e most `haloTx()`-szel ír: papírszínű körvonal
(`rgba(250,245,234,.92)`, a betűméret 0,4-szerese) a név és az alcím mögött. A lecke kódjában, a TortMap
blokkon kívül (a TortMap nem ad rá opciót). Minden térképes lépésen hat – képen ellenőrizve, a
mesetérképen is jól mutat.

## md5 (blokkonként, minden példány azonos)

| modul | verzió | md5 | leckék |
|---|---|---|---|
| MagText | v1.1 | `c526552e07c94a1bd113056cc4a8e601` | 01–10, 12–17 (16) |
| MagHang | v1.1 | `96d167766faa9b0fdbcc3aeb1dfa2c1b` | 01, 02, 03, 05, 10 |
| MagMorph | (változatlan) | `d192e6961674a0c5d40974b3d77312d3` | 04, 05, 07, 08 |
| MagVers | (változatlan) | `0df9a22a29ee2dfcb46bd739a8956ba5` | 10, 12, 14, 15, 16 |
| MagStory | (változatlan) | `28c524df467671c29665a92f7baaec18` | 09, 11, 13, 15, 17 |

## QA

Mind a 17 lecke buildelve (egyenként, figyelmeztetés nélkül) és teljes QA-val futtatva
(`--back --states --det --at 1.5,settle`, ugrópróba): **17/17 ✓ – 0 JS-hiba, 0 túlcsordulás/átfedés.**
Képen átnézve: 04 (2., 4. lépés + állapotok), 05 (5. lépés), 07 (2. lépés), 11 (minden térképes lépés és a
`valosag`/`fele-ut` állapot), 13 (2., 4., 5., 6., 7. lépés). A 01 dúdolása kattintásos Playwright-próbával.

Két QA-jelzés a futás közben, mindkettő elhárítva:
- **13-pal-utcai-fiuk, 6. lépés:** a csata-idézet (`maxW: 1180`) most a helyes fonttal mér, két sorba tördel, a
  „– VIII. fejezet” forrássor kilógott a színpad aljáról. Javítás a lecke `quote()`-jában: `srcRight` esetén a
  forrás az utolsó sor alapvonalára kerül, a sorszélesség jobb szélére (ha elfér mellette; különben alatta).
- **03-hang-betu-fonema, 5. lépés, `--at 1.5`:** „kerek forma” × „kártyaszín” átfedés – a két jelentés-pill
  szándékos áttűnése egy helyen; 4 párhuzamos QA melletti terhelésnél a kép épp az áttűnésre esett. Egyedül
  futtatva hibátlan; a 03 kódja nem változott (a MagText/MagHang-csere rá nem hat).

## Ami maradt (nem magyar modul, vagy nem egyszerű – csak leírás)

- **MagStory.slider** csak 1..n tartományt ad; a 15-toldi az Előhangot is tartalmazó 0..12 csúszkához saját
  `L.slider`-t használ. Egy `min`-opció kényelmes lenne – nem javítottam (működik, és 5 lecke újra-QA-ját
  kérné egyetlen hívásért).
- **Motor (`shared/lesson.js`):** a `U.mix` `rgb()`-t ad, ezért nem ágyazható (11: saját hex-keverő).
- **TortMap:** a `base()` a teljes vásznon tölti a tengert (11: clip előtte); feliratokhoz nincs halo-opció
  (11: leckén belüli `haloTx`).
- **TortScene:** a `markers` `labels: true` címkéi szűk keretben ütköznek a kártyával (09: `labels: false`).
- **TortTimeline:** a `cards` vezetővonalait a rajzolási sorrend dönti el, a felső sor vonala átfuthat az alsó
  kártyáján (17: sorrendcsere). **TortCards:** a tálca az elhelyezett kártya helyén lyukat hagy; csak húzásra
  reagál (05).
- **QA (`tools/`):** az opt-in `idle()` miatt a `--at 1.5` kép is a nyugalmi állapotot fotózza (09, 12).
- **Build:** a `rhyme` adathoz „kivéve” lista (14); a `rhyme` `p` tömbje a teljes idézetsor hosszú (16); egy
  „írott alak ≠ részek” morph-változat (08: lát + j + a = lássa); szöveges adattípus a szakaszokhoz (13).
- A közös leckeügynök-utasítás „MagText `T.layout` `o.w`” buktatója elavult (v1.1 óta `maxW`).
