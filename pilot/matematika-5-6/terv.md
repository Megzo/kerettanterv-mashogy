# Pilot: Matematika 5–6. – a leckesor terve

Forrás: [`kerettanterv/matematika/5-6.md`](../../kerettanterv/matematika/5-6.md) (NAT 2020,
általános iskola, a *Matematika 5–8.* kerettanterv 5–6. sávja: 18 témakör, 272 óra). Az
idézetek szó szerint onnan valók. A lecke-formátum: [`leckek/SZERZODES.md`](../../leckek/SZERZODES.md).
A terv a felhasználó távollétében készült (2026-11-23); a menet közben hozott döntéseket és
indoklásukat az 1.4 pont sorolja fel – ezek jóváhagyásra várnak.

## 1. Bevezető

A pilot **18 leckéje** az 5–6. osztályos matematika-kerettanterv mind a 18 témakörét érinti.
A formátum ugyanaz, mint a fizikánál és a történelemnél: 6–9 lépés, 1920×1080-as színpad, bal
oldalt animáció, jobb oldalt magyarázó panel, világos, papírszerű háttér. A célcsoport 10–12
éves, ezért – a történelemhez hasonlóan – **lépésenként legfeljebb 45 szó** a panelen.

Matematikából a háttér maga is jelentést kap: a szerződés 40 px-es papírrácsa a **kockás
füzet**. A leckék esztétikája a „rajzlap”: tinta vonalak, pontos szerkesztés, kevés dísz. (Az
`../iskola/matek-kor-pi.html` helyi másolata a terv írásakor nem volt elérhető; az ottani
stílust a CLAUDE.md leírása alapján vettük figyelembe.)

### 1.1 Hol ad egy interaktív animáció *valódi* belátást?

A tankönyv és a tábla statikus ábrát ad, a videó egy rögzített menetet. Matematikából hat
helyzetben ad többet az élő, léptethető ábra:

1. **Folytonos nagyítás a számegyenesen.** A tizedek közé századok, azok közé ezredek
   férnek. A ⅓ tizedes alakja „sosem ér véget”, ezt a végtelen nagyítás mutatja meg. A
   negatív számok a 0-ra tükrözve jelennek meg. A tankönyv mindig csak egy kivágatot mutat,
   a nagyítás folyamatát nem.
2. **Pontos geometriai átalakítás (morfolás).** Átdarabolás (paralelogrammából téglalap),
   a háromszög letépett sarkai egy egyenesszöggé állnak össze, a háló kockává hajtogatódik.
   A diák látja, hogy közben semmi nem vész el és semmi nem torzul. Ez a „miért igaz”
   képi bizonyítása.
3. **Húzható, élő ábra (dinamikus geometria).** A diák húzza a csúcsot, közben él a mért
   szög, terület, távolság. A lényeg az, ami *nem változik* (a szögösszeg 180°, PA = PB). Ezt
   a kerettanterv is kéri: „ismer és használ dinamikus geometriai szoftvereket”.
4. **Ugyanaz több alakban, összekapcsolva.** A tört kör-, szalag-, számegyenes- és tizedes
   alakban jelenik meg, az arányosság szövegként, táblázatként és grafikonként, az adat oszlop-
   és kördiagramon. Ha az egyik változik, mind változik.
5. **Sok ismétlés másodpercek alatt.** 10 000 dobás után a relatív gyakoriság
   stabilizálódik. A véletlen zaja és a mögötte álló szabály együtt látszik. Ilyen kísérletet
   egy tanórán nem lehet elvégezni.
6. **Folyamat lépésenként, visszatekerhetően.** A körzős szerkesztés, a kifejezésfa
   kiértékelése, a „tökéletes pénztárgép” váltása, a mérlegelv: minden lépés oka látszik,
   és vissza is lehet léptetni.

### 1.2 Mit hagyunk ki, és miért

- **Gyakorló feladatsorokat (drill), az írásbeli algoritmusok gépies begyakorlását.** Ezt a
  füzet és a feladatgyűjtemény jobban végzi. A leckék a *miértet* mutatják meg; a gyakorlás
  legfeljebb egy `> megjegyzés:` feladat.
- **Projektmunkát, mérést valódi eszközzel, társasjátékot** („Bumm”, „Osztó-fosztó”,
  „Kukás játék”, osztályterem mérése). Ezek tanórai tevékenységek. A lecke legfeljebb
  bevezeti vagy kiértékeli őket.
- **Kvízt, pontozást, „gamifikációt”.** Az interakció a modellt mozgatja, nem jutalmaz.
- **A 7–8. évfolyam anyagát.** A forrás 5–8. évfolyamra szóló dokumentum. A „hozzájárul
  ahhoz, hogy a tanuló a nevelési-oktatási szakasz végére” kezdetű célok a 8. év végére
  vonatkoznak. Ezekből csak azt dolgozzuk fel, ami az 5–6. **fejlesztési feladatai** között is
  szerepel. Kimarad tehát a Pitagorasz-tétel, a középpontos tükrözés, a speciális négyszögek
  rendszere (trapéz, deltoid, rombusz…) és a végtelen nem szakaszos tizedes tört. Ez utóbbi
  csak érdekességként jelenik meg a 08-ban (lásd 6. fejezet).

### 1.3 Kiválasztási elv

1. **Arányosság:** nagyjából óraszám szerint, kb. 15 óránként egy lecke, témakör-csoportokban:

   | csoport | témakörök (óra) | óra | lecke |
   |---|---|---|---|
   | Halmaz, logika | 1 (10), 2 (10) | 20 | 01 (+ a 18 kombinatorika-része) |
   | Természetes számok | 3 (20), 4 (16) | 36 | 02, 03, 04 |
   | Egész számok | 5 (18) | 18 | 05 |
   | Törtek | 6 (18), 7 (18), 8 (14) | 50 | 06, 07, 08 |
   | Arány, szöveges, függvény, sorozat | 9 (20), 10 (20), 11 (10), 12 (8) | 58 | 09, 10, 11, 12 |
   | Geometria | 13 (16), 14 (18), 15 (20), 16 (16) | 70 | 13, 14, 15, 16 |
   | Statisztika, valószínűség | 17 (10), 18 (10) | 20 | 17, 18 |

   A statisztika és a valószínűség kicsit felülreprezentált (10 óra/lecke). Ennek oka a
   2. pont: itt ad az animáció a legtöbbet, és ez a két modul a Matek 9–10-ben is kell.
2. **Ahol a tanterv maga is modellt vagy eszközt kér:** a „tökéletes pénztárgép” (02),
   a „hasábra felcsavart számegyenes” (03), a „párhuzamos számegyenesek” és a „tányérmodell”
   (06), a „mérlegelv” és a „szakaszos ábrázolás” (11), a „sarkok levágása” és a „hurkapálcás
   háromszög” (14), a „3 korong” eseménykártyái és a „10 korong” lépegetős játéka (18). Ezek
   biztosan bekerülnek, mert a lecke itt a tanórai tevékenység digitális párja.
3. **Építőkockák újrahasznosítása:** a leckék 12 közös modulra épülnek (4. fejezet). Ez a
   sorozat építi a **geometriai és számegyenes-eszközkészletet**, amelyet a Matek 9–10 is
   használ.

A leckék sorszáma a kerettanterv sorrendjét követi, a **gyártási sorrend** ettől eltér
(4. fejezet). Az „Adatok” pontok értékei a tartalomfájl `### Adatok` rétegébe kerülnek.
Jelölések: *(kitalált)* = didaktikai példa, nem valós adat (árak, osztályfelmérés);
*(ellenőrizendő)* = valós adat, amelyet a gyártás előtt forrásban ellenőrizni kell. Minden
számpéldát utánaszámoltunk.

### 1.4 Döntések (jóváhagyásra)

1. **18 lecke, nem 16.** A műveleti sorrend és a műveleti tulajdonságok négy témakör (4, 5, 7,
   8) tanulási eredményei között is szerepelnek, mégis egyik leckébe sem fértek bele. Ez lett
   volna a legnagyobb hiány, ezért kapott külön leckét (04). Közben a halmazokat és a logikát
   egy leckébe vontuk össze (01), a kombinatorikát pedig a valószínűségbe tettük (18). A 18
   lecke ugyanúgy hat 3-as kötegben készül el, mint 16 vagy 17 lecke, ezért időben nem kerül többe.
2. **A háromszögek és a négyszögek egy leckében (14).** A 14. témakörben az 5–6. fejlesztési
   feladata csak a háromszög, a téglalap és a négyzet. A négyszögcsalád a 7–8. anyaga,
   ezért itt csak a 360°-os szögösszeg és a „minden négyzet téglalap” szerepel.
3. **A `MatText` (tört- és kitevőszedés a vásznon, pontos törtaritmetika) közös fájl lesz**
   (`shared/matek/mtext.js`). Nem leckén belüli modulként készül, hanem az előkészítő ügynök
   írja meg a build-bővítéssel együtt. Indok: a build és a vászon ugyanazt a jelölést
   (`3/4`, `2^3`) értelmezi, és az első köteg mindhárom párhuzamos leckéjének kell. Ha leckén
   belül készülne, három eltérő változat lenne belőle. Előzmény: a `shared/tort/proj.js` is
   így készült. A `lesson.js` és a `lesson.css` változatlan marad.
4. **A tört jelölése a `.md`-ben automatikus:** a `3/4` (számjegy/számjegy) álló törtként
   jelenik meg. Szó szerinti ferde vonal: `3\/4`. Tanárnak ez a legtermészetesebb; a „km/h”
   betűs, ezért nem érinti.
5. **Halmaz kapcsos zárójellel:** a `{1; 2; 3}` ütközik a `{adatkulcs}` hivatkozással. Szabály:
   ha a zárójel tartalma nem adatkulcs, és van benne `;`, vagy üres, akkor szó szerinti
   halmaz. A `\{ \}` mindig szó szerinti (5.1).
6. **Előjelszínek:** pozitív = cinóber, negatív = kékeszöld, mint a hőmérőn a meleg és a
   hideg. Ez egyezik a kerettanterv „10 korong” játékával is (piros = pozitív irány).
7. **Mappa:** `leckek/matematika-5-6/`, a `fizika-7-8`, `tortenelem-5-6` mintájára.
8. **Árak, nevek, osztályfelmérés kitaláltak.** A valós árak gyorsan elavulnak, és vitát
   szülnek. A `.md` megjegyzésben jelöli őket.

---

## 2. A leckék

| # | slug | cím | témakör | nehézség (1–3) | építőkocka |
|---|---|---|---|---|---|
| 01 | `01-halmazok` | Hová kerül a 15? – halmazok, „és”, „vagy” | 1 (+2) | 2 | **MatVenn**, MatLine |
| 02 | `02-helyi-ertek` | Mit csinál a tökéletes pénztárgép? – helyi érték és számrendszerek | 3 (+4) | 2 | saját (pénztárgép) |
| 03 | `03-oszthatosag` | Miért nem lehet 7 sütit téglalapba rakni? – osztók, prímek, maradékok | 3 | 3 | MatLine, Mat3D |
| 04 | `04-muveleti-sorrend` | Mennyi 2 + 3 · 4? – műveleti sorrend és műveleti tulajdonságok | 4 (+5, 7, 8) | 2 | **MatExpr**, MatGeo |
| 05 | `05-egesz-szamok` | Mennyi −3 − (−5)? – az egész számok | 5 | 2 | MatLine |
| 06 | `06-tortek` | Melyik a nagyobb: 2/3 vagy 3/4? – törtek, bővítés, egyszerűsítés | 6 | 2 | **MatFrac**, MatLine |
| 07 | `07-tortmuveletek` | Miért kell közös nevező? – műveletek törtekkel | 7 | 2 | MatFrac, MatExpr |
| 08 | `08-tizedes-tortek` | Hol van a 0,25? – tizedes törtek a számegyenesen | 6, 8 | 3 | **MatLine ★** |
| 09 | `09-aranyossag` | Mennyibe kerül 7 kifli? – egyenes és fordított arányosság | 9, 11 | 2 | **MatPlot ★** |
| 10 | `10-szazalek` | Visszakapod az árat? – százalékszámítás | 9 | 1 | MatFrac, MatLine |
| 11 | `11-szoveges-feladatok` | Mit gondoltam? – szakaszos ábra, visszafelé gondolkodás, mérlegelv | 10 | 2 | **Mérleg**, MatFrac |
| 12 | `12-sorozatok` | Hány gyufa kell a 100. házhoz? – sorozatok és szabályok | 12, 11 | 1 | MatPlot |
| 13 | `13-terulet` | Miért fele a háromszög a paralelogrammának? – kerület, terület, átdarabolás | 13 | 2 | MatGeo |
| 14 | `14-haromszogek` | Miért mindig 180°? – szögek, háromszögek, négyszögek | 14 (+13) | 3 | **MatGeo ★** |
| 15 | `15-tukrozes-szerkesztes` | Honnan tudja a körző, hol a közép? – tengelyes tükrözés, szerkesztések | 15 | 3 | **MatCon**, MatGeo |
| 16 | `16-testek` | Melyik hálóból lesz kocka? – testek, háló, felszín, térfogat | 16 (+13) | 3 | **Mat3D** |
| 17 | `17-statisztika` | Mit mutat az átlag? – diagramok, átlag, módusz, medián | 17 | 2 | **MatChart** |
| 18 | `18-valoszinuseg` | Melyik összeg a legszerencsésebb? – valószínűségi kísérletek | 18 (+2) | 2 | **MatRand**, MatChart |

A **félkövér** modult az adott lecke építi meg elsőként. A ★ a referencialeckét jelöli (első
köteg, 4. fejezet). A nehézség gyártási nehézséget jelent: 1 = egy fő vizuál, meglévő modul;
2 = egy új modul vagy közepes interakció; 3 = nagy új modul (3D, zoom, húzható geometria)
vagy több szinkron nézet.

Témakörönként: 1 → 01 · 2 → 01, 18 · 3 → 02, 03 · 4 → 04, 02 · 5 → 05 · 6 → 06, 08 · 7 → 07 ·
8 → 08 (+04) · 9 → 09, 10 · 10 → 11 · 11 → 09, 12 · 12 → 12 · 13 → 13 (+14, 16) · 14 → 14 ·
15 → 15 · 16 → 16 · 17 → 17 · 18 → 18.

Közös a briefekben: minden leckében van egy **„Tippelj előbb!”** pillanat (szavazás vagy
becslés, utána az animáció dönt), mert a kerettanterv szinte minden témakörben kéri a
becslést és az ellenőrzést. A tévhitet mindig egy *konkrét ellenpélda* cáfolja a vásznon.

---

## 3. Briefek

### 01 · `01-halmazok` – Hová kerül a 15? – halmazok, „és”, „vagy”

- **Tanulási cél:** Elemeket egy, majd két szempont szerint halmazba rendez. A közös rész
  azokat az elemeket tartalmazza, amelyekre **mindkét** feltétel igaz („és”). Az egyesítésbe
  azok kerülnek, amelyekre **legalább az egyik** igaz („vagy”, tehát mindkettő is jó). A
  kiegészítő halmazba („nem”) a többi elem kerül. Részhalmaz. A „legalább 3 és legfeljebb 8”
  a számegyenesen.
- **Kerettanterv:** „elemeket halmazba rendez több szempont alapján;” · „részhalmazokat
  konkrét esetekben felismer és ábrázol;” · „véges halmaz kiegészítő halmazát
  (komplementerét), véges halmazok közös részét (metszetét), egyesítését (unióját) képezi és
  ábrázolja konkrét esetekben;” · „számokat, számhalmazokat, halmazműveleti eredményeket
  számegyenesen ábrázol.” · (2.) fogalmak: „„és”, „vagy”; „legalább”, „legfeljebb”” · „Konkrét
  elemek két tulajdonság szerinti válogatása során a mindkét tulajdonsággal rendelkező elemek
  és a pontosan egy tulajdonsággal rendelkező elemek elhelyezése a halmazábrán”.
- **Tévhitek:** a „vagy” kizáró („vagy páros, vagy 3-mal osztható, de nem mindkettő”). Az
  egyesítés elemszáma a két halmaz elemszámának összege (a közös elemeket kétszer számolja).
  Ami egyik körben sincs benne, az „nem tartozik sehova”, pedig az alaphalmaz része. A
  halmaz önmagának nem részhalmaza.
- **Kulcsvizuál:** a téglalap az alaphalmaz, benne az 1–20 számkártyák. Két kör: A = páros,
  B = 3-mal osztható. A kártyák a helyükre repülnek, a 15 egy pillanatra megáll a határon
  („Tippelj!”), aztán a B-be, a közös részen kívülre kerül. A kiemelt tartomány kitöltést és
  sraffozást kap.
- **Interaktív:** két legördülő tulajdonság (páros, páratlan, 3-mal osztható, 10-nél nagyobb,
  prím, 5-re végződik, 4-gyel osztható). A kártyák élőben átrendeződnek. Négy tartománygomb:
  „és”, „vagy”, „nem A”, „pontosan az egyik”. A kiírt elemszám mindig a ténylegesen
  besorolt kártyákból számolódik.
- **Lépések:** Válogassunk! · Két szempont egyszerre · „És”: a közös rész · „Vagy”: az
  egyesítés – mindkettő is jó! · Hányan vannak? (a kétszer számolás csapdája) · „Nem”: a
  kiegészítő halmaz · Részhalmaz · Halmaz a számegyenesen · Összefoglalás.
- **Adatok:** alaphalmaz 1–20. Páros: 10 elem; 3-mal osztható: 6 (3, 6, 9, 12, 15, 18);
  közös rész: 6, 12, 18 (3 elem); egyesítés: 10 + 6 − 3 = 13; egyik sem: 20 − 13 = 7
  (1, 5, 7, 11, 13, 17, 19). Részhalmaz: a 4-gyel oszthatók (4, 8, 12, 16, 20) ⊂ párosak.
  Prímek 20-ig: 8 (2, 3, 5, 7, 11, 13, 17, 19). Számegyenes: „legalább 3 és legfeljebb 8” →
  3, 4, …, 8 (6 egész); a „kisebb, mint 8” üres karikát kap.
- **Építőkocka:** MatVenn (első), MatLine (pontok, szakasz).

### 02 · `02-helyi-ertek` – Mit csinál a tökéletes pénztárgép? – helyi érték és számrendszerek

- **Tanulási cél:** A helyi értékes írás csoportosítás: 10 egyforma érméből 1 tízszer
  nagyobb lesz. A számjegy értéke a helyétől függ (alaki, helyi és valódi érték), a 0
  helytartó. Ugyanez a gép 3-as csoportokkal is működik (fabatka). Az írásbeli összeadás
  „maradéka” ugyanez a váltás. A tizedek és századok „apró fiókok”. A római szám nem helyi
  értékes.
- **Kerettanterv:** „érti és alkalmazza a számok helyi értékes írásmódját nagy számok
  esetén;” · „Számok helyi értékes írásmódjának megértése különböző alapú számrendszerekben
  csoportosítást, leltározást, helyiérték-táblázatba rögzítést tartalmazó feladatokon
  keresztül” · „ismeri a római számjelek közül az L, C, D, M jeleket, felismeri az ezekkel
  képzett számokat a hétköznapi helyzetekben;” · „Játék a „tökéletes pénztárgéppel” 10 000-nél
  nagyobb számokkal: a gép a tíz egyforma címletű pénzt kiveszi, és a következő fiókba
  beletesz egy tízszer akkora címletűt, majd kiírja a fiók tartalmát.” · „Vásárlás
  „fabatkával”, […] 1, 3, 9, 27, … címletű játékpénz felhasználásával úgy, hogy minél
  kevesebb érmét használjunk fel” · (4.) „Az írásbeli műveletvégzés algoritmusának segítése a
  „tökéletes pénztárgép” működési elvével” · fogalmak: „helyi érték, alaki érték, valódi érték”.
- **Tévhitek:** a 0 „semmi”, el lehet hagyni (305 ≠ 35). A számjegy értéke mindig ugyanannyi.
  A „10” mindig tízet jelent (a 3-as gépen a 10 három). Az átvitt 1 „egy egyes” (valójában egy
  tízes).
- **Kulcsvizuál:** fiókos pénztárgép, ahol a fiókok jobbról balra 1, 10, 100, 1000…
  címletűek, fölöttük a kijelző. Amikor egy fiókban 10 érme gyűlik össze, azok egy kupacba
  csúsznak, eltűnnek, és a szomszéd fiókba egy nagyobb érme pottyan. A kijelző számjegye
  közben átfordul. Alapváltáskor a címletek 1, 3, 9, 27, 81 lesznek.
- **Interaktív:** +1, +10, +100 gombok; alapcsúszka (2–10); „Fizess 47 fabatkát a legkevesebb
  érmével!” – a diák a fiókokba tesz, a gép vált. Az írásbeli összeadásnál két szám érméi
  öntődnek egy gépbe.
- **Lépések:** A tökéletes pénztárgép · Tíz egyforma → egy nagyobb · Alaki, helyi, valódi
  érték · A nulla helyet tart · Írásbeli összeadás: a gép vált · Fabatka: a 3-as gép ·
  Gép nélkül: római számok · Apró fiókok: tized, század · Összefoglalás.
- **Adatok:** 305: a 3 alaki értéke 3, helyi értéke százas, valódi értéke 300. 478 + 356 =
  834 (egyesek: 14 → 4, marad 1; tízesek: 7 + 5 + 1 = 13 → 3, marad 1; százasok:
  4 + 3 + 1 = 8). 47 = 1 · 27 + 2 · 9 + 0 · 3 + 2 · 1 → 3-as számrendszerben 1202 (5 érme).
  Római: MMXXVI = 2026, MDCCCXLVIII = 1848, L = 50, C = 100, D = 500, M = 1000. Apró fiókok
  (euró): 3,47 € = 3 · 1 € + 4 · 10 cent + 7 · 1 cent. A 10 centes érme és az 1 eurós érme
  létezik; a 10 eurós címlet bankjegy.
- **Építőkocka:** saját pénztárgép-szimuláció (a 08 „×10” lépése átveheti); MatText.
- **Meglévő anyag** (saját ismeret, nincs ellenőrizve): a „tökéletes pénztárgép” a magyar
  tankönyvekben gyakori tevékenység, animált változatáról nem tudunk.

### 03 · `03-oszthatosag` – Miért nem lehet 7 sütit téglalapba rakni? – osztók, prímek, maradékok

- **Tanulási cél:** Egy szám osztói az összes lehetséges téglalap oldalai. A prímszámból csak
  egy sor rakható ki, az 1 nem prím. A prímtényezős felbontás bármilyen sorrendben ugyanazt
  adja. A maradék szerint a számok „oldalakra” oszlanak. A végződési szabályok azért
  működnek, mert 10 és 100 osztható 2-vel, 5-tel, 4-gyel; a jegyösszeg-szabály azért, mert
  10 = 9 + 1. A legkisebb közös többszörös és a legnagyobb közös osztó.
- **Kerettanterv:** „ismeri a prímszám és az összetett szám fogalmakat; el tudja készíteni
  összetett számok prímtényezős felbontását 1000-es számkörben;” · „meghatározza természetes
  számok legnagyobb közös osztóját és legkisebb közös többszörösét.” · „ismeri és alkalmazza a
  2-vel, 3-mal, 4-gyel, 5-tel, 6-tal, 9-cel, 10-zel, 100-zal való oszthatóság szabályait;” ·
  „a természetes számokat osztóik száma alapján és adott számmal való osztási maradékuk
  szerint csoportosítja.” · „Oszthatósági tulajdonságok megfigyelése 3, 4, 5, … oldalú hasábra
  felcsavart számegyenes segítségével” · „„Bumm” játék a közös többszörösök meghatározásához:
  […] az 5 többszöröseinél tapsolnak, a másik csoport tagjai a 7 többszöröseinél dobbantanak”.
- **Tévhitek:** az 1 prím. Minden páratlan szám prím (9, 15, 21). A 2 nem prím, mert páros. Ami
  osztható 2-vel és 4-gyel, az 8-cal is (a 12 nem). A legkisebb közös többszörös a két szám
  szorzata (4 és 6: 12, nem 24).
- **Kulcsvizuál:** n darab süti (négyzetlap) rendeződik át minden lehetséges téglalapba. A 12
  háromféle téglalapot ad, a 7 csak egyet. Aztán egy számegyenes **felcsavarodik egy
  hatszög alapú hasábra** (Mat3D): a 6 többszörösei egy lapra, a 3 többszörösei két szemközti
  lapra, a párosak minden második lapra esnek.
- **Interaktív:** számcsúszka (1–60): a téglalapok kirakása, az osztók listája. Hasáb-csúszka
  (3–8 oldal), a hasáb forgatható. „Bumm”: két ritmus (például 4 és 6) villog a
  számegyenesen, és ahol egyszerre villannak, ott van a közös többszörös.
- **Lépések:** Sütik téglalapban: osztók · Prímek: csak egy sor · Prímtényezős fa · A
  felcsavart számegyenes: maradékok · Végződési szabályok (2, 5, 10, 4, 100) · Jegyek összege
  (3, 9) · Mikor villannak együtt? (közös többszörös) · A legnagyobb közös csempe (közös
  osztó) · Összefoglalás.
- **Adatok:** a 12 osztói 1, 2, 3, 4, 6, 12 (6 osztó, 3 téglalap: 1×12, 2×6, 3×4). A 36 osztói
  1, 2, 3, 4, 6, 9, 12, 18, 36 (9 osztó, páratlan sok, mert négyzetszám). 100-ig 25 prím van.
  360 = 2³ · 3² · 5; 840 = 2³ · 3 · 5 · 7. 4527: a jegyösszeg 18, tehát osztható 9-cel
  (4527 : 9 = 503). 100 = 4 · 25, ezért a 4-gyel való oszthatóságot az utolsó két jegy
  dönti el. lnko(12; 18) = 6: egy 12 × 18-as téglalap 2 · 3 = 6 darab 6 × 6-os csempével
  fedhető le. lkkt(12; 18) = 36; lkkt(4; 6) = 12; a „Bumm” 5-tel és 7-tel a 35-nél talál.
- **Építőkocka:** MatLine (felcsavarás: `MatLine.wrap`), Mat3D (hasáb), saját négyzetrács-
  átrendező.

### 04 · `04-muveleti-sorrend` – Mennyi 2 + 3 · 4? – műveleti sorrend és műveleti tulajdonságok

- **Tanulási cél:** A műveleti sorrend **megállapodás**: először a zárójel, aztán a szorzás és
  az osztás, végül az összeadás és a kivonás. A kifejezésfa megmutatja, mit kell előbb
  kiszámolni. Ugyanazok a számok más zárójelezéssel más eredményt adnak. Felcserélhetőség és
  csoportosíthatóság (fejszámolási trükk), széttagolhatóság (a téglalap kettévágása). Előbb
  becsülj, azzal ellenőrizz.
- **Kerettanterv:** „ismeri és helyesen alkalmazza a műveleti sorrendre és a zárójelezésre
  vonatkozó szabályokat fejben, írásban és géppel számolás esetén is a racionális számok
  körében;” · „a műveleti szabályok ismeretében ellenőrzi számolását, a kapott eredményt
  észszerűen kerekíti;” · „a fejszámoláson és az írásban végzendő műveleteken túlmutató
  számolási feladatokhoz és azok ellenőrzéséhez számológépet használ.” · „Az alapműveletek
  tulajdonságainak (felcserélhetőség, csoportosíthatóság, széttagolhatóság) ismerete és
  alkalmazása a gyakorlatban” · „Zárójeleket tartalmazó műveletsorok átalakítása,
  kiszámolása a természetes számok körében” · „ugyanazokat a számokat tartalmazó, csoportonként
  más-más zárójeles és zárójel nélküli műveletsorok elvégzése, majd az egyes csoportok
  eredményeinek összehasonlítása”.
- **Tévhitek:** mindig balról jobbra számolunk. A kivonás és az osztás is felcserélhető. A
  számológép mindig jól számol. 7 · (10 + 3) = 7 · 10 + 3 (csak az első tagot szorozza).
- **Kulcsvizuál:** a kifejezés szövege fölött felépül a fája. Az értékelés alulról felfelé
  „buborékol”: a részeredmény felszáll, a kifejezés összezsugorodik. A zárójel áthelyezésekor
  a fa átrendeződik. A széttagolhatóságot egy 7 × 13-as téglalap mutatja, amely 7 × 10 és
  7 × 3 részre válik.
- **Interaktív:** a diák zárójelet húz a 8 − 4 : 2 kifejezésre (négy változat), és a fa meg az
  eredmény élőben változik. Két számológép egymás mellett: „sorban számoló” (balról jobbra)
  és „tudományos”. A diák beüti ugyanazt, és látja az eltérést.
- **Lépések:** Ugyanazok a számok, más eredmény? · A megállapodás · A kifejezésfa · A
  számológép-csapda · Cseréld fel, csoportosítsd! · Ami nem cserélhető · Széttagolás: a
  téglalap kettévágása · Becsülj, aztán számolj! · Összefoglalás.
- **Adatok:** 2 + 3 · 4 = 14; (2 + 3) · 4 = 20. 8 − 4 : 2 = 6; (8 − 4) : 2 = 2; 8 : 4 − 2 = 0;
  8 : (4 − 2) = 4. 25 · 7 · 4 = 7 · (25 · 4) = 700; 48 · 25 = 12 · 100 = 1200. 12 − 5 = 7, de
  5 − 12 = −7; 12 : 4 = 3, de 4 : 12 = 1/3. 7 · 13 = 7 · 10 + 7 · 3 = 70 + 21 = 91.
  Becslés: 38 · 52 ≈ 40 · 50 = 2000 (pontosan 1976). Az egyszerű, négyműveletes
  zsebszámológépek jó része a beütés sorrendjében számol, ezért 2 + 3 × 4-re 20-at ír, a
  tudományos számológép 14-et *(ellenőrizendő: legalább két konkrét típuson kipróbálni;
  márkanevet a lecke ne írjon)*.
- **Építőkocka:** MatExpr (első), MatGeo (a téglalap), MatText.

### 05 · `05-egesz-szamok` – Mennyi −3 − (−5)? – az egész számok

- **Tanulási cél:** Negatív számokkal a hőmérőn, a mélységnél és az adósságnál találkozunk. A
  számegyenesen balra haladva a számok egyre kisebbek, ezért −5 < −2. Az ellentett a 0-ra
  tükrözött szám, az abszolút érték a 0-tól mért távolság. Az összeadás lépegetés a
  számegyenesen. Negatív szám kivonása = adósság elengedése (korongmodell). A szorzás
  előjelszabálya egy minta folytatásából adódik.
- **Kerettanterv:** „meghatározza konkrét számok ellentettjét, abszolút értékét;” · „ismeri az
  egész számokat.” · „Negatív számok a gyakorlatban: adósság, tengerszint alatti mélység,
  fagypont alatti hőmérséklet” · „Alapműveletek értelmezése tárgyi tevékenységek, ábrázolások
  alapján a számkörbővítés során” · „Az előírt művelet szemléltetése a számegyenesen való
  lépegetéssel, például „Hol van a kisautó, ha … ?”” · „szerencsekártya használata negatív
  szám kivonásának modellezésére: a bank elengedi 2 Ft adósságodat”.
- **Tévhitek:** −5 > −2, mert 5 > 2. A kivonás mindig csökkent. Két negatív szám összege
  pozitív (keveredik a szorzással). Az abszolút érték annyi, mint „elhagyjuk a mínuszt” (ez
  számoknál igaz, de a fogalom a távolság).
- **Kulcsvizuál:** egy függőleges hőmérő elfordul, és vízszintes számegyenes lesz belőle. A
  kisautó lépeget rajta. Korongmodell: cinóber (+) és kékeszöld (−) korongok, egy +/− pár
  „nullát” ad, és elhalványul.
- **Interaktív:** a diák beállítja a kiinduló számot és a műveletet (+/−, előjeles szám), a
  kisautó lépeget, a korongok közben párosodnak. Kivonásnál, ha nincs elég elvehető korong,
  a gép „nulla-párokat” tesz be: ez a kulcsmozzanat.
- **Lépések:** Hol találkozunk negatív számmal? · A számegyenes két iránya · Melyik a nagyobb?
  · Ellentett és abszolút érték · Összeadás: lépegetés · Kivonás: elengedett adósság · Szorzás:
  folytasd a mintát! · Összefoglalás.
- **Adatok:** −3 − (−5) = 2: 3 kékeszöld (−) korongból kellene 5-öt elvenni, ezért a gép 2
  nulla-párt tesz be; 5 kékeszöldet elveszünk, és marad 2 cinóber (+). −5 < −2; |−7| = 7;
  −(−3) = 3. A szorzás mintája: 3 · (−2) = −6, 2 · (−2) = −4, 1 · (−2) = −2, 0 · (−2) = 0,
  (−1) · (−2) = 2. Valós példa: a hazai melegrekord 41,9 °C (Kiskunhalas, 2007. július 20.),
  a hidegrekord −35 °C (Miskolc-Görömbölytapolca, 1940. február 16.), a különbség
  41,9 − (−35) = 76,9 °C *(ellenőrizendő: HungaroMet)*.
- **Építőkocka:** MatLine (pontok, ugrás-ívek, tükrözés, távolság), saját korongmodell.
- **Meglévő anyag:** PhET *Number Line: Integers* (saját ismeret, nincs ellenőrizve). Nálunk
  a korongmodell és a kivonás a hangsúlyos.

### 06 · `06-tortek` – Melyik a nagyobb: 2/3 vagy 3/4? – törtek, bővítés, egyszerűsítés

- **Tanulási cél:** A törtrész csak **egyenlő** részekből áll. A nevező megmondja, hány részre
  vágtuk az egészet, a számláló, hány részt veszünk belőle. A bővítés finomabb vágás, az
  egyszerűsítés durvább: a mennyiség nem változik. Összehasonlítás közös nevezővel. A tört
  szám, van helye a számegyenesen. Az egynél nagyobb tört vegyes számként is írható.
- **Kerettanterv:** „ábrázol törtrészeket, meghatároz törtrészeknek megfelelő törtszámokat;” ·
  „Törtek összehasonlítása, egyszerűsítés, bővítés” · „Különböző alakokban írt egyenlő törtek
  felismerése” · „két egyenlő nagyságú és alakú téglalap közül az egyik 4, a másik 3 egyenlő
  részre osztása; az elsőben a 3 negyed, a másodikban a 2 harmad színezése” · „Törtek
  szemléltetése és összehasonlítása párhuzamos számegyeneseken” · „Adott törtrészek
  ábrázolása tányérmodellel (2 különböző színű papírtányért egy sugár mentén bevágva
  összecsúsztatunk; az egyik tányéron például 12 egyenlő részt jelző beosztások vannak)”.
- **Tévhitek:** a nem egyenlő részek is „negyedek”. Nagyobb nevező, nagyobb tört (1/8 > 1/4).
  A 2/3 és a 3/4 egyenlő, mert „mindkettőből 1 hiányzik”. A fél pizza mindig ugyanannyi (de
  más egészből más). A tört nem szám, csak „rész”.
- **Kulcsvizuál:** a kerettanterv két téglalapja egymás alatt: 3 negyed és 2 harmad. A
  függőleges vágások egymásra csúsznak, és mindkét téglalap 12 részre bomlik: 9/12 és 8/12.
  A színes terület közben nem változik. Mellette a tányérmodell 12-es beosztással, alatta
  párhuzamos számegyenesek (törtfal).
- **Interaktív:** számláló- és nevezőcsúszka; modellváltó (kör, téglalap, szalag, tányér,
  számegyenes) ugyanarra a törtre; bővítőcsúszka (×1…×4): a vágások sűrűsödnek, a szín
  marad. A „melyik nagyobb” lépésben két törtet lehet beállítani.
- **Lépések:** Egyenlő részek! · Számláló és nevező · Ugyanannyi, más alakban (bővítés) ·
  Egyszerűsítés: durvább vágás · Melyik a nagyobb? · A „hiányzik 1” csapda · Törtek a
  számegyenesen · Egynél több: vegyes szám · Összefoglalás.
- **Adatok:** 2/3 = 8/12, 3/4 = 9/12, tehát 3/4 a nagyobb, 1/12-del. 6/8 = 3/4 = 9/12.
  Tányér, 12-es beosztás: 1/2 = 6/12, 1/3 = 4/12, 1/4 = 3/12, 1/6 = 2/12. A „hiányzik 1”
  ellenpéldája: 1/2 és 99/100 (mindkettőből 1 rész hiányzik, de nagyon különbözőek).
  7/4 = 1 3/4.
- **Építőkocka:** MatFrac (első), MatLine (párhuzamos számegyenesek), MatText.
- **Meglévő anyag:** PhET *Fractions: Intro* és *Fractions: Equality* (saját ismeret, nincs
  ellenőrizve). Nálunk a vágások egymásra csúszása és a tányérmodell az újdonság.

### 07 · `07-tortmuveletek` – Miért kell közös nevező? – műveletek törtekkel

- **Tanulási cél:** Azonos nevezőnél a darabokat egyszerűen összeadjuk. Különböző nevezőnél
  előbb közös vágást kell találni. Tört szorzása egész számmal ismételt összeadás. A tört
  törtrésze a „rész része” (területmodell). Az osztás azt kérdezi, hányszor fér bele, és ebből
  következik a reciprokkal szorzás. Mindig becsüljünk előre.
- **Kerettanterv:** „elvégzi az alapműveleteket a racionális számok körében, eredményét
  összeveti előzetes becslésével;” · „meghatározza konkrét számok reciprokát.” · „Alapműveletek
  értelmezése tárgyi tevékenységek, ábrázolások alapján” · „Reciprok fogalmának ismerete és
  alkalmazása” · „„21-ezés” dominókkal: […] a húzott és megfelelően fordított törteket
  összeadjuk; akinek az összege 2-nél több, kiesik; az győz, aki legjobban megközelíti a 2-t” ·
  fogalmak: „közös nevező, reciprok”.
- **Tévhitek:** 1/2 + 1/3 = 2/5 (összeadja a számlálókat és a nevezőket is). A szorzás mindig
  nagyobbít. Az osztás mindig kisebbít.
- **Kulcsvizuál:** az 1/2 és az 1/3 szalagja egymás mellett, majd mindkettő hatodokra bomlik
  (3/6 + 2/6), és egy szalagba csúszik: 5/6. A 2/5 csapda: a 2/5 szalagja *rövidebb*, mint
  az 1/2 egyedül. A szorzás területmodellje: egy négyzetben a 3/4 függőlegesen, a 2/3
  vízszintesen, a metszetük 6/12. Osztás: hány 1/4-es darab fér a 2 szalagjába?
- **Interaktív:** „21-ezés” dominókkal (determinisztikus keverés, „Új keverés” gomb). A diák
  dönt: húz vagy megáll, a dominót megfordíthatja. A kapott összeg szalagon és törtként is
  látszik, a célvonal a 2. Előtte „Tippelj!”: 1-nél nagyobb lesz az összeg?
- **Lépések:** Azonos nevező: darabok · A 2/5 csapda · Közös nevező: közös vágás · Szorzás
  egész számmal · A rész része · Hányszor fér bele? (osztás, reciprok) · 21-ezés törtekkel ·
  Összefoglalás.
- **Adatok:** 1/2 + 1/3 = 3/6 + 2/6 = 5/6; a hibás 2/5 = 0,4 < 0,5. 3 · 2/5 = 6/5 = 1 1/5.
  2/3 · 3/4 = 6/12 = 1/2. 2 : 1/4 = 8 = 2 · 4. 3/4 : 3/8 = 2. A 2/3 reciproka 3/2, az 5-é 1/5.
  Dominó: a számok 0–6, a 0 nem lehet nevező (a dominót úgy kell fordítani). Az üres–üres
  dominó kimarad.
- **Építőkocka:** MatFrac (szalag, területmodell), MatExpr (pontos racionális kiértékelés),
  MatText.

### 08 · `08-tizedes-tortek` – Hol van a 0,25? – tizedes törtek a számegyenesen ★

- **Tanulási cél:** A tizedesvessző utáni helyi értékek (tized, század, ezred) a számegyenes
  egymás utáni tízszeres nagyításai. Ebből következik az összehasonlítás (0,3 > 0,25). A
  tizedes tört és a közönséges tört kapcsolata. Van, ami sosem ér véget: az 1/3 és az 1/7
  szakaszosan ismétlődik. 10-zel szorozva a számjegyek egy hellyel balra lépnek (nem „nullát
  írunk a végére”). Tizedes törttel úgy osztunk, hogy mértékegységet váltunk. Kerekítés.
- **Kerettanterv:** „érti és alkalmazza a számok helyi értékes írásmódját tizedes törtek
  esetén;” · „megfelelteti egymásnak a racionális számok közönséges tört és tizedes tört
  alakját.” · „ismeri a racionális számokat, tud példát végtelen nem szakaszos tizedes
  törtre.” (7–8. előkészítés, csak érdekesség) · „Számok ábrázolása számegyenesen” · (8.)
  „gyakorlati feladatok megoldása során tizedes törtet legfeljebb kétjegyű egész számmal
  írásban oszt. A hányadost megbecsüli.” · „A tizedes törttel való osztás bemutatása és
  megtapasztalása mértékegység-átváltás segítségével”.
- **Tévhitek:** 0,25 > 0,3, mert 25 > 3. A 0,5 és a 0,50 különböző. 0,1 és 0,2 között nincs
  szám. 10-zel szorzáskor nullát írunk a végére (2,5 → 2,50). 1/3 = 0,3. A szorzás mindig
  nagyobbít (0,5 · 8 = 4).
- **Kulcsvizuál:** a 0–1 számegyenes. Egy „nagyító” keret ráközelít a [0,2; 0,3] szakaszra,
  és az alatta megjelenő második számegyenes ennek tízszeres nagyítása, a kettőt trapéz alakú
  vetítővonal köti össze. Még egy szint lefelé jönnek az ezredek. A 0,25 és a 0,3 helye
  egyszerre látszik mindkét szinten. Az 1/3 nagyításakor a „3” minden szinten újra
  megjelenik: a nagyítás sosem ér véget.
- **Interaktív:** görgetős vagy csúszkás folytonos nagyítás (1× → 1000×, logaritmikusan); a
  diák egy pontot húz, és a tizedes alakja élőben, helyi értékenként színezve látszik. A
  „Tört → tizedes” lépésben számláló- és nevezőcsúszka; az osztás jegyről jegyre íródik ki, a
  periódus ismétlődésekor a maradék kiemelődik.
- **Lépések:** Mi van 0 és 1 között? · Nagyíts tízszer: tizedek · Még tízszer: századok ·
  Melyik a nagyobb: 0,25 vagy 0,3? · Törtből tizedes tört · Soha nem ér véget · Szorzás és
  osztás 10-zel · Osztás tizedes törttel: válts mértékegységet! · Összefoglalás.
- **Adatok:** 0,25 = 1/4 < 0,3 = 3/10. 3/8 = 0,375. 1/3 = 0,333…; 2/3 = 0,666…, kerekítve
  0,67. 1/7 = 0,142857 142857… (6 jegyű periódus; a maradékok 1, 3, 2, 6, 4, 5 után újra 1).
  2,5 · 10 = 25; 2,5 : 10 = 0,25. 2,4 m : 0,3 m = 240 cm : 30 cm = 8. 7,8 : 12 = 0,65
  (becslés: 7,8 : 12 < 1, 8 : 12 ≈ 0,67). Nem szakaszos példa (érdekesség): 0,1010010001…
  (az 1-esek között egyre több 0 áll, ezért nincs ismétlődő szakasz).
- **Építőkocka:** **MatLine – referencialecke** (zoom, adaptív beosztás, kettős szint
  vetítővonallal, húzható pont), MatText.

### 09 · `09-aranyossag` – Mennyibe kerül 7 kifli? – egyenes és fordított arányosság ★

- **Tanulási cél:** Egy pontot két adat ad meg (sor és szék, betű és szám, x és y). Egyenes
  arányosságnál ha az egyik mennyiség 2-szeresére, 3-szorosára nő, a másik is, és a hányados
  állandó. A grafikon pontjai egy **origón átmenő** egyenesre esnek. Nem minden „együtt növő”
  mennyiség arányos. Fordított arányosságnál a szorzat állandó. Darabszámnál a pontokat nem
  kötjük össze.
- **Kerettanterv:** „felismeri az egyenes és a fordított arányosságot konkrét helyzetekben;” ·
  „felismeri és megalkotja az egyenes arányosság grafikonját;” · (11.) „tájékozódik a
  koordináta-rendszerben: koordinátáival adott pontot ábrázol, megadott pont koordinátáit
  leolvassa.” · „Tájékozódás térképen, nézőtéren, sakktáblán és a koordináta-rendszerben” ·
  „„Nem hiszem” páros játék: különböző grafikonok közül az egyenes arányosság grafikonjának
  kiválasztása” · (11.) javasolt tevékenység: „torpedó játék”.
- **Tévhitek:** ami együtt nő, az egyenesen arányos (az életkor és a testmagasság, a taxi
  alapdíjjal). Fordított arányosság = „az egyik nő, a másik csökken” (a 10 − x is ilyen, mégsem
  fordított arányosság). A grafikon pontjait mindig össze kell kötni. A koordináták sorrendje
  mindegy: (3; 2) = (2; 3).
- **Kulcsvizuál:** a mozijegy (sor, szék) és a sakktábla átúszik a koordináta-rendszerbe. A
  kifli-táblázat sorai egyenként pontként „repülnek” a rácsra, és egy origón átmenő egyenesre
  állnak. Mellette a taxi pontjai egy olyan egyenesre esnek, amely *nem* megy át az origón. A
  fordított arányosságot egy 60 km-es út mutatja: a sebesség–idő pontok görbére esnek, és
  mindegyikhez egy 60 egységnyi területű téglalap tartozik.
- **Interaktív:** torpedó (a hajók determinisztikus seedből; a diák koordinátát kattint,
  a lövés helyén (x; y) felirat). A kifli-darabszám csúszkája egy pontot mozgat a táblázatban
  és a grafikonon egyszerre. „Nem hiszem”: négy grafikonból kell kiválasztani az arányosat.
- **Lépések:** Két adat, egy hely · A koordináta-rendszer (torpedó) · Kifli: táblázat ·
  Pontok egy egyenesen, az origón át · Összekössük a pontokat? · Együtt nő, mégsem arányos ·
  Fordított arányosság · Összefoglalás.
- **Adatok:** egy kifli 80 Ft *(kitalált)*: 7 kifli 560 Ft, a hányados mindig 80 Ft/db. Sajt
  *(kitalált)* 400 Ft/10 dkg, folytonos, ezért itt összekötjük a pontokat. Taxi *(kitalált)*:
  1000 Ft alapdíj + 400 Ft/km: 1 km 1400 Ft, 2 km 1800 Ft – kétszer annyi út, de nem kétszer
  annyi pénz. 60 km-es út: 10 km/h → 6 óra, 15 → 4, 20 → 3, 30 → 2, 40 → 1,5, 60 → 1, a
  szorzat mindig 60 km. A pontok jelölése P(3; 2), pontosvesszővel.
- **Építőkocka:** **MatPlot – referencialecke** (rács, tengelyek, pont, vetítővonal, egyenes,
  görbe, táblázat ↔ pont szinkron, kattintás a rácson), MatText.

### 10 · `10-szazalek` – Visszakapod az árat? – százalékszámítás

- **Tanulási cél:** 1 % = 1 század. A fontos százalékok: 50 % (fele), 25 % (negyede), 10 %
  (tizede), 1 % (százada). A kettős szalagon egymás alatt áll a százalék és a mennyiség, így a
  „100 % = egész” bármilyen értékre átskálázható. Visszafelé is számolhatunk (mennyi a 100 %?).
  A 20 %-os drágítás és a 20 %-os kedvezmény nem oltja ki egymást.
- **Kerettanterv:** „ismeri a százalék fogalmát, gazdasági, pénzügyi és mindennapi élethez
  kötődő százalékszámítási feladatokat megold;” · „Századrész és százalék elnevezések
  párhuzamos használata gyakorlati helyzetekben” · „Törtrészkiszámítási feladatok az egyenesen
  arányos mennyiségek kapcsolatainak alkalmazásával” · „Fogyasztási cikkek címkéin,
  reklámokban, társadalomismereti és természetismereti tanulmányokban előforduló százalékos
  adatok értelmezése”.
- **Tévhitek:** 100 %-nál több nem lehet. Ha egy árat 20 %-kal emelnek, majd 20 %-kal
  csökkentenek, visszakapjuk az eredetit. Két 20 %-os kedvezmény 40 %. A 30 % mindig
  ugyanannyi (de mindig valaminek a 30 %-a).
- **Kulcsvizuál:** 10 × 10-es tábla, ahol 71 négyzet kékre színeződik: a Föld felszínének
  71 %-a víz. Utána a kettős szalag (MatLine kettős számegyenes): fent 0–100 %, lent
  0–5000 Ft. A csúszka egyszerre mutatja a két skálát, a 120 % kinyúlik a szalagból.
- **Interaktív:** a diák beállítja az alapot (Ft) és a százalékot, a két skála szinkronban
  mozog. „Akció-gép”: először +20 %, aztán −20 %, a végén az eredmény ott áll az eredeti
  mellett, és látszik a 4 % különbség. Ez elé jön a „Tippelj!”.
- **Lépések:** Mit jelent a 71 %? · Század = százalék · A fontos százalékok · Kettős szalag:
  százalék és forint · Mennyi a 100 %? · Akció! · Fel 20 %, le 20 % – visszakapod? ·
  Összefoglalás.
- **Adatok:** 1 % = 1/100 = 0,01. A Föld felszínének kb. 71 %-át víz borítja *(ellenőrizendő:
  a gyakran idézett érték 70,8 %)*. 5000 Ft 20 %-a 1000 Ft. 5000 Ft + 20 % = 6000 Ft,
  6000 Ft − 20 % = 4800 Ft, ez az eredeti 96 %-a. Két 20 %-os kedvezmény egymás után:
  0,8 · 0,8 = 0,64, vagyis 36 % kedvezmény, nem 40 %. Visszafelé: 30 % = 600 Ft →
  10 % = 200 Ft → 100 % = 2000 Ft. Az árak kitaláltak.
- **Építőkocka:** MatFrac (100-as tábla), MatLine (kettős számegyenes).

### 11 · `11-szoveges-feladatok` – Mit gondoltam? – szakaszos ábra, visszafelé gondolkodás, mérlegelv

- **Tanulási cél:** A szöveg modellje egy ábra. Szakaszos ábrán a „6-tal több” egy
  hosszabb szakasz. Visszafelé gondolkodásnál a fordított műveleteket **fordított
  sorrendben** végezzük. A mérlegelv: ha mindkét oldallal ugyanazt tesszük, megmarad az
  egyensúly. A végén ellenőrzünk (visszahelyettesítés) és becslünk.
- **Kerettanterv:** „egyismeretlenes elsőfokú egyenletet lebontogatással és mérlegelvvel
  megold;” · „különböző szövegekhez megfelelő modelleket készít;” · „matematikából, más
  tantárgyakból és a mindennapi életből vett egyszerű szöveges feladatokat következtetéssel
  vagy egyenlettel megold;” · „megoldását ellenőrzi.” · „Matematikai tartalmú egyszerű
  szöveges feladatok megoldása különféle módszerekkel, például szakaszos ábrázolással,
  visszafelé gondolkodással” · „Törtrészek összehasonlítását tartalmazó szöveges feladatokban
  a törtrészek szemléltetése szakaszokkal” · „„Gondoltam egy számot” játék”.
- **Tévhitek:** a kulcsszó dönt („több” → összeadás). Visszafelé ugyanabban a sorrendben kell
  haladni. Elég a mérleg egyik oldalán változtatni. Ha kijött egy szám, kész vagyunk (nincs
  ellenőrzés).
- **Kulcsvizuál:** a „gondoltam egy számot” gép csővezeték (×3, +4), amelyen a szám
  végigmegy, aztán visszafelé is (−4, :3). A szakaszos ábrán Anna szalagja Béláé + 6. Kétkarú
  mérleg: bal oldalon 3 doboz (x) és 4 egységsúly, jobb oldalon 19 egységsúly. Ha csak az
  egyik oldalról vesznek le, a mérleg *fizikailag billen* (egyszerűsített forgatónyomaték,
  csillapított beállás zárt képlettel).
- **Interaktív:** mérleg-gombok: „Vegyél le 1-et mindkét oldalról”, „Csak bal oldalról”,
  „Oszd 3 egyenlő részre”. A gondolt-szám-gépbe a diák saját számot ír (csúszka 1–20), és a
  gép visszafejti.
- **Lépések:** Gondoltam egy számot · Visszafelé: fordított sorrend · Szakaszos ábra: „6-tal
  több” · A kulcsszó-csapda · Törtrész szakaszokkal · A mérleg egyensúlya · Mérlegelv:
  mindkét oldalon ugyanazt · Ellenőrizz! · Összefoglalás.
- **Adatok:** ×3, +4 → 19; visszafelé (19 − 4) : 3 = 5. Mérleg: 3x + 4 = 19 → 3x = 15 →
  x = 5; ellenőrzés: 3 · 5 + 4 = 19. Két testvérnek együtt 30 matricája van, Annának 6-tal
  több: (30 − 6) : 2 = 12 (Béla), 12 + 6 = 18 (Anna). Kulcsszó-csapda: Annának 23 matricája
  van, 5-tel több, mint Bélának, tehát Bélának 23 − 5 = 18. Peti a pénze 2/5-ét elköltötte,
  maradt 1200 Ft: 3/5 = 1200 Ft → 1/5 = 400 Ft → az egész 2000 Ft. A nevek és az összegek
  kitaláltak.
- **Építőkocka:** Mérleg (első; a Matek 9–10 egyenleteihez is), MatFrac (szakaszos ábra:
  `MatFrac.bar`), MatText.

### 12 · `12-sorozatok` – Hány gyufa kell a 100. házhoz? – sorozatok és szabályok

- **Tanulási cél:** A sorozatot szabály szerint folytatjuk. Néhány tagból szabályt
  keresünk, és egy kezdethez **több szabály** is illeszkedhet. Az ábra, a táblázat és a
  koordináta-rendszer pontjai ugyanazt mutatják. Az n-edik tag szabálya: hogyan kapjuk meg a
  sorszámból (megfeleltetés, a függvény előkészítése). Az állandó növekmény egyenesre eső
  pontokat ad, de ez nem mindig arányosság.
- **Kerettanterv:** „sorozatokat adott szabály alapján folytat;” · „néhány tagjával adott
  sorozat esetén felismer és megfogalmaz képzési szabályt.” · „Adott sorozat esetén legalább
  egy szabály felismerése és megfogalmazása” · „A tanár által megkezdett sorozat minél több
  szabályának gyűjtése csoportmunkában” · (11.) „konkrét halmazok elemei között megfeleltetést
  hoz létre;” · „A matematikából és a mindennapi életből vett megfeleltetések legalább egy
  lehetséges szabályának megadása”.
- **Tévhitek:** egy sorozatnak csak egy szabálya lehet. A 100. tag a 25. tag négyszerese
  (arányossági gondolkodás). Ha a pontok egyenesre esnek, akkor egyenes arányosság.
- **Kulcsvizuál:** gyufaszálas házsor épül, házanként 5 új gyufával. Mellette a táblázat
  (házak száma → gyufák száma), alatta a pontok a koordináta-rendszerben, amelyek egy
  egyenesre esnek, de az 1-nél metszik a függőleges tengelyt: ez az „első fal”. Az 1, 2, 4
  sorozat két folytatása kétfelé ágazik (8 vagy 7). A háromszögszámok pontrácsai nőnek.
- **Interaktív:** házszám-csúszka (1–100), a sor „kicsinyedik”, hogy elférjen. A 25 → 100
  „×4 csapda” gombja megmutatja a 4 · 126 = 504-et az igazi 501 mellett. A diák a következő
  tagot tippeli, és a gép két szabállyal is folytatja.
- **Lépések:** Mi jön ezután? · Gyufaházak · Mennyivel nő? (táblázat) · A 100. ház (szabály
  és csapda) · Pontok a koordináta-rendszerben · Egy kezdet, két szabály · Háromszögszámok ·
  Összefoglalás.
- **Adatok:** házanként egy négyzet és egy tető; a szomszédos házak falat osztanak. 1 ház:
  6 gyufa; minden további ház +5; n ház: 5 · n + 1. 2 ház: 11, 3 ház: 16, 25 ház: 126,
  100 ház: 501 (és nem 4 · 126 = 504). 1, 2, 4, …: duplázással 8, 16; „+1, +2, +3” szabállyal
  7, 11. Háromszögszámok: 1, 3, 6, 10, 15 (a növekmény 2, 3, 4, 5).
- **Építőkocka:** MatPlot (pontok, ugyanaz a rács, mint a 09-ben), saját gyufa-rajzoló.

### 13 · `13-terulet` – Miért fele a háromszög a paralelogrammának? – kerület, terület, átdarabolás

- **Tanulási cél:** A kerület a határ hossza, a terület a lefedett rész. A terület
  egységnégyzetek száma, a téglalapé a · b. Azonos kerületű téglalapok területe különböző
  lehet. 1 m² = 10 000 cm². A paralelogramma téglalappá darabolható át: alap · magasság (és nem
  oldal · oldal). A háromszög egy fél paralelogramma. Bármely sokszög darabokra vágható.
- **Kerettanterv:** „meghatározza háromszögek és speciális négyszögek kerületét, területét;”
  (a speciális négyszögek a 7–8. anyaga, itt csak a paralelogramma) · „Téglalap, négyzet
  kerületének, területének kiszámítása” · „Sokszögek területének meghatározása átdarabolással”
  · „Papírból készült sokszögek átdarabolásának bemutatása, majd egyéni kipróbálás és a saját
  megoldások összehasonlítása” · (9.) „idő, tömeg, hosszúság, terület, térfogat és űrtartalom
  mértékegységeket átvált helyi értékes gondolkodás alapján, gyakorlati célszerűség szerint.”
- **Tévhitek:** a nagyobb kerülethez nagyobb terület tartozik. A paralelogramma területe
  oldal · oldal. 1 m² = 100 cm². Két alakzat területét csak egyforma alaknál lehet
  összehasonlítani.
- **Kulcsvizuál:** 24 m kerítés (egy zárt lánc) téglalapokat fog körbe, a terület élő
  egységnégyzet-számmal, és a négyzetnél a legnagyobb. A paralelogrammáról levágódik egy
  háromszög, és átcsúszik a másik oldalra. A háromszöget a tükörképe egészíti ki
  paralelogrammává. 1 m²-es négyzet, rajta 100 × 100 cm²-es rács, nagyításra.
- **Interaktív:** a téglalap sarka húzható (a kerület rögzített 24 m, egész méterekre ugrik).
  A paralelogramma felső oldala oldalra húzható: a ferdeség változik, a terület (alap ·
  magasság) nem. A „Darabold!” gombbal egy L alakú sokszög két téglalapra esik szét.
- **Lépések:** Kerítés vagy kert? · Számold a négyzeteket! · Ugyanannyi kerítés, más kert ·
  1 m² hány cm²? · A ferde téglalap: paralelogramma · A háromszög: fél paralelogramma ·
  Darabold szét! · Összefoglalás.
- **Adatok:** 24 m kerület: 1 × 11 = 11 m², 2 × 10 = 20, 3 × 9 = 27, 4 × 8 = 32, 5 × 7 = 35,
  6 × 6 = 36 m². 1 m² = 100 dm² = 10 000 cm². Paralelogramma: alap 8, ferde oldal 5,
  vízszintes eltolás 3, ezért a magasság 4 (3–4–5); T = 8 · 4 = 32, és nem 8 · 5 = 40.
  Háromszög: alap 8, magasság 4 → 16. Osztályterem 8 m × 6 m = 48 m² *(kitalált)*.
- **Építőkocka:** MatGeo (sokszög, vágás, mozgatás, egységrács), MatText.
- **Meglévő anyag:** PhET *Area Builder* (saját ismeret, nincs ellenőrizve).

### 14 · `14-haromszogek` – Miért mindig 180°? – szögek, háromszögek, négyszögek ★

- **Tanulási cél:** A szög forgás (nyíló ajtó), a nagysága nem függ a szárak hosszától.
  Szögfajták, szögmérés fokban. Három szakaszból csak akkor lesz háromszög, ha bármely kettő
  összege nagyobb a harmadiknál. A háromszögek csoportosítása oldalak és szögek szerint; az
  egyenlő szárú háromszög tengelyesen szimmetrikus. A belső szögek összege **minden**
  háromszögben 180°. Külső szög. A négyszög belső szögeinek összege 360°, mert egy átló két
  háromszögre vágja. Minden négyzet téglalap.
- **Kerettanterv:** „ismeri a háromszögek tulajdonságait: belső és külső szögek összege,
  háromszög-egyenlőtlenség.” · „csoportosítja a háromszögeket szögeik és oldalaik szerint;” ·
  „ismeri a tengelyesen szimmetrikus háromszöget;” · „Téglalap és négyzet tulajdonságainak
  ismerete, alkalmazása” · „ismeri a négyszögek tulajdonságait: belső és külső szögek összege,
  konvex és konkáv közti különbség, átló fogalma;” (részben) · (13.) „síkbeli tartományok
  közül kiválasztja a szögtartományokat, nagyság szerint összehasonlítja, méri, csoportosítja
  azokat.” · „Papír háromszög sarkainak levágása és egymás mellé helyezése” · „Szívószálból,
  hurkapálcából háromszög készítése (lehetséges és lehetetlen helyzetek)”.
- **Tévhitek:** a hosszabb szárú szög nagyobb. Bármely három pálcából háromszög lesz. A
  nagyobb háromszög szögösszege is nagyobb. Egy háromszögnek lehet két derékszöge. A négyzet
  nem téglalap.
- **Kulcsvizuál:** a háromszög csúcsai húzhatók, a három szög íve színes. A „Tépd le!”
  gombra a három sarok letépett papírként (cakkos szélű körcikk) egy egyenes mentén egymás
  mellé fordul, és egyenesszöget alkot. A szögek összege közben élőben látszik, bármilyen az
  alak. Három pálca (csúszkával állítható hossz) a két végén csuklósan forog: vagy összeér a
  csúcsuk, vagy nem.
- **Interaktív:** csúcshúzás. A háromszög „neve” (hegyes-/derék-/tompaszögű; egyenlő szárú,
  szabályos, általános) élőben változik, a derékszögre és az egyenlő oldalakra rá lehet
  ugrani. Szögmérő a szög csúcsára húzható. Pálcacsúszkák. Négyszögnél az átló ki-be
  kapcsolható.
- **Lépések:** Mi a szög? · Mérjük meg! · Három pálca: mikor záródik? · Oldalak szerint ·
  Szögek szerint · Tépd le a sarkokat: 180° · A külső szög · Négyszög: 360°, és a négyzet is
  téglalap · Összefoglalás.
- **Adatok:** szögfajták: hegyesszög 0° és 90° között, derékszög 90°, tompaszög 90° és 180°
  között, egyenesszög 180°, homorú szög 180° és 360° között, teljesszög 360°. 1° = 60′.
  Pálcák: 3, 4, 8 cm → 3 + 4 < 8, nem záródik; 3, 4, 7 → 3 + 4 = 7, a háromszög „lelapul”
  egy szakasszá; 3, 4, 5 → derékszögű háromszög. Példa: 50° + 60° + 70° = 180°; a 70°-os
  szög melletti külső szög 110° = 50° + 60°; a külső szögek összege 360°. Négyszög:
  2 · 180° = 360°.
- **Építőkocka:** **MatGeo – referencialecke** (húzható pontok kényszerekkel, szakasz, szög
  íve és mérése, derékszögjel, sokszög, egyenlőségjelek az oldalakon, szögmérő, darab
  forgatása/mozgatása), MatText.

### 15 · `15-tukrozes-szerkesztes` – Honnan tudja a körző, hol a közép? – tengelyes tükrözés, szerkesztések

- **Tanulási cél:** A tengelyes tükrözésnél a pont és a képe egyenlő távol van a tengelytől,
  és az összekötő szakaszuk merőleges a tengelyre. A tükörkép körüljárása fordított. A
  szimmetrikus alakzat önmaga tükörképe. A szakaszfelező merőleges azoknak a pontoknak a
  vonala, amelyek A-tól és B-től egyenlő távol vannak, ezért találja meg két egyforma körív a
  felezőpontot. Szögfelező, merőleges és párhuzamos szerkesztése. Előbb vázlat, utána
  szerkesztés.
- **Kerettanterv:** „megszerkeszti alakzatok tengelyes és középpontos tükörképét;” (itt csak a
  tengelyes; a középpontos a 7–8. anyaga) · „ismeri az alapszerkesztéseket: szakaszfelező
  merőlegest, szögfelezőt, merőleges és párhuzamos egyeneseket szerkeszt, szöget másol.” ·
  „a szerkesztéshez tervet, előzetes ábrát készít;” · „felismeri a síkban az egybevágó
  alakzatokat;” · „ismer és használ dinamikus geometriai szoftvereket, tisztában van
  alkalmazási lehetőségeikkel.” · „Tengelyes tükrözésen alapuló szerkesztések elvégzése saját
  eszközökkel (körző, egyélű vonalzó)”.
- **Tévhitek:** a tükrözés „átteszi” az alakzatot a másik oldalra (eltolás, ugyanazzal a
  körüljárással). Ferde tengelynél vízszintesen tükrözünk. A körző nyílása mindegy (pedig a
  két ív sugara egyenlő, és nagyobb, mint AB fele). A szerkesztésnél szabad a vonalzó
  centiméter-beosztásával mérni.
- **Kulcsvizuál:** a papír a tengely mentén összehajlik (perspektivikus hajtás), a festék
  átnyomódik: ez a tükörkép. A szakaszfelezésnél egy húzható P pont mozog: ha PA = PB (élő
  mérőszalagok), P cinóberre vált, és nyomot hagy, amelyből kirajzolódik a merőleges egyenes.
  Utána a körző animálva rajzolja meg a két ívet, a metszéspontokon át húzott egyenes pedig
  pontosan a nyomra esik.
- **Interaktív:** a tükrözendő alakzat és a tengely is húzható és forgatható; a pont–kép
  párokat szaggatott merőleges köti össze. Körző-csúszka (sugár): ha túl kicsi, az ívek nem
  metszik egymást, és ez ki is derül. A P pont húzása. A szerkesztés lépései léptethetők.
- **Lépések:** Hajtsd össze! · A tükrözés szabálya · Ferde tengely, fordított körüljárás ·
  Szimmetrikus alakzatok · Egyenlő távol A-tól és B-től · A körző trükkje: szakaszfelező
  merőleges · Szögfelező · Merőleges és párhuzamos · Összefoglalás.
- **Adatok:** nincs mért tényadat; a szerkesztések geometriája a kódban van. A `.md`
  adatai: a kiinduló pontok koordinátái `pont` típusként (5. fejezet), hogy a tanár más
  példát is beállíthasson. Szöveges állítások: AB = 6 egység esetén a körző sugara
  > 3 egység kell; az ívek metszéspontjai a felezőmerőlegesen, a tengelytől egyenlő távol
  vannak.
- **Építőkocka:** **MatCon** (első; MatGeo-ra épül), MatText.
- **Meglévő anyag:** GeoGebra (a kerettanterv által kért „dinamikus geometriai szoftver”). A
  lecke záró megjegyzése ajánlja: GeoGebra Classic / Geometria, ingyenes, magyar felülettel
  (saját ismeret, nincs ellenőrizve).

### 16 · `16-testek` – Melyik hálóból lesz kocka? – testek, háló, felszín, térfogat

- **Tanulási cél:** A kockának 8 csúcsa, 12 éle és 6 lapja van; lapátló, testátló. Nézetek
  (elöl-, felül-, oldalnézet). A háló a test kiterített felülete. A kockának 11 különböző
  hálója van, de nem minden 6 négyzetből álló alakzat háló. A felszín a háló területe. A
  térfogat az egységkockák száma, a téglatesté a · b · c. 1 dm³ = 1 liter = 1000 cm³. A
  kétszer akkora élű kocka térfogata 8-szoros.
- **Kerettanterv:** „a kocka, a téglatest, a hasáb és a gúla hálóját elkészíti;” · „testeket
  épít képek, nézetek, alaprajzok, hálók alapján;” · „ismeri a kocka, a téglatest, a hasáb és a
  gúla következő tulajdonságait: határoló lapok típusa, száma, egymáshoz viszonyított helyzete;
  csúcsok, élek száma; lapátló, testátló;” · (13.) „egyenes hasáb, téglatest, kocka alakú
  tárgyak felszínét és térfogatát méréssel megadja, egyenes hasáb felszínét és térfogatát
  képlet segítségével kiszámolja; a képleteket megalapozó összefüggéseket érti.” · (13.)
  „Téglatest, kocka alakú üreges test „feltöltése” egységkockákkal (becslés, mérés,
  számolás)” · (4.) „„Nem hiszem” páros játék: […] két liter tej belefér egy 1 dm élű kocka
  alakú edénybe”.
- **Tévhitek:** bármely 6 négyzetből álló alakzat kockaháló. A kockának 6 éle van. Kétszer
  akkora kocka, kétszer akkora térfogat. A felszín és a térfogat ugyanaz („mekkora”). 1 dm³ =
  10 cm³.
- **Kulcsvizuál:** a forgatható kocka csúcsai, élei és lapjai sorban felvillannak a
  számlálóval. A háló a síkban fekszik, a lapok a csuklóélek körül egyenként felhajlanak és
  összezárnak. Hibás hálónál két lap *ütközik* (piros villanás), és egy lap nyitva marad. A
  doboz rétegenként megtelik egységkockákkal. Az 1 dm-es kockába liternyi víz folyik, a
  második liter kicsordul.
- **Interaktív:** a kocka egérrel forgatható (rögzített kezdőnézet: `enter`). Hálóválasztó:
  8–10 hexominó, köztük a 11 háló egy része és néhány nem-háló. A diák előbb tippel („kocka
  lesz?”), aztán a gombra a háló összehajtódik. Élhossz-csúszkák (téglatest a, b, c: 1–6), a
  felszín és a térfogat élőben. Kockaépítmény nézeteinek váltása.
- **Lépések:** Csúcsok, élek, lapok, átlók · Nézetek: elölről, felülről, oldalról ·
  Kiterítjük: a háló · Melyikből lesz kocka? · Felszín: a háló területe · Megtöltjük:
  térfogat · 1 liter = 1 dm³ · Kétszer akkora kocka · Összefoglalás.
- **Adatok:** kocka: 8 csúcs, 12 él, 6 lap; 12 lapátló (laponként 2), 4 testátló. 11 kockaháló
  (a 35 hexominóból). Téglatest 3 × 4 × 5 cm: V = 60 cm³, A = 2 · (12 + 15 + 20) = 94 cm².
  2 cm élű kocka: V = 8 cm³, A = 24 cm²; 4 cm élű: V = 64 cm³ (8-szoros), A = 96 cm²
  (4-szeres). 1 dm³ = 1000 cm³ = 1 l, tehát 2 liter tej nem fér bele egy 1 dm élű kockába.
- **Építőkocka:** **Mat3D** (első: test, forgatás, takart él, háló hajtogatása, ütközés-
  vizsgálat, egységkockák, nézetek), MatText.

### 17 · `17-statisztika` – Mit mutat az átlag? – diagramok, átlag, módusz, medián

- **Tanulási cél:** Az adatokból táblázat, abból diagram lesz. Az oszlopdiagram
  összehasonlít, a kördiagram a rész–egész arányt mutatja, a vonaldiagram az időbeli
  változást. Ugyanaz az adat oszlop- és kördiagramon is ábrázolható. Az átlag a
  „kiegyenlített” érték. A módusz a leggyakoribb adat, a medián a középső. Egy kiugró adat az
  átlagot elhúzza, a mediánt alig.
- **Kerettanterv:** „értelmezi a táblázatok adatait, az adatoknak megfelelő ábrázolási módot
  kiválasztja, és az ábrát elkészíti;” · „különböző típusú diagramokat megfeleltet egymásnak;” ·
  „konkrét adatsor esetén átlagot számol, megállapítja a leggyakoribb adatot (módusz), a középső
  adatot (medián), és ezeket összehasonlítja.” · „Azonos adathalmazon alapuló kördiagram és
  oszlopdiagram összehasonlítása becslés alapján kisméretű minta esetén” · „A táblázatok
  adatainak értelmezése és ábrázolása (oszlopdiagram, kördiagram, vonaldiagram, pontdiagram)
  kisméretű mintán”.
- **Tévhitek:** az átlag mindig egy létező adat. Az átlag mindig a „tipikus” érték (kiugró
  adatnál nem). A kördiagramon is lehet bármilyen adat (időbeli változás nem). A medián a
  rendezetlen lista közepe.
- **Kulcsvizuál:** a strigulák táblázattá rendeződnek, az oszlopok felnőnek. Az oszlopok
  „meghajlanak”, és körcikkekké tekerednek egy körben (morf: minden oszlop a saját cikkévé
  válik). Az átlagot kockákból rakott tornyok mutatják, a kockák a magasabbakról az
  alacsonyabbakra vándorolnak, amíg ki nem egyenlítődnek. A medián a sorba rendezett
  kártyasor közepén áll.
- **Interaktív:** az adatsor (a .md-ből, `lista` típus) bármely eleme húzható. Az átlag, a
  módusz és a medián függőleges vonalai élőben mozognak. A „kiugró adat” gomb a 4-et 12-re
  cseréli, és vissza. Váltógomb: oszlop ↔ kör.
- **Lépések:** Hogyan jöttök iskolába? · Oszlopdiagram · Ugyanez kördiagramon · Melyiket
  mikor? · Az átlag: kiegyenlítjük a tornyokat · Módusz és medián · Egy kiugró adat ·
  Összefoglalás.
- **Adatok** *(kitalált osztályfelmérés)*: 24 diák; gyalog 9, busz 6, autó 6, bicikli 3. Körcikkek:
  135°, 90°, 90°, 45° (37,5 %, 25 %, 25 %, 12,5 %; a busz pontosan negyed kör). Tornyok
  3, 5, 4, 8 → átlag 20 : 4 = 5. Elolvasott könyvek (9 diák): 0, 1, 1, 2, 2, 2, 3, 4, 12 →
  átlag 27 : 9 = 3, medián 2, módusz 2; a 12 nélkül (8 adat) átlag 15 : 8 = 1,875, medián 2.
- **Építőkocka:** **MatChart** (első: oszlop, kör, vonal, pont, oszlop ↔ kör morf, strigula,
  kockatornyok), MatText.
- **Meglévő anyag:** PhET *Mean: Share and Balance* (saját ismeret, nincs ellenőrizve).

### 18 · `18-valoszinuseg` – Melyik összeg a legszerencsésebb? – valószínűségi kísérletek

- **Tanulási cél:** Egy esemény lehet biztos, lehetséges (de nem biztos) vagy lehetetlen. Az
  összes eset rendszerezve: ágrajz (3 korong: 8 eset), táblázat (2 kocka: 36 eset). A
  gyakoriság azt mutatja, hányszor történt meg valami, a relatív gyakoriság azt, hogy az
  összes kísérlet hányad részében. Sok kísérletnél a relatív gyakoriság stabilizálódik. A
  kocka nem emlékszik. A lépegetős játékban a stratégia a „nagyobb eséllyel lehetséges”
  számok választása.
- **Kerettanterv:** „valószínűségi játékokat, kísérleteket végez, ennek során az adatokat
  tervszerűen gyűjti, rendezi és ábrázolja digitálisan is;” · „valószínűségi játékokban érti a
  lehetséges kimeneteleket, játékában stratégiát követ;” · „ismeri a gyakoriság és a relatív
  gyakoriság fogalmát. Ismereteit felhasználja a „lehetetlen”, a „biztos” és a „kisebb/nagyobb
  eséllyel lehetséges” kijelentések megfogalmazásánál.” · (2.) „összeszámlálási feladatok
  megoldása során alkalmazza az összes eset áttekintéséhez szükséges módszereket.” · „Az összes
  eset előállítása során rendszerezési sémák használata: táblázat, ágrajz, szisztematikus
  felsorolás” · „(például 3 korongot feldobunk) […] (például mindhárom kék; több a kék, mint a
  piros; nincs piros; van kék; van két egyforma szín; egyik színből sincs legalább kettő)” ·
  „10 korongot feldobunk; a számegyenesen a 0-ból indulva annyit lépünk pozitív irányba, ahány
  pirosat dobtunk, majd innen annyit negatív irányba, ahány kéket; tippeld meg, hova jutsz;
  válassz 4 számkártyát, nyersz, ha ezek valamelyikére jutsz”.
- **Tévhitek:** két kockánál minden összeg egyformán valószínű. 5 fej után nagyobb az esély
  az írásra. A „lehetséges” 50 %-ot jelent. 10 dobásból biztosan lehet következtetni. „Van két
  egyforma szín” csak lehetséges (pedig 3 korongnál biztos).
- **Kulcsvizuál:** a 3 korong ágrajza ágról ágra kinő (8 levél), az eseménykártyák a
  hozzájuk illő leveleket kiemelik. A 6 × 6-os táblázat átlói azonos összegeket színeznek,
  a 7-es átló a leghosszabb. A szimuláció alatt a relatív gyakoriság grafikonja (log-skálás
  vízszintes tengely) a kísérletek számával lecsendesedik.
- **Interaktív:** „Dobj 1-et / 10-et / 100-at / 10 000-et”. Determinisztikus seed, „Új
  kísérlet” gomb. Az oszlopdiagramon (MatChart) a gyakoriság, alatta a relatív gyakoriság.
  Lépegetős játék: a diák 4 számkártyát választ a számegyenesen (−10…10), aztán 100 kör
  szimuláció. Kiderül, hogy a páratlan számok lehetetlenek, a 0 és a ±2 a legjobbak.
- **Lépések:** Biztos, lehetséges, lehetetlen · Három korong: az összes eset ágrajzon ·
  Melyik a jó kártya? · Dobjunk sokszor! · A kocka nem emlékszik · Két kocka: 36 eset ·
  Szimuláció: a 7 nyer · Lépegetés: válassz 4 számot! · Összefoglalás.
- **Adatok:** 3 korong (kék/piros): 2 · 2 · 2 = 8 eset. Mindhárom kék: 1/8; nincs piros: 1/8;
  van kék: 7/8; több a kék, mint a piros: 4/8; „van két egyforma szín”: 8/8, **biztos**;
  „egyik színből sincs legalább kettő”: **lehetetlen**. Két kocka: 36 eset; összeg 7: 6
  eset; 6 és 8: 5–5; 2 és 12: 1–1. 13: lehetetlen; ≤ 12: biztos; a szorzat 40: lehetetlen.
  10 korong: a végpont = 2 · (pirosak száma) − 10, mindig páros. Esetszámok (1024-ből):
  0 → 252, ±2 → 210, ±4 → 120, ±6 → 45, ±8 → 10, ±10 → 1. Legjobb 4 kártya: 0, 2, −2 és 4
  (vagy −4): 792/1024 ≈ 77 %.
- **Építőkocka:** **MatRand** (első: kocka, érme, korong, urna, ágrajz, esettáblázat,
  szimuláció zárt alakban), MatChart (oszlop), MatLine (lépegetés), MatPlot (relatív
  gyakoriság).
- **Meglévő anyag:** PhET *Plinko Probability* (saját ismeret, nincs ellenőrizve). Ott a
  binomiális eloszlás golyókkal jelenik meg, nálunk a lépegetős játékban.

---

## 4. Építőkockák és gyártási sorrend

### Modulok

| Modul | Mit tud | Leckék | Első megépítés | Matek 9–10 |
|---|---|---|---|---|
| **MatText** · matematikai szöveg | álló tört, vegyes szám, kitevő, index, műveleti jelek a vásznon (`L.tx`-re épül, kulccsal); magyar számformátum; **pontos racionális aritmetika (`MatQ`)**; `.md`-adat konzisztencia-ellenőrzés; a panel tört-CSS-e | mind | **előkészítő ügynök** (`shared/matek/mtext.js`) | mind |
| **MatLine** · számegyenes | folytonos zoom (log), adaptív beosztás (1–2–5 · 10ᵏ), tizedes/tört/egész feliratok, húzható pont, ugrás-ív, szakasz zárt/nyitott véggel, tükrözés, távolság-kapocs, kettős számegyenes, párhuzamos számegyenesek, két szint vetítővonallal, felcsavarás | 01, 03, 05, 06, 08, 10, 18 | **08 ★** | intervallumok, számhalmazok, egyenlőtlenségek |
| **MatPlot** · koordináta-rendszer | rács, tengelyek, P(x; y) feliratok, vetítővonal, húzható pont, egyenes, függvénygörbe (szakadással), értéktáblázat ↔ pont szinkron, kattintás a rácson | 09, 12, 18 | **09 ★** | függvények, transzformációk, egyenletrendszer |
| **MatGeo** · síkgeometria | húzható pontok kényszerekkel, szakasz/egyenes/félegyenes, kör/ív, szög íve és mért értéke, derékszögjel, egyenlőségjelek, sokszög, vágás és mozgatás (átdarabolás), tükrözés/forgatás/eltolás, metszéspontok, szögmérő | 04, 13, 14, 15 | **14 ★** | háromszögek, négyszögek, kör, transzformációk |
| **MatCon** · szerkesztés | körző- és vonalzó-animáció, lépéssor-lejátszó (zárt idő), kész receptek: felezőmerőleges, szögfelező, merőleges, párhuzamos, szögmásolás, tükrözés | 15 | 15 | szerkesztések (20 óra!) |
| **MatFrac** · törtmodellek | kör, téglalap, szalag, csokirács, tányér; bővítés-animáció; törtfal; szorzás-területmodell; szakaszos ábra (`bar`); 100-as tábla | 06, 07, 10, 11 | 06 | (százalék, szöveges feladat) |
| **MatExpr** · kifejezésfa | kifejezés elemzése a `.md`-ből, fa-elrendezés, alulról felfelé kiértékelés animálva, „balról jobbra” számológép-mód, pontos (racionális) eredmény | 04, 07 | 04 | betűs kifejezések, egyenletek |
| **Mat3D** · testek | ortografikus (opcionálisan enyhén perspektivikus) vetítés, forgatás, festő-algoritmus, takart él szaggatva, kocka/téglatest/hasáb/gúla, háló hajtogatása csuklóélek körül, ütközésvizsgálat, egységkockák, nézetek | 03, 16 | 16 | – (11–12. térgeometria, fizika/kémia rácsok) |
| **MatRand** · véletlen kísérlet | érme, kocka, korong, urna, szerencsekerék seedből; az n-edik kísérlet zárt alakban; gyakoriság-tábla; ágrajz; esettáblázat | 18 | 18 | valószínűség, kombinatorika (ágrajz) |
| **MatChart** · diagramok | oszlop, kör, vonal, pont; oszlop ↔ kör morf; strigula; kockatornyok (átlag); átlag/medián/módusz jelzővonal | 17, 18 | 17 | leíró statisztika |
| **MatVenn** · halmazábra | 2–3 halmaz, alaphalmaz, tartomány-kiemelés kitöltéssel és sraffozással, elemek ütközésmentes elhelyezése és repülése | 01 | 01 | halmazok, logika |
| **Mérleg** (`MatBalance`) | kétkarú mérleg dobozokkal és súlyokkal, billenés csillapított zárt képlettel, „mindkét oldalról” műveletek | 11 | 11 | elsőfokú egyenletek |

Saját, nem általánosított elemek: pénztárgép (02), négyzetrács-átrendező (03), korongmodell
(05), gyufaház (12).

### API-vázlatok

A modulok névtere `Mat…`, minden függvény első paramétere az `L` lecke-objektum. Minden
vászonszöveg `{s, k}` párként érkezik (szöveg + md-kulcs), és `L.tx`/`L.pill`/`MatText.draw`
írja ki, így a QA és a review mód látja. Az állapot zárt képletű: minden rajzoló a `t`
(0..1) fázist vagy az `L.st`-t kapja, nem halmoz.

```js
/* MatText + MatQ – shared/matek/mtext.js (előkészítő ügynök) */
MatText.draw(L, s, x, y, o)    // s: '3/4 + 1/4 = 1', '2^3', '2 1/3', 'x · 4' – a .md jelölése (5.1)
                               // o: mint L.tx (s, w, f, c, a, b, k, max) → {w, h, x, y}
MatText.measure(L, s, o)       // → {w, h, asc, desc}
MatText.frac(L, n, d, x, y, o) // n, d: szám vagy szöveg; o.whole (vegyes szám), o.sign
MatText.num(v, d, {plus})      // '−3,25' · '+3' (U.fmt + előjel)
MatText.check(L, key, expected, eps)   // .md-adat ≠ számolt → hibasáv (QA: HIBASÁV)
MatText.css                    // betöltéskor injektált .lp-text .frac / sup stílus
MatQ(n, d)                     // pontos tört: .add .sub .mul .div .neg .inv .cmp .eq
                               //   .v (lebegőpontos) .str ('3/4', '1 1/5') .dec(k) ('0,75'; periódus: {pre, rep})
MatQ.from(datum)               // L.dat(k) (frac / number) → MatQ;  MatQ.gcd, MatQ.lcm

/* MatLine – számegyenes (★ 08-tizedes-tortek) */
const nl = MatLine.create(L, {x0, x1, y, v0, v1, fmt: 'dec'|'frac'|'int', den, minor: true,
                              arrow: true, zeroMark: true})
nl.view(v0, v1) · nl.lerpView(a, b, t)   // logaritmikus zoom két nézet között
nl.x(v) · nl.v(x) · nl.step()            // adaptív főbeosztás (1–2–5 · 10ᵏ)
nl.draw({a, hi: [v…], labels: 'auto'|'none'})
nl.point(v, {label: {s, k}, c, r, hollow, drag: {min, max, snap}}) → aktuális v (húzás után)
nl.jump(v0, v1, t, {c, above, label})    // ugrás-ív (lépegetés), t: rajzolási fázis
nl.span(v0, v1, {c, closed: [true, false]})  // zárt/nyitott vég (9–10: ]a; b[)
nl.mirror(v, t) · nl.brace(v0, v1, {s, k})   // ellentett · távolság (abszolút érték)
MatLine.zoomPair(L, top, bottom, v0, v1, t)  // két szint vetítő-trapézzal (tized → század)
MatLine.double(L, {x0, x1, y, top: {v0, v1, unit}, bot: {v0, v1, unit}})   // kettős számegyenes
MatLine.parallel(L, {x0, x1, y0, dy, dens: [2, 3, 4, …], hi})              // törtfal
MatLine.wrap(L, nl, solid3d, {sides, t})     // felcsavarás hasábra (03, Mat3D-vel)

/* MatPlot – koordináta-rendszer (★ 09-aranyossag) */
const P = MatPlot.create(L, {rect: [x, y, w, h], x: [x0, x1], y: [y0, y1], grid: 1, ticks: {x, y},
                             axis: {x: {s, k}, y: {s, k}}, unit: {x, y}})
P.X(x) · P.Y(y) · P.inv(px, py) · P.view(v, t)
P.axes({a})                                   // rács, tengelyek, nyilak, O, feliratok
P.point(x, y, {name, coords: true, guides: true, c, drag: {snap: 1, box}}) // 'P(3; 2)'
P.fn(f, {x0, x1, t, c, w, dash, samples})     // görbe, szakadásnál megszakad (1/x)
P.line(a, b, {…}) · P.seg(a, b) · P.rect(x0, y0, x1, y1, {fill})   // a fordított arányosság téglalapja
P.table({x, y, rows: [[x, y]…], hi, head: [{s, k}, {s, k}]})  // a hi sor ↔ pont kiemelés
P.click() → {x, y} | null                     // rácsra kattintás (torpedó)

/* MatGeo – síkgeometria (★ 14-haromszogek) */
const G = MatGeo.create(L, {origin: [x, y], unit: 40, grid: false})
G.pt(id, x, y, {name, drag: {snap, constrain(p) → p}, c})   // fogantyú: látható r 12, találati r 28
G.seg(A, B, {c, w, dash, ticks: n, label}) · G.line(A, B) · G.ray(A, B)
G.circle(O, r, {…}) · G.arc(O, r, a0, a1, {t})
G.angle(A, O, B, {r, show: 'value'|'name'|'none', right: 'auto', fill})  // érték a geometriából
G.poly(pts, {fill, stroke, name}) · G.area(pts) · G.perim(pts) · G.dist(A, B) · G.deg(A, O, B)
G.meet.ll(a, b) · G.meet.lc(l, c) · G.meet.cc(c1, c2)
G.reflect(p, axis) · G.rotate(p, O, deg) · G.shift(p, v)
G.cut(poly, line) → [p1, p2] · G.piece(poly, {from: T0, to: T1, t})   // átdarabolás
G.protractor(O, dir, {t, a})                  // szögmérő
G.update()                                    // húzás kezelése, minden képkockán
G.save() / G.load(s)                          // enter(L) visszaállítás

/* MatCon – szerkesztés (15) */
const C = MatCon.create(L, G)
C.compass(O, r, a0, a1, t) · C.ruler(A, B, t)
C.script([{op: 'körző'|'vonalzó'|'pont'|'jelöl', …, note: {s, k}}]).play(t)   // zárt idő
C.bisector(A, B) · C.angleBisector(A, O, B) · C.perpFrom(P, l) · C.perpAt(P, l)
C.parallel(P, l) · C.copyAngle(A, O, B, O2, dir2) · C.reflect(P, l)  → lépéssor

/* MatFrac – törtmodellek (06) */
MatFrac.draw(L, model, {n, d, x, y, size, c, refine: k, t})   // 'kör'|'téglalap'|'szalag'|'csoki'|'tányér'
MatFrac.area(L, {a: q1, b: q2, x, y, size, t})                // szorzás területmodellje
MatFrac.bar(L, {parts: [{w, s, k, c}], x, y, h, unit, brace: {s, k}, t})   // szakaszos ábra
MatFrac.grid100(L, {n, x, y, size, c, t})

/* MatExpr – kifejezésfa (04) */
MatExpr.parse(str) → fa   // · : + − ( ), tört, tizedes tört, negatív szám, x
MatExpr.layout(fa, rect) · MatExpr.draw(L, fa, {t, upTo, hi}) · MatExpr.eval(fa) → MatQ
MatExpr.str(fa) · MatExpr.leftToRight(str) → MatQ   // „sorban számoló” számológép

/* Mat3D – testek (16) */
const S = Mat3D.create(L, {cx, cy, scale, yaw, pitch, persp: 0})
Mat3D.cuboid(a, b, c) · Mat3D.prism(n, r, h) · Mat3D.pyramid(n, r, h) · Mat3D.voxels(cells)
S.draw(solid, {fill, hidden: 'dash', hi: {faces, edges, verts}, labels})
Mat3D.net(solid, spec) → hajtogatási fa;  S.fold(net, t, {stagger}) · Mat3D.netOk(net) → ütközés?
Mat3D.cubeNets  // 11 háló + néhány nem-háló hexominó
S.fill(a, b, c, t) · S.views(voxels) → {front, top, side} · S.drag() · S.save()/load()

/* MatRand – véletlen kísérlet (18) */
const R = MatRand.create(seed)
R.at(i, kind) → az i-edik kísérlet eredménye (zárt alak: hash(seed, i))   // kind: 'érme'|'kocka'|…
R.counts(kind, n) → gyakoriság-tömb (gyorsítótárazva)
MatRand.tree(L, {levels: [[{s, k}…]…], x, y, w, h, t, hi: [útvonal…]})
MatRand.table(L, {rows, cols, cell(i, j) → {s, c}, hi})
MatRand.die(L, v, x, y, size, rot) · MatRand.coin(L, side, x, y, r, flip)

/* MatChart – diagramok (17) */
MatChart.bar(L, {data: [{s, k, v, c}], rect, max, step, t, values: true})
MatChart.pie(L, {data, cx, cy, r, t, labels: 'pct'|'v'|'none'})
MatChart.morph(L, barSpec, pieSpec, t)        // oszlop → körcikk
MatChart.line(L, {…}) · MatChart.dot(L, {…}) · MatChart.tally(L, n, x, y)
MatChart.towers(L, {vals, x, y, cell, level: t})   // átlag kiegyenlítéssel
MatChart.marks(L, {mean, median, mode, axis})

/* MatVenn – halmazábra (01) */
const V = MatVenn.create(L, {n: 2|3, rect, names: [{s, k}…], U: {s, k}})
V.region(item) → 'A'|'AB'|'B'|'U' · V.slot(region, i) → [x, y]   // ütközésmentes rács
V.draw({hi: 'A∩B'|'A∪B'|'¬A'|'A∖B'|'csak egy', t})
V.items(items, {t})                                 // repülés régi → új helyre

/* Mérleg (11) */
const M = MatBalance.create(L, {x, y, arm, plate})
M.set({left: [{kind: 'x'|'1', n}], right: [...]}) · M.tilt(t) · M.draw()
```

### Referencialeckék (első köteg)

1. **`08-tizedes-tortek` → MatLine.** A zoom a legnehezebb számegyenes-funkció. Ha a
   tizedek–századok–ezredek nagyítása működik, minden más (egész, tört, intervallum,
   kettős) egyszerűsített eset.
2. **`09-aranyossag` → MatPlot.** A Matek 9–10 legfontosabb eszköze (függvények, 16 óra), és
   a 12, 18 is erre épül.
3. **`14-haromszogek` → MatGeo.** A húzható, mérő geometria a 13, 15 és a teljes 9–10-es
   geometria alapja.

Mindhárom a `shared/matek/mtext.js`-re épül, amelyet az **előkészítő ügynök** az első köteg
*előtt* ír meg a build-bővítéssel együtt (5. fejezet).

### Gyártási sorrend (legfeljebb 3 párhuzamos lecke kötegenként)

| Köteg | Leckék (nehézség) | Új modul | Újrahasznosított |
|---|---|---|---|
| 0 | előkészítő ügynök | build-bővítés, `MatText`/`MatQ`, szerződés §12 | – |
| 1 | **08-tizedes-tortek** (3), **09-aranyossag** (2), **14-haromszogek** (3) | MatLine, MatPlot, MatGeo | MatText |
| 2 | **06-tortek** (2), **15-tukrozes-szerkesztes** (3), **17-statisztika** (2) | MatFrac, MatCon, MatChart | MatLine, MatGeo |
| 3 | **16-testek** (3), **01-halmazok** (2), **18-valoszinuseg** (2) | Mat3D, MatVenn, MatRand | MatLine, MatPlot, MatChart |
| 4 | **04-muveleti-sorrend** (2), **05-egesz-szamok** (2), **13-terulet** (2) | MatExpr | MatLine, MatGeo |
| 5 | **07-tortmuveletek** (2), **03-oszthatosag** (3), **10-szazalek** (1) | – | MatFrac, MatExpr, MatLine, Mat3D |
| 6 | **11-szoveges-feladatok** (2), **12-sorozatok** (1), **02-helyi-ertek** (2) | Mérleg | MatFrac, MatPlot |

Egy kötegen belül egy modult legfeljebb egy lecke vezet be. A 2–3. köteg leckéi egy-egy új
modult építenek, és egy-egy meglévőt használnak. Így az első köteg modul-API-ja két kötegen
át kipróbálódik, mielőtt a 4–6. köteg csak újrahasznosít. Az utolsó kötegek egyszerűbbek
(nehézség 1–2), mert addigra a modulok kiforrottak.

**A modulok útja:** a referencialecke a modult `/* ── MODUL: … ── */` blokkban írja meg
(mint a történelemnél). A későbbi lecke a blokkot **változtatás nélkül** másolja át. Ha bővítés
kell, visszafelé kompatibilisen bővít, és a fejlécben jelzi (forráslecke + dátum). A
`shared/matek/` alá a modulok csak a felhasználó jóváhagyása után kerülnek; ez a 2. köteg
után lenne ésszerű (MatLine, MatPlot, MatGeo).

### Összehangolás a Matek 9–10-zel

A két matematika-sorozat ugyanazon az éjszakán készül. Javaslat a vezénylő ügynöknek:

- A **0. és az 1. köteg előzze meg** a Matek 9–10 olyan leckéit, amelyek MatLine-t, MatPlot-ot
  vagy MatGeo-t használnak. A 9–10 első kötegébe olyan lecke kerüljön, amely ezek nélkül
  elkészül (pl. kombinatorika/gráfok, logika), vagy kerüljön csúszással az 1. köteg után.
- Ha mégis párhuzamosan kell dolgozni: a fenti API-vázlat a közös szerződés. A 9–10 a saját
  bővítéseit (pl. függvény-transzformáció, intervallum `]a; b[`) *ugyanebben a névtérben*
  írja, és a kiemeléskor a két változatot össze kell fésülni.
- A `MatText`/`MatQ` és a build-bővítés közös: a 9–10 előkészítője ne írja újra, hanem
  bővítse (pl. négyzetgyök, abszolút érték jele, betűs tört).

---

## 5. Build- és szerződés-kiegészítési igények (az előkészítő ügynöknek)

A `tools/build_lesson.py`, a `tools/qa_lesson.py`, a `leckek/README.md` és a
`shared/matek/mtext.js` változásai. Mind visszafelé kompatibilis: a fizika- és
történelemleckék `.content.js`-e bájtra azonos marad (`--all` után `git diff` üres a
`leckek/fizika-7-8`, `leckek/tortenelem-5-6` alatt).

### 5.1 Jelölés a `.md`-ben (panel, `képlet:`, felirat)

| a `.md`-ben | megjelenés | szabály |
|---|---|---|
| `3/4` | álló tört | számjegy(ek) `/` számjegy(ek), előtte-utána nem betű és nem számjegy. Panelen `<span class="frac"><span>3</span><span>4</span></span>`; feliratban a nyers alak marad, a `MatText.draw` szedi. |
| `3\/4` | 3/4 (ferde vonal) | menekítés |
| `2 1/3` | vegyes szám | egész + **egy** szóköz + valódi tört (számláló < nevező); különben két külön elem |
| `−3/4` | −¾ | a mínusz a törtvonal elé kerül |
| `[[x/2]]`, `[[(a + b)/2]]` | álló tört betűvel | explicit forma, ha nem csak számjegy van benne |
| `2^3`, `10^6`, `x^2` | 2³ | `^` után számjegy- vagy betűsor, előtte számjegy, betű vagy `)`; `<sup>` |
| `a_1` | a₁ | meglévő (alsó index) |
| `·`, `:` | szorzás, osztás | `*`, `×`, `x` két szám között, `÷` → **figyelmeztetés** („szorzásjel: ·”) |
| `−` | mínusz | `-` szám előtt vagy szóközök között → **figyelmeztetés** (most csak az Adatokban van) |
| `{1; 2; 3}`, `{ }` | halmaz | ha a kapcsos zárójel tartalma nem adatkulcs, és van benne `;`, vagy üres → szó szerinti. `\{ … \}` mindig szó szerinti. Egyébként marad a mostani hiba, kiegészített tanáccsal: „halmazt pontosvesszővel írj: {1; 2; 3}” |
| `P(3; −2)` | pont | pontosvessző; a `(3, 2)` alak tizedesvesszőnek látszik → **figyelmeztetés** |
| `3,14` | tizedesvessző | `\d\.\d` → **figyelmeztetés** a panelen is (most csak feliratnál van) |
| `45°`, `30′` | fok, szögperc | `'` számjegy után → **figyelmeztetés** („szögperc: ′”) |
| `m²`, `dm³` | mértékegység | `m2`, `cm^2` mértékegység-helyen → **figyelmeztetés** a javított alakkal |
| `≤ ≥ ≠ ≈ ∈ ∉ ⊂ ⊆ ∩ ∪ ∅ ⊥ ∥ π √` | jelek | szó szerint; a fontlefedettséget lásd 5.4 |

- **Szószám:** a tört (`3/4`, `2 1/3`, `[[…]]`) és a hatvány egy szónak számít; a műveleti
  jel és az `=` nem szó (ez most is így van).
- **Felirathossz:** a látható hosszt kell számolni: egy tört = max(számláló, nevező) + 1
  karakter; a `\` menekítés nem számít bele.
- **`képlet:` sor:** ugyanezek a jelölések, nagyobb törttel (`.big-fx .frac`).

### 5.2 Új adattípusok és egységek

Spec-példa és kimenet (`L.dat(k)`):

```json
"data": {
  "első tört":   {"type": "frac", "maxDen": 12, "proper": true, "reduced": false},
  "könyvek":     {"type": "list", "len": [5, 30], "int": true, "min": 0, "max": 50},
  "A pont":      {"type": "point", "box": [-6, -4, 6, 4], "int": true},
  "feladat":     {"type": "expr", "vars": ["x"]},
  "kert oldala": {"dim": "hosszúság", "min": 0.1, "max": 1000},
  "hidegrekord": {"unit": "°C", "sign": true},
  "dobások":     {"unit": "", "int": true, "min": 1, "max": 100000}
}
```

| típus | így írja a tanár | `L.dat(k)` | hibát ad |
|---|---|---|---|
| `frac` | `3/4` · `2 1/3` · `−5/8` · `7/4` | `{t:'frac', n:3, d:4, w:0, neg:false, v:0.75, s:'3/4', red:true}` (vegyes: `w:2, n:1, d:3`) | nevező 0; `maxDen` fölött; `proper` és n ≥ d; `reduced` és nem egyszerűsített („6/8 → 3/4?”) |
| `list` | `0; 1; 1; 2; 12` (pontosvessző, mert a vessző tizedesvessző) | `{t:'list', v:[0,1,1,2,12], u:'', d:0, s:'0; 1; 1; 2; 12'}` | vesszős lista („tizedesvessző? pontosvesszővel válassz el”); `len`; `int`; elemenkénti min/max |
| `point` | `(3; −2)` | `{t:'point', x:3, y:-2, s:'(3; −2)'}` | vessző a pontosvessző helyén; `box`-on kívül; `int` |
| `expr` | `2 + 3 · 4` · `(8 − 4) : 2` · `3x + 4 = 19` | `{t:'expr', s:'2 + 3 · 4', tok:[…]}` | ismeretlen jel, `*`/`/` osztásként, páratlan zárójel, két operátor egymás után, `vars`-ban nem szereplő betű |
| `number` + `int` | `12` | változatlan | nem egész |
| `number` + `sign` | `+3` · `−35 °C` | `s:'+3'` (megtartja a pluszt) | – |
| `number` + `dim` | `24 m` · `2400 cm` · `1,5 l` | `{v, u, d, base, bu}`, pl. `2400 cm` → `base: 24, bu: 'm'` | más dimenziójú egység („5 kg” hosszúságnak) |
| szög | `45° 30′` (spec `unit: "°"`) | `v: 45.5, s:'45° 30′'` | `'` a `′` helyett (figyelmeztetés) |

**Dimenziók** (`dim`) és alapegységük: hosszúság (mm, cm, dm, m, km → m); terület (mm², cm²,
dm², m², a, ha, km² → m²); térfogat (mm³, cm³, dm³, m³ **és** ml, cl, dl, l, hl → l, mert
1 dm³ = 1 l); tömeg (mg, g, dkg, kg, t → kg); idő (s, perc, óra, nap → s); szög (°, ′ → °).
**Egység-aliasok:** `cm2 m2 dm2 mm2 km2` → `²`; `L`, `liter` → `l`; `fok` → `°` (megvan). A
`NUM_RE` előretekintésébe a `′` és a `″` is kell (most a `30′` nem értelmezhető).

A `{kulcs}` hivatkozás a panelen: `frac` → álló tört HTML, `list` → `0; 1; 1; 2; 12`,
`point` → `(3; −2)`, `expr` → a kifejezés a fenti jelöléssel szedve.

### 5.3 Ellenőrzések

- **Build:** az 5.1 figyelmeztetései, az 5.2 hibái, mindegyik sorszámmal és javítási
  javaslattal (pl. „„3*4”: szorzásjelnek ·-ot írj: 3 · 4”).
- **QA (`qa_lesson.py`):** a vászonfeliratok (`L.marks`) szövegén is fusson le a
  tizedespont-, kötőjel-mínusz-, `*`- és `'`-ellenőrzés (figyelmeztetésként).
- **QA, szélső állapotok (javasolt):** ha a lecke definiál
  `window.__qaStates = {3: [{name: 'min', set(L) {…}}, {name: 'max', set(L) {…}}]}`, a
  `--states` kapcsoló lépésenként ezeket is lefotózza (`03-min.png`). A szerződés már most
  előírja a szélső állapotok fotózását, ez automatizálja. A `lesson.js` nem változik.
- **Konzisztencia:** a `MatText.check` a meglévő hibasáv-mechanizmust használja
  (`#lesson-error`), így a QA `HIBASÁV` sora elkapja.

### 5.4 `shared/matek/mtext.js`

Új fájl (a `lesson.js` és a `lesson.css` nem változik). Tartalma a 4. fejezet API-ja
(`MatText`, `MatQ`), plusz:

- **CSS-injektálás** betöltéskor: `.lp-text .frac` (inline-flex oszlop, a számláló alatt
  vonal, `font-size: .82em`, `vertical-align: middle`), `.big-fx .frac`, `sup`.
- **Fontlefedettség:** az előkészítő ellenőrizze a `shared/fonts/` három családján a
  `· × ÷ : − ± ≤ ≥ ≠ ≈ ∈ ∉ ⊂ ⊆ ∩ ∪ ∅ √ π ∠ ° ′ ″ ² ³ → ⊥ ∥ ∞ %` jeleket (pl. fontTools
  egy virtuális környezetben, vagy böngészőben `measureText` összehasonlítással). Az eredmény
  táblázatként kerüljön a fájl fejlécébe, és a `MatText` jelenként a lefedő fontot válassza
  (a π a Fraunces részhalmazából biztosan hiányzik).
- **Méretek:** a tört számlálója és nevezője ≥ 22 px (a QA-küszöb). Ajánlott: ha a
  törtszámjegyek 26–30 px-esek, a törtvonal vastagsága 2,5 px, és a számlálótól meg a
  nevezőtől is 4–6 px-re fut. A kitevő az alapméret 0,65-szöröse, ezért kitevős szöveg alapja
  ≥ 34 px.
- **Önteszt-oldal:** `tools/tests/mtext.html` minden jelöléssel; a QA-képen átnézhető.

### 5.5 README-kiegészítés tanároknak (`leckek/README.md`)

Új alfejezet: „Matematika: tört, hatvány, halmaz, pont, kifejezés”. Az 5.1 táblázatának
tanári része (`3/4`, `2 1/3`, `2^3`, `{1; 2; 3}`, `(3; −2)`, `·` és `:`), a négy új adattípus
egy-egy példával, és a fő szabály: **„Az eredményt ne írd át kézzel – a lecke kiszámolja.
Ha egy eredmény a szövegben is szerepel, és nem egyezik a számolással, a lecke piros sávval
jelez.”**

### 5.6 Önteszt-esetek (`--selftest`)

`3/4` → frac-HTML; `3\/4` → ferde vonal; `km/h` → változatlan; `2 1/3` → vegyes szám;
`5 4/3` → nem vegyes; `−3/4`; `2^3`; `{1; 2; 3}` és `{ }` → szó szerint; `{nincs ilyen}` →
hiba tanáccsal; `3*4` → figyelmeztetés; `5 - 3` → figyelmeztetés. Adatok: `4/0` → hiba;
`6/8` + `reduced` → hiba „3/4?” javaslattal; `2 1/3` → `w=2`; `(3; −2)` → pont; `(3, 2)` →
hiba; `3; 5; 5` → lista; `3, 5` → hiba; `2 + 3 · 4` → kifejezés; `2 + * 3`, `(2 + 3` → hiba;
`2400 cm` (hosszúság) → `base = 24`; `5 kg` (hosszúság) → hiba; `45° 30′` → 45,5; `30'` →
figyelmeztetés. Regresszió: `--all` után a meglévő `.content.js` fájlok változatlanok.

---

## 6. Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / fejlesztési feladat |
|---|---|---|
| 1. Halmazok (10) | 01 | a logikai készlettel játszott játék (tanórai); a három halmazos ábra (9–10) |
| 2. Logika, kombinatorika (10) | 01 („és”, „vagy”, „legalább”), 18 (ágrajz, táblázat) | **igaz és hamis állítások megfogalmazása, néhány lépéses bizonyítási gondolatsor**, nyitott mondat igazsághalmaza (csak a 01 számegyenes-lépésében); számkártyákból számok alkotása, sorba rendezés (permutáció); stratégiai és pénzügyi játékok, Einstein-fejtörő |
| 3. Természetes számok, számelmélet (20) | 02, 03 | a római számok csak kontrasztként (02); nagy számok olvasása és írása; az „Osztó-fosztó” játék |
| 4. Alapműveletek természetes számokkal (16) | 04, 02 (írásbeli összeadás) | **az írásbeli kivonás, szorzás, osztás algoritmusa** (különösen a kétjegyűvel való osztás és a hányados becslése); a fejszámolás gyakorlása |
| 5. Egész számok (18) | 05 | az egész számok osztása (csak megjegyzésként a szorzás után); a műveleti sorrend egész számokkal (a 04 természetes számokkal mutatja) |
| 6. Törtek, tizedes törtek (18) | 06, 08 | a végtelen nem szakaszos tizedes tört csak érdekesség (7–8. cél) |
| 7. Műveletek törtekkel (18) | 07 | a törtek kivonása és az egésszel való osztás csak röviden; a műveleti sorrend törtekkel |
| 8. Műveletek tizedes törtekkel (14) | 08, (04) | **a tizedes törtek írásbeli szorzása és osztása mint algoritmus** (a 08 a helyi érték és a mértékegység-váltás oldaláról mutatja) |
| 9. Arányosság, százalék (20) | 09, 10, (13: terület, 16: térfogat átváltása) | **az idő és a tömeg mértékegységei, átváltásuk**; az egyenes arányosság és a mérés kapcsolata (alkalmi és szabványegységek) |
| 10. Szöveges feladatok (20) | 11 | gazdasági, pénzügyi szöveges feladatok csak a 10-ben (százalék); a becslés külön gyakorlása |
| 11. Függvény előkészítése (10) | 09, 12 | a megfeleltetések tulajdonságainak elemzése (csak a 12 egy lépése); tájékozódás térképen és nézőtéren csak bevezetésként (09) |
| 12. Sorozatok (8) | 12 | ritmus, sorminta, népi motívumok (a sorminta eltolás – tartalék-jelölt) |
| 13. Mérés, mértékegységek (16) | 13, 14 (szögmérés), 16 (felszín, térfogat) | a valódi mérés (osztályterem, mérőhenger, kavicsok) tanórai tevékenység; a háromszög kerülete csak érintőlegesen |
| 14. Síkbeli alakzatok (18) | 14 | **a kör részei; egyenes, félegyenes, szakasz** (csak a MatGeo jelöléseiben); a konvex–konkáv megkülönböztetés; a speciális négyszögek és a Pitagorasz-tétel (7–8. cél); a tangram |
| 15. Transzformációk, szerkesztések (20) | 15 | **a kicsinyítés és a nagyítás; a síkbeli mozgások (eltolás, forgatás)** csak egy-egy mondatban; a szögmásolás csak lépéssorként; a középpontos tükrözés (7–8.) |
| 16. Térgeometria (16) | 16 | **a hasáb és a gúla** csak a hálóválasztóban; **a gömb tulajdonságai**; a zsinóros modellek |
| 17. Leíró statisztika (10) | 17 | adatgyűjtés projektként, táblázatkezelő használata (tanórai) |
| 18. Valószínűség (10) | 18 | szerencsekerék, színes golyós urna (a MatRand tudja, a lecke nem használja); a „Bökős” játék |

**Tartalék-jelöltek**, ha a pilot után folytatódik a sor (a vastagon szedett hiányok miatt,
fontossági sorrendben):

1. `irasbeli-osztas` – az osztás a pénztárgéppel: miért „lehozzuk” a következő jegyet, és
   hogyan becsüljük meg a hányadost (02 gépe + MatText).
2. `kor-reszei` – kör, sugár, átmérő, húr, ív; egyenes, félegyenes, szakasz; a „kör = egyenlő
   távolságra lévő pontok” (MatGeo).
3. `mertekegysegek` – idő, tömeg, hosszúság: átváltás helyi értékkel, a mérőszám és a
   mértékegység fordított viselkedése (MatLine kettős számegyenes).
4. `nagyitas` – kicsinyítés és nagyítás, arányosság a rajzon, térképlépték (MatGeo + MatPlot).
5. `allitasok` – igaz, hamis, ellenpélda, „Rontó” játék, néhány lépéses érvelés (MatVenn).
6. `sorminta-mozgasok` – eltolás és forgatás sormintákon, népi motívumok (MatGeo).
7. `gomb-hasab-gula` – a hasáb, a gúla és a gömb tulajdonságai (Mat3D).

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): a Nemzeti Köznevelési Portál (NKP)
5–6. osztályos digitális matematikatankönyvei; a GeoGebra magyar közösségi anyagai (sok
5–6. osztályos applet, erős átfedés a 13–15-tel – a mi többletünk a lépésenkénti magyarázat
és a tévhit-lépés); a PhET *Fractions*, *Area Builder*, *Number Line*, *Mean: Share and
Balance*, *Plinko Probability* szimulációi (részben magyarul is).

---

## 7. Javasolt szerződés-kiegészítés (kész szöveg)

Az alábbi fejezet változtatás nélkül a `leckek/SZERZODES.md` végére másolható (az
előkészítő ügynök feladata, a build-bővítés után).

````markdown
## 12. Matematika-kiegészítés (5–6. évfolyam)

Matematikaleckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:**
`pilot/matematika-5-6/terv.md` – a saját briefed (3. fejezet), a moduljaid API-ja és a
gyártási sor (4. fejezet).

- **Mappa, fejléc:** `leckek/matematika-5-6/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Matematika · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>`.
- **10–12 évesek:** lépésenként **≤ 45 szó** – a spec-be: `"maxWords": 45`. Új fogalom
  **félkövéren**, egy mondattal megmagyarázva, a kerettanterv szakszavával („számláló”,
  „közös rész”, „szakaszfelező merőleges”). Legyen egy **„Tippelj előbb!”** pillanat:
  becslés vagy szavazás, utána az animáció dönt.
- **A tévhitet ellenpélda cáfolja a vásznon**, nem a szabály kimondása (pl. 1/2 + 1/3 ≠ 2/5,
  mert a 2/5 szalagja rövidebb, mint az 1/2-é).
- **A rajz maga a bizonyíték.** Minden kiírt mért érték (szög, hossz, terület, koordináta,
  relatív gyakoriság) a rajzolt geometriából vagy a lefuttatott szimulációból számolódik,
  ugyanazzal a konstanssal, amellyel rajzolsz. A 3–4–5-ös háromszög valóban 3 : 4 : 5 arányú,
  a 60°-os szög valóban 60°, a számegyenes beosztása egyenletes. Ha egy ábra szándékosan nem
  méretarányos, „vázlat” bélyeget kap (a történelem bélyegstílusával).
- **Pontos számolás:** törtekkel `MatQ`-val (racionális aritmetika), ne lebegőpontosan.
  Tizedes alakot csak kiíráskor kerekíts, és ha kerekítettél, írd ki (≈).
- **Bemenet az `.md`-ben, eredmény a kódban.** A feladat adatai `### Adatok` alatt vannak, az
  eredményt a kód számolja ki. Ha egy eredmény a panelszövegben is szerepel (`{összeg}`), az
  is adat, és a kód ellenőrzi: `MatText.check(L, 'összeg', várt)`. Eltérésnél hibasáv jelenik
  meg, ezt a QA elkapja. Így egy tanári adatjavítás nem hagy hamis állítást a panelen.
- **Jelölés** (a panelen és a vásznon egységesen; a `.md`-jelölés a `leckek/README.md`-ben):
  szorzás `·`, osztás `:`, valódi mínusz `−`, negatív szám zárójelben a műveleti jel után:
  `3 − (−5)`. Tört: `3/4` (álló törtként jelenik meg), vegyes szám `2 1/3`, hatvány `2^3`.
  Halmaz `{1; 2; 3}`, pont `P(3; −2)` – pontosvesszővel, mert a vessző tizedesvessző. Szög:
  `45°`, `30′` (nem aposztróf). Arány `2 : 3`, százalék `25 %`, mértékegység `m²`, `dm³`, `l`,
  `dl`, `ml`. Pont nagy dőlt betű (A), egyenes kis dőlt betű (e), szög görög betű (α); a
  háromszög a, b, c oldala az A, B, C csúccsal szemben van. Ezres tagolás 5 jegytől
  (`U.fmt`): 4527, de 12 000.
- **Betűk:** szám, műveleti jel és mértékegység JetBrains Mono; változó, pont-, egyenes- és
  szögnév dőlt Fraunces; magyarázó felirat Bricolage. A vásznon matematikai szöveget
  (törtet, kitevőt) a `MatText.draw` szed – a darabokat ez is `L.tx`-szel írja, kulccsal.
  Tört számlálója és nevezője ≥ 22 px (ajánlott 26–30 px); kitevős szöveg alapja ≥ 34 px.
  A fontokból hiányzó jeleket (pl. π) a `MatText` tartalékfontra cseréli – saját megoldást
  ne írj.
- **Szereposztás színekkel:** az adott, kiinduló elem tinta; a vizsgált elem és az eredmény
  cinóber (az eredmény vonala vastagabb, 3,5 px); a második elem kékeszöld. Segédvonal
  (körzőív, vetítővonal, vágásvonal) halvány tinta, 2 px, lehet szaggatott. Halmazok: A
  cinóber, B kékeszöld, C okker `#8f5a0c`, a kitöltés α 0,16–0,24, a kiemelt tartomány
  sraffozást is kap (kivetítőn, színtévesztőknek). Előjel: pozitív cinóber, negatív
  kékeszöld (meleg–hideg, mint a hőmérőn). Igaz–hamis: jó/rossz zöld és piros.
- **Rajzlap:** a háttér 40 px-es rácsa a kockás füzet. Ahol egységnégyzetet számolunk
  (terület, koordináta), az egység 40 px többszöröse, a rács a háttérhez igazodik, és
  erősebben rajzolod rá (`rgba(28,36,64,.18)`).
- **Húzható elemek:** a fogantyú látható sugara ≥ 12 px, a találati ≥ 28 px; ráálláskor
  kiemelés; húzás közben a mért érték élőben látszik. Ahol a tananyag egész értéket kér,
  rácsra/egészre ugrik. Az `enter(L)` visszaállítja. Minden húzható elemet legalább két szélső
  helyzetben fotózz (ha a QA tudja: `window.__qaStates`).
- **Véletlen:** csak `U.rng(seed)`, illetve a `MatRand`. Az n-edik kísérlet eredménye a
  seedből és n-ből számolható (visszaléptetés, QA). Az „Új kísérlet” gomb a seedet lépteti. A
  kiírt gyakoriság a ténylegesen kirajzolt kísérletekből jön. Nagy n-t (10 000) ne
  képkockánként szimulálj.
- **Modulok:** a `shared/matek/mtext.js` kész (`MatText`, `MatQ`), a `lesson.js` után töltsd
  be: `<script src="../../shared/matek/mtext.js"></script>`. A többi modul (`MatLine`, `MatPlot`,
  `MatGeo`, `MatCon`, `MatFrac`, `MatExpr`, `Mat3D`, `MatRand`, `MatChart`, `MatVenn`,
  `MatBalance`) először a referencialeckében készül. Jól elhatárolt blokkba kerül
  (`/* ── MODUL: Számegyenes (MatLine) ── */ … /* ── MODUL VÉGE ── */`), a terv 4. fejezetének
  API-ja szerint, saját névtérrel, lecke-specifikus kód nélkül, a blokk elején API-leírással.
  Ha egy modult átveszel, a blokkot **változtatás nélkül** másold át az eddigi legfrissebb
  leckéből. Ha bővíteni kell, csak visszafelé kompatibilisen, a fejlécben jelezve
  (forráslecke + dátum), és írd bele a jelentésbe. A `shared/` módosítása továbbra is csak
  egyeztetve.
- **Kitalált és valós adat:** az árak, nevek és osztályfelmérések kitaláltak – `<!-- kitalált
  példa -->`. Valós adatnál (rekordhőmérséklet, a Föld vízfelülete) a forrás a megjegyzésbe
  kerül.
- **Minden `.md`** végén `<!-- Tanári megjegyzések: … -->` blokk: mely számok kitaláltak, mi
  egyszerűsítés (pl. „csak egész számokat jelölünk”), és hol térhet el a jelölés egyes
  tankönyvekétől.
````
