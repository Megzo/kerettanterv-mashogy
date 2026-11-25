# Pilot: Történelem 9–10. – gyártási metrikák

A 2026-11-25-i nap második sorozata (az első: Történelem 7–8., `pilot/tortenelem-7-8/METRIKAK.md`; az
éjszakai kör összefoglalója és tanulságai: `pilot/EJSZAKAI-GYARTAS.md`). A gimnázium 4 évfolyamos változata,
13 témakör, 121 óra, Hammurapitól 1849-ig.

- **Körülmények – új gyártási mód:** a terv (`terv.md`, benne a „0. Döntések a felhasználó távollétében”) után
  **mind a 17 lecke párhuzamosan** készült: egyszerre 10 al-ügynök (a korábbi sorozatok 5-ös korlátja helyett),
  a felszabaduló helyekre a maradék 7. **Nem volt referencialecke és nem készült új közös modul**: minden lecke a
  Történelem 7–8. két leckéjéből (`13-rendszervaltas`, `12-kadar-rendszer`) bájtra azonosan másolt modulokra
  épül, minden új rajz és szimuláció leckén belüli kód (terv, 0. döntés 3–4.). A kötegek összetétele egyezik a
  terv 6.1 beosztásával. A felhasználó nem volt gépnél; a tervet a koordinátor hagyta jóvá, a leckék egyenként
  commitolva készültek. **A terv tényeit külső forrásban senki nem nézte át** (0. döntés 13.) – ezt a
  leckeügynökök végezték, és sokat javítottak (lásd „Tervhibák”). Szakmai lektor nem volt; a kilenc lektort kérő
  lecke egyike sincs lektorálva.
- **Időtartam:** az al-ügynök futásideje a koordinátor naplójából (HH:MM, a commitig számolva, kb. ±3 perc). A
  „Kész” oszlop a commit időpontja (git, helyi idő). A metrikasorokban nincs időbélyeg.
- **Token:** az al-ügynök saját, Claude Code által jelentett fogyasztása (a koordináló fő munkamenet nélkül), a
  napló ezresre kerekít.
- **Leckék tábla:** a lépésszám és a panelszó a generált tartalomfájlból (`leckek/tortenelem-9-10/<slug>.content.js`,
  a build szószámlálása szerint), a QA tömörítve az al-ügynök metrikasorából (`metrika/<slug>.md`). A 7–8-cal
  ellentétben a metrikasorok szövegét **nem** másoltuk ide szó szerint (a 17 sor együtt kb. 63 ezer karakter):
  az adatok és a forrásaik a `metrika/` fájlokban és a leckék `.md`-jében vannak, a review-pontokat és a
  tervhibákat a dokumentum végén tömörítve, leckénként soroljuk fel.

## Al-ügynökök

| # | Feladat | Indulás | Kész | Időtartam | Token (al-ügynök) | Eredmény |
|---|---|---|---|---|---|---|
| T0 | Leckesor terve (`terv.md`) + szerződés 21. fejezet | 20:01 | 11-25 20:29 | 28 p | ~144 ezer | 17 lecke, 2 köteg |
| 1. köteg (10 ügynök egyszerre) | | | | | | |
| L01 | 01-polisz-demokracia | 20:29 | 21:11 | 42 p | ~221 ezer | kész: 9 lépés, QA hibátlan |
| L02 | 02-romai-koztarsasag | 20:29 | 21:12 | 43 p | ~294 ezer | kész: 9 lépés, QA hibátlan |
| L06 | 06-magyar-ostortenet | 20:29 | 21:17 | 48 p | ~268 ezer | kész: 9 lépés, QA hibátlan; **történész + nyelvész + régész lektorra vár** |
| L11 | 11-reformacio | 20:29 | 21:23 | 54 p | ~303 ezer | kész: 9 lépés, QA hibátlan; **egyháztörténész lektorra vár** |
| L16 | 16-rendi-orszaggyules | 20:29 | 21:24 | 55 p | ~181 ezer | kész: 9 lépés, QA hibátlan |
| L17 | 17-forradalom-1848 | 20:29 | 21:25 | 57 p | ~157 ezer | kész: 9 lépés, QA hibátlan; **történész lektorra vár** |
| L04 | 04-hodito-birodalmak | 20:29 | 21:26 | 57 p | ~91 ezer | kész: 9 lépés, QA hibátlan |
| L12 | 12-hodoltsag-merlege | 20:29 | 21:26 | 57 p | ~84 ezer | kész: 9 lépés, QA hibátlan; **történész lektorra vár** |
| L14 | 14-ujranepesules | 20:29 | 21:34 | 65 p | ~268 ezer | kész: 9 lépés, QA hibátlan; **történész lektorra vár** |
| L13 | 13-francia-forradalom | 20:29 | 21:50 | 81 p | ~258 ezer | kész: **10 lépés** (a terv 9-et írt), QA hibátlan; **történész lektorra vár** |
| 2. köteg (a felszabaduló helyekre) | | | | | | |
| L03 | 03-monoteizmus (01 helyére) | 21:11 | 21:40 | 29 p | ~104 ezer | kész: 9 lépés, QA hibátlan; **vallástörténész lektorra vár** |
| L05 | 05-rendi-tarsadalom (02 helyére) | 21:12 | 21:48 | 36 p | ~219 ezer | kész: 9 lépés, QA hibátlan |
| L07 | 07-arpad-kori-allam (06 helyére) | 21:17 | 22:12 | 55 p | ~174 ezer | kész: 9 lépés, QA hibátlan (első körben 8 hiba, javítva); **történész lektorra vár** (a terv nem kérte) |
| L08 | 08-anjou-gazdasag (11 helyére) | 21:23 | 21:59 | 36 p | ~215 ezer | kész: 9 lépés, QA hibátlan; **történész lektorra vár** (a terv nem kérte) |
| L09 | 09-hunyadiak-torok (16 helyére) | 21:24 | 22:12 | 48 p | ~109 ezer | kész: 9 lépés, QA hibátlan |
| L10 | 10-arforradalom | 21:26 | 22:06 | 40 p | ~280 ezer | kész: 9 lépés, QA hibátlan |
| L15 | 15-iparosodas | 21:26 | 22:07 | 41 p | ~247 ezer | kész: 9 lépés, QA hibátlan; címe az egységesítésben módosul (lásd lent) |
| E1 | Egységesítés (`EGYSEGESITES.md`, a 15 címének igazítása) | 22:12 | – | folyamatban | (becslés: ~200 ezer) | – |
| M1 | Metrikák összesítése (ez a fájl), README-k | 22:12 | – | – | (becslés: ~200 ezer) | kész |

## Leckék

| Lecke | Köteg | Lépések | Panelszó (össz. / max.) | Gyártás | QA (al-ügynök) | Lektor |
|---|---|---|---|---|---|---|
| [01-polisz-demokracia](../../leckek/tortenelem-9-10/01-polisz-demokracia.html) – Ki hozza a törvényt? – Hammurapitól Periklész Athénjáig | 1 | 9 | 400 / 54 | 42 p, ~221 ezer | 0 hiba; 24 állapotkép, review 3, L.checks 12/12 (+1 feltételes) | – |
| [02-romai-koztarsasag](../../leckek/tortenelem-9-10/02-romai-koztarsasag.html) – Hogyan lett a köztársaságból egyeduralom? – a római állam és jog | 1 | 9 | 414 / 55 | 43 p, ~294 ezer | 0 hiba; 22 állapot, L.checks 11/11 | (nyelvi: saját fordítások) |
| [03-monoteizmus](../../leckek/tortenelem-9-10/03-monoteizmus.html) – Hogyan lett egy üldözött hitből birodalmi vallás? – politeizmus, zsidó és keresztény monoteizmus | 2 | 9 | 452 / 55 | 29 p, ~104 ezer | 0 hiba; 16 állapotkép, review 3, L.checks 6 tétel | vallástörténész |
| [04-hodito-birodalmak](../../leckek/tortenelem-9-10/04-hodito-birodalmak.html) – Mekkora volt egy birodalom, és meddig tartott? – Róma bukása, hunok, arab hódítás | 1 | 9 | 415 / 55 | 57 p, ~91 ezer | 0 hiba; 14 állapotkép, review mód, L.checks 12/12 | – |
| [05-rendi-tarsadalom](../../leckek/tortenelem-9-10/05-rendi-tarsadalom.html) – Mennyi maradt a jobbágynak? – rendek, terhek és válság a középkori Európában | 2 | 9 | 434 / 53 | 36 p, ~219 ezer | 0 hiba; 20 állapot, review 3, L.checks 8 tétel | – |
| [06-magyar-ostortenet](../../leckek/tortenelem-9-10/06-magyar-ostortenet.html) – Mit tud a nyelvész, a régész és a genetikus? – a magyar nép eredetének bizonyítékai | 1 | 9 | 387 / 55 | 48 p, ~268 ezer | 0 hiba; 21 állapot, review 7, L.checks 8 tétel | **történész + nyelvész + régész** |
| [07-arpad-kori-allam](../../leckek/tortenelem-9-10/07-arpad-kori-allam.html) – Kié volt a föld? – az Árpád-kori állam a királyi birtoktól az Aranybulláig | 2 | 9 | 379 / 51 | 55 p, ~174 ezer | 0 hiba (első kör: 8, javítva); 12 állapot, L.checks 10/10 | történész (a lecke kéri) |
| [08-anjou-gazdasag](../../leckek/tortenelem-9-10/08-anjou-gazdasag.html) – Mitől lett erős az Anjou-kori király? – arany, kapuadó és a Szent Korona | 2 | 9 | 414 / 55 | 36 p, ~215 ezer | 0 hiba; 13 állapot, L.checks 18/18 | történész (a lecke kéri) |
| [09-hunyadiak-torok](../../leckek/tortenelem-9-10/09-hunyadiak-torok.html) – Mennyibe került megvédeni az országot? – Zsigmondtól Mátyásig a török árnyékában | 2 | 9 | 345 / 47 | 48 p, ~109 ezer | 0 hiba; 19 állapotkép, L.checks 12/12 | – |
| [10-arforradalom](../../leckek/tortenelem-9-10/10-arforradalom.html) – Hová lett Amerika ezüstje? – felfedezések, árforradalom, korai kapitalizmus | 2 | 9 | 402 / 51 | 40 p, ~280 ezer | 0 hiba; 19 állapotkép, review mód, L.checks 12/12 | – |
| [11-reformacio](../../leckek/tortenelem-9-10/11-reformacio.html) – Ki dönti el, mit hisz az alattvaló? – reformáció, katolikus megújulás, vallásbéke | 1 | 9 | 454 / 55 | 54 p, ~303 ezer | 0 hiba; 26 állapotkép, review mód, L.checks 13/13 | egyháztörténész |
| [12-hodoltsag-merlege](../../leckek/tortenelem-9-10/12-hodoltsag-merlege.html) – Mibe került másfél évszázad? – a három részre szakadt ország mérlege | 1 | 9 | 385 / 55 | 57 p, ~84 ezer | 0 hiba; 20 állapotkép, review mód, L.checks 12/12 | történész |
| [13-francia-forradalom](../../leckek/tortenelem-9-10/13-francia-forradalom.html) – Hogyan fordult a szabadság forradalma diktatúrába? – felvilágosodás és francia forradalom | 1 | **10** | 443 / 54 | 81 p, ~258 ezer | 0 hiba; 20 állapotkép, review mód, L.checks 19/19 | történész |
| [14-ujranepesules](../../leckek/tortenelem-9-10/14-ujranepesules.html) – Honnan jöttek az új lakók? – Magyarország a 18. században | 1 | 9 | 392 / 49 | 65 p, ~268 ezer | 0 hiba; 22 állapot, L.checks 17/17 | történész |
| [15-iparosodas](../../leckek/tortenelem-9-10/15-iparosodas.html) – Mitől kellett kilencszer kevesebbet dolgozni egy autóért? – az ipari forradalmak és az új eszmék | 2 | 9 | 418 / 54 | 41 p, ~247 ezer | 0 hiba; 17 állapotkép, L.checks 18/18 | (nyelvi: saját fordítások) |
| [16-rendi-orszaggyules](../../leckek/tortenelem-9-10/16-rendi-orszaggyules.html) – Miért tartott évtizedekig egy reform? – a reformkor országgyűlése és vitái | 1 | 9 | 383 / 52 | 55 p, ~181 ezer | 0 hiba; 18 állapotkép, L.checks 6 tétel; headlessben egyszer 310 ms-os `enter()`-figyelmeztetés (7. lépés) | – |
| [17-forradalom-1848](../../leckek/tortenelem-9-10/17-forradalom-1848.html) – Mit vívtak ki 1848-ban, és miért kellett megvédeni? – áprilisi törvények és szabadságharc | 1 | 9 | 401 / 54 | 57 p, ~157 ezer | 0 hiba; 25 állapot, L.checks 19/19 | történész |

A QA minden leckénél: JS-hiba, túlcsordulás, átfedés, ugrópróba, `--det`, `--back`, többnyire `--at 1.5,settle` és
`--states`; az al-ügynökök minden képet átnéztek. A 15 címe a metrikasorban és a terv eredeti szövegében még „Mitől
lett tízszer olcsóbb egy autó?” – a lecke maga mutatta ki, hogy dollárban csak kb. 3,2×, munkaórában kb. 9× (lásd
„Tervhibák”), ezért az egységesítő kör a címet a tartalomhoz igazítja (a táblában már az új cím áll).

## Összesítés

- **Leckék:** 17 kész a tervezett 17-ből; **lépések összesen: 154** (16 lecke 9 lépéses, a 13-francia-forradalom 10).
  Mind a 13 kerettantervi témakörnek van leckéje (a nyitóoldal Történelem 9–10. oszlopa: 17 lecke, 13 témakör).
- **Panelszöveg:** összesen 6918 szó, átlag 44,9 szó/lépés; a lépésenkénti maximum mindenhol ≤ 55 (alapérték,
  nincs `maxWords`), hét leckében van pontosan 55 szavas lépés. A terv 40–50 szavas célt adott; a 7–8. 43,8-as
  átlagánál valamivel sűrűbb.
- **Gyártási idő leckénként:** átlag 49,6 perc, medián 48 perc (legrövidebb 03-monoteizmus: 29 p; leghosszabb
  13-francia-forradalom: 81 p); összesen 844 perc = 14,1 óra. Az 1. köteg (a nehezebb, többnyire lektort kérő
  leckék) átlaga 55,8 perc, a 2. kötegé 40,7 perc. A terv 45–60 percet becsült leckénként.
- **Token leckénként:** átlag ~204 ezer, medián ~219 ezer (legkevesebb 12-hodoltsag-merlege: ~84 ezer és
  04-hodito-birodalmak: ~91 ezer – a napló szerinti értékek, nem ellenőriztük; legtöbb 11-reformacio: ~303 ezer);
  összesen **~3 473 ezer**.
- **Terv:** 28 p, ~144 ezer token. Adat- vagy modul-előkészítés nem volt.
- **A sorozat saját al-ügynök-költsége** (terv + leckék): **14,5 óra**, **~3 617 ezer token**. Az egységesítéssel
  (becslés ~200 ezer) és ezzel az összesítéssel (becslés ~200 ezer) **~4 017 ezer token**. A koordinátor fő
  munkamenete nincs benne.
- **Falióra:** a terv indulásától (20:01) ennek az összesítésnek a végéig (kb. 22:40): **kb. 2,6 óra**. A terv
  commitjától (20:29) az utolsó lecke commitjáig (22:12, 07 és 09) **103 perc**; ebben az ablakban 844
  al-ügynök-perc futott, azaz átlagosan **~8,2 párhuzamos al-ügynök** (csúcs: 10, 20:29–21:11). A terv két köteget
  × 60–75 percet (2–2,5 óra) becsült a leckékre – 1 óra 43 perc lett.
- **QA:** mind a 17 lecke 0 JS-hibával, 0 túlcsordulással/átfedéssel zárt (az al-ügynökök saját futtatása, összesen
  kb. 328 állapotkép, `L.checks` a számolt adatokra). A build (`--check`, az összesítéskor futtatva) mind a 17
  leckénél 0 figyelmeztetést ad.
- **Modulmásolatok:** az összesítéskor újraszámolva (a `MODUL:` sortól az első utána következő `MODUL VÉGE` sor
  végéig, a commitolt állapoton): a 10 átvett modul minden példánya bájtra egyezik a két forráslecke
  (`tortenelem-7-8/13-rendszervaltas`, `12-kadar-rendszer`) példányával. **Egyik lecke sem javított a saját
  modulpéldányában** – minden modulhibát leckén belüli kóddal kerültek meg (lásd lent).
- **Tanári/szakmai review-pontok:** 119 (leckénként átlag 7,0); kötelező szakmai lektorálás: **9 lecke** – 06
  (történész + nyelvész + régész), 03 (vallástörténész), 11 (egyháztörténész), 07, 08, 12, 13, 14, 17 (történész).
  Nyelvi lektort kér a saját fordítások miatt a 02 és a 15 metrikasora is (a 03, 07, 13, 14 saját fordításai a
  szakmai lektorra várnak).
- **Tervhibák:** a 17 leckéből 16 javított legalább egy tervbeli tényt (csak a 04 igazolta a terv számait változtatás
  nélkül).

### Összevetés a Történelem 7–8.-cal

| | Történelem 7–8. | Történelem 9–10. |
|---|---|---|
| Gyártási mód | terv → 0. köteg (adat) → referencialeckék új modulokkal → a többi, 5 hely | terv → mind a 17 egyszerre (10 + 7), referencialecke és új modul nélkül |
| Egyszerre futó al-ügynök | legfeljebb 5 (átlag ~4,3) | legfeljebb 10 (átlag ~8,2) |
| Falióra (terv indulása → összesítés vége) | kb. 4,7 óra | **kb. 2,6 óra** |
| Terv | 48 p, ~282 ezer | 28 p, ~144 ezer |
| Adat/modul-előkészítés | A1 + A2: 61 p, ~420 ezer; 4 új modul + 2 adatfájl | – |
| Lecke: átlag / medián idő | 50,0 / 48 p | 49,6 / 48 p |
| Lecke: átlag / medián token | ~175 / ~130 ezer | ~204 / ~219 ezer |
| Leckék összesen | 850 p, ~2 970 ezer | 844 p, ~3 473 ezer |
| Javító- és egységesítő körök | J1 + E1 + E2: ~660 ezer | 1 kör, becslés ~200 ezer |
| Teljes al-ügynök-token (összesítéssel) | ~4 532 ezer | ~4 017 ezer (becslés) |
| Lépések / panelszó-átlag | 153 / 43,8 | 154 / 44,9 |
| QA | 0 hiba | 0 hiba |
| Lektort kérő lecke / review-pont | 8 / 142 | 9 / 119 |

A 7–8. falióráját a modulfüggőség határozta meg: a 0. köteg (adat) és a `TortTerr` referencialeckéje egymás után
futott, kb. 2 óra 10 perces kritikus úttal, és öt lecke ideiglenes segéddel indult, amit utólag cserélni kellett
(E1). Itt nem volt függőség: a kritikus út a terv (28 p) + a leghosszabb lánc (06 → 07: 48 + 55 p).

## Átvett modulok és moduligények

| Modul | md5 (forráslecke) | Leckék |
|---|---|---|
| `TtTipp` | `fa839199…` (13-rendszervaltas) | mind a 17 |
| `TortTimeline` | `9c5cebae…` (13-rendszervaltas) | mind a 17 |
| `TortSource` | `a59b1074…` (13-rendszervaltas) | mind a 17 |
| `TortMap` v1.1 | `05bd08a1…` (13-rendszervaltas) | mind, kivéve 15, 16 |
| `TortCards` | `2c411077…` (12-kadar-rendszer) | 02, 03, 04, 05, 06, 07, 10, 13, 14, 15, 16 |
| `TortState` v1.1 | `5c74bd23…` (13-rendszervaltas) | 01, 02, 05, 11, 12, 13, 16, 17 |
| `FoldChart` | `92a03151…` (13-rendszervaltas) | 02, 03, 04, 05, 10, 12, 14, 15 |
| `MatChart` v1.1 | `02e37100…` (12-kadar-rendszer) | 01, 07, 08, 12, 14, 15, 16 |
| `TortTerr` v1.0 | `d7e8dcc3…` (13-rendszervaltas) | 08, 09, 12, 14, 17 |
| `TortParl` v1.1 | `875d1496…` (13-rendszervaltas) | 02, 16 |

A terv a `TortTerr`-t a 07-be, a `TortCards`-ot az 01, 08, 09, 11, 12, 17-be, a `MatChart`-ot a 05, 09, 17-be, a
`TortParl`-t a 17-be is betervezte – nem kellett. Térképadat: `shared/tort/` (`map-vilag`, `map-mediterran`,
`map-europa`, `map-karpat`, `map-torthatar` – ez utóbbiból csak a `mo1914hsz` keret, 1914 előtti csoport nincs).
Leckén belüli, nem modul kód: sztélé és esetkalkulátor, Kleiszthenész-keverő (01); jobbágy-költségvetés (05);
bizonyítékmátrix, nyelv–gén modell (06); birtokmodell-sáv (07); falumodell (08, 11); zsold-modell (09);
pénzmennyiségi és részvény-modell (10); kettős adó, offscreen kompozitos hódoltsági térkép (12); Newton ágyúja
(RK4, 13); vámmodell (14); futószalag-szimuláció (15); örökváltság-számoló (16); kéve- és rostamodell (17) – és a
legtöbb leckében kézzel rajzolt, dátumozott vázlatos sokszögek.

A metrikasorokban jelzett modulhibák és -igények (mind kerülőúttal megoldva; az egységesítés dolga –
`EGYSEGESITES.md`):

- **TortMap v1.1:** Equal Earth vetületen elfajuló nézetdoboz, ha a térkép kisebb a színpadnál – Eurázsia és
  Afrika eltűnik (10, kézi `vb`); `map.line` nem bontja a ±180°-os varratot (10); a `labels` csendben elhagyja az
  ütköző neveket (01, 13); halvány varrat a `map-vilag`/`map-mediterran` és a `map-europa` 60° K-i kivágathatárán
  (04, 06); a `mountains` réteg a foltokkal sáros barnát ad (11).
- **TortTerr:** a `{land:true}` vágás csak a `map-karpat` kivágatán belül működik (09, saját maszk); egymást átfedő
  félig átlátszó foltok sötétednek (12, offscreen kompozit).
- **TortSource:** a kártya keskeny szélességnél 22 px alá zsugorítja a címet (09); a mini-idővonal kb. 150 px-szel
  nyújtja a kártyát, tört évre „1348.4563”-at ír (05, 12); kompakt mód kellene (14); a `stamp` nem ismeri a
  „vitatott” fajtát (08).
- **TortState:** az automatikus „irányít” nyíl nem kerüli ki a dobozokat (02); a kikapcsolt élek felirata halványan
  megmarad (05); a `card` sűrű sémán más feliratokra lóg (13), kézi x/y mellett nem mutat a dobozra (16).
- **FoldChart:** a `vspan` felirata a sávhoz zsugorodik, 22 px alá is (05, 15); az `endLabels` vezetővonala mindig a
  jobb szélről indul (04); a `cursor` címkéje ütközik az y-tengely címével (15).
- **TortCards / MatChart / TortTimeline / TtTipp:** a `TortCards` zónacíme fix 40 px (06), a tálca minden kártyának
  sort foglal (07); a `MatChart` hosszú kategória-feliratai átfednek, az alfelirat egysoros, a `pie` címkéi
  ütköznek (08, 14, 16); a `MatChart` abszolút alfát vár, a többi modul szorozza a `globalAlpha`-t – vegyesen
  könnyű kétszer szorozni (07, 12); a `TortTimeline.cards` nem igazít (05); a `TtTipp.stamp` alfája a 4.
  paraméterből jön (01), a fejléc a 2. kérdéssorban nem tölti a „#”-et (03); `TortParl` „szavazás” mód (02, igény).
- **Build:** az idézetforrás halálozási éve csak 3–4 jegyű lehet (Kr. u. 14 → „0014”, 02); a `series` x-egysége csak
  egységes x-értékekkel adható meg (03, 10); a „(kitalált példa)” jelölés nem támogatott (10); idézetkulcshoz
  `"quotes": {kulcs: {}}` kell a specben (17). **Fontok:** a ✓/✗ jel hiányzik (17, saját rajz). **Panel:** sok gomb
  (3 tipp + 1) túlcsordulást okoz (12).
- **Motor/QA:** új motor- vagy QA-funkció nem kellett.

## A sorozat tanulságai

1. **A párhuzamos gyártás modulfüggőség nélkül kb. 45 %-kal rövidebb falióra.** A 7–8. 4,7 órájával szemben
   2,6 óra, ugyanannyi leckével és lépéssel, ugyanakkora leckénkénti gyártási idővel (49,6 vs. 50,0 perc). A
   10 egyszerre futó ügynök nem lassította érezhetően egymást (az 1. köteg 42–81 perce a 7–8. 38–77 percének
   nagyjából megfelel; a 10 párhuzamos Chromium-QA-tól tartott a terv 6.1). Feltétele, hogy a sorozat **kész
   modulokra** épüljön: ez a 7–8. 4 új moduljával és a `shared/tort/` adattal most adott volt. Javaslat: ahol egy tárgynak
   már van modulkészlete, ez legyen az alapmód; ahol nincs, a 7–8. mintája (adat + referenciamodul előbb).
2. **Az ára: a kerülőutak a leckékben maradnak.** Mivel senki nem írhatott modult, és egyik lecke sem javított a
   saját modulpéldányában, a hibákat (TortMap Equal Earth-nézetdoboz, TortTerr szárazföld-vágás, átfedő foltok
   stb.) leckénként, külön-külön kerülték meg – a fenti lista kb. 30 tétele. A modulmásolatok így tiszták, de az
   egységesítés dolga nagyobb: a kerülőutakat visszavezetni a modulokba (v1.2), és a leckékből kivenni. Közös,
   újrahasznosítható új elem sem született (a 17 leckében kb. 15 egyedi modell/szimuláció).
3. **Token: drágább lecke, olcsóbb sorozat.** A leckénkénti átlag (~204 ezer) nagyobb a 7–8. ~175 ezerénél –
   valószínűleg mert minden ügynök maga olvasta végig a két forrásleckét és a modulok buktatóit, és több volt az
   ellenőrizendő tény (a terv itt nem volt átnézve). A teljes sorozat (~4,0 M) mégis kevesebb (7–8.: ~4,5 M),
   mert nem volt adatkör, referencialecke-javítás és cserekör.
4. **A terv tényei rendszeresen hibásak – a leckeügynöki ellenőrzés működött.** 16 leckéből jött tervjavítás
   (téves szám, dátum, idézet vagy forrás; lásd „Tervhibák”), és több lecke kihagyta a forrásban nem igazolható
   adatot (09: Mátyás „1–2 milliós” bevétele, a végvárrendszer éves költsége; 10: „heti egy nap robot, 1514”; 14: az
   „impopulációs pátens (1689)”; 17: a pákozdi erőoszlop). Ez megerősíti az `EJSZAKAI-GYARTAS.md` 7. tanulságát.
   **De:** a 11 hosszú dátumsort „általános ismeretből, nem webes forrással” írt, a 15 néhány dátumot
   emlékezetből – ezeket a tanár nézze át kézikönyvvel.
5. **Több lektor kell, mint a terv gondolta.** A terv hét leckéhez kért lektort; a 07 és a 08 ügynöke maga tett a
   leckébe történészi „Szakmai ellenőrzés” blokkot (a jövedelemjegyzék, a birtokmodell, a Szent Korona-tan és a
   saját latin fordítások miatt). A szerzői jogi szabály (0. döntés 11.: modern fordítás helyett saját fordítás
   vagy parafrázis) miatt sok a saját fordítás (Hammurapi, Livius, Res Gestae, Tacitus, Biblia, Aranybulla,
   Rousseau, a Nyilatkozat, Recrudescunt, Engels, Burke stb.) – ezekhez **nyelvi/filológiai lektor** is kell. A
   06 egyszerre három szakterületet kér, és a bizonyítékmátrix 30 celláját egyenként.
6. **Vázlatos térképek 1914 előtt.** Történeti határadat 1914 előtt nincs (`TORT_HATAR` csak `mo1914hsz`
   kerettel), ezért tíz lecke kézzel rajzolt, dátumozott sokszögekkel dolgozik (04, 05, 06, 08, 09, 11, 12, 13, 14,
   17). Csak a 12 és a 17 írja, hogy atlasszal egybevetette; a 04 egybevetendőnek jelöli, a 09, 11, 13, 14
   kifejezetten nem vetette össze. A terv szerint ez tudatos (0. döntés 7.), de ha a sorozat folytatódik, egy
   kora újkori `shared/tort/` adatkör (hódoltság, Erdélyi Fejedelemség, Habsburg Monarchia) több leckét is
   pontosabbá tenne.
7. **Az érzékeny tartalom szerkesztői elvei tarthatók voltak** (a metrikasorok szerint): áldozatszám csak
   tartománnyal és forrással, effektus, számláló és „Tippelj!” nélkül (03, 10, 11, 13, 17); a 12 a Buda 1686-os
   civil áldozatszámot szándékosan kihagyta; vallások leíró keretben (03, 11); a hun–magyar azonosság
   „hagyomány”, a kettős honfoglalás „vitatott” réteg (06). Hogy ez szakmailag is megáll-e, azt csak a lektor
   mondhatja meg.

## Tanári/szakmai review-lista

### Elsőbbség – szakmai lektor kötelező (9 lecke)

A kilenc leckében a spec `"review"` mezője lektort kér, és a `<!-- Szakmai ellenőrzés: <szerep>, <dátum> -->` blokk
szándékosan **„még nincs lektorálva”** állapotú: csak valódi szakmai lektor töltheti ki. Ezek a leckék lektorálás
nélkül nem használhatók.

- **06-magyar-ostortenet** (történész + nyelvész + régész) – a bizonyítékmátrix mind a 30 cellája és a 6 státusz
  egyenként (különösen: hunok × régészet = „ellentmond”, × genetika = „részben”; kettős honfoglalás × régészet =
  „részben”; 895 × monda = „ellentmond”); a Gyuris 2025 és a Maróti 2022 eltérő forrásmodellje („vitatott”); az uráli
  és ugor szétválás tartománya; a vázlatos foltok (Magna Hungaria, Etelköz, nyelvrokonok, honfoglalás 895/900/907).
- **03-monoteizmus** (vallástörténész) – a Stark-modell és a „kb. 3–6 millió = 5–10 %” tartomány; a „birodalmi szintű
  üldözés kb. 12 év” definíciója; a hagyomány- és a forráskeret elkülönítése; a saját bibliai és latin fordítások.
- **11-reformacio** (egyháztörténész) – a négy tanításkártya és a szervezeti sémák kiegyensúlyozottsága (pl. a
  katolikus „hit és jó cselekedetek”, az unitárius megfogalmazás); a felekezeti foltok 1600 körül; a „többség
  protestáns a 16. sz. végére” állítás.
- **12-hodoltsag-merlege** (történész) – a 17 kulcsállapotú hódoltsági térkép és a kimaradt elemek; a Mohács-okok
  négy nézőpontja; a népesség 1700 körül (az Acsády-féle régi becslés elvetése).
- **13-francia-forradalom** (történész) – az időben változó intézményséma egyszerűsítései; a jakobinus diktatúra
  kezdete; a Greer-statisztika (másodlagos forrásból) és az összes áldozat 35–45 ezres tartománya; Robespierre
  értékelés nélkül.
- **14-ujranepesules** (történész) – a betelepítés szándékának két nézőpontja; a bevándorlás nagysága (kb. 1 M vs.
  „több mint 3 M”); a kuruc foltok, a Temesi bánság és a Határőrvidék vázlata.
- **17-forradalom-1848** (történész) – a havi ellenőrzési foltok (13 csempe × 12 hónap) hónaponként; az 1849. nyári
  erőbecslések és a megtorlás számai (Hermann Róbert eredeti tanulmányával).
- **07-arpad-kori-allam** (történész, a lecke kéri) – a birtokmodell tartományai; a jövedelemjegyzék keltezése és
  összevetése; a 31. cikkely és a striga-cikkely saját fordítása; a két nézőpont II. Andrásról.
- **08-anjou-gazdasag** (történész, a lecke kéri) – a tartományúri foltok; az aranytermelés és a harmincad vitatott
  értékei; a Szent Korona-tan két nézőpontja; a falumodell.

### Tervhibák (a koordinátori terv nem megbízható forrás – ezeket nézze először a tanár)

A terv tényei nem voltak külső forrásban átnézve (0. döntés 13.). A leckeügynökök javításai, tömörítve:

- **01** – „kétszáz évvel Kleiszthenész után” = pontosan 178 év (a forráskártya ezt számolja).
- **02** – „nullum crimen sine lege” helyett „nulla poena sine lege”, és az sem római (Feuerbach, 1801); az „egyéb 5
  centuria” = 2 fabri + 2 kürtös + 1 proletarii; Caesar „dictator perpetuo” napja ismeretlen (csak a hónap); a Kr. e.
  70-es census tartomány (900–910 ezer); a köztársaság kezdete Kr. e. 509 (a kerettanterv 510-et ír – a panel kimondja).
- **03** – a Szentháromság-tant nem 325 zárta le (a Szentlélekről 381 szólt); a „milánói rendelet” nem ediktum, hanem
  megállapodás (Licinius levele); Diocletianus üldözése Keleten 313-ig tartott; a 300 körüli „kb. 10 %” helyett
  „kb. 3–6 millió = 5–10 %” három szerzővel.
- **04** – a terv csúcsértékei (Róma 117: 5,0; hunok 441: 4,0; kalifátus 720: 11,1 millió km²) helyesek; Poitiers
  732/733 „vitatott”.
- **05** – Adalbero költeménye kb. 1025–1030 (nem 1027–1031); a nagy éhínség halálozása kb. 10–15 % (az „5–12 %” nem
  igazolható); a vázlat kitalált reálbér-sora helyett Clark 2007; az angliai 1500-as népességpont interpoláció volt –
  kivéve.
- **06** – Szeifert 2022 a Human Molecular Genetics-ben jelent meg (nem a Communications Biology-ban); a tehén és a kecske
  szófejtése vitatott – kimaradt; az ugor szétválás Kr. e. 2000–500 (nem csak a Kr. e. 1. évezred); a Brenta-csata
  napja forrásonként eltér – csak az év; új forrás a tervhez képest: Gyuris és mtsai 2025 (Cell).
- **07** – III. Béla jövedelemjegyzéke nem „1185–1186”, hanem 1185–1195 között vitatott; a birtokszerkezetre nincs szám
  a forrásokban (modell-sáv); a „serviens” = „nemes” régi fordítás – saját fordítás a latinból. Eltérés: nincs
  püspökség-/vármegyetérkép (az 5–6. kulcsvizuálja), helyette folyamábra; `TortTerr` nem kellett.
- **08** – a jövedelemfolyamok célja Visegrád (1323-tól), nem Buda; a 18 dénáros kapuadó 1338/39-től (1336: 3 garas);
  a harmincad Anjou-kori mértéke vitatott; a 2–2,5 t aranytermelés régebbi, magas becslés.
- **09** – Mátyás átlagos évi bevétele kb. 628 ezer (500–750 ezer) aranyforint, nem 650 ezer / 800–900 ezres csúcs; a
  „Bonfini szerinti 1–2 millió” forrásban nem található – kimaradt; a fekete sereg kb. 9–15 ezer (nem 8–10 ezer); a
  végvárrendszer éves költségére nincs megbízható szám (a lecke kimondja, modellel válaszol).
- **10** – a tordesillasi vonal hosszúságát a szerződés nem rögzíti (vázlatosan kb. 46,6° Ny); a „heti egy nap robot,
  1514” nem igazolható – kimaradt; az 1569-es csőd kimaradt.
- **11** – a „cuius regio, eius religio” formula Joachim Stephanitól ered, évszáma forrásonként eltér – „évtizedekkel
  később”.
- **12** – a végvári költség nem „évi 1–1,5 millió, a bevételek harmada–fele”, hanem zsold 1,3–1,6 / összesen 1,7–2,1
  millió rajnai forint, a bevétel a zsold 25–30 %-át fedezte; a népesség 1700 körül kb. ötödével nőtt (nem
  „stagnált”; a „1720: kb. 4 millió” Horvátország nélküli adat); az emlékkő felirata „Hős ellenfél volt békesség
  vele!”; Schulhof krónikájának fordítása nem közkincs – parafrázis.
- **13** – a „Nem értek egyet veled, de…” nem Voltaire-é (E. B. Hall, 1906); a terror összes áldozata kb. 35–45 ezer
  (nem 35–40); 1812-ben Osztrák Császárság (nem „Habsburg Birodalom”); 10 lépés 9 helyett.
- **14** – a majtényi fegyverletétel 1711. ápr. 30. (máj. 1. a béke aláírása); a Recrudescunt 1703/1704; az
  „impopulációs pátens (1689)” nem ellenőrizhető – helyette az 1723. évi CIII. tc.; a bevándorlás nagysága vitatott.
- **15** – a T-modell ára nem „1908: 850” (a Houston-tábla 1909-től: 825/850); **„tízszer olcsóbb” dollárban nem igaz**
  (kb. 3,2×), munkaórában kb. 9× – ezért módosul a cím; 12 ó 28 p → 1 ó 33 p munkaidő, nem átfutási idő; a brit vasút
  1840-ben kb. 2650 km (nem 2400); Chadwick 57 %-a a halálesetek, nem a születettek 57 %-a; a szén 1854 előtti
  becslése kimaradt.
- **16** – a felsőtábla nem szavazott, a nádor „mérlegelt”; Kölcsey 1835-ben mondott le (a „Szatmár új utasítás 1834.
  nov. 10.” pontatlan); a Lánchíd-törvény 1836:XXVI. (nem IV.); Lőw Lipót első magyar prédikációja 1845 (nem 1844);
  a Hitel-idézet szövege eltért; 1834. dec. 10.: hivatalosan 22 : 26, a forrás csak 24 „nem” megyét nevez meg.
- **17** – a választók aránya kb. 6 % (nem 7–9 %); Aradon 12 tábornok + 1 ezredes (nem 13 tábornok); a zsidókat a
  „bevett vallás” feltétele zárta ki, nem külön szakasz; a pákozdi erőoszlop és az urbárium robotnapszámai kimaradtak
  (nincs összevethető forrás).

### Leckénként

Zárójelben a pontok száma (összesen 119); a „lektor kötelező” tétel egy pontnak számít. A tételek a metrikasorok
„Review” részeiből valók, tömörítve; a tervhibák fent.

- **01-polisz-demokracia** (8): a §196–205 és §215–217 saját fordítása (King + Harper alapján) – kiadással vetendő össze ·
  a három társadalmi csoport magyar neve · Hammurapi uralkodása középső kronológia szerint („vitatott”) · a sematikus
  Attika nem térkép, a 30 harmad helye jelképes · a régi 4 phülé elvontan · a 100 pöttyös polgárrács arányai modell ·
  a napidíj „valószínűleg 2 obolosz” · a részvételi arány (12–24 %) egyszerűsített; a cserépszavazás 6000-es
  küszöbének két értelmezése
- **02-romai-koztarsasag** (6): Livius, Res Gestae 34, Tacitus Ann. I. 2 és Cicero saját fordítás – nyelvi lektor ·
  a polgárok osztályonkénti aránya kitalált (modell) · a „Marius-reform” és a census-ugrás értelmezése vitatott · a
  limes a Duna mai medre (vázlatos) · a 6. lépés sémájában a princeps „irányít” nyila átfut a dictator dobozán ·
  509 vs. 510 (panelen kimondva)
- **03-monoteizmus** (5): **vallástörténész lektor kötelező** · a Stark-táblázat a nyomtatott kötettel vetendő össze ·
  minden idézet saját fordítás (5Móz 6,4; Mk 12,31 / 3Móz 19,18; Tacitus Ann. 15,44; Plinius Ep. X,97) · a
  „birodalmi szintű üldözés kb. 12 év” definíciós kérdés · hagyomány- és forráskeret elkülönítése
- **04-hodito-birodalmak** (7): a birodalom-foltok saját vázlatok – atlasszal vetendők össze (hun befolyási övezet,
  Frank 511/565, Bizánc 650/800) · a vándorlási és hódítási nyilak vázlatosak · a Keletrómai 450-es érték kihagyva,
  a 350→500 szakasz szaggatott · a Taagepera 1979-es adat csak másodlagosan · Priszkosz parafrázisként; a
  dzsizja/áttérés-kártya minőségi állítás · Kelet-Ázsia nincs a leckében · Poitiers 732/733
- **05-rendi-tarsadalom** (6): a jobbágy-költségvetés modell (4 ha, 160 kg/ha, 5 fő × 220 kg, heti 2 robotnap) –
  nagyságrend · a „kilenced” magyar intézmény nyugati példaként · Adalbero latin sorai emlékezetből, kiadással nem
  vetve össze · a rendek arányai nagyságrendi becslések · a pestis-foltok vázlatosak, az érkezési hónapok ± 1 · a
  népesség-leolvasás két adatpont közt interpolál
- **06-magyar-ostortenet** (8): **történész + nyelvész + régész lektor kötelező** · a bizonyítékmátrix 30 cellája és 6
  státusza egyenként · Gyuris 2025 vs. Maróti 2022 („vitatott”) · Szubbotci keltezése · Magna Hungaria, Etelköz, a
  nyelvrokonok területe, a honfoglalás kulcsállapotai és a hegygerincek kézi vázlatok · „a helyi népesség nyelvileg
  beolvadt” a „valószínű” oszlopban · a nyelv–gén modell számai kitaláltak („modell”) · az uráli és ugor szétválás
  tartománya
- **07-arpad-kori-allam** (7): **történész lektor kötelező** (a lecke kéri) · a birtokmodell tartományai (királyi 55–80
  % → 10–30 %) · saját fordítás: Aranybulla 31. cikkely, Kálmán striga-cikkelye · a 10 cikkely-kártya parafrázisa és
  csoportosítása · a két nézőpont II. Andrásról · a házassági helyek jelképesek, néhány év ± 1–2 · a jövedelemjegyzék
  márkás összevetése csak nagyságrendi
- **08-anjou-gazdasag** (7): **történész lektor kötelező** (a lecke kéri) · a tartományúri foltok kézi vázlatok · a 4.
  lépés falumodellje kitalált · a koronázás-tábla „részben” cellája (1301) · a „kilenced a király adója” tévhit
  megfogalmazása · a Szent Korona stilizált rajz · a Szent Korona-tan két nézőpontja
- **09-hunyadiak-torok** (7): a politikai térkép erősen vázlatos, atlasszal nem vetve össze · a végvárláncok pontjai
  reprezentatívak · a 6. lépés zsold-modellje egész évre számol · 1 Ft ≈ 1 dukát · Bonfini csak forráskritikai
  kártyán · a tévhit-cáfolatok és az oszmán nézőpont kártyái · a végvárrendszer költségére nincs szám (kimondva)
- **10-arforradalom** (7): Hamilton 1934 nem volt elérhető – az évtizedes ezüstsor recenzióból rekonstruált · a
  spanyol árindexnek csak 4 pontja van · a „népirtás-vita” két álláspontja, áldozatszám csak tartománnyal · a 7.
  lépés kitalált példa, az 5. modell · az Elba–Lajta vonal vázlatos tendencia · az útvonalak vázlatosak, az ezüstút
  vonalvastagsága becslés · a tordesillasi vonal kb. 46,6°-on
- **11-reformacio** (8): **egyháztörténész lektor kötelező** · a négy tanításkártya és a szervezeti sémák egyszerűsítése
  · a felekezeti foltok (Európa, Kárpát-medence, 1600 körül) kézi vázlatok, atlasszal nem vetve össze · az Erdélyi
  Fejedelemség határa (1570 utáni vázlat) · a falumodell kitalált · „a lakosság többsége protestáns a 16. sz. végére” ·
  a barokk homlokzat illusztráció · **a dátumsor egy része „általános ismeretből”, nem webes forrással** (Luther,
  Kálvin, Worms, Trento, Pázmány, Vizsolyi Biblia stb.)
- **12-hodoltsag-merlege** (8): **történész lektor kötelező** · a hódoltság/Erdély/Thököly sokszögei kézi vázlatok 17
  kulcsállapotban · kimaradt: Erdély 1551–1556, Esztergom/Győr/Veszprém ide-oda kerülése, Bethlen hét vármegyéje, a
  kettős adózású peremsáv, a horvát végek · a Mohács-okok négy nézőpontja rangsor nélkül · a kettős adó modell
  arányai kitaláltak · Schulhof és Dietz keletkezési éve becslés · Buda 1686 civil áldozatszám szándékosan nincs · a
  Thököly-folt címkéje a 9. lépés kis térképén nem mindig jelenik meg
- **13-francia-forradalom** (8): **történész lektor kötelező** · az intézményséma egyszerűsít (vétó 1789 óta,
  bizottságok 1794, fructidor 1797, konzulátus) · a jakobinus diktatúra kezdete vitatott (a sáv jún. 2-át mutatja) ·
  a Greer-összetétel másodlagos forrásból · az 1812-es térkép kézi vázlat · a Rajnai Szövetség, Svájc, Portugália
  felirata csak kattintásra · az USA-séma „leválthatja” éle egyszerűsít · az aktív polgárok 4,3 milliója általánosan
  idézett, nem ellenőrzött szám
- **14-ujranepesules** (8): **történész lektor kötelező** · a betelepítés szándékának két nézőpontja · a kuruc foltok,
  a Temesi bánság és a Határőrvidék kézi vázlat · a nyilak útvonala és időzítése a lecke választása · a visszavonás
  1790. jan. 28. (a hu-wiki nem adja meg) · a kettős vámhatár vámtételei kitaláltak · a Recrudescunt magyar sora saját
  fordítás · a bevándorlás nagysága vitatott (kb. 1 M vs. több mint 3 M)
- **15-iparosodas** (7): a futószalag-szimuláció modell (csak a két végpont mért) · a 7. lépés 100 pöttye modell
  (gyerekhalottak átlagkora 1,5 év feltevés) · emlékezetből írt adatok (Newcomen, Watt, Liverpool–Manchester,
  Edison, Great Stink, Alkali Act, New York 1900) – kézikönyvvel vetendők össze · a négy eszme-idézet saját fordítás –
  nyelvi lektor; a Constant-idézet második fele nem a teljes szövegből · a szocializmus a kerettanterv 11.
  témakörében nincs (a koordinátor kérte) · a hullám-besorolás tankönyvi · a Manchester-szegregáció Engels
  leírásából készült vázlat
- **16-rendi-orszaggyules** (6): az örökváltság-számoló kiinduló értékei (modell) · az 1834-es megyei szavazatlisták
  másodlagos összesítésből – levéltári ellenőrzés javasolt · az örökváltsági szerződések számára nincs adat
  („kevés”) · a Felelet „második útja” inkább Wesselényi (vitatott) · Széchenyi 1842-es beszéde másodlagos
  irodalomból · a TortParl színei rendi csoportot jelölnek, nem pártot
- **17-forradalom-1848** (6): **történész lektor kötelező** · a havi ellenőrzési foltok vázlatok, frontvonalnak nem
  alkalmasak · az 1849. nyári erőbecslések és a megtorlás számai Hermann Róbert eredetijével · a 3. lépés „1 % szavazó
  nemes” saját modell · a 4. lépés 100 kévéje modell · a nemzetiségi követelések rövidített összefoglalások

## Kerethasználat (becslés)

**A felhasználó mérése (heti keret % a gyártás előtt és után) erre a sorozatra hiányzik** – az alábbi szám a
2026-11-23-i mérésből (`EJSZAKAI-GYARTAS.md`: ~35 % heti keret / 79 lecke ≈ **0,45 %/lecke**, ~7 %/sorozat;
~18 805 ezer token ≈ 35 % → ~537 ezer token / 1 %) becsült, nem mért érték.

| Becslés | Heti keret (kb.) |
|---|---|
| leckeszám szerint: 17 lecke × 0,45 % | **~7,7 %** |
| token arányában: terv + leckék, 3 617 ezer token | **~6,7 %** |
| + egységesítés (becslés ~200 ezer token) | ~7,1 % |
| + ez az összesítés (becslés ~200 ezer token): ~4 017 ezer token | **~7,5 %** |

A felhasználó ezt a sorozatot a heti keret-reset előtti utolsó órára, a maradék kb. 9 %-ra időzítette. A becslés
szerint belefért (kb. 1,5 % tartalékkal), de a koordinátor fő munkamenete – ebben a módban 17 párhuzamos ügynök
indítása és követése – egyik sorban sincs benne. A terv becslése (6.1: 7,5–8 %) a leckeszám szerinti értékkel
egyezik.
