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
  fut: kezdőértéket közvetlenül az adatból (`L.num`) vegyen.
- Tartalom: `L.lab(k)` felirat · `L.num(k)` szám · `L.unit(k)` · `L.val(k, d?)` → „0,92 g/cm³”.
- Szöveg a vásznon: **csak `L.tx(s, x, y, o)` / `L.pill(s, x, y, o)`** – ezekből tudja a QA és a
  review mód, hol van felirat. `o`: `s` px, `w` vastagság, `f` (`F.D` Fraunces, `F.B` Bricolage,
  `F.M` JetBrains Mono), `i` dőlt, `a` igazítás, `b` alapvonal, `c` szín, `ls` betűköz,
  `max` (szélesség, fölötte kicsinyít), `k` md-kulcs vagy kulcslista, `qa: false` (szándékos
  átfedés, pl. képletjel a dobozban). `L.pill`: `bg`, `bd`, `pad`, `r` – a doboz a szöveghez méreteződik.
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
- Alsó index a panelen: `F_fel` → F<sub>fel</sub> (a build alakítja át; ne írj saját megoldást).

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
