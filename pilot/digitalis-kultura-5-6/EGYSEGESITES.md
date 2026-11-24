# Digitális kultúra 5–6. – egységesítő és javítókör (2026-11-24)

Cél: a sorozat DK-moduljainak (DigBit, DigDoc) a metrikasorokban jelzett hibáit a modulban javítani,
az új változatot bájtra azonosan minden használó leckébe másolni, és a leckékben a kerülőutakat
egyszerűsíteni. A DigBlock/DigRobot blokkokhoz (v1.1, a 01–04, 07, 09-ben bájtra azonosak) ez a kör
nem nyúlt; a `08-vonalkoveto` párhuzamosan készül, ezt a leckét a kör nem írta.

Az md5 a blokkra vonatkozik: a `/* ── MODUL: … (Név)` sortól a `/* ── MODUL VÉGE: Név ── */` sor
végéig, záró újsor nélkül.

## 1. DigBit v1.1 (referencia: `17-szamitogep.html`)

| lecke | sorok | md5 |
|---|---|---|
| 05-csomagok | 1074–1324 | `d0c04117765277012eddb23ad3dcec6b` |
| 06-jelszo | 696–946 | `d0c04117765277012eddb23ad3dcec6b` |
| 13-pixel | 377–627 | `d0c04117765277012eddb23ad3dcec6b` |
| 14-hang-video | 379–629 | `d0c04117765277012eddb23ad3dcec6b` |
| 17-szamitogep (ref.) | 840–1090 | `d0c04117765277012eddb23ad3dcec6b` |

(v1.0: `ef03f6107042ae34954d7dc5211aa884`.) Változások (a blokk fejében változásnapló):

- **`big`: kerekítés 10⁶ alatt.** Megadott `o.sig` mellett 10⁶ (`o.ezer`: 10⁴) alatt is értékes
  jegyre kerekít (1707, `sig: 2` → „1700”). `o.sig` nélkül a régi, pontos szöveg marad
  (a 06 a pontos lehetőségszámot `sig` nélkül kéri: „456 976”).
- **`big`: kitevő felső indexszel.** 10³³ fölött „2,9 · 10³⁹” (Unicode felső index – ugyanez a
  build sima szöveges alakja, `tools/build_lesson.py` `SUP_OUT`; a jelek mindhárom fontcsaládban
  megvannak, `shared/fonts/README.md` 2. pont, próbaoldalon mindhárom fonttal ellenőrizve).
  v1.0: „2,9 · 10^39” (kalap). Új mező: `sci` (true, ha hatványalakú).
- Node-próba: 1707 → „1700” (sig 2) / „1707”; 456 976 → „456 976” / „457 000” (sig 3);
  17 345 → „17 ezer” (ezer, sig 2); 2,9 · 10³⁹ → „2,9 · 10³⁹”, sci; 999,6 milliárd → „1 billió”.

Lecke-oldali egyszerűsítés (06-jelszo):

- `timeStr`: a „10⁶ év alatt saját kerekítés” ág helyett 1000 év fölött `DigBit.big(y, {sig: 2})`
  (a kiírt szöveg változatlan: „1700 év”, „17 000 év”, „92 trilliárd év”). A soha nem ható
  `ezer: true` kikerült (a kiírás így azonos maradt a korábbival).
- a hatványalak felismerése `!bs.includes('^')` helyett `!DigBit.big(N).sci`.

## 2. DigDoc v1.1 (referencia: `10-formazas.html`)

| lecke | sorok | md5 |
|---|---|---|
| 10-formazas (ref.) | 425–1168 | `2d8e4b654f53b79f0206112dc4732fda` |
| 11-dokumentum | 752–1495 | `2d8e4b654f53b79f0206112dc4732fda` |
| 12-bemutato | 415–1158 | `2d8e4b654f53b79f0206112dc4732fda` |

(v1.0: `d53cad83110e7e772476d6f6a7df23dc`.) Változások:

- **`D.drag`:** a `keepRatio` csak a sarokfogóra hat; az oldalfogó mindig torzít (az API-leírás
  szerint; v1.0-ban az oldalfogó is arányos volt). Kipróbálva a 11 1. lépésében egérhúzással:
  oldalfogó 126 × 84 → 79 × 84 mm (torzul), sarokfogó utána 79 × 84 → 98 × 104 mm (arányos).
- **`D.draw`:** a tördelés az alfa-kilépés előtt fut, így láthatatlan rajz után is érvényes a
  `D.lines`/`D.pbox` – a `DigDoc.slide` `parts`-a `a ≤ 0,005` mellett sem üres.
- **`DigDoc.slide`:** `x`, `y` alapértéke 0 (v1.0: NaN); új `paras: [{s, k, b, col, bullet}]`
  (bekezdések a cím és a felsorolás között, id-k: `p0`, `p1`, …); a háttér és a kép csak látható
  alfánál rajzol. Próbaoldalon: x/y nélkül nincs NaN, a `parts` kulcsai `cím, p0, p1, b0, b1`,
  `a: 0` mellett `cím, b0, kép`.
- **`DigDoc.blurAt`:** a sugár és a felbontás kapcsolata leírva (a kép r/1,1 px-es cellákra
  kicsinyül: N = 1,1 · w / r feloldható részlet); új `o.n` – ennyi részlet maradjon feloldható
  (felülírja az `o.r`-t).
- **layout `o.hyph`** (a 11 metrikasorából): a visszahívás mindig az egész szót kapja (v1.0-ban a
  sortörés utáni maradékot is, pl. „útállomáson”), és az indexek a feltételes elválasztójel nélküli
  szóra vonatkoznak (v1.0-ban a jellel együtt értelmezte). A 11 5. lépésének tördelése képen
  ellenőrizve (vasút-|állomáson, talál-|koztunk, Fent-|ről, völ-|gyet).

Lecke-oldali egyszerűsítés:

- 11-dokumentum: a lenyomáskori `img.keepRatio = (part === 'kép-sarok')` kerülőút törölve.
- 12-bemutato: a `blurAt` hívás `r: 1,1 · w / N` helyett `n: viewN(d)`-t ad. A `mkSlide`/`fitPt`
  marad (a dia rajz nélküli tördelésével keresi a legnagyobb elférő betűméretet, és más léptékben is
  rajzol – ezt a `slide` nem tudja); a fejkommentje frissítve. A `R.parts[g]` ellenőrzése maradt
  (biztonsági, nem kerülőút).

## 3. 07-szenzor, 6. (és 7.) lépés: a távolság-görbe vágása

`plotRun` (a BioPlot-blokkon kívül): a `PL.line` hívás a rajzterületre (`PL.box`) vágott
`ctx.save/clip/restore`-ban fut. A „nincs visszhang” (400 cm) és a forduláskori ugrás így pontosan a
100-as felső rácsvonalnál ér véget (a BioPlot saját vágása 2 px-cel tágabb, a görbe 105-ig volt
számolva), nem fut a tengelycímbe. Képen ellenőrizve: 06-settle, -gyors-10, -küszöb-5, -zaj,
07-settle. A párhuzamosan készülő 08-vonalkoveto (szintén BioPlot-idősor) ugyanezzel a mintával vághat.

## 4. A többi metrikasor DK-modulos megjegyzése

| hol | mi | döntés |
|---|---|---|
| 16-alhir | `DigUI.para` `o.a` = igazítás, nem alfa | API-kérdés, nem hiba: a javítás minden hívót érintene → marad (a doksi helyes) |
| 17-szamitogep | `DigBit.ladder` szorzója a magasabb fok bal alsó sarkában | szándékos (a fokhatáron átfedett), a doksi írja → marad |
| 11-dokumentum | `hyph` maradékra / feltételes elválasztójeles index | javítva (DigDoc v1.1, fent) |
| 13, 14, 15 | DigPixel, DigUI | hibát nem jeleztek |

Közös (nem DK-) modulok – csak leírva, nem javítva:

- **BioPlot** (07, 14): az alfát szorozza (hívás előtt `globalAlpha`/`al(1)`); a görbe vágása 2 px-cel
  tágabb a rajzterületnél (07: a lecke vág).
- **TortCards** (11, 15, 16): a `draw` szorozza az alfát – előtte `al(1)`.
- **TortProj.equalEarth** (05): `lon0 ≠ 0` mellett a varraton átnyúló sokszög vízszintes csíkot húz.
- **TortTimeline** (05): a kártyákat a hívónak kell sor szerint csökkenő sorrendbe rendeznie.
- **TortMap** (05): a base a teljes vásznat tengerrel tölti – a lecke vág.
- **MatGraf.tree** (01): középponttól középpontig húzza az ágat (blokk-csúcsoknál átlós).
- **Motor/CSS** (03): a letiltott panelgomb nem látszik szürkének.

## 5. DigBlock / DigRobot – nyitott igények (a v1.1 után, ebben a körben nem nyúltunk hozzájuk)

A v1.1 már megoldotta: futtatható `def` törzs/eljárás, világ-megállás (`halt`), a hibafelirat helye
(`errAt`), azonnali programozott szerkesztés, a ciklusköri IGAZ/HAMIS törlése, `opClick`.
Nyitva:

1. **`E.paramBox(id, i)`** (09): a paraméterkapszula doboza a tippnyilakhoz (most `L.measure`-rel
   becsülve a blokk jobb széléről).
2. **`DigBlock.def` kategória-opció** (07, 09): a `def` a kategóriát 'saját'-ra állítja, a hívó
   utólag írja át ('mozgás', 'érzékelés'); `def({…, cat})` kellene.
3. **Rejtett paraméter** (09): a 'fordulj' fok-paraméterét a lecke a modulon kívül rejti
   (`BLOCKS['fordulj'].args[1].hide`) – hivatalos opció kellene.
4. **Értékadás időzítése** (04): a változó a frame **elején** kapja az új értéket, így lassú
   animációnál a változódoboz előre vált (a lecke igazítja).
5. **`kérdezd` frame** (04): a `val` a válasz; a kérdés szövegét nem tárolja.
6. **`watch`** (04): a végén `globalAlpha = 1`-et állít (nem állítja vissza a korábbit).
7. **ha-különben IGAZ/HAMIS jelzés** (04): széles feltételnél x ≈ 870-ig ér (elrendezési kényszer).
8. **DigRobot robotméret** (04): a test (r = 6 → 12 cm) kis alakzatot eltakar, nincs méretskálázás.
9. **DigRobot.fromProg** (07, 02 metrika): saját kiértékelője az 'érték' alakú sense-blokkot
   logikaivá alakítja (a DigBlock v1.1 már a nyers értéket adja).

## 6. QA

Mind a 9 módosított lecke (05, 06, 07, 10, 11, 12, 13, 14, 17) egyenként buildelve
(`tools/build_lesson.py`, a .md nem változott; a 06 egyetlen figyelmeztetése a hiányzó szakmai
lektorálási blokk, ez korábban is így volt), és a teljes QA lefutott:
`--back --states --det --at 1.5,settle` + ugrópróba – az eredmény leckénként az alábbi
táblázatban. Képen átnézve: 07 6–7. lépés (görbevágás), 06 4. lépés (`írásjel-20`: hatványalak,
„92 trilliárd év”), 11 1. lépés (egérhúzás oldal/sarok) és 5. lépés (elválasztás), 12 2. lépés
(elmosás `n`-nel) és 6. lépés (`parts`, szemmodell), DigBit/DigDoc próbaoldal.

| lecke | QA |
|---|---|
| 05-csomagok | ✓ 0 hiba, 0 figyelmeztetés; 27 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #9) ✓ |
| 06-jelszo | ✓ 0 hiba, 0 figyelmeztetés; 25 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #9) ✓ |
| 07-szenzor | ✓ 0 hiba, 0 figyelmeztetés; 26 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #8) ✓ |
| 10-formazas | ✓ 0 hiba, 0 figyelmeztetés; 24 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #9) ✓ |
| 11-dokumentum | ✓ 0 hiba, 0 figyelmeztetés; 23 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #8) ✓ |
| 12-bemutato | ✓ 0 hiba, 0 figyelmeztetés; 27 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #8) ✓ |
| 13-pixel | ✓ 0 hiba, 0 figyelmeztetés; 31 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #8) ✓ |
| 14-hang-video | ✓ 0 hiba, 0 figyelmeztetés; 24 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #8) ✓ |
| 17-szamitogep | ✓ 0 hiba, 0 figyelmeztetés; 28 állapot, --back, --det, --at 1.5,settle, ugrópróba (8 ugrás + #9) ✓ |

A DigUI (04, 05, 06, 15, 16: `f1db216d…`) és a DigPixel (13, 14, 16: `f273cb2f…`) blokkok változatlanok és
továbbra is bájtra azonosak (a 13, 14-ben a DigBit 10 sorral hosszabb lett, ezért a DigPixel sorszáma
eltolódott).

A módosított leckék metrikasora (05, 06, 07, 10, 11, 12, 13, 14, 17) egy „Egységesítés (2026-11-24)” mondattal
bővült (új md5, hivatkozás erre a fájlra); a sorok régi md5-jei a v1.0-ra vonatkoznak.
