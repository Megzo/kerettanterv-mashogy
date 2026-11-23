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
- Index, kitevő, képlet a panelen: `F_fel`, `x^2`, `` `x^2 - 4x + 3 = 0` ``, `[[a/b]]` – a build alakítja
  át (táblázat: `leckek/README.md` „Képlet, tört, kitevő…”); ne írj saját megoldást. A vásznon
  ugyanezt a jelölést a `MatText.draw` szedi (`shared/matek/mtext.js`, 12. fejezet).

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
- A QA ezeket is nézi (`!` = figyelmeztetés, nem rontja a kilépési kódot): a fontokból hiányzó
  karakter (glif), 300 ms-nál lassabb `enter()`, matekleckében tizedespont/kötőjel-mínusz a
  vásznon. Kapcsolók: `--det` (determinizmus: ugyanannál az `L.st`-nél oda-vissza léptetve
  ugyanaz a kép?), `--states` (`window.__qaStates = {3: [{name: 'min', set(L) {…}}]}` – szélső
  állapotok fotója), `--poke '{…}'` (a lecke `L.poke(o)`-ja), `--data` (az adatok listája).
  Ha a lecke ad `L.checks()` függvényt (→ `[{name, ok, got, want}]`), minden képnél lefut.

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
  `NN ZZ QQ RR` → ℕ ℤ ℚ ℝ, `√(…)`/`gyök(…)`, a betűk dőltek, `sin lg log max…` állók);
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
  változhat.
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
