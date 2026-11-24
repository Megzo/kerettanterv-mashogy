# Pilot: Digitális kultúra 5–6. – a leckesor terve

Forrás: [`kerettanterv/digitalis-kultura/5-6.md`](../../kerettanterv/digitalis-kultura/5-6.md) és
[`_bevezeto-5-8.md`](../../kerettanterv/digitalis-kultura/_bevezeto-5-8.md) (NAT 2020, általános iskola,
8 témakör, 68 óra). Az idézetek szó szerint onnan valók, a forrás elírásaival együtt. A zárójeles szám
(pl. „(7.)”) azt jelzi, ha az idézet nem a lecke fő témaköréből jön. A lecke-formátum leírása:
[`leckek/SZERZODES.md`](../../leckek/SZERZODES.md). A tantárgyi kiegészítő szabályok kész szövegként a
7. fejezetben vannak; ugyanez a szöveg a `SZERZODES.md` 19. fejezete.

Jelölések az „Adatok” pontokban: *(becslés)* – a forrás tartományt ad, vagy a szám kerekített nagyságrend;
a leckében is ki kell mondani. *(ellenőrizendő)* – gyártás előtt forrásban ellenőrizni kell. *(modell)* –
a lecke didaktikus modellje, nem mért adat. *(kitalált példa)* – szemléltető adat, a `.md`-ben is így
jelölve. Ahol egy számot a terv kiszámolt, ott a számolás is szerepel. A koordinátori brief nem megbízható
forrás (`pilot/EJSZAKAI-GYARTAS.md`, 7. tanulság): a leckeügynök minden számot ellenőriz, és az eltérést a
jelentésében jelzi.

## 0. Döntések a felhasználó távollétében

A felhasználó nem volt elérhető, ezért ezekben magam döntöttem. Mind visszavonható.

1. **Mappa- és slugnevek.** Terv: `pilot/digitalis-kultura-5-6/terv.md`; leckék:
   `leckek/digitalis-kultura-5-6/NN-slug.{md,html,content.js}`. A metaadat-sor:
   `tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>` (a
   `tools/build_index.py` `HEAD_RE`-je és `SUBJECTS` listája – „Digitális kultúra”, `digkult` – ezt
   már ismeri). **A slugok az egész repóban egyediek**, mert a QA alapértelmezett mappája
   `build/qa/<slug>/` (a tantárgy nélkül). Ellenőrizve a 160 meglévő sluggal: nincs ütközés (a
   `01-kommunikacio` foglalt – ezért lett a 05-ös `05-csomagok`).
2. **17 lecke** (a 15–17 felső határa). A gerinc 7 lecke: 4 algoritmizálás + 3 robotika (25 óra =
   37 %; 7/17 = 41 %). A többi 10 lecke 43 órán osztozik. A szövegszerkesztés (12 óra) csak 2, a
   bemutatókészítés (8 óra) csak 1 leckét kap: e témakörök óráinak nagy része a valódi programban
   végzett gyakorlás (a kerettanterv „Javasolt tevékenységei” szinte mind dokumentumkészítések), amit
   lecke nem pótol. A mögöttük lévő *fogalom* (rétegek, rejtett jelek, stílus, olvashatóság távolból)
   viszont két-három leckében teljesen elfér.
3. **Fogalom, nem kezelés.** Egyik lecke sem szoftverkezelési útmutató: nincs menüút, gyorsbillentyű,
   valódi program képernyőképe. A lecke a mögöttes működést mutatja (pl. a bekezdés egy
   „tulajdonságcédula”, a kép három szám pixelenként, a jelszó próbálgatások száma), a kezelést a tanár
   az iskolai programban tanítja. A `> megjegyzés:` ehhez ad egy mondatnyi átvezetést.
4. **Saját blokknyelv, nem Scratch-másolat.** A Scratch neve, macskája, kinézete (kirakós-fülek,
   kategóriaszínek, fehér betű színes blokkon) nem jelenik meg. Saját vizuális nyelv: papír alapú,
   tintaszövegű blokk, bal oldalt kategóriasáv rajzolt ikonnal, a tartalmazó blokkot behúzás és
   kategóriaszínű „sín” jelzi, alul „… vége” záró sávval (mint a pszeudokód). A blokkfeliratok magyar
   felszólító igék a `.md`-ből („lépj előre # lépést”, „ismételd # -szor”). Közös csak a fogalom
   (szekvencia, ciklus, elágazás, változó, esemény). Valódi környezet (Scratch, MakeCode stb.) neve csak a
   tanári megjegyzésben, semlegesen: „az órán használt környezetben a blokkok másképp néznek ki”.
5. **Két gerincmodul, egy közös referencialeckében.** A blokkszerkesztő és -értelmező (**DigBlock**) és
   a robotszimulátor (**DigRobot**) a `02-ciklus`-ban épül meg (1. köteg). A DigBlock blokk-katalógusa
   már ott teljes (ciklus, elágazás, változó, esemény, művelet), mert az értelmező kicsi, és a 03, 04
   párhuzamos változat nélkül örökölje. A DigRobot szenzorai (távolság, fény, motorvezérlés) **tervezett,
   visszafelé kompatibilis bővítésként** (v1.1) a `07-szenzor`-ban készülnek (2. köteg). Az API-t ez a
   terv rögzíti előre (4.2), így a bővítés csak hozzáad.
6. **Négy további új modul:** **DigDoc** (dokumentum és diakocka, ref. `10-formazas`), **DigPixel**
   (raszter, vektor, RGB, képműveletek, ref. `13-pixel`), **DigBit** (bitkapcsolók, bájt, kódolás,
   mértékegység-létra, ref. `17-szamitogep`), **DigUI** (semleges képernyő-elemek: telefon, böngésző,
   csevegés, e-mail, poszt, keresőoldal, belépés, ref. `15-labnyom`). A névtér: `Dig…` (Digitális
   kultúra). Átvett kész modul: TtTipp, MatGraf, TortCards, TortTimeline, TortMap, MagText, MagHang,
   BioPlot (4.1).
7. **Nincs billentyűzetes szövegbevitel.** A jelszóleckében sincs beviteli mező: a diák csempékből és
   csúszkákkal „épít” jelszót, így saját, valódi jelszót sem véletlenül, sem kivetítve nem ír be. A
   megjelenő jelszópélda mindig generált (seedelt `U.rng`), és a vásznon ott a felirat: „ezt ne
   használd – mostantól nem titok”. A kérdezd-blokk válasza is választható csempe (04).
8. **Kitalált világ az online leckékben.** Személyek: kitalált keresztnév + monogramos kör, arc nélkül.
   Címek: csak foglalt példadomainek (`.example`, RFC 2606), IP-címek csak a dokumentációs
   tartományokból (192.0.2.x, 198.51.100.x, 203.0.113.x, RFC 5737), telefonszám csak a 112 és a Kék Vonal
   116-111 *(ellenőrizendő a gyártáskor)*. Valódi cég-, termék- és márkanév nincs a vásznon; a tanári
   megjegyzésben csak ott, ahol a forrás megnevezése miatt kell. Valódi weboldal, alkalmazás képernyője,
   logója nem jelenik meg.
9. **Három „online biztonság” lecke szakmai lektorálást kér:** `06-jelszo`, `15-labnyom`, `16-alhir`
   (spec `"review": ["online biztonság"]`). A `15-labnyom` az 1. kötegben van, hogy a hangnem
   (nem ijesztget, nem hibáztat, mindig ad segítségkérési utat) korán visszajelzést kapjon.
10. **Mértékegység:** 1 kB = 1000 bájt (SI-előtag; IEC 80000-13). A 1024-es váltás („KiB”, illetve
    amit egyes operációs rendszerek „KB”-nak írnak) csak a `> megjegyzés:`-ben és a tanári megjegyzésben
    szerepel. A bit és a bájt jele a vásznon kiírva: „bit”, „bájt” (a „B” csak a kB, MB, GB részeként).

---

## 1. Bevezető

A sorozat **17 leckéje** a 10–12 éveseknek szól. A mércét a kerettanterv maga adja. A
`_bevezeto-5-8.md`: „A szövegszerkesztési, a bemutatókészítési, a rajzolási, a képfeldolgozási és a
multimédia ismereteknél a gyakorlati felhasználás, a dokumentumkészítés lényegesebb, mint egy szoftver
részletes funkcionalitásának ismerete.”, illetve: „nem a technikai újdonságokra kell helyezni a
hangsúlyt, hanem az „okos eszközök” „okos használatára””. A sáv bevezetője (`5-6.md`): „A hangsúlyt
azonban nem a mélyebb összefüggésekre (pl. programozási tételekre) kell helyeznünk, hanem a problémák
játékos, de átgondolt, kreatív megközelítésére, algoritmikus megoldására, többféle lehetőség végig
gondolására.” Ezért a ritmus ugyanaz, mint a természettudomány 5–6-nál:
**Tippelj! → kipróbálom → magyarázat**. A diák előbb jósol (mit rajzol a program? hány próbálkozás kell?),
aztán a szimuláció dönt, és csak utána jön a „miért”.

A formátum: 1920×1080-as színpad, 7–9 lépés, világos papírháttér, a panelen lépésenként **legfeljebb 45
szó** (`"maxWords": 45`).

### Hol ad egy animáció *valódi* belátást ebben a tárgyban?

1. **A program futása láthatóvá válik.** A táblán a program szöveg; itt a futó blokk kigyullad, a
   változó doboza átíródik, a feltétel kiírja: IGAZ vagy HAMIS, a robot pedig *közben* mozog. Lépésenként
   előre-hátra léptethető – ez maga a hibakeresés.
2. **A gép betű szerint végrehajt.** A „betű szerinti robot” azt csinálja, amit írtunk, nem amit
   gondoltunk (01). A szöveg szétcsúszik, ha szóközzel igazítottuk (10). A labirintusból kijutó program
   a másik pályán körbe-körbe megy (09). A hiba itt nem szidás, hanem látvány.
3. **Láthatatlan rétegek.** A dokumentum rétegei (oldal ⊃ bekezdés ⊃ karakter) szétnyílnak, a rejtett
   jelek (¶ ·) előjönnek. A kép belenagyítva pixelekre, a pixel három számra esik szét. A hang lépcsős
   mintasorrá, a videó képkockákká, az üzenet csomagokká válik.
4. **Nagy számok kézzelfoghatóan.** Egy 8 kisbetűs jelszó kb. 3,5 perc, egy 16 kisbetűs kb. 1,4 millió év
   *(modell: 1 milliárd próba/s)*. Egy perc CD-minőségű hang kb. 10,6 MB. A „hossz többet ér, mint a
   bonyolultság” így nem szabály, hanem számolt eredmény.
5. **Szenzor és visszacsatolás.** A robot nem „lát”: mér, és a program dönt. Az ultrahang-impulzus
   lassítva oda-vissza fut, a vonalkövető cikázik a vonal szélén, a mért érték élőben görbét rajzol.
6. **Mit árul el egy poszt?** Öt ártatlannak tűnő kitalált poszt darabjaiból kirakós lesz: iskola, utca,
   edzésidő. Az összerakás a „wow”, és ebből jön a beállítás és az óvatosság – ijesztgetés nélkül.

### Mit hagyunk ki?

- **Szoftverkezelést**: menük, gyorsbillentyűk, egy konkrét szövegszerkesztő, bemutató- vagy
  képszerkesztő felülete, fájlkezelő ablakai. A tanár a saját programjában tanítja.
- **Valódi eszközök kézi használatát**: fényképezés, hangfelvétel, szkennelés, valódi robot építése és
  programozása, e-mail tényleges elküldése. A lecke előkészít, a `> megjegyzés:` ajánlja a tevékenységet.
- **Projektmunkát és csoportmunkát** mint tevékenységet. A csoportmunka *eszközeit* (közös szerkesztés,
  megosztás, jogosultság) a 05, 12 és 17 egy-egy lépésben mutatja.
- **Valódi közösségi oldal, kereső, alkalmazás** bemutatását – mind kitalált, semleges felület (DigUI).
- **A táblázatkezelést** – az 5–6. kerettantervben nincs (7–8., 7. témakör).

### Kiválasztási elv

1. **Arányosság.** 68 óra / 17 lecke = 4 óra leckénként.

   | Témakör (óra) | Leckék | Óra/lecke |
   |---|---|---|
   | 1. Algoritmizálás és blokkprogramozás (14) | 01, 02, 03, 04 | 3,5 |
   | 2. Online kommunikáció (5) | 05, 06 | 2,5 |
   | 3. Robotika (11) | 07, 08, 09 | 3,7 |
   | 4. Szövegszerkesztés (12) | 10, 11 | 6 |
   | 5. Bemutatókészítés (8) | 12 | 8 |
   | 6. Multimédiás elemek készítése (8) | 13, 14 | 4 |
   | 7. Az információs társadalom, e-Világ (6) | 15, 16 (+05, 06) | 3 |
   | 8. A digitális eszközök használata (4) | 17 (+05: felhő) | 4 |

   A szöveg- és bemutatókészítés alulsúlyozott (0. döntés, 2. pont); az online kommunikáció és az
   e-Világ felülsúlyozott, mert itt a legnagyobb a belátás (csomag, próbálgatás, lábnyom), és a
   korosztálynak itt a legfontosabb a biztonság.
2. **Gerinc.** A 7 programozós lecke egymásra épül: algoritmus (01) → szekvencia és ciklus (02) →
   elágazás (03) → változó, adattípus, esemény (04) → szenzor (07) → visszacsatolás (08) → tesztelés és
   hibakeresés (09). Mindegyik ugyanazt a blokknyelvet és robotot használja, így a diák a nyelvet egyszer
   tanulja meg.
3. **Nincs fölösleges átfedés a meglévő sorozatokkal.** Ahol a téma már megvan, ott más szemszögből:

   | DK 5–6 lecke | Meglévő lecke | Ott | Itt (más szemszög) |
   |---|---|---|---|
   | 02-ciklus | (matematika 5–6: szögek, sokszögek) | szögmérés | a sokszög mint ismétlés; 360° / n a programból |
   | 03-elagazas | matematika-9-10/02-halmazok-logika, matematika-5-6/01-halmazok | „és”, „vagy”, igazságtábla | feltétel a programban; a sorrend dönt a többirányú elágazásban |
   | 06-jelszo | matematika-9-10/03-fa-diagram | szorzási elv, rendszámok | a próbálgatás ideje; a hossz többet ér; szótártámadás, kétlépcsős azonosítás |
   | 07-szenzor | fizika-7-8/12-hullam-hang | hangsebesség, visszhang | ultrahangos távolságmérés mint robotérzékelés (343 m/s ugyanonnan) |
   | 13-pixel | fizika-7-8/13-szinek (6. lépés: a fények összeadódnak, a képernyő alpixelei) | fényfizika | a szín mint három szám (0–255), felbontás, fájlméret, vektor |
   | 14-hang-video | fizika-7-8/12-hullam-hang | frekvencia, hangmagasság | mintavétel, kvantálás, képkocka, fájlméret |
   | 17-szamitogep | matematika-5-6/02-helyi-ertek (8. lépés: kettes számrendszer) | 13 = 1101 | bit és bájt mint kapcsoló, a betű kódja, mértékegység-létra |
   | 05-csomagok | tortenelem-5-6/14-konyvnyomtatas | a nyomtatás terjedése | az üzenet útja ma; az időszalag hivatkozik a könyvnyomtatásra |
   | 01-algoritmus | magyar-5-6/01-kommunikacio | feladó, címzett, kód | algoritmus mint pontos utasítássor (a kód szó itt más értelmű – a panel egyszer kimondja) |

4. **A 7–8. folytatás.** A 7–8. évfolyam ugyanezeket a témaköröket mélyíti (eljárás, függvény,
   vektorgrafika csomópontjai, táblázat a szövegben, e-kereskedelem, internetes bűnözés, tömörítés). Ezek
   itt legfeljebb egy `> megjegyzés:`-ben kerülnek elő („ezt majd 7. osztályban…”).
5. **Építőkockák.** Hat új modul (4.2), nyolc kész modul bájtra azonos átvétele (4.1).

A leckék sorszáma a kerettanterv sorrendjét követi. A **gyártási sorrend** ettől eltér (6. fejezet).

**Célcsoport: 10–12 évesek.** Panel ≤ 45 szó, rövid mondatok, tegező, kérdező hang, minden új fogalom
**félkövéren**, egy mondattal. Angol szakszó csak a megjegyzésben, egyszer, zárójelben. A „Meglévő
anyag” pontok saját ismereten alapulnak, nincsenek ellenőrizve.

---

## 2. A leckék

| # | slug | cím | témakör | építőkocka | nehézség (1–3) |
|---|---|---|---|---|---|
| 01 | `01-algoritmus` | Hogyan kenjen zsíros kenyeret a robot? – az algoritmus | 1 | DigBlock (saját blokkok), MatGraf, TtTipp | 2 |
| 02 | `02-ciklus` | Hányszor írjam le ugyanazt? – szekvencia és ciklus | 1 (+3) | **DigBlock** (ref.), **DigRobot** v1.0 (ref.), TtTipp | 3 |
| 03 | `03-elagazas` | Melyik ládába kerül az alma? – feltétel és elágazás | 1 | DigBlock, TtTipp | 2 |
| 04 | `04-valtozo` | Hol tartja számon a gép a szavazatokat? – változó, adattípus, esemény | 1 | DigBlock, DigRobot, DigUI, TtTipp | 2 |
| 05 | `05-csomagok` | Hogyan jut el az üzenet a barátodhoz? – csomag, cím, e-mail, felhő | 2 (+7, +8) | DigUI, DigBit, TortMap, TortTimeline, TtTipp | 2 |
| 06 | `06-jelszo` | Hány próbálkozás kell egy jelszóhoz? – online identitás és jelszó | 2 (+7) | DigUI, DigBit, MatGraf, TtTipp | 2 |
| 07 | `07-szenzor` | Honnan tudja a robot, hogy fal jön? – robot, szenzor, vezérlés | 3 | **DigRobot** v1.1 (szenzorok, ref.), DigBlock, BioPlot, TtTipp | 3 |
| 08 | `08-vonalkoveto` | Hogyan marad a robot a vonalon? – fényszenzor és visszacsatolás | 3 | DigRobot, DigBlock, BioPlot, TtTipp | 3 |
| 09 | `09-labirintus` | Kijut-e a robot bármelyik útvesztőből? – tesztelés és hibakeresés | 3 (+1) | DigRobot (rács), DigBlock, TtTipp | 2 |
| 10 | `10-formazas` | Miért csúszik szét a szóközzel igazított cím? – karakter, bekezdés, oldal, stílus | 4 | **DigDoc** (ref.), TtTipp | 3 |
| 11 | `11-dokumentum` | Mindig igaza van a helyesírás-ellenőrzőnek? – kép, elválasztás, idézés | 4 (+5) | DigDoc, MagText, TortCards, TtTipp | 2 |
| 12 | `12-bemutato` | Mit lát a hátsó sor? – a jó diakocka | 5 | DigDoc, TtTipp | 2 |
| 13 | `13-pixel` | Miért kockás a felnagyított fénykép? – pixel, vektor, felbontás, RGB | 6 | **DigPixel** (ref.), DigBit, TtTipp | 3 |
| 14 | `14-hang-video` | Hogyan lesz a hangból szám? – mintavétel és képkocka | 6 (+8) | DigPixel, DigBit, MagHang, BioPlot, TtTipp | 3 |
| 15 | `15-labnyom` | Mit árulnak el rólad a nyomaid? – digitális lábnyom, adatvédelem, segítségkérés | 7 (+2) | **DigUI** (ref.), TortCards, TtTipp | 3 |
| 16 | `16-alhir` | Igaz-e, amit a neten olvasol? – keresés, szűrés, álhír | 7 | DigUI, DigPixel, TortCards, TtTipp | 2 |
| 17 | `17-szamitogep` | Mi történik, ha lenyomod az „A” betűt? – a gép részei, bit, bájt, fájl, mappa | 8 (+2) | **DigBit** (ref.), MatGraf, TortCards, TtTipp | 3 |

Nehézség = gyártási nehézség: 1 = egy fő vizuál, kevés adat; 2 = kész modulokra épülő közepes
szimuláció vagy új interakció; 3 = új modul, összetett szimuláció vagy kényes tartalom.

**Témakörönként** (óra → lecke): 1 (14) → 01, 02, 03, 04 (+09) · 2 (5) → 05, 06 (+15) · 3 (11) → 07, 08,
09 (+02: geometrikus ábra) · 4 (12) → 10, 11 · 5 (8) → 12 (+11: forrás) · 6 (8) → 13, 14 · 7 (6) → 15, 16
(+05: információs társadalom múltja, 06: adatbiztonság) · 8 (4) → 17 (+05: felhő, helyi hálózat, 14:
digitalizálás).

---

## 3. Briefek

Közös minden briefben (a 7. fejezet szabályai szerint):

- **Tippelj!** – legalább egy jóslat a kipróbálás *előtt* (2–4 válasz a TtTipp-pel, a megoldás a
  választásig rejtve, utána „a te tipped” jel). Rossz tipp után: „Sokan gondolják így – nézzük meg!”
- **Kipróbálom** – legalább egy valódi interakció, amely a modellt mozgatja (blokk paramétere, húzás,
  csúszka, kapcsoló). A program a lépés `enter()`-jében visszaáll az alapra.
- **Tévhit-lépés** – a felsorolt tévhitek közül legalább egyet a vászon *cáfol* (lefuttatva,
  ellenpéldával), nem csak kimond.
- **Bélyegek** (TtTipp `stamp`): „modell”, „kitalált”, „lassítva”, „nagyítás · szemléltetés”,
  „sematikus”; a valódi programokra utaló ábrán „a te programodban másképp néz ki”.
- **Biztonsági mondat** (06, 15, 16, és ahol előkerül): segítséget kérni mindig lehet és érdemes –
  „szólj egy felnőttnek, akiben megbízol”; Kék Vonal: 116-111.

### 01 · `01-algoritmus` – Hogyan kenjen zsíros kenyeret a robot? – az algoritmus

- **Tanulási cél:** Az **algoritmus** véges sok, pontos, egyértelmű lépés, amely egy feladatot megold. A
  végrehajtó (ember, robot, számítógép) csak azt teszi, amit leírtunk: amit „mindenki tud”, azt is le
  kell írni. A lépések **sorrendje** számít. Egy nagy lépést kisebbekre bontunk (**lépésenkénti
  finomítás**), amíg minden lépés **elemi** lesz. Az algoritmusnak van **bemenete** (amiből dolgozik) és
  **kimenete** (az eredmény). Ugyanazt az algoritmust leírhatjuk szöveggel, rajzzal (folyamatábra) és
  blokkokkal.
- **Kerettanterv:** „érti, hogyan történik az egyszerű algoritmusok végrehajtása a digitális eszközökön” ·
  „egyszerű algoritmusokat elemez és készít” · „Hétköznapi tevékenységek és információáramlási folyamatok
  algoritmusának elemzése, tervezése” · „Nem számítógéppel megoldandó feladatok algoritmizálása” · „Az
  algoritmus végrehajtásához szükséges adatok és az eredmények kapcsolata” · „egyszerű algoritmusok
  tervezése az alulról felfelé építkezés és a lépésenkénti finomítás elvei alapján” · Fogalmak:
  „algoritmus, folyamat, adat, […] bemenet, kimenet, problémamegoldó tevékenység, […] algoritmus leírása,
  […] lépésenkénti finomítás elve” · tevékenység: „Az algoritmizálás nem számítógépes megvalósítása, az
  algoritmus eljátszása, személyes élmények szerzése”.
- **Tévhitek:** „Az algoritmus = számítógépes program.” (A recept, az útbaigazítás, a tűzriadó rendje is
  algoritmus.) „A gép kitalálja, mire gondoltam.” „A sorrend mindegy, ha minden lépés benne van.” „Egy
  feladatra csak egy jó algoritmus van.” „Minél rövidebb a leírás, annál jobb.” (Ha nem elemi, a
  végrehajtó elakad.)
- **Kulcsvizuál:** felülnézeti konyhapult (sematikus): kenyér, zsír, kés, só, lilahagyma, tányér. Rajta
  egy „betű szerinti” robotkar (ipari kar, nincs arca). Balra a recept DigBlock **saját blokkokból** (a
  blokkfelirat a `.md`-ből: „vágj egy szelet kenyeret”). Futáskor a futó blokk kigyullad, a kar
  végrehajtja. Ha a lépés nem elemi („kend meg a kenyeret”), a kar megáll egy cinóber kérdőjel-buborékkal:
  „Mivel? Melyik oldalát?” Ha a sorrend rossz (a sózás a kenés előtt), a só a puszta kenyérre kerül, és a
  zsír rákenve „eltakarja” (stilizált, humoros, nem csúnya). A finomítás: a „kend meg” blokk kinyílik
  (MatGraf fa, balról jobbra): vedd a kést → merítsd a zsírba → húzd végig a szeleten → tedd le a kést.
- **Kipróbálom:** a recept blokkjai húzhatók (sorrend); ▶ futtatás és „egy lépés”. A „kend meg” blokk
  kattintásra kinyílik/összecsukódik (finomítás). Az utolsó előtti lépésben ugyanaz az algoritmus
  háromféle leírásban: szöveg (`DigBlock.text`), folyamatábra (`DigBlock.flow`), blokk – egy kapcsolóval
  váltva, a futó lépés mindhárom nézetben ugyanott világít.
- **Tippelj!** 2. lépés: „A robot ezt kapja: »Kend meg a kenyeret zsírral.« Mit csinál? jól megkeni /
  megáll, nem tudja, mivel / az egész veknit bekeni”. 4. lépés: „Felcseréltük a sózást és a kenést. Mi
  lesz? ugyanolyan / a só a zsír alá kerül / a robot leáll”.
- **Lépések:** Mi az algoritmus? (recept, útbaigazítás, tűzriadó) · A robot betű szerint dolgozik ·
  Elemi lépések · A sorrend számít · Lépésenkénti finomítás · Bemenet és kimenet (hozzávalók → zsíros
  kenyér; ha nincs hagyma? – „ha”, előre a 03-ra) · Háromféle leírás · Összefoglalás.
- **Adatok:** nincs mért adat; minden *(kitalált példa)*. A recept lépései a `.md` Feliratok rétegében
  (a tanár átírhatja más ételre: a blokkok száma a kódban, a feliratuk a `.md`-ben).
- **Átfedés:** a 3–4. évfolyamon a „robotika és kódolás alapjai” elemi lépéseket és sorrendet már
  tanított (padlórobot). Itt az új: a finomítás, a bemenet–kimenet és a háromféle leírás.
- **Építőkocka:** DigBlock (saját blokktípus `lépés`, `text`, `flow`), MatGraf (`layout` + `tree`, nem
  egyenletes fa, a finomításhoz), TtTipp.
- **Meglévő anyag:** a Bebras-verseny algoritmikus feladatai, a „robot-szülő” szendvicskészítő
  osztálytermi játék (több változatban ismert) *(nincs ellenőrizve)*. Nálunk a finomítás és a
  háromféle leírás élőben a többlet.

### 02 · `02-ciklus` – Hányszor írjam le ugyanazt? – szekvencia és ciklus

- **Tanulási cél:** A **szekvencia** egymás után végrehajtott utasítások sora. Ha egy részlet ismétlődik,
  **ciklusba** tesszük: rövidebb, és könnyebb javítani. A **ciklusmag** az, ami ismétlődik. A ciklusok
  **fajtái**: adott számszor ismétlő (*számlálós*), feltételig ismétlő (*feltételes*: „amíg nem ütközik”)
  és a soha meg nem álló (*végtelen*). Ciklusba ciklus is tehető. Egy szabályos sokszögnél a robot
  összesen 360°-ot fordul, ezért egy fordulat 360° / oldalszám.
- **Kerettanterv:** „a probléma megoldásához vezérlési szerkezetet (szekvencia, elágazás és ciklus)
  alkalmaz a tanult blokkprogramozási nyelven” · „mozgásokat vezérel szimulált vagy valós környezetben” ·
  „ismeri és használja a programozási környezet alapvető eszközeit” · „Elágazások, feltételek kezelése;
  többirányú elágazás; ciklusok fajtái” · „Animáció, grafika programozása” · (3.) „Geometrikus ábrák
  útján mozgó robot programozása” · Fogalmak: „szekvencia, […] ciklus, ciklusok fajtái, […] fejlesztői
  felület, blokkprogramozás, kódolás”.
- **Tévhitek:** „A ciklus csak rövidít, a program ugyanaz.” (Ugyanazt csinálja, de egy helyen javítható:
  a 4-ből 6 lesz, és hatszög.) „A négyzetnél 4 × 90°, tehát a háromszögnél 3 × 60°.” (Nem: a robot a
  *külső* szöggel fordul, 120°-ot – ezt a futás mutatja meg, a 60°-os program nyitott vonalat rajzol.)
  „A végtelen ciklus mindig hiba.” (A robot „mindig” ciklusa szándékos: figyel, amíg ki nem kapcsolják –
  előre a 07-re.) „A kör nem sokszög.” (36, majd 360 apró lépés: a szem körnek látja.)
- **Kulcsvizuál:** felülnézeti asztallap (papír, halvány cm-rács), rajta a DigRobot tollal; a nyoma
  tintavonal. Balra a DigBlock-szerkesztő, középen fut a robot. A 2. lépésben a 8 blokkos szekvencia
  „összecsúszik” egy ciklusba (a négy egyforma pár egymásra úszik – áttűnés). A 6. lépésben egy
  „virág”: ismételd 12-szer [négyzet; fordulj 30°] – a beágyazott ciklus a szerkesztőben két színes
  sínnel, a vásznon rajzolódó mintával.
- **Kipróbálom:** a „ismételd # -szor” és a „fordulj # fokot” paramétere kattintással/léptetővel
  állítható (3–12; 10°-os lépés + a 360/n segédgomb). Sebesség-csúszka (lassú / gyors / azonnal). A
  4. lépésben oldalszám-csúszka 3 → 36 → 360: a sokszög körré simul.
- **Tippelj!** 3. lépés: „ismételd 5-ször [lépj előre 100 lépést, fordulj jobbra 72 fokot] – mit rajzol?
  ötszöget / csillagot / nyitott vonalat”. 5. lépés: „Ha 72° helyett 144°-ot fordul? ötszög / csillag /
  két kör” → csillag (ötágú, kétszer fordul körbe: 5 · 144° = 720°).
- **Lépések:** Rajzolj négyzetet! (szekvencia, 8 blokk) · Négyszer ugyanaz: a ciklus · Tippelj: mit
  rajzol? · Sokszögből kör · Csillag: kétszer körbe · Ciklus a ciklusban · Meddig ismételjen? – számlálós,
  feltételes („amíg nem ütközik”, az ütköző már v1.0), végtelen · Összefoglalás.
- **Adatok:** a sokszög fordulási szöge 360° / n *(számolt, a kód számolja)*; az ötágú csillag 144°-a
  (5 · 144° = 720° = 2 teljes fordulat); a robot sebessége a vásznon *(modell)*: 20 cm/s, fordulás
  90°/s.
- **Átfedés:** a szögmérés és a sokszögek a matematika 5–6. anyaga; itt a program felől.
- **Építőkocka:** **DigBlock** (referencia – a teljes katalógus, 4.2), **DigRobot** v1.0 (referencia:
  `asztal` és `rács` mód, toll, falak, ütköző), TtTipp.
- **Meglévő anyag:** „teknőcgrafika” (Logo, Seymour Papert, 1960-as évek vége – *ellenőrizendő*); a
  magyar iskolákban régóta használt Logo-hagyomány (Comenius Logo, Imagine) *(nincs ellenőrizve)*. A
  `> megjegyzés:` egy mondatban megemlítheti, hogy ez a rajzolós robot ötlete régi.

### 03 · `03-elagazas` – Melyik ládába kerül az alma? – feltétel és elágazás

- **Tanulási cél:** A **feltétel** egy kérdés, amire a válasz IGAZ vagy HAMIS. Az **elágazás** a
  feltételtől függően más-más utasítást hajt végre („ha … akkor … különben”). A **többirányú
  elágazásban** a gép fentről lefelé nézi a feltételeket, és az *első* igaznál dönt – a sorrend
  megváltoztatja az eredményt. Két feltétel „és”-sel, „vagy”-gyal köthető össze. A **határeset** (pontosan
  7 cm) külön próbát kér: „nagyobb” vagy „nagyobb vagy egyenlő”?
- **Kerettanterv:** „Szekvencia, elágazások és ciklusok” · „Elágazások, feltételek kezelése; többirányú
  elágazás” · „A vezérlési szerkezetek megfelelői egy programozási környezetben” · „Tesztelés, elemzés” ·
  tevékenység: „Vezérlőszerkezetek tudatos választását igénylő blokkprogramozási feladatok megoldása” ·
  „a kimeneti eredmények elemzése szélsőséges bemeneti értékek esetén” · Fogalmak: „elágazás, […]
  feltétel, algoritmustervezés”.
- **Tévhitek:** „A gép minden feltételt megnéz, és a »legjobbat« választja.” (Az elsőt, amelyik igaz.)
  „A »különben« ág mindig lefut.” „Ha két feltétel igaz, mindkét ág lefut.” (Egy elágazásban csak egy.)
  „A 7 cm-es alma nagyobb, mint 7 cm.” „Az »és« és a »vagy« ugyanaz.”
- **Kulcsvizuál:** válogatószalag oldalnézetben: az almák (kitalált méret és szín) balról jönnek, egy
  mérőkapu (méret, szín – sematikus szenzor) alatt mennek át, és egy terelőlap a programtól függően A, B
  vagy C ládába löki őket. Mellette a DigBlock-program, a futó feltétel kiírja: „7,5 cm > 7 cm? IGAZ”
  (kékeszöld) / „HAMIS” (halvány). A program mellett ugyanaz folyamatábrán (rombusz – `DigBlock.flow`).
- **Kipróbálom:** a feltételek sorrendje húzással felcserélhető; a küszöb (5–9 cm) és a reláció (>, ≥)
  kattintással állítható. Az alma-sorozat a `.md` Adatai közül jön (méret, szín), a diák egy „saját
  almát” is betehet (méret-, színválasztó). „És/vagy” kapcsoló a 6. lépésben: két lámpa (IGAZ/HAMIS) és
  az eredmény-lámpa – négy eset kis táblázatban.
- **Tippelj!** 4. lépés: „Program: ha nagyobb, mint 7 cm → A; különben ha piros → B; különben → C. Hová
  kerül a nagy piros alma? A / B / mindkettőbe” → A (az első igaz dönt). 5. lépés: „A pontosan 7 cm-es
  alma? A / B vagy C / a gép elakad” → nem A (a „nagyobb” itt HAMIS).
- **Lépések:** Döntések körülöttünk (ha esik → esernyő) · Feltétel: IGAZ vagy HAMIS · Ha … akkor …
  különben · Többirányú elágazás: az első igaz dönt · Határeset: pontosan 7 cm · „És” vagy „vagy”? ·
  Teszteljük szélsőséges almákkal (1 cm, 20 cm, zöld-piros) · Összefoglalás.
- **Adatok:** az alma-sorozat méretei és színei *(kitalált példa)*, a küszöb 7 cm *(kitalált példa)*; a
  `.md`-ben `list` típus (pl. „6,5; 7; 7,5; 8,2 cm”).
- **Átfedés:** az „és”, „vagy”, „nem” halmazelméleti oldala a matematika-5-6/01-halmazok leckében van;
  itt csak a program felől, egy táblázattal. Igazságtábla, logikai szita: 9–10. (matematika-9-10/02).
- **Építőkocka:** DigBlock (`ha`, `ha-különben`, összehasonlítás, `és`/`vagy`, `flow`), lecke-saját
  szalag és terelőlap, TtTipp.

### 04 · `04-valtozo` – Hol tartja számon a gép a szavazatokat? – változó, adattípus, esemény

- **Tanulási cél:** A **változó** egy névvel ellátott tároló, amelynek értéke a futás közben változhat
  (címkés doboz). Az **értékadás** („legyen pont = 0”) beírja, a „növeld” átírja. Az **adat** lehet
  **szám** vagy **szöveg** (adattípus): a 5 + 5 = 10, de az „5” és az „5” összefűzve „55”. A program
  **bemenetet** kap (kérdés, gombnyomás) és **kimenetet** ad (kiírás, rajz). Az **eseményvezérelt**
  program vár, és egy esemény (kattintás) indít el egy blokksort. **Tesztelni** szélsőséges bemenettel
  is kell (0, negatív, nagyon nagy, szám helyett szó).
- **Kerettanterv:** „megkülönbözteti, kezeli és használja az elemi adatokat” · „adatokat kezel a
  programozás eszközeivel” · „tapasztalatokkal rendelkezik az eseményvezérlésről” · „Számok és szöveges
  adatok” · „Animáció, grafika programozása” · tevékenység: „Változók használatát igénylő folyamatok
  programozása, és a kimeneti eredmények elemzése szélsőséges bemeneti értékek esetén” · „Objektum
  tulajdonságának és viselkedésének beállítását igénylő feladat megoldása blokkprogramozási környezetben”
  · Fogalmak: „adat, adattípus, szöveges adatok, számok, bemenet, kimenet, […] változó, […] tesztelés,
  elemzés, hibajavítás”.
- **Tévhitek:** „A változó a betű az egyenletben.” (Itt egy doboz, ami *most* ennyit tartalmaz.) „Az
  „5” és az 5 ugyanaz.” „A változó magától számol.” (Csak az írja át, akinek a program megengedi.) „A
  program akkor jó, ha a próbapéldára jó.” (A „−3 éves” és a „tizenkét” bemenet is jön.) „Az esemény
  akkor is fut, ha nem történt meg.”
- **Kulcsvizuál:** egy osztálytermi **szavazógép** (DigUI egyszerű panel két nagy gombbal: „alma” /
  „körte”, a lecke saját rajza). Alatta két címkés doboz (`DigBlock.watch`): `alma = 3`, `körte = 5`;
  kattintáskor a doboz tartalma kiugrik, és az új szám beúszik. Két kis eseményprogram („ha rákattintanak
  az alma gombra → növeld alma-t 1-gyel”). A 7. lépésben a 02-ből ismert tollas robot **spirált** rajzol:
  „legyen hossz = 5; ismételd 40-szer [lépj hossz lépést; fordulj 90°; növeld hossz-t 5-tel]”.
- **Kipróbálom:** a szavazógép gombjai valódi eseményt váltanak ki (a QA-állapotban rögzített
  kattintássorral). „Kérdezd meg: hány éves vagy?” – a válasz csempékből választható: 11, 0, −3, 200,
  „tizenegy” (nincs billentyűzet, 0. döntés 7.). A program kiírja: „Jövőre 12 leszel”, illetve hibát
  (cinóber keret a `+` blokkon: „a + csak számokkal működik”). Spirál: a növekmény (1–15) és a fordulás
  (85–95°) állítható – kis eltérés, látványos minta.
- **Tippelj!** 3. lépés: „összefűz „5” és „5” = ? 10 / 55 / hiba” → 55. 6. lépés: „Ha valaki −3-at ad
  meg, mit ír ki a program? hibát / »Jövőre −2 leszel« / semmit” → „Jövőre −2 leszel” (a gép nem tudja,
  hogy ez értelmetlen – a tesztelő dolga észrevenni, és feltételt írni rá).
- **Lépések:** A szavazógép: esemény · A változó: címkés doboz · Szám vagy szöveg? · Bemenet és kimenet
  · Mi lesz a „tizenegy”-gyel? · Tesztelés szélsőséges bemenettel (és javítás egy „ha”-val) · Változó a
  ciklusban: spirál · Összefoglalás.
- **Adatok:** nincs mért adat; a szavazatok, a tesztbemenetek *(kitalált példa)*. Az elfogadott
  életkor-tartomány a javított programban (pl. 6–18) a `.md`-ben.
- **Átfedés:** a 02 ciklusa és tolla, a 03 feltétele visszatér; új: változó, típus, esemény.
- **Építőkocka:** DigBlock (`legyen`, `növeld`, `változó`, `összefűz`, `+`, `kérdezd`, `mondd`,
  `kattintáskor`, `watch`), DigRobot (asztal, toll), DigUI (`toggle`/gomb stílus – opcionális), TtTipp.

### 05 · `05-csomagok` – Hogyan jut el az üzenet a barátodhoz? – csomag, cím, e-mail, felhő

- **Tanulási cél:** Az elküldött üzenet és kép nem „repül át” egyben: **csomagokra** bomlik, minden
  csomagon ott a **cím** (feladó és címzett) és a sorszám. A csomagok gépről gépre (útválasztók) jutnak
  el, akár más-más úton, és a célnál sorszám szerint állnak össze; az elveszettet újra kéri a gép. A
  csevegő- és az e-mail-üzenet általában egy **szolgáltató szerverén** át megy, és ott **másolat**
  marad. A **felhő** egy másik gépen tárolt mappa, amit megoszthatsz (megtekintő vagy szerkesztő
  **jogosultsággal**). Mivel az elküldött üzenet másolatként él tovább, gondold át, mit, kinek és
  hogyan írsz (**netikett**).
- **Kerettanterv:** „ismeri, használja az elektronikus kommunikáció lehetőségeit, a családi és az
  iskolai környezetének elektronikus szolgáltatásait” · „ismeri és betartja az elektronikus
  kommunikációs szabályokat” · „Online kommunikációs csatornák önálló használata, online kapcsolattartás”
  · „Etikus és hatékony online kommunikáció a csoportmunka érdekében” · „Adattárolás és -megosztás
  felhőszolgáltatások használatával” · Fogalmak: „e-mail, chat, felhőszolgáltatások, adattárolás,
  megosztás” · (7.) „ismeri az információs társadalom múltját, jelenét és várható jövőjét” · (8.) „helyi
  hálózat, jogosultságok”.
- **Tévhitek:** „Az üzenet egyenesen a barátom telefonjára megy.” „A törölt üzenet mindenhonnan
  eltűnik.” „Az internet egy nagy kábel / a műholdakon megy.” (Túlnyomórészt földi és tenger alatti
  üvegszálon – *ellenőrizendő arányszám nélkül, csak „főleg”*.) „A felhő a levegőben van.” „A megosztott
  link csak annak működik, akinek küldtem.” (Akinek továbbküldik, annak is – ha „bárki, akinél a link
  van” a beállítás.) „A CSUPA NAGYBETŰ csak kiemelés.” (Online kiabálásnak olvassák.)
- **Kulcsvizuál:** két kitalált gyerek (monogram, DigUI `phone`) – Anna a városban, Bence a
  szomszéd utcában. Az elküldött fotó *(lassítva)* színes kis borítékokra (csomagokra) esik szét; mindegyiken
  cím (dokumentációs IP-cím, RFC 5737) és sorszám. Egy hálózatrajz (lecke-saját gráf, csomópontok =
  útválasztók) a TortMap halvány Európa-alapján: a csomagok egy *(kitalált, valószerű)* szerverig mennek
  (pl. Frankfurt környéke), onnan vissza. A 4. lépésben a diák „elvágja” az egyik kábelt (kattintás): a
  csomagok kerülő úton mennek, a sorrend összekeveredik, a célnál sorba állnak. Az utolsó előtti lépésben
  TortTimeline: üzenetküldés régen és ma (futár → posta → távíró → telefon → e-mail → okostelefon).
- **Kipróbálom:** kábelvágás (bármelyik él, kattintásra, újra kattintva visszaáll); a kép mérete
  (100 kB / 3 MB) → a csomagok száma (a kód számolja: méret / 1500 bájt). A felhőmappa
  megosztásakor kapcsoló: „csak megtekintheti / szerkesztheti / bárki, akinél a link van” – a vásznon
  látszik, kik érik el a mappát. Netikett-lépés: egy kitalált üzenet három változata (csupa nagybetű,
  bántó hangnem nélküli, tárgy nélküli e-mail) – a diák kiválasztja a jót (TortCards párosítás:
  hiba → javítás).
- **Tippelj!** 1. lépés: „Anna fotót küld a szomszéd utcába. Merre megy? egyenesen Bence telefonjára / egy
  szerveren át, akár másik országon keresztül / műholdon” → szerveren át. 3. lépés: „Egy 3 MB-os fotó hány
  csomag? kb. 2 / kb. 200 / kb. 2000”.
- **Lépések:** Merre megy a fotó? · Cím minden csomagon · Csomagokra bontva · Ha elvágják az utat ·
  Milyen gyors? (üvegszálban a fény kb. 200 000 km/s → Budapest–Frankfurt kb. 4 ms) · E-mail, csevegés,
  felhő – hol van a másolat, ki éri el? (megosztás, jogosultság) · Régen napok, ma ezredmásodpercek
  (időszalag) · Netikett: mit, kinek, hogyan · Összefoglalás. *(9 lépés.)*
- **Adatok:** Ethernet-keret legnagyobb adatmezője (MTU) 1500 bájt (IEEE 802.3) → 3 MB / 1500 bájt =
  2000 csomag *(becslés: a fejlécek miatt valamivel több)*; a fény sebessége üvegszálban kb. 200 000 km/s
  (törésmutató kb. 1,47–1,5 → c / 1,5) *(becslés)*; Budapest–Frankfurt légvonalban kb. 810 km
  *(ellenőrizendő)* → kb. 4 ms egy irányba (a valódi út hosszabb, a mért késés tipikusan 10–25 ms –
  *becslés*). IPv4-cím: 4 szám 0–255 között = 4 bájt (előre a 17-re). Időszalag: távíró (Morse, 1844 –
  Washington–Baltimore), telefon (Bell, 1876), Puskás Tivadar Telefonhírmondója (Budapest, 1893), első
  hálózati e-mail (Ray Tomlinson, 1971), a web (Tim Berners-Lee, CERN, 1989/1991), okostelefonok
  elterjedése (2007 után) – *mind ellenőrizendő, a tortenelem-5-6/14 könyvnyomtatás-évszámával
  egyeztetve*.
- **Átfedés:** a kommunikáció tényezői (magyar-5-6/01) – itt nem ismételjük, csak a „csatorna” szó
  visszautal. A protokollok, a helyi hálózat részletei: 7–8. (9. témakör).
- **Építőkocka:** DigUI (`phone`, `chat`, `mail`, `toggle`), DigBit (`bytes` – az IP-cím négy bájtja),
  TortMap (`shared/tort/proj.js` + `map-vilag.js`, Európa-kivágat, halványan), TortTimeline, TortCards,
  TtTipp.
- **Meglévő anyag:** NKP Digitális kultúra 5–6. *(nincs ellenőrizve)*; „Internet-csomag” osztálytermi
  játékok (CS Unplugged) *(nincs ellenőrizve)*.

### 06 · `06-jelszo` – Hány próbálkozás kell egy jelszóhoz? – online identitás és jelszó

- **Tanulási cél:** Az **online identitás** (felhasználónév + jelszó, és ha van, egy második lépés)
  bizonyítja, hogy te vagy te. A jelszót a támadó gép **próbálgatással** keresi: a lehetőségek száma =
  (a jelkészlet mérete)^(a hossz). Minden plusz jel megsokszorozza a próbák számát, ezért **a hossz
  többet ér, mint a bonyolultság**. A gép először a gyakori jelszavakat és a szavak + évszám mintákat
  próbálja (**szótár**). Jó jelszó: hosszú, véletlen (pl. több véletlen szó), **minden fiókhoz más**, és
  senkinek nem adod meg. A **kétlépcsős azonosítás** akkor is véd, ha a jelszó kitudódott.
- **Kerettanterv:** „tisztában van a hálózatokat és a személyes információkat érintő fenyegetésekkel,
  alkalmazza az adatok védelmét biztosító lehetőségeket” · „Online identitás védelmében teendő lépések,
  használható eszközök” · tevékenység: „Az adatok védelmét biztosító lehetőségek használata az online
  kommunikációs alkalmazásokban” · Fogalmak: „online identitás” · (7.) „Adatok biztonságos kezelése,
  technikai és etikai problémák” · (7.) Fogalmak: „e-ügyintézés; […] adatbiztonság; adatvédelem”.
- **Tévhitek:** „A *Bodri2014!* erős, mert van benne nagybetű, szám és írásjel.” (Kutyanév + évszám +
  felkiáltójel: a szótár ezt az elsők között próbálja.) „Egy jó jelszó elég mindenhova.” (Ha egy helyről
  kiszivárog, minden fiók nyitva – dominó.) „A barátomnak megadhatom.” „Ha a weboldal elfogadta, biztos
  jó.” „A hosszú jelszót úgysem lehet megjegyezni.” (Négy-öt véletlen szóból kép lesz.) „A kétlépcsős
  azonosítás csak a felnőtteknek kell.”
- **Kulcsvizuál:** DigUI `login` egy kitalált fiókhoz; a jelszó **csempékből** épül (kisbetű, nagybetű,
  szám, írásjel, szó). Jobbra egy „próbálgató gép” *(modell)* pörgő számlálóval és egy logaritmikus
  időszalaggal (másodperc → perc → nap → év → millió év), amelyen a becsült idő pöttye csúszik. A 2.
  lépésben a 4 számjegyes kód (10 000 lehetőség) mint fa: MatGraf `band` módban 10 · 10 · 10 · 10 levél,
  minden szint egy jel. A 6. lépésben dominó: egy kiszivárgott jelszó → öt fiók dől.
- **Kipróbálom:** csúszkák: hossz (4–20), jelkészlet (kapcsolók: kisbetű 26 / +nagybetű 52 / +szám 62 /
  +írásjel 94); a lehetőségek száma (DigBit `big`, hatványalak + szóval: „218 billió”) és az idő a
  kódból számolva. „Szómód”: 1–6 szó egy 2000 szavas *(kitalált méretű)* listából. A „Bodri2014!”-szerű
  minták egy gombra a szótárba ugranak: az idő a számolt érték helyett „azonnal”.
- **Tippelj!** 3. lépés: „Melyik nehezebb a gépnek? 8 jel kis- és nagybetűvel és számmal / 16 jel csak
  kisbetűvel / egyforma” → 16 kisbetű (26^16 ≈ 4,4 · 10^22 vs 62^8 ≈ 2,2 · 10^14). 5. lépés: „Mennyi idő
  kell a »Bodri2014!«-hez? évek / napok / szinte azonnal” → szinte azonnal (szótár).
- **Lépések:** Ki vagy az interneten? · Hány lehetőség? (4 számjegy: 10 000) · Hossz vagy bonyolultság?
  · A gép próbálgat (modell: 1 milliárd próba/s; a weboldal viszont pár hibás próba után letilt) · A
  szótár mindent előre próbál · Egy jelszó – sok fiók? (dominó) · Kétlépcsős azonosítás · Senkinek, még
  barátnak sem · Összefoglalás.
- **Adatok:** a próbálgatás sebessége **1 milliárd (10^9) próba/s** *(modell; a valós sebesség a jelszó
  tárolásának módjától függően ennél sokkal kisebb vagy nagyobb is lehet – nagyságrendi forrás: a
  hashcat nyilvános teljesítménymérései és a Hive Systems évenkénti jelszótáblázata, ellenőrizendő)*.
  Számolt értékek *(teljes keresés; átlagosan a fele elég – a panel egyszer kimondja)*: 4 számjegy 10^4 →
  10 µs; 8 kisbetű 26^8 ≈ 2,1 · 10^11 → kb. 3,5 perc; 8 jel 62 féléből ≈ 2,2 · 10^14 → kb. 2,5 nap; 12
  kisbetű ≈ 9,5 · 10^16 → kb. 3 év; 12 jel 62 féléből ≈ 3,2 · 10^21 → kb. 100 ezer év; 16 kisbetű ≈ 4,4 ·
  10^22 → kb. 1,4 millió év. Szómód (2000 szó): 4 szó 1,6 · 10^13 → kb. 4,4 óra; 5 szó 3,2 · 10^16 →
  kb. 1 év; 6 szó 6,4 · 10^19 → kb. 2000 év *(a panel nem ígér „feltörhetetlent”)*. Jelkészlet: 26
  kisbetű (angol ábécé), 26 nagybetű, 10 számjegy, 32 írásjel (ASCII nyomtatható jelek: 95, a szóköz
  nélkül 94). Ajánlás: hosszú jelszó, összetételi kényszer nélkül – NIST SP 800-63B (a 2024–2025-ös
  4. változat szerint *ellenőrizendő*: legalább 15 jel, ha csak jelszó véd); „három véletlen szó” – az
  Egyesült Királyság NCSC ajánlása (2021) *(ellenőrizendő)*. A gyakori jelszavak listáját (pl. „123456”)
  a lecke **nem** mutatja, csak a tanári megjegyzés említi (0. döntés, 7.).
- **Átfedés:** a szorzási elv és a fa-diagram a matematika-9-10/03-ban; itt a fa csak „ennyi út van”
  szemléltetés, a hangsúly az időn. Az adathalászat részletei: 7–8. („internetes bűnözés”); itt egy mondat:
  „jelszót senki nem kér e-mailben vagy üzenetben – a valódi szolgáltató sem”.
- **Építőkocka:** DigUI (`login`, `notif`), DigBit (`big`), MatGraf (`band` módú fa), TtTipp; a
  logaritmikus időszalag lecke-saját (a DeepTime túl nagy ehhez).
- **Biztonsági mondat:** „Ha gyanús üzenetet kapsz, vagy valaki a jelszavadat kéri, ne válaszolj, és
  szólj egy felnőttnek, akiben megbízol.”
- **Szakmai lektor:** `"review": ["online biztonság"]`.

### 07 · `07-szenzor` – Honnan tudja a robot, hogy fal jön? – robot, szenzor, vezérlés

- **Tanulási cél:** A **robot** érzékel, a program dönt, a motor cselekszik – ez a **vezérlés** köre. A
  **szenzor** egy mennyiséget mér, és számmá vagy IGAZ/HAMIS jellé alakítja: az **ütköző**
  (érintésérzékelő) jelez, ha nekiment; az **ultrahangos távolságmérő** hangimpulzust küld, és a
  visszhang idejéből számol távolságot; a **fényérzékelő** a padló világosságát méri. Szenzor nélkül a
  robot „vakon” megy a beprogramozott úton; szenzorral a környezethez igazodik. A mérés nem tökéletes
  (zaj, ferde fal, puha felület), ezért **küszöböt** adunk meg.
- **Kerettanterv:** „adatokat gyűjt szenzorok segítségével” · „mozgásokat vezérel szimulált vagy valós
  környezetben” · „Robotvezérlési alapfogalmak” · „Szenzorok, robotok vezérlésének kódolása
  blokkprogramozással” · „Algoritmusok megvalósítása, modellezése egyszerű eszközök segítségével” ·
  tevékenység: „A környezeti akadályokra reagáló robot programozása” · Fogalmak: „robot, szenzor,
  algoritmus, blokkprogramozás, kódolás, vezérlés”.
- **Tévhitek:** „A robot lát, mint mi.” (Egy számot mér egy irányba.) „A robot tudja, hol van a fal.”
  (Csak azt tudja, amit a szenzor éppen mér.) „A szenzor mindig pontos.” „A robot gondolkodik.” (A
  program dönt, a szabályt mi írtuk.) „A robot a kamerájával mér távolságot.” (Ez itt ultrahang.)
- **Kulcsvizuál:** felülnézeti asztal, falakkal és akadályokkal (DigRobot v1.1). Az 1. lépésben a vak
  robot „lépj 50 cm-t” programmal nekimegy egy közelebb tolt falnak (stilizált koccanás, cinóber
  villanás – nincs törés). A 3. lépésben *(lassítva)* az ultrahang-impulzus (koncentrikus ívek) kifut,
  visszaverődik, visszaér; közben stopper (ms), és a kód kiszámolja: távolság = 343 m/s · idő / 2. A
  4. lépésben ferde fal: a visszhang elkerül, a mért érték „nincs visszhang” / túl nagy. Jobb oldalt
  élő BioPlot-görbe a mért távolságról az idő függvényében, a küszöb vízszintes vonallal.
- **Kipróbálom:** a fal húzható (távolság), a fal szöge kapcsolóval (merőleges / ferde / puha függöny).
  A program küszöbe (5–40 cm) és sebessége állítható; az akadályt kikerülő program („mindig: ha
  távolság < küszöb → fordulj; különben lépj”) fut az akadálypályán. Zaj-kapcsoló: ± kis véletlen
  (seedelt) – a görbe remeg, a túl kicsi küszöb hibát okoz.
- **Tippelj!** 1. lépés: „A falat 10 cm-rel közelebb toltuk. A »lépj 50 cm-t« robot: megáll a fal előtt
  / nekimegy / visszafordul” → nekimegy. 4. lépés: „Mit mér a szenzor egy ferde falnál? pontos távolságot
  / túl nagyot vagy semmit / kisebbet”.
- **Lépések:** Vakon: a program nem tudja, hol a fal · Érzékel – dönt – cselekszik · Ütköző: IGAZ vagy
  HAMIS · Ultrahang: visszhangból távolság · Mikor téved a szenzor? · Küszöb: mikor forduljon? · Az
  akadálykerülő robot · Összefoglalás.
- **Adatok:** hangsebesség 20 °C-os levegőben 343 m/s (fizika-7-8/12-hullam-hang ugyanígy: 331 m/s +
  0,6 m/s · t) → 1 m-es távolságnál az oda-vissza út 2 m, az idő 2 / 343 s ≈ 5,8 ms *(számolt)*; a
  tipikus iskolai ultrahangos szenzor kb. 40 kHz-en sugároz, és kb. 2 cm – 4 m között mér *(becslés,
  adatlapok alapján – terméknév nélkül)*; az ember kb. 20 kHz-ig hall *(becslés; korral csökken)* →
  ezért nem halljuk. A denevér is visszhanggal tájékozódik – egy mondat a megjegyzésben.
- **Átfedés:** a hang mint hullám, a hangsebesség hőmérsékletfüggése (fizika-7-8/12) – csak a számot
  vesszük át. A 3–4-es padlórobot itt kap először szenzort.
- **Építőkocka:** **DigRobot** v1.1 (referencia: `sense`, távolság-szenzor ív, `echo`, ütköző, zaj),
  DigBlock (`érzékelő`, `mindig`, `ha-különben`), BioPlot (élő görbe, küszöbvonal), TtTipp.

### 08 · `08-vonalkoveto` – Hogyan marad a robot a vonalon? – fényszenzor és visszacsatolás

- **Tanulási cél:** A fényérzékelő a padlóról visszavert fényt méri: fehéren nagy, feketén kicsi az
  érték. Egyetlen szenzorral a robot a vonal **szélét** követi: „ha sötét → kicsit balra, különben
  kicsit jobbra” – ezért cikázik. Ez **visszacsatolás**: mér → dönt → mozdul → újra mér, sokszor
  másodpercenként. Túl gyorsan a kanyarban lerepül, mert két mérés között túl messzire jut. Két
  szenzorral négy eset van (többirányú elágazás), és simább a mozgás.
- **Kerettanterv:** „Szenzorok, robotok vezérlésének kódolása blokkprogramozással” · „A gyakorlati
  életből vett egyszerű problémák megoldása algoritmusok segítségével” · „Algoritmus készítése lépésekre
  bontással” · tevékenység: „Robotok vezérlése blokkprogramozással” · (1.) „többirányú elágazás” · (1.)
  „Mozgások vezérlése valós és szimulált környezetben, az eredmények tesztelése, elemzése”.
- **Tévhitek:** „A robot látja a vonalat.” (Egy pontban mér világosságot.) „Egyenesen megy a vonalon.”
  (Cikázik a szélén.) „Gyorsabban jobb.” „Ha egy szenzor jó, a két szenzor duplán jó.” (Más szabály
  kell hozzá.) „A visszacsatolás csak robotokban van.” (Termosztát, a kerékpáron egyensúlyozó ember is
  így működik.)
- **Kulcsvizuál:** felülnézeti pálya: fehér papír, fekete vonal (egyenes, ív, éles kanyar, 8-as). A
  robot a DigRobot motorvezérlésével halad (`motor`, kerékseb.), a nyoma halvány tinta. Fölötte a
  szenzor pontja és egy kis „mért érték” sáv (0–100). Jobbra a visszacsatolási kör négy állomása (mér →
  dönt → mozdul → mér) – a körben egy fénypötty fut minden méréskor; alatta BioPlot: mért érték–idő, a
  küszöb vonalával (a cikázás itt fűrészfog).
- **Kipróbálom:** sebesség-csúszka (lassú → gyors), fordulási erő-csúszka, szenzorszám (1 / 2), és a
  pálya (4 változat). A futás determinisztikus trace-ből jön (rögzített 20 ms-os vezérlési ütem – a
  zárt `DigRobot.motor` szimulációból, nem a képkocka-időből), így a QA és a visszaléptetés ugyanazt
  mutatja.
- **Tippelj!** 3. lépés: „Kétszer gyorsabban megy az éles kanyarban. Mi lesz? simán veszi / lassabban
  ér célba / lerepül a vonalról” → lerepül. 6. lépés: „Két szenzor, mindkettő fehéret mér. Merre menjen?
  előre / álljon meg / forduljon” → előre (a vonal a kettő között van).
- **Lépések:** Fehér vagy fekete? – a fényérzékelő · Egy szenzor, két szabály: cikázás · Gyorsabban? ·
  A visszacsatolás köre · Mi lesz a 8-asnál? · Két szenzor, négy eset · Kitekintés: minél sötétebb, annál
  jobban fordul (arányos kormányzás – csak megmutatva) · Hol van még visszacsatolás? · Összefoglalás.
- **Adatok:** a fehér és a fekete felület mért értéke *(modell: 90 és 10 egység a 0–100-as skálán)*; a
  küszöb a kettő közepe (50) *(modell)*; a vezérlési ütem 20 ms *(modell)*. Valódi iskolai robotoknál
  a vezérlés másodpercenként több tucatszor mér *(becslés)*.
- **Átfedés:** a 03-as többirányú elágazás itt robotként; a 07-es fényszenzort itt használjuk
  folyamatosan.
- **Építőkocka:** DigRobot v1.1 (`motor`, fényszenzor, padlóvonal `floor`), DigBlock (`mindig`,
  `ha-különben`, két szenzorral többirányú), BioPlot, TtTipp.
- **Meglévő anyag:** a vonalkövető a robotikaórák klasszikus feladata (iskolai robotkészletek
  leírásai) *(nincs ellenőrizve)*.

### 09 · `09-labirintus` – Kijut-e a robot bármelyik útvesztőből? – tesztelés és hibakeresés

- **Tanulási cél:** Egy program, amely *egy* pályán működik, még nem jó: **tesztelni** kell más
  pályákon, szélsőséges esetekben is. Az általános szabály (a jobb kéz mindig a falon: „ha jobbra
  szabad → fordulj jobbra és lépj; különben ha előre szabad → lépj; különben fordulj balra”) sok
  útvesztőből kijut, de nem mindegyikből. A **hibakeresés** módszere: lépésenként futtatjuk, figyeljük a
  változókat és a szenzorértékeket, megállunk a gyanús helyen, és megkeressük, hol tér el a várt a
  valóstól. A **végtelen ciklust** onnan ismerjük fel, hogy a robot ugyanoda tér vissza ugyanabban az
  irányban.
- **Kerettanterv:** „A program megtervezése, kódolása” · „Tesztelés, elemzés” · Fogalmak: „tesztelés,
  elemzés, hibajavítás” · tevékenység: „Mozgások vezérlése valós és szimulált környezetben, az eredmények
  tesztelése, elemzése” · (3.) „A környezeti akadályokra reagáló robot programozása” · (3.) „Az
  algoritmikus gondolkodás fejlesztése”.
- **Tévhitek:** „Ha egyszer működött, kész.” „A hiba ott van, ahol a robot elakadt.” (Gyakran sokkal
  korábban.) „A hibát úgy javítom, hogy mindent átírok.” (Egy dolgot változtatunk, és újra tesztelünk.)
  „A jobbkéz-szabály mindig kivezet.” (Ha a cél egy „szigeten” van, a fal mentén körbe-körbe megy.)
- **Kulcsvizuál:** rácsos útvesztő (DigRobot `rács` mód, falak a cellák élein) felülnézetben; a robot
  nyoma színezett (minden bejárás új árnyalat); a jobb oldali szenzorok kis jelzői (fal elöl? fal
  jobbra?). A szerkesztő mellett a „hibakereső” sáv: ▶ futás, „egy lépés”, töréspont (cinóber pötty a
  blokk mellett), a változók és a szenzorok aktuális értéke. A 7. lépésben négy pálya egymás mellett
  kicsiben (teszttábla): ✓ kijutott / ✗ körbe jár – a jel rajz, nem karakter.
- **Kipróbálom:** a kézi program („lépj 3, fordulj jobbra, lépj 2…”) az 1. pályán fut, majd ugyanaz a
  2. pályán (elakad). A szabályprogram blokkjai sorrendbe húzhatók; a 6. lépésben egy **hibás**
  szabályprogram (a „balra” és a „jobbra” felcserélve egy ágban – a hiba a `.md`-ben leírva) – a diák
  töréspontot tesz, léptet, és rákattint a hibás blokkra. Pályaválasztó (4 pálya, az egyik szigetes).
- **Tippelj!** 3. lépés: „Ugyanez a program a 2. pályán? kijut / elakad a falnál / másik kijáraton megy
  ki” → elakad. 7. lépés: „A jobbkéz-szabály ebből (szigetes) pályából? kijut / körbe-körbe megy /
  megáll” → körbe-körbe (a lépéskorlát kimondja: „végtelen ciklus?”).
- **Lépések:** A cél: ki az útvesztőből · Kézzel megírt út · Másik pályán? · Általános szabály: jobb
  kéz a falon · Lépésenként: hibakeresés · Hol a hiba? (töréspont) · Teszteljük minden pályán ·
  Összefoglalás: tervezés → kódolás → tesztelés → javítás (kör).
- **Adatok:** a pályák *(kitalált példák)*, a lépéskorlát (pl. 400 lépés) a `.md`-ben.
- **Átfedés:** a gráfbejárás és a szélességi keresés 9–10. (és felsőbb) anyag – itt nem kerül elő.
- **Építőkocka:** DigRobot (`rács` mód, falérzékelők), DigBlock (`debug`: töréspont, egy lépés,
  `watch`), TtTipp.

### 10 · `10-formazas` – Miért csúszik szét a szóközzel igazított cím? – karakter, bekezdés, oldal, stílus

- **Tanulási cél:** A dokumentum egymásba ágyazott **szövegegységekből** áll: karakter ⊂ szó ⊂ sor ⊂
  **bekezdés** ⊂ oldal. Mindegyiknek saját **formázása** van, mint egy tulajdonságcédula: a **karakternél**
  betűtípus (talpas, talpatlan, egyenlő szélességű), méret (pont), stílus (félkövér, dőlt, aláhúzott),
  szín; a **bekezdésnél** igazítás, **behúzás**, térköz; az **oldalnál** **lapméret** és **margó**. Az
  Enter a bekezdés végét jelenti, nem a sor végét. Ha szóközökkel igazítunk, a szöveg szétcsúszik, amint
  betűtípust, méretet vagy szöveget változtatunk – az igazítás a bekezdés tulajdonsága. A **stílus** egy
  elnevezett formázás: egy helyen átírod, és minden vele formázott bekezdés megváltozik.
- **Kerettanterv:** „ismeri és tudatosan alkalmazza a szöveges és multimédiás dokumentum készítése során
  a szöveg formázására, tipográfiájára vonatkozó alapelveket” · „a tartalomnak megfelelően alakítja ki a
  szöveges vagy a multimédiás dokumentum szerkezetét” · „Szövegszerkesztési alapelvek” · „Szöveges
  dokumentumok létrehozása, formázása” · tevékenység: „Nyomtatott dokumentumokban alkalmazott betű- és
  bekezdésformátumok elemzése” · Fogalmak: „szövegbevitel, […] kijelölés, […] szövegegységek, karakter,
  karakter formázása, karakter típusa, karakter stílusa, karakter mérete, bekezdés, bekezdés
  formázása, behúzás, margó, lapméret”.
- **Tévhitek:** „Az Enter a sor vége.” (A szövegszerkesztő magától tördel; az Enter új bekezdést kezd.)
  „Középre igazítani szóközökkel is lehet.” „Az első sor behúzása = öt szóköz.” „A nagyobb betű mindig
  jobban olvasható.” „A kiemelés: félkövér + dőlt + aláhúzott + piros egyszerre.” (Egy kiemelés elég.)
  „Minden címet egyesével formázok.”
- **Kulcsvizuál:** egy A4-es oldal (DigDoc) – egy kitalált iskolai plakát („Őszi papírgyűjtés”). A 8.
  lépésben a rétegek **szétnyílnak** (ál-3D, egymás mögé csúszó lapok): oldal (margóvonalak, lapméret) →
  bekezdések (dobozok, igazításjelek) → karakterek (minden betű dobozzal). Minden réteg mellett a
  tulajdonságcédulája (`.md`-ből: „betűtípus: talpatlan”, „méret: 14 pont”). A 5. lépésben a szóközzel
  „középre igazított” cím egyenlő szélességű betűvel (JetBrains Mono) tökéletes, majd betűtípus-csere
  (Fraunces) → szétcsúszik; a szóközök pöttyként (·) láthatóvá válnak.
- **Kipróbálom:** betűtípus-kapcsoló (talpas / talpatlan / egyenlő szélességű), méret-csúszka (8–28
  pont), igazítás (balra / középre / jobbra / sorkizárt), behúzás és margó húzással a vonalzón.
  „Rejtett jelek” kapcsoló (¶ · →). Stílus-lépés: a „Címsor” stílus méretét átírva mind a három cím
  egyszerre változik; a kézzel formázott negyedik nem (a diák rájön, melyik „lóg ki”).
- **Tippelj!** 5. lépés: „A szóközökkel középre tett címnek betűtípust váltunk. Mi történik? középen
  marad / elcsúszik / eltűnik” → elcsúszik. 7. lépés: „A »Címsor« stílus betűméretét 18-ról 24-re
  írjuk. Hány cím változik? 1 / mind, ami ezzel a stílussal készült / mind, ami félkövér”.
- **Lépések:** Mit látsz egy plakáton? (szövegegységek) · A karakter cédulája · Talpas, talpatlan,
  egyenlő szélességű · A bekezdés cédulája (igazítás, behúzás, térköz; az Enter) · Szóközzel igazítva? ·
  Rejtett jelek · A stílus: egy helyen javítasz · Az oldal: lapméret, margó – és a rétegek egymásban ·
  Összefoglalás.
- **Adatok:** 1 pont (tipográfiai, DTP) = 1/72 hüvelyk ≈ 0,353 mm *(számolt: 25,4 mm / 72)*; A4 =
  210 × 297 mm (ISO 216); a nyomtatott folyó szöveg szokásos mérete kb. 10–12 pont *(becslés,
  tipográfiai gyakorlat)*; a plakátcím mérete *(kitalált példa)*. A képernyőn megjelenő oldal
  méretaránya a valóságos A4-é (a kód a mm-értékekből rajzol, szerződés 9.).
- **Átfedés:** a magyar helyesírás nem kerül elő (az a 11-ben, kritikus használatként).
- **Építőkocka:** **DigDoc** (referencia: `page`, `para`, `layout`, `draw` rétegekkel és rejtett
  jelekkel, `styles`, `spaceAlign`), TtTipp.
- **Meglévő anyag:** NKP Digitális kultúra 5. szövegszerkesztési fejezete *(nincs ellenőrizve)*.

### 11 · `11-dokumentum` – Mindig igaza van a helyesírás-ellenőrzőnek? – kép, elválasztás, idézés

- **Tanulási cél:** A képet **arányosan** méretezzük (a sarkánál fogva), különben torzul. A kép és a
  szöveg viszonya beállítás: a sorban áll, körbefuttatja a szöveg, vagy a szöveg mögött van. A
  **helyesírás-ellenőrző** egy szótárral veti össze a szavakat: aláhúzza, ami nincs benne (akkor is, ha
  helyes, pl. egy ritka név), és nem húzza alá a létező, de rossz helyen álló szót („kár” a „kar” helyett).
  Ezért kritikusan használjuk. Az **elválasztás** a szótagolás szabályait követi, az összetett szót a
  tagjai határán választjuk el (*vas-út*). Kézi kötőjellel ne válasszunk el: ha a szöveg átrendeződik, a
  kötőjel a sor közepén marad. Más szövegét **idézőjelben** és **forrással** vesszük át; a képnek is van
  szerzője.
- **Kerettanterv:** „ismeri és kritikusan használja a nyelvi eszközöket (például helyesírás-ellenőrzés,
  elválasztás)” · „etikus módon használja fel az információforrásokat, tisztában van a hivatkozás
  szabályaival” · „A dokumentum céljának megfelelően képek választása, beillesztése, átméretezése,
  elhelyezése” · „Nyelvi funkciók kritikus használata, helyesírás-ellenőrzés, elválasztás” · „Az
  információforrások etikus felhasználásának kérdései” · Fogalmak: „helyesírás-ellenőrző, elválasztás,
  kép beillesztése, képméret változtatása, információforrások etikus felhasználása, idézés szabályai” ·
  (5.) „Az információforrások etikus felhasználásának kérdései”.
- **Tévhitek:** „Ami nincs aláhúzva, az helyes.” „Ami alá van húzva, az hibás.” „A kép szélét húzva
  arányosan nő.” „Amit a neten találok, szabadon felhasználhatom.” „Ha átírok pár szót, már nem kell
  forrás.” „Elválasztani bárhol lehet, ahol kifut a sor.”
- **Kulcsvizuál:** DigDoc oldal: egy kitalált fogalmazás („Kirándulás a Bakonyban”) egy saját rajzú
  képpel (TtIkon nélkül: egyszerű tájrajz – lecke-saját). A 1. lépésben a kép oldalfogóját húzva a fa
  megnyúlik (torzítás, cinóber „torz” bélyeg); a sarokfogóval arányos. A 3–4. lépésben a „helyesírás-
  ellenőrző” mint szótár-polc: minden szó egy kártya, a gép megkeresi a polcon; amelyik nincs ott, piros
  hullámvonalat kap. A 5. lépésben egy keskenyedő hasáb: a szavak elválasztási pontjai (MagText
  szótagolás + összetételhatár a `.md`-ből) kis pöttyként, a sorvégen a kötőjel automatikusan jön és megy;
  a kézi kötőjel a sor közepén ragad (cinóber).
- **Kipróbálom:** kép-fogók (oldal vs sarok), körbefuttatás-kapcsoló (sorban / körbefuttatva / mögötte).
  Hasábszélesség-csúszka (az elválasztás élőben). Párosítás (TortCards): idézet → helyes forrásmegjelölés
  (könyv, weboldal, kép – kitalált adatokkal), és „szabad-e így felhasználni?” (saját fotó / szabad
  licencű kép forrásmegjelöléssel / letöltött kép forrás nélkül).
- **Tippelj!** 3. lépés: „»Elestem, és megütöttem a károm.« (a karom helyett) – aláhúzza az ellenőrző a
  »károm« szót? igen / nem” → nem: a *károm* létező szóalak (a kár szóból). A pontos mondatot a `.md`
  adja; legyen természetes és egyértelmű. 5. lépés: „Hol válasszuk el a »vasút« szót? va-sút / vas-út /
  mindkettő jó” → vas-út.
- **Lépések:** Kép a szövegben: arányosan! · Sorban, körbefuttatva, mögötte · Hogyan dolgozik a
  helyesírás-ellenőrző? · Mit nem vesz észre? · Elválasztás: a gép dolga · Más szövege, más képe ·
  Hogyan jelöljük a forrást? · Összefoglalás.
- **Adatok:** elválasztás: *A magyar helyesírás szabályai*, 12. kiadás (2015), 223–238. pont (javítva 2026-11-24; vas-út: 234.)
  *(ellenőrizendő paragrafusszámok)*; a hivatkozás mintája (szerző: cím. kiadó, év; weboldal: cím, URL,
  a megtekintés dátuma) *(a gyártáskor egy iskolai ajánlással egyeztetendő – nincs egységes kötelező
  forma, a panel ezt kimondja)*; Creative Commons licencek léte (creativecommons.org) – csak a fogalom
  („szabad felhasználás feltétellel”), licencfajták nélkül.
- **Átfedés:** a szótagolás szabályai a magyar-5-6/03 és a magyar 5–6 helyesírás anyaga; itt csak a
  gépi elválasztás felől. A szerzői jog részletei 7–8.
- **Építőkocka:** DigDoc (`image`, `wrap`, hasáb, `o.hyph` visszahívás), MagText (`syllabify`), TortCards,
  TtTipp.

### 12 · `12-bemutato` – Mit lát a hátsó sor? – a jó diakocka

- **Tanulási cél:** A **prezentáció** a beszédet *támogatja*, nem helyettesíti. Egy diakockán egy
  gondolat, kevés szó, nagy betű, erős **kontraszt**. A **vizuális hierarchia** (méret, szín, hely,
  üres tér) megmutatja, mit nézzen először a néző. A **lényegkiemelés**: egy bekezdésből három kulcsszó és
  egy kép. Az **animáció** akkor segít, ha azt mutatja meg, amiről éppen beszélsz; ha minden mozog, elvonja
  a figyelmet. A képnek és az adatnak forrása van a dián is. A **dokumentumformátum** döntés: a
  szerkeszthető fájl a közös munkához, a nem szerkeszthető (pl. PDF) a továbbküldéshez.
- **Kerettanterv:** „ismeri a prezentációkészítés alapszabályait, és azokat alkalmazza” · „Bemutatószerkesztési
  alapelvek” · „A bemutató objektumaira animációk beállítása” · „Iskolai, hétköznapi problémák közös
  megoldása, a csoportmunka támogatása” · Fogalmak: „prezentáció, animáció, dokumentumformátum,
  csoportmunka eszközei, lényegkiemelés, információforrások etikus felhasználása”.
- **Tévhitek:** „Minél több szöveg van a dián, annál többet tanul a közönség.” (Olvasni és hallgatni
  egyszerre nehéz.) „A felolvasott dia jó előadás.” „Minden betű látszik, ha a monitoron látszik.” (A
  hátsó sorból nem.) „Világoskék szöveg fehér alapon szép.” „Minél több animáció, annál érdekesebb.”
- **Kulcsvizuál:** egy kitalált kiselőadás („A méhek”, saját egyszerű rajzokkal) két diakockája (DigDoc
  `slide`). A 2. lépésben egy osztályterem oldalnézetben (sematikus): vászon elöl, padsorok 2, 5 és 9 m-re;
  a dia mindhárom távolságból, a távolsággal arányos elmosással *(modell: a látásélesség kb. 1′-es
  szögfelbontásából – a kód számolja)*. A 4. lépésben „szemkövető” pöttyök *(modell, nem mért)*: a
  hierarchia szerint 1-2-3 sorrendben ugranak a dia elemeire; rossz hierarchiánál összevissza.
- **Kipróbálom:** a dia betűmérete (12–48 pt egyenérték), a szöveg mennyisége (bekezdés → felsorolás →
  3 szó + kép) és a háttér/szöveg színpár (4 változat) kapcsolható; mindhárom távolságnézet élőben
  frissül. Animáció-kapcsoló: „minden ugrál” / „egyszerre egy, amikor róla beszélsz”.
- **Tippelj!** 1. lépés: „Melyik diáról emlékszel többre az előadás után? sok szöveg / kép + három szó /
  egyforma” → kép + három szó (a beszéddel együtt – a panel nem állít többet, mint a forrás). 2. lépés:
  „Olvasható-e a 9 m-es sorból a 14-es betű? igen / alig / nem”.
- **Lépések:** Mire való a dia? · Mit lát a hátsó sor? · Kontraszt · Mit nézel először? – vizuális
  hierarchia · Lényegkiemelés: kevesebb szöveg · Animáció mértékkel · Forrás a dián, formátum, közös
  munka · Összefoglalás.
- **Adatok:** a látásélesség normál értéke kb. 1 szögperc (a Snellen-tábla betűje 5′, egy vonása 1′)
  *(ellenőrizendő)*; 9 m-ről az 5′-es betű magassága 9000 mm · tan(5′) ≈ 13 mm *(számolt)* – ez a
  *határ*, a kényelmes olvasáshoz többszöröse kell *(becslés)*; a vászon magassága és a teremméret
  *(kitalált példa: 1,5 m-es vászon, 9 m mély terem)*. A kép + beszéd hatásáról: Mayer multimédiás
  tanulási elvei (koherencia, redundancia) – *ellenőrizendő; a panel csak óvatosan fogalmaz („sokan
  jobban megjegyzik”)*.
- **Átfedés:** a leckék saját formája (vászon + panel) maga is példa – a `> megjegyzés:` egy mondatban
  utalhat rá.
- **Építőkocka:** DigDoc (`slide`, `blurAt(dist)` – a lecke saját elmosás-modelljével), TtTipp.

### 13 · `13-pixel` – Miért kockás a felnagyított fénykép? – pixel, vektor, felbontás, RGB

- **Tanulási cél:** A digitális fénykép **pixelekből** (képpontokból) álló rács – ez a
  **rasztergrafika** (bittérkép). Minden pixel egy szín, a szín három szám: vörös, zöld, kék (**RGB**),
  egyenként 0–255 (1 bájt). A **felbontás** a pixelek száma (szélesség × magasság): több pixel →
  részletesebb kép, nagyobb fájl. Nagyításkor a raszterkép kockás vagy elmosódott lesz; a
  **vektorgrafika** alakzatok leírása (kör: középpont, sugár, szín), ezért bármekkorára nagyítható élesen.
  A **képszerkesztés** számokkal végzett művelet: tükrözés, forgatás, kivágás, kitöltés, világosítás,
  **retusálás**.
- **Kerettanterv:** „ismeri egy bittérképes rajzolóprogram használatát, azzal ábrát készít” ·
  „bemutatókészítő vagy szövegszerkesztő programban rajzeszközökkel ábrát készít” · „digitális képeken
  képkorrekciót hajt végre” · „Képszerkesztési műveletek: beillesztés, vágás, kitöltés, kijelölés,
  színválasztás, feliratozás, retusálás, képméret változtatása, transzformációk” · Fogalmak: „rajz,
  rasztergrafika létrehozása, rasztergrafika szerkesztése, rajzeszközök; […] transzformációk,
  színválasztás, retusálás, képméret változtatása” · tevékenység: „Bemutatókészítő vagy szövegszerkesztő
  programban vektorgrafikus rajzeszközökkel ábrakészítés”.
- **Tévhitek:** „A képernyő színei festékként keverednek: piros + zöld = barna.” (Fénynél sárga.) „A kis
  képet nagyítva több részlet jön elő.” (Nem: a pixelek csak nagyobbak lesznek – a „krimis nagyítás”
  mítosza.) „A vektoros kép is pixelekből áll a fájlban.” „A fehér a színek hiánya.” (Képernyőn mindhárom
  szín teljes erővel: 255, 255, 255.) „A nagyobb fájl mindig szebb kép.”
- **Kulcsvizuál:** egy saját rajzú „fénykép” (lecke-saját táj: alma a fán, raszterizálva `DigPixel.fromDraw`).
  Az 1. lépésben folyamatos nagyítás (zoom 1× → 40×) egy almára: előbukkannak a kockák, majd minden
  kockában a három szám. A 3. lépésben három fénykör (vörös, zöld, kék) sötét háttér előtti kis „ablakban”
  (a lap papír marad, a fényes keverés egy sötét keretes kijelzőn) – additív keverés. A 5. lépésben ugyanaz
  a betű/alma raszterben és vektorban, egymás mellett nagyítva: kockás vs éles (a vektor csomópontjai
  kis körökként).
- **Kipróbálom:** RGB-csúszkák (0–255) → a szín és a három bájt (DigBit 8 bites lámpasor csatornánként).
  Felbontás-kapcsoló 8 × 8 / 32 × 32 / 128 × 128 → a kép és a fájlméret (a kód számolja: sz × m × 3 bájt).
  Pixelrajzoló pad (16 × 16, `DigPixel.paint`: ceruza, kitöltés, radír) – a rajz számtáblája élőben.
  Művelet-gombok: tükrözés, forgatás 90°, világosítás (+40 minden számhoz), kivágás.
- **Tippelj!** 3. lépés: „Vörös fény + zöld fény = ? barna / sárga / fehér” → sárga. 5. lépés: „Melyik
  marad éles 10× nagyítva? a fotó / a vektoros alma / egyik sem” → a vektoros.
- **Lépések:** Nagyíts bele! – pixelek · Egy pixel = három szám · Fényből keverve: RGB · Felbontás és
  fájlméret · Nagyítás: raszter vs vektor · Mikor melyik? (fotó vs ábra, logó) · A képszerkesztés
  számtan (tükrözés, kitöltés, világosítás, retusálás) · Összefoglalás.
- **Adatok:** 8 bit/színcsatorna → 256 fokozat, 256³ = 16 777 216 szín *(számolt)*; Full HD 1920 × 1080 =
  2 073 600 pixel *(számolt)*, tömörítetlenül 3 bájt/pixel → 6 220 800 bájt ≈ 6,2 MB; egy tipikus 12
  megapixeles telefonfotó (4000 × 3000) tömörítetlenül 36 MB, JPEG-ben kb. 2–5 MB *(becslés)*. A
  képernyő alpixelei: fizika-7-8/13-szinek (ugyanaz a három szín).
- **Átfedés:** a fények összeadódása és a festékek kivonó keverése a fizika-7-8/13 6–7. lépésében van; itt
  egy lépés, a számok felől. A vektorgrafika csomópontjai, görbéi: 7–8. (6. témakör) – itt csak a fogalom.
- **Építőkocka:** **DigPixel** (referencia: `fromDraw`, `grid`, `zoom`, `resample`, `vector`, `rgb`,
  `paint`, `ops`), DigBit (`bits` csatornánként), TtTipp.
- **Meglévő anyag:** az `iskola/informatika-mnist.html` 2. lépése („A kép = 784 szám”) – az ötlet innen;
  PhET *Color Vision* (részben magyarul) *(nincs ellenőrizve)*.

### 14 · `14-hang-video` – Hogyan lesz a hangból szám? – mintavétel és képkocka

- **Tanulási cél:** A **digitalizálás** a folytonos jelet számsorrá alakítja. A mikrofon a levegő
  rezgését feszültséggörbévé alakítja; a gép ezt másodpercenként sokszor megméri (**mintavétel**), és
  minden mérést egy adott számú szintre kerekít (**bitmélység**). Több minta és több szint → hűbb hang,
  nagyobb fájl. A CD másodpercenként 44 100 mintát vesz, 16 biten. A **mozgókép** gyorsan egymás után
  mutatott állóképek (**képkockák**) sora; kb. 10–12 kocka/s fölött a szem mozgásnak látja, a film 24-et
  használ. A nagy fájlméret miatt **tömörítünk**.
- **Kerettanterv:** „digitális eszközökkel önállóan rögzít és tárol képet, hangot és videót” ·
  „Digitalizáló eszközök megismerése. Kép, hang és video digitális rögzítése” · Fogalmak: „kép, hang,
  video digitális rögzítése; digitalizáló eszköz” · tevékenység: „A saját eszközzel készített képből,
  videóból képrészlet kivágása” · (8.) Fogalmak: „digitalizálás, minőség”.
- **Tévhitek:** „A gép a hangot hangként tárolja.” „Minél több minta, annál hangosabb.” „A videó egy
  folyamatos film, nem képek.” „30 kocka/s kevés, a szem 100-at is lát.” *(óvatosan: a folyamatosság
  érzete és a villogás észlelése más; a panel csak a „mozgásnak látszik” küszöbről beszél)*. „A kisebb
  fájl ugyanolyan, csak összenyomták.” (A tömörítés egy része információt hagy el.)
- **Kulcsvizuál:** felül egy hanggörbe (BioPlot tengelyein, saját szinuszkeverék – egy kitalált
  „dallam”), rajta a mintavételi pöttyök függőleges szárakkal; alatta a kerekített lépcsős görbe. A
  mintavételi gyakoriság növelésével a lépcső simul. Jobbra a minták számai egy szalagon futnak ki, mint a
  bájtok (DigBit). A 6. lépésben pörgetőkönyv: egy pattogó labda 12 képkockája (DigPixel kis rácsok)
  egymás mellett, majd egymásra pörgetve; fps-csúszka.
- **Kipróbálom:** mintavételi gyakoriság (2 / 4 / 8 / 22,05 / 44,1 kHz – a kis értékek a kitalált
  dallamhoz méretezve) és bitmélység (2 / 4 / 8 / 16 bit) csúszka; ▶ meghallgatás (MagHang `unlock()` →
  saját `AudioBuffer` a mintákból – csak kattintásra, mérsékelt hangerő; hang nélkül is teljes).
  Fájlméret-számláló (a kód: minta/s × bit × csatorna × idő / 8). Képkocka/s csúszka 2–60.
- **Tippelj!** 3. lépés: „Hány mintát vesz a CD másodpercenként? 44 / 4410 / 44 100” → 44 100. 6. lépés:
  „Hány képkocka kell másodpercenként, hogy a labda folyamatosan mozogjon? 3 / kb. 12 / 100”.
- **Lépések:** A hang rezgés – a mikrofon görbéje · Mintavétel: pöttyök a görbén · Tippelj: a CD ·
  Hány szint? – bitmélység · Mekkora a fájl? · Mozgókép = képkockák · Videó: képek és hang együtt –
  miért tömörítünk? · Összefoglalás: digitalizálás.
- **Adatok:** CD-hang: 44,1 kHz, 16 bit, 2 csatorna (IEC 60908, „Red Book”) → 44 100 · 16 · 2 = 1 411 200
  bit/s *(számolt)* → 1 perc ≈ 10,6 MB *(számolt)*; tömörített zene 128 kbit/s-on ≈ 0,96 MB/perc
  *(számolt; a tömörítés fajtája a tanári megjegyzésben)*; az emberi hallás felső határa kb. 20 kHz
  *(becslés, korral csökken; ugyanaz a szám, mint a 07-ben)*; a mintavételnek a legmagasabb hang
  frekvenciájának több mint kétszeresének kell lennie (Nyquist–Shannon) – a panelen „kétszer olyan sűrűn”
  formában; 16 bit → 65 536 szint *(számolt)*; film 24 kocka/s, a hazai (PAL) tévé 25 kocka/s
  *(ellenőrizendő)*; a folyamatos mozgás érzete kb. 10–12 kocka/s fölött *(becslés, forrásonként eltér)*;
  Full HD videó tömörítetlenül 6,2 MB/kocka · 25 = kb. 155 MB/s *(számolt, a 13-mal közös konstansból)*.
- **Átfedés:** a hang fizikája (frekvencia, amplitúdó, hangmagasság): fizika-7-8/12 – itt nem ismételjük,
  csak „a görbe magassága a hangerő, a sűrűsége a hangmagasság” egy mondatban. Tömörítés, kódolási
  problémák: 7–8. (9. témakör).
- **Építőkocka:** DigPixel (képkockák `grid` kicsiben), DigBit (`bytes` szalag, `size`), MagHang
  (`unlock`, `ready`, `vol` – bájtra azonosan; a mintalejátszás lecke-saját, ugyanazokkal a szabályokkal),
  BioPlot (tengely, görbe), TtTipp.

### 15 · `15-labnyom` – Mit árulnak el rólad a nyomaid? – digitális lábnyom, adatvédelem, segítségkérés

- **Tanulási cél:** Minden online lépés nyomot hagy: amit posztolsz (**aktív lábnyom**), és amit a
  szolgáltatás rögzít rólad (hol, mikor, mit kerestél, mit kedveltél – **passzív lábnyom**). Ezekből
  **virtuális személyiség** (profil) áll össze, és erre épülnek az ajánlások. Egyenként ártatlan adatok
  együtt sokat elárulhatnak (iskola, utca, napirend). A **személyes adat** a tiéd: dönthetsz, kinek
  mutatod (láthatósági beállítás), de az elküldött kép másolata már nem a te kezedben van. Ha valaki
  online bánt (**internetes zaklatás**): nem a te hibád; ne válaszolj, mentsd el, tiltsd le és jelentsd,
  és szólj egy felnőttnek, akiben megbízol – a Kék Vonal is segít (116-111).
- **Kerettanterv:** (7.) „ismeri a digitális környezet, az e-Világ etikai problémáit” · „védekezik az
  internetes zaklatás különböző formái ellen, szükség esetén segítséget kér” · „Adatok biztonságos
  kezelése, technikai és etikai problémák” · „Az informatikai eszközök használatának következményei a
  személyiségre és az egészségre vonatkozóan” · Fogalmak: „virtuális személyiség; információs társadalom;
  adatbiztonság; adatvédelem; digitális eszközöktől való függőség” · tevékenység: „Megfigyelések végzése
  és értelmezése a közösségi portálokon, keresőmotorok használata közben rögzített szokásokról,
  érdeklődési körökről, személyes profilokról” · „Az elektronikus kommunikáció gyakorlatában felmerülő
  problémák megismerése, valamint az ezeket megelőző vagy ezekre reagáló biztonságot szavatoló
  beállítások megismerése, használata” · (2.) „Online identitás védelmében teendő lépések”.
- **Tévhitek:** „Ha törlöm, eltűnik.” (A képernyőkép, a továbbküldött másolat megmarad.) „Csak a barátaim
  látják.” (A beállítástól függ, és ők is továbbküldhetik.) „Egy fotó nem árul el semmit.” (Háttér,
  felirat, egyenruha, helyadat.) „Az ingyenes alkalmazás ingyen van.” (Az adataiddal és a figyelmeddel
  fizetsz – semlegesen, egy mondatban.) „Ha bántanak, az az én hibám / nem szabad szólnom.”
- **Kulcsvizuál:** egy kitalált gyerek („Zsófi”, monogram) egy kitalált napja idővonalon: reggeltől
  estig pöttyök, mindegyik egy nyom (poszt, keresés, helyadat, kedvelés) – két színnel: aktív (cinóber) és
  passzív (kékeszöld). A 3. lépésben öt poszt (DigUI `post`, saját egyszerű rajzokkal) – a diák a
  részletekre kattint (egyenruha-felirat, buszmegálló táblája, „minden kedden 5-kor edzés”), és a
  darabok egy kirakóvá állnak össze: „ezt tudhatja bárki”. A 5. lépésben láthatósági körök (csak én /
  ismerősök / ismerősök ismerősei / nyilvános) – kapcsolóval nő-csökken, és egy „képernyőkép” ikon a
  körön kívülre viszi a másolatot. A 7. lépésben (zaklatás) a bántó üzenet **elmosott buborék**, a
  szövege nem látszik; négy lépés kártyán: ne válaszolj · mentsd el · tiltsd le, jelentsd · szólj.
- **Kipróbálom:** a kirakós (kattintás a poszt részletére); a láthatósági kapcsoló; az „ajánló” lépésben
  (4.) a kedvelések kártyái (kitalált témák: foci, rajz, kutyák, főzés) húzhatók a profilba, és a
  „neked ajánlott” sáv ennek alapján változik *(modell)*. Kártyarendezés (TortCards): mi személyes adat?
  (név, lakcím, telefonszám, iskola, fotó, jelszó vs kedvenc szín, kedvenc könyv).
- **Tippelj!** 3. lépés: „Zsófi öt posztjából mit tudhat meg egy idegen? semmit / a kedvenc színét / hol
  és mikor található” → hol és mikor. 5. lépés: „Zsófi törli a posztot. Eltűnik mindenhonnan? igen / nem, ha
  valaki elmentette” → nem.
- **Lépések:** Egy nap nyomai · Aktív és passzív lábnyom · Öt ártatlan poszt (kirakós) · A profil és az
  ajánló · Ki látja? – láthatóság és másolat · Mi a személyes adat? · Ha online bántanak · Összefoglalás
  (mit tehetsz: gondold át, állítsd be, kérj segítséget).
- **Adatok:** a GDPR szerint Magyarországon a 16 év alattiak adatkezeléséhez (információs társadalmi
  szolgáltatásnál) szülői hozzájárulás kell *(ellenőrizendő: GDPR 8. cikk, Infotv. – a hazai korhatár)*; a
  közösségi oldalak jellemzően 13 éves kort írnak elő *(becslés, szolgáltatónként eltér – név nélkül)*;
  Kék Vonal Gyermekkrízis Alapítvány: 116-111, ingyenes *(ellenőrizendő: elérhetőség, nyitvatartás)*;
  jogsértő tartalom bejelentése: NMHH Internet Hotline *(ellenőrizendő)*. Zsófi, a posztok, a témák
  *(kitalált példa)*.
- **Átfedés:** a jelszó (06), az álhír (16). Az e-kereskedelem, az internetes bűnözés: 7–8. A „függőség”
  fogalma itt csak egy mondat az ajánló lépésben („az ajánló azt mutatja, amin megakad a szemed – te
  döntöd el, meddig maradsz”); az egészségi oldal a 17-ben.
- **Építőkocka:** **DigUI** (referencia: `phone`, `post`, `profile`, `toggle`, `notif`, `avatar`, `blurMsg`
  – a teljes katalógus, 4.2), TortCards, TtTipp; a kirakós és az idővonal lecke-saját.
- **Biztonsági és hangnemi szabály:** nincs ijesztő kép (sötét alak, figyelő szem, lakat-zsákutca), nincs
  „ragadozó” szó; a veszély a *másolhatóság* és az *összerakhatóság*, nem egy gonosz szereplő. A
  zaklatás áldozata semmilyen formában nem hibás; a lecke a szemlélőt is megszólítja („ha látod, hogy
  mást bántanak, ne továbbítsd, és szólj”).
- **Szakmai lektor:** `"review": ["online biztonság"]`.

### 16 · `16-alhir` – Igaz-e, amit a neten olvasol? – keresés, szűrés, álhír

- **Tanulási cél:** A kereső nem „tudja” a választ: a beírt **kulcsszavakhoz** keres oldalakat egy előre
  elkészített jegyzékből, és sorba rendezi őket. Jobb kulcsszó, **pontos kifejezés** (idézőjel) és
  **szűrés** (idő, típus, oldal) → jobb találat. A találati lista első helye nem a legigazabb; a
  **hirdetés** jelölve van. Az **álhír** szándékosan hamis vagy félrevezető hír; jelei: harsány cím,
  érzelemre hat, nincs szerző, dátum, forrás, furcsa webcím. Ellenőrzés: állj meg, nézd meg, ki írta, keresd
  máshol is, keresd az eredetit (a kép eredetijét is). Az adatbázisok **keresési űrlapját** mezőnként
  töltjük ki.
- **Kerettanterv:** „önállóan keres információt, a találatokat hatékonyan szűri” · „az internetes
  adatbázis-kezelő rendszerek keresési űrlapját helyesen tölti ki” · „Az információ szerepe a modern
  társadalomban” · „Információkeresési technikák, stratégiák” · tevékenység: „Érdeklődési körnek,
  tanulmányoknak megfelelően információk keresése valamelyik keresőmotorban, és a találatok hatékony
  szűrése” · „Nyilvános és baráti fórumba hozzászólás, posztolás, mások hozzászólásának értékelése”.
- **Tévhitek:** „Az első találat a legjobb / az igaz.” „Ha sokan megosztották, igaz.” „Ha van benne kép,
  igaz.” (A kép lehet régi, kivágott vagy máshonnan való.) „A kereső egész mondatot ért.” „Az álhírt
  mindig rosszakarók írják.” (Sokszor tévedés terjed – a lecke a szándékot nem találgatja.)
- **Kulcsvizuál:** DigUI `browser` + `search`: egy kitalált kereső találati listája egy valódi kérdésre
  („Milyen mély a Balaton?”) – a találatokban más-más szám (átlagos mélység vs legmélyebb pont): figyelmes
  olvasás. A 5. lépésben egy kitalált, ártalmatlan álhír-cikk (pl. „Jövőre eltörlik a nyári szünetet!”)
  `.example` címen, és mellette a jelek kártyái, amelyek a cikk részeire mutatnak. A 7. lépésben egy
  fotó (DigPixel): a teljes kép és egy kivágott részlete – a részlet mást sugall (pl. „üres strand” a
  kivágásban, tömeg a teljes képen).
- **Kipróbálom:** kulcsszó-építő: csempékből áll össze a keresés (kérdés mondatban / kulcsszavak / „pontos
  kifejezés” / + szűrő: év, típus); a találati lista *(modell: a lecke saját, kitalált jegyzékéből
  pontozva)* átrendeződik. Keresési űrlap (könyvtári katalógus, kitalált): szerző, cím, év mezőbe
  kártyák húzhatók; rossz mezőben 0 találat. Álhírjel-kártyák a cikk részeire (TortCards zónák). A 6.
  lépésben két kitalált cikk – „igaz vagy hamis?” – az ellenőrzés gombjaival (szerző, dátum, „keresd
  máshol”).
- **Tippelj!** 2. lépés: „Melyik keresés talál gyorsabban a Balaton legnagyobb mélységére? »milyen mély a
  balaton« / »balaton legnagyobb mélység« / mindegy” (a lecke modellje szerint a kulcsszavas; a panel
  kimondja: a mai keresők a kérdést is jól értik, a pontos kulcsszó mégis segít). 6. lépés: „Igaz-e a
  hír? igaz / hamis / nem tudom eldönteni, ellenőrizni kell” → ellenőrizni kell (az ellenőrzés után:
  hamis).
- **Lépések:** Hogyan keres a kereső? · Kulcsszó és pontos kifejezés · A találati lista olvasása
  (hirdetés, forrás, dátum) · Szűrés és keresési űrlap · Az álhír jelei · Igaz vagy hamis? – ellenőrizd! ·
  A kép is hazudhat (kivágás) · Összefoglalás: állj meg – ki írta? – keresd máshol – keresd az eredetit.
- **Adatok:** a Balaton átlagos mélysége kb. 3,2 m, legmélyebb pontja kb. 12,2 m (Tihanyi-kút)
  *(ellenőrizendő: KDTVIZIG / Balaton Limnológiai Kutatóintézet; a tankönyvek eltérő kerekítést is
  adnak)*; a lecke találati listája, cikkei, webcímei *(kitalált példa, `.example`)*. Az ellenőrzés
  négy lépése saját megfogalmazás Mike Caulfield SIFT-módszere nyomán *(ellenőrizendő a hivatkozás;
  szó szerinti átvétel nincs)*.
- **Átfedés:** a „Honnan tudjuk?” forráskritikai lépések a történelemsorozatban (tortenelem-5-6) – a
  gondolat ugyanaz, itt online forrásra. A digitális lábnyom és az ajánló (15) – az ajánló „buborékja”
  egy mondat.
- **Építőkocka:** DigUI (`browser`, `search`, `post`), DigPixel (`crop`), TortCards, TtTipp.
- **Tartalmi szabály:** a lecke nem használ valódi hírt, médiumot, közszereplőt, politikai, egészségügyi
  vagy vallási témát; a kitalált álhír ártalmatlan, iskolai témájú. „Hazug” vagy „buta” szó nem
  minősíti a terjesztőt.
- **Szakmai lektor:** `"review": ["online biztonság"]`.

### 17 · `17-szamitogep` – Mi történik, ha lenyomod az „A” betűt? – a gép részei, bit, bájt, fájl, mappa

- **Tanulási cél:** A számítógép **bemeneti** perifériákon át kap adatot (billentyűzet, egér, mikrofon),
  a **processzor** feldolgozza, a **memória** a munka közbeni adatot tartja, a **háttértár** kikapcsolás
  után is megőrzi, a **kimeneti** periféria (képernyő, hangszóró, nyomtató) megmutatja; az érintőképernyő
  mindkettő. A gépben minden **bit** (0 vagy 1, ki- vagy bekapcsolt). 8 bit = 1 **bájt**, ez 256-féle
  érték: egy szám, egy betű kódja (az „A” = 65 = 01000001), egy színcsatorna. A nagyobb egységek ezres
  lépcsők (kB, MB, GB, TB). A **fájl** névvel ellátott adat, a **mappák** fába rendezik; az elérési út a fa
  egy ága. Mentés nélkül a memória tartalma kikapcsoláskor elvész.
- **Kerettanterv:** „célszerűen választ a feladat megoldásához használható informatikai eszközök közül” ·
  „önállóan kezeli az operációs rendszer mappáit, fájljait és a felhőszolgáltatásokat” · „az informatikai
  eszközöket önállóan használja, a tipikus felhasználói hibákat elkerüli” · „értelmezi az informatikai
  eszközöket működtető szoftverek hibajelzéseit, és azokról beszámol” · „Az informatikai eszközök
  működési elveinek megismerése és használata” · „Az informatikai eszközök be- és kiviteli perifériái, a
  háttértárak, továbbá a kommunikációs eszközök” · „Az informatikai eszközök egészségre gyakorolt
  hatásai” · „Állományok tárolása, kezelése és megosztása a felhőben” · Fogalmak: „adat, információ, hír,
  digitalizálás, minőség, ergonómia, be- és kiviteli periféria, háttértár, kommunikációs eszközök, fájl,
  fájlműveletek, mappa, mappaműveletek, […] jogosultságok”.
- **Tévhitek:** „A számítógép = a monitor.” „A memória és a háttértár ugyanaz.” („Van 8 GB-om” – melyik?)
  „A gép betűket tárol.” (Számokat; a betű a kódtábla szerint lesz betű.) „Egy ékezetes betű is egy bájt.”
  (UTF-8-ban az „ő” két bájt.) „A kuka = törlés.” „A fájl a mappán belül fizikailag egy dobozban van.”
- **Kulcsvizuál:** egy sematikus asztali gép „átlátszó” nézetben (billentyűzet → kábel → doboz:
  processzor, memória, háttértár → kábel → képernyő). Az 1. lépésben *(lassítva)* a lenyomott „A”
  útja: a billentyű alatt jel → a processzor → a memóriában a 65 → a képernyőn a betű pixelei (DigPixel
  kis rács) kigyulladnak. A 3. lépésben nyolc kapcsoló (DigBit `bits`), alattuk a helyiértékek (128 … 1),
  a lámpák szerint a szám, a betű és a szín. A 5. lépésben mértékegység-létra (`ladder`): bájt → kB → MB → GB
  → TB, minden fokon egy kitalált, de reális példa (egy betű, egy oldal szöveg, egy fotó, egy film, egy
  osztálynyi fotóarchívum). A 7. lépésben a mappafa (MatGraf `tree`, balról jobbra): `Dokumentumok →
  Iskola → Digitális kultúra → plakat.docx`; az elérési út kiemelt ág.
- **Kipróbálom:** a 8 kapcsoló kattintható (érték, betű, szürke árnyalat egyszerre). Periféria-
  válogatás (TortCards: bemenet / kimenet / mindkettő / háttértár). „Áramszünet” gomb: mentés előtt és után
  (a memória dobozai kiürülnek, a háttértáré megmarad). Mappafa: fájlművelet-gombok (másolás = új levél a
  fán, áthelyezés = a levél átkerül, törlés = a kuka-ágra kerül, végleges törlés).
- **Tippelj!** 3. lépés: „Hány különböző értéket tud 8 kapcsoló? 8 / 16 / 256” → 256. 6. lépés: „Írsz egy
  fogalmazást, és mentés nélkül elmegy az áram. Mi marad meg? minden / semmi az új szövegből / a fele” →
  semmi az új szövegből (ami nem került a háttértárra).
- **Lépések:** Lenyomod az „A”-t – mi történik? · Bemenet, feldolgozás, kimenet (perifériák) · Bit és
  bájt · A betű is szám (az „ő” két bájt) · Mennyi az a gigabájt? · Memória és háttértár (Neumann János:
  a program is a memóriában – egy mondat) · Fájl, mappa, elérési út (és a felhő ugyanez másik gépen,
  jogosultsággal) · A gép és a tested – ergonómia, szünet · Összefoglalás.
- **Adatok:** „A” = 65 (ASCII, ISO/IEC 646; a Unicode első 128 jele ugyanaz) = 01000001 *(számolt)*; „ő” =
  U+0151, UTF-8-ban 2 bájt: C5 91 *(számolt)*; 1 kB = 1000 bájt, 1 KiB = 1024 bájt (IEC 80000-13);
  2^8 = 256 *(számolt)*; Neumann János 1945-ös EDVAC-jelentése (First Draft of a Report on the EDVAC) – a
  tárolt program elve *(ellenőrizendő a megfogalmazás)*; a létra példái *(becslés: egy oldal szöveg kb. 2–3
  kB, egy telefonfotó kb. 3 MB – a 13-mal azonos konstans, egy 2 órás film kb. 2–5 GB)*; ergonómia: a
  képernyő kb. karnyújtásnyira, a teteje szemmagasságban vagy kicsit alatta, rendszeres szünet *(becslés;
  forrás: munkavédelmi ajánlások, a gyártáskor egyeztetendő – a „20-20-20” szabály csak forrással)*.
- **Átfedés:** a kettes számrendszer a matematika-5-6/02-helyi-ertek 8. lépésében (13 = 1101) – itt a
  kapcsoló és a kód felől; a helyiérték-táblát nem ismételjük, csak hivatkozunk. Tömörítés, operációs
  rendszer segédprogramjai: 7–8.
- **Építőkocka:** **DigBit** (referencia: `bits`, `value`, `char`, `utf8`, `ladder`, `big`, `bytes`,
  `size`), MatGraf (`layout` + `tree` a mappafához), TortCards, DigPixel (opcionális: az „A” pixelei – ha
  a 13 előbb kész, különben lecke-saját 8 × 8 rács), TtTipp.

---

## 4. Közös modulok

### 4.1 Mi jön változatlanul (bájtra azonosan, szerződés 16.)

Az md5 a `/* ── MODUL:` sor elejétől a `MODUL VÉGE` sor végéig (az utolsó újsor nélkül, UTF-8) számolva,
2026-11-24. Bármelyik azonos md5-ű leckéből másolható; az „ajánlott forrás” a legfrissebb.

| Modul | Ajánlott forrás (blokk) | md5 | Lecke ebben a sorozatban | Mire kell itt |
|---|---|---|---|---|
| **TtTipp** | `termeszettudomany-5-6/16-folyo` | `fa839199626ca8aa31f3693a24150d81` | mind | „Tippelj!” fej, válaszsor, visszajelzés, bélyegek |
| **MatGraf** | `matematika-9-10/15-valoszinuseg` | `1aed606e543be455b8f7d9e1ba2269f7` | 01, 06, 17 | finomítási fa, a PIN-kód fája (`band`), mappafa |
| **TortCards** | `termeszettudomany-5-6/03-meres` (a 25 leckében egyező változat; a `tortenelem-5-6/18`-é eltér, ne onnan) | `2c411077c00d1ba0d984102651b64c44` | 05, 11, 15, 16, 17 | rendezés, párosítás |
| **TortTimeline** | `termeszettudomany-5-6/05-ido` | `9c5cebae791ce43f3d93b5f2785e6dfd` | 05 | az üzenetküldés időszalagja |
| **TortMap** v1.1 (+ `shared/tort/proj.js`, `map-vilag.js`) | `termeszettudomany-5-6/16-folyo` | `05bd08a1c2d32bdd050cba4c4fdbc2e2` | 05 | Európa-alap a csomagok útjához |
| **MagText** v1.1 | `magyar-5-6/13-pal-utcai-fiuk` | `c526552e07c94a1bd113056cc4a8e601` | 11 | szótagolás az elválasztáshoz |
| **MagHang** v1.1 | `magyar-5-6/01-kommunikacio` | `96d167766faa9b0fdbcc3aeb1dfa2c1b` | 14 | `unlock`, `ready`, `vol`, `stop` – a hangszabályok |
| **BioPlot** | `termeszettudomany-5-6/03-meres` | `c38b534d3ea4c947ce3ed4fe9dad5351` | 07, 08, 14 | élő görbe, küszöbvonal, hanggörbe tengelye |

Függőségek: a **TortMap** a `shared/tort/proj.js`-re épül (a 16-folyo `<script>`-sorrendje a minta). A
**MagHang** blokk nagy (487 sor), de csak a 14 használja – a szintézisrészeit nem hívjuk, a blokkot mégis
egészben másoljuk (szerződés 16.: párhuzamos változat nincs). A **TtTipp** maga teszi a `<head>`-be a
panel-elmosás CSS-ét. Az **MatGraf** címkéi `{s, k}` párok – a fájlneveket (`plakat.docx`) a `.md` adja.

### 4.2 Új modulok (hat)

A szerződés 16. fejezete szerint: a referencialeckében, külön MODUL-blokkban, `Dig…` névtérrel. Blokkhatár
egységesen: `/* ── MODUL: <név> (<Névtér>) · forrás: digitalis-kultura-5-6/NN-slug, <dátum> ── */` …
`/* ── MODUL VÉGE: <név> ── */`. Csak a Lesson motorra (`L.ctx`, `L.tx`, `L.pill`, `L.measure`,
`L.pointer`, `L.button`, `L.st`, `Lesson.U`, `Lesson.FONTS`) épülnek; minden felirat `{s, k}` párként
érkezik, és **csak** `L.tx`/`L.pill` írja ki (QA, review mód). Alfa: a modul az `o.a`-t a hívó
alap-alfájával szorozva **állítja** (a TtTipp mintája, 6. tanulság), a vonalstílust visszaállítja. Minimális
betűméret a vásznon 22 px, blokkfelirat 24 px. Ikonok (▶, lakat, kuka, mappa, lámpa, pipa, X): **rajzolt
útvonalak, nem Unicode-jelek vagy emojik** (a három fontban nincsenek, tartalékfontra esnének).

| Modul | Referencialecke | Átvevők | Mi a lényege |
|---|---|---|---|
| **DigBlock** – blokkszerkesztő és értelmező | `02-ciklus` | 01, 03, 04, 07, 08, 09 | saját blokknyelv, szerkesztés, determinisztikus futás-nyomvonal, kiemelés, változónézet, folyamatábra, szöveg |
| **DigRobot** – asztal- és rácsrobot | `02-ciklus` (v1.0), `07-szenzor` (v1.1) | 04, 08, 09 | felülnézeti robot, toll, falak, szenzorok, motorvezérlés; a DigBlock „világa” |
| **DigDoc** – dokumentum és diakocka | `10-formazas` | 11, 12 | oldal, bekezdés, karakter rétegei, rejtett jelek, stílus, kép, dia, távolsági elmosás |
| **DigPixel** – raszter, vektor, RGB | `13-pixel` | 14, 16, (17) | pixelrács, zoom, újramintavétel, vektoralak, RGB-keverő, rajzolópad, képműveletek |
| **DigBit** – bit, bájt, kód | `17-szamitogep` | 05, 06, 13, 14 | kapcsolósor, érték, karakterkód, UTF-8, mértékegység-létra, nagy számok |
| **DigUI** – semleges képernyő-elemek | `15-labnyom` | 04, 05, 06, 16 | telefon, böngésző, csevegés, e-mail, poszt, profil, kereső, belépés, kapcsoló, értesítés |

#### DigBlock – blokkszerkesztő és értelmező · referencia: `02-ciklus`

**Miért kell?** Hat lecke ír és futtat programot. A program futását mindegyiknek ugyanúgy kell mutatnia
(kiemelés, változók, lépésenkénti futtatás), és visszaléptetéskor, QA-ban determinisztikusnak kell
lennie. Ez a sorozat legnagyobb ismétlődő kódja.

**Vizuális nyelv** (0. döntés, 4.; színek: 7. fejezet táblázata): papír alapú, lekerekített (r = 10)
blokk, tinta szöveg (Bricolage 600, 24–26 px), bal szélén 16 px-es kategóriasáv rajzolt ikonnal. A
paraméter kategóriaszínű keretes kapszula; kattintásra léptet (szám: ±lépés vagy értéklista; választó:
következő elem). A tartalmazó blokk (ciklus, elágazás) fejlécsávja után a törzs 36 px-szel beljebb, bal
oldalán kategóriaszínű sín, alul záró sáv („ismétlés vége”, „elágazás vége”). Kirakós-fül, színes
kitöltés fehér betűvel **nincs**. A futó blokk 3 px-es cinóber keretet kap, a lefutott halványabb pipát
(rajz). A feltétel kiértékelése a blokk mellett pill: „IGAZ” (kékeszöld) / „HAMIS” (halvány tinta).

```text
── Program (adat, nem rajz) ──
DigBlock.prog(spec) → P        a spec beágyazott tömb, pl.
     [['indításkor'], ['ismételd', 4, [['lépj', 100], ['fordulj', 'jobbra', 90]]]]
     ['ha-különben', ['<', ['érzékelő', 'távolság'], 20], [[…]], [[…]]]
   A P csomópontjai {id, op, args, body?, alt?} – az id az út a fában ('0', '1.b.0', '1.a.1'),
   determinisztikus. DigBlock.clone(P), DigBlock.equal(P, Q), DigBlock.count(P).
DigBlock.BLOCKS[op] → {kind, args: [{t: 'szám'|'irány'|'választó'|'logikai'|'érték'|'változó'|'szöveg',
     min, max, step, opts}], body: 0|1|2, shape: 'utasítás'|'feltétel'|'érték'|'esemény'}
   Katalógus (v1.0-ban TELJES):
   esemény    indításkor · kattintáskor (cél) · gombra (gombkulcs)
   mozgás     lépj (n) · fordulj (balra|jobbra, fok) · (rács:) lépj egyet · fordulj balra · fordulj jobbra
   toll       tollat le · tollat fel · tollszín (szín)
   vezérlés   ismételd (n){} · amíg (feltétel){} · mindig{} · ha (f){} · ha-különben (f){}{} · várj (mp) · állj
   érzékelés  érzékelő (név) → érték · ütközik? → logikai · fal elöl? / fal jobbra? / fal balra? (rács)
   adat       legyen (változó, érték) · növeld (változó, d) · változó (név) → érték · kérdezd (kérdés,
              [válaszok]) → válasz
   művelet    + − · : · < > = ≤ ≥ · és · vagy · nem · összefűz (a, b) · véletlen (a, b) (seedelt)
   kimenet    mondd (érték)
   saját      lépés (md-kulcs) – lecke-definiálta művelet a világ adapterének (01: „vágj egy szeletet”)
DigBlock.def(op, desc)           lecke-saját blokk felvétele (csak 'saját' kategóriába)
   Felirat: a .md `<op> blokk` kulcsa, a paraméterhelyek #-jellel („lépj előre # lépést”). Az init a #-ek
   számát összeveti az args hosszával; eltérésnél console.error (a QA JS-hibának látja).
   Típusok: szám és szöveg külön (a '+' csak számra; szövegre hibát ad: {err: 'típus', id}); az
   összefűz szöveget ad. A kérdezd válasza mindig szöveg; a 'szám(…)' átalakítást a 04 nem használja – a
   „tizenegy” bemenet a '+' blokkon hibát ad (ez a tananyag).

── Futás (determinisztikus nyomvonal) ──
const R = DigBlock.run(P, world, o)
   world: adapter {init() → s, act(s, op, args) → {s, dur}, sense(s, name) → érték, lerp(s0, s1, u) → s}
   (a DigRobot.world ezt adja; a 01, 03 lecke-saját világa is ezt valósítja meg)
   o = {maxSteps: 2000, seed: 1, events: [{t, name, target}] (04: kattintások), tick: .15 (mp: egy
        vezérlőblokk kiértékelésének látható ideje), vars: {kezdőértékek}}
   → R = {frames: [{t0, t1, id, op, s0, s1, vars, val, test: true|false|null, err}], T (teljes idő),
          end: 'kész' | 'korlát' (maxSteps → „végtelen ciklus?”) | 'hiba', err: {id, k}}
   Az eseménykezelők egyszálúan, sorban futnak (egy kezelő végig, aztán a következő esemény) – egyszerű,
   determinisztikus; párhuzamos szál nincs.
R.at(t) → {i, frame, id, s (a világ állapota lerp-pel), vars, done: [id…]}   tisztán az időből
R.next(t) / R.prev(t) → a következő / előző blokkhatár ideje („egy lépés” gomb, töréspont)
R.until(t, pred) → az első frame-idő, ahol pred(frame) igaz (töréspontok: pred = f => bp.has(f.id))

── Szerkesztő ──
const E = DigBlock.editor(L, {x, y, w, h, prog: P, palette: [op…] | null, edit: 'nincs' | 'paraméter' |
                              'sorrend' | 'teljes', maxBlocks: 20, font, onChange(P)})
E.update()                  a draw-ból hívva: L.pointer alapján húzás, beszúrás, törlés (a palettára húzva),
                            paraméter-léptetés; az átrendezés animált (.25 mp), a végállapot zárt
E.draw({a, run: R, t, hi, bp: Set(id), dim: [id], scale})    rajz (a run + t alapján kiemel)
E.prog() → P · E.set(P) (animáció nélkül – enter()-ben, QA-állapotban) · E.version (szám, változáskor nő)
E.hit(px, py) → {id, part: 'blokk'|'paraméter'|'sín'|null} · E.box(id) → {x, y, w, h} (nyílhoz, címkéhez)
E.toggleBp(id)             töréspont ki/be (cinóber pötty a blokk bal szélén)

── Segédnézetek ──
DigBlock.controls(L, {run, step, reset, speed: [.5, 1, 4, 'azonnal']}) → gombok (L.button), a feliratuk a
     .md-ből: 'futtatás gomb', 'egy lépés gomb', 'alaphelyzet gomb', 'sebesség csúszka'
DigBlock.clock(L) → {t(), start(), pause(), seek(t), speed}   a futás órája L.st-ből (nem valós időből):
     t = (L.st − t0) · speed, szünetben rögzített – így visszaléptetés és QA (`__lesson.st`) azonos képet ad
DigBlock.watch(L, vars, {x, y, prev, t, a})   változódobozok (címke + érték; változáskor a régi érték kiugrik,
     az új beúszik .3 mp alatt)
DigBlock.flow(L, P, {x, y, s, hi, a})          ugyanaz folyamatábrán (ovális start/stop, téglalap, rombusz,
     visszacsatoló nyíl a ciklusnál) – legfeljebb kb. 12 csomópont
DigBlock.text(P) → [{s, k, depth, id}]         pszeudokód-sorok a .md feliratokból („ha … akkor”) – a 01
     háromféle leírásához; a hívó írja ki L.tx-szel
```

**Nem része a modulnak:** a világok rajza (DigRobot; a 01 konyhája, a 03 szalagja lecke-saját).
**Teljesség az első körben:** a katalógus minden blokkja működik a 02-ben (ott csak a mozgás, a toll és
a ciklusok látszanak). A referencialecke ügynöke a jelentésében egy rövid futási próbát ad meg (a 03, 04
és a 09 mintaprogramja, a terv 3. fejezetéből) – a próbát a saját munkamappájában futtatja, a leckébe nem
kerül rejtett tesztállapot.

#### DigRobot – asztal- és rácsrobot · referencia: `02-ciklus` (v1.0), `07-szenzor` (v1.1)

**Miért kell?** Öt lecke mozgat robotot (02, 04, 07, 08, 09); kettő rácson, három asztalon, három
szenzorral. A robot és a világ fizikája egyetlen, zárt modell: a DigBlock nyomvonala ebből számol.

**Rajz:** felülnézet. Kör alakú test (tinta körvonal, papír kitöltés), két kerék oldalt (sötét téglalap), elöl
irányjelző ék. **Nincs arc, szem, mosoly.** A szenzorok kis műszaki elemek a helyükön: az ultrahangos
egy rácsos téglalap elöl (nem két kör – ne „szemnek” lássék), a fényérzékelő kis négyzet a test alatt
(halvány fényfolttal), az ütköző ív elöl. A toll a középpontban; a nyom tinta (vagy `tollszín`).

```text
── v1.0 (02-ciklus) ──
const W = DigRobot.world({
   mode: 'asztal' | 'rács',
   size: [w, h]  (asztal: cm; rács: cellák száma), cell: 1,
   walls: [[x1, y1, x2, y2], …]  (asztal: cm-ben; rács: cellaélek: [cx, cy, 'É'|'K'|'D'|'Ny']),
   obstacles: [{x, y, w, h} | {x, y, r}],
   start: {x, y, dir (fok, 0 = a vászon teteje / É, óramutató szerint)},
   robot: {r: 6 (cm), bumper: true},
   speed: {v: 20 (cm/s), w: 90 (fok/s)}, pen: {down: false, col: tinta, w: .4 (cm)}
})  → W, egyben DigBlock-világ: W.init(), W.act(s, op, args), W.sense(s, name), W.lerp(s0, s1, u)
   Az állapot s = {x, y, dir, pen, col, trail: [[x, y, col]…] (csak indexhatár – a nyom a frame-ekből
   rajzolódik), bump: false, cells (rács: bejárt cellák)}
   Ütközés: az act a falig megy, ott megáll, s.bump = true, a dur a valódi megtett úthoz igazodik.
DigRobot.view(L, W, {x, y, w, h, fit: true}) → V   leképezés: V.px(x, y), V.s (px/cm), a rács vagy az
   asztallap rajzáig
DigRobot.draw(L, W, V, s, {a, trail: R (nyomvonal) + t, grid: true, labels: {k…}, ghost: s2 (a várt
   végállapot halványan), hl})
DigRobot.trailTo(R, t) → vonalszakaszok a t időig (a nyom a nyomvonalból, nem halmozott állapotból:
   visszaléptetés-biztos)

── v1.1 (07-szenzor) – csak hozzáad ──
W = DigRobot.world({…, robot: {…, sensors: [
       {id: 'távolság', type: 'ultrahang', ang: 0, range: [2, 400] (cm), cone: 15 (fok)},
       {id: 'bal fény', type: 'fény', dx: −3, dy: 5 (cm, a robothoz képest)},
       {id: 'ütköző', type: 'érintés'}]},
     floor: [{path: [[x, y]…], w: 2 (cm), col: '#1c2440'}] (padlóvonal: 08),
     noise: {seed, amp} (± mérési zaj, seedelt, az időből – nem képkockából)})
W.sense(s, 'távolság') → cm | null (nincs visszhang: a ferde/puha fal a `walls` elem `kind: 'ferde' |
   'puha'` jelzőjéből) · W.sense(s, 'bal fény') → 0..100 (a padlóvonal lefedettsége a szenzorfolt alatt,
   fehér 90, fekete 10 – modell) · W.sense(s, 'ütköző') → logikai · rácsban: 'fal elöl', 'fal jobbra',
   'fal balra' → logikai
DigRobot.echo(L, W, V, s, u, o)   ultrahang-impulzus: u 0..1 az oda-vissza út (ívek ki, visszaverődés,
   vissza); o.slow: lassítás-bélyeg; visszaadja {d (cm), ms (oda-vissza idő a hangsebességből – a
   hangsebesség a hívó .md-adata: o.c, m/s)}
DigRobot.rays(L, W, V, s, o)      a szenzorok érzékelési tartománya halványan (kúp, folt)
DigRobot.motor(W, s0, ctl, o) → R  folyamatos vezérlés: ctl(s, sense) → {bal, jobb} (kerékseb. −1..1),
   o = {T: 20 (mp), dt: .02 (rögzített vezérlési ütem), base: 20 (cm/s)} → ugyanolyan nyomvonal-objektum,
   mint a DigBlock.run-é (R.at(t), R.frames) – a vonalkövető és a 07 akadálykerülője így ugyanúgy
   rajzolható, léptethető és fotózható. A ctl lehet egy DigBlock-program fordítása is:
   DigRobot.fromProg(P) → ctl (a 'mindig' törzsét minden ütemben kiértékeli).
```

#### DigDoc – dokumentum és diakocka · referencia: `10-formazas`

**Miért kell?** A 10, 11 és 12 ugyanazt a „lapot” rajzolja: mért tördelés, formázás rétegenként, rejtett
jelek, kép, és a diakocka ugyanezzel a tipográfiával. A tördelés a `L.measure`-re épül (nincs fix doboz;
a Windows-on eltérő font is helyesen tördel).

```text
const D = DigDoc.create(L, {page: {w: 210, h: 297 (mm), margin: [25, 25, 25, 25] (fent, jobb, lent, bal)},
                            scale: px/mm, x, y})
D.para({runs: [{s, k, font: 'talpas'|'talpatlan'|'egyenlő' (→ Fraunces / Bricolage / JetBrains Mono),
               size: pont, b, i, u, col}],
        align: 'balra'|'középre'|'jobbra'|'sorkizárt', indent: {first, left, right} (mm),
        before, after (pont), line: 1,15, style: 'Címsor' | null}) → p
D.styles = {Címsor: {size, b, font, after}, Normál: {…}}   D.applyStyle(név, változás) – minden p, amelynek
   style-ja ez, átveszi (a kézzel formázott nem)
D.image({src: (c, w, h) => rajz, w, h (mm), wrap: 'sorban'|'körbefuttatás'|'mögötte', keepRatio: true,
         handle: null|'oldal'|'sarok'}) → img (a 11 torzítás-demója: keepRatio: false + 'oldal')
D.layout(o) → lines   mért tördelés: o.width (hasábszélesség mm-ben, alap: a margók között), o.hyph(word)
   → [elválasztási indexek] (visszahívás: a 11 MagText-tel adja; nélküle nem választ el), o.manual:
   kézi kötőjelek megtartása (a 11 tévhit-demója)
D.draw({a, marks: 0..1 (rejtett jelek: ¶ bekezdésvég, · szóköz, → tabulátor – rajzolt jelek, nem
        betűk), explode: 0..1 (rétegek ál-3D-ben szét: oldal, bekezdés-dobozok, karakter-dobozok),
        layers: {oldal, bekezdés, karakter} (kiemelés 0..1), cards: true (tulajdonságcédulák a
        rétegek mellett, a .md-ből), ruler: true (vonalzó margó- és behúzásfogóval), hi: {p, run},
        squiggle: [{p, from, to}] (helyesírás-aláhúzás, cinóber hullám)})
D.hit(px, py) → {p, run, ch, part: 'margó'|'behúzás'|'kép-sarok'|'kép-oldal'|null}
DigDoc.spaceAlign(text, nSpaces) → a sor elejére tett szóközökkel „igazított” bekezdés (align: 'balra'):
   a 10 tévhit-demója – betűtípus-cserénél a kód nem igazít utána, ezért csúszik szét
DigDoc.slide(L, {x, y, w, h (16:9), title, bullets: [{s, k}], img, bg, fg, anim: [{id, at}], u}) – diakocka
   ugyanezzel a tipográfiával
DigDoc.blurAt(L, draw, dist, o) – a dia képe dist méterről: kis offscreen vászonra rajzol, majd simítva
   felnagyít (minden böngészőben azonos; a ctx.filter nem kell); az elmosás mértékét a hívó számolja
   (a 12 látásélesség-modellje)
```

#### DigPixel – raszter, vektor, RGB · referencia: `13-pixel`

```text
img = {w, h, d: Uint8ClampedArray (r, g, b soronként)}     – minden művelet új img-et ad (tiszta függvény)
DigPixel.fromDraw(w, h, fn(c, w, h)) → img     raszterizálja a lecke saját rajzát (offscreen vászon)
DigPixel.grid(L, img, {x, y, px (cellaméret), a, lines: 0..1 (rácsvonal), nums: 0..1 (a cellában a
   három szám, csak ha px ≥ 64 – különben nem ír, 22 px-es szabály), hi: [[i, j]…], from: rect (részlet)})
DigPixel.zoom(L, img, {from: rect (forrás), to: rect (képernyő), u (0..1 zoomszint), mode:
   'kockás' (legközelebbi szomszéd) | 'simított' (bilineáris)})
DigPixel.resample(img, w2, h2, mode) → img
DigPixel.vector(L, shapes, {x, y, s, nodes: 0..1, a}) – shapes: [{t: 'kör'|'ellipszis'|'sokszög'|'görbe',
   pts, r, fill, stroke}] – bármilyen s-nél éles; a csomópontok kis körök
DigPixel.rgb(L, {x, y, r, g, b, a, lights: true (három fénykör additív keveréssel, 'lighter' komp.)})
DigPixel.paint(L, img, {x, y, px, tool: 'ceruza'|'kitöltés'|'radír', col}) → img' (a draw-ból, L.pointer
   alapján; a kitöltés 4-szomszédos, iteratív – nincs rekurzió)
DigPixel.ops: flipH(img) · flipV · rot90 · crop(img, rect) · bright(img, d) · fill(img, i, j, col) ·
   gray(img) · retouch(img, rect, from) (egyszerű folt-másolás – „retusálás”)
DigPixel.size(w, h, bpp = 24) → bájt (a fájlméret-kiírások egyetlen forrása)
```

#### DigBit – bit, bájt, kód · referencia: `17-szamitogep`

```text
DigBit.bits(L, v, {x, y, n: 8, s: 56 (lámpaméret), place: true (helyiértékek alatta: 128 … 1), hi,
   click: true, a}) → {v', hit}   kapcsoló/lámpasor; kattintásra billen (a hívó tárolja az értéket)
DigBit.value(bits) · DigBit.toBits(v, n)
DigBit.char(v) → jel | null    (32–126 ASCII; a többihez null → a hívó „nem betű”-t ír)
DigBit.utf8(ch) → [bájtok]    (pl. 'ő' → [0xC5, 0x91]); DigBit.hex(b) → 'C5'
DigBit.ladder(L, {x, y, w, h, steps: ['bájt', 'kB', 'MB', 'GB', 'TB'], base: 1000, ex: [{s, k}…]
   (példák fokonként), hi, u})
DigBit.big(n) → {s ('218 billió'), pow ('2,2 · 10¹⁴'), words}   nagy számok magyarul (ezer, millió,
   milliárd, billió, billiárd, trillió – hosszú skála), a felső index rajzolt, nem Unicode-függő
DigBit.bytes(L, arr, {x, y, cell, per: 8, u (kifutás 0..1), hi, hex: false})  bájtszalag (IP-cím, minták)
DigBit.size(b, base = 1000) → {v, u, s ('10,6 MB')}   (magyar tizedesvesszővel, U.fmt-tel)
```

#### DigUI – semleges képernyő-elemek · referencia: `15-labnyom`

**Szabály** (7. fejezet): valódi alkalmazás kinézete, logója, színei, neve nem jelenhet meg. Saját,
semleges, papírszerű stílus: lekerekített keret, tinta körvonal, a projekt színeiből. Személy: monogramos
kör (két betű a `.md`-ből), nincs arc, fotó. Webcím: csak `.example`. Minden szöveg `{s, k}`.

```text
DigUI.phone(L, {x, y, h, a}) → rect          telefonkeret (képernyő-téglalapot ad vissza)
DigUI.browser(L, {x, y, w, h, url: {s, k}, lock: true|false|null, a}) → rect   (lakat: rajz)
DigUI.chat(L, rect, msgs: [{who: 'én'|'ő', s, k, t, seen, blur: false}], {u (megjelenés 0..1), a})
DigUI.mail(L, rect, {from, to, cc, subj, body: [{s, k}], att}, {hl: 'tárgy'|'címzett'|…, a})
DigUI.post(L, rect, {who: {init, name: {s, k}, col}, s, k, img: (c, w, h) => rajz, likes, vis:
   'nyilvános'|'ismerősök'|'csak én', loc: {s, k} | null, t}, {hl: [részletkulcs], a}) → {parts: {kulcs:
   rect}} (a 15 kirakósa a részletek dobozait kapja vissza)
DigUI.profile(L, rect, {who, tags: [{s, k}], recs: [{s, k}]}, {u, a})
DigUI.search(L, rect, {q: [{s, k}] (csempék), results: [{title, url, snippet, ad: false, date}], hl, u})
DigUI.login(L, rect, {user: {s, k}, pass: [{t: 'kis'|'nagy'|'szám'|'jel'|'szó', s}] (csempék – a jelszó
   csak csempe, nincs beviteli mező), twofa: false, meter: 0..1 | null})
DigUI.toggle(L, x, y, on, {k, a}) · DigUI.notif(L, x, y, {s, k}, {u, a}) · DigUI.avatar(L, x, y, r, {init,
   col}) · DigUI.blurMsg(L, x, y, w, h, {a}) (a bántó üzenet: elmosott buborék, olvasható szöveg nélkül)
```

**Nem kell új modul** (lecke-saját marad): a konyha és a robotkar (01), a válogatószalag (03), a
szavazógép (04), a csomaghálózat és a kábelvágás (05), a logaritmikus idősáv (06), a visszacsatolási kör
(08), a teszttábla (09), a tájrajz (11), az osztályterem-metszet (12), a pörgetőkönyv labdája (14), a nap
idővonala és a kirakós (15), a kereső pontozása (16), a gép átlátszó rajza (17).

### 4.3 Referencialeckék – az első kör

| Lecke | Mit épít / próbál ki | Miért ez |
|---|---|---|
| **02-ciklus** | **DigBlock** (teljes katalógus, szerkesztő, nyomvonal, `clock`, `watch`, `flow`, `text`) + **DigRobot** v1.0 (asztal, rács, toll, falak, ütköző) | a gerinc; itt dől el, hogy a futás az időből determinisztikus, visszaléptethető és QA-zható-e, és hogy a blokknyelv kivetítve olvasható-e |
| **10-formazas** | **DigDoc** (rétegek, rejtett jelek, stílus, `spaceAlign`, vonalzó) | a mért tördelés a legkényesebb (Windows-fontok!); a 11 és a 12 erre épül |
| **17-szamitogep** | **DigBit** (minden függvény, a `big` is – a 06 ezt örökli) | kicsi, jól ellenőrizhető, és a 05, 06, 13, 14 alapja |
| **15-labnyom** | **DigUI** (a teljes katalógus, a `login`, `search`, `browser` is – a 05, 06, 16 örökli) | a hangnem és a semleges stílus mintája az összes online leckének; a lektorálás korán indulhat |

A 2. kötegben: **07-szenzor** → DigRobot v1.1 (szenzorok, `motor`, `echo`); **13-pixel** → DigPixel. Az első
kör után a koordinátor átnézi a négy modult (API, 22–24 px, alfa, rajzolt ikonok, determinizmus), és csak
utána indul a 2. köteg.

---

## 5. Build-, QA- és motorigények

### 5.1 A helyzet (ellenőrizve: `tools/build_lesson.py` fejléce, `shared/lesson.js` fejléce, 2026-11-24)

Minden, ami a gyártáshoz **kell**, már megvan:

| Igény | Megoldás a meglévő eszközökkel |
|---|---|
| 45 szavas panel | spec `"maxWords": 45` |
| lektorálás jelzése (06, 15, 16) | spec `"review": ["online biztonság"]` → a build kéri a `<!-- Szakmai ellenőrzés: … -->` blokkot |
| forrás minden adathoz (05, 06, 13, 14, 17) | spec `"sources": true` |
| becslés, modell jelölés | „kb.”, „(becslés)”, „(modell)” → `est`, `model` |
| időtartamok (5,8 ms, 3,5 perc, 1,4 millió év) | `"dim": "idő"` (ms, s, perc, óra, nap, év; szorzószó: „1,4 millió év”) |
| frekvencia, adatmennyiség (44,1 kHz, 1500 bájt, 10,6 MB) | `number` rögzített spec-egységgel (`"unit": "kHz"`, `"MB"`) – átváltás nélkül |
| listák (almaméretek, 03; pályák, 09) | `list` (`"len"`, `min`/`max`) |
| programok, blokkfeliratok | `### Feliratok`: `<op> blokk` kulcsok, `#` paraméterhellyel; a program szerkezete kód |
| pointer-húzás, kattintás | `L.pointer` (`pressed`, `released`, `events`) |
| hang (14) | MagHang + a magyar sorozat QA-hangpróbája (kattintás nélküli `AudioContext` → `!`) |
| QA-állapotok (programváltozat, futás közepe) | `__qaStates` + `--states` (állapot `set` nélkül is, BUILD-3-KOR 4.) és `--at idle` |

**Új build-, QA- vagy motorfunkció a gyártáshoz nem kell.** Billentyűzetes bevitel sem (0. döntés, 7.).

### 5.2 Kis, nem blokkoló javaslatok (a koordinátornak)

1. **`"dim": "adat"`** a buildben: bit, bájt, kB, MB, GB, TB (1000-es lépcső) + KiB, MiB, GiB (1024), alap:
   bájt. Haszna: a 13, 14, 17 egységet válthatna („3 MB” és „3000 kB” ugyanaz), és a build ellenőrizné a
   „kB” vs „KB” írásmódot (a „KB” figyelmeztetés). Addig `number` rögzített egységgel.
2. **`"dim": "frekvencia"`**: Hz, kHz, MHz, GHz (07, 14, 17). Addig rögzített egység.
3. **Glifpróba a DK-sorozatban is** (a magyar QA mintájára): ¶ · → „ ” – … ≤ ≥ ≠ · ⁰–⁹ mind a négy
   fontváltozatban. A rajzolt ikonok szabálya (4.2) mellett ez kiszűri, ha egy lecke mégis Unicode-jelet
   ír (▶ ✓ ✗ 🔒).
4. **QA-konvenció a programleckékhez** (nem funkció): minden futtatható lépésben `__qaStates`-ben
   `fut-közben` (a nyomvonal felénél) és `fut-vége`, a hibakereső leckében `töréspont`, a végtelen
   ciklusnál `korlát`. A 7. fejezet rögzíti.
5. A hat `Dig…` modul az első kör után a `shared/dig/` alá kerülhet (egyeztetve), mint a többi tantárgyi
   modul később.

### 5.3 A szerződés kiegészítése

A 7. fejezet kész szövege a `SZERZODES.md` 19. fejezeteként beillesztve (2026-11-24).

---

## 6. Gyártási sorrend és lefedettség

### 6.1 Gyártási sorrend (legfeljebb 5 párhuzamos lecke kötegenként)

Egyszerre legfeljebb 5 al-ügynök fut. Minden al-ügynök saját, egyedi scratchpad-almappát kap
(`EJSZAKAI-GYARTAS.md`, 8. tanulság).

| Köteg | Leckék (nehézség) | Új modul | Újrahasznosított |
|---|---|---|---|
| 1 | **02-ciklus** (3), **10-formazas** (3), **17-szamitogep** (3), **15-labnyom** (3) | DigBlock + DigRobot v1.0 (02) · DigDoc (10) · DigBit (17) · DigUI (15) | TtTipp, MatGraf, TortCards |
| 2 | **07-szenzor** (3), **13-pixel** (3), **01-algoritmus** (2), **03-elagazas** (2), **05-csomagok** (2) | DigRobot v1.1 (07) · DigPixel (13) | DigBlock, DigRobot, DigBit, DigUI, BioPlot, MatGraf, TortMap, TortTimeline, TortCards |
| 3 | **08-vonalkoveto** (3), **14-hang-video** (3), **04-valtozo** (2), **11-dokumentum** (2), **06-jelszo** (2) | – | DigRobot v1.1, DigBlock, DigPixel, DigBit, DigDoc, DigUI, MagText, MagHang, BioPlot, MatGraf |
| 4 | **09-labirintus** (2), **12-bemutato** (2), **16-alhir** (2) | – | DigRobot, DigBlock, DigDoc, DigUI, DigPixel, TortCards |

Indoklás: az 1. köteg csak referencialeckékből áll, mert a sorozat 17 leckéjéből 14 új modulra épül – egy
rossz API itt sokszorozódna. A **02** egyedül két modult épít (DigBlock + DigRobot), ez a legkockázatosabb
lecke: ha a köteg végére nem készül el, a 2. kötegből a 07, 01, 03 vár rá, a 13 és a 05 nem. A **15** azért
került előre, mert a lektorálást kérő online leckék (06, 16) hangnemét és DigUI-stílusát ő adja; a 06 és a
16 a 3–4. kötegben a lektori visszajelzés után készül. A **07** a 2. kötegben bővíti a DigRobotot (v1.1);
a 08 és a 09 ezt örökli, ezért későbbi. A **09** az utolsó programozós lecke: a hibakereső felületet a
02–08 tapasztalata alapján lehet a legjobban kitalálni. Becsült költség az `EJSZAKAI-GYARTAS.md` és a
kerethasználati jegyzet alapján: 17 lecke × ~0,45 % ≈ **7–8 % heti keret**; a négy referencialecke
modulmunkája miatt inkább a felső érték, kb. 4 köteg × 45–60 perc falióra.

### 6.2 Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / fejlesztési feladat |
|---|---|---|
| 1. Algoritmizálás és blokkprogramozás (14) | 01, 02, 03, 04, (09) | **„Projektmunkában egyszerű részekre bontott feladat elkészítése”** – csak a finomítás (01) és a tesztelés (09) szintjén; valódi projekt, csoportmunka nincs. Az animáció programozása csak tollrajzként (02, 04), sprite-mozgatás nincs. „Ciklusok fajtái” közül a hátultesztelő nincs külön (csak „amíg”, számlálós, végtelen). |
| 2. Online kommunikáció (5) | 05, 06, (15) | e-mail tényleges írása, csevegőprogram használata (tanórai gyakorlat); a „családi és iskolai környezet elektronikus szolgáltatásai” (e-napló, e-ügyintézés) csak egy-egy mondat. |
| 3. Robotika (11) | 07, 08, 09, (02) | **valódi robot** építése és programozása (tanórai); „egyszerű játékok készítése” események kezelésével – csak a 04 szavazógépe; az „együttműködési készség” (csoportmunka) nem animálható. |
| 4. Szövegszerkesztés (12) | 10, 11 | megnyitás, mentés, kijelölés, másolás, áthelyezés mint műveletek (a vágólap fogalma sincs külön – tartalék); a dokumentumtípusok elkészítése (menü, napirend, címke, termékismertető) – tanórai gyakorlat. |
| 5. Bemutatókészítés (8) | 12, (11: forrás) | a bemutató paramétereinek beállítása (mintafájl, áttűnés-típusok); kiselőadás tartása – tanórai. |
| 6. Multimédiás elemek készítése (8) | 13, 14 | kép, hang, videó **tényleges rögzítése** telefonnal, fényképezővel; a feliratozás és a beillesztés más dokumentumba csak a 11-ben; videó vágása nincs. |
| 7. Az információs társadalom, e-Világ (6) | 15, 16, (05, 06) | **„ismeri az információs technológia fejlődésének gazdasági, környezeti, kulturális hatásait”** – csak a 05 időszalagja; e-ügyintézés egy mondat; hozzászólás nyilvános fórumba (tevékenység). |
| 8. A digitális eszközök használata (4) | 17, (05: felhő, megosztás) | a mobileszközök operációs rendszerei; a hibajelzések értelmezése (csak a mentés nélküli áramszünet); a helyi hálózat csak említés. |

**A forrásszöveg kinyerési hibái** (a `kerettanterv/digitalis-kultura/5-6.md`-ben, javítás nélkül): a 8.
témakör javasolt tevékenységei között „kacsolódóan” áll („Projektfeladathoz kacsolódóan használandó
perifériák…”) – a forrás elírása, az idézetek így hagyják. A 3. témakörben „A témakör tanulása hozzájárul…”
és „A témakör tanulása eredményeként…” alatt ugyanaz a mondat is szerepel („ismeri és használja a
blokkprogramozás alapvető építőelemeit”) – a forrás ismétlése. Az „önállóan kezeli az operációs rendszer
mappáit, fájljait és a felhőszolgáltatásokat” a 2. és a 8. témakörben is tanulási eredmény. A 7. témakör
tevékenységei között ott az „Elektronikus levél írása…” (a 2. témakörrel átfedve). A témakörök áttekintő
táblázata kétszer szerepel (a konverzió és a forrás táblázata) – a tartalmat nem érinti. Az óraszámok
összege 68, egyezik a forrással. A sávbevezető „végig gondolására” írásmódja (helyesen: végiggondolására)
a forrásé – az idézet így hagyja.

**Tartalék-jelöltek**, ha a sorozat folytatódik (fontossági sorrendben):

1. `vagolap` – kijelölés, másolás, kivágás, beillesztés: a vágólap mint egy „zseb” (4.; DigDoc). Rövid,
   de a kerettanterv fogalomlistájának jelentős része.
2. `esemenyek-jatek` – egyszerű játék eseményekkel (két szereplő, ütközés, pontszám) (1., 3.; DigBlock,
   DigRobot „asztal” sprite-ként).
3. `felho-jogosultsag` – a felhő mappafája és a jogosultságok önálló leckében (2., 8.; MatGraf, DigUI).
4. `tomorites` – miért kisebb a JPEG és az MP3? (6., 8.; DigPixel, DigBit) – 7–8-as határeset.
5. `informacios-tarsadalom` – a technológia gazdasági, környezeti hatásai (e-hulladék, energiafogyasztás)
   (7.; FoldChart, MatChart) – óvatos számokkal.

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): az NKP *Digitális kultúra 5.* és *6.* digitális
tankönyve; a Bebras nemzetközi verseny magyar feladatai; CS Unplugged (algoritmus- és hálózatjátékok);
PhET *Color Vision*; Code.org és a hazai „Kódolás hete” anyagai; a Logo-hagyomány (Imagine Logo); az
NMHH és a Kék Vonal gyerekeknek szóló online biztonsági anyagai. Nálunk a többlet: a futás láthatóvá
tétele, a számolt nagy számok és a rétegek szétnyitása – egy közös blokknyelvvel és robottal.

---

## 7. Javasolt szerződés-kiegészítés (kész szöveg a `leckek/SZERZODES.md`-hez)

A következő fejezet változtatás nélkül beillesztve a `SZERZODES.md` végére, a 18. (Magyar nyelv és
irodalom-kiegészítés) után (2026-11-24).

```markdown
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
```
