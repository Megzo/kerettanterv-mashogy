# Természettudomány 5–6. – egységesítő és javítókör (2026-11-24)

A sorozat 16 kész leckéje (01–15, 17; a 16-folyo ekkor még készült, nem része a körnek) közös
„Tippelj!”- és bélyegkódja modullá vált, a TtMuszer dokumentációt és `o.abs` opciót kapott, és néhány
egyszerű, leckén belüli hiba javítva lett. Tartalmi (.md) változás nincs; a `.content.js` fájlok a
buildtől nem változtak.

## 1. TtTipp – „Tippelj!” és bélyegek (új közös modul)

**Előtte** három változat élt a sorozatban:

| változat | leckék | jellemző |
|---|---|---|
| 01-tocsa „A SOROZAT MINTÁI” (lecke-saját kód) | 01, 02, 04–09, 11–15, 17 | `stamp(kind, x, y, a, o)`, `Tip/tipReset/panelVeil/tipGuess/tipControls/tipU/rhythm/tipHead/tipFeedback`; a 02-ben `o.q2` nélkül, a 08-ban +1 bélyegfajta, a 17-ben `o.noRhythm` + `o.qv` bővítéssel; a leckék a `STAMP`-ot a blokkon kívül bővítették (nem méretarányos, sematikus, vázlatos, képzeletbeli) |
| 03-meres „TT-STÍLUS” | 03 | `stamp(kind, k, x, y, o)` ékezet nélküli fajtákkal, `tip = {keys, ok: index, pick}`, `tipRow` / `tipPick` / `tipVerdict` (dőlt szöveges visszajelzés), panel-elmosás nélkül |
| 10-erdo „közös logika” | 10 | `stamp(k, x, y, o)` kulccsal, egyetlen globális `TIP`, `tipButtons`, `blurPanel`, `tipBadge` (sarokjelvény), `yourTip` (keret a jelenet eleme körül); a tippgombok maradtak, `on` osztállyal |

**Most:** mind a 16 lecke a `/* ── MODUL: „Tippelj!” és bélyegek (TtTipp) … ── */ … /* ── MODUL VÉGE: TtTipp ── */`
blokkot tartalmazza, **bájtra azonosan** (az API-dokumentáció a blokk tetején). A blokk az utolsó
átvett modul után, a lecke saját kódja előtt áll. Csak a Lesson motorra épül; a `.tt-rejtett` CSS-t
és a letiltott csúszka halványítását maga teszi a `<head>`-be (a leckék `<style>`-sora törölve).

md5 (a nyitó sortól a `MODUL VÉGE: TtTipp` sorig, a sorvégi újsorral együtt):
`e334f46119af5db9f6231d308a810a85` – mind a 16 leckében egyezik
(ellenőrzés: `awk '/^\/\* ── MODUL: „Tippelj!” és bélyegek \(TtTipp\)/{p=1} p{print} p&&/MODUL VÉGE: TtTipp/{exit}' <lecke>.html | md5sum`).

A modul a három változat igényeit fedi le: a 01-es API változatlan nevekkel (a 17-es `noRhythm`/`qv` és a
02-ből hiányzó `q2` is benne), a 03 igénye a külön hívható `tipRow(P, st, a, x, y, o)` (válaszsor bárhová,
`o.tExp` késleltetéssel), a 10 igénye a `stamp` `o.col` opciója és a választás sorszáma (`P.keys.indexOf(P.guess)`).
Minden ismert bélyegfajta beépült (`STAMP`), ismeretlen fajta halvány tintával rajzolódik.

### Viselkedésbeli változások (szándékosak)

- **A tipp után csak a tippgombok tűnnek el**, nem az egész gombsor. Korábban a `tipControls` a sor
  egészét rejtette – a **07-foldgomb 7. lépésében** így a tipp után eltűnt a „Késik az 1. műhold órája” /
  „Pontos az óra” gomb is (a kísérlet nem volt elérhető). Most ott maradnak.
- **03-meres:** a 01-es kinézetet kapta (válaszsor: cinóber keret + „a te tipped”, a helyes zöld keret +
  pipa; visszajelzés pillben „Jó tipp!” / „Sokan gondolják így – nézzük meg!” – korábban dőlt, piros
  szöveg). A tipp után a tippgombok eltűnnek (korábban maradtak, de nem reagáltak); a „Példasor” és „Újra”
  gomb marad. A 5. és 7. lépés `enter`-je `veilIf`-et hív (a panelszöveg most egy bekezdés, ezért nem
  mos el semmit – ha a tanár bekezdést tesz hozzá, a 2. bekezdéstől elmosódik). Bélyegek: `kitalált`
  ékezettel, betűköz 0,06 → 0,08 em (a sorozat stílusa).
- **10-erdo:** a tippgombok a tipp után eltűnnek (a sorozat mintája; korábban maradtak, és a tipp
  átírható volt). A visszajelzés a modul `tipFeedback`-je (rossz tippnél kékeszöld, nem cinóber). A
  sarokjelvény (`tipBadge`) és „a te tipped” keret (`yourTip`) lecke-saját maradt, mert a metszet és a
  háló a teljes vásznat kitölti, a `rhythm`/`tipHead` fejléc nem fér el – ez a sorozat egyetlen tudatos
  eltérése. A jelenet-áttűnés alfája a `draw()`-ban a `GA`-ba kerül (a modul `ga()`-ja ezt olvassa).
- A panel-elmosás a `.lp-text > *` elemekre hat (korábban csak a `<p>`-kre; a 10-es már így működött) –
  egy tippes lépésben lévő lista vagy a `> megjegyzés:` doboz sem árulja el a választ (a megjegyzés tehát a
  tippig most elmosódik; ha egy lépésben ez zavar, a megjegyzés a tanári blokkba tehető).
- A letiltott (`input.disabled`) csúszka a panelen halványan látszik (08-noveny metrikasorának
  „ismert hiányossága”; a 01, 06, 07, 08, 15, 17 tippes lépéseit érinti).

### Átállítás egy 01-tocsa-segédes leckénél (pl. 16-folyo) – lépésről lépésre

1. **Modul beszúrása:** a fenti blokkot (pl. a `01-tocsa.html`-ből, a nyitó sortól a
   `/* ── MODUL VÉGE: TtTipp ── */` sorig) bájtra azonosan másold az utolsó `/* ── MODUL VÉGE …` sor után,
   a lecke saját kódja elé. md5-tel ellenőrizd.
2. **A régi segédblokk törlése:** a lecke kódjában a `/* ═══…` sortól (amely után az
   „A SOROZAT MINTÁI (természettudomány 5–6, szerződés 17.)” megjegyzés jön) a `function tipFeedback(…) {…}`
   záró `}`-éig minden törlendő (`STAMP`, `stamp`, `Tip`, `tipReset`, `panelVeil`, `tipGuess`,
   `tipControls`, `tipU`, `rhythm`, `tipHead`, `tipFeedback`), és a helyére ez a három sor kerül:
   ```js
   /* „Tippelj!” és bélyegek: a TtTipp modulból (fent) – a sorozat közös mintája (szerződés 17.) */
   TtTipp.bind({ L: () => L, ga: () => GA });
   const { stamp, Tip, tipReset, panelVeil, veilIf, tipGuess, tipHide, tipControls, tipU, rhythm, tipHead, tipRow, tipFeedback } = TtTipp;
   ```
   (Ha a leckében nincs `GA`, a `ga` elhagyható – alapértéke `() => 1`; vagy a `draw()`-ban állítsd a
   jelenet-alfára, mint a 10-erdóban.)
3. **Törlendő sorok a lecke saját kódjából:** `function veilIf(P) { panelVeil(!P.guess); }` (vagy
   `const veilIf = …`), és minden `STAMP['…'] = MUT;` bővítés (a fajták a modulban vannak; új fajtához
   `TtTipp.STAMP['új'] = szín` vagy `stamp(…, {col})`).
4. **Átírandó:** a `guessQA`-ban (és bárhol) az `if (P.row) P.row.style.display = 'none';` →
   `tipHide(P);` (a `P.row` megszűnt; a gombok a `P.btns`-ben). QA-állapotban a teljes választás egy
   hívással is megy: `tipGuess(P, k, L2.st - 30)`.
5. **CSS:** a `<style>`-ból a `/* „Tippelj!”: a megoldás a tippig elmosva … */` és a
   `.lp-text p.tt-rejtett { … }` sor törlendő (a modul injektálja).
6. Ha a lecke a `tipControls(P)` után ugyanabba a gombsorba más gombot is tesz, az most a tipp után is
   látszik – ha a kísérlet gombjának a tippig rejtve kell lennie, azt a lecke maga rejtse (pl. `P.on`).
7. `node --check` (vagy a QA) a dupla deklarációkra: ha a lecke a fenti nevek valamelyikét (pl. `tipRow`,
   `tipHide`, `rhythm`) maga is definiálja, a destrukturáló sorból hagyd ki.

A sorozat leckéin ezt egy szkript végezte (1–5. pont), ellenőrzés: `node --check` az összes inline
scriptre, md5, majd teljes QA leckénként.

## 2. TtMuszer v1.1

A blokk fejléce dokumentálja a buktatót: a műszerek az `o.a`-t a **pillanatnyi `globalAlpha`-val szorozzák**,
ezért hívás előtt `al(1)` kell (különben egy előtte elhalványított felirat a műszert is eltünteti – a 04-ben
így tűnt el a stopper). Új opció: `o.abs: true` → az `o.a` (alap 1) abszolút alfa; ilyenkor a
jelenet-áttűnést a hívó szorozza bele (`{abs: true, a: GA * a}`). A meglévő hívások változatlanok.

md5 (nyitó sortól a `MODUL VÉGE: Mérőeszközök` sorig): `7e6551aa6d7f241fd50da9ca081337cf` –
03-meres, 04-magnes, 06-terkep, 17-idojaras (mind egyezik; a korábbi `30a9dcf2…` helyett).

## 3. 03-meres 4. lépés – nagyító

A mérőhenger meniszkuszán lévő kis kör (r 60) a skála „60” és „70” számát takarta. Most r 44 (a jobb széle a
skálaszámok előtt ér véget), a nagyítás mértéke változatlan (`zoom: to.R / 60`), így a nagy kör tartalma
ugyanaz maradt.

## 4. Metrikasorok – mi lett javítva, mi maradt

Javítva (leckén belül): 07 – a 7. lépés kísérletgombjai a tipp után eltűntek (lásd fent); 08 (és a többi
tippes csúszka) – a letiltott csúszka nem halványult; 01/17 – a 17-es `tipHead`-bővítés és a bélyegfajta-
bővítések bekerültek a közös modulba; 04 – TtMuszer-alfa dokumentálva; 03 – nagyító.

Maradt (közös modul, `tools/` vagy motor – csak leírva, a koordinátornak):

- **TortCards** `draw` és **BioPlot** `axes/line/point` a hívó `globalAlpha`-ját is szorozza (áttűnéskor a²) –
  a leckék `al(1)`-gyel kerülik (09, 13, 15).
- **MatChart.pie** abszolút alfát állít, a többi modul szoroz (11, 13) – egységes alfa-szabály kellene a
  modulokban (a TtTipp és a TtMuszer `o.abs` most kétféle utat ad).
- **BioFlow:** nincs színparaméter (08: a vízpöttyöket a lecke rajzolja).
- **BioZoom** level-draw: a saját `al(1)` felülírja az áttűnést (11).
- **DeepTime.logView** alsó vége 1e-3 (05).
- **BioNet** jelmagyarázat ▲/▼ glifje a Bricolage-ban nincs meg (10: rajzolt háromszög).
- **TtIkon** (sorozaton belüli, de nem egyszerű): szemesostoros, „ülő” kárókatona póz hiányzik (12); a `bab`
  `pale` + `sy` nyújtás a levelet is torzítja (08).
- **Motor:** `L.tx` sortörés (08 saját `wrapBox`), `U.mix` csak `#rrggbb`-t fogad (17), a letiltott csúszka
  halványítása motorszintre is jó lenne (most a TtTipp injektálja).
- **QA (tools):** a kör alakú rajzolt pont–felirat takarást nem veszi észre (03 – a 4. lépés esete is ilyen
  volt); `--states` TypeError, ha egy állapotnak csak `st`-je van (14; azóta lehet, hogy javítva);
  a `sources`-ellenőrzés csak az adat utáni vagy a szakasz eleji forrásmegjegyzést fogadja (03).
- **Build:** a terület-`dim` nem fogad „ezer ha”-t, vegyes szorzós range nem értelmezhető (11).
- **Terv/tartalom:** 14 – a 7. lépés időcsúszkája helyhiány miatt kimaradt (szándékos, nem javítva).
- A 06 buktatója (a `guessQA` a `gt`-t `L.st − 30`-ra teszi, a tipp utáni késleltetett állapotokhoz `st`
  kell) változatlan; a `tipGuess(P, k, gt)` most ugyanezt egy hívással adja.

## QA

Minden módosított lecke: build ✓, `qa_lesson.py --back --states --det --at 1.5,settle` (ugrópróbával) –
eredmény: **mind a 16 leckén „✓ nincs hiba”** – 0 JS-hiba, 0 túlcsordulás/átfedés, visszaléptetés, ugrópróba,
determinizmus és minden `__qaStates`-állapot rendben. A „Tippelj!” lépések képei tipp előtt és után átnézve:
01 (1.), 03 (5., 7.), 07 (7. – a kísérletgombok a tipp után is látszanak), 08 (2. – halvány letiltott csúszka),
10 (2., 6.), 17 (1. – `q2` + `qv`); a 03 4. lépésén a „60” látszik.
