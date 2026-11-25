# Szerződés lecke-készítőknek

Ezt a fájlt + a briefedet kapod. Minden, ami egy lecke elkészítéséhez kell, itt van.
Mintalecke: `leckek/fizika-7-8/01-suruseg.{html,md}` – nézd meg, mielőtt elkezded.

## 1. Cél és mérce

12–18 éveseknek szóló, **kivetített** (16:9, világos terem) interaktív lecke egy kerettantervi
témakörhöz. Két mérce egyszerre: legyen benne **„wow”** (meglepő kép, valódi fizikai/matematikai
modell, élő interakció), és a diák **tényleg értse meg** (egy gondolat lépésenként, tévhit
kimondva és megcáfolva, a végén összefoglalás). 6–9 lépés. A számok valódiak és pontosak,
a modell legyen becsületes (ha egyszerűsítesz, a panelszöveg mondja ki).

**Ne ugorj át ok-okozati lépést.** Minden „ezért” mögött legyen ott a mechanizmus, vagy
hagyd ki az állítást. Rossz: „a jég kisebb sűrűségű, *ezért* fagynak be a tavak felülről”
(a hideg felülről jön; a sűrűség azért számít, mert a jég fent marad és szigetel – ha
lesüllyedne, a tó alulról töltődne fel jéggel). Ha egy következtetéshez a leckében nem
szereplő tudás kell, ne állítsd egy mondatban.

## 2. Fájlok

```
leckek/<tárgy>-<sáv>/NN-slug.html        kód: rajz, mozgás, geometria + lesson-spec
leckek/<tárgy>-<sáv>/NN-slug.md          MINDEN tanár által olvasott szöveg és tényadat
leckek/<tárgy>-<sáv>/NN-slug.content.js  generált (python3 tools/build_lesson.py …), commitolva
shared/lesson.js, shared/lesson.css, shared/fonts/   közös motor – NE módosítsd (csak egyeztetve)
```

Offline, dupla kattintásra működjön: csak sima `<script src>` tagek, **nincs** CDN, fetch/XHR,
ES-modul, külső kép. Képet kóddal rajzolj (canvas), adatot JS-fájlba tegyél.
A repó publikus: abszolút útvonal, név, e-mail nem kerülhet egyetlen fájlba sem.

## 3. HTML-váz

```html
<!doctype html><html lang="hu"><head><meta charset="utf-8">
<title>…</title>
<link rel="stylesheet" href="../../shared/lesson.css">
<script type="application/json" id="lesson-spec">
{ "steps": 8,
  "labels": { "jéghegy": 20, "úszik": null },                       // felirat → max. karakter (null = 32)
  "data":   { "jég sűrűsége": {"unit": "g/cm³", "min": 0.8, "max": 1.0} } }
</script></head><body>
<script src="NN-slug.content.js"></script>
<script src="../../shared/lesson.js"></script>
<script>
(function () { 'use strict';
const U = Lesson.U, F = Lesson.FONTS; let L, c;
L = Lesson.create({
  content: window.LESSON_CONTENT, home: false,
  steps: [ { settle: 6, enter(L) {}, controls(L) {} }, … ],   // cím+szöveg a .md-ből jön
  init(Lx) { L = Lx; c = L.ctx; },
  draw(Lx) { /* háttér + jelenetek áttűnéssel */ },
});
})();
</script></body></html>
```

A spec a **szerződés a .md és a kód között**: minden kulcs, amit a kód használ, benne van;
a build hibát ad hiányzó, fölösleges, túl hosszú, rossz egységű vagy tartományon kívüli
értékre. A JSON-ban nem lehet megjegyzés (a fenti `//` csak magyarázat).

## 4. Motor-API (shared/lesson.js – a fájl tetején részletesen)

- Színpad 1920×1080 logikai px, letterbox. `L.ctx` már skálázva. Vizuális terület **x 0–1360**;
  1380–1896 között a panel takar.
- Idő: `L.st` (mp a lépésbe lépés óta), `L.t`, `L.dt` (≤ 0,05), `L.step`, `L.sp` (simított
  lépésindex áttűnéshez), `L.dir` (+1/−1), `L.prog(a, b)`.
- Lépés: `settle` (mp, ennyi után nyugalmi az állapot – visszalépéskor innen indul, a QA ezt
  fotózza), `enter(L)` (állítsd vissza a szimulációt), `leave(L)`, `controls(L)`.
- Vezérlők: `L.slider({label, k, min, max, step, value, format, onInput})`,
  `L.button(label, fn, k)` – a `k` a .md-kulcs (review módhoz). A `controls` az `enter` ELŐTT
  fut: kezdőértéket közvetlenül az adatból (`L.num`) vegyen. A csúszka kezelője
  `{el, input, set(v, o), get()}`: `set(v)` csak a csúszkát és a kiírt értéket állítja, **nem**
  hívja az `onInput`-ot; `set(v, {fire: true})` hívja is (pl. `__qaStates`-ben: a csúszka és az
  állapot együtt mozog). `L.sliders` az aktuális lépés csúszkái (`L.sliders[k]` a kulcs szerint).
- Mutató: `L.pointer` `{x, y, down, inside}`; egy gyors (egy képkockán belüli) kattintásnál a
  `down` a `draw` előtt már újra `false` – kattintásra ezért a **`L.pointer.pressed`** (lenyomás
  volt az előző képkocka óta; `px, py`: hol), felengedésre a `released` figyeljen, vagy az
  `events` sor (`[{type: 'down'|'up', x, y, button, ts}]`); ezeket a motor a `draw` után üríti. Saját
  `pointerdown`-figyelő nem kell. A `ts` az esemény ideje ms-ban (`performance.now()`-skála) – képkockánál
  pontosabb időméréshez (reakcióidő: `ev.ts` − az inger megjelenésekor mért `performance.now()`;
  `L.now` az aktuális képkocka időbélyege ugyanezen a skálán).
- Nyugalom (`idle`): ha a jelenetben egy `L.st`-hez kötött átmenet a lépés `settle`-je **után** is fut
  (tipikusan: visszalépéskor a `settle`-től induló kamera-áttűnés), add meg:
  `Lesson.create({idle: (L) => L.st >= camEnd, …})` – a QA (`--det`, `--back`, settle-kép) addig vár.
  A kép nem változik tőle.
- Tartalom: `L.lab(k)` felirat · `L.num(k)` szám · `L.unit(k)` · `L.val(k, d?)` → „0,92 g/cm³”.
- Szöveg a vásznon: **csak `L.tx(s, x, y, o)` / `L.pill(s, x, y, o)`** – ezekből tudja a QA és a
  review mód, hol van felirat. `o`: `s` px, `w` vastagság, `f` (`F.D` Fraunces, `F.B` Bricolage,
  `F.M` JetBrains Mono), `i` dőlt, `a` igazítás, `b` alapvonal, `c` szín, `ls` betűköz,
  `max` (szélesség, fölötte kicsinyít), `k` md-kulcs vagy kulcslista, `qa: false` (szándékos
  átfedés, pl. képletjel a dobozban). `L.pill`: `bg`, `bd`, `pad`, `r` – a doboz a szöveghez méreteződik;
  `max`-szal a kicsinyített szöveghez (a doboz szélessége legfeljebb `max` + 2·`pad`).
  A QA forgatott feliratnál (`c.rotate` után `L.tx`) a forgatott téglalappal számol (függőleges
  tengelycímhez nem kell `qa: false`), és a pill dobozát is: ha egy pill egy másik feliratot takar,
  az átfedés.
- `U`: `clamp, lerp, smooth, inOut, out, outBack, rng(seed), rgba, mix, fmt(v, d)`
  (magyar szám: `fmt(-3.14159, 2)` → „−3,14”, `fmt(19300)` → „19 300”).

## 5. Tartalom (.md) – szabályok

Formátum: `leckek/README.md` „A .md formátuma”. Röviden: `# Cím`, metaadat-sor
(`tantárgy: … · évfolyam: … · témakör: …`), `## Közös`, `## N. Lépéscím` + bekezdések,
`képlet:`, `- felsorolás`, `> megjegyzés:`, `### Feliratok` és `### Adatok` (`- kulcs: érték`).

- **Minden** diák által látott szöveg a .md-ben van (panel, vászonfeliratok, gombok, csúszkák).
  Kivétel csak: tengelyszámok, képletjelek (ρ, m, V), mértékegység-jelek – ezek `qa`/review
  szerint „kódban rögzítettek”.
- Minden **tényadat**, amitől az animáció függ (sűrűség, évszám, hőmérséklet), `### Adatok`
  alatt van, és a kód onnan olvassa. Panelszövegben `{kulcs}`-csal hivatkozz rá.
- Kulcs: olvasható magyar kifejezés (`jég sűrűsége`), nem változik. Felirat ≤ 32 karakter,
  kivéve, ha a spec mást ír.
- Panel: lépésenként **≤ 55 szó** (a `> megjegyzés:` is beleszámít), rövid mondatok, tegező, kérdező hang. Legyen benne egy
  `==kiemelés==` a lényegre. `> megjegyzés:` = tanári tipp / feladat / érdekesség.
- Magyar írásmód: tizedesvessző (3,14), valódi mínusz (−), „magyar idézőjel”, nagygondolatjel (–),
  szám és mértékegység között szóköz (10 g, 92 %), kivéve a szögfokot (15°).
- Index, kitevő, képlet a panelen: `F_fel`, `x^2`, `` `x^2 - 4x + 3 = 0` ``, `[[a/b]]` – a build alakítja
  át (táblázat: `leckek/README.md` „Képlet, tört, kitevő…”); ne írj saját megoldást. A vásznon
  ugyanezt a jelölést a `MatText.draw` szedi (`shared/matek/mtext.js`, 12. fejezet). A `#` címben is
  írható (ott Unicode lesz: `` `x^2` `` → x², kémiában `H2O` → H₂O).

## 6. Megjelenés – világos téma (kötelező)

Kivetítőn, világos teremben: **meleg papír háttér, sötét tinta**. Nincs sötét mód, nincs tiszta
fehér nagy felület (vakít), nincs halvány pasztell kulcselemen.

| szerep | szín | használat |
|---|---|---|
| papír | `#f7f1e6` → `#efe6d6` radiális + rács `rgba(28,36,64,.045)` / 40 px | háttér |
| kártya | `#fffaf1`, keret `rgba(28,36,64,.16)` | dobozok, táblázatok |
| tinta | `#1c2440` | fő szöveg, vonalak |
| halvány tinta | `#565d72` | másodlagos szöveg (≥ 22 px!) |
| cinóber | `#c8401c` | fő kiemelés, a lényeg |
| kékeszöld | `#0a6f86` | második kiemelés |
| jó / rossz | `#1d7a45` / `#b3261e` | igaz–hamis, úszik–elmerül |
| víz | kitöltés `rgba(70,150,215,.30→.50)`, vonal `#1b5a94` | |

- Szöveg a papíron ≥ 4,5 : 1 kontraszt. Tárgyak kitöltése lehet világos, de **körvonal mindig
  sötét változat** (2,5–3 px). Fehér szöveg csak telített háttéren (pill).
- Betűk: cím/kiemelt mondat Fraunces (dőlt is), felirat Bricolage, szám/egység JetBrains Mono.
  A panel CSS-ét ne írd felül (kivétel: apró `.lp-text` finomhangolás a lecke `<style>`-jában).

## 7. Elrendezés

- Vizuális terület x 0–1360, y 0–1080; hagyj ~40 px margót.
- Vászonfelirat **≥ 22 px** (kivetítés!), fő címke 26–28 px, jelenetcím 40–58 px.
- Szöveghez igazodó doboz (`L.pill`, `L.measure`), **soha fix dobozméret** – Windowson a fontok
  szélesebbek lehetnek, mint headless Linuxon. Hosszabb feliratnál adj `max`-ot.
- Felirat ne fedjen felirat; vezetővonal (szaggatott) a távoli címkéhez.

## 8. Animáció és állapot

- Az állapot a **lépésindexből és `L.st`-ből számolható** (zárt képlet: `clamp((st − t0)/d)`,
  csillapított beállás képlettel), ne képkockánkénti összegzésből. Így a QA az `L.st` beállításával
  bármely pillanatot lefotózhatja, és a visszaléptetés is jó.
- Interakció után (csúszka, gomb): jegyezd fel a kiinduló állapotot és `L.st`-t, onnan zárt
  képlettel menj a célba. `enter(L)` mindent alaphelyzetbe állít.
- Jelenetek áttűnése: `w = clamp(1 − |L.sp − i|·2)`, a jelenet a saját utolsó idejét kapja
  (lásd a mintalecke `draw`-ját). Új elem: 0,4–0,8 s beúszás; egy lépés ≤ ~8 s alatt nyugalomba ér.
- Kiemelés/elhalványítás: ami épp nem fontos, halványuljon (α ≈ 0,15–0,3), ne tűnjön el.
- **Vászonállapot:** a motor alapból csak a transzformációt állítja vissza képkockánként; a többi
  (`globalAlpha`, `lineCap`/`lineJoin`, `setLineDash`, `shadow*`, `textAlign`, `font`…) az előző
  képkocka végéről átszivárog – ez rontja a `--det` próbát, és az első képkocka másképp néz ki.
  **Új leckében kapcsold be:** `Lesson.create({ resetCtx: true, … })` → minden képkocka előtt
  alapállapot (mint egy friss vásznon; `L.resetCtx()` kézzel is hívható). Ekkor minden rajzoló
  függvény maga állítsa be, amit használ (pl. `c.lineCap = 'round'`). A meglévő leckékben azért
  nincs alapból, mert több közülük tudtán kívül a szivárgó `'round'` vonalvégre támaszkodik.

## 9. QA – kötelező, minden körben

```bash
python3 tools/build_lesson.py leckek/<…>/NN-slug.md
python3 tools/qa_lesson.py leckek/<…>/NN-slug.html --at 1.5,settle --back --review 3
```

- A kimenet lépésenként egy sor; minden `✗` sort javíts (JS-hiba, panel-túlcsordulás, panel
  alá lógó / 22 px alatti / átfedő felirat, hiányzó kulcs).
- **Nézd meg az összes képet** (`build/qa/NN-slug/`): a QA csak a szövegeket ellenőrzi, az
  alakzat–szöveg ütközést, a csúnya arányokat, az olvashatatlan színt csak te látod.
  A korai (`1.5`) képeken az animáció közbenső állapota, a `-vissza` képeken a visszalépés látszik.
- Próbáld ki az interakciókat is (szélső értékek!), pl. Playwrighttal: csúszka `fill`, gomb `click`,
  utána `__lesson.st += 5`, képernyőkép. **Minden interaktív lépésnél legalább két szélső
  állapotot fotózz, és vesd össze a kiírt számot a rajzzal** (pl. 0,99 g/cm³-es hajó pereme a
  vízszintnél legyen, ne alatta). Egy fizikai mennyiség rajza és számítása **ugyanabból a
  geometriai konstansból** dolgozzon – két, hasonló, de eltérő tartály-/skálaobjektum
  tipikus hibaforrás.
- Ellenőrizd a review módot (`review-*.png`): minden felirat lila keretes (van kulcsa).
- A QA ezeket is nézi (`!` = figyelmeztetés, nem rontja a kilépési kódot): a fontokból hiányzó
  karakter (glif – a unicode-range és a fontfájl tényleges tartalma szerint is), 300 ms-nál lassabb
  `enter()`, matekleckében tizedespont/kötőjel-mínusz a vásznon, kattintás nélkül létrehozott
  `AudioContext`. Hiba (`✗`): kattintás nélkül induló hang, gépi felolvasás (`speechSynthesis`). Kapcsolók: `--det` (determinizmus: ugyanannál az `L.st`-nél oda-vissza léptetve
  ugyanaz a kép? – ha a lecke ad `idle`-t, a nyugalomig vár), `--states`
  (`window.__qaStates = {3: [{name: 'min', set(L) {…}}]}`, a kulcs 1-alapú lépésszám – szélső
  állapotok fotója; a `set(L)` közvetlenül az exponálás előtt fut, `L.st = settle` után, így
  `S.t0 = L.st − 2` = „2 mp-cel az indítás után”; `{st: 3.2}` más időpontot, `{wait: 600}` hosszabb
  várakozást ad; a QA figyelmeztet, ha egy állapot nem változtatott a képen),
  `--poke '{…}'` (a lecke `L.poke(o)`-ja), `--data` (az adatok listája).
  Ha a lecke ad `L.checks()` függvényt (→ `[{name, ok, got, want}]`), minden képnél lefut.
- **Ugrópróba** (alapból fut, `--no-jump` kihagyja, `--jump-only` csak ezt futtatja): 1. → utolsó,
  utolsó → 1., véletlen ugrások (számbillentyű: áttűnés közben a **köztes jelenetek is
  rajzolódnak, az `enter()`-jük nélkül**), és betöltés közvetlenül `#N`-re. Minden jelenet `draw`-ja
  működjön akkor is, ha a lépésébe még nem léptünk be: a jelenetállapotot az `init()`-ben hozd
  létre (az `enter()` csak visszaállítsa), vagy őrizd (`if (!S) return`). Egy `draw`-ban dobott hiba
  leállítja a motor főciklusát – a lecke megfagy.

## 10. Kész, ha

- [ ] `build_lesson.py` hiba és figyelmeztetés nélkül fut; a `.content.js` friss.
- [ ] `qa_lesson.py … --back` ✓ minden lépésen; minden képet megnéztél.
- [ ] Minden diák által látott szöveg és tényadat a `.md`-ben; a tényadatok ellenőrzött,
      valós értékek (forrást a `.md` `<!-- -->` megjegyzésében adj meg, ha nem közismert).
- [ ] Világos téma a fenti palettával; ≥ 22 px feliratok; nincs fix dobozméret.
- [ ] Lépésenként ≤ 55 szó; van tévhit-lépés és összefoglaló lépés; van legalább egy valódi
      interakció (csúszka/gomb), amely a modellt mozgatja.
- [ ] Offline, dupla kattintással megy; a `shared/` változatlan (vagy a változás egyeztetett,
      visszafelé kompatibilis, és a `lesson.js` fejlécében dokumentált).
- [ ] Rövid jelentés: lépések listája, ismert gyengeségek, mennyi ideig tartott.

## 11. Történelem-kiegészítés (5–6. évfolyam)

Történelemleckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:**
`pilot/tortenelem-5-6/terv.md` 4. fejezet (szerkesztői elvek: főáram, monda, eredetkérdések,
háborúk, határok, anakronizmus) és a saját briefed a 3. fejezetben.

- **Mappa, fejléc:** `leckek/tortenelem-5-6/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Történelem · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>`.
- **10–12 évesek:** lépésenként **≤ 45 szó** – a spec-be írd: `"maxWords": 45`. Rövid mondatok,
  új fogalom **félkövéren**, egy mondattal megmagyarázva.
- **Három réteg, három jelölés** (minden leckében egységesen, a vásznon és a forráskártyán):
  - *forrás* (kortárs vagy későbbi írott forrás, tárgyi lelet): kékeszöld `#0a6f86` folytonos
    keret, 2,5 px;
  - *rekonstrukció* (történészek, régészek következtetése): tinta `#1c2440` **szaggatott** keret
    (8/6 px), 2,5 px;
  - *monda, hagyomány*: okker kartus – keret `#8f5a0c` (5,1 : 1 a papíron), kitöltés
    `rgba(201,150,60,.16)`, lekerekített/csigás sarok.
  A réteg neve kis feliratként (`forrás` / `rekonstrukció` / `monda`) a keret sarkában is álljon.
  Vallási szövegeknél (bibliai történetek) és élő hagyománynál a felirat `hagyomány`, ne `monda`.
  A tárgyi lelet maga `forrás`; a belőle levont következtetés (pl. egy elterjedési térkép)
  `rekonstrukció`.
- **Bélyegek:** „vázlatos” (kézi határ, vázlatos térkép), „illusztráció” (stilizált alak, jelenet),
  „becslés” (bizonytalan szám). `L.pill`, Bricolage 22 px, 600, betűköz 0,08 em, kisbetű, −3°-kal
  elforgatva, háttér `#fffaf1`, keret 2 px – „vázlatos”/„illusztráció”: halvány tinta `#565d72`,
  „becslés”: okker `#8f5a0c`. A bélyeg szövege is a `.md`-ből jön (felirat-kulcs).
- **„Honnan tudjuk?”** – minden leckében legalább egy lépés vagy forráskártya: ki írta / mi a
  lelet, mikor keletkezett, **hány évvel az esemény után**, résztvevő vagy kortárs volt-e.
- **Új adattípusok** (`leckek/README.md`, a részletek a `tools/build_lesson.py` fejlécében). Spec:
  `"data": {"Róma alapítása": {"type": "year"}, "Pest": {"type": "coord", "box": [9, 42, 30, 51]},
  "sereg": {"type": "range", "unit": "fő"}, "forradalom": {"type": "date"}}`.
  `L.val(k)` a magyar alakot adja („Kr. e. 753”, „kb. 50–70 ezer fő”); `L.dat(k)` a teljes objektumot:
  évszám `{v: −753, a: −752}` (eltelt évek: `b.a − a.a`), dátum `{ymd, a}` (`a`: tört év az
  idővonalhoz), koordináta `{lat, lon}`, tartomány `{lo, hi, v, u}`; becslésnél `est: true`
  (→ „becslés” bélyeg vagy „kb.”). Minden évszám, dátum, helyszín és létszám, amelyet a vászon
  mutat, `### Adatok` alatt legyen – ettől javítható a tanárnak az idővonal és a térkép.
- **Térképadat:** `shared/tort/map-karpat.js` (1:10m), `map-mediterran.js` (1:50m), `map-vilag.js`
  (1:110m, gömbhöz), `map-orszaghatarok.js` (mai határok – csak halvány, kikapcsolható, „mai
  határok” feliratú réteg); vetületek és dekódolás: `shared/tort/proj.js` (`TortProj.lcc`, `ortho`,
  `view`, `fit`, `trace`). Formátum, ajánlott vetület-paraméterek, példa: `shared/tort/README.md`.
  A folyók és partok mai állapotúak: `modern` jelű tározót/csatornát régi korban hagyd el, a
  szabályozás előtti vizeket „vázlatos” saját réteg mutassa. Közkincs, más térképet (atlaszlap,
  tankönyvi kép) ne vegyél át; a „Made with Natural Earth” a `.md` megjegyzésébe kerüljön.
- **Új közös modulok leckén belül:** a térképmotor, az időszalag, a forráskártya és a jelenet-metszet
  (terv.md 5. fejezet) először a referencialeckében készül, a lecke `<script>`-jében **külön,
  jól elhatárolt blokkban** (`/* ── MODUL: Térkép ── */ … /* ── MODUL VÉGE ── */`), saját
  névtérrel (pl. `const TortMap = (() => { … })();`), a blokk elején rövid API-leírással, a
  lecke-specifikus kódra való hivatkozás nélkül – hogy változtatás nélkül átemelhető legyen a
  `shared/tort/` alá. A `shared/` módosítása továbbra is csak egyeztetve.
- **Minden `.md`** végén `<!-- Vitatott / bizonytalan pontok: … -->` blokk a tanári review-hoz,
  forrásokkal (bizonytalan számnál: honnan, mennyire bizonytalan).

## 12. Matematika-kiegészítés (5–6. és 9–10. évfolyam)

Matematikaleckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:** a
saját sávod terve – `pilot/matematika-5-6/terv.md` (3. briefek, 4. modulok API-ja és gyártási
sor) vagy `pilot/matematika-9-10/terv.md` (3. briefek, 4. szerkesztői elvek, 5. modulok).
A *(5–6)* / *(9–10)* jelű pont csak arra a sávra vonatkozik.

- **Mappa, fejléc:** `leckek/matematika-5-6/…` ill. `leckek/matematika-9-10/…`; metaadat-sor:
  `tantárgy: Matematika · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>`.
  Spec: `"math": true`; *(5–6)* `"maxWords": 45`, *(9–10)* 55 (alap). Egy képletszakasz, tört,
  hatvány 1 szónak számít, a `képlet:` sor 3-nak.
- **Jelölés a `.md`-ben (egységes, mindkét sávban):** képlet `` `…` `` között vagy `képlet:` sorban
  (`*` → ·, `-` → −, `<=` `>=` `!=` `~=` `|->` `=>` `<=>` `+-` → ≤ ≥ ≠ ≈ ↦ ⇒ ⇔ ±, `pi` → π,
  `NN ZZ QQ RR` → ℕ ℤ ℚ ℝ, `√(…)`/`gyök(…)`, a betűk – a görög kisbetűk (α, β, γ′) is – dőltek,
  `sin lg log max…`, a π és a görög nagybetűk (Δ, Σ, Ω) állók);
  kitevő `2^3`, `10^-3`, `2^(n+1)`; index `x_1`, `D_f`; tört a szövegben is `3/4` (álló), vegyes
  szám `2 1/3`, emeletes tört `[[a + b/2]]` vagy a `képlet:` sorban `(a + b) / (2a)`; halmaz
  `{1; 2; 3}`, pont `A(2; −3)`, intervallum `[a; b]`, `]a; b[` – pontosvesszővel, mert a vessző
  tizedesvessző. A build figyelmeztet: `3*4`, `5 - 3`, `3.14`, `30'`, `(3, 2)`, `cm2`, és ha sor
  `>`-vel kezdődik (az megjegyzésdoboz – egyenlőtlenség `` `x > 3` `` alakban). Szög `45°`, `30′`;
  arány `2 : 3`; százalék `25 %`; ezres tagolás 5 jegytől (`U.fmt`): 4527, de 12 000. Közelítő
  értéknél „≈”, sosem „=”.
- **Szaknyelv:** szorzás `·`, osztás `:`, negatív szám zárójelben a műveleti jel után
  (`3 − (−5)`); pont nagy dőlt betű, egyenes kis dőlt, szög görög betű; a háromszög `a, b, c`
  oldala az `A, B, C` csúccsal szemben; `ℕ` tartalmazza a 0-t; `e ∥ f`, `e ⊥ f`. *(9–10)* A
  nevezetes pontok betűi `### Feliratok` alatt legyenek (tankönyvenként eltérnek).
- **A vásznon** matematikai szöveget (tört, kitevő, index, gyök, képlet) **csak a `MatText.draw`**
  szed: `<script src="../../shared/matek/mtext.js"></script>` a `lesson.js` után;
  `MatText.draw(L, L.lab('megoldás'), x, y, {s: 34, k: 'megoldás', math: true})`. A darabokat
  `L.tx`-szel írja, kulccsal (QA, review). Unicode-kitevő (⁵) vagy kézzel rakott darabok helyett
  is ezt használd. Betűk: szám, műveleti jel JetBrains Mono (`o.f`), változó dőlt Fraunces (`o.vf`),
  magyarázó felirat Bricolage. Méret: tört részei az alap 0,8-szorosa → alap ≥ 28 px; kitevő
  0,65-szöröse → alap ≥ 34 px. A hiányzó jeleket (π, ≤, ∈…) a fontkészlet unicode-range-dzsel
  pótolja; a QA jelzi, ha valami mégis kiesik.
- **Pontos számolás:** törtekkel `MatQ` (racionális aritmetika: `MatQ(1, 2).add(MatQ(1, 3))`,
  `.str('mixed')`, `.dec()` → periódus), nem lebegőpontosan. Tizedes alakot csak kiíráskor
  kerekíts, és akkor „≈”. Kifejezés-adat (`expr`) kiértékelése: `MatText.evalExpr(L.dat(k).tree,
  {x: 2})` / `MatQ.evalExpr` – `eval` nincs.
- **Bemenet az `.md`-ben, eredmény a kódban.** A feladat adatai `### Adatok` alatt (`frac`, `point`,
  `list`, `expr`, `ratio`, `"int": true`, `"dim": "terület"`); az eredményt a kód számolja. Ha egy
  eredmény a panelen is szerepel (`{összeg}`), az is adat, és a kód ellenőrzi:
  `MatText.check(L, 'összeg', várt)` – eltérésnél hibasáv, a QA elkapja.
- **A rajz maga a bizonyíték.** Minden kiírt mért érték a rajzolt geometriából vagy a lefuttatott
  szimulációból számolódik, ugyanazzal a konstanssal; a kerekítés egy közös függvényen megy át
  (`U.fmt`, ≤ 2 tizedes, szög 1). Szándékosan nem méretarányos ábra „vázlat” bélyeget kap.
  *(9–10)* Ami csak mér, „mérés” bélyeget kap; a bizonyító lépés „bizonyítás” (cinóber keret),
  a végén `∎`; a panel kimondja, ha egy állítást a lecke nem bizonyít.
- **A tévhitet ellenpélda cáfolja a vásznon** (1/2 + 1/3 ≠ 2/5: a 2/5 szalagja rövidebb az 1/2-énél).
  *(5–6)* Legyen egy „Tippelj előbb!” pillanat.
- **Szerepek színekkel:** adott elem tinta; vizsgált elem és eredmény cinóber (eredmény 3,5 px);
  második elem kékeszöld; segédvonal halvány tinta 2 px. Halmazok A cinóber, B kékeszöld, C okker
  `#8f5a0c`, kitöltés α 0,16–0,24, a kiemelt rész sraffozva is. Előjel: pozitív cinóber, negatív
  kékeszöld. Grafikon: tengely tinta 2,5 px nyíllal, rács `rgba(28,36,64,.08)`, fő görbe 4 px
  cinóber, a görbe vágva és szakadásnál megszakítva; nyílt végpont üres, zárt teli karika.
  Rajzlap: 40 px-es rács; egységnégyzetnél az egység 40 px többszöröse, erősebb rács.
- **Húzható elem:** látható fogantyú ≥ 12 px, találati sugár ≥ 28 px, húzás közben élő érték;
  egészre/rácsra ugrik, ahol a tananyag kéri; pályán marad; elfajuló helyzetben halványul, és
  `.md`-felirat jelzi. Billentyűvel/csúszkával is elérhető. Az `enter(L)` visszaállítja. A szélső
  helyzeteket a QA-val fotózd: `window.__qaStates` + `--states`.
- **Véletlen:** csak `U.rng(seed)` (ill. a `MatRand`); az n-edik kísérlet a seedből és n-ből
  számolható; a kiírt gyakoriság a kirajzolt kísérletekből jön; 10 000 kísérletet ne
  képkockánként szimulálj. QA: `--det`.
- **Kitalált és valós adat:** kitalált példa `<!-- kitalált példa -->` (*(9–10)* a vásznon
  „kitalált adat” bélyeg); valós adat forrással és dátummal a megjegyzésben.
- **Modulok:** a `shared/matek/mtext.js` kész. A többi `Mat…` modul (`MatLine`, `MatPlot`,
  `MatGeo`, `MatFrac`, `MatRand`, `MatVenn`, `MatFv`, `MatSzerk`…) a 16. fejezet szerint, a terv
  4./5. fejezetének API-jával. A 9–10 terv `MatKeplet` modulja nem készül külön: az a `MatText.draw`.
- **Minden `.md`** végén *(5–6)* `<!-- Tanári megjegyzések: … -->` (kitalált számok,
  egyszerűsítések, tankönyvi jelöléseltérés), *(9–10)* `<!-- Matematikai ellenőrzés: … -->`
  (számpéldák, tételek, mivel ellenőrizted, dátum).

## 13. Kémia-kiegészítés (7–8. évfolyam)

**Kötelező olvasmány:** `pilot/kemia-7-8/terv.md` 5. fejezet (szerkesztői elvek) és a saját
briefed (3. fejezet).

- **Mappa, fejléc:** `leckek/kemia-7-8/…`; `tantárgy: Kémia · évfolyam: 7–8. · témakör: N. …`.
  Spec: `"chem": true`.
- **Képlet a `.md`-ben:** ASCII-ként (`H2O`, `Ca(OH)2`, `Na^+`, `SO4^2-`, `->`) vagy Unicode-dal
  (`H₂O`, `Na⁺`, `→`); a build a panelre `<sub>`/`<sup>`-t, a feliratba Unicode-ot tesz, és minden
  átalakítást `info:` sorban kiír – nézd át (vitamin- vagy útjelzés-szerű szavakat, pl. `B12`,
  nem alakít át; egyedi esetben `\` elé). Adat: `formula` (`{"atoms": …, "charge": …}`) és
  `equation` (a build ellenőrzi az atom- és töltésmérleget). Mol, ⇌, állapotjel nincs.
- **A vásznon:** a Unicode-alak (`H₂O`, `Na⁺`) `L.tx`-szel is helyesen jelenik meg (a fontkészlet
  lefedi); egyenlethez és nagy képlethez `MatText.draw(L, L.lab('reakció'), x, y, {chem: true,
  s: 34})` – valódi index, a QA-nak egy kulccsal. A `KemTx`, ha kell, erre épüljön.
- **Szóegyenlet először** („metán + oxigén → szén-dioxid + víz”), a képletes egyenlet kiegészítő.
- **Három szint:** makro (természetes színek), részecske (csak nagyítóban/részecskeablakban,
  tintakeret, „nagyítás · szemléltetés” felirat a `.md`-ből), jel (JetBrains Mono).
- **Magyar nevek** (AkH., nevezéktan): szén-dioxid, nátrium-klorid; nátriumion, kloridion;
  Na⁺-ion. Ionvegyületnél nincs „molekula”. Antropomorf szó („szeretne”) nincs.
- **Atomszínek** a `KemMol.EL` szerint (H fehér, C fekete, O piros, N kék, Cl zöld, S sárga,
  Na lila), sötét körvonallal; kiemelés gyűrű/fényudvar (cinóber), nem kitöltés.
- **A modell becsületessége:** a részecskerajz mérete, távolsága, sebessége nem arányos – ahol
  félrevezethet, a panel kimondja; a Bohr-modell „modell”.
- **Biztonság (kötelező; részletek: terv 5. fejezet):** veszélyes kísérlet soha nem recept
  (nincs mennyiség, lépéssor, látványos robbanás), „NE PRÓBÁLD KI” (keret `#b3261e`) vagy
  „tanári bemutató” bélyeggel, a veszély okát mutatja. Otthon csak konyhai anyag, azzal is:
  nem kóstoljuk, nem szagoljuk, szemvédelem. A helyes cselekvést írjuk (fedő, szellőztetés, 112).
  GHS-jel csak valósághű. Biztonsági szám (gyulladási hőmérséklet, határérték) forrással.
- **Részecskeszimuláció:** determinisztikus visszajátszás (`S.at(L.st, events)`), az események
  időbélyeggel naplózva, az `enter(L)` üríti; nem `L.dt`-vel léptetve. QA: `--det`.
- **Minden `.md`** végén `<!-- Modell-egyszerűsítések és források: … -->`.

## 14. Biológia-kiegészítés (7–8. évfolyam)

**Kötelező olvasmány:** `pilot/biologia-7-8/terv.md` – a saját briefed (3.), a modulok (4.) és a
teljes kiegészítés-szöveg (7. fejezet: emberi test, szaporodás, egészség, evolúció, emberi
sokféleség – ezek a szerkesztői elvek kötelezők).

- **Mappa, fejléc:** `leckek/biologia-7-8/…`; `tantárgy: Biológia · évfolyam: 7–8. · témakör: N. …`.
  ≤ 55 szó; új fogalom félkövéren, egy mondattal.
- **„Honnan tudjuk?”** lépés vagy kártya minden leckében; elavult tankönyvi számnál az újabb, az
  eltérést kimondva.
- **Emberi test:** stilizált, nemileg semleges, nem szexualizált alak; több testalkat, egyik sem
  „ideális”; semleges bőrtónus; nincs vér, sérülés, ijesztgetés. Szaporodás csak a kerettanterv
  szintjén, sematikus metszetrajzzal.
- **Szervrendszer-színkód** (egyszerre ≤ 3 rendszer színes): oxigéndús vér `#c0392b`,
  oxigénszegény vér `#7b2440` (**soha nem kék**), levegő/O₂ `#0a6f86` (CO₂ `#565d72`), tápanyag
  `#8f5a0c`, kiválasztás `#6b6a12`, ideg `#2a4d9b`, hormon `#7b4fa0`, csont `#ece1c9`/`#6b5a3e`,
  izom `#e3a593`/`#8c3b2a`.
- **Egészség, elsősegély:** minden egészségügyi szám forrással; nincs egyéni tanács, márka. Az
  elsősegély az ERC/MRT aktuális ajánlása szerint, a számok és a lépések sorrendje `### Adatok`
  alatt; spec `"review": ["elsősegély"]` → a build kéri a `<!-- Szakmai ellenőrzés: <szerep>,
  <dátum>, <ajánlás verziója> -->` blokkot (név nélkül). 112; az utolsó lépés gyakorlati képzésre bíztat.
- **Evolúció, sokféleség:** tudományos keretben, elágazó bokor (nincs „majomtól emberig” sor),
  célelvű szavak nélkül; egy emberi faj, folytonos változatosság, nincs tipológiai ábra.
- **Számok:** mikro `µ` (nem `u`; a build az `um`-ot átírja); nagy szám szóval (`480 millió`);
  **billió = 10¹²** – angol forrásból kétszer ellenőrizd; élettani adat tartománnyal és kire
  vonatkozik: `60–100/perc` (`range`), ütem `70/perc`; `"dim": "térfogat"` stb., ha az egység
  változhat (a `range` típus is fogad `dim`-et: `60–90 µm` → `blo`, `bhi`, `base` méterben).
- **Szimulációk** (populáció, öröklődés, járvány): csak `U.rng(seed)`; az `enter()`-ben vagy az
  interakció után előre lefut (≤ 200 ms – a QA 300 ms fölött szól), a rajz az `L.st` szerinti
  pillanatot mutatja; „Újra” új seedet ad, a QA az alapseeddel fotóz (`--det`). A panel kimondja,
  ha az eredmény a véletlentől függ, és ha a modell didaktikus.
- **Képek csak saját rajzból** (canvas); állatkísérlet, boncolás nincs.

## 15. Földrajz-kiegészítés (9–10. évfolyam)

**Kötelező olvasmány:** `pilot/foldrajz-9-10/terv.md` 4. fejezet (modulok, adatfájlok), a saját
briefed (3.) és a teljes kiegészítés-szöveg (7. fejezet – a 7. „Határok, nevek” és a 8. „Érzékeny
témák” pont kötelező). A Történelem-kiegészítésből érvényes: bélyegstílus, térképadat, „mai
határok” réteg.

- **Mappa, fejléc:** `leckek/foldrajz-9-10/…`; `tantárgy: Földrajz · évfolyam: 9–10. · témakör: N. …`.
  Spec: `"sources": true`. A kerettanterv fogalma első előfordulásakor félkövér; topográfiai
  név a kerettanterv írásmódjával.
- **Négyféle adat:** *mért* (forrássorral), *becslés* („kb.” / „becslés” bélyeg), *előrejelzés*
  (szaggatott vonal 8/6 px vagy sáv, „előrejelzés” bélyeg kékeszöld kerettel, forrás + kiadás +
  változat), *modell* („modell” bélyeg halvány tinta; a panel kimondja, mit hagy el). Kézi
  áramlás, partvonal: „vázlatos”.
- **Az adat éve a `.md`-ben:** `- világ népessége: 8,2 milliárd fő (2025, frissítendő)`,
  `(2050, előrejelzés)`, `(modell)` → `L.dat(k).yr / .upd / .proj / .model`; a kód ebből
  rajzolja a bélyeget és a forrássor évét. `python3 tools/build_lesson.py --stale` listázza a
  2 évnél régebbi „frissítendő” adatokat.
- **Forrás a `.md`-ben:** minden adat mellé `<!-- forrás: <hivatkozás>, lekérdezve: ÉÉÉÉ-HH-NN,
  licenc -->` ugyanabban vagy a következő sorban, vagy a szakasz elején egyszer `<!-- forrás
  (az alábbiakra): … -->`; a build szól, ha hiányzik. A vásznon minden diagram és tematikus
  térkép alatt forrássor („Forrás: <intézmény, adatkészlet>, <év>”, Bricolage 22 px, egy
  `forrás …` felirat-kulcsból).
- **Nagy adat** a `shared/foldrajz/<id>.js` alatt (`tools/build_geodata.py`, fejlécben forrás,
  licenc, verzió); a `.md` `dataset` típusú adattal hivatkozik rá (`- korfa: ENSZ WPP 2024`, spec
  `{"type": "dataset", "id": "korfa-wpp2024"}` – a szöveg a forrássor rövid neve; a build
  ellenőrzi, hogy a fájl létezik, és a benne írt évszám a fájl fejlécének verziójában is szerepel). Amit a
  panel kimond vagy a vászon kiemel, az `### Adatok` alatt is szerepel. Havi sorozat: `list`
  (`"len": 12`); időzóna: `utc`; mély idő: `ago`; koordináta: `coord`.
- **Lépték és vetület:** keresztmetszetnél „függőleges torzítás N×” bélyeg, és legalább egyszer
  méretarányos nézet. Globális folyamat gömbön (`TortProj.ortho`) vagy egyenlő területű
  vetületen (`TortProj.equalEarth`); Mercatoron területet nem hasonlítunk. Log. tengelyen
  „log. skála” felirat.
- **Színek:** szekvenciális papír → cinóber / kékeszöld, 4–6 osztály; divergens kékeszöld ↔ papír
  ↔ cinóber értelmes középponttal; „nincs adat” halvány sraffozás; ország nem kap „jó” zöld /
  „rossz” piros színt; meleg/hideg áramlás cinóber / `#1b5a94`.
- **Érzékeny témák semlegesen, adattal** (migráció ENSZ/UNHCR-fogalmakkal, fejlettség
  mutatókkal, éghajlatváltozás az IPCC AR6 konszenzusa szerint, pénzügyben nincs márka/ajánlás,
  katasztrófa tisztelettel) – a terv 7. fejezet 8. pontja szerint.
- **Licenc:** közkincs vagy nyílt (CC BY, ODC-BY, CC BY 3.0 IGO), nevezéssel a `.md`-ben és a
  forrássorban; más csak jóváhagyással. Kép, atlaszlap, műholdfelvétel nem kerül be.
- **QA:** modellnél mindkét szélső beállítás (`--states`) és kézi ellenőrző számolás; gömbnél a
  hátoldal is; időcsúszkánál az első és az utolsó adatév; `--data` kiírja az adatok évét és jelölőit.

## 16. Közös modulok és párhuzamos gyártás

- **Kész közös fájlok** (betöltés sima `<script>`-tel, a `lesson.js` után): `shared/matek/mtext.js`
  (`MatText`, `MatQ`), `shared/tort/proj.js` + térképadatok, `shared/foldrajz/*.js` adatkészletek.
  Ezeket a leckeügynök **nem módosítja**; hiba vagy hiány esetén a jelentésében jelzi
  (fájl, függvény, mi kellene, miért).
- **Új tantárgyi modul** (pl. `MatLine`, `KemMol`, `Reszecske`, `BioTest`, `FoldSection`) először a
  terv szerinti **referencialeckében** készül, a lecke `<script>`-jében külön blokkban:
  `/* ── MODUL: Számegyenes (MatLine) · forrás: matematika-5-6/03-…, 2026-11-23 ── */ … /* ── MODUL VÉGE ── */`,
  saját névtérrel (`const MatLine = (() => { … })();`), a blokk elején API-leírással, a
  lecke-specifikus kódra való hivatkozás nélkül.
- **Átvétel:** a többi lecke a blokkot **bájtra azonosan** másolja az eddigi legfrissebb leckéből
  (ellenőrzés: `diff` a két blokk között). Ha bővíteni kell, csak visszafelé kompatibilisen, a
  fejlécben jelezve, és a jelentésben kiemelve – a koordinátor viszi vissza a referenciába, majd
  (több átvétel után) a `shared/` alá. Párhuzamos változatot ne írj.
- **Párhuzamos munkában** a leckeügynök csak a saját leckéjének fájljait írja
  (`leckek/<tárgy>-<sáv>/NN-slug.{md,html,content.js}`); a `shared/` és a `tools/` alá nem ír,
  a `build_index.py`-t nem futtatja. Build **csak a saját leckére**:
  `python3 tools/build_lesson.py leckek/<…>/NN-slug.md` – a `--all` más, épp készülő leckék
  fájljait is újraírná. QA a saját `--out` mappába (vagy az alapértelmezett `build/qa/<lecke>/`-ba).
- **Build- vagy QA-igény** (új adattípus, jelölés, QA-ellenőrzés) a jelentésbe kerül, nem a
  `tools/`-ba; addig a lecke a meglévő típusokkal és egy `<!-- -->` megjegyzéssel old meg mindent.

## 17. Természettudomány-kiegészítés (5–6. évfolyam)

**Kötelező olvasmány:** `pilot/termeszettudomany-5-6/terv.md` – a saját briefed (3. fejezet), a
modulok és a forrásleckék (4. fejezet). Ahol a lecke más sorozat modulját vagy témáját használja, ott
annak a tantárgyi fejezete is érvényes (pl. a 13. Kémia biztonsági pontja, a 14. Biológia emberi
test pontja, a 15. Földrajz forrássora) – ez a fejezet csak a 10–12 évesekre vonatkozó eltéréseket
és kiegészítéseket adja.

- **Mappa, fejléc:** `leckek/termeszettudomany-5-6/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Természettudomány · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>`.
  Spec: `"maxWords": 45`; ha a lecke valódi mért adatot mutat diagramon vagy térképen:
  `"sources": true`; a 02-es leckében `"review": ["tűzvédelem"]`, a 13-asban `"review": ["egészség"]`.
- **Nyelv 10–12 éveseknek.** Rövid mondatok (legfeljebb kb. 15 szó), tegező, kérdező hang. Lépésenként
  egy új fogalom, **félkövéren**, egy egyszerű mondattal megmagyarázva. Csak a kerettanterv
  fogalomlistájának szintjén: ami ott nincs (pl. elektron, fotoszintézis, szublimáció, LAI), az
  legfeljebb a `> megjegyzés:`-ben kerül elő, „ezt majd 7–8. osztályban tanulod” formában. Nagy
  számot hasonlattal is adj („kb. 230 kg – mint három felnőtt”). A hasonlat is tényadat, ezért a kód
  számolja ki, vagy az `### Adatok` alatt szerepel. Latin fajnév csak a `.md` megjegyzésében. Idegen szó
  helyett a magyar („ásványi anyag”, nem „minerál”).
- **„Tippelj!” → kísérlet → magyarázat.** Minden leckében legalább egy jóslat a kísérlet előtt:
  2–4 `L.button` a `.md` `tipp …` kulcsaival (a felirat-kulcsok vége `… tipp`, `… gomb`). A
  választásig a megoldás nem látszik; utána a vásznon „a te tipped” jel (cinóber keret) és a helyes
  válasz. Ha rossz volt a tipp, nem jár érte szidás, a panel így folytatja: „Sokan gondolják így – nézzük meg!”.
  Az állapot a lépés `enter(L)`-jében törlődik. QA: `__qaStates` `tipp-jó` és `tipp-rossz` állapottal.
- **Kísérlet-bélyegek** (a KemGHS bélyegstílusával, a szöveg a `.md`-ből): „otthon is kipróbálhatod”
  (kékeszöld keret) – csak veszélytelen, konyhai anyaggal; „felnőttel együtt” (okker `#8f5a0c`) –
  forró víz, kés, üveg, vízpart; „tanári bemutató” – tűz, sav, áram; „NE PRÓBÁLD KI” (`#b3261e`) –
  amit a lecke csak a veszély megértéséért mutat. Minden valódi kísérlet rajzán legyen pontosan egy
  bélyeg.
- **Biztonsági elv.** Veszélyes kísérletet a lecke soha nem mutat követendőként: nincs
  mennyiség, lépéssor, látványos robbanás vagy lángolás. A veszély okát mutatja meg (pl. a vízcsepp
  gőzzé robban a forró olajban), és a helyes cselekvést írja le (fedő, gázcsap, 112, szellőztetés,
  kimenni). Kötelező mondatok, ahol a téma előkerül: a konnektorral (230 V) nem kísérletezünk; a
  Napba soha nem nézünk (szemüveggel, távcsővel, telefonnal sem); kis erős mágnes nem kerül a
  szánkba; villámláskor nem állunk fa alá, és kijövünk a vízből; a jégre és a vízpartra csak felnőttel;
  a gombát és a bogyót nem kóstoljuk meg; vegyszert nem szagolunk és nem kóstolunk. A tűz ábrázolása
  jelzésszerű: nincs égő ember, sérült, áldozat; a füst stilizált. Segélyhívó: 112.
- **Élőlények ábrázolása.** Saját, stilizált rajz (`TtIkon`), felismerhető hazai fajok a hivatalos
  magyar nevükkel (az `.md`-ben). Nincs emberi arc, ruha, mosoly, rajzfilmszem, és nincs antropomorf
  szó („a róka gonosz”, „a növény szeretne”, „a hóvirág bátor”): a „siet” vagy „keres” szót csak
  idézőjelben vagy magyarázattal használjuk (a hóvirág „siet” = korán virágzik, amíg fény jut le). A
  ragadozás jelzésszerű: a zsákmány halványul vagy eltűnik, nincs vér, tetem, szenvedés. A pusztuló
  halak halványulnak. Az arányok nem méretarányosak – ha félrevezető lehet, „nem méretarányos”
  bélyeg. A „kártevő”, „gyom” szó mellett egyszer elhangzik: „az ember szempontjából”. Védett fajnál
  a „ne szedd le / ne zavard” üzenet indoklással szerepel, nem tiltásként. Élő állattal végzett
  kísérletet a lecke nem mutat. Ha a kerettanterv megfigyelést javasol (giliszta, csiga), a megjegyzés
  kíméletes, rövid megfigyelést és visszaengedést kér.
- **Az ember ábrázolása.** A Biológia-kiegészítés (14.) emberi test pontja érvényes (semleges
  `BioBody`, több alkat, egyik sem „ideális”, semleges bőrtónus, szervrendszer-színkód). A
  10–12 évesekre vonatkozó kiegészítések: nincs testsúly-, BMI-, kalória- vagy „ideális” méretcél, és
  ételt sem minősítünk „rossz”-nak. Az étrendet a hivatalos ajánlás arányaival mutatjuk, pontozás
  nélkül. Kamaszkorról csak a növekedési ugrás és az, hogy „mindenkinél máskor kezdődik”. Nemi jelleg
  nem jelenik meg, a lelki változásokról egy semleges, támogató mondat szól. Egyéni tanácsot a lecke nem
  ad („ha valami aggaszt, kérdezd meg az orvost, a védőnőt vagy a szüleidet”). Egészségügyi szám
  csak forrással és tartománnyal, megnevezve, kire vonatkozik (10–12 évesek, felnőttek).
- **A modell becsületessége.** Minden egyszerűsített szimuláció (növekedés, erózió, szukcesszió,
  eutrofizáció, füst, futás, energiafalu, homokasztal) „modell” bélyeget kap, és a panel egy
  mondatban kimondja, mit hagy el. A kitalált helyszín és adat (Tóvölgy, a kitalált nap, a falu)
  `<!-- kitalált példa -->` és a vásznon „kitalált” bélyeg. A részecskék csak a nagyítóban
  („nagyítás · szemléltetés”, Kémia-kiegészítés) jelennek meg.
- **Adatok, források.** A valódi adat forrással, évvel, és ahol kell, „frissítendő” jelöléssel
  szerepel (a Földrajz-kiegészítés szerint; a forrássor a vásznon diagramnál és tematikus térképnél
  kötelező). Ugyanaz a tény a sorozatokban ugyanaz a szám: ha egy másik lecke már tartalmazza (pl. a
  tengelyferdeség, Budapest éghajlati adatai, a Föld kora, a papucsállatka mérete), vedd át onnan, és
  a megjegyzésben nevezd meg a leckét. A kerekítést a panel jelzi („kb.”).
- **Kapcsolódás más sorozatokhoz.** Ahol a téma 7–10. osztályos változata már elkészült (a terv.md
  1. fejezetének táblázata), ott ne ismételd a részleteit. A `> megjegyzés:` egy mondatban nevezze
  meg a folytatást („7. osztályban a fizikában…”).
- **Kulcsnevek** (a Feliratok és az Adatok közös névtérben vannak): az adatkulcs egy főnévi
  kifejezés a mennyiséggel („jég sűrűsége”, „Budapest hőmérséklete”); a felirat-kulcs végén a szerepe
  áll („… cím”, „… gomb”, „… csúszka”, „… tipp”, „… bélyeg”, „… felirat”). Kettőspont nem lehet a
  kulcsban.
- **Modulok:** a `TtIkon` (referencia: `10-erdo`) és a `TtMuszer` (referencia: `03-meres`) a
  16. fejezet szerint, a terv 4.2 pontjának API-jával. A blokkhatár egységesen
  `/* ── MODUL: <név> (<Névtér>) · forrás: termeszettudomany-5-6/NN-slug, <dátum> ── */` …
  `/* ── MODUL VÉGE: <név> ── */`. A többi modult (4.1 táblázat) bájtra azonosan vedd át. A SKY
  („ÉGBOLT-MODUL”) blokkot a saját, nem szabványos jelölőivel együtt másold.
- **Minden `.md`** végén `<!-- Tanári megjegyzések és források: … -->` blokk: kitalált példák,
  modell-egyszerűsítések, bizonytalan számok (honnan, mennyire bizonytalan), a tankönyvektől eltérő
  jelölés vagy beosztás (pl. a földrészek száma, a magassági színek határai). A 02-es és a 13-as
  leckében ezen felül `<!-- Szakmai ellenőrzés: <szerep>, <dátum>, <ajánlás verziója> -->` (név nélkül).

## 18. Magyar nyelv és irodalom-kiegészítés (5–6. évfolyam)

Magyarleckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:**
`pilot/magyar-5-6/terv.md` – a saját briefed (3. fejezet) és a modulok API-vázlata (4. fejezet). A
build-jelölések a terv 5. fejezetéhez képest egyszerűbbek: **ez a fejezet és a `leckek/README.md`
„Magyar nyelv és irodalom” szakasza a mérvadó.**

- **Mappa, fejléc:** `leckek/magyar-5-6/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Magyar nyelv és irodalom · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>`.
  Spec: `"maxWords": 45`, irodalomleckében `"interpretive": true`. Rövid mondatok, tegező hang, új
  fogalom **félkövéren**, egy mondattal megmagyarázva.
- **Build-jelölések** (részletek és példák: `leckek/README.md`; a mezők: a `tools/build_lesson.py` fejléce):
  - `### Idézet` blokk (bármely `##` alatt), soronként `- kulcs: szöveg`; a kulcs olvasható
    (`jv 1/1` = János vitéz 1. fejezet 1. sor). A sorban `|` = sormetszet (a megjelenő szövegből eltűnik).
    A blokk **előtt** kötelező: `<!-- idézet: <szerző>: <mű> (<év>), <hely> · szöveg: <kiadás/MEK-szám/URL> · szerző † <év> · közkincs -->`
    (népköltészet: `népköltészet · gyűjtő † <év>`; kerettanterv-szöveg: `jogszabály`; fordításnál a
    `fordító † <év>` is). A build **hibát ad**, ha a forrásmegjegyzés, a `szöveg:` vagy a † év hiányzik,
    vagy ha bármely † év + 70 ≥ az idei év (védett). A JS-ben: `L.quote(k)` (szöveg), `L.quoteDat(k)`
    (`{s, syl, v: a magánhangzók indexei, cut, ci, ref}`); a review mód a sorát mutatja.
  - **Verssor-ellenőrzés** a specben: `"quoteSets": {"jv": {"syll": 12, "cut": 6, "lines": 24}}` (a
    `jv …` kulcsú sorokra; `"syll": [8, 6]` soronként váltakozik) vagy `"quotes": {"jv 1/1": {…}}`. A
    szótagszám = a magánhangzók száma (az *y* csak a spec `"yVowel"` listájának szavaiban). Eltérés
    (szótagszám, metszet) **hiba**, kivéve, ha a sor végén ott a `<!-- szótagszám: 11, a forrásban is -->`
    (a számnak egyeznie kell) vagy `<!-- eltérés: … -->` megjegyzés – ekkor figyelmeztetés.
  - **Rím és metrum kézzel jelölve**, a build nem elemez: `### Adatok` alatt `- jv rímképlet: aabb`
    (spec `{"type": "rhyme", "quotes": "jv"}` vagy `"lines": [...]`; x = rímtelen; versszakonként
    ismétlődik) – figyelmeztet, ha egy rímpár utolsó magánhangzója eltér. `- huszt 1 metrum: — ∪ ∪ | — ∪ ∪ | — ×`
    (spec `{"type": "metrum", "line": "huszt 1"}`; `-` `u` `x` is írható) – hiba, ha a jelek száma ≠
    a sor szótagszáma; figyelmeztet, ha hosszú magánhangzó (á é í ó ő ú ű) ∪ helyen áll. A
    helyzeti hosszúságot (rövid magánhangzó + két mássalhangzó) a build **nem** számolja: azt a `.md`
    jelöli, és a tanári review ellenőrzi.
  - **Szóelem:** `- kertészeknek: kert + ész (képző) + ek (jel) + nek (rag)` (`{"type": "morph"}`;
    fajta: tő, képző, jel, rag, kötőhangzó, előtag; változatlista külön adatként: `-ban/-ben (rag)`).
    Hiba: rag után jel vagy képző; figyelmeztetés: hangrend-eltérés (kivétel, pl. *célba*: a sor végére
    `<!-- ingadozó -->`). **Ejtés:** `- kútba: kútba [kúdba]` (`"pron"`). **Szereplőkapcsolat:**
    `- Gergely és Éva: Gergely – Éva: szerelem (I–V)` (`"rel"`; fajta: barát, ellenség, család,
    szerelem, szolgál, vezet; a szereplők és az egységek: spec `"rel": {"people": [...], "units": [...]}`).
  - **`> értelmezés: …`** a panelen „Egy lehetséges olvasat” fejlécű doboz (`shared/lesson.css`
    `.interp`), a szókorlátba beleszámít. `"interpretive": true` mellett a build figyelmeztet, ha
    nincs a leckében ilyen doboz és kérdéssel végződő lépés sem.
- **Szerzői jog – kötelező (a repó nyilvános).**
  - Szó szerint csak **közkincs** szöveg idézhető: a szerző halálát követő év január 1-jétől
    számított 70 év letelt (Szjt. 31. §), 2026-ban a legkésőbb 1955-ben elhunytaké. Közkincs pl.
    Petőfi (†1849), Arany (†1882), Kölcsey (†1838), Vörösmarty (†1855), Csokonai (†1805), Fazekas
    (†1828), Jókai (†1904), Ady (†1919), Gárdonyi (†1922), Móra (†1934), Juhász Gyula és József
    Attila (†1937), Karinthy és Dsida (†1938), Reményik (†1941), Radnóti (†1944), Molnár Ferenc
    (†1952), Ilosvai, Tinódi, Szendrey Júlia.
  - **Védett** (legfeljebb cím + egy-két mondatos saját szavas utalás): Weöres Sándor, Kányádi
    Sándor, Nemes Nagy Ágnes, Nagy László, Ágh István, Szabó Magda, Fekete István, Lázár Ervin,
    Kittenberger Kálmán (†1958, 2029-től közkincs), Széchenyi Zsigmond, O. Nagy Gábor, Illyés Gyula
    (népmese-feldolgozásai is!), és **minden mai vagy 70 éven belül elhunyt fordító fordítása**
    (Ovidius, Saint-Exupéry, Defoe, görög mítoszok, modern Biblia-fordítások). Bibliai szöveg csak
    Károli Gáspár 1590-es fordításából idézhető, egyébként saját összefoglaló, leíró keretben.
  - A **népköltészet** közkincs, de a szöveg csak közkincs **gyűjtésből vagy kiadásból** vehető át
    (pl. Arany László, Benedek Elek, Kriza János) – a gyűjtő † éve a forrásmegjegyzésben.
  - A szöveget **két független kiadásból** vesd össze (pl. MEK + Wikisource), az eltérést a
    megjegyzésben jelezd. Emlékezetből soha ne idézz.
  - Filmet, rajzfilmet, előadást, illusztrációt (Jankovics, Fábri, Várkonyi stb.) csak címmel
    említs. Kép csak saját canvas-rajz; közkincs festmény legfeljebb hivatkozásként. Térkép: a
    `shared/tort/` adatai; utcatérkép csak saját, „vázlatos” bélyegű rajz (OSM-adat nem: ODbL).
- **A szöveg hűsége.** Az idézet a forráskiadás írásmódjával marad (*Kukoricza*, *Taljánország*,
  *kislyány*): ne modernizáld, ne „javítsd”; zavaró régi írásmódnál „régi írásmód” bélyeg (felirat).
  Versszakot ne rövidíts kipontozás nélkül; kihagyás: „[…]”. A szótagszám-eltérést ne simítsd el:
  mutasd meg, és mondd ki, hogy a költő nem gép.
- **Helyesírás:** *A magyar helyesírás szabályai* (AkH.), 12. kiadás (2015) – vagy az épp érvényes
  (gyártás előtt ellenőrizd); vitás esetben a HUN-REN NYTI helyesírási portálja. Szabályt a
  pontszámával idézz a `.md` megjegyzésében (`<!-- AkH. 12. § … -->`). Kiejtés szögletes zárójelben,
  a betűk szerint ([kúdba]), IPA-jelek nélkül (a build figyelmeztet).
- **Nyelvtani rendszer.** A szófaji csoportosítás, a magánhangzók besorolása, a szóelemek neve
  tankönyvenként eltér: a lecke a briefben megadott rendszert követi, a `.md` megjegyzése rögzíti,
  és a panel egyszer kimondja: „Más tankönyvben ezt másképp is csoportosíthatják.” A modul nem ragoz
  és nem elemez szabadon: minden alakot, szóelemzést és kivételt a `.md` ad meg (`morph`, `pron`).
- **Nyelvi sokszínűség.** A köznyelvi normát mutatjuk be, de a nyelvjárás, a természetes kiejtés
  és a beszélt nyelv nem „hiba”: „helytelen” helyett „a köznyelvben / a helyesírásban így írjuk”.
  Nyelvjárást, beszédhibát, akcentust nem teszünk nevetségessé. Kitalált szót (pl. `07`) egy második
  ember nézzen át (ne hasonlítson durva, csúfolódó vagy létező szóra).
- **Értelmezési sokszínűség.** Ami értelmezés (rejtett üzenet, szerkezeti besorolás, motívum
  jelentése), az `> értelmezés:` dobozban vagy „egy lehetséges olvasat” felirattal jelenik meg;
  tényként csak a szövegből ellenőrizhető állítás. Ne írd: „a költő ezt akarta mondani”. Értelmező
  feladatnál a gép **nem pontoz** hibának egy eltérő, de védhető választ: összeveti a `.md`
  olvasatával, és kérdést tesz fel. Minden irodalomleckében van nyitott kérdés („Te hogyan döntenél?”).
- **Irodalom és történelem.** Történeti eseményhez kötődő műnél (*Egri csillagok*, *Toldi*, *A walesi
  bárdok*, *Himnusz*) válaszd el a regényt/mondát a történeti ténytől (a 11. fejezet „forrás /
  rekonstrukció / monda” jelöléseivel), és hivatkozz a történelemleckére (`leckek/tortenelem-5-6/16-eger`),
  ne ismételd meg. Háború, halál, kegyetlenség jelzésszerű: nincs vér, nincs égő alak; a veszteséget
  szöveg és csend mutatja. Nemzeti jelképet (Himnusz, Szózat) nem teszünk játékká, és nem torzítunk.
- **Hang.** Csak a `MagHang` modulon át: szintetizált dallam, magánhangzó, zörej, kopogás. Nincs
  felvett emberi hang, gépi felolvasás (TTS), más szerző zenéje. A hang csak kattintásra indul (▶),
  mérsékelt hangerővel; az `AudioContext` is csak a kattintáskor jön létre. **A lecke hang nélkül is
  teljes** (dallamvonal, szótagpötty, kopogássáv). A QA hangpróbája: kattintás nélkül létrehozott
  `AudioContext` → `!`, kattintás nélkül induló hang vagy `speechSynthesis` → `✗`.
- **Glifek.** A QA magyarleckében glifpróbát futtat (ő ű ‚ ’ „ ” – — ∪ × [ ] mind a négy
  fontváltozatban), és a vászon/panel minden jelét a fontfájl tényleges tartalma szerint is nézi
  („tartalékfontra esik” → cseréld a jelet). A rövid szótag jele a ∪ (U+222A), nem a ⏑ vagy a ˘.
- **Színkódok** (minden leckében egységesek):
  | mit | szín |
  |---|---|
  | tő | tinta `#1c2440` keret, kártya-kitöltés |
  | képző | kékeszöld `#0a6f86` |
  | jel | okker `#8f5a0c` |
  | rag | cinóber `#c8401c` |
  | kötőhangzó | halvány tinta `#565d72`, kisebb betű |
  | rímpárok | a: cinóber · b: kékeszöld · c: okker · d: lila `#7b4fa0` |
  | magas / mély hangrend | kékeszöld / okker (vegyes: mindkettő csíkban) |
  | szófajok (a szó aláhúzása) | ige `#c8401c` · főnév `#0a6f86` · melléknév `#7b4fa0` · számnév `#8f5a0c` · határozószó `#2a4d9b` · névmás `#6b6a12` · igenév: az ige színe szaggatva · viszonyszó, mondatszó `#565d72` |
  A szóelemek kitöltött csempék, a szófajok aláhúzások. A rímszín a sorvég utolsó magánhangzójától a
  sor végéig tart (`L.quoteDat(k).v` utolsó eleme).
- **Verssor a vásznon:** legalább 26 px, a szótagpötty és az ütemjel felirata legalább 22 px; hosszú
  sornál mindig `max`. Ha egy versszak nem fér ki, lapozz versszakonként, ne kicsinyíts. Sort ne
  törj két képernyősorra jelölés nélkül (ha kell: behúzott folytatás + „↩”).
- **Új közös modulok leckén belül:** a `MagText`, `MagMorph`, `MagVers`, `MagHang` és `MagStory`
  (terv 4. fejezet) először a referencialeckében készül, külön blokkban
  (`/* ── MODUL: Verstan (MagVers) · forrás: magyar-5-6/10-janos-vitez-vers, <dátum> ── */ … /* ── MODUL VÉGE ── */`),
  `Mag…` névtérrel és API-leírással (16. fejezet). A történelemmodulokat (TortMap, TortGlobe,
  TortTimeline, TortSource, TortCards, TortScene) bájtra azonosan vedd át a legfrissebb leckéből.
- **Minden `.md`** végén `<!-- Vitatott / bizonytalan pontok: … -->` blokk a tanári review-hoz: a
  szövegforrás(ok) és eltéréseik, a választott tankönyvi rendszer, az értelmezésként jelölt
  állítások, a kitalált szavak listája (ha van).

## 19. Digitális kultúra-kiegészítés (5–6. évfolyam)

Digitális kultúra-leckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:**
`pilot/digitalis-kultura-5-6/terv.md` – a saját briefed (3. fejezet), a modulok API-vázlata (4. fejezet).
A 17. fejezet (Természettudomány) „Tippelj!”-pontja és nyelvi pontja itt is érvényes, az alábbi
eltérésekkel.

- **Mappa, fejléc:** `leckek/digitalis-kultura-5-6/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>`.
  Spec: `"maxWords": 45`; valódi adatnál `"sources": true`; a 06, 15, 16 leckében
  `"review": ["online biztonság"]`. A slug az egész repóban egyedi (a QA-mappa `build/qa/<slug>/`).
- **Fogalom, nem kezelés.** A lecke nem szoftverkezelési útmutató: nincs menüút, gyorsbillentyű,
  valódi program vagy weboldal képernyőképe, logója. A vászon a mögöttes működést mutatja (réteg, szám,
  csomag, próbálkozás); a valódi programra a `> megjegyzés:` egy mondattal utal („az órán használt
  programban ezt a … beállításnál találod” – programnév nélkül).
- **Nyelv 10–12 éveseknek.** Rövid mondatok, tegező hang, új fogalom **félkövéren**, egy mondattal. A
  kerettanterv szavait használjuk (fájl, mappa, felhőszolgáltatás, blokkprogramozás, prezentáció,
  rasztergrafika); angol szakszó csak a megjegyzésben, egyszer, zárójelben. Gépre, robotra nem
  mondunk emberi igét: a robot nem „lát”, „gondolkodik”, „akar” – **érzékel, mér, a program szerint
  dönt**; a kereső nem „tudja” – **keres, sorba rendez**.
- **„Tippelj!” → kipróbálom → magyarázat.** Minden leckében legalább egy jóslat a futtatás előtt, a
  TtTipp modullal (17. fejezet). Programleckében a tipp jellemzően: „mit rajzol / hová kerül / kijut-e”.
  QA: `__qaStates` `tipp-jó` és `tipp-rossz`.
- **Blokknyelv (DigBlock).** Saját vizuális nyelv: papír alapú blokk tinta szöveggel, bal oldalt
  kategóriasáv rajzolt ikonnal, a tartalmazó blokk behúzással, kategóriaszínű sínnel és „… vége” záró
  sávval. **Tilos:** a Scratch (vagy más környezet) neve a vásznon és a panelen, macskája, kirakós-fülei,
  kategóriaszínei, fehér betű színes blokkon. A blokkfelirat magyar felszólító ige a `.md`-ből
  (`<op> blokk` kulcs, `#` a paraméterhely). Ugyanaz a program mindenhol ugyanúgy néz ki: lecke-saját
  blokkrajz nincs.
- **Determinisztikus futás.** A program nyomvonalát (`DigBlock.run`, `DigRobot.motor`) a lecke a
  programból és a világból számolja ki egyszer, és **az időből** rajzol (`R.at(t)`, a futás órája
  `L.st`-ből – `DigBlock.clock`). Nincs képkockánként halmozott állapot, nincs `Math.random` (csak
  seedelt `U.rng`). Minden futás léptethető („egy lépés”), és van lépéskorlát (végtelen ciklusnál
  „végtelen ciklus?” jelzés, nem lefagyás). A futó blokk cinóber keretet kap, a feltétel kiírja: IGAZ /
  HAMIS. A lépés `enter()`-je visszaállítja a lépés alapprogramját (a diák módosítása nem viszi át a
  következő lépésre). QA-állapotok: `fut-közben`, `fut-vége`, és ahol van: `hibás-program`, `töréspont`,
  `korlát`.
- **A robot (DigRobot).** Felülnézeti, műszaki rajz: kör test, két kerék, irányjelző ék, a szenzorok a
  helyükön. **Nincs arc, szem, mosoly**, és az ultrahangos szenzor sem két kör („szem”). Ütközés:
  stilizált koccanás, semmi nem törik. A szimuláció „modell” bélyeget kap, és a panel egyszer kimondja,
  mit hagy el (súrlódás, akkumulátor, kerékcsúszás).
- **Online biztonság és etika (05, 06, 15, 16, és ahol előkerül).**
  - **Hangnem:** tájékoztat, nem ijesztget. Nincs sötét alak, figyelő szem, „ragadozó”, „hacker” mint
    figura, áldozatot hibáztató mondat. A veszély a másolhatóság, az összerakhatóság és a próbálgatás –
    nem egy gonosz szereplő.
  - **Segítségkérés:** ahol zaklatás, gyanús üzenet vagy kellemetlen tartalom előkerül, ott egy mondat:
    „Szólj egy felnőttnek, akiben megbízol.” A 15-ös leckében a Kék Vonal (116-111) is – a szám
    érvényességét gyártáskor ellenőrizd, és írd a forrást a megjegyzésbe. A szemlélőt is megszólítjuk
    („ne továbbítsd, szólj”).
  - **Zaklatás ábrázolása:** a bántó üzenet szövege nem jelenik meg – elmosott buborék (`DigUI.blurMsg`).
  - **Kitalált világ:** személy csak kitalált keresztnévvel és monogramos körrel (nincs arc, fotó);
    webcím csak `.example` (RFC 2606); IP-cím csak 192.0.2.x, 198.51.100.x, 203.0.113.x (RFC 5737);
    e-mail-cím csak `…@pelda.example`; telefonszám csak a 112 és a 116-111. Valódi cég, termék, közösségi
    oldal, kereső neve, logója, színvilága a vásznon nem jelenik meg; a tanári megjegyzésben csak
    forrásként, semlegesen.
  - **Jelszó:** a lecke soha nem mutat valódi, ismert vagy gyakori jelszót (a „123456”-típusú listát
    sem – az legfeljebb a tanári megjegyzésben). A példajelszó generált (seedelt), mellette a felirat:
    „ezt ne használd – mostantól nem titok”. Beviteli mező nincs: a jelszó csempékből épül. A
    próbálgatási sebesség „modell” bélyegű, nagyságrendi forrással.
  - **Álhír, keresés:** csak kitalált, ártalmatlan, iskolai témájú példa; nincs valódi hír, médium,
    közszereplő, politikai, egészségügyi vagy vallási téma. A terjesztőt nem minősítjük („hazug”,
    „buta”).
  - **Életkor, jog:** korhatárt (GDPR, szolgáltatói szabály) csak forrással, „szolgáltatónként eltér”
    kitétellel. Jogi tanácsot a lecke nem ad.
- **Szerzői jog.** Minden kép saját canvas-rajz; valódi fotó, képernyőkép, ikonkészlet nincs. Fontok: csak
  a projekt három fontja (a „talpas / talpatlan / egyenlő szélességű” bemutatása is ezekkel). Hang: csak
  szintetizált, a MagHang szabályai szerint (18. fejezet „Hang” pontja: csak kattintásra, mérsékelten,
  hang nélkül is teljes; az `AudioContext` csak a kattintáskor jön létre). Zene, felvett hang nincs. Ha a
  lecke a szerzői jogról szól (11), a példa forrásai kitaláltak.
- **Ikonok és jelek.** Minden ikon (▶, szünet, lakat, kuka, mappa, pipa, X, ¶, ·, →) **rajzolt útvonal**,
  nem Unicode-jel vagy emoji – a három fontban nincsenek benne, tartalékfontra esnének. Emoji sehol.
- **Számok, egységek.** 1 kB = 1000 bájt (SI); az 1024-es váltás (KiB) csak a megjegyzésben. A „bit” és a
  „bájt” kiírva; kB, MB, GB, TB nagy B-vel, a „k” kicsi. Nagy szám: hatványalak és szó („2,2 · 10¹⁴ –
  218 billió”, `DigBit.big`; hosszú skála: billió = 10¹²). Számolt érték (kombinációk, fájlméret, idő)
  mindig a kódból jön a `.md` alapadataiból (jelkészlet, sebesség, felbontás) – kézzel kiírt eredmény
  nincs (9. fejezet). A modellsebesség és a kitalált adat bélyeget kap.
- **Színkódok** (minden leckében egységesek):
  | mit | szín |
  |---|---|
  | blokk: esemény | tinta `#1c2440` |
  | blokk: mozgás | kékeszöld `#0a6f86` |
  | blokk: toll | lila `#7b4fa0` |
  | blokk: vezérlés (ciklus, elágazás, várj) | okker `#8f5a0c` |
  | blokk: érzékelés | kék `#2a4d9b` |
  | blokk: adat (változó) | olíva `#6b6a12` |
  | blokk: művelet | halvány tinta `#565d72` |
  | blokk: kimenet, bemenet (mondd, kérdezd) | bordó `#8a2f5b` |
  | blokk: saját (lecke-definiált lépés) | tinta keret, okker sáv halványan |
  | futó blokk, „a te tipped”, hiba | cinóber `#c8401c` |
  | IGAZ / HAMIS | kékeszöld / halvány tinta |
  | RGB-csatornák | vörös `#c62828` · zöld `#2e7d32` · kék `#1e5bc6` |
  | aktív / passzív lábnyom (15) | cinóber / kékeszöld |
- **Kapcsolódás.** Ha a téma más sorozatban megvan (fizika-7-8/12 hang, 13 színek; matematika-5-6/02 kettes
  számrendszer; matematika-9-10/03 fa-diagram; magyar-5-6/01 kommunikáció), ugyanaz a szám ugyanaz
  (pl. a hangsebesség 343 m/s), és a `> megjegyzés:` egy mondatban hivatkozik. A 7–8. évfolyamos
  folytatást („eljárás”, „vektorgrafika csomópontjai”, „tömörítés”) csak megnevezzük.
- **Modulok:** a `DigBlock` és a `DigRobot` (ref. `02-ciklus`; a DigRobot v1.1 szenzorai: `07-szenzor`), a
  `DigDoc` (ref. `10-formazas`), a `DigPixel` (ref. `13-pixel`), a `DigBit` (ref. `17-szamitogep`) és a
  `DigUI` (ref. `15-labnyom`) a 16. fejezet szerint, a terv 4.2 pontjának API-jával. A blokkhatár
  egységesen `/* ── MODUL: <név> (<Névtér>) · forrás: digitalis-kultura-5-6/NN-slug, <dátum> ── */` …
  `/* ── MODUL VÉGE: <név> ── */`. A többi modult (terv 4.1: TtTipp, MatGraf, TortCards, TortTimeline,
  TortMap, MagText, MagHang, BioPlot) bájtra azonosan vedd át, az ott megadott md5-tel ellenőrizve.
- **Minden `.md`** végén `<!-- Tanári megjegyzések és források: … -->` blokk: kitalált példák és
  személyek, modell-egyszerűsítések (a robot, a próbálgató gép, a kereső pontozása), a bizonytalan számok
  forrása és bizonytalansága, és az, hogy a lecke blokknyelve miben tér el az órán használt
  környezettől. A 06, 15, 16 leckében ezen felül `<!-- Szakmai ellenőrzés: <szerep>, <dátum> -->` (név
  nélkül).

## 20. Történelem-kiegészítés (7–8. évfolyam)

Történelemleckénél a 7–8. évfolyamon a fenti szabályok, a 11. fejezet (Történelem 5–6.) és ezek együtt érvényesek.
**Kötelező olvasmány:** `pilot/tortenelem-7-8/terv.md` – a 0. fejezet (döntések), az 1.3 pont (szerkesztői elvek),
a saját briefed (3. fejezet) és a modulok API-vázlata (4. fejezet).

- **Mappa, fejléc:** `leckek/tortenelem-7-8/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Történelem · évfolyam: 7–8. · témakör: N. <a kerettanterv témakörének címe>`.
- **Panel:** lépésenként ≤ 55 szó (alapérték, nincs `maxWords`), a cél 40–50 szó; új fogalom **félkövéren**, egy
  mondattal. Spec: `"sources": true` minden leckében.
- **Rétegek és bélyegek:** a 11. fejezet szerint (forrás / rekonstrukció / hagyomány; „vázlatos”, „illusztráció”,
  „becslés”), kiegészítve: „vitatott” (okker, mint a „becslés”) és „modell”, „kitalált” (halvány tinta). „Honnan
  tudjuk?” minden leckében – a 20. századnál a statisztika forráskritikájával is: ki számolt, milyen kategóriával
  (anyanyelv vagy nemzetiség, egy vagy több válasz), mit titkoltak, mikor javították.
- **Vitatott kérdések:** ahol a szakirodalom vitatkozik (áldozatszám, létszám, felelősség megoszlása), a lecke
  **tartományt és legalább két forrást** mutat (`range`, „kb.”, „(becslés)”, „vitatott” bélyeg), és értékítélet
  helyett forrást, adatot, kérdést ad. Az értékelő fejlesztési feladatokat („Ítélet megfogalmazása…”, „Vélemény
  megfogalmazása…”) a lecke kérdésként adja a tanárnak (`> megjegyzés:` vagy záró kérdés), a vásznon tény áll. A
  népirtás és a háborús bűn ténye nem vita tárgya. A `.md` végén a `<!-- Vitatott / bizonytalan pontok: … -->` blokk
  kötelező (11. fejezet), forrással és a bizonytalanság mértékével.
- **Felelősség pontos alanya:** „a náci Németország”, „az SS”, „a magyar kormány”, „a csendőrség”, „a szovjet
  hadsereg”, „az NKVD” – nem „a németek”, „a magyarok”, „az oroszok”. Kollektív bűnösséget egyik irányban sem
  sugallunk (kitelepítések, Beneš-dekrétumok, délvidéki megtorlások – ugyanazzal a mércével).
- **Semlegesség:** pártpolitikai semlegesség, különösen 1990 után. Élő politikust nem értékelünk. 1990 után csak
  intézmény, alkotmányos működés és adat; kormányfő, köztársasági elnök neve csak tényszerű címkeként (név, hivatali
  idő). Valódi választási eredmény **szürke árnyalatokban**, a pártok mai színei és logói nélkül; a választási
  kalkulátor kitalált pártokkal („A párt” …), egy színárnyalat tónusaival és mintázattal. A rendszerváltás
  idővonala 2004-gyel zárul; utána legfeljebb a választások évei név nélkül.
- **Holokauszt, népirtás, háborús áldozatok: méltóság, nincs játékosítás.** Nincs pontszám, nincs „Tippelj!”
  áldozatszámra (a 08-ban csak forráskritikai kérdés), nincs látványos robbanás vagy villanás, nincs csúszka,
  amely áldozatszámot „lejátszik”, nincs animált halottszámláló, nincs vér, nincs kitalált áldozati történet,
  nincs hangeffektus. Az áldozatszám mindig forrással és tartománnyal áll; a térképes folyamat (deportálás)
  gombnyomásra, lassan, lépésenként halad. Áldozatot és embermentőt csak dokumentált forrásból, névvel és hellyel
  mutatunk. Ezek a leckék (08, és ahol a brief jelzi) **szakmai lektort kérnek**: spec `"review": ["történész",
  "emlékezetpedagógus"]` (08) vagy `"review": ["történész"]` (04, 05, 07, 10, 11, 13, 14) → a `.md` végén
  `<!-- Szakmai ellenőrzés: <szerep>, <dátum>, <ajánlás verziója> -->` (név nélkül); amíg nincs lektorálva:
  „dátum: –, (még nincs lektorálva)”.
- **Trianon:** tényadat forrással – terület, népesség, az 1910-es népszámlálás anyanyelvi adata, az utódállamok
  népszámlálása mellette (a KSH és a terv 04-es briefje szerinti számokkal). A győztesek és az utódállamok érvei
  és a magyar érvek egyaránt, azonos hangsúllyal. Sem revizionista, sem lekicsinylő hangnem. A szerződés neve a
  vásznon „trianoni békeszerződés”; a kerettanterv „békediktátum” kifejezését a lecke magyarázza (miért nevezi így a
  magyar szóhasználat). Az anyanyelvi adat mellett a forráskritika: anyanyelv ≠ nemzetiség, asszimilációs nyomás,
  a zsidóság magyar anyanyelvűként számolva.
- **Szerzői jog:** szó szerint csak közkincs szöveg idézhető – a szerző (és a fordító) legalább 70 éve halt meg,
  vagy hivatalos jogszabály- és szerződésszöveg (`### Idézet` + `<!-- idézet: … · szerző † <év> · közkincs -->`;
  jogszabálynál † nélkül; a build elutasítja, ha † + 70 ≥ az idei év). Közkincs eredeti, de nem közkincs fordítás
  esetén **saját fordítás**, így jelölve. Élő vagy 70 évnél frissebben elhunyt szerzőtől (pl. Churchill, Kádár
  János, Márton Áron, a DEGOB-jegyzőkönyvek, a kortárs visszaemlékezések) legfeljebb egy-két mondatos idézet a
  TortSource kártyán forrással, inkább **parafrázis** – nem `### Idézet` blokkban. Fotó, plakát, karikatúra,
  festmény, bankjegykép, térképlap nem kerül be; minden vizuál saját rajz. **Önkényuralmi jelkép**
  (horogkereszt, nyilaskereszt, sarló-kalapács, ötágú vörös csillag) nem rajzolódik ki: a szöveg megnevezi, a
  vásznon semleges „jelkép” helyőrző áll. Személyről nincs „hiteles” portré: sziluett vagy névkártya.
- **Térképek, határok:** történeti határ **csak** a `shared/tort/map-torthatar.js` (`TORT_HATAR`) csoportjaiból
  (TortTerr) vagy kézzel rajzolt, „vázlatos” bélyegű, dátumozott foltként/vonalként. A `TORT_HATAR` a Natural
  Earth (közkincs) mai közigazgatási egységeinek uniója és kézi vágóvonalak; minden csoportja vázlatos, a `notes`
  mezője megmondja, miben tér el. Európa-alaptérkép: `shared/tort/map-europa.js`. A hivatalos **területet és
  népességet** mindig az `### Adatok`-ból mutasd, soha ne a sokszögből számold. Frontvonal: a lecke kódjában
  kulcskockák (geometria), a dátumuk az `### Adatok` alatt; „vázlatos”, a `.md` megjegyzése felsorolja a
  felhasznált atlaszokat (csak egybevetés, onnan geometriát nem veszünk át). A HistoGIS, a CShapes, a tankönyvi
  atlaszok, az OSM és más térképszolgáltatások geometriája nem kerülhet a leckébe. Mai határ csak halvány,
  kikapcsolható, „mai határok” feliratú réteg; mai korszakról szóló térképen (EU, népszámlálás 2021–22) a mai
  országhatár a fő réteg. Helynév: a korabeli magyar név, első említéskor a mai hivatalos névvel (Kassa – ma
  Košice).
- **Számformátum magyarul:** tizedesvessző (54,5 %), valódi mínuszjel (−46 %), ezres tagolás nem törő szóközzel
  (437 402 – a build `U+202F`-et tesz), dátum „1944. március 19.”, tartomány nagygondolatjellel („500–565 ezer”),
  pénz „12 500 korona”, nagy szám szorzószóval („2,5 millió”); hatványalak (10²⁹) csak logaritmikus tengelyen és a
  `06-pengo` hiperinflációs lépéseiben. A számot az `L.val(k)` / `U.fmt` adja, kézzel formázott szám nincs a
  kódban.
- **Színek:** a 11. fejezet semleges oldalszínei (indigó `#3b4590`, szilva `#7d3a66`) háborús feleknél és
  tömböknél; nincs „jó” zöld és „rossz” piros. Pártállami „irányít” kapcsolat: bordó `#8a2f5b`; demokratikus
  ellenőrzés: kékeszöld `#0a6f86`. A 08-ban tompa paletta: tinta, papír, a forrás kékeszöldje, halvány okker.
- **Modulok:** a **TortTerr** (ref. `07-masodik-vilaghaboru`), a **TortCity** (ref. `02-dualizmus`), a **TortParl**
  és a **TortState** (ref. `16-demokracia`) a 16. fejezet szerint, a terv 4.2 pontjának API-jával; blokkhatár
  `/* ── MODUL: <név> (<Névtér>) · forrás: tortenelem-7-8/NN-slug, <dátum> ── */` … `/* ── MODUL VÉGE: <név> ── */`.
  A többi modult (terv 4.1: TtTipp, TortMap, TortTimeline, TortSource, TortCards, TortScene, TortGlobe, FoldChoro,
  FoldChart, MatChart, BioPlot) **bájtra azonosan** vedd át, az ott megadott md5-tel ellenőrizve; a TortSource
  `50d3c6fd…`/`134cb7b3…` és a TortCards `c2a85a56…` változata nem használható. A `shared/tort/` adatfájljait a
  leckeügynök nem módosítja (hiba vagy hiány: jelentés).
- **Kapcsolódás.** Ha a szám más leckében is szerepel (`foldrajz-9-10/10-nepesseg`, `14-penz`; a sorozaton belül
  04 ↔ 07 ↔ 14, 10 ↔ 14, 07 ↔ 08), ugyanaz a szám ugyanazzal a forrással áll, és a `> megjegyzés:` egy mondatban
  hivatkozik.
- **Kész, ha** (a 10. fejezeten felül): [ ] minden szám, dátum, helyszín az `### Adatok` alatt, forrással;
  [ ] bizonytalan szám tartománnyal és jelöléssel; [ ] van „Honnan tudjuk?” lépés; [ ] érzékeny tartalomnál nincs
  pontszám, áldozatszám-tipp, effektus, csúszka áldozatszámon; [ ] nincs önkényuralmi jelkép, fotó, plakát; [ ] a
  szó szerinti idézet közkincs vagy jogszabály; [ ] 1990 utáni tartalom intézmény és adat, szürke pártszínek;
  [ ] a történeti határ „vázlatos” és dátumozott; [ ] lektort kérő leckében ott a `Szakmai ellenőrzés` blokk.
