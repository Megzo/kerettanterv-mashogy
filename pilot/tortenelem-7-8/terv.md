# Pilot: Történelem 7–8. – a leckesor terve

Forrás: [`kerettanterv/tortenelem/7-8.md`](../../kerettanterv/tortenelem/7-8.md) (NAT 2020, általános iskola,
14 témakör, 124 óra + 12 óra szabad mélyítés). Az idézetek szó szerint onnan valók, a forrás elírásaival együtt. A
zárójeles szám (pl. „(13.)”) azt jelzi, ha az idézet nem a lecke fő témaköréből jön. A lecke-formátum leírása:
[`leckek/SZERZODES.md`](../../leckek/SZERZODES.md). A tantárgyi kiegészítő szabályok kész szövegként a 7. fejezetben
vannak; ugyanez a szöveg a `SZERZODES.md` 20. fejezete. Az 5–6. évfolyamos előzmény:
[`pilot/tortenelem-5-6/terv.md`](../tortenelem-5-6/terv.md) – annak 4. fejezete (szerkesztői elvek) itt is érvényes,
az 1.3 pont kiegészítéseivel.

Jelölések az „Adatok” pontokban:
- *(becslés)* – a forrás tartományt ad, vagy a szám kerekített nagyságrend; a leckében is ki kell mondani.
- *(vitatott)* – a szakirodalomban több érték él; a lecke tartományt vagy két forrást mutat.
- *(ellenőrizendő)* – gyártás előtt forrásban ellenőrizni kell (a terv emlékezetből vagy másodlagos forrásból írta).
- *(modell)* – a lecke didaktikus modellje, nem mért adat.
- *(kitalált példa)* – szemléltető adat, a `.md`-ben is így jelölve.

Ahol egy számot a terv számolt, ott a számolás is szerepel. A tényeket két önálló ellenőrző kör nézte át
(2026-11-25, a forrás-URL-ek az adott pontnál). A koordinátori brief nem megbízható forrás
(`pilot/EJSZAKAI-GYARTAS.md`, 7. tanulság): a leckeügynök minden számot ellenőriz, és az eltérést a jelentésében jelzi.

## 0. Döntések a felhasználó távollétében

A felhasználó nem volt elérhető, ezért ezekben magam döntöttem. Mind visszavonható.

1. **Mappa- és slugnevek.** Terv: `pilot/tortenelem-7-8/terv.md`; leckék:
   `leckek/tortenelem-7-8/NN-slug.{md,html,content.js}`. A metaadat-sor:
   `tantárgy: Történelem · évfolyam: 7–8. · témakör: N. <a kerettanterv témakörének címe>` (a
   `tools/build_index.py` `SUBJECTS` listája – „Történelem”, `tortenelem` – és a `7–8` évfolyam-oszlop ezt már
   ismeri). **A slugok az egész repóban egyediek** (a QA alapértelmezett mappája `build/qa/<slug>/`). Ellenőrizve a
   166 meglévő sluggal: nincs ütközés. Közeli, de eltérő: `foldrajz-9-10/10-nepesseg` (≠ `15-nepesedes`),
   `foldrajz-9-10/14-penz` (≠ `06-pengo`), `tortenelem-5-6/18-gozgep`, `19-marcius-15`, `20-szabadsagharc`.
2. **17 lecke.** A 124 órából a legnagyobb témakörök több leckét kapnak: 9. (20 óra) → 3 lecke (11, 12, 13),
   3. (11 óra) → 2 (03, 04), 6. (10 óra) → 2 (07, 08). A többi témakör egy-egy leckét kap, a 13. (Régiók, 14 óra)
   és a 14. (Mérlegen, 8 óra) csak részben (6.2). Az elv: **ahol egy szám, egy térkép vagy egy folyamat
   mozgásban többet mutat, mint egy felsorolás** – határváltozás népességadattal, front dátum szerint, infláció
   logaritmikus skálán, korfa, választási rendszer kalkulátorral, hatalmi ágak kapcsolókkal.
3. **Szókorlát: 55 szó** (a szerződés alapértéke, nincs `maxWords` a spec-ben). A 12–14 évesek bírják, de a
   panel célja 40–50 szó; a hosszabb magyarázat a vászonra (forráskártya, adatkártya) kerül.
4. **Történeti határok: saját, levezetett adatfájl.** Két új közös adatfájl készül a 0. kötegben (külön
   előkészítő lépés, nem leckeügynök): `shared/tort/map-torthatar.js` (Kárpát-medence 1:10m + Európa 1:50m
   történeti egységek) és `shared/tort/map-europa.js` (Európa-alaptérkép 1:50m, Skandináviával és a Volgával).
   Módszer: **a Natural Earth (közkincs) mai közigazgatási egységeinek uniója**, és ahol a történeti határ nem
   esik egybe mai egységhatárral, **kézi vágóvonal** a build-szkriptben (töréspont-táblázat, forrással
   kommentezve). Minden történeti egység „vázlatos” jelű. A leckék a hivatalos **területet és népességet az
   `### Adatok`-ból** mutatják, soha nem a sokszögből számolva. Részletek: 4.2. A HistoGIS (ÖAW, licence nem
   tisztázott), a CShapes 2.0 (CC BY-NC-SA – a licenc nem keverhető) és a tankönyvi atlaszok **csak vizuális
   ellenőrzésre** használhatók, adatot nem adnak. Az OpenHistoricalMap (CC0) használható forrás, ha az adott
   határ ott megvan és ellenőrzött – ezt az előkészítő lépés dönti el, és a `.md`-forrássorba írja.
5. **Négy új modul:** **TortTerr** (történeti területek, dátum szerinti hovatartozás, frontvonalak; ref.
   `07-masodik-vilaghaboru`), **TortCity** (vázlatos Budapest-alaptérkép: Duna, szigetek, hidak évszámmal,
   körutak, városhatár; ref. `02-dualizmus`), **TortParl** (parlamenti patkó, mandátumszámító; ref.
   `16-demokracia`), **TortState** (intézményséma: ki választ, ki ellenőriz, kapcsolók dátummal; ref.
   `16-demokracia`). Átvett kész modul: TtTipp, TortMap, TortTimeline, TortSource, TortCards, TortScene,
   FoldChoro, FoldChart, MatChart, TortGlobe, BioPlot (4.1).
6. **Érzékeny leckék: szakmai lektor kötelező.** A `08-holokauszt` spec-je `"review": ["történész",
   "emlékezetpedagógus"]`; a `04-trianon`, `05-diktaturak`, `07-masodik-vilaghaboru`, `10-szovjetizalas`,
   `11-forradalom-1956`, `13-rendszervaltas`, `14-hataron-tul` spec-je `"review": ["történész"]`. A build ettől
   kéri a `<!-- Szakmai ellenőrzés: … -->` blokkot. A tanári review ezen felül mindegyiknél kötelező.
7. **Holokauszt, népirtás, háborús áldozatok: méltóság, nincs játékosítás.** Nincs pontszám, nincs
   „Tippelj!” áldozatszámra, nincs látványos robbanás, nincs csúszka, amely áldozatszámot „játszik le”, nincs
   vér, nincs kitalált áldozati történet. Az áldozatszám mindig forrással és tartománnyal áll. A deportálás
   térképe gombnyomásra, zónánként, lassan halad (nem csúszka). A 08-ban a „Tippelj!” csak forráskritikai kérdés
   lehet (pl. „melyik iratból tudjuk a számot?”).
8. **Trianon: tény és két nézőpont.** A kerettanterv a „trianoni békediktátum” kifejezést használja. A lecke a
   szerződés hivatalos nevét („trianoni békeszerződés”, 1921. évi XXXIII. tc.) használja, és egy lépésben
   elmagyarázza, miért nevezi a magyar szóhasználat diktátumnak (a vesztes fél nem tárgyalhatott, népszavazás
   csak Sopronban volt). Megmutatja a győztesek és az utódállamok érvelését (népek önrendelkezése, a nemzetiségi
   többség a lakott területeken) és a magyar érvelést (etnikai elv következetlen alkalmazása, 3,2–3,3 millió
   magyar anyanyelvű határon túl, gazdasági egység szétvágása). Sem revizionista („igazságtétel”), sem
   lekicsinylő hangnem. Az 1910-es anyanyelvi adat mellett ott a forráskritika (anyanyelv ≠ nemzetiség,
   asszimilációs nyomás, a zsidóság magyar anyanyelvűként számolva) és az utódállamok 1920–1930-as
   népszámlálása.
9. **Semlegesség 1990 után.** Pártpolitikai semlegesség; élő politikust nem értékelünk. 1990 után csak
   intézmény, alkotmányos működés és adat. Kormányfők neve csak tényszerű címkeként az idővonalon (név,
   hivatali idő), mondat nélkül. A rendszerváltás leckéje 2004-gyel zárul (EU-csatlakozás); a 16 az Alaptörvényt
   és a választási rendszert intézményként mutatja. Az 1990-es választás eredménye szürke árnyalatokban, a
   pártok mai színei nélkül. A választási kalkulátor **kitalált pártokkal** dolgozik („A párt” … „D párt”), az
   egy színárnyalat sávjaiból és mintázatból kevert jelöléssel, hogy egyik se hasonlítson mai pártszínre.
10. **Szerzői jog: 70 éves szabály.** Szó szerint csak közkincs szöveg idézhető: a szerző 70+ éve halt meg (2026-ban:
    1955 vagy korábban), vagy hivatalos jogszabály- és szerződésszöveg. Fordításnál a fordítóra is ez vonatkozik –
    ha nincs közkincs magyar fordítás, **saját fordítás** áll („saját fordítás” megjelöléssel). Fotó, plakát,
    karikatúra, festmény nem kerül be; minden vizuál saját rajz. Élő vagy 70 évnél frissebben elhunyt szerzőtől
    (pl. Churchill † 1965, Kádár János † 1989, Márton Áron † 1980) legfeljebb egy-két mondatos idézet forrással a
    TortSource kártyán, inkább parafrázis. Önkényuralmi jelkép (horogkereszt, nyilaskereszt, sarló-kalapács,
    vörös csillag) **nem rajzolódik ki**; a nevét a szöveg mondja, a vásznon semleges „jelkép” helyőrző áll.
11. **Számformátum magyarul:** tizedesvessző, valódi mínuszjel (−), ezres tagolás nem törő szóközzel
    (`19 300`, a build a `U+202F`-et teszi be), dátum „1944. március 19.”, évtized „1930-as évek”, százalék
    „54,5 %”. A pénzösszegek: „12 500 korona”, „400 000 kvadrillió pengő”; a hatványalak (`4 · 10²⁹`) csak a
    `06-pengo` logaritmikus tengelyén.
12. **Sorrend és kronológia.** A leckék számozása időrendi; a gyártás a modulfüggőség szerint halad (6.1). A
    2. kötegtől minden lecke a 0. köteg adatfájljaira épül, ezért a 0. köteg előfeltétel.
13. **A Közel-Kelet kimarad.** A 13. témakör Közel-Kelet-altémája folyamatban lévő fegyveres konfliktus, amelyhez
    külön szerkesztői irányelv kell (6.2). Izrael Állam megalapítása (1948) a hidegháborús idővonalon tényként
    szerepel.

---

## 1. Bevezető

A 7–8. évfolyam a 20. század: két világháború, két totális diktatúra, Trianon, a holokauszt, 1956, a Kádár-rendszer
és a rendszerváltoztatás – a legtöbb vitatott, a családi emlékezetben élő anyag a teljes tantervben. A leckék
mércéje ezért kettős: **látványos belátás** (az animáció mutasson meg valamit, ami szövegből nem jön át) és
**szerkesztői fegyelem** (forrás, tartomány, nézőpont, méltóság).

### 1.1 Hol ad egy animáció *valódi* belátást ebben a tárgyban?

| Belátás | Hogyan | Lecke |
|---|---|---|
| A határ nem vonal, hanem emberek | 1914 → 1920 térkép, az elcsatolt részek kiúsznak, mindegyiken terület + népesség + anyanyelvi kördiagram | 04, 14 |
| Mozgó és álló front | dátumcsúszka: a nyugati front 3 év alatt alig mozdul, a keleti száz kilométereket | 03, 07 |
| Mit jelent a hiperinfláció | logaritmikus tengely, ahol minden osztás tízszeres ár; „15 óránként duplázódó ár” | 06 |
| Hogyan bontható le egy demokrácia | intézményséma, amelyben dátummal kapcsolnak ki egy-egy „ellenőrzést” | 05, 10, 13 |
| A választási rendszer nem arányos | kalkulátor: ugyanazok a szavazatok más szabállyal más parlamentet adnak | 16 (10, 13) |
| A népesség szerkezete emlékezik | a magyar korfa 1950 → 2020: a Ratkó-korszak „púpja” felfelé vándorol | 15 |
| Az eladósodás üteme | adósság-görbe 1970–1990, a titkolt és a később közölt adatsor | 12 |
| Egy város története | Budapest hídjai, körútjai, határa évszám szerint; 1956 helyszínei óráról órára | 02, 11, (07, 08) |
| Kétpólusú világ | blokktérkép évről évre; a robbanófejek száma két görbén | 09 |
| Fogyó közösségek | a határon túli magyarság népszámlálásról népszámlálásra, régiónként | 14 |

### 1.2 Kiválasztási elv

- **Témakörönként legalább egy lecke**, kivéve a 13. Közel-Kelet- és India–Kína-altémáit és a 14. „Lábnyomaink”
  altémáját (6.2, tartalék).
- **A fogalomlista legyen a vásznon**, nem a panelen: a kerettanterv „Fogalmak” sorainak legalább fele minden
  leckében megjelenik feliratként, kártyán vagy diagramcímként.
- **„Honnan tudjuk?”** minden leckében (az 5–6. évfolyam szabálya): ki írta, mikor, milyen céllal; a 20. századnál
  ehhez jön a **statisztika forráskritikája** (ki számolt, milyen kategóriával, mit titkoltak).
- **A tanári review gyorsítása:** minden szám, dátum, helyszín az `### Adatok` alatt van; a geometria (határ, front,
  Duna-vonal) a kódban, a tanár jelezni tudja.

### 1.3 Szerkesztői elvek (az 5–6. évfolyam 4. fejezetén felül)

1. **Vitatott kérdések: több nézőpont, jelölt bizonytalanság.** Ahol a szakma vitatkozik (áldozatszámok,
   felelősség megoszlása, „mi lett volna, ha”), a lecke tartományt és legalább két forrást mutat, és értékítélet
   helyett **forrást, adatot, kérdést** ad. A kerettanterv értékelő fejlesztési feladatait („Ítélet megfogalmazása…”,
   „Érvelés a 20. század kirekesztő ideológiáival szemben”) a lecke kérdésként adja tovább a tanárnak, a vászon
   tényt mutat. A népirtás és a háborús bűn ténye nem vita tárgya: ezt a lecke kimondja.
2. **Semlegesség** (0. döntés, 9.).
3. **Méltóság** (0. döntés, 7.). Áldozatokat számmal és – ahol közkincs vagy dokumentált forrás van – névvel,
   hellyel mutatunk; az embermentőket névvel, tettel, forrással.
4. **Trianon** (0. döntés, 8.).
5. **Szerzői jog** (0. döntés, 10.).
6. **Térképek** (0. döntés, 4.): történeti határ csak a `map-torthatar.js`-ből vagy a leckében kézzel, „vázlatos”
   bélyeggel és dátummal; mai határ csak halvány, kikapcsolható, „mai határok” feliratú réteg. Helynév: a korabeli
   magyar név, első említéskor a mai hivatalos névvel (Kassa – ma Košice; Újvidék – ma Novi Sad).
7. **Számformátum** (0. döntés, 11.).
8. **Felelősség pontos alanya.** „A németek” helyett „a náci Németország”, „az SS”; „a magyarok” helyett „a magyar
   kormány”, „a csendőrség”, „a közigazgatás”; „a szovjetek” helyett „a szovjet hadsereg”, „az NKVD”. Ez a
   kollektív bűnösség elkerülésének eszköze minden irányban (németek kitelepítése, Beneš-dekrétumok, délvidéki
   megtorlások).

---

## 2. A leckék

| # | slug | cím | témakör | építőkocka | nehézség (1–3) |
|---|---|---|---|---|---|
| 01 | `01-nemzetallamok` | Miért akart minden nép saját államot? – nemzetállamok, nagyhatalmak, eszmék | 1 (+13) | TortTerr, FoldChoro, MatChart, TortCards, TortSource, TortMap, TtTipp | 2 |
| 02 | `02-dualizmus` | Hogyan lett Pestből és Budából világváros? – a dualizmus kora | 2 (+14) | **TortCity** (ref.), TortMap, FoldChart, MatChart, TortTimeline, TortCards, TtTipp | 3 |
| 03 | `03-elso-vilaghaboru` | Miért nem mozdult a front négy évig? – az első világháború | 3 | TortTerr (front), TortMap, TortScene, FoldChart, TortSource, TtTipp | 3 |
| 04 | `04-trianon` | Mit vesztett el az ország 1920-ban? – a trianoni békeszerződés | 3 (+10, +14) | TortTerr, TortMap, MatChart, TortTimeline, TortSource, TtTipp | 3 |
| 05 | `05-diktaturak` | Hogyan bontható le egy demokrácia lépésről lépésre? – totális diktatúrák | 4 | TortState, TortParl, TortTerr, TortCards, TortMap, TortSource, TtTipp | 3 |
| 06 | `06-pengo` | Mennyit ért a pengő? – a Horthy-korszak és a nagy infláció | 5 (+8) | FoldChart (log), MatChart, TortTimeline, TortSource, TtTipp | 2 |
| 07 | `07-masodik-vilaghaboru` | Hogyan mozgott a front 1939 és 1945 között? – a második világháború | 6 | **TortTerr** (ref.), TortMap, TortCity, TortTimeline, FoldChart, TortGlobe, TortSource, TtTipp | 3 |
| 08 | `08-holokauszt` | Hogyan vezetett a jogfosztás a népirtásig? – a holokauszt | 6 (+4, +5) | TortTerr, TortCity, TortTimeline, TortSource, TortMap, MatChart | 3 |
| 09 | `09-hideghaboru` | Hogyan osztotta ketté Európát a vasfüggöny? – a hidegháború | 7 (+13) | TortTerr, FoldChart, TortMap, TortTimeline, TortGlobe, TortSource, TtTipp | 3 |
| 10 | `10-szovjetizalas` | Hogyan lett a többpártrendszerből egypártrendszer? – Magyarország 1945–1953 | 8 | TortParl, TortState, TortMap, TortTerr, TortTimeline, TortSource, TtTipp | 3 |
| 11 | `11-forradalom-1956` | Mi történt 13 nap alatt? – az 1956-os forradalom és szabadságharc | 9 | TortCity, TortTimeline, TortMap, MatChart, TortSource, TtTipp | 3 |
| 12 | `12-kadar-rendszer` | Hány évet kellett várni egy autóra? – élet a Kádár-rendszerben | 9 | FoldChart, TortState, MatChart, TortCards, TortSource, TtTipp | 2 |
| 13 | `13-rendszervaltas` | Hogyan omlott össze egy év alatt a keleti blokk? – a rendszerváltoztatás | 9 (+13) | TortTerr, TortState, TortParl, TortTimeline, FoldChart, TortSource, TtTipp | 3 |
| 14 | `14-hataron-tul` | Miért lettek kevesebben a határon túli magyarok? – együttélés a Kárpát-medencében | 10 (+14) | TortTerr, FoldChoro, FoldChart, MatChart, TortTimeline, TortSource, TtTipp | 3 |
| 15 | `15-nepesedes` | Miért lett nyolcszor annyi ember 200 év alatt? – népesedés és társadalom | 11 | FoldChart (korfa), BioPlot, MatChart, TortTimeline, TtTipp | 2 |
| 16 | `16-demokracia` | Ki dönt, és ki ellenőrzi? – a demokratikus állam és a választás | 12 | **TortParl** (ref.), **TortState** (ref.), TortCards, TtTipp | 3 |
| 17 | `17-europai-unio` | Hogyan lett hat országból huszonhét? – az Európai Unió és Közép-Európa | 13 (+14) | TortTerr, FoldChoro, TortTimeline, TortState, FoldChart, TtTipp | 2 |

Nehézség = gyártási nehézség: 1 = egy fő vizuál, kevés adat; 2 = kész modulokra épülő közepes szimuláció vagy új
interakció; 3 = új modul, összetett térkép/szimuláció vagy kényes tartalom (lektor).

**Témakörönként** (óra → lecke): 1 (5) → 01 · 2 (7) → 02 · 3 (11) → 03, 04 · 4 (5) → 05 (+08) · 5 (9) → 06 (+04:
Horthy kormányzóvá választása, +08: numerus clausus) · 6 (10) → 07, 08 · 7 (5) → 09 · 8 (10) → 10 (+06: 1946) ·
9 (20) → 11, 12, 13 · 10 (8) → 14 (+04, +10: kitelepítés) · 11 (5) → 15 · 12 (7) → 16 · 13 (14) → 17 (+09: USA,
+13: Közép-Európa, +01: USA létrejötte) · 14 (8) → részben 02, 04, 14, 17 (tartalék: Lábnyomaink).

---

## 3. Briefek

Közös minden briefben (a 7. fejezet szabályai szerint):

- **Tippelj!** – legalább egy jóslat a kipróbálás *előtt* (2–4 válasz a TtTipp-pel, a megoldás a választásig rejtve).
  Rossz tipp után: „Sokan gondolják így – nézzük meg!” **Kivétel:** áldozatszámra soha (08: csak forráskritikai
  kérdés; 03, 07, 11: a tipp nem a halottak számára vonatkozik).
- **Kipróbálom** – legalább egy valódi interakció (dátumcsúszka, kapcsoló, húzás, kalkulátor). Az állapot a lépés
  `enter()`-jében visszaáll.
- **Tévhit-lépés** – a felsorolt tévhitek közül legalább egyet a vászon *cáfol* (adattal, térképpel, forrással).
- **„Honnan tudjuk?”** – legalább egy lépés vagy forráskártya (TortSource), a 20. századnál a statisztika
  forráskritikájával.
- **Rétegek, bélyegek** (5–6. évfolyam, szerződés 11.): *forrás* (kékeszöld keret), *rekonstrukció* (szaggatott
  tinta), *hagyomány* (okker kartus – itt ritka: pl. a „pesti srácok” emlékezete); bélyegek: „vázlatos”,
  „illusztráció”, „becslés”, „vitatott”, „modell”, „kitalált”.
- **Lépésszám:** 7–9 lépés, az utolsó összefoglalás; a lépéscímek kérdések vagy rövid állítások.

### 01 · `01-nemzetallamok` – Miért akart minden nép saját államot? – nemzetállamok, nagyhatalmak, eszmék

- **Tanulási cél:** A **nemzeti eszme** szerint a közös nyelvű, közös múltú közösségnek saját állam jár; a 19. század
  ebből rajzolt új térképet (Olaszország, **Németország 1871**). A 20. század elején néhány **nagyhatalom** és
  **gyarmatbirodalom** uralta a világot – a Föld szárazföldjének nagy része európai uralom vagy befolyás alatt állt.
  A korszak **politikai eszméi** (liberalizmus, konzervativizmus, szocializmus és kommunizmus,
  keresztényszocializmus) másként válaszoltak arra, mi a jó társadalom.
- **Kerettanterv:** „A nemzeti eszme és a nemzetállamok Európája.” · „A világ nagyhatalmai és ellentéteik a 20.
  század kezdetén.” · „Gyarmatbirodalmak a világ térképén.” · Fogalmak: „nacionalizmus, liberalizmus,
  konzervativizmus, demokrácia, szocializmus, kommunizmus, keresztényszocializmus.” · Személyek: „Bismarck, Marx.” ·
  Kronológia: „1871 Németország egyesítése.” · Topográfia: „Németország, Olaszország, Brit Birodalom, Amerikai
  Egyesült Államok, Japán.” · „A 20. század eleji nagyhatalmak azonosítása, és a korabeli világra gyakorolt hatásuk
  feltárása térképek és egyszerű ábrák segítségével.” · tevékenység: „Németország területi egyesítés előtt és utáni
  térképének összehasonlítása, értékelése.”, „Összehasonlító táblázat készítése a korszak politikai eszméiről.”
- **Tévhitek:** „Németország mindig is egy ország volt.” „A nemzet = az állam.” „A gyarmatok kis szigetek voltak.”
  „A liberális és a konzervatív a mai pártokat jelenti.” „A szocializmus és a kommunizmus ugyanaz, és
  mindenhol diktatúrát jelentett.” (A 19. századi eszme és a 20. századi rendszer nem ugyanaz – a 05 viszi tovább.)
- **Kulcsvizuál:** Közép-Európa-térkép (TortMap, `map-europa.js`): 1815 után a Német Szövetség sok kis
  állama „csempékként”, a Porosz Királyság tintafoltja nő (1866 Königgrätz, 1870–71), és 1871-ben az egész
  egyetlen körvonallá olvad (TortTerr: `de1871` egység + vázlatos belső foltok). Utána világtérkép (Equal Earth,
  FoldChoro `cat`): a mai országok a **1914-es** uralkodó hatalom színével („mai határokkal közelítve”, „vázlatos”
  bélyeg). Mellette MatChart-oszlopok: anyaország vs gyarmatok területe.
- **Kipróbálom:** a világtérképen a hatalmak jelmagyarázata kapcsoló – egyet kiválasztva csak annak birodalma
  marad színes, az adatkártya mutatja a területet és a népességet. Az eszmék lépésben TortCards: 8 rövid
  állítás (közkincs forrásból, saját fordításban vagy parafrázisban) húzható az eszmék dobozaiba.
- **Tippelj!** 5. lépés: „Hányszor nagyobb volt 1914-ben a Brit Birodalom, mint maga Nagy-Britannia (Írországgal)?
  kb. 10× / kb. 50× / több mint 100×” (33,8 millió km² : kb. 0,31 millió km² ≈ 107× – a számolás a `.md`
  megjegyzésében).
- **Lépések:**
  1. Mi a nemzet? – nyelv, múlt, jelképek. Zászló és himnusz *kitalált* példán, nem valódi országén, hogy a
     fogalom legyen a lényeg.
  2. Egy ország, sok állam – a Német Szövetség 1815-ben (39 tagállam *(ellenőrizendő)*).
  3. Vas és vér – Bismarck: 1866 Königgrätz, 1870 Sedan, 1871. január 18. Versailles, a császárság kikiáltása. Közben
     Olaszország egyesítése mini-idővonalon (1861, Róma 1870).
  4. A nagyhatalmak 1914-ben: Nagy-Britannia, Franciaország, Németország, Oroszország, Osztrák–Magyar Monarchia,
     (Olaszország), Egyesült Államok, Japán. A két nem európai hatalom felemelkedése egy-egy adattal: az USA
     népessége 1870 → 1910 (népszámlálás), Japán 1868 Meidzsi-fordulat.
  5. Gyarmatbirodalmak a világtérképen – Tippelj!
  6. Ellentétek: hol ütközik a hatalmak érdeke (Balkán, Afrika, tengerek)? Három nyíl a térképen. Ez átvezet a
     03-hoz.
  7. Eszmék – mit akar a liberális, a konzervatív, a szocialista, a keresztényszocialista? TortCards-rendezés.
  8. Honnan tudjuk? – a korabeli statisztikai évkönyvek (Hübner-féle táblák, 1914): ki számolta a gyarmatok
     népességét, és miért becslés.
  9. Összefoglalás – az 1914-es világ egy képen.
- **Adatok:**
  - Németország kikiáltása: 1871. január 18., Versailles; Königgrätz 1866. július 3.; Sedan 1870. szeptember 1.
    (a kapituláció szeptember 2.) – szokásos kronológia, ellenőrizve.
  - Gyarmatbirodalmak 1914 (Hübner: *Geographisch-statistische Tabellen*, 1914; közli Lenin 1916, marxists.org
    – a táblázat a forrás, nem az idéző mű) – terület millió km², népesség millió fő:
    - Brit Birodalom: gyarmatok 33,5 · 393,5; anyaországgal 33,8 · 440;
    - Franciaország: 10,6 · 55,5; anyaországgal 11,1 · 95,1;
    - Oroszország: 17,4 („gyarmat”); anyaországgal 22,8 · 169,4;
    - Németország: 2,9 · 12,3 (a Wikipédia 2,66–2,95 millió km²-t és 12,0 millió főt ad: *(vitatott)*).
    Nagyságrendben megbízható, a gyarmati népesség *(becslés)*.
  - „A szárazföld kb. 84 %-a európai uralom vagy befolyás alatt” – másodlagos szakirodalmi állítás
    (Fieldhouse), *(vitatott)*; csak így: „közvetlen uralom vagy befolyás”.
  - Német Szövetség tagállamai 1815: 39 *(ellenőrizendő)*; a Német Császárság 25 tagállama + Elzász-Lotaringia
    *(ellenőrizendő)*.
  - USA népessége: 1870: 38,6 millió; 1910: 92,2 millió (US Census) *(ellenőrizendő)*.
  - Eszme-állítások: Mill: *A szabadságról* (1859, † 1873), Burke: *Töprengések a francia forradalomról* (1790,
    † 1797), Marx–Engels: *A Kommunista Párt kiáltványa* (1848, † 1883 / † 1895), XIII. Leó: *Rerum novarum*
    (1891, † 1903) – **mind közkincs**, a fordítás saját vagy közkincs (a fordító halálozási évét is jelölni kell).
- **Modulok:** TortMap, TortTerr (`de1871`, Európa 1914), FoldChoro (`cat`, FOLD_ORSZAGOK), MatChart (`bars`),
  TortCards, TortSource, TortTimeline (`mini`), TtTipp.
- **Review-pontok:** a gyarmati térkép „mai határokkal közelítve” – a tanár lássa, hol téves (pl. Arab-félsziget,
  Perzsia befolyási övezetei); az eszme-állítások ne legyenek karikatúrák; a „kommunizmus” itt 19. századi eszme.

### 02 · `02-dualizmus` – Hogyan lett Pestből és Budából világváros? – a dualizmus kora

- **Tanulási cél:** A **kiegyezés** (1867) után a Monarchia két egyenrangú államból állt, **közös ügyekkel**
  (külügy, hadügy és az ezeket fedező pénzügy). Az ország gyorsan modernizálódott: **vasút** (MÁV), folyószabályozás,
  ipar, feltalálók. **Budapest** (1873) fél évszázad alatt háromszorosára nőtt: hidak, körutak, Andrássy út,
  földalatti, a **Millennium** (1896). Közben az ország **soknemzetiségű** maradt; a zsidóság **emancipációja**
  (1867) után a modernizáció egyik motorja lett; a cigányság hagyományos mesterségekből élt. A város és a vidék
  élete nagyon különbözött.
- **Kerettanterv:** „Magyar feltalálók és találmányok, az ipar fejlődése.” · „Vasútépítés, folyószabályozás.” · „Egy
  világváros kiépülése – az urbanizáció Budapest példáján.” · „A soknemzetiségű ország.” · „A zsidó emancipáció, a
  hazai zsidóság szerepe a magyarországi modernizációban.” · „A cigányság helyzete, hagyományos mesterségek.” ·
  Fogalmak: „közös ügyek, dualizmus, MÁV, Millennium, emancipáció, urbanizáció.” · Személyek: „Andrássy Gyula.” ·
  Kronológia: „1896 a Millennium.” · „A korszak ipari fejlődésének nyomon követése diagramok, táblázatok
  segítségével.” · „A dualizmus kori vidék és város lakóinak és életmódjának bemutatása.” · (14.) „Tudósok és
  feltalálók (pl. informatika, autóipar, űrkutatás).”
- **Tévhitek:** „A kiegyezés után Magyarország független ország lett.” „Budapest mindig is egy város volt.” „1910-ben
  is a mai Budapest területén laktak a budapestiek.” (A mai határ 1950-es.) „A vasút a semmiből jött.” „Az ország
  lakóinak többsége városban élt.”
- **Kulcsvizuál:** a **TortCity** Budapest-térkép felülnézetben, papír alapon. Évszám-csúszka 1867 → 1914: 1873-ban
  Pest, Buda, Óbuda foltja egybeolvad; a hidak felépülnek (Lánchíd már áll; Margit 1876, Ferenc József 1896,
  Erzsébet 1903); kirajzolódik az Andrássy út (1876), a Nagykörút (1896-ra), a földalatti (1896); a lakosságszámláló
  az 1869-es 270 ezerről 1910-re 880 ezerre nő. Utána Kárpát-medence-térkép: a fővonalak csillagszerűen kinőnek
  Budapestről, mellette FoldChart-görbe a vasúthálózat hosszáról.
- **Kipróbálom:** évszám-csúszka a városon (a hidak és utak feliratukkal úsznak be); a „Mi volt itt 1867-ben?”
  kapcsoló a mai Duna-partot és a régit egymásra teszi. A „közös ügyek” lépésben kártyák (TortCards): melyik ügy
  közös, melyik magyar, melyik osztrák.
- **Tippelj!** 4. lépés: „Hányszor annyi ember élt Budapesten 1910-ben, mint 1869-ben? kb. 1,5× / kb. 3× / kb.
  10×” (880 371 : kb. 270 000 ≈ 3,3×).
- **Lépések:**
  1. 1867 – a kiegyezés: két ország, egy uralkodó, közös ügyek (séma két oszloppal, a közös ügyek középen).
  2. Közös ügyek – rendezés (TortCards).
  3. Sín és gát – a vasút (MÁV, 1868) és a folyószabályozás: a Tisza 1 419 km-ről 966 km-re rövidült.
     Előtte/utána vázlatos kanyarulat-animáció egy szakaszon.
  4. Három városból egy – 1873, Budapest; Tippelj!
  5. A világváros kiépül – hidak, Andrássy út (gróf Andrássy Gyula, az első közös külügyminiszter, a
     sugárút névadója), Nagykörút.
  6. 1896, Millennium – földalatti (1896. május 2.), ünnepségek; *(hagyomány)*: a honfoglalás „ezredik évét”
     megállapodással tették 1896-ra.
  7. Sok nyelv, egy ország – 1910-es anyanyelvi kördiagram (Horvátország nélkül), a zsidó emancipáció (1867), a
     cigányság (1893-as összeírás); a feltalálók sora (Bánki–Csonka, Puskás Tivadar, Zipernowsky–Bláthy–Déri,
     Kandó, Eötvös).
  8. Város és falu – két életmód-kártya (lakás, munka, iskola, közlekedés) + az agrárnépesség aránya. „Honnan
     tudjuk?”: a népszámlálás (1869 az első modern).
  9. Összefoglalás.
- **Adatok:**
  - Kiegyezés: 1867. évi XII. tc.; zsidó emancipáció: 1867. évi XVII. tc. *(ellenőrizendő)*.
  - Budapest egyesítése: 1872. évi XXXVI. tc., az egyesített város 1873. november 17-én alakult (a nap *(ellenőrizendő)*).
  - Budapest népessége: 1869 kb. 270 000 (egy táblázat 1870-re 270 349-et ad); 1900: 733 358; 1910: 880 371
    (Nagy-Budapest mai területén 1910-ben 1 110 453) – Budapesti statisztikai évkönyv,
    `real-j.mtak.hu/30254/…`.
  - Hidak: Lánchíd 1849. november 20.; Margit híd 1876. április 30.; Ferenc József (ma Szabadság) híd 1896. október
    4.; Erzsébet híd 1903. október 10.
  - Andrássy út (Sugárút): 1872–1876; földalatti: 1896. május 2. (hvg.hu); Nagykörút: „1896-ra elkészült”
    *(a részletek vitatottak: 1895 forgalom, 1896. augusztus 31. ünnepélyes átadás)*.
  - Vasút: 1867 kb. 2 200 km *(ellenőrizendő)*; 1900: 17 281 km; az első világháború végén: 22 869 km
    (Közlekedéstudományi Szemle 2021/1, `real.mtak.hu/123767/…`). MÁV: 1868 *(ellenőrizendő)*.
  - Tisza-szabályozás: 1846-tól; hossz 1 419 km → 966 km (egyes források 977 km), −32 %; Vásárhelyi Pál terve 102
    átvágással (Springer 2018; Földrajzi Értesítő 2001).
  - Anyanyelv (Horvátország nélkül): magyar 1880: 46,6 % → 1910: 54,5 % (regscience.hu). Az 1910-es teljes
    megoszlás (román 16,1 %, szlovák 10,7 %, német 10,4 %, rutén 2,5 %, szerb 2,5 %, horvát 1,1 %, egyéb
    2,2 %) *(ellenőrizendő a KSH 1910-es kötetében)*.
  - Cigányösszeírás 1893: kb. 275 000 fő *(ellenőrizendő)*.
  - Feltalálók: karburátor (Bánki–Csonka, 1893), telefonhírmondó (Puskás, 1893), transzformátor (Zipernowsky–
    Bláthy–Déri, 1885), torziós inga (Eötvös, 1890-es évek) *(évek ellenőrizendők)*.
- **Modulok:** **TortCity** (ref.: Duna, szigetek, hidak, utak, városhatár, helyszínek, évszám-állapot), TortMap
  (vasútvázlat), FoldChart (vonal), MatChart (kör), TortTimeline, TortCards, TtTipp.
- **Review-pontok:** a fővonalak vázlata (nem teljes hálózat); a millenniumi „ezer év” hagyomány-jelölése; a
  nemzetiségi kérdés ne csak idilli „sokszínűség” legyen: a választójog szűk volt (kb. 6 % *(ellenőrizendő)*), a
  nemzetiségi mozgalmak követeléseit egy mondat említse.

### 03 · `03-elso-vilaghaboru` – Miért nem mozdult a front négy évig? – az első világháború

- **Tanulási cél:** A szarajevói merénylet (1914. június 28.) egy már feszült szövetségi rendszert indított be:
  **antant** és **központi hatalmak**. A gépfegyver, a szögesdrót és a lövészárok miatt nyugaton **állóháború**
  alakult ki: évekig alig mozdult a front, a támadások százezrek életébe kerültek. Keleten és Itáliában a front
  mozgott (Doberdó, Isonzó, Piave). A **hátország** is szenvedett (jegyrendszer, hiány). 1917-ben Oroszországban
  a **bolsevikok** vették át a hatalmat (Lenin). Magyarországról kb. 3,6 millió férfit soroztak be.
- **Kerettanterv:** „A halálos lövés: a világháború kirobbanása.” · „A hadviselő felek: az antant és a központi
  hatalmak.” · „Az állóháború.” · „Magyarok a világháborúban.” · „A hátország megpróbáltatásai.” · „Lenin és a
  bolsevik hatalomátvétel.” · Fogalmak: „antant, központi hatalmak, front, állóháború, hátország, bolsevik” ·
  Személyek: „Tisza István, Lenin” · Kronológia: „1914–1918 az első világháború, 1917 a bolsevik hatalomátvétel” ·
  Topográfia: „Szarajevó, Szerbia, Doberdó” · „A fontosabb hadviselő országok csoportosítása a szövetségi
  rendszerek szerint.” · „Az első világháborús hadviselés összehasonlítása a korábbi háborúkéval.” · tevékenység:
  „Grafikonok, táblázatok elemzése a háború legfontosabb adatairól (pl. résztvevők száma, veszteségek, háborús
  kiadások, fegyverek száma stb.).”
- **Tévhitek:** „Egy lövés okozta a háborút.” „Mindenki gyors győzelemre számított – és ez így is lett.” „Az
  állóháború azt jelenti, hogy nem harcoltak.” „Magyarország nem harcolt saját frontján.” (Doberdó, Isonzó, a Kárpátok
  1914–15.) „A háború 1918. november 11-én mindenhol egyszerre ért véget.” (Padova: november 3.)
- **Kulcsvizuál:** Európa 1914 (TortTerr, `map-europa.js`): a két szövetség semleges színekkel (indigó `#3b4590` /
  szilva `#7d3a66`, TortBattle.SIDES), a belépők dátummal (Olaszország 1915 → antant; Bulgária 1915 → központi; USA
  1917). A **frontvonalak dátum szerint** (TortTerr `front`): a nyugati vonal 1914 ősze és 1918 tavasza között
  szinte áll, a keleti (Bruszilov 1916) és az olasz (Caporetto 1917) mozog. Mellette egy **lövészárok-metszet**
  (TortScene, „illusztráció” bélyeg): árok, szögesdrót, senkiföldje, a két árok távolsága méterben – vér és
  test nélkül.
- **Kipróbálom:** dátumcsúszka 1914. augusztus → 1918. november; a csúszka mellett „mennyit mozdult a front?” mérőszalag:
  két kijelölt pont között a frontvonal elmozdulása km-ben, a TortTerr-ből számolva (a geometria vázlatos, ezért
  „kb.” és „vázlatos”).
- **Tippelj!** 3. lépés: „1915 és 1917 között mennyit mozdult a nyugati front a legtöbb helyen? kevesebb mint 20 km /
  kb. 100 km / több mint 300 km”.
- **Lépések:**
  1. Szarajevó, 1914. június 28. – a merénylet és a láncreakció (július 28.: Monarchia–Szerbia; utána a szövetségek
     sorban) idővonalon; Tisza István kezdeti ellenvetése egy forráskártyán *(parafrázis)*.
  2. Két tábor – antant és központi hatalmak a térképen, a belépők dátummal.
  3. Állóháború – nyugati front, Tippelj!; Verdun (1916) és a Somme első napja (1916. július 1.) számokkal.
  4. Miért nem lehetett áttörni? – lövészárok-metszet: gépfegyver, drót, tüzérség; összehasonlítás egy korábbi
     háborúval (1849: lovasroham, mozgó csaták – visszautalás a `tortenelem-5-6/20-szabadsagharc`-ra).
  5. Magyarok a fronton – Kárpátok 1914–15, Doberdó és az Isonzó 12 csatája, Piave 1918. A besorozottak száma.
  6. A hátország – jegyrendszer, nők a munkában, hiány; FoldChart: egy ár- vagy fejadag-görbe *(ellenőrizendő
     adattal)*.
  7. 1917 – Oroszország kilép: a bolsevik hatalomátvétel (Lenin) és Breszt-Litovszk (1918. március 3.).
  8. Vége és mérleg – Padova (1918. november 3., hatályos november 4.), Compiègne (november 11.). Veszteségek
     tartománnyal (FoldChart sávok, nincs animált „számláló”). Honnan tudjuk? – a hadügyi veszteséglista és a
     belügyi korrekció: miért különbözik a két szám.
  9. Összefoglalás – átvezetés a 04-hez (a Monarchia felbomlása).
- **Adatok:**
  - Szarajevó: 1914. június 28.; hadüzenet Szerbiának: július 28.; Compiègne: 1918. november 11.; Padova: 1918.
    november 3. (hatályos november 4., 15 óra) – ellenőrizve.
  - Verdun: 1916. február 21. – december 18.; összes veszteség (halott, sebesült, eltűnt) kb. 700 000 (francia kb.
    377 000, német kb. 337 000), ebből kb. 300 000 halott; egyes becslések kb. 900 000 *(vitatott)*.
  - Somme, 1916. július 1.: 57 470 brit veszteség, ebből 19 240 halott.
  - Isonzó: 12 csata, 1915. június – 1917 ősze; a 12. Caporetto (Kobarid), 1917. október 24. Piave: 1918. június
    15–23. Bruszilov-offenzíva: 1916. június 4. Breszt-Litovszk: 1918. március 3.
  - Bolsevik hatalomátvétel: 1917. november 7. (a régi naptár szerint október 25.) *(ellenőrizendő a lecke
    megfogalmazásában)*.
  - A Monarchia mozgósítása: 8 322 000 fő, ebből a történeti Magyarország (Horvátországgal) 43 %-a, kb. 3,6 millió
    (a népesség 17,2 %-a); a szakirodalomban kb. 3,4–3,8 millió *(becslés)* – KSH: *A nagy háború*,
    `ksh.hu/docs/hun/xftp/idoszaki/haboruvalsag/nagy_haboru.pdf` (Mike Gyula 1927 nyomán).
  - Magyar halottak: 381 000 (hadügyi veszteséglisták) – 661 000 (belügyi korrekció, az eltűntek és a fogságban
    meghaltak egy részével) *(vitatott)*; sebesült 743 000, eltűnt 400 000, hadifogoly 615 000 (KSH, uo.). A
    gyakran idézett „530 ezer” forrása nem található – ne szerepeljen.
  - Világszerte: katonai halott kb. 8,5–11 millió, polgári kb. 6–13 millió *(vitatott)* – USHMM
    Encyclopedia, „World War I”.
- **Modulok:** TortTerr (Európa 1914, belépők, frontok), TortMap, TortScene (árok-metszet), FoldChart (sávok),
  TortTimeline, TortSource, TtTipp.
- **Review-pontok:** a frontvonalak vázlatosak (atlaszokkal egybevetve, a `.md` sorolja); a halottak tartománya; a
  „háborús bűnösség” kérdése (versailles-i 231. cikk) csak a 04-ben, nézőpontként; a háborús dalok/versek közül csak
  közkincs (pl. Gyóni Géza † 1917).

### 04 · `04-trianon` – Mit vesztett el az ország 1920-ban? – a trianoni békeszerződés

- **Tanulási cél:** 1918 őszén a Monarchia felbomlott; Magyarországot 1918–1919-ben a szomszédos államok csapatai
  fokozatosan **megszállták**, közben a Károlyi-kormány, majd a **Tanácsköztársaság** (1919. március 21. –
  augusztus 1.) bukott el, a **vörösterrort** a **fehér különítmények megtorlásai** követték; 1920. március 1-jén
  Horthy Miklóst kormányzóvá választották. A **Párizs környéki békék** a veszteseket büntették. A **trianoni
  békeszerződés** (1920. június 4.) után az ország területének kb. 71 %-a és népességének kb. 64 %-a az
  utódállamokhoz került, köztük kb. 3,2–3,3 millió magyar anyanyelvű ember. A **kisantant** az új határok őrzésére
  jött létre. A diák lássa a győztesek és az utódállamok érveit és a magyar érveket is – és azt, hogy az 1910-es
  népszámlálás adata mit mér és mit nem.
- **Kerettanterv:** „A forradalmi kísérlet – elhibázott kül- és katonapolitika.” · „Magyarország megszállásának
  folyamata.” · „A tanácsköztársaság hatalomra kerülése és bukása.” · „Az ellenforradalom.” · „A Párizs környéki
  békék alapelvei, a vesztesek büntetése.” · „A trianoni békediktátum – a megcsonkított Magyarország.” ·
  „Magyarország területi, népességi és gazdasági veszteségei.” · „A kisantant.” · Fogalmak: „tanácsköztársaság,
  vörösterror, fehér különítményes megtorlások, kisantant.” · Személyek: „Károlyi Mihály, Horthy Miklós.” ·
  Kronológia: „1920. június 4. a trianoni békediktátum.” · Topográfia: „Kárpátalja, Felvidék, Délvidék, Burgenland,
  Erdély, Csehszlovákia, Jugoszlávia, Románia, Ausztria.” · „Európa háború előtti és utáni térképének
  összehasonlítása, a változások értelmezése.” · „A történelmi Magyarország szétesésének bemutatása térképen az
  elcsatolt területek történelmi megnevezésével.” · „Vélemény megfogalmazása a történelmi Magyarország felbomlásának
  okairól.” · „A trianoni békediktátum területi és demográfiai következményeinek értékelése.” · (14.) „Trianon máig
  tartó hatásai: a kisállami lét kényszerpályái a nagyhatalmak árnyékában.” · tevékenység: „Trianon a gyermek
  szemével – kortárs visszaemlékezések felkutatása és megbeszélése.”
- **Tévhitek:** „A határt egyetlen nap alatt húzták meg.” (A megszállás 1918 novemberétől 1919 nyaráig tartott.)
  „Az elcsatolt területeken csak magyarok éltek.” „Az elcsatolt területeken nem éltek magyarok.” „Trianonról a
  magyarok tárgyalhattak.” „Az 1910-es anyanyelvi adat = nemzetiség.” „Trianon csak Magyarországot érintette.”
  (Saint-Germain, Neuilly, Sèvres – minden vesztest.)
- **Kulcsvizuál:** a Kárpát-medence (TortMap + TortTerr, `map-torthatar.js`). Az 1914-es Magyar Királyság
  (Horvát-Szlavónországgal, külön árnyalattal) egy egységként; a **megszállás** dátumozott sávokban (demarkációs
  vonalak, 1918. november – 1919. augusztus) halványan rárétegződik. A békeszerződés lépésében az elcsatolt részek
  (Felvidék, Kárpátalja, Erdély és Partium, Délvidék, Őrvidék/Burgenland, Fiume; Horvát-Szlavónország) **lassan
  kiúsznak** a helyükről a későbbi utódállam felé, mindegyiken „pill”-kártya: terület, 1910-es népesség,
  anyanyelvi kördiagram (MatChart). A maradék ország (kb. 93 000 km²) középen marad. Mellette egy 100 négyzetből
  álló rács: 71 négyzet kiúszik (terület), egy másik rácsban 64 (népesség).
- **Kipróbálom:** a kiúszott darabokra kattintva az adatkártya két forrást mutat egymás mellett: az 1910-es magyar
  népszámlálást és az utódállam első népszámlálását (1920/1921/1930) – a diák látja, hogy a két szám miért tér el.
  A „mai határok” kapcsoló a mai országokat halványan ráteszi.
- **Tippelj!** 5. lépés: „Hány magyar anyanyelvű ember került 1920-ban az új határokon kívülre? kb. 300 ezer / kb.
  1 millió / kb. 3 millió”.
- **Lépések:**
  1. 1918 ősze – a Monarchia felbomlik; Károlyi Mihály kormánya (1918. október 31.); Tisza István meggyilkolása
     (október 31.). Idővonal.
  2. A megszállás folyamata – dátumozott sávok a térképen (belgrádi katonai konvenció, 1918. november 13.; a
     Vix-jegyzék 1919. március 20.) *(a vonalak vázlatosak)*.
  3. Tanácsköztársaság és megtorlások – 133 nap idővonalon; vörösterror és fehérterror áldozatai tartománnyal,
     egymás mellett; 1919. augusztus 4.: román csapatok Budapesten; Horthy kormányzó 1920. március 1.
  4. Párizs környéki békék – öt szerződés öt vesztessel; a wilsoni elv („népek önrendelkezése”, 1918. január 8.,
     közkincs, saját fordítás).
  5. 1914 → 1920 – a darabok kiúsznak, Tippelj!; 100-as rácsok.
  6. Kik éltek ott? – anyanyelvi kördiagramok régiónként; „Honnan tudjuk?”: az 1910-es népszámlálás (anyanyelv,
     nem nemzetiség; a zsidóság többsége magyar anyanyelvűként; asszimilációs nyomás) és az utódállamok
     népszámlálásai (más kategóriák, a magyarok egy része elmenekült vagy kiutasították).
  7. Két nézőpont – két hasábos kártya: az utódállamok és a győztesek érvei (önrendelkezés, a többségi nemzetiség,
     1918. december 1. Gyulafehérvár, október 30. Turócszentmárton) és a magyar érvek (népszavazás csak Sopronban,
     etnikai határ helyett stratégiai és vasúti szempont, Apponyi Albert beszéde 1920. január 16. – † 1933,
     közkincs). Miért nevezik a magyar szóhasználatban „diktátumnak”? A szerződés szövegéből egy cikk (1921. évi
     XXXIII. tc., jogszabály).
  8. Gazdasági veszteség és a kisantant – erdők, bányák, vasutak aránya oszlopokon; a kisantant (Csehszlovákia,
     Románia, Jugoszlávia) a térképen.
  9. Összefoglalás – „kisállami lét”: az ország népessége kb. 7,6 millió, a szomszédjai erősebbek. Kérdés a tanárnak:
     „Mi lett volna igazságos határ – és ki szerint?” (nincs válasz a vásznon).
- **Adatok** (fő forrás: KSH *Területi Statisztika* 2020/1, Hajdú Zoltán, 1. táblázat, az 1920-as népszámlálás
  összefoglaló kötete alapján – `ksh.hu/statszemle_archive/regstat/2020/2020_01/rs100103.pdf`):
  - A Magyar Királyság Horvát-Szlavónországgal: 325 411 km², 1910-ben 20 886 487 fő; Horvátország nélkül
    282 870 km² és 18 264 533 fő (levonva Horvát-Szlavónország 42 541 km²-ét és 2 621 954 lakosát).
  - A trianoni terület: 92 952 km² (a KSH 1920-as táblája, 28,6 %); a később szokásos 93 073 km² az 1921–1924-es
    határkiigazítások (Sopron és mások) utáni érték *(vitatott → „kb. 93 000 km²”)*. Népessége 1910-ben
    7 615 134 (a KSH STADAT a mai területre 7 612 ezret ad); 1920-ban 7 986 875 (STADAT 7 987 ezer). A „7 990 202”
    forrása nem található – ne szerepeljen.
  - Elcsatolt terület és népesség (1910): Románia 102 813 km² (gyakori változat: 103 093), 5 237 911 fő;
    Csehszlovákia 61 646 km², 3 516 815 fő (más forrásban 61 633 km²); Szerb–Horvát–Szlovén Királyság
    Horvátországgal 63 370 km², 4 149 840 fő (Horvátország nélkül kb. 20 829 km², kb. 1,53 millió – számolt);
    Ausztria 4 020 km², 292 631 fő; Lengyelország 589 km², 24 880 fő; Olaszország (Fiume) 21 km², 49 806 fő.
    Összesen 232 459 km² (71,4 %) és 13 271 353 fő (63,5 %).
  - Magyar anyanyelvűek 1910: Horvátország nélkül 9 944 627 (54,5 %; a pontos hányados 54,45 %, ezért a források
    54,4 vagy 54,5 %-ot írnak – a lecke egységesen „54,5 %”); Horvátországgal 10 050 575 (48,1 %) –
    `hrcak.srce.hr/file/177096`.
  - Az új határokon kívül rekedt magyar anyanyelvűek: kb. 3,2–3,3 millió (Horvátországgal 3,3, nélküle kb. 3,2
    millió; „a magyarság harmada”) *(vitatott ±0,1 millió)*. Régiónkénti anyanyelvi megoszlás 1910-ben (Erdély
    és Partium: magyar kb. 1,66 millió; Felvidék stb.) *(ellenőrizendő a KSH 1910-es köteteiben vagy Kocsis
    Károly etnikai táblázataiban – csak a számot vegyük át, a térképet nem)*.
  - Az utódállamok első népszámlálásai: Csehszlovákia 1921, Románia 1930 (az 1920-as erdélyi összeírás),
    Jugoszlávia 1921 *(ellenőrizendő, magyar számokkal)*.
  - Békeszerződés: aláírva 1920. június 4., Versailles, Nagy-Trianon-palota; becikkelyezve 1921. évi XXXIII. tc.
    (kihirdetve 1921. július; a ratifikációs jegyzőkönyv 1921. július 26.) – `njt.jog.gov.hu/jogszabaly/1921-33-00-00`.
  - Soproni népszavazás: 1921. december 14–16.; Sopron és 8 község, kb. 65 % Magyarország mellett *(ellenőrizendő)*.
  - Tanácsköztársaság: 1919. március 21. – augusztus 1.; vörösterror áldozatai kb. 590, fehérterror áldozatai kb.
    1 000–3 000 *(mindkettő ellenőrizendő és vitatott; a lecke két forrást mutat)*.
  - Gazdasági veszteségek (erdő, vasérc, só, vasútvonal aránya) *(ellenőrizendő, KSH 1920-as évek)*.
- **Modulok:** TortTerr (1914 → 1920 egységek, `explode`, dátumozott megszállási sávok), TortMap, MatChart (kör,
  négyzetrács), TortTimeline, TortSource (két nézőpont, jogszabály-idézet), TtTipp.
- **Review-pontok:** **történész lektor**; a két nézőpont egyensúlya (szó- és helyarány a vásznon); a „diktátum”
  magyarázat; a megszállási vonalak dátumai; a vörös- és fehérterror számai; a „Trianon a gyermek szemével”
  tevékenységhez a tanári megjegyzés családi visszaemlékezést javasol (a lecke nem közöl élő szerzőtől szöveget).

### 05 · `05-diktaturak` – Hogyan bontható le egy demokrácia lépésről lépésre? – totális diktatúrák

- **Tanulási cél:** A **totális állam** az élet minden területét (párt, rendőrség, sajtó, iskola, gazdaság,
  magánélet) egyetlen akarat alá vonja. A Szovjetunióban Lenin, majd **Sztálin** építette ki: **államosítás**,
  kényszerkollektivizálás, éhínség, **terror**, **GULAG** munkatáborok, **személyi kultusz**. Németországban
  **Hitler** 1933-ban legális úton jutott hatalomra, és néhány hónap alatt felszámolta a demokrácia
  intézményeit; a **nemzetiszocializmus** a **fajelméletre** és az **antiszemitizmusra** épült, és terjeszkedésbe
  kezdett (Ausztria, Csehszlovákia). A két diktatúra ideológiája ellentétes, eszközei sokban hasonlók.
- **Kerettanterv:** „Lenin és Sztálin diktatúrája.” · „Az államosítás.” · „A terror és a munkatáborok.” · „A
  nemzetiszocializmus: fajelmélet és antiszemitizmus.” · „A náci hatalomátvétel, a hitleri diktatúra és terror.” ·
  „A hitleri Németország terjeszkedése: Ausztria és Csehszlovákia.” · Fogalmak: „személyi kultusz, GULAG, totális
  állam, nemzetiszocializmus, antiszemitizmus, fasizmus.” · Személyek: „Sztálin, Hitler.” · Kronológia: „1933 a náci
  hatalomátvétel.” · Topográfia: „Szovjetunió, Szibéria (munkatáborok).” · „A totális diktatúrák összehasonlítása
  (pl. jelképek, ideológiák, hatalmi eszközök).” · „Érvelés a 20. század kirekesztő ideológiáival szemben.” ·
  tevékenység: „GULÁG táborok és a náci koncentrációs táborok helyszíneinek térképen való azonosítása.”
- **Tévhitek:** „Hitler puccsal jutott hatalomra.” (1923-ban megpróbálta, 1933-ban kinevezték.) „A németek többsége
  a nácikra szavazott.” (A legjobb szabad eredményük 37,3 %, 1932. július.) „A GULAG néhány börtön volt.” „A két
  diktatúra ugyanaz.” / „A két diktatúra semmiben sem hasonlít.” „A diktatúra egyik napról a másikra jön.”
- **Kulcsvizuál:** a **TortState** intézményséma – Weimari Köztársaság: választók → Reichstag → kancellár, mellette
  elnök, bíróságok, sajtó, pártok, szakszervezetek, tartományok; a kapcsolók („ellenőrzés”) zöld helyett
  kékeszöld vonalak. A hatalomátvétel lépésében **dátumozott kapcsolók** egyenként kialszanak (1933. február 28.
  rendelet → március 23. felhatalmazási törvény → május 2. szakszervezetek → július 14. egypárttörvény → 1934.
  augusztus 2. „vezér és kancellár”). Előtte **TortParl** patkók: a Reichstag 1928, 1930, 1932 júl., 1932 nov.,
  1933 márc. – a pártok semleges árnyalatban, csak az NSDAP és a KPD kiemelve. A GULAG-lépésben Szovjetunió-
  térkép (Equal Earth részlet): a táborrendszer fő központjai pontként, nagyságrendi körökkel *(vázlatos)*.
- **Kipróbálom:** a TortState kapcsolói kézzel is kapcsolhatók: „mi történik, ha kikapcsolod a szabad sajtót?” –
  a séma jelzi, melyik ellenőrzés vész el; a dátum-gomb a valódi sorrendet játssza le. A záró lépésben TortCards:
  12 jellemző (pl. „egy párt”, „titkosrendőrség”, „fajelmélet”, „osztályharc”, „államosított ipar”, „magántulajdon
  megmarad, de alárendelt”) rendezése három dobozba: náci, szovjet, mindkettő.
- **Tippelj!** 3. lépés: „Hány százalékot kapott az NSDAP a legjobb szabad választásán? kb. 20 % / kb. 37 % / több
  mint 50 %”. 6. lépés: „Hány nap telt el Hitler kinevezése és a felhatalmazási törvény között? kb. 50 / kb. 200 /
  kb. 500” (január 30. → március 23. = 52 nap).
- **Lépések:**
  1. Mi a totális állam? – a TortState üres sémája: minden terület egy szálon.
  2. Lenin és Sztálin – 1917 → 1924 (Lenin halála) → Sztálin; államosítás, kollektivizálás, éhínség 1932–33
     (tartománnyal), személyi kultusz *(jelkép helyőrző, nincs portré)*.
  3. Terror és GULAG – térkép, számok tartománnyal; a „nagy terror” 1937–38. Honnan tudjuk? – az 1991 után megnyílt
     NKVD-archívumok.
  4. Weimar választásai – TortParl 1928 → 1933, Tippelj!
  5. 1933. január 30. – kinevezés, nem puccs (Hindenburg elnök). Fasizmus: Mussolini 1922 egy mondatban.
  6. 52 nap – a kapcsolók kialszanak; Tippelj!
  7. Fajelmélet és antiszemitizmus – nürnbergi törvények (1935. szeptember 15.), a kirekesztés lépcsői idővonalon
     (bojkott 1933. április 1. *(ellenőrizendő)*, „kristályéjszaka” 1938. november 9–10.); átvezetés a 08-ra.
  8. Terjeszkedés – Anschluss (1938. március 12–13.), München (1938. szeptember 29–30.), Prága (1939. március 15.):
     TortTerr Európa-darabok dátum szerint.
  9. Két diktatúra – TortCards-összehasonlítás és összefoglalás. Kérdés a tanárnak: „Miért nem állította meg senki?”
- **Adatok:**
  - Reichstag-választások (szavazat %: NSDAP / SPD / KPD; NSDAP-mandátum / összes): 1928. május 20.: 2,6 / 29,8 /
    10,6; 12 / 491 · 1930. szeptember 14.: 18,3 / 24,5 / 13,1; 107 / 577 · 1932. július 31.: 37,3 / 21,6 / 14,3–14,6;
    230 / 608 · 1932. november 6.: 33,1 / 20,4 / 16,9; 196 / 584 · 1933. március 5.: 43,9 / 18,3 / 12,3; 288 / 647
    (már nem szabad választás) – gonschior.de, LeMO (DHM). A többi párt (Zentrum, DNVP, DVP, DDP stb.)
    eredménye ugyanonnan *(a leckeügynök kiegészíti)*.
  - Dátumok: kinevezés 1933. január 30.; Reichstag-tűz február 27., rendelet február 28.; felhatalmazási törvény
    március 23. (a Reichstag megszavazta; kihirdetve március 24.); szakszervezetek feloszlatása május 2.;
    egypárttörvény július 14.; Hindenburg halála 1934. augusztus 2. (a hivatalok összevonásáról szóló törvény
    augusztus 1-jei); nürnbergi törvények 1935. szeptember 15.; Anschluss 1938. március 12. (bevonulás) / 13.
    (törvény); müncheni egyezmény szeptember 29-én kelt, éjfél után írták alá; Prága megszállása 1939. március 15.
  - Lenin halála 1924. január 21.; Sztálin halála 1953. március 5.
  - GULAG: 1930–1953 között kb. 18 millió ember fordult meg a táborokban; ezen felül kb. 6 millió deportált/
    „különtelepes”; a táborokban meghaltak száma kb. 1,5–1,8 millió (archív adat 1,6–1,7 millió; magasabb
    becslések is vannak) *(vitatott)*. A „nagy terror” (1937–38): 681 692 kivégzés (NKVD-adat); 1929–1953 között
    összesen 777 975 politikai kivégzés – Britannica „Gulag”, HURI, Wikipédia „Excess mortality under Joseph Stalin”.
  - Éhínség 1932–33: Ukrajna 3,5–5 millió (a HURI demográfiai becslése 3,9 millió közvetlen veszteség), a teljes
    Szovjetunióban 1930–33 között 5,5–8,7 millió *(vitatott)*.
  - GULAG-központok koordinátája (Kolima/Magadan, Vorkuta, Norilszk, Karaganda, Szolovki) *(a leckeügynök
    ellenőrzi)*.
- **Modulok:** TortState, TortParl, TortTerr (1938–39 Európa-darabok), TortMap/FoldChoro (Szovjetunió), TortCards,
  TortTimeline, TortSource, TtTipp.
- **Review-pontok:** **történész lektor**; jelkép-tilalom (0. döntés, 10.); a két diktatúra összehasonlítása se
  „egyenlőségjel”, se „felmentés” – a TortCards „mindkettő” doboza adja az árnyalást; az áldozatszámok tartománya.

### 06 · `06-pengo` – Mennyit ért a pengő? – a Horthy-korszak és a nagy infláció

- **Tanulási cél:** Az 1920-as évek elején a **korona** gyorsan veszített az értékéből. A Bethlen-kormány
  népszövetségi kölcsönnel stabilizált, megalapította a Magyar Nemzeti Bankot (1924), és bevezette a **pengőt**
  (1927, 1 pengő = 12 500 korona). Az 1920-as évek gazdasági eredményeit az 1929-es **világválság** törte meg
  (gabonaár-zuhanás). A társadalom erősen rétegzett volt (nagybirtok, kevés földű parasztság). Klebelsberg Kuno
  iskolaépítő programja és a tudomány (Szent-Györgyi Albert, Nobel-díj 1937) a korszak eredményei közé tartozik;
  a politikai antiszemitizmus (numerus clausus, 1920) és a revíziós törekvés a problémái és céljai közé. A háború
  után a pengő a világtörténelem egyik legnagyobb inflációjában omlott össze: 1946 júliusában az árak kb. **15
  óránként duplázódtak**; 1946. augusztus 1-jén jött a **forint**: 1 forint = 400 000 kvadrillió (4 · 10²⁹) pengő.
- **Kerettanterv:** „Horthy, a kormányzó.” · „Antikommunizmus és revíziós törekvések.” · „A politikai
  antiszemitizmus.” · „Bethlen István miniszterelnöksége.” · „Külpolitikai kényszerpályák.” · „Gazdasági
  eredmények.” · „Az oktatás, a kultúra és a tudomány néhány kiemelkedő képviselője.” · „Társadalmi rétegződés és
  érintkezési formák Magyarországon.” · „Életmód, szabadidő, sport.” · Fogalmak: „revízió, numerus clausus,
  pengő.” · Személyek: „Bethlen István, Klebelsberg Kuno, Szent-Györgyi Albert.” · Kronológia: „1920–1944 a
  Horthy-korszak.” · „A Horthy-korszak gazdasági, kulturális, politikai és társadalmi eredményeinek és
  problémáinak felidézése.” · (8.) „A tervgazdaság működése.” *(csak a forint bevezetésének keretében)*.
- **Tévhitek:** „Az infláció azt jelenti, hogy több a pénz – tehát gazdagabbak vagyunk.” „A pengő mindig rossz pénz
  volt.” (1927–1938 között a térség egyik stabil valutája volt *(ellenőrizendő megfogalmazás)*.) „A forint a
  semmiből jött.” „A válság csak a városokat érintette.” „Az árak lineárisan nőttek.” (Logaritmikus skála kell.)
- **Kulcsvizuál:** egy **kifli** (vagy egy kiló kenyér) ára FoldChart **logaritmikus** tengelyen 1914 → 1946 (a
  tengely osztásai 10⁰, 10³, 10⁶ … 10²⁹ – hatványalakkal, „log” jelzéssel). A görbe 1927 és 1938 között szinte
  vízszintes (pengő), 1945–46-ban szinte függőleges. Mellette egy „pénzköteg”-mérleg: hány bankjegy kell egy
  kenyérhez – ez **nem** fizikai torony (az csillagászati lenne), hanem a bankjegyen szereplő nullák száma nő
  (100 millió b.-pengő = 10²⁰ pengő). A korszak-lépésekben MatChart: a földbirtok-megoszlás („100 emberből…”), a
  foglalkozási szerkezet, az iskolaépítés oszlopai.
- **Kipróbálom:** dátumcsúszka 1945. július → 1946. július a log-tengelyen; egy „óra” kijelző mutatja, hány óra
  alatt duplázódott az ár az adott hónapban. Átváltó: a diák beír/csúsztat egy pengőösszeget (10⁰ … 10³⁰), és
  az átváltó forintban, adópengőben és a „mennyi kenyér?” kérdésben válaszol (csak 1946. júliusi árakon).
- **Tippelj!** 8. lépés: „1946 júliusában mennyi idő alatt duplázódtak az árak? kb. egy hónap / kb. egy hét / kb. 15
  óra”.
- **Lépések:**
  1. 1920 – a megcsonkított ország és a korona: árak és béke (az 1914-es árszint 100).
  2. A kormányzó és a korszak – idővonal 1920–1944: Horthy kormányzó, miniszterelnökök (Bethlen 1921–1931), numerus
     clausus (1920), revíziós törekvés (a 07-ben az eredményei).
  3. Stabilizáció – népszövetségi kölcsön (1924), MNB (1924), pengő (1927. január 1., 12 500 korona).
  4. Eredmények és válság – az ipari termelés és a gabonaár 1925–1935 között; a világválság 1929.
  5. 100 emberből… – társadalmi rétegek és földbirtok (MatChart, négyzetrács).
  6. Iskola és tudomány – Klebelsberg népiskolai programja (tanterem-oszlopok); Szent-Györgyi Albert, C-vitamin,
     Nobel-díj 1937; sport (1936, Berlin – az olimpia magyar eredménye *(ellenőrizendő)*).
  7. Háborúból háborúba – hadikiadások és pénznyomtatás 1938–1945; a pengő értékvesztése megindul.
  8. A világrekord közelében – 1945–46 hiperinfláció a log-tengelyen; Tippelj!; adópengő; a legnagyobb kibocsátott
     bankjegy.
  9. 1946. augusztus 1. – a forint; Honnan tudjuk? – a KSH árstatisztikája és a Hanke–Krus-táblázat; miért vitatott a
     „világrekord” (Zimbabwe, 2008). Összefoglalás.
- **Adatok:**
  - Pengő: 1927. január 1., 1 pengő = 12 500 korona (1925. évi XXXV. tc.) – MNB: *A 100 éves MNB története
    bankjegyeken és érméken keresztül* (`mnb.hu/letoltes/hergar-eszter-katus-magdolna-…`).
  - MNB megalapítása: 1924 (működés 1924. június 24. *(ellenőrizendő)*); népszövetségi kölcsön 1924, összege
    *(ellenőrizendő)*.
  - 1946. július (csúcs): havi 4,19 · 10¹⁶ %, naponta kb. 207 %, az árak kb. 15 óránként duplázódtak (Hanke–Krus,
    `bcci.bg/resources/files/hanke-krus-hyperinflation-table.pdf`); népszerű források „11 órát” írnak – kiugró érték,
    ne szerepeljen. Danyi (Statisztikai Szemle 2022/12) a „világrekord” rangsort vitatja Zimbabwével szemben, a havi
    értéket nem.
  - Forint: 1946. augusztus 1.; 1 Ft = 4 · 10²⁹ pengő (400 000 kvadrillió) = 200 millió adópengő – MNB, *Már hetven
    éve forinttal fizetünk* (`mnb.hu/letoltes/horvath-karoly-…`).
  - Legnagyobb kibocsátott bankjegy: 100 millió b.-pengő = 10²⁰ pengő, 1946. július 11.; az 1 milliárd b.-pengős
    (10²¹) kinyomtatták, de nem bocsátották ki.
  - Kifli/kenyér ára havonta 1945–46 *(ellenőrizendő: KSH Magyar Statisztikai Szemle 1946–47; a leckeügynök
    egyetlen termék sorát vegye, forrással)*.
  - Numerus clausus: 1920. évi XXV. tc. (1920. szeptember 26.; a zsidókat nem nevezi meg, arányuk kb. 6 %; 1928-ban
    módosították) – net.jogtar.hu.
  - Klebelsberg népiskolai programja 1926-tól: kb. 5 000 tanterem és tanítói lakás *(ellenőrizendő)*;
    Szent-Györgyi Nobel-díja: 1937 (élettani/orvosi) – ellenőrizve (szokásos adat).
  - Földbirtok- és foglalkozási szerkezet 1930/1935 *(ellenőrizendő, KSH 1930-as népszámlálás és 1935-ös
    földbirtok-statisztika)*.
  - Bethlen miniszterelnök: 1921. április 14. – 1931. augusztus 24. *(ellenőrizendő)*.
- **Build:** a hatványalakú szám (`4 · 10^29 pengő`) a mostani `number` típusban nem megy (5.2/1). Megoldás a
  bővítésig: `series` a 10-es kitevőkkel („1946. július: 26”), a `.md`-ben megjegyzéssel, vagy szorzószóval, ahol
  van (`billió` = 10¹²).
- **Modulok:** FoldChart (log, `vspan`, `cursor`, `source`), MatChart, TortTimeline, TortSource, TtTipp.
- **Review-pontok:** a Horthy-korszak „eredmények és problémák” egyensúlya (a kerettanterv mindkettőt kéri); a
  numerus clausus pontos megfogalmazása (a törvény nem nevezi meg a zsidókat, de ellenük szólt – USHMM, origo
  forrás); a kenyérár-sor forrása.

### 07 · `07-masodik-vilaghaboru` – Hogyan mozgott a front 1939 és 1945 között? – a második világháború

- **Tanulási cél:** A Molotov–Ribbentrop-paktum (1939. augusztus 23.) után Németország és a Szovjetunió felosztotta
  Kelet-Európát; a háború 1939. szeptember 1-jén kezdődött. A **tengelyhatalmak** 1942 őszéig terjeszkedtek, utána a
  **szövetségesek** fordítottak (Sztálingrád, Normandia), a háború Európában 1945. május 8-án, Ázsiában az
  **atombombák** után szeptember 2-án ért véget. Magyarország a **bécsi döntésekkel** és két katonai akcióval
  1938–1941 között területet nyert vissza; 1941. június 27-től hadban állt a Szovjetunióval; a **2. magyar hadsereg**
  a **Donnál** (1943. január) óriási veszteséget szenvedett; **1944. március 19-én** a német hadsereg megszállta az
  országot, **október 15-én** a kiugrási kísérlet kudarca után a **nyilasok** (Szálasi Ferenc) vették át a
  hatalmat; Budapest ostroma 1945. február 13-ig tartott; a harcok **1945. április** közepén értek véget az
  országban. Ez **totális háború** volt: a hátország, a városok és a civilek is a háború célpontjai lettek.
- **Kerettanterv:** „Sztálin-Hitler paktum, kezdeti német sikerek.” · „A háború európai frontjai és a
  csendes-óceáni hadszíntér.” · „Fordulatok a háborúban: Sztálingrád és Normandia, Berlin, az atombomba.” · „Európa
  felosztása.” · „A revíziós eredmények” · „A Szovjetunió elleni háború – a 2. magyar hadsereg a Donnál.” · „Német
  megszállás.” · „A kiugrási kísérlet és a nyilas hatalomátvétel.” · „A hadszíntérré vált Magyarország.” · „A
  bombázások és városi harcok – Budapest példáján.” · Fogalmak: „tengelyhatalmak, szövetségesek, bécsi döntések,
  nyilasok, totális háború” · Személyek: „Franklin D. Roosevelt, Churchill, Teleki Pál, Szálasi Ferenc” ·
  Kronológia: „1939–1945 a második világháború, 1941. június a Szovjetunió megtámadása, 1944. március 19.
  Magyarország német megszállása, 1945. április a háború vége Magyarországon.” · Topográfia: „Sztálingrád,
  Normandia, Hirosima, Don-kanyar” · „Magyarország területi változásait és világháborús részvételét, valamint a
  második világháború főbb eseményeit bemutató térképek értelmezése.” · „A magyar külpolitika háború előtti és alatti
  törekvéseinek és mozgásterének bemutatása.” · „A magyar honvéd helytállásának felidézése források alapján.” ·
  (13.) „A második világháború hadszíntere.”
- **Tévhitek:** „A háborút csak Németország kezdte.” (A Szovjetunió is megtámadta Lengyelországot, 1939.
  szeptember 17.) „Magyarország háború nélkül kapta vissza a területeit.” (A kárpátaljai és a délvidéki akció
  katonai volt.) „A Don-kanyarban mindenki meghalt.” „A háború Magyarországon 1945. április 4-én ért véget.” (Az
  1950-es években kijelölt ünnepnap; a harcok április 11–13-án értek véget.) „A front egyenletesen haladt
  nyugat felé.”
- **Kulcsvizuál:** Európa-térkép (TortMap, `map-europa.js`) a **TortTerr** egységeivel: minden darab a dátum szerinti
  „ellenőrző hatalom” árnyalatával (tengely: indigó-skála; szövetséges: szilva-skála; semleges: papír; megszállt
  terület sraffozva). Rajta a **keleti és a nyugati front** dátum szerint interpolált vonala. Külön nézet: a
  Kárpát-medence 1938–1941 – a négy visszacsatolt terület egymás után „becsúszik” (első bécsi döntés, Kárpátalja,
  második bécsi döntés, Délvidék), rajtuk kártya: terület, népesség, magyar arány **két népszámlálás szerint**
  (az elcsatoló és a visszacsatoló állam adata). A végén Budapest (TortCity): az ostrom gyűrűje 1944. december 26.,
  a felrobbantott hidak dátummal.
- **Kipróbálom:** dátumcsúszka 1939. szeptember 1. → 1945. május 8. (a front és a hovatartozás együtt mozog); a
  Csendes-óceán gombra kis gömb-nézet (TortGlobe) Japán legnagyobb kiterjedésével (1942) és Hirosima, Nagaszaki
  pontjával – robbanás nélkül, egy halvány gyűrűvel és dátummal.
- **Tippelj!** 4. lépés: „Mikor volt a legnagyobb a tengelyhatalmak által megszállt terület Európában? 1940 nyarán /
  1942 őszén / 1944 tavaszán”.
- **Lépések:**
  1. Revízió 1938–1941 – a négy terület, két népszámlálás arányai; Teleki Pál halála (1941. április 3.).
  2. A paktum és Lengyelország – 1939. augusztus 23., szeptember 1., szeptember 17. – a darabok két színre válnak.
  3. Villámháború nyugaton – 1940: Dánia, Norvégia, Benelux, Franciaország; Nagy-Britannia kitart (Churchill).
  4. 1941. június 22. – a Szovjetunió megtámadása; Magyarország hadba lép (június 27.). Tippelj!
  5. Fordulat – Sztálingrád (1942–43) és a Don (1943. január 12.): a 2. magyar hadsereg létszáma és veszteségei
     tartománnyal; „Honnan tudjuk?” – a hadtörténeti kutatás számai miért változtak.
  6. A gyűrű szűkül – 1943 Kurszk, 1944. június 6. Normandia, 1944 nyara; közben Magyarország: 1944. március 19.
     német megszállás, október 15. kiugrási kísérlet, nyilas hatalomátvétel.
  7. Hadszíntér Magyarország – a front átvonul az országon (1944 szeptember – 1945 április); Budapest ostroma a
     TortCity-n (hidak, dátumok); a háború vége április 11–13. (és miért ünnepelték április 4-ét).
  8. Berlin és Hirosima – 1945. május 8.; augusztus 6. és 9.; szeptember 2. Roosevelt, Churchill, Sztálin a
     konferenciákon (Teherán, Jalta, Potsdam – Európa felosztása).
  9. Mérleg – a háború halottai tartománnyal (FoldChart sávok, nincs animált számláló); átvezetés a 08-ra és a 09-re.
- **Adatok:**
  - Első bécsi döntés: 1938. november 2.; 11 927 km², kb. 1,06 millió fő; magyar arány az 1941-es magyar
    népszámlálás szerint 84 %, az 1930-as csehszlovák szerint 57 % (a Wikipédia 59 / 86,5 %-ot ad) – Romsics
    Ignác: *Trianon revíziója…* (`real.mtak.hu/190216/1/17_romsics_i.pdf`). A „869 ezer” fő nem igazolt – ne
    szerepeljen.
  - Kárpátalja: 1939. március 15–18.; kb. 12 000 km², kb. 700 000 fő, 70–75 % ruszin; magyar arány ≤ 10 % (1941) vs
    kb. 5 % (1930); a kelet-szlovákiai sáv (1939. április) kb. 1 897 km², 69 630 fő *(Wikipédia, ellenőrizendő)*.
  - Második bécsi döntés: 1940. augusztus 30.; 43 104 km², kb. 2,5 millió fő (egyes források 2,4 millió); 1941-es
    magyar népszámlálás: 52 % magyar, 38 % román; 1930-as román népszámlálás: 49 % román, 38 % magyar.
  - Délvidék: 1941. április; kb. 11 475 km² (Bácska–Baranya 9 771 + Muraköz–Muravidék 1 704), kb. 1,03 millió fő;
    magyar arány 37 % (1941, magyar) vs 30 % (1931, jugoszláv).
  - Együtt: az ország területe kb. 93 000 → 171 000 km², népessége 9,3 → 14,6 millió.
  - Molotov–Ribbentrop-paktum 1939. augusztus 23.; Lengyelország lerohanása szeptember 1., szovjet támadás
    szeptember 17.; francia fegyverszünet 1940. június 22.; Barbarossa 1941. június 22.; Kassa bombázása június 26.,
    hadba lépés június 27.; Sztálingrád bekerítése 1942. november 19–23., kapituláció 1943. február 2.; Normandia
    1944. június 6.; Berlin, kapituláció 1945. május 8.; Hirosima augusztus 6., Nagaszaki augusztus 9.; japán
    kapituláció szeptember 2. *(szokásos kronológia; a leckeügynök egy forrással rögzíti)*.
  - 2. magyar hadsereg: kb. 207 000 fő élelmezési létszám (ebből 35 000 munkaszolgálatos), összesen kb. 250 000 fő
    szolgált benne; az áttörés 1943. január 12.; az első tíz nap 42 000 halott, 28 000 sebesült, 26 000 fogoly; az
    egész év kb. 50 000 halott, 50 000 sebesült, 27–28 000 fogoly, összesen kb. 127–128 000 (régebbi számok: 93 500,
    120 000, 148 000) *(vitatott, de jól behatárolt)* – HM Hadtörténeti Intézet, 2026
    (`mki.gov.hu/assets/articles/2026/01/MKI%20jan12.pdf`).
  - Német megszállás 1944. március 19.; kiugrási kísérlet október 15.; Budapest bekerítése 1944. december 26.
    (24–26., meghatározás szerint), Pest 1945. január 18., Buda február 13. (kitörés február 11.).
  - A háború vége Magyarországon: a hivatalos ünnep április 4. (Nemesmedves); a harcok valójában április 11–13-án
    értek véget (Magyarbüks április 11., Pinkamindszent környéke április 12.) – Ravasz István, Hadtudományi Szemle
    (`folyoirat.ludovika.hu/hsz/article/view/1410`).
  - Budapest hídjai: a Margit híd 1944. november 4-én véletlen robbanás; a többit a német csapatok Pestről
    kivonulva robbantották fel 1945. január 14–18. között, a Lánchidat és az Erzsébet hidat utoljára (18-án); az
    **Árpád híd** ekkor még befejezetlen volt, nem robbantották fel (1950. november 7-én adták át). A pontos
    napok *(ellenőrizendők)*.
  - Halottak: világszerte kb. 60–80 millió (a források 60–85 milliót adnak) *(vitatott)*; Magyarország (a
    holokauszt áldozataival) kb. 830–950 ezer, gyakran „kb. 900 ezer” *(vitatott; hivatalos KSH-szám nincs)*.
- **Modulok:** **TortTerr** (ref.: darabok × dátum → hovatartozás, front-kulcskockák, `explode`), TortMap, TortCity,
  TortTimeline, FoldChart, TortGlobe, TortSource, TtTipp.
- **Review-pontok:** **történész lektor**; a frontvonal-kulcskockák dátumai és helye (atlaszokkal); a két népszámlálás
  egymás mellett; „a magyar honvéd helytállása” – a lecke a katonák sorsát forrással és tisztelettel mutatja (egy
  közkincs levél vagy hivatalos jelentés részlete, ha van), dicsőítés és felmentés nélkül; a munkaszolgálatosok a
  Donnál is külön számmal.

### 08 · `08-holokauszt` – Hogyan vezetett a jogfosztás a népirtásig? – a holokauszt

> **Érzékeny lecke.** Szakmai lektor: történész + emlékezetpedagógus (spec `"review": ["történész",
> "emlékezetpedagógus"]`). Nincs „Tippelj!” áldozatszámra, nincs pontszám, nincs látványos effektus, nincs csúszka
> áldozatszámon. Színek: tompa tinta és papír, a vásznon csak a forrás kékeszöldje és egy halvány okker.

- **Tanulási cél:** A **holokauszt** az európai zsidóság szervezett, állami megsemmisítése volt a náci Németország
  vezetésével; a **cigányság** (roma, szinti) elpusztítását is megkísérelték. Magyarországon a jogfosztás lépésről
  lépésre haladt (numerus clausus 1920, **zsidótörvények** 1938, 1939, 1941; munkaszolgálat; Kamenyec-Podolszkij
  1941); a német megszállás (1944. március 19.) után a magyar közigazgatás és csendőrség a német SS-sel
  együttműködve néhány hét alatt **gettókba** zárta és **deportálta** a vidéki zsidóságot – kb. 437 000 embert,
  többségüket Auschwitz-Birkenauba. A budapesti zsidóság egy része túlélt; ebben **embermentők** (diplomaták,
  egyháziak, magánemberek) is szerepet játszottak. A magyarországi zsidó áldozatok száma kb. 500–565 ezer.
  Honnan tudjuk: a tettesek iratai, a túlélők vallomásai, a népszámlálások.
- **Kerettanterv:** „A náci koncentrációs és megsemmisítő táborok.” · „Az európai és magyarországi zsidótörvények.” ·
  „Kísérlet az európai és a magyar zsidóság és cigányság elpusztítására.” · „Áldozatok és bűnösök, felelősség és
  embermentés: néhány kiemelkedő példa.” · Fogalmak: „holokauszt, gettó, deportálás, koncentrációs tábor,
  zsidótörvények” · Személyek: „Salkaházi Sára.” · Topográfia: „Auschwitz.” · „Ítélet megfogalmazása a második
  világháborús népirtásokról és háborús bűnökről.” · „Példák gyűjtése az ellenállás és embermentés formáira.” · (5.)
  „A politikai antiszemitizmus.” · (4.) „A nemzetiszocializmus: fajelmélet és antiszemitizmus.” · tevékenység:
  „Ismeretek szerzése és megvitatása a holokauszt történetét feldolgozó gyűjtemények, online adatbázisok
  segítségével (pl. látogatás a Holokauszt Emlékközpontban).”, „Egy magyarországi embermentő (pl. Boldog Salkaházi
  Sára) tevékenységének megismerése és értékelése.”
- **Tévhitek:** „A holokauszt egy pillanat alatt történt.” (Évtizedes jogfosztás előzte meg.) „Magyarországon a
  deportálást csak a németek hajtották végre.” (A gettósítást és a deportálást a magyar közigazgatás és
  csendőrség végezte, a német Eichmann-különítmény irányításával.) „Csak a zsidókat üldözték.” (Romák, politikai
  ellenfelek, homoszexuálisok, fogyatékkal élők is.) „A koncentrációs tábor és a megsemmisítő tábor ugyanaz.”
  „Senki nem segített.” / „Mindenki segített.”
- **Kulcsvizuál:** három, nyugodt tempójú réteg:
  1. **Idővonal** (TortTimeline) 1920 → 1945 a jogfosztás lépcsőivel: minden törvény egy lépcsőfok, a lépcső
     lefelé vezet; a lépcsőfokon a törvény száma és egy mondatos tartalma (jogszabály – közkincs, szó szerint
     idézhető).
  2. **Térkép** (TortTerr, `map-torthatar.js` `zonak1944`) az 1941-es országterülettel: a deportálási **zónák**
     gombnyomásra, egyenként, dátummal sötétednek el; mellettük a Veesenmayer-jelentés kumulált száma és a
     szerelvények száma, csak szám és dátum. Utána egy halvány vonal Auschwitz-Birkenauig (TortMap, Európa).
  3. **Budapest** (TortCity): a pesti gettó (1944. november – 1945. január 17–18.), a „nemzetközi gettó” védett
     házai (Újlipótváros), a Duna-part (nyilas gyilkosságok – helyszínként, jelölés nélküli emléksorral), és az
     embermentők helyszínei (svéd, svájci követség, Salkaházi Sára rendháza *(ellenőrizendő helyszín)*).
- **Kipróbálom:** forrásréteg-kapcsoló (TortSource): ugyanarra a kérdésre („hány embert deportáltak?”) három forrás –
  Veesenmayer követ táviratai (437 402), Ferenczy csendőr alezredes jelentése (434 351, 147 szerelvény), egy
  DEGOB-jegyzőkönyv *(parafrázisban, szám nélkül, a jegyzőkönyv számával)*. A diák látja, ki írta, mikor, milyen
  céllal. Az embermentő-térképen helyszínre kattintva a mentő neve, tette és a forrás.
- **Tippelj!** (forráskritikai) 9. lépés: „Melyik forrásból tudjuk legpontosabban a deportáltak számát? a tettesek
  saját jelentéseiből / a túlélők visszaemlékezéseiből / a háború utáni népszámlálásból” – a válasz: mindhárom kell,
  más-más kérdésre.
- **Lépések:**
  1. Kik voltak? – a magyarországi zsidóság 1941-ben (725 007 izraelita vallású, + kb. 100 000 a faji törvények
     szerint), városok és falvak, foglalkozások – emberi közösségként, nem statisztikaként (egy-két dokumentált,
     közkincs forrásból ismert életút; pl. Radnóti Miklós † 1944, közkincs).
  2. A lépcső lefelé – 1920, 1938, 1939, 1941: a jogszabályok idővonalon; munkaszolgálat.
  3. Kamenyec-Podolszkij (1941) – az első tömeggyilkosság magyar állampolgárok ellen; Újvidék 1942 *(egy mondat,
     ellenőrizendő szám)*.
  4. Európa – a táborrendszer térképe: koncentrációs és megsemmisítő tábor különbsége; a hat millió (5,1–6,0 millió
     tartomány); a roma áldozatok tartománya.
  5. 1944. március 19. után – sárga csillag (1944. április 5. *(ellenőrizendő)*), gettók (április–május).
  6. Zónáról zónára – 1944. május 15. – július 9., gombnyomásra, zónánként. Honnan tudjuk? (Veesenmayer, Ferenczy.)
  7. Auschwitz-Birkenau – az érkezők nagy részét azonnal meggyilkolták; csak szám, forrás, hely. Egy csendes lépés:
     a vászon szinte üres, egy mondat és a dátum.
  8. Budapest és az embermentők – Horthy július eleji leállítása, nyilas terror, gettó, Wallenberg, Lutz, Perlasca,
     Rotta nuncius, Sztehlo Gábor, Salkaházi Sára (1944. december 27.).
  9. Emlékezés és felelősség – áldozatok száma tartománnyal, a felelősség pontos alanyai; a magyarországi
     holokauszt-emléknap (április 16.), a roma holokauszt emléknapja (augusztus 2.); forráskritikai Tippelj!;
     ajánlás: Holokauszt Emlékközpont, DEGOB, Yad Vashem adatbázisai.
- **Adatok:**
  - Zsidóság 1941 (háborús határok): 725 007 izraelita vallású + kb. 100 000 a faji törvények szerint zsidónak
    minősülő, kb. 825 000 – USHMM Encyclopedia, „The Holocaust in Hungary”.
  - Zsidótörvények: 1920. évi XXV. tc. (numerus clausus, 1920. szeptember 26.: egyetemi felvétel a „népfajok és
    nemzetiségek” arányában, a zsidókat nem nevezi meg, arányuk kb. 6 %; 1928-ban módosítva); 1938. évi XV. tc. (20 %
    a szabad foglalkozásokban és a 10 főnél több alkalmazottú cégeknél); 1939. évi IV. tc. (6 %, részben faji
    meghatározás); 1941. évi XV. tc. (házassági tilalom, nagyszülők szerinti faji meghatározás) – net.jogtar.hu
    *Ezer év törvényei*.
  - Kamenyec-Podolszkij (1941. augusztus 26–28.): összesen kb. 23 600 áldozat; a Magyarországról kiutasított több
    mint 20 000 emberből kb. 14–16 ezret vittek oda (USHMM, Yad Vashem) – a „16–18 ezer” túl magas.
  - Deportálás: 1944. május 15. – július 9.; Veesenmayer 1944. július 11-i összesítése 437 402 fő; Ferenczy László
    csendőr alezredes: 434 351 fő, 147 szerelvény (július 9-ig; a szerelvények száma forrásonként 145–148).
    Zónánként (Braham, *A magyarországi holokauszt*; a napok és a zónaszámok *(ellenőrizendők)*):
    I+II. zóna (Kárpátalja és Északkelet-Magyarország; Észak-Erdély): május 15. – június 7., 289 357 fő, 92
    szerelvény; III. zóna (Budapesttől északra, Miskolc és Kassa környéke): június 11–16., 50 805 fő; IV. zóna
    (Duna–Tisza köze déli része és a Tiszántúl, Szeged, Debrecen, Szolnok): június 25–28., 41 499 fő (ebből kb.
    15 000 Strasshofba, nem Auschwitzba); V+VI. zóna (Dunántúl és a Budapest környéki települések): kb. június 30./
    július 4. – július 9., együtt 55 741 fő (Veesenmayer csak együtt közli). A négy szám összege pontosan 437 402;
    a július 6-i kumulált érték (381 661) az I–IV. zóna összege – Wikipédia „Operation Höss”, phdn.org (Klarsfeld),
    Braham magyarul a MEK-en (`mek.oszk.hu/11500/11506/…`).
  - Auschwitzba érkezett kb. 420 000 emberből kb. 330 000-et érkezéskor meggyilkoltak (USHMM).
  - Magyarországi zsidó áldozatok (háborús határok): az USHMM szerint kb. 550 000 (több mint 65 %); a HDKE „több mint
    500 000”-et ír (`hdke.hu/qr-086/`) → a lecke: **kb. 500–565 ezer** *(vitatott a tartományon belül)*.
  - Európai zsidó áldozatok: kb. 6 millió (USHMM, Yad Vashem); a szakirodalmi tartomány kb. 5,1–6,0 millió.
  - Roma áldozatok: Magyarországon legalább kb. 5 000, a magas becslések 15–20 ezer *(nagyon bizonytalan)*; az
    „50–70 ezer” az üldözöttek, nem a megöltek száma; Európában kb. 200–500 ezer vagy több *(vitatott)* –
    `kisebbsegkutato.tk.hu/…/Pharrajimos.pdf`, `coe.int/en/web/roma-genocide/hungary`.
  - Budapesti gettó felszabadulása: 1945. január 17–18. (a nemzetközi gettó január 16.) – USHMM.
  - Wallenberg érkezése: 1944. július 9. (USHMM); a „100 000 megmentett” túlzás, a USHMM „ezreket” ír, a többi semleges
    követséggel együtt „több ezer – több tízezer” *(vitatott)*; Carl Lutz: több mint 50 000 (USHMM), felső becslés
    62 000 (svájci külügy életrajza) *(vitatott)*.
  - Salkaházi Sára: kivégezték 1944. december 27-én (Yad Vashem: Világ Igaza; boldoggá avatták 2006-ban).
  - Horthy leállító rendelkezése: 1944. július 7. körül *(ellenőrizendő)*; sárga csillag: 1944. április 5.
    *(ellenőrizendő)*; Sztehlo Gábor által mentett gyermekek száma *(ellenőrizendő)*.
- **Modulok:** TortTerr (`zonak1944`, 1941-es országterület), TortCity, TortTimeline (lépcső), TortSource (három
  forrás), TortMap (Európa, táborok), MatChart (tartomány-sávok; a MatChart `bars` hiba-sávval vagy FoldChart `band`).
- **Review-pontok:** **történész + emlékezetpedagógus**; minden szám és dátum forrással; a „felelősség alanya”
  megfogalmazás; a 7. lépés (Auschwitz) hangneme; a Duna-parti helyszín jelölése; Radnóti-idézet (ha van) a
  lektorral egyeztetve; nincs kitalált személy; a „Tippelj!” csak forráskritikai.

### 09 · `09-hideghaboru` – Hogyan osztotta ketté Európát a vasfüggöny? – a hidegháború

- **Tanulási cél:** A háború után két **szuperhatalom** (USA, Szovjetunió) és két tömb alakult ki: **NATO** (1949) és
  **Varsói Szerződés** (1955). A **vasfüggöny** kettévágta Európát és **Németországot** (NSZK, NDK), Berlinben
  1961-től **fal** állt. A két fél nem harcolt közvetlenül, de **fegyverkezési versenyt** folytatott (atomfegyverek),
  és helyi háborúkban, válságokban ütközött (**Korea** 1950–53, **Kuba** 1962). Nyugaton **piacgazdaság** és
  **jóléti állam**, keleten tervgazdaság és diktatúra. Az **ENSZ** (1945) a béke őrzésére jött létre.
- **Kerettanterv:** „A kétpólusú világ – a vasfüggöny leereszkedése.” · „Németország kettéosztása.” · „Fegyverkezési
  verseny a Szovjetunió és az Amerikai Egyesült Államok között.” · „Hidegháborús konfliktusok: Korea, Kuba.” · „A
  nyugati demokrácia és piacgazdaság.” · „A jóléti társadalom.” · „Az új tömegkultúra kialakulása.” · Fogalmak:
  „Egyesült Nemzetek Szervezete (ENSZ), hidegháború, vasfüggöny, berlini fal, szuperhatalom, Észak-atlanti
  Szerződés Szervezete (NATO), Varsói Szerződés, piacgazdaság, jóléti állam.” · Személyek: „Hruscsov, Kennedy.” ·
  Kronológia: „1947 a párizsi béke, a hidegháború kezdete, 1948 Izrael Állam megalapítása.” · Topográfia: „Berlin,
  Németországi Szövetségi Köztársaság (NSZK), Német Demokratikus Köztársaság (NDK), Észak- és Dél-Korea, Kuba.” ·
  „Információk szerzése, rendszerezése és értelmezése a két szuperhatalom fegyverkezési versenyéről diagramok,
  táblázatok, képek és térképek segítségével.” · „A nyugati világ és a keleti blokk életkörülményeinek
  összehasonlítása.” · (13.) „Az Amerikai Egyesült Államok világhatalommá válása.”
- **Tévhitek:** „A hidegháborúban nem volt háború.” (Korea: kb. 2,5–3 millió halott *(ellenőrizendő)*.) „A berlini fal
  Kelet- és Nyugat-Németország határa volt.” (Nyugat-Berlint vette körül.) „Az atomfegyverek száma a hidegháború
  végéig nőtt.” (Az USA 1967-ben tetőzött.) „Magyarország semleges volt.”
- **Kulcsvizuál:** Európa-térkép (TortTerr, 1949-es egységek: NSZK, NDK, Berlin négy szektora, Ausztria
  1945–1955 megszállási övezetei *(opcionális)*): az államok a tömbtagság árnyalatával évről évre (évszám-csúszka
  1945 → 1991); a vasfüggöny vastag szaggatott vonal Stettintől Triesztig. Két FoldChart-görbe: amerikai és
  szovjet robbanófejek 1945–2024 (két semleges szín, végcímkékkel). Korea-betét: a front 1950 június → 1953 július
  (TortTerr `front`, négy kulcskocka). Kuba-betét: távolság-körök (vázlatos).
- **Kipróbálom:** évszám-csúszka a blokktérképen (NATO-belépők: 1952, 1955, 1982; Albánia kilépése 1968); a
  robbanófej-görbén kurzor: az adott év két száma; Berlin-nézet: kapcsoló a fal előtt/után.
- **Tippelj!** 5. lépés: „Melyik évben volt a legtöbb atomrobbanófej a világon? 1962 / 1986 / 2000” (1986, kb.
  70 300).
- **Lépések:**
  1. 1945 – győztesek: Jalta, Potsdam, ENSZ (1945. október 24.); párizsi béke (1947. február 10.).
  2. Leereszkedik a vasfüggöny – Fulton, 1946. március 5. (Churchill – † 1965, **nem közkincs**: egymondatos
     idézet forrással vagy parafrázis); a vonal a térképen.
  3. Németország kettéosztása – négy övezet, berlini blokád (1948. június 24. – 1949. május 12.), NSZK és NDK
     (1949), a fal (1961. augusztus 13.).
  4. Két tömb – NATO (1949. április 4., 12 ország) és Varsói Szerződés (1955. május 14., 8 ország) évszám-csúszkán.
  5. Fegyverkezési verseny – robbanófej-görbék; Tippelj!; a csúcs és a leszerelés.
  6. Korea – a front négy kulcskockája; fegyverszünet a 38. szélességi kör közelében (1953. július 27.).
  7. Kuba, 1962 – 13 nap (október 16–28.), Hruscsov és Kennedy; a hatótávolság-kör vázlatos.
  8. Két életmód – a nyugati jóléti állam és a keleti tervgazdaság: GDP/fő (Ausztria vs Magyarország, 1950–1990)
     FoldChart-on *(ellenőrizendő adatsor: Maddison Project Database 2023, CC BY 4.0)*; tömegkultúra
     (televízió, rock and roll, farmer) egy kártyán. Izrael Állam megalapítása (1948. május 14.) az idővonalon,
     értékelés nélkül.
  9. Honnan tudjuk? – a robbanófejek száma titok volt: a FAS becslése és ennek frissítései. Összefoglalás: a
     kétpólusú világ egy térképen.
- **Adatok:**
  - NATO: 1949. április 4., 12 alapító; Görögország és Törökország 1952. február 18.; NSZK **1955. május 6.**
    (május 9. az első részvétel – ne ezt írjuk); Spanyolország 1982. május 30. – `nato.int` „Member countries”.
  - Varsói Szerződés: 1955. május 14., 8 tag; Albánia 1961–62-től nem vett részt, 1968. szeptember 13-án kilépett;
    Magyarország kilépési nyilatkozata 1956. november 1.; katonai szervezete 1991. március 31-én, maga a szerződés
    1991. július 1-jén (Prága) szűnt meg.
  - Fulton-beszéd 1946. március 5.; berlini blokád 1948. június 24. – 1949. május 12. (a légihíd szeptember 30-ig);
    berlini fal 1961. augusztus 13. – 1989. november 9.; koreai háború 1950. június 25. – fegyverszünet 1953. július
    27.; kubai válság 1962. október 16–28.
  - Robbanófejek (USA / Szovjetunió–Oroszország): 1945: 2 / 0 · 1950: 299 / 5 · 1955: 2 422 / 200 · 1960: 18 638 /
    1 627 · 1965: 31 139 / 6 144 · 1970: 26 008 / 11 736 · 1975: 27 519 / 19 235 · 1980: 24 104 / 30 665 · 1985:
    23 368 / 38 582 · 1990: 21 392 / 32 980 · 1995: 10 904 / 18 179 · 2000: 10 577 / 12 188 · 2010: 5 066 / 5 215 ·
    2024: 3 708 / 4 380. Csúcs: USA 31 255 (1967), Szovjetunió 40 159 (1986); a világ összesen kb. 70 300 (1986) –
    FAS (Kristensen–Korda), OWID „Nuclear warhead stockpiles” (CC BY 4.0) *(a FAS frissíti: „FAS, 2025-ös
    adatsor”; a 2013-as táblázat késő szovjet értékei magasabbak)*.
  - NSZK és NDK megalakulása: 1949. május 23. és október 7. *(ellenőrizendő)*; Izrael: 1948. május 14.; ENSZ
    alapokmány hatálya: 1945. október 24.; párizsi béke: 1947. február 10. *(szokásos kronológia)*.
  - Koreai háború halottai kb. 2,5–3 millió *(ellenőrizendő)*.
- **Modulok:** TortTerr (1949-es Európa, Berlin, Korea-front), TortMap (`map-europa.js`), FoldChart (két görbe,
  `endLabels`, `cursor`), TortTimeline, TortGlobe (USA–SZU távolság), TortSource, TtTipp.
- **Review-pontok:** a vasfüggöny-vonal és a berlini szektorok vázlata; a „jóléti állam vs tervgazdaság”
  összehasonlítás adattal, nem jelzővel; a robbanófej-adatsor verziója; a hidegháború és a mai világ összevetése
  (fejlesztési feladat) csak kérdésként a tanárnak.

### 10 · `10-szovjetizalas` – Hogyan lett a többpártrendszerből egypártrendszer? – Magyarország 1945–1953

- **Tanulási cél:** 1945-ben a szovjet hadsereg megszállta Magyarországot; százezreket hurcoltak **„malenkij
  robotra”**; a **németeket** kollektív bűnösség elve alapján **kitelepítették**, Csehszlovákiával **lakosságcsere**
  történt. Az **1945-ös** választáson a Független Kisgazdapárt abszolút többséget szerzett, a kommunisták 17 %-ot.
  A Magyar Kommunista Párt szovjet támogatással, „szalámitaktikával” szorította ki ellenfeleit (Kovács Béla
  elhurcolása 1947), az **1947-es** „kékcédulás” választáson csalással is; 1948–49-re **egypártrendszer** jött
  létre. A **Rákosi-diktatúra** (1948–1956): **ÁVH**, személyi kultusz, egyházüldözés (Mindszenty József),
  **államosítás**, **tervgazdaság**, internálótáborok (Recsk), kitelepítések (Hortobágy). A határon túli magyarokat
  is deportálások és munkatáborok sújtották.
- **Kerettanterv:** „Háborús pusztítás és szovjet megszállás, deportálások a szovjet munkatáborokba.” · „Bűnbakká tett
  németek és magyarok – kitelepítések, lakosságcsere.” · „Az 1945-ös és 1947-es választások.” · „Egypártrendszer,
  államosítás, diktatúra.” · „Az ÁVH működése.” · „A személyi kultusz.” · „Az egyházüldözés.” · „A tervgazdaság
  működése.” · „A határon túli magyarok megpróbáltatásai: deportálások Csehszlovákiában; szovjet, román és jugoszláv
  munkatáborok.” · „Magyarországi kitelepítések és munkatáborok.” · Fogalmak: „malenkij robot, államosítás,
  tervgazdaság, Államvédelmi Hatóság (ÁVH).” · Személyek: „Kovács Béla, Rákosi Mátyás, Mindszenty József.” ·
  Kronológia: „1945 szovjet megszállás, választás Magyarországon, 1948–1956 a Rákosi-diktatúra.” · Topográfia:
  „Recsk, Hortobágy, Duna-delta.” · tevékenység: „Új iparvárosok azonosítása térképen.”
- **Tévhitek:** „1945-ben a kommunisták megnyerték a választást.” „Az egypártrendszer egy nap alatt jött létre.”
  „A malenkij robot csak katonákat érintett.” „A kitelepítés csak a háborús bűnösöket érintette.” „A tervgazdaság
  azt jelenti, hogy mindenki megkapta, amire szüksége volt.”
- **Kulcsvizuál:** **TortParl** patkó 1945 → 1947 → 1949, ugyanazzal a semleges pártszínkészlettel; a **TortState**
  sémán (Országgyűlés, kormány, pártok, sajtó, egyházak, bíróság, rendőrség, szövetkezetek, magántulajdon) a
  „szalámi”-szeletek egyenként, dátummal válnak le vagy kerülnek a párt alá (szürke → bordó keret). Külön lépésben
  Kárpát-medence + Szovjetunió-térkép (TortMap, `map-europa.js`): a malenkij robot és a kitelepítések irányai
  vékony, halvány nyilakkal *(vázlatos, nagyságrendi vastagság)*, nem animált tömeg.
- **Kipróbálom:** a TortState „szalámi” gombja lépésenként veszi le a szeleteket; a TortParl-on a kékcédula
  kapcsoló megmutatja, mennyit változtat a csalás tartománya a mandátumokon (a tartomány két végével, „becslés”
  bélyeggel) – és hogy a csalás **nem** fordította meg az 1947-es eredményt, a kiszorítás már előtte megtörtént.
- **Tippelj!** 3. lépés: „Hány százalékot kapott a kommunista párt 1945 novemberében? kb. 17 % / kb. 35 % / több mint
  50 %”.
- **Lépések:**
  1. 1945 – megszállás és pusztítás; malenkij robot (tartomány), visszaemlékezés *(parafrázis)*.
  2. Bűnbakok – a németek kitelepítése; a csehszlovák–magyar lakosságcsere és a csehországi deportálás; a
     jugoszláv és a román munkatáborok, a Duna-delta (a 14-gyel összhangban).
  3. 1945. november 4. – a választás, TortParl; Tippelj!
  4. Szalámitaktika – Kovács Béla (1947. február 25., szovjet hatóság), Nagy Ferenc lemondása (1947. június)
     *(ellenőrizendő)*; TortState-szeletek.
  5. 1947. augusztus 31. – kékcédulás választás, tartomány; a választói névjegyzékből kihagyottak.
  6. Egypártrendszer – MDP (1948. június), 1949-es egylistás választás, 1949. évi XX. törvény (alkotmány, augusztus
     20.) – a kapcsolók kialszanak.
  7. Rákosi-diktatúra – ÁVH, személyi kultusz *(jelkép-helyőrző)*, Mindszenty-per (1949), államosítás (1948–49),
     tervgazdaság (első ötéves terv 1950); új iparvárosok (Sztálinváros/Dunaújváros, Kazincbarcika, Komló stb.) a
     térképen.
  8. Kitelepítés „békeidőben” – Budapest 1951; Hortobágy 1950–53 (12 tábor); Recsk (1950–53). Honnan tudjuk? – az
     ÁBTL iratai és a túlélők visszaemlékezései.
  9. Összefoglalás – 1945 → 1949: hány intézmény maradt szabad?
- **Adatok:**
  - Malenkij robot (hadifoglyok és polgári deportáltak együtt): kb. 600–700 ezer (Stark Tamás); a szovjet iratok
    500–540 ezret adnak; ebből polgári kb. 100–300 ezer; kb. 200 000-en nem tértek vissza *(vitatott)* –
    Történelmi Szemle 2012/2 (`epa.oszk.hu/00600/00617/00033/…`).
  - Németek: az 1941-es népszámlálás a trianoni területen 477 057 német anyanyelvű és kb. 302–303 ezer német
    nemzetiségű *(a nemzetiségi szám ±1 000 bizonytalan)* (az 533 045 a megnagyobbodott ország adata – ne keverjük);
    kitelepítés 1946–48: kb. 170–200 ezer (1946-ban kb. 120–135 ezer az amerikai, 1947–48-ban kb. 50 ezer a szovjet
    övezetbe; gyakran idézett: 185 000) *(vitatott)* – Tóth Ágnes.
  - Csehszlovák–magyar lakosságcsere (1947. április – 1948. december): kb. 73 000 szlovák távozott, kb. 68–73 ezer
    magyar érkezett a csere keretében (azon kívül távozókkal kb. 90 000); kb. 44 000 magyart Csehországba deportáltak
    – Acta Historica (`ojs.bibl.u-szeged.hu/…/10256/…`) *(vitatott)*.
  - Választás 1945. november 4.: FKGP 57,03 % (2 697 137 szavazat), SZDP 17,41 %, MKP 16,96 % (801 986 / 4 729 301;
    a magyar források gyakran 16,95 %-ot írnak – kerekítés), NPP 6,87 %, PDP 1,62 %; részvétel kb. 92,5 %
    (Nohlen–Stöver). Mandátumok (FKGP 245, MKP 70, SZDP 69, NPP 23, PDP 2; összesen 409) *(ellenőrizendő)*.
  - Választás 1947. augusztus 31.: MKP 22,25 % (1 111 001 szavazat); a kékcédulás pótszavazatok kb. 60–200 ezer
    *(vitatott)*; kb. 500 000 választót hagytak ki a névjegyzékből – parlament.hu Országgyűlési Múzeum
    „Koalíció – kékcédula”.
  - Hortobágy (1950–53): legalább 8 000, kb. 10 000 ember, 12 tábor (8 a Hortobágyon, 4 a Nagykunságon); az 1953-as
    belügyi jelentés 7 200-nál több főt számolt (a „2 000–2 500” valószínűleg a családok száma, nem igazolt) –
    hvg.hu 2010.
  - Budapesti kitelepítés (1951. május 21. – július 18.): kb. 12 700–14 000 fő (Jávor: 13 670; Széchenyi Kinga: kb.
    14 000), + 1 194 vidéki városokból.
  - Recsk: 1950–1953, a foglyok száma kb. 1 300–1 700 *(ellenőrizendő)*; Mindszenty letartóztatása 1948. december 26.,
    ítélet 1949. február *(ellenőrizendő)*; MDP: 1948. június 12. *(ellenőrizendő)*; 1949. évi XX. törvény (augusztus
    20.) – jogszabály.
- **Modulok:** TortParl, TortState, TortMap, TortTerr (1945–47 határ: a pozsonyi hídfő három faluja), TortTimeline,
  TortSource, TtTipp.
- **Review-pontok:** **történész lektor**; a „bűnbakká tett” megfogalmazás (a kerettantervé) mellett a pontos alany
  (a kitelepítést a magyar kormány hajtotta végre a potsdami döntés alapján); a malenkij robot és a kitelepítés
  tartományai; a csalás mértékének óvatos bemutatása.

### 11 · `11-forradalom-1956` – Mi történt 13 nap alatt? – az 1956-os forradalom és szabadságharc

- **Tanulási cél:** 1956. október 23-án egy diáktüntetésből forradalom lett; a harcokat (Corvin köz, „pesti
  srácok”) a fegyverszünet és a többpártrendszer helyreállítása követte; Nagy Imre kormánya november 1-jén
  kilépett a Varsói Szerződésből és kimondta a semlegességet. November 4-én a szovjet hadsereg leverte a
  forradalmat. Kb. 2 700 magyar halt meg, kb. 200 000 ember menekült el, a **megtorlásban** kb. 229 embert
  végeztek ki (köztük Nagy Imrét, 1958). A forradalom a világ figyelmének középpontjába került, de nyugati
  katonai segítség nem jött (Szuezi válság). A forradalom jelképei: a lyukas zászló, a Kossuth-címer, a 16 pont.
- **Kerettanterv:** „Október 23., a forradalom kirobbanása.” · „A pesti srácok és szabadsághősök.” · „A forradalom
  lakóhelyünkön és környékén.” · „Szovjet tankokkal a népakarat ellen.” · „A forradalom jelképei.” · „A magyar
  forradalom a világtörténelem színpadán.” · „A kádári megtorlás.” · Fogalmak: „Molotov-koktél, sortüzek,
  munkásőrség” · Személyek: „Nagy Imre, Kádár János” · Kronológia: „1956. október 23. a forradalom kitörése, 1956.
  november 4. a szovjet támadás” · Topográfia: „Corvin köz, Mosonmagyaróvár.” · „Beszámolók készítése az 1956-os
  forradalom és szabadságharc hőseiről.” · „Az 1956-os forradalom és szabadságharc utáni megtorlások
  kegyetlenségének bemutatása példákon keresztül.” · tevékenység: „Térképvázlat készítése az 1956-os események
  budapesti helyszíneiről.”
- **Tévhitek:** „A forradalom egy napig tartott.” „Csak Budapesten történt valami.” (Mosonmagyaróvár, Miskolc,
  Győr…) „A Nyugat katonailag segített.” „Nagy Imre végig a forradalom vezetője volt.” (Fokozatosan állt mellé.)
  „1956 után minden ugyanúgy folytatódott, mint előtte.” (A 12 viszi tovább.)
- **Kulcsvizuál:** a **TortCity** Budapest-térkép éjszakai helyett **papír** alapon, a helyszínek az idővonal
  óráival: Műegyetem (október 22., a 16 pont), Bem tér, Kossuth tér, a Rádió (Bródy Sándor utca – az első lövések),
  a Sztálin-szobor ledöntése (Dózsa György út), Corvin köz, Széna tér, Köztársaság tér. A 13 nap TortTimeline-on,
  minden naphoz egy-két esemény. Vidéki betét (TortMap, Kárpát-medence): a forradalmi tanácsok és a sortüzek
  helyszínei (Mosonmagyaróvár, Miskolc, Győr, Tiszakécske stb.) *(ellenőrizendő lista)*. A menekültek lépésében
  vékony, halvány nyilak Ausztria és Jugoszlávia felé, majd tovább a befogadó országokba (MatChart-sáv a befogadók
  szerint *(ellenőrizendő)*).
- **Kipróbálom:** idővonal-csúszka október 23. 14 óra → november 11.; a térképen a helyszínek a csúszka szerint
  gyulladnak ki, rákattintva rövid, forrásolt eseménykártya. A „lakóhelyünkön” lépésben a tanár a `.md`-ben egy saját
  helyszínt adhat meg (kulcs + koordináta) – a lecke kirajzolja.
- **Tippelj!** 6. lépés: „Hány ember hagyta el az országot 1956 végéig? kb. 20 ezer / kb. 150 ezer / kb. 1 millió”.
- **Lépések:**
  1. Előzmények – Sztálin halála (1953), Nagy Imre első kormánya, 1956 tavasza (az SZKP XX. kongresszusa), a lengyel
     október.
  2. Október 22–23. – a 16 pont, a tüntetés útvonala, a Rádió; TortCity + idővonal.
  3. Harcok – Corvin köz, Molotov-koktél, „pesti srácok” (*hagyomány*-réteg: az emlékezet és a források
     különbsége); sortüzek (Kossuth tér október 25., Mosonmagyaróvár október 26.) tartománnyal.
  4. Győzelem? – október 28. tűzszünet, többpártrendszer, november 1. kilépés a Varsói Szerződésből; jelképek
     (lyukas zászló – rajzolva).
  5. November 4. – szovjet támadás; Kádár János kormánya; a harcok vége.
  6. A világ színpadán – ENSZ, Szuez (október 29.), menekültek; Tippelj!
  7. Áldozatok – magyar és szovjet halottak, sebesültek, tartománnyal; nincs animált számláló.
  8. Megtorlás – a kivégzettek száma, Nagy Imre (1958. június 16.); munkásőrség (1957). Honnan tudjuk? – a perek
     iratai (perek56.hu), a KSH titkos 1957-es jelentése *(ellenőrizendő)*.
  9. Emlékezet – 1989. június 16. újratemetés; október 23. nemzeti ünnep (1990. évi XXVIII. tv. *(ellenőrizendő)*); összefoglalás.
- **Adatok:**
  - Október 23. és november 4. – ellenőrizve; Nagy Imre kivégzése 1958. június 16.
  - Magyar halottak: kb. 2 500 ismert, összesen kb. 2 700 (Betekintő 2016/3, Tulipán–Molnár); kb. 13 000 sebesültet
    láttak el (KSH).
  - Szovjet halottak: a Britannica szerint több mint 650 halott, kb. 1 250 sebesült; más számok 669 vagy 699 halott és
    51 eltűnt → „kb. 700” *(vitatott)*.
  - Menekültek: kb. 150 000 1956. december 31-ig (KSH infografika 2024); 1957-tel együtt kb. 176–200 ezer
    *(vitatott)* – `ksh.hu/infografika/2024/1956_2024_infograf_hun.pdf`.
  - Kivégzettek: kb. 229 (a szokásos szám; más számolások 225 – szigorúan 1956-os ügyben – vagy 220–340) – NEB/Kúria
    adatbázis (perek56.hu).
  - Szuezi válság: 1956. október 29. *(szokásos kronológia)*; Varsói Szerződésből való kilépés: november 1.
  - Sortüzek áldozatai (Kossuth tér, Mosonmagyaróvár) *(ellenőrizendő, tartománnyal)*; a bevetett szovjet erők
    létszáma *(ellenőrizendő)*; elítéltek és internáltak száma *(ellenőrizendő)*.
  - Helyszínek koordinátái (Wikidata, CC0) a `.md` `### Adatok` alatt.
- **Modulok:** TortCity, TortTimeline (13 nap, órás felbontás), TortMap (vidék, menekültek), MatChart, TortSource,
  TtTipp.
- **Review-pontok:** **történész lektor**; a sortüzek számai; a „pesti srácok” emlékezetének rétegjelölése; a
  forradalmárok és a szovjet katonák áldozatai egyaránt számként, méltósággal; a megtorlás példái névvel csak
  közismert esetben (Nagy Imre, Mansfeld Péter *(ellenőrizendő)*).

### 12 · `12-kadar-rendszer` – Hány évet kellett várni egy autóra? – élet a Kádár-rendszerben

- **Tanulási cél:** A megtorlás után a **Kádár-rendszer** (1956–1989) „kompromisszumot” kínált: nem szólsz bele a
  politikába – cserébe lassan javuló életszínvonal („**gulyáskommunizmus**”, „a legvidámabb barakk”). A
  **pártállam** megmaradt: egy párt (MSZMP), tömegszervezetek (KISZ, úttörő), munkásőrség, cenzúra. A
  **téeszesítés** (1959–61) felszámolta a paraszti gazdaságokat, a **háztáji** és a **második gazdaság** (maszek)
  pótolta, amit a tervgazdaság nem adott. A **hiánygazdaság**ban sorban álltak (autó, lakás, telefon). Az
  életszínvonalat egyre több **külföldi hitelből** tartották fenn: az adósság 1973 és 1989 között
  tízszeresére nőtt.
- **Kerettanterv:** „A pártállam működése: az elnyomás változó formái.” · „Ellenőrzött társadalom,
  tömegszervezetek.” · „A paraszti gazdaságok felszámolása, téeszesítés.” · „A szocialista modernizáció – „a
  legvidámabb barakk”.” · „A hiánygazdaság.” · „A második gazdaság kiépülése.” · „Életszínvonal-politika és
  eladósodás.” · Fogalmak: „Magyar Szocialista Munkáspárt (MSZMP), Kommunista Ifjúsági Szövetség (KISZ), úttörő,
  termelőszövetkezet, háztáji, maszek, gulyáskommunizmus” · Kronológia: „1956–1989 a Kádár-rendszer” · „Érvek
  gyűjtése a Kádár-rendszer diktatórikus jellegének alátámasztására.” · „A Kádár-rendszer és napjaink
  életkörülményeinek összehasonlítása.” · tevékenység: „Gazdasági és társadalmi diagramok, grafikonok elemzése a
  szocializmus válságának időszakából.”
- **Tévhitek:** „A Kádár-rendszer nem volt diktatúra.” „A Kádár-rendszerben mindenki egyformán élt.” „A jólét a
  saját termelésből jött.” (Részben hitelből.) „A hiány azt jelenti, hogy nem volt pénz.” (Pénz volt, áru nem.)
  „Az adósság az 1980-as évek végén hirtelen keletkezett.”
- **Kulcsvizuál:** a **sorban állás** – egy Merkur-várólista *(modell)* animációja: a diák a sor végére áll, a sor
  évente csak néhány helyet halad, és a „várható idő” kijelző a kínálat/kereslet aránytól függ. Mellette a valódi
  adat (2–5 év, 1988-ban 360 000 várakozó). Utána a FoldChart **adósság-görbe** 1970–1990 (milliárd USD), két
  változattal az 1980-as évek végén: a korábban közölt és a később (1989) feltárt, magasabb adatsor. A pártállam
  lépésben TortState: MSZMP a séma fölött, minden intézmény felé „irányít” nyíl.
- **Kipróbálom:** a várólista-modell két csúszkája (évi kínálat, igénylők száma) – „miért nem segít, ha több a
  pénz?”; az adósság-görbén kurzor és kapcsoló a két adatsor között.
- **Tippelj!** 6. lépés: „Hányszorosára nőtt a bruttó devizaadósság 1973 és 1989 között? kb. 2× / kb. 10× / kb.
  100×” (2,12 → 20,4 milliárd USD ≈ 9,6×).
- **Lépések:**
  1. Megtorlás után – „aki nincs ellenünk, az velünk van” (Kádár, 1961 *(parafrázis; † 1989, nem közkincs)*); az
     1963-as amnesztia *(ellenőrizendő)*.
  2. A pártállam – TortState; tömegszervezetek; munkásőrség; a „3 T” (tiltott, tűrt, támogatott); az elnyomás
     változó formái (megfigyelés, útlevél, állás).
  3. Téeszesítés – 1959–61: a paraszti földek a szövetkezetekbe (oszlopok); háztáji.
  4. Új gazdasági mechanizmus (1968) és a második gazdaság – maszek, gmk (1982).
  5. Hiánygazdaság – a várólista-modell; a valódi várakozási idők.
  6. Eladósodás – adósság-görbe; Tippelj!; IMF-tagság (1982. május 6.).
  7. Mindennapok – úttörő, KISZ, televízió, Balaton, utazás nyugatra (világútlevél 1988 *(ellenőrizendő)*); a
     „legvidámabb barakk” jelentése: vidámabb, de barakk.
  8. Honnan tudjuk? – a titkosított statisztika: miért javította fel az MNB 1989-ben az adósságadatot.
  9. Összefoglalás – érvek a diktatórikus jellegre (a kerettanterv feladata) egy táblán, adatokkal.
- **Adatok:**
  - Bruttó konvertibilis devizaadósság, év vége, milliárd USD: 1970: kb. 0,5 (Szalai, MNB); 1973: 2,12; 1975: 4,20;
    1980: kb. 10,5 („1980-ra 10 milliárd felett”); 1985: 14,0; 1987: 19,6 (a felülvizsgált MNB-sor; a korábban
    közölt kb. 17,7); 1989: 20,4; 1990: 21,3 – Nagy Pongrác, *Gazdaság és Társadalom* 1999/1–2, 2. táblázat
    (`epa.hu/05000/05050/00036/…`), Szalai Zoltán, MNB (`mnb.hu/letoltes/szalai-zoltan-…`) *(1980 és 1987
    vitatott)*.
  - IMF-tagság: 1982. május 6.
  - Autóra várakozás (Merkur): kb. 2–5 év a keleti autókra, 10 % előleggel; Skoda, Dacia kb. 1 év; 1988-ban 360 000
    várakozó (penzcentrum.hu, 2009) *(ellenőrizendő; a „Trabantra 4–6 év” szóbeszéd, nem adat)*.
  - Téeszesítés: 1959–61 (1961 februárjában „befejezettnek” nyilvánítva); 1961–62-re a szocialista szektor
    (szövetkezet + állami gazdaság) a mezőgazdasági terület több mint 95 %-án, ebből a szövetkezetek kb. 75–80 %
    *(vitatott a megosztás)*.
  - Második gazdaság: a háztartások kb. ¾-e vett részt, a munkaidő kb. ⅓-a *(ellenőrizendő – forrás nélkül nem
    kerülhet a vászonra)*.
  - Új gazdasági mechanizmus: 1968. január 1. *(szokásos)*; gmk: 1982 *(ellenőrizendő)*.
- **Modulok:** FoldChart (görbe, `band`, kurzor), TortState, MatChart, TortCards, TortSource, TtTipp.
- **Review-pontok:** a várólista-modell „modell” bélyeggel, a valódi adat mellette; a „nosztalgia” és a „csak
  elnyomás” egyoldalúsága helyett adat; a kerettanterv „Érvek gyűjtése a Kádár-rendszer diktatórikus jellegének
  alátámasztására” feladatát a lecke tényekkel szolgálja ki (egypártrendszer, megfigyelés, cenzúra, választás
  egyetlen listával).

### 13 · `13-rendszervaltas` – Hogyan omlott össze egy év alatt a keleti blokk? – a rendszerváltoztatás

- **Tanulási cél:** Az 1980-as években a szovjet rendszer gazdasági és politikai válságba került (Gorbacsov
  reformjai 1985-től). 1989-ben Közép-Európában **dominóként** dőltek a kommunista rendszerek: Lengyelország
  (június), Magyarország (tárgyalásos átmenet: **Nemzeti Kerekasztal**, köztársaság 1989. október 23.), az NDK
  (berlini fal, november 9.), Csehszlovákia (november 17.), Bulgária, Románia (december). Magyarország szerepe: a
  határzár bontása és a keletnémet menekültek átengedése (1989. szeptember 11.). 1990-ben **szabad választás**,
  1991-ben a szovjet csapatok kivonulása, a Varsói Szerződés és a **Szovjetunió felbomlása** (15 állam). Utána
  **piacgazdaság** és **jogállam** épült – vesztesekkel és nyertesekkel (munkanélküliség, privatizáció);
  **NATO**-tagság 1999, EU-tagság 2004.
- **Kerettanterv:** „A Szovjetunió és a szocialista rendszer országainak válsága.” · „Az ellenzék megszerveződése
  Magyarországon.” · „A tárgyalásos rendszerváltoztatás.” · „A kétpólusú világ megszűnése.” · „Az első szabad
  országgyűlési és önkormányzati választás.” · „Antall József kormánya.” · „A demokrácia és a piacgazdaság
  kiépítése.” · „A többpártrendszer működése.” · „Gazdasági válság és felzárkózás – vesztesek és nyertesek.” · „A
  társadalom átalakulása.” · „Magyarország NATO-tagsága.” · Fogalmak: „rendszerváltoztatás, privatizáció, jogállam,
  többpártrendszer.” · Személyek: „Gorbacsov, Reagan, II. János Pál, Antall József, Göncz Árpád, Horn Gyula, Orbán
  Viktor.” · Kronológia: „1989–1990 a rendszerváltoztatás, 1990 az első szabad választások, 1991 a Szovjetunió
  felbomlása, 1999 Magyarország belép a NATO-ba.” · „A magyar történelem legfontosabb politikai eseményeinek
  időrendbe állítása a rendszerváltoztatástól napjainkig.” · (13.) „A visegrádi együttműködés.”
- **Tévhitek:** „A rendszerváltás egyetlen nap volt.” „A berlini fal leomlása indította el.” (Lengyelország és
  Magyarország már előtte.) „Mindenhol békésen zajlott.” (Románia.) „A piacgazdaság mindenkinek azonnal jobb volt.”
  „A Szovjetunió és Oroszország ugyanaz.”
- **Kulcsvizuál:** Közép- és Kelet-Európa (TortTerr, 1989-es egységek): az országok a dátum szerint váltanak (sötét
  tinta → papír), **dominó**-sorrendben, minden dominón dátum és egy szó („választás”, „kerekasztal”, „fal”,
  „bársony”, „december”). Mellette TortTimeline 1985 → 1991. A TortState-sémán az 1989-es alkotmánymódosítás
  „bekapcsolja” az intézményeket (köztársasági elnök, Alkotmánybíróság, szabad választás, többpártrendszer,
  szabad sajtó) – a 10-es lecke kialvó kapcsolóinak tükörképe. Az 1990-es **TortParl** patkó **szürke
  árnyalatokban**, a pártok nevével és mandátumával (a mandátumszám szerinti sorrendben). A záró lépésben a
  Szovjetunió 15 utódállama szétválik (TortTerr `explode`).
- **Kipróbálom:** dominó-csúszka (1989. január → december) és kattintható országok (adatkártya: dátum, mi történt,
  áldozatok, ha voltak). A TortState-en a diák kapcsolja be az intézményeket, és a séma kiírja, mit ellenőriz az új
  intézmény.
- **Tippelj!** 3. lépés: „Melyik országban dőlt meg elsőként a kommunista párt hatalommonopóliuma 1989-ben?
  Lengyelország / NDK / Románia”.
- **Lépések:**
  1. Válság – adósság, hiány, Gorbacsov (1985), II. János Pál lengyel pápa (1978) és a Szolidaritás (1980), Reagan
     fegyverkezési nyomása – tényként, egy-egy mondatban.
  2. Magyar ellenzék – szervezetek alapítása idővonalon (név és dátum, értékelés nélkül) *(ellenőrizendő dátumok)*.
  3. 1989 – a dominó; Tippelj!
  4. A határ megnyílik – május 2., június 27., augusztus 19., szeptember 11.; Nagy Imre újratemetése (június 16.).
  5. Tárgyalásos átmenet – Nemzeti Kerekasztal (június 13. – szeptember 18.), köztársaság (október 23.); TortState
     bekapcsol.
  6. 1990 – az első szabad választás (március 25., április 8.), szürke TortParl; önkormányzati választás (1990 ősz);
     kormányfő és köztársasági elnök tényként (Antall József, Göncz Árpád).
  7. A kétpólusú világ vége – szovjet kivonulás (1991. június 19.), Varsói Szerződés (július 1.), Szovjetunió
     (december 26.) – 15 utódállam; Visegrád (1991. február 15.).
  8. Piacgazdaság – privatizáció, munkanélküliség, GDP (FOLD_WDI-görbe 1990–2004), „vesztesek és nyertesek” két
     oszlopban, adattal. Honnan tudjuk? – a KSH munkaerő-felmérése (1992-től) *(ellenőrizendő)*.
  9. Idővonal napjainkig – 1990 → 2004: kormányfők tényszerű címkével (név, hivatali idő), NATO (1999. március
     12.), EU (2004. május 1.); a 2004 utáni rész csak az országgyűlési választások éveivel, név nélkül.
     Összefoglalás.
- **Adatok:**
  - Határzár bontása 1989. május 2.; Horn–Mock jelképes drótvágás június 27. (Sopron/Klingenbach közelében);
    páneurópai piknik augusztus 19.; a határ megnyitása a keletnémetek előtt szeptember 11. 0 óra (bejelentés
    szeptember 10. este) – bpb.de, cvce.eu.
  - Nagy Imre újratemetése június 16.; Nemzeti Kerekasztal június 13. – szeptember 18.; a köztársaság kikiáltása
    október 23.; lengyel választás június 4. (második forduló június 18.); berlini fal november 9.; bársonyos
    forradalom november 17.; Románia: Temesvár december 16., Ceaușescu kivégzése december 25. *(szokásos
    kronológia)*.
  - Választás 1990. március 25. és április 8.: MDF 164, SZDSZ 92, FKGP 44, MSZP 33, Fidesz 21, KDNP 21,
    Agrárszövetség 1, független 6, közös jelölt 4 – összesen 386 (176 egyéni + legfeljebb 152 területi listás +
    legalább 58 országos kompenzációs) – Wikipédia „1990 Hungarian parliamentary election” (az eredménytábla; az
    infobox tévesen SZDSZ 94), 1989. évi XXXIV. tv.
  - Szovjet csapatok: az utolsó katona 1991. június 19.; Varsói Szerződés 1991. július 1.; Szovjetunió 1991. december
    26. (Gorbacsov lemondása december 25.).
  - NATO-tagság 1999. március 12.; EU 2004. május 1.; Visegrád 1991. február 15.
  - Kormányfők 1990–2004 (név, hivatali idő) *(ellenőrizendő: parlament.hu, kormany.hu archívum)*; Antall József
    1990. május 23.; Göncz Árpád köztársasági elnök 1990. augusztus 3. *(ellenőrizendő)*.
  - Munkanélküliségi ráta és GDP 1990–2004: FOLD_WDI (Világbank WDI, CC BY 4.0) – a foglalkoztatási adat 1991-től.
- **Modulok:** TortTerr (1989 Európa, SZU 15 utódállam), TortState, TortParl, TortTimeline, FoldChart (FOLD_WDI),
  TortSource, TtTipp.
- **Review-pontok:** **történész lektor**; **semlegesség 1990 után** (0. döntés, 9.): a TortParl szürke, a pártok
  sorrendje mandátum szerint; nincs jelző kormányokra, pártokra; az ellenzéki szervezetek felsorolása teljes és
  kiegyensúlyozott; a „vesztesek és nyertesek” adattal.

### 14 · `14-hataron-tul` – Miért lettek kevesebben a határon túli magyarok? – együttélés a Kárpát-medencében

- **Tanulási cél:** 1920 óta kb. 3 millió magyar él a szomszédos országokban; a számuk népszámlálásról
  népszámlálásra csökken (**asszimiláció**, **kivándorlás**, alacsony születésszám, a háború utáni **kitelepítések**
  és megtorlások). A fordulópontok: a felosztás (1920), a revízió (1938–41), az 1944–45-ös magyarellenes
  atrocitások, a kitelepítések, a rendszerváltás. Magyarországon is élnek **nemzetiségek** (roma, német, szlovák,
  román, horvát, szerb és mások – 13 elismert nemzetiség); arányuk a 19. század óta az asszimiláció és a
  kitelepítés miatt csökkent. A kerettanterv két példamutató életútja: **Esterházy János** és **Márton Áron**.
- **Kerettanterv:** „Határon túli magyarlakta területek.” · „Fordulópontok a határon túli magyarok történetében: a
  történelmi Magyarország felosztása, a revízió, magyarellenes megtorlások, rendszerváltoztatás.” · „A kisebbségi lét
  nehézségei egykor és ma: adminisztratív intézkedések és mindennapok.” · „Kivándorlás és asszimiláció.” ·
  „Magyarország nemzetiségi arányainak változása.” · „Az asszimiláció folyamata.” · „A hazai cigány/roma népesség
  története.” · „A nemzetiségi jogok a mai Magyarországon.” · Fogalmak: „kitelepítés, asszimiláció.” · Személyek:
  „Esterházy János, Márton Áron.” · Kronológia: „1944–1945 magyarellenes atrocitások.” · Topográfia: „Szlovákia,
  Ukrajna.” · „A Kárpát-medence 1910-es és 1990 utáni etnikai térképének összehasonlítása a magyarság és a
  nemzetiségek elhelyezkedése szempontjából.” · „Példák gyűjtése a Kárpát-medence népeinek együttműködésére és
  konfliktusaira a történelem során.” · (14.) „Új típusú kapcsolatépítés a rendszerváltoztatás után a kisebbségbe
  került magyarsággal.”
- **Tévhitek:** „A határon túli magyarok bevándorlók.” (Nem ők mozdultak, hanem a határ.) „Minden határon túli
  terület magyar többségű.” „A fogyás csak elvándorlás.” „Magyarországon nincsenek nemzetiségek.” „A népszámlálás
  mindig ugyanazt méri.” (Anyanyelv, nemzetiség, több válasz.)
- **Kulcsvizuál:** a mai szomszéd országok **megyéi/régiói** (FoldChoro a `map-torthatar.js` admin-1 egységein,
  Natural Earth) a magyar nemzetiségűek aránya szerint színezve, két állapottal: **1910** (az akkori anyanyelvi
  adat, ugyanarra a mai egységre átszámolva – csak ha a forrás így közli *(ellenőrizendő)*) és a **legutóbbi
  népszámlálás** (2021/2022). Áttűnés a két állapot között. Mellette FoldChart: országonként egy görbe 1910 → 2022
  (Románia, Szlovákia, Szerbia/Vajdaság, Ukrajna/Kárpátalja, Horvátország, Ausztria/Burgenland, Szlovénia). A
  hazai nemzetiségek lépésében MatChart: 1910 (a mai területen) → 1941 → 2011 → 2022.
- **Kipróbálom:** régióra kattintva az adatkártya a népszámlálási sort mutatja (év, fő, arány, a kérdés típusa:
  anyanyelv vagy nemzetiség); az „anyanyelv / nemzetiség” kapcsoló, ahol mindkét adat megvan (Románia 2021,
  Kárpátalja 2001).
- **Tippelj!** 3. lépés: „Melyik szomszéd országban fogyott a magyarság a legnagyobb arányban 1991 óta? Románia /
  Szlovákia / Szerbia (Vajdaság)” (Vajdaság 339 491 → 182 321, kb. −46 %; Románia 1 620 199 → 1 002 151, kb.
  −38 %; Szlovákia 567 296 → 422 065, kb. −26 % – számolt).
- **Lépések:**
  1. Nem ők mentek el – a határ mozdult (visszautalás a 04-re): 1910 → 1920, kb. 3,2–3,3 millió.
  2. Fordulópontok – idővonal 1920 → 1989: revízió, 1944–45 atrocitások (Délvidék, Felvidék), Beneš-dekrétumok
     (1945), lakosságcsere, falurombolási terv (Románia, 1988 – Bözödújfalu), rendszerváltás (kisebbségi pártok).
  3. A számok – országonkénti görbék; Tippelj!
  4. Miért fogy? – asszimiláció (vegyes házasság, iskola nyelve), kivándorlás, születésszám; „Honnan tudjuk?” – a
     népszámlálások kérdései különböznek (anyanyelv vs nemzetiség, egy vagy több válasz).
  5. Hol élnek? – a megyetérkép két állapota.
  6. Életutak – Esterházy János (1942. május 15.: egyedül szavazott a zsidók deportálását lehetővé tevő szlovák
     törvény ellen *(ellenőrizendő)*; † 1957, mírovi börtön) és Márton Áron (gyulafehérvári püspök; 1944. május 18.
     kolozsvári beszéde a zsidók deportálása ellen; 1949–1955 börtön *(ellenőrizendő)*) – parafrázis, forrással.
  7. Nemzetiségek Magyarországon – arányok; a németek kitelepítése (10); a roma népesség története (1893-as
     összeírás, 1944, mai helyzet); a nemzetiségi jogok (2011. évi CLXXIX. törvény, 13 nemzetiség).
  8. Együttműködés és konfliktus – kártyák (TortCards): példák mindkettőre, mindkét irányban (a kerettanterv
     feladata).
  9. Kapcsolatok 1990 után – intézmények és jogszabályok dátummal, értékelés és szám nélkül (pl. a nemzeti
     összetartozás napja, 2010. évi XLV. tv.; az egyszerűsített honosítás, 2010. évi XLIV. tv.); összefoglalás.
- **Adatok:**
  - Románia (magyar nemzetiségű): 1910 a későbbi román területen kb. 1,66 millió (anyanyelv) *(ellenőrizendő)*;
    1930: 1 425 507; 1992: 1 620 199 (egyes források 1 624 959); 2002: 1 431 807; 2011: 1 227 623; 2021: 1 002 151
    (anyanyelv szerint 1 038 806) – Wikipédia „Hungarians in Romania” (INS), a leckeügynök az INS-oldallal
    ellenőrzi.
  - Szlovákia: 1910 a mai területen 884 309 (30,2 %; más számolások 881 320, a Csehszlovákiához került egész
    területen 896 271 → „kb. 0,88 millió”); 1930: 571 952; 1991: 567 296; 2001: 520 528 *(ellenőrizendő)*; 2011:
    458 467 *(ellenőrizendő)*; 2021: 422 065 (a második nemzetiséggel 456 154) – Wikipédia „Hungarians in
    Slovakia” (ŠÚ SR).
  - Szerbia/Vajdaság: 1910 Vajdaság kb. 425 672 *(ellenőrizendő, Kocsis)*; 1921: 363 000; 1931: 376 000; 1991:
    343 942 (Vajdaság 339 491 *(ellenőrizendő)*); 2002: 293 299 (Vajdaság 290 207); 2011: 253 899 (251 136); 2022:
    184 442 (182 321) – Wikipédia „Hungarians in Serbia” (RZS).
  - Kárpátalja: 1910: 184 287 (más forrás 183 623); 1930 (csehszlovák): 116 441; 2001: 151 516 nemzetiség (158 700
    anyanyelv) – `hungarian-geography.hu/konyvtar/kiadv/etnika/ethnicMAP/…`.
  - Horvátország 2021: 10 315 *(ellenőrizendő)*; Szlovénia 2002 (az utolsó nemzetiségi népszámlálás): 6 243
    *(ellenőrizendő)*; Burgenland 2001: kb. 6 600 (köznapi nyelv) *(ellenőrizendő)*.
  - Magyarországi nemzetiségek (több válasz lehetséges), 2011 → 2022: roma 315 583 → 209 909; német 185 696 →
    142 551; szlovák 35 208 → 29 881; román 35 641 → 27 554; horvát 26 774 → 21 824; szerb 10 038 → 11 622 (a 2022-es
    adatok a roma kivételével a KSH-adatbázisban ellenőrizendők: nepszamlalas2022.ksh.hu).
  - Az 1941-es népszámlálás németjei és a kitelepítés: a 10-es leckével azonos számok.
  - Megyénkénti magyar arány (Románia 2021, Szlovákia 2021, Szerbia 2022, Ukrajna 2001) *(a leckeügynök gyűjti a
    statisztikai hivataloktól; csak a közölt számok, saját átszámolás nélkül)*.
  - 1944–45-ös délvidéki és felvidéki atrocitások áldozatai *(vitatott, ellenőrizendő; a lecke csak tartományt és
    forrást ad, ha a szakirodalom egyetért a nagyságrendben, különben „nem ismert pontosan”)*.
- **Modulok:** TortTerr (1920-as darabok a visszautaláshoz), FoldChoro (admin-1 egységek), FoldChart (görbék,
  `endLabels`), MatChart, TortTimeline, TortCards, TortSource, TtTipp.
- **Review-pontok:** **történész lektor**; a „hűség és helytállás” (kerettanterv) megfogalmazása tényekkel, nem
  jelzőkkel; a magyarellenes atrocitások és az 1941–44-es magyar megtorlások (Újvidék 1942) ugyanazzal a
  mércével; a népszámlálási kategóriák jelölése; a 9. lépés semlegessége.

### 15 · `15-nepesedes` – Miért lett nyolcszor annyi ember 200 év alatt? – népesedés és társadalom

- **Tanulási cél:** A **hagyományos (agrár)társadalomban** sok gyerek született és sokan meghaltak, a népesség lassan
  nőtt (járványok, éhínségek; **nagy pestisjárvány** 1347–1351). Az ipari forradalom, a közegészségügy (pl.
  **Semmelweis** kézmosása) és az élelmiszertermelés növekedése után a halálozás csökkent, a születés később – a
  kettő közötti időben **népességrobbanás** volt (**demográfiai átmenet**). Ma a fejlődő világban nő, a fejlett
  világban fogy a népesség. Magyarország népessége 1980-ban tetőzött; 1981 óta több a halálozás, mint a születés.
  A **korfa** a múlt nyomait őrzi (Ratkó-korszak). A **migráció** okai: taszító és vonzó tényezők. A **nők** szerepe
  az oktatás, a munka és a választójog terén megváltozott.
- **Kerettanterv:** „Letelepedés és élelemtermelés: növénytermesztés és állattenyésztés.” · „A népességnövekedés
  korlátai.” · „A hagyományos társadalom (hierarchia és család).” · „Az ipari forradalmak hatásai: népességrobbanás
  és városiasodás.” · „Népességnövekedés a fejlődő és népességfogyás a fejlett világban.” · „A migráció.” · „A
  modern/ipari társadalom (egyenjogúság és individualizmus).” · „A női szerepek változásának áttekintése a történelem
  során.” · Fogalmak: „háziasítás, nagy pestisjárvány, népességrobbanás, migráció, multikulturalizmus, terrorizmus,
  globalizáció.” · Személyek: „Semmelweis Ignác.” · „A népesedés nagy korszakainak és azok jellemzőinek
  felidézése.” · tevékenység: „A népesedéstörténet statisztikai adatainak értelmezése, csoportosítása és felhasználása
  állítások alátámasztására vagy cáfolására.”
- **Tévhitek:** „A népesség mindig egyenletesen nőtt.” „Régen azért halt meg sok ember, mert rövidebb volt az
  élet – 40 évesen mindenki öreg volt.” (A csecsemőhalandóság húzta le az átlagot.) „A népességrobbanás azért van,
  mert több gyerek születik.” (Azért, mert kevesebb hal meg.) „Magyarország népessége a kivándorlás miatt fogy.”
  (Főleg a természetes fogyás miatt.) „A korfa csak a jelent mutatja.”
- **Kulcsvizuál:** három adatvizuál:
  1. a világ népessége Kr. e. 10 000 → 2022 (FoldChart, lin. és log. kapcsolóval), a milliárdos mérföldkövekkel;
  2. a **demográfiai átmenet** (modell: születési és halálozási ráta görbéje, a köztük lévő terület kitöltve) és
     mellette a valódi magyar adat (FOLD_KORFA `cbr`, `cdr` 1950-től) – a 1981-es metszéspont kirajzolódik;
  3. a **magyar korfa** 1950 → 2020 (FoldChart `pyramid` + `pyrRows` 'cohort' mód) – a Ratkó-nemzedék „púpja” felfelé
     vándorol, és 20–25 évvel később visszhangja születik.
  Semmelweis: két oszloppár (I. és II. klinika, 1841–46 és 1848) – a kézmosás bevezetése után a különbség eltűnik.
- **Kipróbálom:** évcsúszka a korfán (1950–2020, opcionálisan 2050-ig „előrejelzés” bélyeggel); rákattintva egy
  korcsoportra kiírja: „ők ebben az évtizedben születtek”. A Semmelweis-lépésben kapcsoló: „klórmeszes kézmosás
  be/ki” *(a görbe a valódi adatsor, nem szimuláció)*.
- **Tippelj!** 2. lépés: „Mennyi idő alatt nőtt a világ népessége 7-ről 8 milliárdra? kb. 11 év / kb. 50 év / kb.
  100 év”. 4. lépés: „Mekkora volt a gyermekágyi láz halálozása Semmelweis kórtermében (I. klinika) 1841–46-ban?
  kb. 1 % / kb. 4 % / kb. 10 %”.
- **Lépések:**
  1. Letelepedés – háziasítás és földművelés (kb. 10 000 éve), a népességnövekedés korlátai; a pestis 1347–51
     (európai veszteség tartománnyal).
  2. Milliárdos mérföldkövek – Tippelj!
  3. A hagyományos és a modern társadalom – család, hierarchia, egyenjogúság (két kártya).
  4. Semmelweis – oszloppárok; Tippelj!; „Honnan tudjuk?”: Semmelweis saját kórházi statisztikája (1861, közkincs).
  5. Demográfiai átmenet – modell + magyar adat.
  6. A magyar korfa – 1950 → 2020; a Ratkó-korszak (1953–56) és visszhangja.
  7. 1981 – fordulópont: több halálozás, mint születés; a népesség csúcsa (1980) és 2022.
  8. Két világ – Nigéria és Japán korfája (FOLD_KORFA) egymás mellett; migráció: taszító és vonzó tényezők (modell,
     értékelés nélkül); városiasodás.
  9. Női szerepek – iskolázottság, munka, választójog (a nők választójoga Magyarországon 1920-ban korlátozottan,
     1945-ben általánosan *(ellenőrizendő)*); összefoglalás.
- **Adatok:**
  - Világnépesség: 1 milliárd kb. 1804, 2 milliárd 1927, 3 milliárd 1960, 4 milliárd 1974, 5 milliárd 1987, 6 milliárd
    1999, 7 milliárd 2011, 8 milliárd 2022. november 15. (ENSZ – az 1804 és az 1927 kb.) – `un.org/en/global-issues/
    population`; ugyanaz, mint a `foldrajz-9-10/10-nepesseg` adata (a két lecke számai egyezzenek).
  - Világnépesség Kr. e. 10 000 és Kr. u. 1 körül *(becslés, ellenőrizendő: HYDE / ENSZ, tartománnyal)*; a pestis
    európai vesztesége 30–50 % *(becslés)*.
  - Semmelweis (saját adatai): 1841–46 I. klinika 1 989 halott / 20 042 szülés = 9,92 %; II. klinika 691 / 17 791 =
    **3,88 %** (a sokszor idézett 3,38 % elírás); a klórmeszes kézmosás 1847 május közepétől (a nap nem ismert);
    1847 I. klinika 5,0 %; 1848 I. klinika 45 / 3 556 = 1,27 %, II. klinika kb. 1,33 %. Született 1818. július 1.,
    Buda (Tabán), meghalt 1865. augusztus 13., Bécs (Döbling) – PMC3807776, Wikipédia „Historical mortality rates of
    puerperal fever”.
  - Születések: 1953: 206 926; 1954: **223 347** (az 1945 utáni csúcs – nem a valaha volt legnagyobb; az 1920-as
    évek elején több *(ellenőrizendő)*); 1955: 210 430; 1956: 192 810 – Statisztikai Szemle 1958/7. A Ratkó-féle
    rendelet 1953 (1004/1953), 1954-től enyhítés, 1956 júniusától gyakorlatilag kérésre engedélyezett abortusz – KSH.
  - Népesség: csúcs 10 709 463 (az 1980-as népszámlálás, 1980. január 1.); 2022: 9 603 634 (népszámlálás) – KSH.
    A mai területen (ezer fő): 1910: 7 612; 1920: 7 987; 1930: 8 685; 1941: 9 316; 1949: 9 205 (KSH STADAT).
  - Természetes fogyás 1981 óta *(a leckeügynök a FOLD_KORFA `births`/`deaths` sorából számolja, és a KSH-val
    egyezteti)*.
  - Korfa, mutatók: FOLD_KORFA (ENSZ WPP 2024, CC BY 3.0 IGO) – `shared/foldrajz/korfa-wpp2024.js`, spec
    `dataset`.
- **Modulok:** FoldChart (log, `pyramid`, `pyrRows`, `cross`), BioPlot (átmenet-modell, ha kell), MatChart,
  TortTimeline, TtTipp.
- **Review-pontok:** a migráció-lépés semlegessége (definíciók és modell, mai politikai vita nélkül; a kerettanterv
  „multikulturalizmus, terrorizmus” fogalmai csak definícióként); egyezés a `foldrajz-9-10/10-nepesseg` számaival.

### 16 · `16-demokracia` – Ki dönt, és ki ellenőrzi? – a demokratikus állam és a választás

- **Tanulási cél:** A demokrácia gyökere az **athéni népgyűlés** (Kr. e. 5. század, Periklész) – a polgárok
  közvetlenül döntöttek, de a lakosság kis része volt polgár. A modern demokrácia **képviseleti**: a
  **parlamentáris rendszerben** (Nagy-Britannia) a parlament többsége adja a kormányt; az **elnöki rendszerben**
  (USA, 1776, alkotmány 1787, George Washington) a választók külön választják az elnököt. A **hatalmi ágak**
  (törvényhozó, végrehajtó, bírói) egymást ellenőrzik. Magyarország **Alaptörvénye** (2012) szerint az
  Országgyűlés 199 tagú: **106 egyéni** és **93 listás** mandátum; a kormányt a miniszterelnök vezeti, akit az
  Országgyűlés választ; az Alkotmánybíróság, a bíróságok, a köztársasági elnök és más intézmények ellenőrző
  szerepet töltenek be. A **választási rendszer** vegyes: ugyanazok a szavazatok más szabállyal más parlamentet
  adnak.
- **Kerettanterv:** „Az athéni demokrácia működése.” · „A parlamentáris rendszer működése Nagy-Britanniában.” · „Az
  elnöki rendszer működése az Amerikai Egyesült Államokban.” · „Az Alaptörvény.” · „Az Országgyűlés, a kormány és
  az igazságszolgáltatás.” · „Az országgyűlési és önkormányzati választási rendszer.” · Fogalmak: „népgyűlés, hatalmi
  ágak, alkotmány, elnök, általános választójog.” · Személyek: „Periklész, George Washington.” · Kronológia: „Kr. e.
  5. sz. az athéni demokrácia fénykora, 1776 az amerikai Függetlenségi nyilatkozat, 2012 Magyarország
  Alaptörvénye.” · „Demokratikus döntéshozatal ábrázolása egy folyamatábrán.” · „A brit parlamentáris és az amerikai
  elnöki rendszer összehasonlítása.” · „Áttekintő ábra értelmezése a magyarországi államszervezetről és a választási
  rendszerről.” · tevékenység: „Csoportos szerepjáték demokratikus döntéshozatalról (pl. az athéni demokráciában).”
- **Tévhitek:** „Demokrácia = a többség azt tesz, amit akar.” (Alkotmány, jogok, ellenőrzés.) „Athénban mindenki
  szavazhatott.” „A köztársasági elnök vezeti a kormányt.” „A mandátumok aránya mindig egyenlő a szavazatok
  arányával.” „Az egyéni körzetben a győztesre adott szavazat nem számít a listán.” (A győztes többlete is
  töredékszavazat 2014 óta.)
- **Kulcsvizuál:** a **TortState** áttekintő ábra: választópolgárok → Országgyűlés → miniszterelnök → kormány; az
  Országgyűlés választja a köztársasági elnököt, az Alkotmánybíróság tagjait, a Kúria elnökét, a legfőbb ügyészt, az
  alapvető jogok biztosát; a bíróságok függetlenek. Minden nyíl címkézett („választ”, „ellenőriz”, „kinevez”). Három
  változat egymás mellett (TortState `layout` váltással): Athén, Egyesült Királyság, USA, Magyarország. A
  választás-lépésekben a **TortParl** kalkulátor: 8 *kitalált* egyéni körzet + országos lista; **kitalált pártok**
  („A párt”, „B párt”, „C párt”, „D párt”), egy színárnyalat négy tónusa + mintázat (pötty, csík, sraffozás, teli).
- **Kipróbálom:**
  - a kalkulátor csúszkái (pártonkénti országos szavazatarány, körzetenkénti eltolás) → egyéni győztesek, a vesztes
    és a győztes többlet-szavazatai (**töredékszavazat**), az **5 %-os küszöb**, **D'Hondt**-elosztás a listán, a
    199-es patkó; a ½ (100) és a ⅔ (133) vonal;
  - kapcsoló „tisztán arányos / tisztán egyéni / vegyes”;
  - a TortState-en kattintás egy intézményre: ki választja, mennyi időre, kit ellenőriz.
- **Tippelj!** 6. lépés: „Lehet-e egy pártnak a mandátumok több mint felét megszerezni a szavazatok kevesebb mint
  felével? igen / nem / csak ha csalás van” (a kalkulátor megmutatja: igen, a vegyes rendszer egyéni része miatt).
- **Lépések:**
  1. Athén – népgyűlés (ekklészia), sorsolás, Periklész; polgárok aránya a lakosságban (becslés): ki maradt ki?
  2. Képviselet – miért nem tud 8 millió választó népgyűlést tartani? (A Lesson-motor egyszerű számolása: 1 perc
     felszólalás mindenkinek = hány év?)
  3. Parlamentáris és elnöki – Egyesült Királyság és USA TortState-ábrán; 1776, 1787; az amerikai elektori
     kollégium egy mondatban.
  4. Hatalmi ágak – Montesquieu (1748, közkincs) – a három ág és az ellenőrzések.
  5. Magyarország Alaptörvénye – az intézményséma; egy közkincs idézet: „Magyarország független, demokratikus
     jogállam.” (B) cikk (1).
  6. Az országgyűlési választás – 106 + 93, egyéni körzet, lista, küszöb, töredékszavazat; Tippelj!
  7. A kalkulátor – szabad kipróbálás; a ⅔ jelentése (sarkalatos törvények, az Alaptörvény módosítása).
  8. Önkormányzat – polgármester és képviselő-testület, 5 évre; Budapest kétszintű rendszere.
  9. Összefoglalás – folyamatábra: egy törvény útja (javaslat → vita → szavazás → köztársasági elnöki aláírás /
     Alkotmánybíróság → kihirdetés).
- **Adatok:**
  - Országgyűlés 2014 óta: 199 képviselő = 106 egyéni választókerületi + 93 listás (pártlista vagy nemzetiségi lista)
    – parlament.hu „Election of the Members of Parliament”; a választásokról szóló 2011. évi CCIII. törvény (küszöb:
    5 %, két párt közös listájánál 10 %, három vagy több pártnál 15 %; töredékszavazat; D'Hondt) *(a számok a
    törvényszövegből ellenőrizendők)*.
  - Alaptörvény: elfogadva 2011. április 18., aláírva április 25., hatályos 2012. január 1. (szokásos adat,
    ellenőrizve).
  - Köztársasági elnök: az Országgyűlés választja 5 évre; Alkotmánybíróság: 15 tag, 12 évre; miniszterelnök: az
    Országgyűlés választja; önkormányzati ciklus 5 év (2014 óta) *(ellenőrizendők az Alaptörvény szövegéből)*.
  - Athén: polgárok kb. 30–60 ezer, a teljes lakosság kb. 250–300 ezer *(becslés, vitatott)*; Periklész kb. Kr. e.
    495–429.
  - Függetlenségi nyilatkozat 1776. július 4.; alkotmány 1787; Washington elnök 1789–1797; elektori kollégium: 538
    *(ellenőrizendő)*.
  - Montesquieu: *A törvények szelleméről* (1748, † 1755 – közkincs; fordítás saját vagy közkincs).
  - A kalkulátor összes szavazata és körzete *(kitalált példa)* – a `.md` így jelöli.
- **Modulok:** **TortParl** (ref.: patkó, mandátumszámító: egyéni győztes, töredék, küszöb, D'Hondt, ½ és ⅔ vonal),
  **TortState** (ref.: intézményséma, címkézett nyilak, kapcsolók dátummal, elrendezések), TortCards, TtTipp.
- **Review-pontok:** **semlegesség**: kitalált pártok, nincs mai pártszín; a választási törvény részletei (küszöbök,
  töredékszavazat, nemzetiségi kedvezményes mandátum) a törvényszövegből; az intézményi jogkörök az Alaptörvényből;
  a kalkulátor számolása egy kézzel ellenőrzött példán (a `.md` megjegyzésében).

### 17 · `17-europai-unio` – Hogyan lett hat országból huszonhét? – az Európai Unió és Közép-Európa

- **Tanulási cél:** A második világháború után a nyugat-európai államok a gazdasági **integrációval** akarták a
  háborút lehetetlenné tenni: szén- és acélközösség (1951), **római szerződés** (1957, 6 állam). A közösség hullámokban
  bővült, a **maastrichti szerződés** (1992) után **Európai Unió** lett, közös piaccal, **euróval** (1999/2002),
  szabad mozgással. **Magyarország 2004. május 1-jén** csatlakozott, a **visegrádi együttműködés** (1991)
  tagjaként – a név egy 1335-ös királytalálkozóra utal. **Közép-Európa** sajátossága: szárazföldi helyzet,
  birodalmi függés, nemzeti sokszínűség. Az integrációnak eredményei és gondjai is vannak (pl. a brit kilépés,
  2020).
- **Kerettanterv:** „Az Európai Unió születése és bővülése.” · „Az európai integráció céljai, eredményei és gondjai.”
  · „Magyarország európai uniós tagsága.” · „A régió sajátosságai (jellemzően kontinentális helyzet, birodalmi
  függés és nemzeti sokszínűség).” · „A visegrádi együttműködés.” · Fogalmak: „integráció, euró, Európai Unió,
  visegrádi együttműködés” · Kronológia: „1957 a római szerződés, 1992 a maastrichti szerződés, 2004 Magyarország
  belép az Európai Unióba.” · Topográfia: „Brüsszel, Lengyelország, Csehország” · „A közép-európai régió
  középkori, újkori és mai térképeinek összehasonlítása.” · tevékenység: „Információk gyűjtése a visegrádi
  együttműködés előzményeiről és jelenlegi tartalmáról.” · (14.) „Magyarország mint szuverén európai hatalom a
  középkorban.”
- **Tévhitek:** „Az EU egy ország.” „Minden EU-tagnak euró a pénze.” „Az EU mindig 27 tagú volt.” „Európa = EU.”
  (Svájc, Norvégia…) „A visegrádi együttműködés ősi szövetség.” (1991; a név utalás.)
- **Kulcsvizuál:** Európa-térkép (FoldChoro a FOLD_ORSZAGOK mai országain – ez **mai** korszak, a mai határ itt
  helyénvaló; a nyolc évszámos bővülés **gombnyomásra** vagy csúszkán: 1957 → 1973 → 1981 → 1986 → 1995 → 2004 →
  2007 → 2013 → 2020). Minden bővülésnél a taglétszám-számláló és a népesség (FOLD_WDI). Az euróövezet külön
  rétegként (sraffozás). A Közép-Európa-lépésben a **visegrádi** térkép: 1335 (három király, vázlatos birodalom-
  foltok, a 5–6. évfolyam TortTerr-elve szerint) → 1991 (három állam) → 1993 (négy).
- **Kipróbálom:** bővülés-csúszka; országra kattintva csatlakozás éve, euró (igen/nem, év); az intézmény-lépésben
  TortState-kicsiben: Bizottság, Parlament, Tanács, Bíróság – ki választja, ki dönt.
- **Tippelj!** 2. lépés: „Melyik évben csatlakozott a legtöbb ország egyszerre? 1973 / 1995 / 2004”.
- **Lépések:**
  1. Miért? – a háborúk után: szén- és acélközösség (1951), római szerződés (1957. március 25.).
  2. Bővülések – csúszka; Tippelj!
  3. Maastricht (1992. február 7.) – EU, uniós polgárság, a négy szabadság (áru, szolgáltatás, tőke, munkaerő).
  4. Euró – 1999 (számla), 2002 (készpénz); ma 21 tag (Bulgária 2026. január 1.); Magyarország pénze a forint.
  5. Magyarország útja – 1991 társulás *(ellenőrizendő)*, 1994 jelentkezés *(ellenőrizendő)*, 2003 népszavazás
     *(ellenőrizendő)*, 2004. május 1.; Schengen (2007. december 21. *(ellenőrizendő)*).
  6. Hogyan működik? – intézmények (TortState).
  7. Közép-Európa – a régió sajátosságai (szárazföld, birodalmak, nemzetek) három térképen: 1335, 1914 (Monarchia),
     ma; Visegrád.
  8. Eredmények és gondok – kereskedelem, szabad mozgás, kohéziós támogatás; gondok: válságok, a brit kilépés
     (2020. január 31.) – adatokkal és tényként, a mai magyar–uniós viták értékelése nélkül.
  9. Összefoglalás – hat országtól huszonhétig; „Honnan tudjuk?” – az uniós szerződések hivatalos szövege
     (eur-lex.europa.eu), a népszámlálás és az Eurostat.
- **Adatok:**
  - Római szerződés 1957. március 25.; bővülések: 1973. január 1. (Egyesült Királyság, Írország, Dánia) → 9; 1981
    (Görögország) → 10; 1986 (Spanyolország, Portugália) → 12; 1995 (Ausztria, Finnország, Svédország) → 15; 2004.
    május 1. (10 állam) → 25; 2007 (Bulgária, Románia) → 27; 2013 (Horvátország) → 28; 2020. január 31. (az
    Egyesült Királyság kilép) → 27 – szokásos, ellenőrizve.
  - Maastricht 1992. február 7. (hatályos 1993. november 1. *(ellenőrizendő)*).
  - Visegrád: 1991. február 15., 3 állam; 1993. január 1-jétől 4; a visegrádi királytalálkozó 1335 (Károly Róbert,
    János cseh és Kázmér lengyel király) *(ellenőrizendő)*.
  - Euró: 1999. január 1. számlapénz (11 állam), 2002. január 1. készpénz (12 állam, Görögország 2001-től);
    Bulgária 2026. január 1., a 21. tag – ECB sajtóközlemény 2026-01-01.
  - Magyar uniós népszavazás 2003. április 12. *(ellenőrizendő: igen-arány, részvétel)*.
  - Európai Parlament: 720 képviselő (2024), Magyarország 21 *(ellenőrizendő)*.
  - Tagállamok népessége: FOLD_WDI (Világbank, CC BY 4.0).
- **Modulok:** FoldChoro (FOLD_ORSZAGOK, `cat`), TortTerr (1335 / 1914 vázlat), TortTimeline, TortState (kicsi),
  FoldChart, TtTipp.
- **Review-pontok:** semlegesség (0. döntés, 9.): az uniós intézmények és a magyar tagság tényként, értékelés
  nélkül; az 1335-ös térkép vázlatos; a „Közép-Európát sikeresen egyesítő birodalom” (14., kerettanterv) mint
  értékelő állítás a tanári megjegyzésben kérdésként.

---
## 4. Közös modulok

### 4.1 Mi jön változatlanul (bájtra azonosan, szerződés 16.)

Az md5 a `/* ── MODUL:` sor elejétől a `MODUL VÉGE` sor végéig (az utolsó újsor nélkül, UTF-8) számolva,
2026-11-25, a `leckek/*/*.html` összes példányán. Bármelyik azonos md5-ű leckéből másolható; az „ajánlott forrás” a
legfrissebb példány. **Két eltérő változat nem használható:** TortSource `50d3c6fd…` (`tortenelem-5-6/03-gorogok`) és
`134cb7b3…` (`tortenelem-5-6/18-gozgep`), TortCards `c2a85a56…` (`tortenelem-5-6/18-gozgep`).

| Modul | Ajánlott forrás (blokk kezdősora) | md5 | példány | Lecke ebben a sorozatban | Mire kell itt |
|---|---|---|---|---|---|
| **TtTipp** | `digitalis-kultura-5-6/08-vonalkoveto` (250) | `fa839199626ca8aa31f3693a24150d81` | 34 | mind, kivéve 08 (ott csak a `stamp`) | „Tippelj!”, bélyegek |
| **TortMap** v1.1 (+ `shared/tort/proj.js` és a `map-*.js` adatok) | `digitalis-kultura-5-6/05-csomagok` (1326) | `05bd08a1c2d32bdd050cba4c4fdbc2e2` | 24 | 01, 02, 03, 04, 05, 07, 08, 09, 10, 11, 13, 14, 17 | alaptérkép, kamera, címkézés, nyilak; a TortTerr és a TortCity erre épül |
| **TortTimeline** | `digitalis-kultura-5-6/05-csomagok` (1780) | `9c5cebae791ce43f3d93b5f2785e6dfd` | 24 | 01, 02, 04, 05, 06, 07, 08, 09, 10, 11, 13, 14, 15, 17 | idővonal, kártyák (csökkenő sorrend!), `mini` |
| **TortSource** | `tortenelem-5-6/20-szabadsagharc` (1447) – vagy bármely `a59b1074…` | `a59b107413f4949197b9d51f1c5a174e` | 33 | mind | forráskártya, „Honnan tudjuk?”, rétegkeretek |
| **TortCards** | `digitalis-kultura-5-6/11-dokumentum` (376) | `2c411077c00d1ba0d984102651b64c44` | 29 | 01, 02, 05, 12, 14, 16 | rendezés, párosítás |
| **TortScene** | `magyar-5-6/12-alfold` (557) | `2ffe3e9ed4362ed08e69c297fc91213f` | 12 | 03 | lövészárok-metszet (nézetek, rétegek, hotspotok) |
| **TortGlobe** v1.1 | `termeszettudomany-5-6/17-idojaras` (920) | `35472d60b468679e013140e7db43d6c6` | 14 | 07, 09 | csendes-óceáni betét, szuperhatalmak a gömbön |
| **FoldChoro** v1.1 | `termeszettudomany-5-6/07-foldgomb` (1121) | `bbea5aa7105f6fc78d8a991d74b57014` | 6 | 01, 14, 17 | gyarmatbirodalmak (`cat`), megyetérkép, EU-bővülés |
| **FoldChart** | `termeszettudomany-5-6/16-folyo` (1411) | `92a03151ff1c93037ec9a611e70c9e91` | 14 | 02, 03, 06, 07, 09, 12, 13, 14, 15, 17 | log-tengely (06), korfa (15), sávok (tartományok), végcímkék |
| **MatChart** v1.1 | `termeszettudomany-5-6/14-energia` (928) | `02e3710065229ffbf2fd7f1ac155933a` | 9 | 01, 02, 04, 06, 08, 11, 12, 14, 15 | oszlop, kör (anyanyelv), pontrács (100-as rács) |
| **BioPlot** | `digitalis-kultura-5-6/08-vonalkoveto` (2218) | `c38b534d3ea4c947ce3ed4fe9dad5351` | 26 | 15 (opcionális) | a demográfiai átmenet modellgörbéje |
| (TortBattle) | `tortenelem-5-6/20-szabadsagharc` (1757) | `4e95050f0cd4f4fc7fc13034ceb024b3` | 5 | – (csak a `SIDES` színkonstansok: indigó `#3b4590`, szilva `#7d3a66` – értékként átvéve, a blokk nélkül) | – |

Függőségek és buktatók (a korábbi sorozatok ismert hibái, pl. `pilot/foldrajz-9-10/METRIKAK.md`; itt is érvényesek):
- **TortSource.card** idővonal nélküli leckében a `window.TortTimeline = window.TortTimeline || {Y: null}` csonkot
  kéri – a 12 és a 16 ellenőrizze (a többi leckében van idővonal).
- **TortTimeline.cards** elemei csökkenő sorrendben (sor szerint) adandók.
- **FoldChoro** jelmagyarázata és kártyája a pillanatnyi `globalAlpha`-val szoroz – előtte `al(1)`.
- **Equal Earth** (`TortProj.equalEarth`) `lon0: 0`-val (01, 09 világtérkép), a bbox a középmeridiánhoz igazodjon.
- A jelenet-állapotot `init()`-ben is inicializáld, ne csak `enter()`-ben; modulblokk másolásánál nézd meg, hol ér
  véget a blokk (`MODUL VÉGE` sor).

### 4.2 Új modulok és adatfájlok

A szerződés 16. fejezete szerint: a referencialeckében, külön MODUL-blokkban, `Tort…` névtérrel. Blokkhatár:
`/* ── MODUL: <név> (<Névtér>) · forrás: tortenelem-7-8/NN-slug, <dátum> ── */` … `/* ── MODUL VÉGE: <név> ── */`.
Csak a Lesson motorra (`L.ctx`, `L.tx`, `L.pill`, `L.measure`, `L.pointer`, `L.st`, `Lesson.U`, `Lesson.FONTS`), a
TortProj-ra és – ahol jelölve – a TortMap-re épülnek; minden felirat `{s, k}` pár, és **csak** `L.tx`/`L.pill` írja
ki. Alfa: a modul az `o.a`-t a hívó alfájával szorozva **állítja**, a vonalstílust visszaállítja. Minimális
betűméret a vásznon 22 px. Szöveghez igazodó doboz (`L.measure`), nincs fix szélességű címke.

| Modul / adat | Referencia | Átvevők | Lényeg |
|---|---|---|---|
| `shared/tort/map-torthatar.js` (`TORT_HATAR`) + `shared/tort/map-europa.js` (`TORT_MAP_EUROPA`) | **0. köteg** (előkészítő lépés, `tools/build_tortmap.py`) | 01, 03, 04, 05, 07, 08, 09, 10, 13, 14, 17 | történeti egységek topologikus formában; Európa-alaptérkép |
| **TortTerr** – történeti területek, hovatartozás dátum szerint, frontok | `07-masodik-vilaghaboru` | 01, 03, 04, 05, 08, 09, 10, 13, 14, 17 | egységcsoportok kitöltése és egyesített körvonala; dátum → ellenőrző hatalom; kiúsztatás; front-interpoláció; találat |
| **TortCity** – vázlatos Budapest | `02-dualizmus` | 07, 08, 11 | Duna, szigetek, hidak (épült / lerombolva / újjáépült), utak, városhatár év szerint, helyszínek |
| **TortParl** – patkó és mandátumszámító | `16-demokracia` | 05, 10, 13 | patkó, egyéni győztes, töredékszavazat, küszöb, D'Hondt, ½ és ⅔ vonal, semleges paletta + mintázat |
| **TortState** – intézményséma | `16-demokracia` | 05, 10, 12, 13, 17 | csomópontok, címkézett nyilak (választ / ellenőriz / kinevez / irányít), kapcsolók dátummal, elrendezésváltás |

#### Adat: `map-torthatar.js` és `map-europa.js` · 0. köteg (előkészítő lépés)

**Ki készíti:** a koordinátor egy külön **adat-ügynököt** indít a gyártás előtt (nem leckeügynök). Ő az egyetlen,
aki a `shared/tort/` és a `tools/` alá ír ebben a sorozatban: új szkript `tools/build_tortmap.py` (stdlib, a
`tools/build_geodata.py` `edge_union`, `pack_rings`, `topo_simplify`, `write_js`, `meta` függvényeit importálja vagy
másolja), és két új fájl. Bemenet: a már letöltött Natural Earth fájlok (`sources/foldrajz/naturalearth/`
`ne_10m_admin_1_states_provinces.geojson`, `ne_50m_admin_0_countries.geojson`; a `sources/naturalearth/` 1:50m
szárazföld, folyó, tó – a `manifest.json` URL-lel és SHA-256-tal). A forrásmappában szkript nem fut; Python `-I`.
Licenc: **Natural Earth – közkincs** („Made with Natural Earth”). A kézi vágóvonalak töréspontjai saját munka,
forrásként a szerződés- és jogszabályszöveg határleírása (közkincs) és legalább két mainstream atlasz (csak
egybevetésre) – a szkript kommentjében tételesen. Becsült munka: 1,5–3 óra ügynöki idő.

**`map-europa.js` (`TORT_MAP_EUROPA`)** – a meglévő `map-*.js` formátumában (`shared/tort/README.md`): 25° Ny – 60° K,
33–72° É, NE 1:50m szárazföld, tavak, folyók (a fő folyók magyar névvel a `build_mapdata.py` táblájából), q = 100.
A `map-mediterran.js` 56° É-nál vág – Skandinávia, Leningrád, a Baltikum, Moszkva környéke kell a 03, 07, 09, 17
leckéhez.

**`map-torthatar.js` (`TORT_HATAR`)** – topologikus formátum (közös ívek, hogy egy csoport körvonala futás közben
számolható legyen):

```
{ id: 'torthatar', q: 1000 (Kárpát) / ívenként, src, ver, lic: 'Natural Earth – közkincs; kézi vágás: saját',
  arcs:   [delta-kódolt vonal, …],                    // közös ívek; egy ív két egységet választ el
  units:  [{id: 'RO-HR', n: 'Hargita', set: 'karpat' | 'europa', c: [lon, lat] (belső címkepont),
            r: [[ívindex (±: irány), …], …]}, …],     // építőelemek: mai admin-1/admin-0 egység vagy kézzel vágott darab
  groups: { 'mo1914': [unit-id, …], 'hsz1914': […], 'mo1920': […], 'felvidek': […], 'karpatalja': […],
            'erdely': […], 'delvidek': […], 'orvidek': […], 'bd1': […], 'karpatalja1939': […], 'bd2': […],
            'delvidek1941': […], 'pozsonyi-hidfo1947': […],
            'zonak1944': {'I-II': […], 'III': […], 'IV': […], 'V-VI': […]},
            'eu1914': {'DE': […], 'AH-AT': […], 'AH-HU': […], 'RU': […], 'IT': […], 'FR': […], …},
            'eu1923': {…}, 'eu1938': {…}, 'eu1942': {…}, 'eu1949': {'NSZK': […], 'NDK': […], 'Berlin-Ny': […],
            'Berlin-K': […], …}, 'szu1991': {15 állam: […]} },
  points: {fiume: [lon, lat], …},                      // túl kicsi egységek pontként
  notes:  {groupId: 'vázlatos: …, eltérés: …', …} }    // minden csoporthoz rövid pontossági megjegyzés
```

Építés (a szkript kommentje és a `notes` mező rögzíti):
- **Kárpát-medence, 1:10m admin-1** (ROU 42 megye, SVK 8 kerület, UKR 25 terület, AUT 9 tartomány, HUN 43, SRB 25
  körzet, HRV 21 megye, SVN 193 község) – a 1914-es királyság, Horvát-Szlavónország, az 1920-as darabok és a
  maradék ország **mai egységek uniója**:
  - *Erdély és Partium* = 16 román megye (Alba, Arad, Bihor, Bistrița-Năsăud, Brașov, Caraș-Severin, Cluj, Covasna,
    Harghita, Hunedoara, Maramureș, Mureș, Sălaj, Satu Mare, Sibiu, Timiș);
  - *Felvidék* = Szlovákia; *Kárpátalja* = Zakarpattia; *Őrvidék* = Burgenland; *Muraköz* = Međimurska;
    *Muravidék* = a Pomurska régió községei; *Bácska, Bánát nyugati része* = a vajdasági körzetek;
    *Baranyai háromszög* = Osječko-baranjska megye **Drávától északi része** (kézi vágás a NE Dráva-vonalán);
  - *Horvát-Szlavónország* = Horvátország a dalmát megyék (Zadarska, Šibensko-kninska, Splitsko-dalmatinska,
    Dubrovačko-neretvanska), az Isztria és a kvarneri szigetek nélkül, + a Szerémség (Sremski körzet) – vázlatos;
  - *mo1920* = a mai Magyarország (eltérés: a soproni népszavazás 1921, az 1922–24-es kiigazítások, a pozsonyi
    hídfő három faluja 1947 – a `notes`-ban);
  - **kézi vágóvonal** csak ott, ahol a határ mai egységen fut át: az első bécsi döntés vonala (1938), a
    kelet-szlovákiai sáv (1939. április), a második bécsi döntés vonala (1940), a Duna Újvidéknél (Bácska 1941
    déli széle), a 1920-ban Lengyelországhoz került árvai–szepesi falvak (elhanyagolható, 589 km² – a `notes`
    jelzi). Egy vágóvonal legfeljebb kb. 40 töréspont, helységnevekkel kommentezve („Kassa ↑ magyar, Nyitra ↓”).
  - *zonak1944*: a deportálási zónák mai egységekből és a fenti darabokból, **vázlatosan** (a csendőrkerületek
    pontos határa nem rekonstruálható mai egységekből) – a `notes`: „a zónák fekvését mutatja, határuk vázlatos;
    Braham alapján, történész ellenőrizze”.
- **Európa, 1:10m admin-1 → 1:50m tűrésre egyszerűsítve** (a varratok ugyanabból a topológiából, ezért nincs rés):
  az államok a mai egységek uniói, kézi vágás a fő eltéréseknél: a német–lengyel határ (1914, 1923, 1945), a
  lengyel–szovjet (rigai határ 1921, Molotov–Ribbentrop-vonal 1939), Romániá 1914-es határa (Besszarábia,
  Bukovina, Erdély nélkül), Olaszország 1914 (Dél-Tirol, Trieszt, Isztria nélkül), Elzász-Lotaringia (francia
  départements – mai egység), a francia megszállási vonal 1940 (kézi), Jugoszlávia felosztása 1941 (vázlatos),
  Berlin két része (kézi, a mai Berlin egységen belül). Az 1991-es 15 szovjet utódállam = mai országok.
- **Ellenőrzés a szkriptben:** minden csoport területét kiszámolja (gömbi felszín), és a `notes`-ba írja a hivatalos
  értéktől való eltérést (pl. „mo1914: 325 411 km² hivatalos, a vázlat 3 % eltérés”) – ez csak QA-adat, **a leckék
  nem jelenítik meg**. 10 %-nál nagyobb eltérés hibának számít, javítandó. Vizuális egybevetés a HistoGIS-szel
  és a CShapes 2.0-val képernyőképen (az ő adatuk nem kerül a fájlba).
- **Méret:** a Kárpát-rész kb. 120–180 KB, az Európa-rész kb. 150–250 KB *(becslés)*; ha a kettő együtt 400 KB
  fölé menne, két fájl: `map-torthatar.js` (Kárpát) és `map-torthatar-europa.js`.
- A `shared/tort/README.md` táblázata két új sorral bővül (fájl, globális név, kivágat, forrás, méret).

#### TortTerr – történeti területek · referencia: `07-masodik-vilaghaboru`

A TortMap-re épül (a nézet a `map.frame()`-ből jön), a `TORT_HATAR` adatból dolgozik.

```
const T = TortTerr.create(L, TORT_HATAR, {map})        // map: TortMap példány; egyszer, init()-ben
T.group(id) → {ids: [unit-id…], c: [lon, lat]}          // pl. 'mo1914' vagy 'eu1942.DE'; c: a legnagyobb egység címkepontja
T.fill(ctx, items, o)                                   // items = [{g: csoport | [unit-id…], c: '#rrggbb', a, hatch: true,
                                                        //   dx, dy (px eltolás – kiúsztatás)}]; o = {land: true (szárazföldre vág), blur}
T.outline(ctx, g, o)                                    // EGYESÍTETT körvonal (a csoporton belül kétszer használt ívek kimaradnak)
                                                        //   o = {c, w, dash, a, halo}
T.control(rules, d) → {unitId: hatalom}                 // rules = [{g, who, from: dátumkulcs-érték (a), to}] – a dátumok
                                                        //   L.dat(k).a tört évei a .md-ből; d: tört év
T.blend(rules, d, fade) → [{g, who, t}]                 // váltás áttűnéssel (fade: évben, pl. 0,05 ≈ 18 nap)
T.explode(g, toward, u) → {dx, dy}                      // kiúsztatás: a csoport u (0..1) arányban a toward [lon, lat] felé
T.label(L, g, t, o)                                     // pill-címke a csoport címkepontján (t = {s, k}); o = {sub: {s, k}, a}
T.hit(px, py, gs) → g | null                            // melyik csoportra kattintott (a gs listából)
T.front(keys, d) → [[lon, lat]…]                        // keys = [{a: tört év, pts: [[lon, lat]…]}] – minden kulcskockát N pontra
                                                        //   mintavételez ívhossz szerint, d szerint lineárisan interpolál
T.drawFront(ctx, pts, o)                                // frontvonal: o = {c, w, teeth: 'bal' | 'jobb' (a támadó oldal fogazata), a}
T.shift(keysA, keysB, i0, i1) → km                      // a két front közti elmozdulás két kijelölt pontnál (03 mérőszalag, „kb.”)
TortTerr.asChoro(TORT_HATAR, ids) → {q, counties: [{n: id, p: [gyűrű]}]}   // FoldChoro.load-kompatibilis nézet (14)
```

- A frontok kulcskockái a lecke **kódjában** (geometria), a dátumuk a `.md` `### Adatok` alatt (date típus). A
  `.md` megjegyzése felsorolja a felhasznált atlaszokat. Minden front „vázlatos”.
- Szín: az ellenőrző hatalmak színe a leckéből (semleges skálák: tengely = indigó-tónusok, szövetséges =
  szilva-tónusok, semleges = papír, megszállt = sraffozás). Nincs „jó” zöld, „rossz” piros.
- **Terület és népesség soha nem a sokszögből**: a modul nem ad `area()` függvényt a leckének.

#### TortCity – vázlatos Budapest · referencia: `02-dualizmus`

A TortMap-re épül (kamera, címkézés), saját Lambert-vetülettel Budapestre (`lcc({lon0: 19.05, lat0: 47.5,
lat1: 47.3, lat2: 47.7})`).

```
const C = TortCity.create(L, {map, rect})               // a geometria a modulban (vázlatos, lásd lent)
C.base(ctx, {year, a, labels: true})                    // Duna két partja, szigetek (Margit, Óbudai, Csepel-sziget csúcsa),
                                                        //   városhatár az év szerint: < 1873 három város (vázlatos foltok),
                                                        //   1873–1949 vázlatos határ, ≥ 1950 Nagy-Budapest (NE admin-1 'Budapest')
C.bridges(ctx, years, d, o)                             // years = {lanchid: {built, destroyed?, rebuilt?}, …} az L.dat-ból;
                                                        //   d: tört év → álló / épülő (szaggatott) / lerombolt (megtört, halvány) /
                                                        //   újjáépült; o = {labels, a}
C.roads(ctx, items, o)                                  // items = [{id: 'andrassy' | 'nagykorut' | 'kiskorut' | 'rakoczi' | …,
                                                        //   p: 0..1 (kirajzolás), c, w}]
C.places(L, items, o)                                   // [{id, lon, lat, s, k, pri, t (megjelenés 0..1)}] → map.labels
C.ring(ctx, pts, o)                                     // bekerítés, gettó- vagy körzethatár (lecke adja: pts)
C.pt(lon, lat) → {x, y} · C.hit(px, py, items) → id
```

- **Geometria és jog:** a Duna középvonala a **hidak hídfőinek felezőpontjain** halad át (a hídfők koordinátái
  Wikidata, CC0 – a kódban, forrással), a parttávolság szakaszonként megadott mederszélesség (kb. 300–600 m
  *(vázlatos)*); a szigetek egyszerű sokszögek. Térképszolgáltatás (OSM, Google) geometriáját **nem** másoljuk
  (ODbL/jogvédett). „Vázlatos” bélyeg.
- A hidak évszámai és a helyszínek koordinátái a leckék `.md`-jében (date, coord – `box: [18.9, 47.35, 19.35, 47.65]`).

#### TortParl – patkó és mandátumszámító · referencia: `16-demokracia`

```
TortParl.hemi(L, o) → hits                              // o = {cx, cy, r0, r1 (belső/külső sugár), seats: [{id, n, col, pat}],
                                                        //   order: [id…] (balról jobbra), rows (alap: automatikus), sel: id,
                                                        //   lines: [100, 133] (küszöbjelek a patkón), a, t (beúszás 0..1)}
TortParl.legend(L, items, o)                            // jelmagyarázat: név {s, k}, mandátum, %, minta
TortParl.palette(n, o) → [{col, pat}]                   // semleges: egy színárnyalat n tónusa + minta ('teli', 'pötty', 'csík',
                                                        //   'sraff'); o.grey: true → szürke tónusok (1990, 13)
TortParl.dhondt(votes: {id: n}, seats) → {id: n}
TortParl.calc(o) → {smd, frag, list, total, thr}        // o = {districts: [{votes: {id: n}}], list: {id: n}, listSeats: 93,
                                                        //   threshold: 0.05 (vagy {1: .05, 2: .10, 3: .15}), frag: 'vesztes+győztes' |
                                                        //   'vesztes' | 'nincs', method: 'dhondt'} – a 16 kalkulátora
TortParl.bar(L, a, b, o)                                // szavazatarány vs mandátumarány két sávban (aránytalanság)
```

- A pártnevek és -adatok a `.md`-ből; a 05, 10, 13 valódi választás **eredményét** jeleníti meg (`seats`), a
  `calc`-ot csak a 16 használja *(kitalált adattal)*.

#### TortState – intézményséma · referencia: `16-demokracia`

```
const S = TortState.create(L, {nodes: [{id, s, k, x, y, kind: 'nép' | 'testület' | 'személy' | 'bíróság' | 'párt' |
                                        'sajtó' | 'egyéb'}],
                               edges: [{from, to, rel: 'választ' | 'ellenőriz' | 'kinevez' | 'irányít' | 'felügyel',
                                        s, k (a nyíl felirata)}]})
S.layout(name, pos)                                     // több elrendezés: {id: [x, y]}; S.morph(a, b, u) áttűnés
S.set(id | edgeIndex, on, t)                            // kapcsoló: ki/be (kialvó nyíl, szürkülő csomópont, áthúzott felirat)
S.timeline(events, d)                                   // events = [{a: tört év, off: [id…], on: [id…], over: {id: 'párt'}}] →
                                                        //   a d pillanat állapota (visszaléptetéskor is helyes – nincs halmozás)
S.draw(ctx, {hl, dim, a, t})                            // dobozok L.measure-rel, a szöveghez igazodva; nyílhegyek, címkék
S.hit(px, py) → id · S.card(L, id, lines, o)            // kattintásra kártya: ki választja, mennyi időre, kit ellenőriz
```

- A nyílfeliratok és a kapcsolók dátumai a `.md`-ből; a dobozok helye a kódban. Az „irányít” (pártállam) nyíl
  bordó `#8a2f5b`, a demokratikus kapcsolatok tinta, az ellenőrzés kékeszöld.

### 4.3 Referencialeckék – az első kör

| Lecke | Mit épít / próbál ki | Miért ez |
|---|---|---|
| **0. köteg (adat)** | `map-torthatar.js`, `map-europa.js`, `tools/build_tortmap.py` | minden térképes lecke erre épül; a pontosság itt dől el, és itt ellenőrizhető egy helyen |
| **07-masodik-vilaghaboru** | **TortTerr** (minden függvény, a `front` és az `explode` is – a 03, 04, 09 örökli) | a legösszetettebb térképes lecke: hovatartozás dátum szerint + frontok + Kárpát-medencei revízió; ha itt működik, minden más egyszerűbb |
| **02-dualizmus** | **TortCity** (`base` év szerint, `bridges`, `roads`, `places`) | a város „évszámos” állapotgépe; a 07, 08, 11 örökli |
| **16-demokracia** | **TortParl** (teljes, `calc` is) + **TortState** (teljes, `timeline` is) | a semleges paletta és a kitalált pártok mintája; a TortState `timeline`-ja a 05, 10, 13 kapcsolóinak alapja |
| **06-pengo** | – (FoldChart log-tengely, a hatványalak megoldása) | nem épít modult, de a 20. századi adatkezelés (log, hatványalak, két forrás) mintája |
| **15-nepesedes** | – (FoldChart korfa, FOLD_KORFA) | adatvezérelt, kész modulokra épül – a köteg ötödik helyét tölti ki függőség nélkül |

Az első kör után a koordinátor átnézi a négy modult (API, 22 px, alfa, visszaléptetés, semleges színek) és az
adatfájl `notes`-ait, és csak utána indul a 2. köteg. A 16 egyedül két modult épít – ez a köteg legkockázatosabb
leckéje; ha csúszik, a 2. kötegből a 05 és a 10 vár rá, a 04, 08, 03 nem.

---

## 5. Build-, QA- és motorigények

### 5.1 A helyzet (ellenőrizve: `tools/build_lesson.py` fejléce, 2026-11-25)

| Igény | Megoldás a meglévő eszközökkel |
|---|---|
| 55 szavas panel | alapérték (nincs `maxWords`) |
| lektorálás jelzése (04, 05, 07, 08, 10, 11, 13, 14) | spec `"review": ["történész"]` (08: `["történész", "emlékezetpedagógus"]`) → a build kéri a `<!-- Szakmai ellenőrzés: … -->` blokkot |
| forrás minden adathoz | spec `"sources": true` (mind a 17 leckében) |
| évszám, dátum, hónap | `year`, `date` („1946. július” – a nap `null`, `a` tört év) |
| tartomány, becslés | `range` („kb. 500–565 ezer fő”), „kb.”, „(becslés)” → `est` |
| helyszín | `coord` + `box` (Kárpát: `[9, 42, 30, 51]`; Európa: `[-25, 33, 60, 72]`; Budapest: `[18.9, 47.35, 19.35, 47.65]`) |
| idősor (adósság, robbanófej, népszámlálás) | `series` („1973: 2,12 · 1975: 4,20”, `"ux": "év"`, `"unit": "milliárd USD"`) |
| korfa, mutatók | `dataset` `{"id": "korfa-wpp2024"}`; FOLD_WDI: `{"id": "fejlettseg-wdi"}` |
| jogszabály- és közkincs idézet | `### Idézet` + `<!-- idézet: … · szerző † <év> · közkincs -->` (jogszabály: † nélkül); a build elutasítja, ha † + 70 ≥ 2026 |
| kitalált pártok, körzetek (16) | „(kitalált példa)” a `.md`-ben, `model` |
| QA-állapotok (dátumcsúszka közepe, kalkulátor-esetek) | `__qaStates` + `--states`; késői állapot: `__lesson.st` közvetlen állítása |

**Új build-, QA- vagy motorfunkció a gyártáshoz nem kell** – egy kivétellel, amelyre van kerülőút (5.2/1).

### 5.2 Kis, nem blokkoló javaslatok (a koordinátornak)

1. **Hatványalak a `number`/`series` típusban:** `4 · 10^29 pengő`, `10^20` – és a szorzószavak bővítése (billiárd
   10¹⁵, trilliárd 10²¹, kvadrillió 10²⁴, kvadrilliárd 10²⁷; a „trillió” figyelmeztetés maradjon). Haszna: a 06
   kifejezheti a hiperinflációt a `.md`-ben. Kerülőút a bővítésig: `series` a 10-es kitevőkkel és
   megjegyzéssel. Ha a koordinátor a 0. kötegben megcsinálja, a 06 már ezt használja.
2. **„Érzékeny lecke” jelző a spec-ben** (`"sensitive": true`): a QA figyelmeztet, ha a leckében TtTipp-blokk,
   pontszám (`score`) vagy hangeffektus van. Addig a szerződés 20. fejezetének kézi ellenőrzőpontja.
3. **`date`-tartomány** („1944. május 15. – július 9.”) egy kulccsal (`lo`, `hi`, mint a `range`) – most két kulcs
   kell.
4. **Glif-próba:** a ⅓, ⅔, ½, ¾, ², ⁹ és a cirill/román/szlovák ékezetek (ă, ș, ț, č, ž – a mai helynevekhez:
   Timișoara, Košice) mind a négy fontváltozatban. A latin-ext ezt tartalmazza, de ellenőrizendő.
5. A négy új modul az első kör után a `shared/tort/` alá kerülhet (egyeztetve): `terr.js`, `city.js`, `parl.js`,
   `state.js`.

### 5.3 A szerződés kiegészítése

A 7. fejezet kész szövege a `SZERZODES.md` 20. fejezeteként beillesztve (2026-11-25).

---

## 6. Gyártási sorrend és lefedettség

### 6.1 Gyártási sorrend (legfeljebb 5 párhuzamos lecke kötegenként)

Egyszerre legfeljebb 5 al-ügynök fut; mindegyik saját, egyedi scratchpad-almappát kap (`EJSZAKAI-GYARTAS.md`,
8. tanulság).

| Köteg | Leckék (nehézség) | Új modul / adat | Újrahasznosított |
|---|---|---|---|
| 0 | – (adat-ügynök) | `map-torthatar.js`, `map-europa.js`, `tools/build_tortmap.py`; opcionálisan 5.2/1 | – |
| 1 | **07-masodik-vilaghaboru** (3), **02-dualizmus** (3), **16-demokracia** (3), **06-pengo** (2), **15-nepesedes** (2) | TortTerr (07) · TortCity (02) · TortParl + TortState (16) | TortMap, TortTimeline, TortSource, TortCards, TortGlobe, FoldChart, MatChart, BioPlot, TtTipp |
| 2 | **04-trianon** (3), **08-holokauszt** (3), **03-elso-vilaghaboru** (3), **05-diktaturak** (3), **10-szovjetizalas** (3) | – | TortTerr, TortCity, TortParl, TortState, TortScene, + a fentiek |
| 3 | **11-forradalom-1956** (3), **09-hideghaboru** (3), **14-hataron-tul** (3), **13-rendszervaltas** (3), **12-kadar-rendszer** (2) | – | TortCity, TortTerr, TortParl, TortState, FoldChoro, FoldChart |
| 4 | **01-nemzetallamok** (2), **17-europai-unio** (2) | – | TortTerr, FoldChoro, MatChart, TortCards, TortState |

Indoklás:
- **0. köteg előfeltétel.** A 07 (TortTerr) a valódi adatfájlra épül; vázlatos tesztadattal építeni, majd
  átállni dupla munka lenne.
- **1. köteg:** a három referencialecke + két független, adatvezérelt lecke. A 06 és a 15 a 20. századi
  adatkezelés (log-tengely, hatványalak, korfa, két forrás) mintája, és a 08-as lektorálás előtt beállítja a
  forrásjelölés hangját.
- **2. köteg:** a lektort kérő nagy leckék (04, 08, 05, 10, 03). A **08** a 2. köteg elején induljon, mert a
  lektori kör a leghosszabb; a koordinátor a 08 brief-jét (3. fejezet) a lektornak már az 1. köteg alatt
  megküldheti (tanári/lektori előzetes, nem gyártás).
- **3. köteg:** a második világháború utáni leckék a 2. köteg modulhasználati tapasztalatával.
- **4. köteg:** a két legkevésbé kockázatos lecke; a 01 időrendben első, de nem függ semmitől, ami később
  készül – a többi lecke nem hivatkozik rá.
- **Költség** (`EJSZAKAI-GYARTAS.md` és a kerethasználati jegyzet alapján): 17 lecke × ~0,45 % ≈ **7–8 % heti
  keret** + a 0. köteg kb. 0,5–1 %; az 5–6. évfolyamos történelemleckék kb. 38 perc / 181 ezer tokenes átlaga
  felett, a térképek és a lektori pontok miatt inkább 45–60 perc leckénként; 4 köteg × 60–75 perc falióra.

### 6.2 Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / fejlesztési feladat |
|---|---|---|
| 1. A modern kor születése (5) | 01 | a nemzeti jelképek (zászlók, himnuszok) csak kitalált példán; az USA létrejöttének „okai” csak egy lépés |
| 2. A dualizmus kora (7) | 02 | a „legjelentősebb kulturális alkotások” (Operaház, Parlament stb.) csak helyszínként; a cigányság mesterségei egy kártya |
| 3. Az első világháború és következményei (11) | 03, 04 | a „hátország” csak egy lépés; háborús emlékhelyek felkeresése (tevékenység) – tanári |
| 4. Totális diktatúrák (5) | 05 (+08) | a fasiszta Olaszország csak egy mondat; filmek (tevékenység) |
| 5. A Horthy-korszak (9) | 06 (+04, +08) | „Életmód, szabadidő, sport” csak egy lépés részeként; „Külpolitikai kényszerpályák” a 07 revíziós lépésében; „érintkezési formák” (társadalmi illem) nincs |
| 6. A második világháború (10) | 07, 08 | „A világháború fegyverei” csak felsorolásszerűen (nem fegyvertechnikai lecke – szándékos); „Az ellenállás formái” csak az embermentés példáin |
| 7. A megosztott világ (5) | 09 | „Az új tömegkultúra kialakulása” egy kártya; a hidegháború és a mai világ összevetése csak tanári kérdés |
| 8. Magyarország szovjetizálása (10) | 10 (+06: 1946, forint) | „A személyi kultusz” jelkép-helyőrzővel (nincs portré, plakát); csasztuskák, viccek (tevékenység) – szerzői jog és hangnem miatt nem |
| 9. A forradalomtól az ezredfordulóig (20) | 11, 12, 13 | „A forradalom lakóhelyünkön” csak tanári helyszínnel; a „rendszerváltoztatástól napjainkig” idővonal 2004-ig (0. döntés, 9.); a „Többpártrendszer működése” a 16-ban intézményként |
| 10. Együttélés a Kárpát-medencében (8) | 14 (+04, +10) | az 1910-es és 1990 utáni **etnikai térkép** települési szinten (Kocsis-féle térképek – jogvédett; csak megyei szintű saját choropleth); a „hűség és helytállás” példái csak a két életút |
| 11. Népesedés és társadalom (5) | 15 | a „multikulturalizmus, terrorizmus, globalizáció” csak definíció-szinten; fiktív napló (tevékenység) |
| 12. A demokratikus állam (7) | 16 | szerepjáték (tevékenység) – a kalkulátor helyettesíti részben |
| 13. Régiók története (14) | 17 (+09: USA, +13: Közép-Európa, +01) | **India, Kína, Közel-Kelet, az amerikai polgárháború** – nincs saját lecke (tartalék 2, 3); a Közel-Kelet szándékosan kimarad (0. döntés, 13.) |
| 14. Mérlegen a magyar történelem (8) | részben 02 (feltalálók), 04 (Trianon máig), 14 (kapcsolatok), 17 (Közép-Európa) | **„Lábnyomaink a nagyvilágban”** (utazók, tudósok, olimpikonok, művészek) – tartalék 1; „A magyar megmaradás kérdései” középkori–kora újkori része az 5–6. évfolyamé |

**A forrásszöveg kinyerési hibái** (a `kerettanterv/tortenelem/7-8.md`-ben, javítás nélkül):
- A 3., 9. és 11. témakör táblázatában a fejléc alatt egy „Fejlesztő feladatok” sor áll – a táblázat fejléce
  kétszer került be.
- A 8. témakör végén két üres `**` sor maradt.
- A 8. témakörben „megpróbáltatása-inak” elválasztójel maradt a szóban („A határon túli magyarok
  megpróbáltatása-inak bemutatása”).
- A 9. témakör kronológiája két sorba tört („…1956–1989 a Kádár-rendszer,” / „1989–1990 a rendszerváltoztatás…”).
- A 14. témakör „Javasolt személyek” listája két sorba tört („Egerszegi Krisztina,” / „Balczó András”).
- A 6. témakörben „ellenállás és embermentés   formáira” többszörös szóköz.
- Az óraszámok összege 124, egyezik a forrással; a sávbevezető táblázata ehhez „Két mélységelvű téma: 12” órát
  ad (összesen 136), a szöveg viszont „6–10 óra”-t ír – a forrás belső ellentmondása.

Az idézetek a forrás alakját követik, a hibákkal együtt, „[sic]” nélkül.

**Tartalék-jelöltek**, ha a sorozat folytatódik (fontossági sorrendben):

1. `18-labnyomaink` – magyar tudósok, Nobel-díjasok, olimpikonok időrendben és térképen (14.; TortTimeline, MatChart,
   TortGlobe) – adatvezérelt, de a válogatás szerkesztői döntés (kanonizálás veszélye).
2. `19-kina-india` – Gandhi és a függetlenség (1947), Mao és a Kínai Népköztársaság (1949), a gazdasági felemelkedés
   (FOLD_WDI GDP-görbék) (13.).
3. `20-usa` – az USA létrejötte, a polgárháború (Lincoln), világhatalommá válás gazdasági adatsorokkal (13.).
4. `21-kozel-kelet` – csak külön szerkesztői irányelvvel és két lektorral (13.).
5. `22-sport-eletmod` – a Horthy-kori és a Kádár-kori életmód, sport, szabadidő (5., 9.).

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): az NKP *Történelem 7.* és *8.* digitális tankönyve; a
Holokauszt Emlékközpont, a DEGOB és a Zachor Alapítvány oktatási anyagai; a Terror Háza és a NEB 1956-os
adatbázisai (perek56.hu); az ÁBTL online kiállításai; a KSH történeti statisztikai idősorai. Nálunk a többlet: a
dátum szerint mozgó térkép, a számok forrással és tartománnyal, és az interaktív intézményi és választási
modellek.

---

## 7. Javasolt szerződés-kiegészítés (kész szöveg a `leckek/SZERZODES.md`-hez)

A következő fejezet változtatás nélkül beillesztve a `SZERZODES.md` végére, a 19. (Digitális kultúra-kiegészítés)
után (2026-11-25).

```markdown
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
```
