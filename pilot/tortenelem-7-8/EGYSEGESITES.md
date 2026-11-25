# Történelem 7–8. – modul-egységesítő és javítókör (2026-11-25)

Cél: a sorozat 17 leckéjének közös moduljait egyeztetni, a metrikasorokban jelzett **látható** modulhibákat a
modulban javítani (verziószám + változásnapló a blokk fejében), az új változatot bájtra azonosan minden használó
leckébe másolni, a leckékben a kerülőutakat egyszerűsíteni, és a TortTerr következő (v1.1) körének igényeit
összegyűjteni. A sorozaton kívüli leckékhez (földrajz 9–10, történelem 5–6, természettudomány 5–6, magyar 5–6,
digitális kultúra 5–6) ez a kör **nem nyúlt**.

Az md5 a blokkra vonatkozik: a `/* ── MODUL: …` sortól az első utána következő `/* ── MODUL VÉGE…` sor végéig,
záró újsor nélkül (a MatChart végjele névtelen: `/* ── MODUL VÉGE ── */`).

## 1. Modulleltár (a kör után)

Minden modul minden példánya bájtra azonos volt a kör előtt is (eltérő változat nem volt). A kör után:

| modul | változat | md5 | példány | leckék |
|---|---|---|---|---|
| TtTipp | – | `fa839199626ca8aa31f3693a24150d81` | 17 | mind |
| TortTimeline | – | `9c5cebae791ce43f3d93b5f2785e6dfd` | 17 | mind |
| TortSource | – | `a59b107413f4949197b9d51f1c5a174e` | 17 | mind |
| TortMap | v1.1 | `05bd08a1c2d32bdd050cba4c4fdbc2e2` | 12 | 01, 02, 03, 04, 05, 07, 08, 09, 10, 11, 13, 14 |
| TortTerr | v1.0 | `d7e8dcc3e82e93db533ecaef134c4a26` | 11 | 01, 03, 04, 05, 07, 08, 09, 10, 13, 14, 17 |
| FoldChart | – | `92a03151ff1c93037ec9a611e70c9e91` | 10 | 02, 03, 06, 07, 09, 12, 13, 14, 15, 17 |
| TortCards | – | `2c411077c00d1ba0d984102651b64c44` | 6 | 01, 02, 05, 12, 14, 16 |
| **TortState** | **v1.1** (új) | `5c74bd23baebc49fc0345746b1c4ab47` | 6 | 05, 10, 12, 13, 16 (ref.), 17 |
| MatChart | v1.1 | `02e3710065229ffbf2fd7f1ac155933a` | 5 | 02, 04, 06, 11, 12 |
| TortCity | v1.1 | `22789cd02faf78782c77841ee1b452aa` | 4 | 02, 07, 08, 11 |
| **TortParl** | **v1.1** (új) | `875d1496e5cd038b159ec13c96dde51f` | 4 | 05, 10, 13, 16 (ref.) |
| **FoldChoro** | **v1.2** (új) | `cdb1ad798defc4cb21a47cbf2fbf373e` | 3 | 01, 14, 17 (ref.) |
| TortGlobe | v1.1 | `35472d60b468679e013140e7db43d6c6` | 2 | 07, 09 |
| TortScene | – | `2ffe3e9ed4362ed08e69c297fc91213f` | 1 | 03 |

Korábbi md5-ök: TortState v1.0 `904c85fa2dde679486ce4e74ba769a3d`, TortParl v1.0
`133ef9683ec72199b2ec249538e21591`, FoldChoro v1.1 `bbea5aa7105f6fc78d8a991d74b57014`.

Sorszámok (MODUL-sor – MODUL VÉGE-sor) a három új változatnál:

| modul | lecke: sorok |
|---|---|
| FoldChoro v1.2 | 01: 1992–2270 · 14: 1726–2004 · 17: 1712–1990 |
| TortParl v1.1 | 05: 2264–2589 · 10: 2212–2537 · 13: 2445–2770 · 16: 1440–1765 |
| TortState v1.1 | 05: 2590–2866 · 10: 2539–2815 · 12: 2333–2609 · 13: 2772–3048 · 16: 1767–2043 · 17: 2418–2694 |

### Melyik sorozat melyik változatot használja (a sorozatközi modulok)

| modul | változat | sorozat |
|---|---|---|
| FoldChoro | v1.1 `bbea5aa7…` | földrajz 9–10 (5 lecke), természettudomány 5–6 (1 lecke) |
| FoldChoro | **v1.2** `cdb1ad79…` | **csak történelem 7–8** (01, 14, 17) |
| TortMap | v1.1 `05bd08a1…` | történelem 5–6, 7–8, földrajz 9–10, magyar 5–6, természettudomány 5–6, digitális kultúra 5–6 (változatlan) |
| TortSource | `a59b1074…` | történelem 7–8, földrajz 9–10, magyar 5–6, és a történelem 5–6 nagy része (ott még két régebbi változat is él: `134cb7b3…`, `50d3c6fd…` – nem e kör tárgya) |
| TortState, TortParl, TortTerr | – | csak történelem 7–8 |

A FoldChoro v1.2 visszafelé kompatibilis a v1.1-gyel (az egyetlen viselkedésváltozás, a `q.fill` hívásának
szűkítése, a `q.fillAll: true`-val visszakapcsolható); a földrajz 9–10 egy későbbi egységesítő körben
átveheti. A v1.2 blokk fejsora jelzi, hogy egyelőre csak ebben a sorozatban él.

## 2. Javított modulok

### 2.1 FoldChoro v1.2 (referencia: `17-europai-unio.html`)

- **`M.draw` – `q.fill` csak adatos elemre** (17 metrikasora): a v1.1 a felülíró `fill(key, szín)`-t a semleges
  (`val` → `undefined`) és a „nincs adat” (`null`) elemekre is meghívta, `undefined`/`null` színnel – egy
  `U.mix(LAND, col, t)` jellegű hívó ezen elhasalt, minden hívónak őrfeltétel kellett. v1.2: a `fill` csak
  színes elemre hívódik; `q.fillAll: true` a régi viselkedés. Böngészőpróba (Equal Earth, 1 adatos HUN + 1 DEU,
  1 null AUT, a többi semleges): v1.2 → 2 hívás (csak szín), `fillAll` → 2 szín + 1 null + 174 undefined.
  A 01 és a 17 hívói (`col ? … : col`, `JOIN[k] == null ? col`) így is helyesek – maradtak.
- **`M.legend` – `q.bg` / `q.pad`** (17 metrikasora): kártyaszerű háttér a **mért** tartalom alá (árnyék, papír
  kitöltés, halvány keret), a térképen így olvasható. A rajz előtt külön elrendezési (mérő) menet fut, a
  visszaadott `{x, y, w, h, items}` változatlan (a w/h a háttér nélküli tartalomé; próbán `bg` nélkül és
  `bg`-vel azonos `items`).

Lecke-oldali egyszerűsítés:

- **17-europai-unio**, 4. és 9. lépés: a jelmagyarázat alatti, **fix méretű** `soft(…, 370, …)` /
  `soft(…, 300, 156, …)` doboz helyett `legend({…, bg: true})` – a háttér a szöveghez mérve (Windows-fontokkal sem
  lóg ki).
- **14-hataron-tul**, 5. lépés: a fix `card(16, 700, 300, 296)` helyett `legend({…, bg: true, pad: 16})`.

### 2.2 TortState v1.1 (referencia: `16-demokracia.html`)

- **`S.draw` – `o.hlEdge: 'key'`** (05 metrikasora): a v1.0-ban egy él akkor is kiemelt volt, ha a kulcsa nem
  szerepelt a `hl`-ben, de mindkét végpontja igen – így két kiemelt doboz közti él nem volt halványítható (a 05
  két példányt úsztatott át). `hlEdge: 'key'`: az él csak a saját kulcsával kiemelt (az automatikus „irányít”
  nyíl ekkor is a végpontok szerint). Alap: `'ends'` (a v1.0 viselkedése). Próba: `hl: ['a', 'b']` → az él
  alap módban teljes, `'key'` módban halvány, `hl: ['a', 'b', 'e']` + `'key'` → teljes.
- **`S.timeline(events, d, fade, o)` – `o.align`** (05 metrikasora): a v1.0-ban az átmenet a dátumon **indul**
  (`smooth((d − a) / fade)`), így az esemény a saját dátumán még nem hat. `align: 'end'`: `[a − fade, a]`
  (a dátumra lezajlik), `'mid'`: a dátum az átmenet közepe. Alap: `'start'` (v1.0). Próba (fade .5): a dátum
  pillanatában `start` → nincs hatás, `end` → kész (0), `mid` → fél (0,5); `end` mód a = 2000 − .6-nál még nincs.
  A doksi pontosítva: az `i` az utolsó **elért és már ható** esemény.

Lecke-oldali egyszerűsítés: **05-diktaturak**, 6. lépés – `a: evA(i) − .015` eltolás helyett
`{ align: 'end' }` (azonos kép; a 6. lépés képei és állapotai átnézve). A 05 1. lépésének két példánya
(`ST1` / `ST1T`) **maradt**: ott nem csak élhalványítás, hanem elrendezés- és élkészlet-csere is történik
(a demokratikus ellenőrző élek helyére a párt „irányít” nyilai jönnek) – a két példány áttűnése ott a jó megoldás.

### 2.3 TortParl v1.1 (referencia: `16-demokracia.html`)

- **`TortParl.legend` – `o.pd`** (10 metrikasora): a % tizedesjegyei (alap 1, mint eddig). A v1.0 fixen
  1 tizedest írt, a 10 saját sávjain 2 tizedes állt (57,03 % ↔ 57,0 %). Próba: `pd: 2` → „57,03 %”, az oszlop
  szélessége mérve nő.

Lecke-oldali: **10-szovjetizalas** `legend()` → `pd: 2` (3., 5. lépés: a jelmagyarázat és a sávok most egyezően
két tizedest mutatnak; a 9. lépés `seatsOnly`, ott nincs %).

## 3. Kozmetika: 11-forradalom-1956, 4. lépés (vidéki térkép)

A vidéki városok kétsoros feliratát (név + mi történt) a `TortMap.labels` a kis (790 × 470) térképen távolra,
szaggatott vezetővonallal tette (Mosonmagyaróvár, Győr, Debrecen), a halo (≈ 2,5 px körvonal) a folyókat és a
határt nem takarta, a „Pécs” felirat 50 px-re volt a pontjától. A modul (TortMap v1.1, hat sorozat közös modulja)
ezt nem tudja jobban, ezért a **leckekódban**:

- `cityLabel4()` – a öt vidéki város kézi elhelyezéssel (`PLACE4`: a pont fölött/alatt, vízszintes igazítás,
  eltolás; a nézet rögzített), a doboz a **mért** szöveghez igazodik, és a térkép keretén belül marad;
  **papírszínű háttér** (`rgba(250,246,238,.9)`, lekerekített) a két sor alatt, a pontnak is papír-halo.
  Pécsnél az alsor van fölül, így a „Pécs” név közvetlenül a pont fölött áll.
- Budapest és a tanár által átírható „saját hely” (Szeged) továbbra is `TortMap.labels`-szel (adatfüggő hely),
  a kézi dobozokat és pontokat elkerülve (`avoid`), és egy `draw: false` mérő menet után ezek is papírszínű
  hátteret kapnak.

## 4. A metrikasorok többi modul-megjegyzése – döntések

| hol | modul | mi | döntés |
|---|---|---|---|
| 03, 07 (+ a koordinátori utasítás) | TortMap.labels | id szerint megjegyzi a felirat helyét → lépésváltás után más hely lehet (det-hiba) | **nyitva, csak leírva**: a viselkedés szándékos (mozgó kamerán nem ugrál a felirat), a leckék jelenetenkénti id-előtaggal kerülik, látható hiba nincs. A TortMap hat sorozat közös modulja – egy sorozaton belüli eltérő változat többet ártana. Javaslat a következő közös TortMap-körre (v1.2): `labels(L, items, {memo: 'jelenet-kulcs' \| false})` – névtér vagy kikapcsolás |
| 03, 07 | TortSource.stamp | nincs „vitatott” fajta | **nyitva, csak leírva**: a leckék `TtTipp.stamp`-pel pótolják (látható hiba nincs); a TortSource négy sorozat közös modulja (17 + 15 + 3 + 17 példány). Javaslat: `T['vitatott']` + szaggatott cinóber keret a következő közös körben |
| 05 | TortMap.frame | hívásonként új nézet-objektum | nem hiba; a TortTerr nézetértékre gyorsítótáraz (a v1.0 már így), a buktató a koordinátori utasításban |
| 09 | TortSource.card | az alfát szorozza → előtte `al(1)` | dokumentált viselkedés (mint a FoldChoro és a TortCards) |
| 13 | TortSource.card | a sorcímke-oszlop szélessége a leghosszabb címke – egy hosszú címke az egész kártyát szélesíti | nyitva (javaslat: `o.lw` max. címkeszélesség, tördeléssel) |
| 09 | FoldChart.cursor | a kurzorfelirat ütközik az y-tengely címével | nyitva (sorozatközi modul; a lecke saját címsort tesz följebb) |
| 06 | FoldChart.upTo | log skálán lineárisan interpolál | nyitva (sorozatközi modul; a lecke log-térben interpolál) |
| 12 | FoldChart | az y2-tengely nem kapcsolható ki (két példány kell) | nyitva (javaslat: `y2: null` / `o.y2: false`) |
| 09, 14, 17 | TortTimeline.cards | dátummal 2 soros kártya 62-es pitch-nél átfed; a vezetővonal átfut a felső kártyán (sorrend); csak függőleges rétegezés | nyitva (a kártyákat a hívó rendezi – már a koordinátori utasításban) |
| 14 | FoldChoro.card | a kártya a leghosszabb sorhoz méreteződik (itt 640 px), a térképen eltakarja a régiót | nem hiba (tartalomhoz mért); a lecke saját keskeny kártyát rajzol |
| 14 | FoldChoro `hl` | kiemelésnél a többi alapból .35-tel halványul | dokumentált (`dim: 0` kikapcsolja; a 14 így hívja) |
| 14 | U.mix / FoldChart | az `U.mix` rgb()-t ad, a FoldChart hexet vár | nyitva (motor/FoldChart) |
| 10 | TortMap.base | a teljes vásznat tengerrel tölti → mindig vágni kell | ismert (DK 5–6 EGYSEGESITES 4.) |
| 11 | TortCity.places | alapból pontot rajzol, nincs `rect` opció | nyitva (a lecke `dot: false` + `avoid` dobozokkal) |
| 01, 04, 08, 10 | adat | a `map-torthatar.js`-ben nincs porosz/német 1815/1866-os csoport; a `map-karpat.js` kivágásszélén kék rés (04), keleti szélén ék alakú hiány (08); a `map-europa.js` 60° K-nél véget ér (10) | adatigény, nem modulhiba – `shared/tort/` következő adatköre |

## 5. TortTerr v1.1 – javasolt API (NEM megvalósítva; a leckék most saját kódban pótolják)

A TortTerr v1.0 (`d7e8dcc3…`, referencia `07-masodik-vilaghaboru.html`) 11 leckében él. Az alábbi igények a
leckék saját segédkódjából jönnek; a v1.1 után ezek a segédek törölhetők. Minden javaslat visszafelé
kompatibilis bővítés.

1. **Közös határív két csoport közt** (09 `arcsPath`, 13 `commonBorder` – vasfüggöny, HU–AT szakasz):
   `T.common(gA, gB, o?) → Path2D` – a mindkét csoportban használt ívek (a v1.0 `outline` belső-ív logikájának
   párja), nézetenként gyorsítótárazva; o = {view}. Kényelmi rajzoló: `T.strokeCommon(ctx, gA, gB, {c, w, dash,
   halo, a})`.
2. **Több csoport körvonala egy útvonalban** (14 `multiOutline`): `T.outline(ctx, [gA, gB, …], o)` vagy
   `T.outlines(ctx, gs, o)` – csoportonként a külső ívek, minden ív **egyszer** (áttetsző tintánál a közös határ
   nem sötétedik kétszeresre).
3. **`g` = csoportkulcs-lista** (05, 13, 17 `TG` + `TG_MEMO`): ma a tömb egység-azonosítók listája. Javaslat:
   `{any: ['eu1942.DE', 'mo1941', …]}` (vagy `T.union(...gs)` → `{ids}`, gyorsítótárazva) – az egységlisták
   uniója, kulcsonként egyszer számolva. (A sima tömb jelentése ne változzon – visszafelé kompatibilitás.)
4. **`asChoro` régiókulcs szerint, `lp`-vel** (14 `choroOf`): `TortTerr.asChoro(H, {régió: [g…], …})` →
   régiónként egy FoldChoro-elem (a gyűrűk összefűzve), `lp`: a régió (legnagyobb egységének) címkepontja. A
   tömbös hívás (egységenként) maradjon.
5. **Nézet TortMap nélkül** (17 `TMAP`/`tt(V)` nézet-tartó): `TortTerr.create(L, H, {view: () => V})` vagy
   minden rajzolónál `o.view: V` (TortProj.view); `map` nélkül nincs `land`-vágás (dokumentálva).
6. **Kézi sokszög körvonala** (17 `polyLine`): `T.outline(ctx, {poly: [[lon, lat]…]}, o)` – a `T.fill` poly-jával
   azonos 1°-os sűrítéssel.
7. **`hit` / `at` kapjon nézetet** (13: a kattintás előtt `MAPE.frame(VW.e3)`, mert a v1.0 a térkép
   pillanatnyi nézetén vizsgál): `T.hit(px, py, gs, {view})`.
8. **Gyorsítótár-kulcs a vetülettel** (10: két LCC-vetület egy leckében): a v1.0 `viewKey()` csak
   `lon, lat, s, x, y`-t néz – két vetület azonos nézetértékkel ütközne. Javaslat: a kulcsba a
   `V.proj.kind` és a vetület paraméterei (`lon0, lat0, lat1, lat2`) is (mint a FoldChoro `project`-jében).

## 6. QA

Mind a 9 módosított lecke (01, 05, 10, 11, 12, 13, 14, 16, 17) újraépítve (`tools/build_lesson.py`, a
`.content.js` nem változott – a `.md`-khez nem nyúltunk), és teljes QA-val futtatva
(`--back --states --det --at 1.5,settle`, ugrópróba): **mind 0 hiba** (JS, túlcsordulás, átfedés,
determinizmus, visszaléptetés, ugrópróba; 01: 13, 05: 26, 10: 14, 11: 7, 12: 16, 13: 14, 14: 13, 16: 29,
17: 26 állapotkép).

Képen átnézve: 05 – 6. lépés (`egyparti`, `vege`: az események a saját dátumukon teljesen lezajlottak,
Hindenburg halálakor az elnöki doboz és élei kialszanak); 10 – 3. és 5. lépés jelmagyarázata (két tizedes,
a szélesebb %-oszlop is a 1360-as vizuális határon belül); 11 – 4. lépés (`1.5`, `settle`, `vissza`);
14 – 5. lépés (jelmagyarázat mért háttérrel, `nyitra` állapot); 17 – 4. lépés (`Schengen`, `EU`,
kártyaállapotok) és 9. lépés (jelmagyarázat mért háttérrel); 01 – 5. lépés (FoldChoro `fill` őrfeltétellel,
változatlan kép); 12 – 2. lépés (TortState, változatlan).

Modulpróba böngészőben (a leckék oldalán, az új opciókra – egyik lecke sem használja mind): TortState
`hlEdge` és `timeline align`, FoldChoro `fill`/`fillAll` hívásszám és `legend bg` (azonos `items`),
TortParl `pct`/`legend pd` – eredmények a 2. fejezetben.

## 7. Nyitott tételek (összesen 12)

1. TortTerr v1.1 (5. fejezet, 8 igény) – következő kör.
2. TortMap.labels memo-névtér (sorozatközi TortMap v1.2-be).
3. TortSource „vitatott” bélyeg (sorozatközi).
4. TortSource.card címkeoszlop-szélesség (13).
5. FoldChart.cursor felirat ↔ y-tengelycím (09).
6. FoldChart.upTo log skálán (06).
7. FoldChart y2 kikapcsolása (12).
8. TortTimeline.cards: 2 soros kártya átfedése, vezetővonal-sorrend, vízszintes rétegezés (09, 14, 17).
9. U.mix rgb() ↔ FoldChart hex (14).
10. TortCity.places `rect` / `dot` alapérték (11).
11. Térképadat: porosz/német 1815/1866 csoport, map-karpat szélei, map-europa 60° K-en túl (01, 04, 08, 10).
12. A FoldChoro v1.2 visszavezetése a földrajz 9–10 / természettudomány 5–6 sorozatba (sorozatközi egységesítés).
