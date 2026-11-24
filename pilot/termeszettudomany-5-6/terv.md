# Pilot: Természettudomány 5–6. – a leckesor terve

Forrás: [`kerettanterv/termeszettudomany/5-6.md`](../../kerettanterv/termeszettudomany/5-6.md) és
[`_bevezeto-5-6.md`](../../kerettanterv/termeszettudomany/_bevezeto-5-6.md) (NAT 2020, általános
iskola, 16 témakör, 136 óra). Az idézetek szó szerint onnan valók. A zárójeles szám (pl. „(3.)”)
azt jelzi, ha az idézet nem a lecke fő témaköréből jön. A lecke-formátum:
[`leckek/SZERZODES.md`](../../leckek/SZERZODES.md). A tantárgyi kiegészítő szabályok a 7. fejezetben
vannak, kész szövegként a szerződéshez.

Jelölések az „Adatok” pontokban: *(becslés)* – a szakirodalom tartományt ad, a leckében is ki kell
mondani; *(ellenőrizendő)* – gyártás előtt forrásban ellenőrizni kell; *(modell)* – a lecke
didaktikus modellje, nem mért adat; *(kitalált példa)* – szemléltető szám, a `.md`-ben is így
jelölve. Ahol egy számot a terv kiszámolt, ott a számolás is szerepel. A koordinátori brief nem
megbízható forrás (`pilot/EJSZAKAI-GYARTAS.md`, 7. tanulság): a leckeügynök minden számot ellenőriz,
és az eltérést a jelentésében jelzi.

---

## 1. Bevezető

A sorozat **17 leckéje** a 10–12 éveseknek szól. Ez az a kor, amikor a kerettanterv szerint a
gyerekek „többnyire érdeklődéssel fordulnak az élő és élettelen környezet, a természet felé”. A
`_bevezeto` két mondata adja a sorozat mércéjét: „10–12 éves korosztályban kiemelt fontosságú a
természetből érkező érzelmi hatások befogadása, amelyek akár egy életre is meghatározhatják a
gyerekek természettudományokhoz történő hozzáállását, attitűdjét”, illetve: „Hangsúlyozza a
kísérleti problémamegoldás lépéseit, különös tekintettel a várható eredmény becslésére
(hipotézisalkotásra).” Ezért minden lecke ugyanazt a ritmust követi: **Tippelj! → kísérlet →
magyarázat**. A diák előbb jósol, aztán a virtuális kísérlet dönt, és csak utána jön a „miért”.

A formátum ugyanaz, mint a többi sorozaté: 1920×1080-as színpad, 7–8 lépés, világos papírháttér.
A panelen lépésenként **legfeljebb 45 szó** áll (`"maxWords": 45`, mint a történelem és a matematika
5–6-nál).

### Hol ad egy animáció *valódi* belátást ebben a korban?

1. **Láthatatlan folyamatok láthatóvá tétele.** A párolgó tócsa, a hideg pohárra lecsapódó pára, a
   mágnes mezeje, a lufi töltése, a növény szárában felfelé áramló víz vagy a füstréteg, amely
   felülről tölti meg a szobát. Ezek a hétköznapokban vannak jelen, de nem látszanak. Az animáció
   nagyítója („nagyítás · szemléltetés”) és az áramló pöttyök a *mechanizmust* mutatják, nem csak az
   eredményt.
2. **Mérés és becslés.** A tipp és a mérés eltérése, a leolvasási hiba, az ismételt mérés és az átlag
   (a saját reakcióidő mérése). A középhőmérséklet nem „képlet”: a lecke valódi görbéből számolja.
3. **Méretarány és térkép.** A falu, amely a képernyőn „összemegy”. A domb, amelyet vízszintes
   szeletekre vágunk, és szintvonal lesz belőle. A gömb, amely nem teríthető ki síkra (ezért látszik
   Grönland akkorának, mint Afrika). Ezt egy statikus ábra nem tudja megmutatni, egy mozgó igen.
4. **„Mi lenne, ha…?” kísérletek, amelyek a valóságban nem végezhetők el.** Mi lenne, ha a Föld
   tengelye nem dőlne meg? Mi lenne a réttel, ha 40 évig senki nem kaszálná? Mi történik a tóval, ha
   túl sok tápanyag kerül bele? Mit visz el a kétszer gyorsabb folyó? Csúszkával *kipróbálható*, a
   modell becsületesen „modell” bélyeget kap.
5. **Életközösségek kapcsolatai.** Táplálékláncból háló, az erdő szintjei és a lejutó fény, a
   hóvirág „sietsége”. Kattintással kivehető egy faj, és látszik, kire hat.
6. **„Miért” kérdések, a gyerekek saját kérdései.** Miért mutat északra az iránytű? Miért kell
   guggolni a füstben? Miért reped szét a fagyasztóban felejtett üveg? Miért zavaros az árvíz? A
   leckecímek ilyen kérdések.
7. **Nagy számok kézzelfogható hasonlattal.** Egymilliárd másodperc kb. 31,7 év. A tanterem
   levegője kb. 230 kg. Budapest kb. 1130 km/h sebességgel forog körbe. Ezek a „wow” pillanatok, de
   mindegyik mögött ott van a számolás.

### Mit hagyunk ki?

- **Terepmunkát, kézműves és labortevékenységet**, ami csak a valóságban megy: kirándulás védett
  területre, iránytű készítése, madárodú, talaj- és kőzetvizsgálat kézzel, növény- és állathatározás,
  mikroszkópozás, papucsállatka-tenyészet, „zsebkomposzt”, minivulkán, mérőállomás építése. A lecke
  ezekhez *előkészít*: megmutatja, mit fog a diák látni és miért. A `> megjegyzés:` ajánlja a
  valódi tevékenységet. Kivétel a **virtuális terepmunka**: a 06-os leckében a diák egy kitalált
  iskolakörnyék térképvázlatát, útvonaltervét készíti el (7. témakör). A 07-esben a GPS
  helymeghatározását próbálja ki, a 03-asban pedig a saját reakcióidejét méri.
- **Fajlistákat, galériákat**, mint „a mező gyógynövényei” vagy „erdeink madarai”. A leckékben csak
  annyi faj van, amennyi egy kapcsolat megértéséhez kell. Ezeket a kerettanterv szerint mind
  hazai fajok közül választjuk.
- **Napirend-, étrend- és bőrápolási tanácsadást**, egyéni egészségügyi tanácsot, testsúly-
  minősítést (13: csak általános ajánlás, forrással).
- **A kamaszkori nemi érést** – csak a növekedési ugrás és a „mindenkinél máskor” üzenet jelenik meg,
  semleges testrajzzal (13, 7. fejezet).

### Kiválasztási elv

1. **Arányosság.** 136 óra / 17 lecke ≈ 8 óra leckénként. Minden témakör legalább egy lecke fő
   témája. Ahol két témakör ugyanazt a készséget építi, ott összevonunk: az 5. és a 7. témakör
   (térkép és a valóság, gyakorlati térképészet, 14 óra) egy leckét kap (06), a gyakorlati rész
   egy darabja a 07-be kerül (GPS). Az 1. témakör (12 óra) két leckét kap (víz, levegő és tűz),
   a talajrésze a 11-be kerül. A 15. témakör (10 óra) is kettőt (belső erők és kőzetek; a folyó
   munkája), a talajpusztulás itt is a 11-ben van.
2. **Miért 17 és nem 16?** 16 témakör van, de a 15. témakör két, egymástól független mechanizmust
   tanít (hegyképződés és a víz felszínformáló munkája), ezek nem férnek egy 8 lépéses leckébe. A
   tűzvédelem (1.) biztonsági okból önálló lecke. Az 5. és a 7. témakör összevonása ebből egyet
   visszahoz. A 16 leckés változat a 02-es kihagyása lenne, de ezt nem javasoljuk (2. fejezet).
3. **Nincs fölösleges átfedés a meglévő sorozatokkal.** Ahol egy téma a `leckek/` alatt már
   megvan, ott a 10–12 évesek szintjén, *más szemszögből* jön, és a `> megjegyzés:` megnevezi a
   „folytatást”. A teljes összevetés:

   | TT 5–6 lecke | Meglévő lecke | Ott | Itt (más szemszög) |
   |---|---|---|---|
   | 01-tocsa | fizika-7-8/06-halmazallapot, kemia-7-8/01, 04, fizika-7-8/01-suruseg | melegítési görbe, golyómodell, oldhatóság, sűrűség | a víz körforgása a tájban, a fagyó víz ereje (fagyaprózódás), a Föld vizei; a részecskék csak a nagyítóban |
   | 02-tuz | kemia-7-8/09-eges-korrozio, 11-levego | tűzháromszög, oltás, a gyertyás kísérlet cáfolata | a levegő tulajdonságai (tömeg, légnyomás, hőtágulás, felszáll), a füst viselkedése, menekülés |
   | 04-magnes | fizika-7-8/08-aramkor (1. lépés: dörzsölés) | áramkör, Ohm | mágneses mező, iránytű, a Föld mágnessége, villám és távolsága |
   | 05-ido | fizika-7-8/15-fold-forgasa, 16-holdfazisok, biologia-7-8/02-mely-ido, foldrajz-9-10/07 | égbolt, árnyékbot, csillagképek, „Föld egy nap alatt” | lámpa–földgömb osztálytermi modell, „mi lenne, ha nem dőlne a tengely?”, napirend, millió vs. milliárd másodperc |
   | 07-foldgomb | tortenelem-5-6/13-felfedezesek, foldrajz-9-10/01-idozonak | lapos Föld-tévhit, időzónák | kontinens-kirakó, nevezetes szélességi körök, fekvés, szomszédok, GPS |
   | 08-noveny | biologia-7-8/06 (3. lépés: van Helmont fűzfája) | a fa tömege a levegőből | csírázási kísérlet: egyszerre egy változó (kontroll), színezett víz a szárban, évgyűrűk |
   | 10-erdo, 11-ret-szanto | biologia-7-8/05-biomok, 06-taplalekhalozat, 09-monokultura | biomok, energiapiramis, kártevő-terjedés | hazai erdő szintjei és fénye, rét és kaszálás (szukcesszió), talajerózió, komposzt |
   | 12-to | kemia-7-8/12-viztisztitas | víztisztítás | a tó övei, egy csepp tóvíz, oxigén a vízben, algavirágzás |
   | 13-emberi-test | biologia-7-8/10–13, 17 | vérkör, felület, reflex, újraélesztés | futás közben: a szervek *együtt* dolgoznak; kamaszkori növekedés; hallásvédelem |
   | 14-energia | fizika-7-8/02-energia, 14-uveghaz, kemia-7-8/11, 14 | energiaátalakulás, üvegházhatás, szmog, kőolaj | honnan jön az áram, a szélkerék v³-trükkje, nappal–éjjel energiafalu, LED |
   | 15-hegyek, 16-folyo | foldrajz-9-10/02, 03, 07, 08 | lemeztektonika, rengéskatalógus, kanyarulat, Tisza-szabályozás | gyűrődés vagy vetődés (rugalmas–merev), hazai kőzetek próbái; homokasztal, a „hatodik hatvány” |
   | 17-idojaras | foldrajz-9-10/04, 05, 09, biologia-7-8/05 | felhőképződés, légkörzés, övezetesség | piktogramok, saját előrejelzés, három övezet egyszerűen, az előrejelzés megbízhatósága |

4. **A 3. témakör** (megfigyelés, kísérletezés, 8 óra) nem egy lecke, hanem a sorozat
   módszere. Saját leckét csak a mágnesesség és az elektromos állapot kap (04). A növények
   életfeltételei a 08-ba, a csapadékképződés a 01-be, az energiahordozók és az energiatakarékosság a
   14-be kerülnek.
5. **Építőkockák.** A sorozat szinte teljesen kész modulokra épül (4. fejezet). Ezek a kémia
   (Reszecske, KemLab, KemGHS), a biológia (BioNet, BioFlow, BioBody, BioZoom, BioPlot, DeepTime), a
   földrajz és a történelem (TortMap, TortGlobe, TortCards, TortTimeline, FoldSection, FoldFlow,
   FoldChart, FoldClimate, FoldChoro), a matematika (MatChart) és a fizika (ÉGBOLT/SKY) moduljai. Új
   modul csak kettő: **TtIkon** (hazai élőlények rajzai, 6 lecke) és **TtMuszer** (mérőműszerek,
   iránytű, 4 lecke). Új adat egy van: a Kárpát-medence domborzati rácsa (D1, a meglévő
   `tools/build_geodata.py` ETOPO-forrásából).

A leckék sorszáma a kerettanterv sorrendjét követi. A **gyártási sorrend** ettől eltér (4. fejezet).

---

## 2. A leckék

| # | slug | cím | témakör | építőkocka | nehézség (1–3) |
|---|---|---|---|---|---|
| 01 | `01-tocsa` | Hová tűnik a tócsa? – a víz halmazállapot-változásai | 1 (+3, +15) | FoldSection, KemLab, Reszecske, MatChart | 2 |
| 02 | `02-tuz` | Miért kell lehajolni a füstben? – a levegő tulajdonságai és a tűz | 1 (+3) | KemLab, Reszecske, FoldFlow, KemGHS, TortCards | 2 |
| 03 | `03-meres` | Mennyi lehet? – becslés, mérés, középhőmérséklet | 2 (+16) | **TtMuszer** (ref.), KemLab, BioPlot, FoldChart, FoldClimate, TortCards | 3 |
| 04 | `04-magnes` | Miért mutat északra az iránytű? – mágnes, elektromos állapot, villám | 3 (+5) | TtMuszer, FoldFlow, TortGlobe, TortCards | 2 |
| 05 | `05-ido` | Mitől van nap, év és évszak? – a Föld mozgásai és az idő skálái | 4 (+16) | SKY, TortGlobe, DeepTime + TortTimeline, MatChart | 3 |
| 06 | `06-terkep` | Hogyan lesz a faluból térkép? – alaprajz, méretarány, jelek, domborzat | 5, 7 | TtMuszer, FoldSection, TortMap, TortCards, D1 | 3 |
| 07 | `07-foldgomb` | Hol vagyunk a Földön? – földgömb, fokhálózat, fekvés, GPS | 6 (+7) | TortGlobe, TortMap, FoldChoro, TortCards | 2 |
| 08 | `08-noveny` | Mi kell a babnak? – a növény részei és életfeltételei | 8 (+3, +1) | TtIkon, BioFlow, BioPlot, TortCards | 2 |
| 09 | `09-allat` | Hogyan halad a giliszta, ha nincs lába? – gerinctelenek és gerincesek | 9 (+1) | TtIkon, TortCards, BioPlot | 2 |
| 10 | `10-erdo` | Miért siet a hóvirág? – az erdő szintjei és táplálékhálózata | 10 | **TtIkon** (ref.), BioNet, BioPlot, FoldSection | 3 |
| 11 | `11-ret-szanto` | Mi lenne a réttel kaszálás nélkül? – rét, szántóföld és a talaj | 11 (+1, +15, +8) | TtIkon, BioNet, BioPlot, MatChart, FoldSection | 2 |
| 12 | `12-to` | Mi él egy csepp tóvízben? – vízi és vízparti életközösségek | 12 (+9) | TtIkon, BioZoom, BioNet, FoldSection, BioPlot | 2 |
| 13 | `13-emberi-test` | Mi történik a testedben, ha futsz? – szervek együttműködése, egészség | 13 | BioBody, BioFlow, BioPlot, MatChart | 3 |
| 14 | `14-energia` | Honnan jön az áram a konnektorba? – energiaforrások | 14 (+3) | FoldChart, MatChart, TortCards, TtIkon | 2 |
| 15 | `15-hegyek` | Hogyan kerül kagyló a hegytetőre? – kőzetek, gyűrődés, vetődés, vulkán | 15 | FoldSection, TortCards, KemGHS, TortMap | 2 |
| 16 | `16-folyo` | Miért zavaros az árvíz? – a folyó munkája és vízjárása | 15 (+6) | FoldFlow, FoldSection, FoldChart, TortMap, D1 | 3 |
| 17 | `17-idojaras` | Esernyő kell holnap? – időjárás, éghajlat, éghajlati övezetek | 16 (+2) | TtMuszer, FoldClimate, TortGlobe, TortMap | 2 |

Nehézség = gyártási nehézség: 1 = egy fő vizuál, kevés adat; 2 = kész modulokra épülő közepes
szimuláció; 3 = új modul, összetett modell vagy kényes tartalom (egészség, saját geometria).

**Témakörönként** (lecke → becsült óra): 1 (12) → 01, 02, 11 · 2 (7) → 03 (+17) · 3 (8) → 04 (+01,
08, 14) · 4 (6) → 05 · 5 (7) → 06 · 6 (7) → 07 (+16) · 7 (7) → 06, 07 · 8 (10) → 08 (+11) · 9 (10) →
09 (+12) · 10 (11) → 10 · 11 (9) → 11 · 12 (10) → 12 · 13 (10) → 13 · 14 (6) → 14 · 15 (10) → 15, 16
(+01, 11) · 16 (6) → 17 (+05, 03). Egy lecke kb. 4–14 órát fed le; a legtöbbet a 11-es (rét +
talaj), a legkevesebbet a 02-es (tűz).

---

## 3. Briefek

Közös minden briefben (a 7. fejezet szabályai szerint):

- **Tippelj!** – minden leckében legalább egy jóslat a kísérlet *előtt* (2–4 válasz `L.button`-nal,
  a megoldás a választásig rejtve; utána a vásznon „a te tipped” jel). A brief megnevezi, melyik
  lépésben.
- **Kipróbálom** – legalább egy valódi interakció, amely a modellt mozgatja (csúszka, húzás,
  kattintás). A brief megnevezi.
- **Kísérlet-bélyeg** – ha a lecke valódi kísérletet mutat, jelölje, kipróbálhatja-e a diák:
  „otthon is kipróbálhatod”, „felnőttel együtt”, „tanári bemutató” vagy „NE PRÓBÁLD KI”.
- **Tévhit-lépés** – a briefben felsorolt tévhitek közül legalább egyet a vászon *cáfol* (kísérlettel,
  ellenpéldával), nem csak kimond.

### 01 · `01-tocsa` – Hová tűnik a tócsa? – a víz halmazállapot-változásai

- **Tanulási cél:** A víz bármilyen hőmérsékleten párolog, nem csak forraláskor. A párolgás a
  felszínen zajlik, a forrás az egész folyadékban, buborékokkal. A hideg tárgyon a levegő
  vízgőze lecsapódik. A felhő apró vízcseppekből és jégkristályokból áll, a csapadék ezekből
  hízik meg. Fagyáskor a víz térfogata kb. 9 %-kal nő, ezért szétfeszíti a palackot és a
  sziklarepedést. Az olvadás egy anyag halmazállapot-változása (jég → víz), az oldódás két anyag
  keveredése (cukor + víz). A Föld vizének csak kis része iható édesvíz.
- **Kerettanterv:** „megfigyeli a különböző halmazállapot-változásokhoz (olvadás, fagyás, párolgás,
  forrás, lecsapódás) kapcsolódó folyamatokat, példákat gyűjt hozzájuk a természetben, a
  háztartásban és az iparban” · „bizonyítja és hétköznapi példákkal alátámasztja a víz fagyásakor
  történő térfogat-növekedést” · „felismeri az olvadás és az oldódás közötti különbséget kísérleti
  tapasztalatok alapján” · „korábbi tapasztalatai és megfigyelései révén felismeri a víz különböző
  tulajdonságait, különböző szempontok alapján rendszerezi a vizek fajtáit” · „kísérletek során
  megfigyeli a különböző halmazállapotú anyagok vízben való oldódásának folyamatát” · (3.) „A
  csapadékképződés folyamata” · (3.) „kísérleti úton megfigyeli az időjárás alapvető folyamatait,
  magyarázza ezek okait és következményeit”.
- **Tévhitek:** a víz csak 100 °C-on párolog; a tócsa „beszivárog a földbe”, és kész (részben igen,
  de a nagy része a levegőbe megy). A hideg pohár „izzad”, vagy a víz átszivárog az üvegen. A
  forrásban lévő víz buborékjai levegőből vannak (vízgőzből vannak). A felhő vízgőz (a vízgőz
  láthatatlan; a felhő cseppek). A cukor „elolvad” a teában. A víz fagyáskor összehúzódik, mint a
  legtöbb anyag. Sok iható vizünk van, „hiszen a Föld kék”.
- **Kulcsvizuál:** egy iskolaudvar oldalnézetben (FoldSection: talaj, a tócsa, egy domb, mögötte egy
  tó, fölötte égbolt). Rajta a nap járása és a hőmérő. A tócsa fölött **KemLab.lens** nagyító,
  benne Reszecske-vízmolekulák: a felszínről egyenként szöknek el a gyorsak. A hideg poharon
  harmatcseppek nőnek. A 5. lépésben egy lezárt üvegpalack (rajz) a fagyasztóban: a jég feltolja,
  majd szétfeszíti; mellette egy sziklarepedés ék alakban nyílik ki (télről télre). A 7. lépésben
  „100 liter” vizes kanna, amely osztódik: 97 l tengervíz, 2,5 l édesvíz, ebből 1,7 l jég.
- **Kipróbálom:** a táj hőmérséklet-csúszkája (−10 … +35 °C) és egy „napsütés / felhő” kapcsoló: a
  tócsa párolgási üteme, a pára, a jég és a hó a beállításból számolódik (zárt képlet, *modell*).
  Fagyás-csúszka a palacknál: a jégréteg vastagsága → a térfogat kijelzett %-a (a rajz és a szám
  ugyanabból a konstansból, szerződés 9.). „Olvad vagy oldódik?” párosítás (TortCards: jégkocka a
  teában, cukor a teában, só a levesben, vaj a serpenyőben, hó a tenyérben, tabletta a vízben).
- **Tippelj!** 1. lépés: „Hová lett a tócsa? a földbe / a levegőbe / sehova, eltűnt”. 5. lépés: „A
  tele, lezárt palack a fagyasztóban: összemegy / ugyanakkora marad / szétreped”. 7. lépés: csúszkán
  tippel, a 100 literből hány liter a folyékony édesvíz.
- **Lépések:** Hová tűnik a tócsa? · Párolgás és forrás · Izzad a hideg pohár? – lecsapódás · Felhő,
  eső, hó: a csapadék születése · A fagyó víz szétfeszít · Olvad vagy oldódik? · A Föld vizei 100
  literben · Összefoglalás: a víz körforgása.
- **Adatok:** a jég sűrűsége 0,917 g/cm³, a vízé 0 °C-on 0,9998 g/cm³ → 1 l víz kb. 1,09 l jég
  (0,9998 / 0,917 = 1,090, tehát **kb. 9 %**). A víz forráspontja 1013 hPa-n 100 °C. Kékestetőn
  (1014 m, kb. 897 hPa a normállégkörben) kb. 97 °C, a Mount Everesten (8849 m, kb. 314 hPa) kb.
  70 °C *(becslés; a forrásponti görbéből, a fizika-7-8/06 adataival egyeztetendő)*. Egy vízmolekula
  átlagosan kb. 9 napot tölt a levegőben *(becslés: 8–10 nap, Trenberth és mtsai)*. A Föld vize
  (USGS, Shiklomanov 1993 alapján): óceánok 96,5 %, édesvíz 2,5 % (ennek 68,7 %-a jég, 30,1 %-a
  felszín alatti, 1,2 %-a felszíni és egyéb) → 100 literből ≈ 2,5 l édesvíz, ≈ 1,7 l jég, ≈ 0,75 l
  felszín alatti, ≈ 0,03 l (3 cl) felszíni és egyéb *(ellenőrizendő)*. A cukor (szacharóz) kb.
  186 °C-on olvad, közben bomlik (karamell) *(ellenőrizendő, forrásonként 160–186 °C)*; a jég 0 °C-on.
- **Átfedés:** a melegítési görbe (fizika-7-8/06) és a golyómodell részletei (kemia-7-8/01) *nem*
  jönnek ide. A részecskék csak a nagyítóban jelennek meg, egy mondattal. A jég úszását
  (fizika-7-8/01) a 5. lépés egy megjegyzésben említi („ezért fagy be a tó felülről – erről a fizika
  7. osztályban”).
- **Építőkocka:** FoldSection (`foldrajz-9-10/03-foldrenges-vulkan` – a táj metszete, `víz`, `jég`,
  `levegő` minta), KemLab (`kemia-7-8/01-reszecskemodell` – `lens`, `beaker`, `thermo`), Reszecske
  (ugyanonnan – `attract` folyadék, párolgás `remove` eseménnyel), MatChart (`matematika-5-6/17` –
  a 100 liter szalagja), TortCards (`tortenelem-5-6/07-kozepkori-varos`).
- **Kísérlet-bélyeg:** a hideg pohár, a tócsa megfigyelése „otthon is kipróbálhatod”; a fagyasztott
  üvegpalack „NE PRÓBÁLD KI” (szilánk – helyette műanyag palack, félig töltve, „felnőttel együtt”).
- **Meglévő anyag:** PhET *States of Matter: Basics* (magyarul is), NKP Természettudomány 5.
  *(nincs ellenőrizve)*. Nálunk a körforgás a tájban és a fagyás ereje a többlet.

### 02 · `02-tuz` – Miért kell lehajolni a füstben? – a levegő tulajdonságai és a tűz

- **Tanulási cél:** A levegő anyag. Helyet foglal el (a víz alá nyomott „üres” pohárba nem megy be a
  víz), tömege van (egy tanterem levegője több mint 200 kg), és nyomást fejt ki (minden
  négyzetcentiméterünkre kb. 1 kg-nyi levegő nehezedik). Melegítve kitágul, és a meleg levegő
  felszáll. Ezért gyűlik a forró füst a mennyezet alá, és ezért tölti meg felülről a szobát. Az
  égéshez oxigén kell (a levegő kb. ötöde). Vannak éghető és éghetetlen anyagok. Tűz esetén:
  riasztás (112), lehajolva el a füst alól, ajtót becsukni, liftet nem használni, nem elbújni.
- **Kerettanterv:** „korábbi tapasztalatai és megfigyelései révén felismeri a levegő egyes
  tulajdonságait” · „elsajátítja a tűzveszélyes anyagokkal való bánásmódot, tűz esetén ismeri a
  szükséges teendőket” · „A levegő tulajdonságai, összetétele, szerepe az élővilág és az ember
  életében” · „Tűzveszélyes anyagok” · tevékenység: „A levegő jelenlétének kimutatása egyszerű
  kísérletekkel” · fogalmak: „éghető, éghetetlen”, „légnyomás”, „hőmérséklet”.
- **Tévhitek:** az „üres” pohárban nincs semmi. A levegőnek nincs súlya. A füst a padló közelében
  is ugyanolyan sűrű. Tűzben az ágy alá vagy a szekrénybe kell bújni. Égő olajat vízzel kell
  oltani. A tűzben a láng a legveszélyesebb (a legtöbb áldozatot a füst okozza). A gyertya a pohár
  alatt azért alszik el, mert „elfogyott az oxigén” – ezt itt csak egy mondat és egy hivatkozás
  cáfolja (kemia-7-8/11).
- **Kulcsvizuál:** a lecke egy kis lakásmetszetben játszódik (szoba ajtóval, ablakkal, mennyezettel).
  Az eleje „kísérletpad”: víz alá nyomott pohár légbuborékkal, mérlegen lezárt doboz, palack nyakán
  lufi a meleg vízben. A nagyító (Reszecske) mutatja: melegen gyorsabbak és távolabb kerülnek egymástól
  a részecskék. Utána a szobában egy (nem lángoló, jelzésszerű) füstforrás, a füst FoldFlow-pöttyökkel
  felszáll, a mennyezet alatt szétterül, majd a réteg lefelé vastagszik. Egy semleges, stilizált alak
  áll vagy guggol. A „belélegzett levegő” sávja színkóddal mutatja a különbséget.
- **Kipróbálom:** a terem méretének csúszkái (hossz, szélesség, magasság) → a levegő tömege élőben
  (kg és „ennyi zsák krumpli”). Hőmérséklet-csúszka a palacknál (20–60 °C) → a lufi térfogata
  T(K)-val arányos (*modell*). Füstszimuláció időcsúszkával (0–3 perc, *modell*): „Állva / Guggolva”
  kapcsoló, ajtó „nyitva / csukva” kapcsoló. Éghető–éghetetlen kártyák (TortCards: papír, fa,
  gyertya, benzin, homok, kő, üveg, víz, vas szög – a vasforgács ég! a csillagszóró megjegyzésként).
- **Tippelj!** 2. lépés: „Mennyi a tanterem levegőjének tömege? 2 kg / 20 kg / 200 kg”. 7. lépés:
  „Hol tisztább a levegő a füstös szobában? fent / középen / lent”.
- **Lépések:** Üres-e az üres pohár? · Mennyit nyom a terem levegője? · Melegen kitágul · A meleg
  levegő felszáll · Mi kell a tűzhöz? – éghető és éghetetlen · Veszély a konyhában · Ha tűz van:
  lehajolni, kimenni, hívni · Összefoglalás.
- **Adatok:** a levegő sűrűsége 20 °C-on, 1013 hPa-n 1,20 kg/m³ (1,204). Egy 9 m × 7 m × 3 m-es
  terem 189 m³ → kb. 227 kg (a kód az adatokból számolja). Légnyomás a tengerszinten 1013 hPa
  = 10,13 N/cm² → kb. 1,03 kg-nyi súly négyzetcentiméterenként. Állandó nyomáson a gáz térfogata a
  kelvinben mért hőmérséklettel arányos: 20 °C → 60 °C: 333 / 293 = 1,137 → kb. 14 %-kal nagyobb. A
  levegő összetétele (térfogat): nitrogén 78,08 %, oxigén 20,95 %, argon 0,93 %, szén-dioxid
  kb. 0,04 % *(frissítendő: kb. 424 ppm, 2024, NOAA)*. 1 l víz gőzzé válva kb. 1700 l *(becslés:
  1600–1700-szoros térfogat 100 °C-on)* – ezért robbanásszerű, ha égő olajra víz kerül. Segélyhívó
  szám: 112 (tűzoltóság: 105). A lakástűz percek alatt életveszélyessé válhat *(ellenőrizendő:
  katasztrófavédelmi tájékoztató; pontos percszámot csak forrással)*. A tűzhalálok nagy részét a
  füstmérgezés okozza *(becslés; forrással)*.
- **Átfedés:** a tűzháromszöget és az oltási módokat a kemia-7-8/09 mutatja részletesen. Itt egy
  lépés, és a hangsúly a *viselkedésen* van. A gyertyás kísérlet (kemia-7-8/11, 2. lépés) itt
  nem szerepel.
- **Építőkocka:** KemLab (`kemia-7-8/01` – pohár, lens, thermo), Reszecske (ugyanonnan – hőmérséklet,
  `walls` a „lufis” határhoz), FoldFlow (`foldrajz-9-10/05-legkorzes` – sík mód, analitikus mező:
  felszálló csóva + mennyezeti terülés; a rétegvastagság zárt képlet, a pöttyök csak díszítik),
  KemGHS (`kemia-7-8/10-sav-bazis` – GHS02 láng, „NE PRÓBÁLD KI” bélyeg), TortCards
  (`tortenelem-5-6/07`), BioBody (`biologia-7-8/11-verkor` – semleges alak, `build` váltakozva) – csak
  a sziluett.
- **Biztonság:** a lecke tűzzel kapcsolatos kísérletet nem mutat követendőként. A lufis palack
  „felnőttel együtt” (forró víz), az olajtűz „NE PRÓBÁLD KI” bélyeget kap, csak sematikus ábrával:
  a vízcsepp lesüllyed a forró olajba, és gőzzé robban. A helyes cselekvés a fedő, a gáz elzárása és
  a 112. Láng, égő ember, sérült nem jelenik meg. Spec: `"review": ["tűzvédelem"]` (lektor:
  tűzoltó vagy katasztrófavédelmi oktató, szerepként a `.md`-ben).

### 03 · `03-meres` – Mennyi lehet? – becslés, mérés, középhőmérséklet

- **Tanulási cél:** Mérni annyi, mint egy egységgel összehasonlítani. A becslés hasznos, de a mérés
  dönt. Minden eszköznek van mérési tartománya és legkisebb osztása. Jól csak merőlegesen
  ránézve lehet leolvasni, a mérőhengerben a folyadék görbült felszínének aljánál. Egyetlen mérés
  pontatlan lehet, ezért többször mérünk, és átlagolunk. A napi középhőmérséklet a nap több mérésének
  átlaga. A napi hőingás a legmagasabb és a legalacsonyabb érték különbsége. Az évi közepes hőingás a
  legmelegebb és a leghidegebb hónap középhőmérsékletének különbsége. Ezt az éghajlati diagramról is
  le lehet olvasni.
- **Kerettanterv:** „önállóan végez becsléseket, méréseket és használ mérőeszközöket a hőmérséklet,
  a hosszúság, a tömeg, az űrtartalom és az idő meghatározására” · „észleli, méri az időjárási
  elemeket, a mért adatokat rögzíti, ábrázolja” · „Magyarországra vonatkozó adatok alapján
  kiszámítja a napi középhőmérsékletet, a napi és évi közepes hőingást” · „leolvassa és értékeli a
  Magyarországra vonatkozó éghajlati diagramok és éghajlati térképek adatait” · tevékenység:
  „Természeti rekordok, legek mérhető tulajdonságainak gyűjtése”.
- **Tévhitek:** a mért érték „pontos”, nincs hibája. Egy mérés elég. Az átlag mindig egy mért érték.
  A napi középhőmérséklet a legmagasabb és a legalacsonyabb érték átlaga (lehet így is becsülni,
  de nem ez a szabály). A legmelegebb időpont a dél (inkább kora délután). A hőingás és a
  középhőmérséklet ugyanaz. Az éghajlati diagram egy nap időjárása.
- **Kulcsvizuál:** egy „mérőasztal” a TtMuszer eszközeivel: mérőszalag, konyhai mérleg, mérőhenger
  (KemLab), hőmérő, stopper. Minden leolvasásnál egy nagyító ugrik a skálára. A 4. lépésben egy
  szemikon mozog a mérőhenger előtt: felülről, merőlegesen és alulról nézve más értéket „lát”
  (parallaxis), és látszik a meniszkusz is. A 6. lépésben egy kitalált tavaszi nap óránkénti
  hőmérséklet-görbéje: a négy mérési időpont kiemelve, a max és a min jelölve. A 7. lépésben
  Budapest valódi éghajlati diagramja (FoldClimate) és mellette Kékestetőé.
- **Kipróbálom:** **Mérd meg a reakcióidődet!** Egy stopper „indul”, a diák kattint, amikor a jel
  megjelenik (5 próbálkozás, `L.pointer.events[].ts`). A mért értékek BioPlot-pontokként jelennek meg,
  az átlaguk vonalként. (QA: `__qaStates`-ben rögzített próbasor, a véletlen késleltetés seedelt.)
  Leolvasós csúszka: a szem magassága a mérőhenger előtt. A 6. lépésben húzható mérési időpontok:
  ha más órákban mérnénk, mennyit változna a középhőmérséklet? A 7. lépésben hónapkurzor a
  diagramon, és élő számítás: évi közép és évi közepes hőingás.
- **Tippelj!** 1. lépés: becslés csúszkán – milyen hosszú a tanterem, mennyi a hátizsák tömege, hány
  liter a kancsó. A mérés után a vásznon „a te tipped” és a mért érték közti eltérés %-ban látszik.
  5. lépés: „Mennyi a reakcióidőd? 0,02 s / 0,2 s / 2 s”.
- **Lépések:** Tippelj, aztán mérj! · Mérni = összehasonlítani · Melyik eszközzel? · Olvasd le jól!
  · Mérd meg a reakcióidődet! · Egy nap hőmérséklete · Egy év Budapesten · Összefoglalás: magyar legek.
- **Adatok:** reakcióidő egyszerű vizuális jelre kb. 0,2–0,3 s *(becslés; a 10–12 éveseknél
  inkább a felső határ)*. Lépéspár (két lépés) egy 11 évesnél kb. 1,2–1,4 m *(becslés)*. A
  napi középhőmérséklet a tankönyvi gyakorlat szerint négy mérés (1, 7, 13 és 19 órakor)
  átlaga *(ellenőrizendő: az NKP Természettudomány 5. szövege; a HungaroMet ma az óránkénti
  mérésekből számol – a panel ezt kimondja)*. A kitalált nap *(kitalált példa)*: 1 óra 14 °C,
  7 óra 13 °C, 13 óra 24 °C, 19 óra 21 °C → (14 + 13 + 24 + 21) : 4 = **18 °C**. Max 25 °C (15 óra),
  min 12 °C (5 óra) → napi hőingás **13 °C**. Budapest (WMO 1991–2020 klímanorma, NOAA NCEI, WMO
  12840; ugyanaz az adat, mint a `foldrajz-9-10/09-ovezetesseg` leckében): havi középhőmérséklet 1,3;
  3,1; 7,5; 13,3; 17,6; 21,5; 23,3; 22,9; 17,8; 12,3; 7,2; 2,1 °C → évi közép 149,9 : 12 =
  **12,5 °C**, évi közepes hőingás 23,3 − 1,3 = **22,0 °C**; évi csapadék 526,2 mm. Kékestető
  (ugyanonnan, `biologia-7-8/05-biomok`): évi közép 76,2 : 12 = **6,4 °C**, hőingás 16,4 − (−3,4)
  = **19,8 °C**. Magyar legek *(ellenőrizendő: HungaroMet rekordlista)*: legmelegebb 41,9 °C
  (Kiskunhalas, 2007. július 20.), leghidegebb −35,0 °C (Miskolc-Görömbölytapolca, 1940. február
  16.), a legtöbb csapadék egy nap alatt 260 mm (Dad, 1953. június 9.); legmagasabb pont Kékes
  1014 m, legmélyebb Gyálarét kb. 75,8 m. Földi legek: −89,2 °C (Vosztok, 1983. július 21.), 56,7 °C
  (Death Valley, 1913 – a WMO elismeri, de vitatott).
- **Átfedés:** az átlag számolását a matematika-5-6/17 (MatChart: „kockatornyok”) részletesen
  tanítja. Itt csak alkalmazzuk, egy megjegyzés hivatkozik rá.
- **Építőkocka:** **TtMuszer (referencia, ebben épül)**, KemLab (`kemia-7-8/01` – `cylinder`), BioPlot
  (`biologia-7-8/07-populacio` – reakcióidő-pontok, átlagvonal), FoldChart (`foldrajz-9-10/10-nepesseg`
  – napi görbe, forrássor), FoldClimate (`foldrajz-9-10/09-ovezetesseg`), TortCards (`tortenelem-5-6/07`
  – „melyik eszközzel?”). Spec: `"sources": true`.

### 04 · `04-magnes` – Miért mutat északra az iránytű? – mágnes, elektromos állapot, villám

- **Tanulási cél:** A mágnesnek két pólusa van. Az egynemű pólusok taszítják, a különneműek vonzzák
  egymást. A mágnes körül mező van, ezt a vasreszelék rajzolja ki. A kettévágott mágnesből két
  teljes, kétpólusú mágnes lesz. A mágnes nem minden fémet vonz, csak például a vasat, a nikkelt és a
  kobaltot. A Föld is egy óriási mágnes, ezért áll be az iránytű tűje észak–déli irányba. Dörzsöléssel
  a testek elektromos állapotba kerülnek: az egyneműek taszítják, a különneműek vonzzák egymást. A
  villám egy óriási szikra a felhő és a föld (vagy két felhő) között. A villámlás és a dörgés közötti
  másodpercekből a távolság becsülhető.
- **Kerettanterv:** (3.) „megfigyeli a mágneses kölcsönhatásokat, kísérlettel igazolja a vonzás és
  a taszítás jelenségét, példákat ismer a mágnesesség gyakorlati életben való felhasználására” ·
  „megfigyeli a testek elektromos állapotát és a köztük lévő kölcsönhatásokat, ismeri ennek
  gyakorlati életben való megjelenését” · „A mágneses tulajdonságok megfigyelése” · „Testek
  elektromos állapotának létrehozása” · „A villám keletkezése” · (5.) „mágneses kölcsönhatásként
  értelmezi az iránytű működését”.
- **Tévhitek:** a mágnes minden fémet vonz. A kettévágott mágnes egyik fele „északi”, a másik
  „déli”. A mágnes ereje a nagyságától függ (egy kis neodímium erősebb, mint egy nagy hűtőmágnes).
  Az iránytű a Sarkcsillag felé mutat. A villám ugyanoda nem csap be kétszer. Az autóban a
  gumikerék véd a villámtól (a fémkaszni vezeti el a földbe). A dörgés a felhők összeütközése.
- **Kulcsvizuál:** egy asztallap felülnézetben. Rajta két rúdmágnes, köztük **vasreszelék-minta**:
  FoldFlow sík módban, rögzített `t`-vel rajzolva statikus „szálak”, amelyek a mező irányába állnak.
  Körülöttük egy rács apró iránytűkből (TtMuszer), amelyek a mezőhöz fordulnak. A 5. lépésben a
  Föld (TortGlobe) belsejébe egy „mintha rúdmágnes” kerül, köré mezővonalak. Egy magyarországi
  iránytű kis eltéréssel északra mutat. A 6. lépésben egy lufi és egy haj sematikusan: pluszok és
  mínuszok vándorolnak. A 7. lépésben zivatarfelhő-metszet: a töltések szétválnak (fent +, lent −),
  villám, majd egy hanghullám-gyűrű lassan halad a megfigyelő felé.
- **Kipróbálom:** a mágnesek húzhatók és forgathatók. A vasreszelék-minta és az iránytű-rács élőben
  követi őket (a mező zárt képletű dipólösszeg, *modell*; az előszámítás a húzás befejezésekor).
  „Vágd ketté!” gomb. Anyagválasztó (vasszög, alufólia, rézdrót, papírkapocs, ezüstkanál, nikkel).
  **Villámszámláló:** a villanáskor elindul a számláló, a dörgésre a diák megállítja. A kód kiírja
  a távolságot, vagy csúszkán állítható a távolság, és hallható-látható a késés.
- **Tippelj!** 3. lépés: „Ha kettévágod a mágnest: egy északi és egy déli fél lesz / két mágnes lesz /
  elveszti a mágnességét”. 4. lépés: tippkártyák (vonzza / nem vonzza) a kísérlet előtt.
- **Lépések:** Vonz vagy taszít? · A láthatatlan mező · Kettévágom: két mágnes · Mit vonz a mágnes? ·
  A Föld egy óriási mágnes · Lufi a hajon: elektromos állapot · A villám: óriási szikra ·
  Összefoglalás: mire használjuk?
- **Adatok:** a Föld mágneses mezeje a felszínen kb. 25–65 µT; egy hűtőmágnes közvetlenül a
  felületén kb. 5–10 mT *(becslés)*. A mágneses elhajlás Budapesten kb. 5–6° kelet felé
  *(ellenőrizendő: NOAA WMM2025, 2026-ra)*. Az északi mágneses pólus vándorol, kb. 35–55 km/év
  *(ellenőrizendő)*. A hang sebessége 20 °C-os levegőben 343 m/s → 3 s ≈ 1 km (1029 m). A villám
  csatornája kb. 30 000 °C *(becslés: forrásonként 20 000–30 000 °C)*, kb. ötször melegebb a Nap
  felszínénél (kb. 5500 °C). A Földön másodpercenként kb. 44 villám csap le *(ellenőrizendő: NASA
  OTD/LIS, Christian és mtsai 2003)*. Ha a villámlás és a dörgés között 30 másodpercnél kevesebb
  telik el (kb. 10 km), menedéket kell keresni *(ellenőrizendő: hazai villámvédelmi/
  katasztrófavédelmi ajánlás)*.
- **Átfedés:** az elektronok vándorlását a fizika-7-8/08 1. lépése mutatja. Itt csak „pozitív és
  negatív töltés”, elektron szó nélkül vagy egy mondatban.
- **Építőkocka:** TtMuszer (`03-meres` – iránytű), FoldFlow (`foldrajz-9-10/05-legkorzes` – sík mód,
  analitikus mező, statikus `t`), TortGlobe (`tortenelem-5-6/13-felfedezesek`, v1.1:
  `foldrajz-9-10/01-idozonak`), TortCards (`tortenelem-5-6/07`).
- **Biztonság:** a konnektorral és a hálózati árammal (230 V) soha ne kísérletezz (kötelező mondat a
  6. lépésben). Kis, erős mágnesgolyót nem veszünk a szánkba (lenyelve életveszélyes), és nem
  tesszük telefon vagy bankkártya mellé. Villámláskor ne állj magányos fa alá, gyere ki a vízből.
  Az autó és az épület véd. A lufis kísérlet „otthon is kipróbálhatod”.
- **Meglévő anyag:** PhET *Balloons and Static Electricity*, *Magnet and Compass* (magyarul is)
  *(nincs ellenőrizve)*. Nálunk a Föld mint mágnes és a villámtávolság a többlet.

### 05 · `05-ido` – Mitől van nap, év és évszak? – a Föld mozgásai és az idő skálái

- **Tanulási cél:** A nap a Föld egy forgása a saját tengelye körül (kb. 24 óra). A napszakok
  azért váltakoznak, mert a Föld egyik fele mindig a Nap felé néz. A Föld nyugatról keletre forog,
  ezért kel a Nap keleten. Az év a Föld egy keringése a Nap körül (kb. 365 és negyed nap, ezért
  van szökőév). Az évszakokat a ferde tengely okozza: nyáron magasabban jár a Nap, és tovább van
  fent. Nem a távolság a lényeg, januárban vagyunk a legközelebb a Naphoz. Az időt sokféle
  skálán mérjük: a pislogástól a Föld 4,54 milliárd évéig. A saját napunk 24 órája is beosztható.
- **Kerettanterv:** „megérti a Föld mozgásai és a napi, évi időszámítás közötti összefüggéseket” ·
  „modellezi a Nap és a Föld helyzetét a különböző napszakokban és évszakokban” · „tervet készít
  saját időbeosztására vonatkozóan” · „tudja értelmezni az időt különböző dimenziójú skálákon” ·
  „Idő és időtartam mérése különböző dimenziójú skálákon” · tevékenység: „Időszalag készítése a
  földtörténetre, az emberi történelemre, egy ember életére” · (16.) „értelmezi az évszakok
  változását”.
- **Tévhitek:** nyáron azért van meleg, mert közelebb vagyunk a Naphoz. A Nap kering a Föld körül
  (a látszat). A Nap mindig pontosan keleten kel. Délben a Nap pont fölöttünk áll (Magyarországon
  soha). Az egész Földön egyszerre van nyár. Egymillió és egymilliárd másodperc között „nincs nagy
  különbség”.
- **Kulcsvizuál:** **az osztálytermi modell:** egy lámpa (Nap) és egy ferde tengelyű földgömb
  (TortGlobe, a terminátorral a SKY napállásából). A földgömb a lámpa körül kering. A gömbön
  Budapest piros pötty, mellette egy „nappal / éjjel” óralap. A 4. lépésben a gömb mellett egy
  zseblámpafolt: ugyanaz a fénynyaláb nyáron kis, télen nagy területre esik. Egy kis horizontkép
  mutatja a Nap delelési magasságát. A 6. lépésben egy 24 órás kördiagram (MatChart), a saját nap
  szeletei. A 7–8. lépésben egy logaritmikus időszalag (DeepTime + TortTimeline): pislogás,
  szívverés, nap, év, egy emberélet, honfoglalás, piramisok, dinoszauruszok, a Föld kora.
- **Kipróbálom:** **„Mi lenne, ha…?” tengelyferdeség-csúszka** (0°–90°, alapérték 23,44°): élőben
  változik Budapest nappalának hossza június 21-én és december 21-én, a déli napmagasság és a
  zseblámpafolt. 0°-nál nincs évszak, mindenhol 12 órás a nappal. Dátumcsúszka a keringéshez.
  Napirend: húzható szeletek (alvás, iskola, mozgás, tanulás, játék, képernyő…), az összeg mindig
  24 óra. Az alvásszelet mellé az ajánlás kerül (9–12 óra), minősítés nélkül. Időszalag: lineáris ↔
  log. kapcsoló.
- **Tippelj!** 5. lépés: „Mikor vagyunk a legközelebb a Naphoz? júliusban / januárban / mindig
  ugyanolyan messze”. 7. lépés: „Mennyi idő egymilliárd másodperc? 3 nap / 3 év / 31 év”.
- **Lépések:** Egy nap: egyszer megfordul a Föld · Merre kel a Nap? · Egy év: egy kör a Nap körül ·
  A ferde tengely – mi lenne, ha nem dőlne? · Tévhit: nyáron közelebb vagyunk? · A te napod 24
  órája · Millió vagy milliárd másodperc? · Összefoglalás: a pislogástól a Föld koráig.
- **Adatok:** tengelyferdeség 23,44° (2026-ban 23,436°, a `fizika-7-8/15` adatával egyezik).
  Budapest szélessége 47,5°. Déli napmagasság Budapesten: június 21. 90 − 47,5 + 23,44 ≈ **66°**,
  december 21. ≈ **19°**, napéjegyenlőség 42,5°. A nappal hossza Budapesten (a napkorong szélével és
  a fénytöréssel): június 21. kb. 15 óra 58 perc (**kb. 16 óra**), december 21. kb. 8 óra 26 perc
  (**kb. 8 és fél óra**). A geometriai érték (cos H = −tg φ · tg δ) 15,8 óra és 8,2 óra, a különbség
  kb. 12 perc. A kód a SKY-ból számol, a panel kerekít. Zseblámpafolt: 1 / sin(19°) ≈ 3,1 és
  1 / sin(66°) ≈ 1,1 → télen ugyanaz a fény **kb. háromszor** akkora területre jut. A forgás
  sebessége az Egyenlítőn kb. 1670 km/h, Budapesten 1670 · cos 47,5° ≈ **1130 km/h**. A Föld
  pályasebessége kb. 30 km/s. Napközel kb. január 3., 147,1 millió km; naptáv kb. július 4.,
  152,1 millió km. Év 365,2422 nap (Gergely-naptár: 4 évente szökőév, a 100-zal osztható évek közül
  csak a 400-zal oszthatók). 1 millió s = 11,6 nap; 1 milliárd s = 1e9 / 31 557 600 = **31,7 év**.
  Időszalag (`ago`, ill. `dim: idő`): pislogás 0,1–0,4 s *(becslés)*; szívverés kb. 1 s; honfoglalás
  895 (a `tortenelem-5-6/09` adatával egyezzen); a Kheopsz-piramis kb. Kr. e. 2560 *(becslés; a
  `tortenelem-5-6/02` adatával egyezzen)*; a jégkorszak vége 11 700 éve; *Homo sapiens* kb. 300 ezer
  éve; a dinoszauruszok kihalása 66 millió éve; a Föld kora 4,54 milliárd év (a `biologia-7-8/02`
  adataival egyezzen). Alvás 6–12 éveseknek 9–12 óra (AASM, 2016), mozgás naponta átlagosan legalább
  60 perc (WHO, 2020) – a 13-as leckével egyezzen.
- **Átfedés:** a fizika-7-8/15 csillagos égboltja, árnyékbotja és csillagképei nem jönnek ide. A
  tévhit-lépés rövidebb, mint ott. Új a lámpa–földgömb modell, a tengely-csúszka és a napirend. A
  Hold mozgása (javasolt tevékenység) a fizika-7-8/16-holdfazisok – megjegyzés hivatkozik rá.
- **Építőkocka:** SKY („ÉGBOLT-MODUL”, `fizika-7-8/15-fold-forgasa` – csak a számoló függvények:
  `sun(day, P)` a `P.eps` paraméterrel, a szárazföld-maszk nélkül; a blokk jelölője nem szabványos,
  bájtra azonosan másolandó, a jelentés jelezze), TortGlobe (`foldrajz-9-10/01-idozonak`, v1.1),
  DeepTime + előtte TortTimeline (`biologia-7-8/02-mely-ido`; a DeepTime a TortTimeline-ra épül),
  MatChart (`matematika-5-6/10-szazalek`, v1.1 – kördiagram, húzható szeletek a lecke kódjában).
- **Biztonság:** „Soha ne nézz a Napba – napszemüveggel, távcsővel, telefonnal sem” (kötelező
  mondat, ahol a Nap rajza vagy a napmagasság-mérés szerepel).

### 06 · `06-terkep` – Hogyan lesz a faluból térkép? – alaprajz, méretarány, jelek, domborzat

- **Tanulási cél:** A térkép a valóság felülnézeti, kicsinyített, jelekkel egyszerűsített képe. A
  méretarány megmutatja, hányszor kisebb a térkép a valóságnál (1 : 10 000 → 1 cm = 100 m). A
  vonalas aránymértékkel a távolság közvetlenül lemérhető. Minél nagyobb területet ábrázol egy
  térkép ugyanakkora lapon, annál kevesebb részlet fér rá. A jelkulcs a térkép nyelve. A térkép teteje
  általában észak, a fő- és mellékvilágtájakkal megadható, mi merre van. A domborzatot szintvonalak
  és színek mutatják: a sűrű szintvonal meredek lejtőt jelent. Az útvonaltervezéskor szempontokat
  mérlegelünk (rövidebb vagy laposabb). A domborzati, közigazgatási, autós és turistatérkép
  ugyanazt a tájat más célra mutatja.
- **Kerettanterv:** (5.) „érti a térkép és a valóság közötti viszonyt” · „felismeri a felszínformák
  ábrázolását a térképen” · „megérti a méretarány és az ábrázolás részletessége közötti
  összefüggéseket” · „fő- és mellékégtájak segítségével meghatározza különböző földrajzi objektumok
  egymáshoz viszonyított helyzetét” · „felismeri és használja a térképi jelrendszert és a
  térképfajtákat (domborzati térkép, közigazgatási térkép, autós térkép, turistatérkép)” · (7.) „a
  valóságban megismert területről egyszerű, jelrendszerrel ellátott útvonaltervet, térképet
  készít” · „meghatározott szempontok alapján útvonalat tervez a térképen” · (7.) „Térképvázlat
  készítése ismert területről”.
- **Tévhitek:** a nagyobb méretarányszám (1 : 1 000 000) részletesebb térképet jelent (fordítva).
  A térkép „fényképkép”, minden rajta van. A kék szín a térképen mindig vizet jelent (a domborzati
  térképen a zöld alföldet, nem rétet). A szintvonal az „út a hegyen”. Észak mindig „fent” van a
  valóságban is. A légvonalbeli táv és az út hossza ugyanaz.
- **Kulcsvizuál:** **virtuális terepmunka egy kitalált településen** („Tóvölgy”, *kitalált példa*):
  iskola, templom, patak hídon, erdő széle, domb kilátóval. 1. lépés: madártávlati, ferde rajz, amely
  felülnézetté „dől”, aztán a házak alaprajzzá egyszerűsödnek. 2–3. lépés: a kép összemegy, kiírt
  méretaránnyal; vonalas aránymérték és húzható mérőszalag (TtMuszer). 4. lépés: kizoomolás Tóvölgyből
  a megyén át Magyarországig (a végén TortMap, valódi adat). A részletek elmaradnak, a jelek
  egyszerűsödnek. 6. lépés: a domb 3D-s, ferde rajza, amelyet 10 m-enként vízszintes síkok szelnek.
  A metszésvonalak lehullanak a síkra, és szintvonalak lesznek. Mellette a valódi Alföld–Bükk szelvény
  (FoldSection, `szelveny-alfold-bukk`). 8. lépés: Magyarország domborzati térképe színfokozattal
  (D1), majd ugyanaz közigazgatási, autós és turista stílusban.
- **Kipróbálom:** méretarány-csúszka (1 : 1000 … 1 : 1 000 000) élő részletességgel. Mérőszalag:
  két pont között a térképi cm → valódi m/km, a kód számolja. „Merre van?” feladat: kattints arra,
  ami az iskolától északkeletre van. Szintvonal-csúszka (szintköz 5–25 m). **Útvonaltervező:** két
  útvonal a kilátóig. A diák választ, és a kód kiírja a hosszt és a szintemelkedést; egy
  oldalnézeti profil mutatja a meredekséget. Jelkulcs-párosítás (TortCards).
- **Tippelj!** 2. lépés: „Melyik térkép részletesebb: 1 : 10 000 vagy 1 : 100 000?”. 6. lépés: „Hol
  meredekebb a domb: ahol sűrűk vagy ahol ritkák a szintvonalak?”.
- **Lépések:** Felülről nézve: alaprajz · Kicsinyítés: a méretarány · Mérj a térképen! · Nagyobb
  terület, kevesebb részlet · Jelek és égtájak · A domb szeletei: szintvonalak · Útvonalterv:
  rövidebb vagy laposabb? · Összefoglalás: négy térkép, egy táj.
- **Adatok:** 1 : 10 000 → 1 cm = 100 m; 1 : 100 000 → 1 cm = 1 km; 1 : 1 000 000 → 1 cm = 10 km
  (`ratio`). A hazai turistatérképek jellemzően 1 : 40 000-esek, az autóatlaszok 1 : 250 000-esek
  *(ellenőrizendő; „jellemző”, nem szabály)*. A domborzati térkép magassági színei a tankönyvi
  beosztás szerint: alföld 200 m alatt (zöld), dombság 200–500 m (sárga, világosbarna), hegység 500 m
  fölött (barna) *(ellenőrizendő: NKP Természettudomány 5., a határok tankönyvenként eltérhetnek)*.
  Kékes 1014 m, Gyálarét kb. 75,8 m *(ellenőrizendő; a 03-as lecke adatával egyezzen)*. Tóvölgy
  méretei, magasságai *(kitalált példa)*.
- **Építőkocka:** TtMuszer (`03-meres` – mérőszalag, iránytű a szélrózsához), FoldSection
  (`foldrajz-9-10/03` + `shared/foldrajz/szelveny-alfold-bukk.js`), TortMap (`foldrajz-9-10/13-magyarorszag`,
  v1.1 + `shared/tort/map-karpat.js`, `map-orszaghatarok.js`; a megyehatárokhoz
  `shared/foldrajz/megyek.js`), TortCards (`tortenelem-5-6/07`), **D1** domborzati rács (4. fejezet).
  Lecke-saját: a kitalált település rajzolója, a 3D domb és a szintvonal-szeletelés (marching squares
  egy analitikus felületen: Gauss-dombok összege).
- **Ha a D1 nincs kész:** a 8. lépés a FoldSection szelvényével és a TortMap tájfoltjaival készül,
  „vázlatos” bélyeggel, és a jelentés jelzi.

### 07 · `07-foldgomb` – Hol vagyunk a Földön? – földgömb, fokhálózat, fekvés, GPS

- **Tanulási cél:** A Föld gömb alakú. A gömb felszíne torzítás nélkül nem teríthető ki síkra, ezért
  minden világtérkép valamit torzít. A Föld felszínének kb. 71 %-a óceán. A földrészeket és az
  óceánokat a gömbön és a térképen is fel kell ismerni. A fokhálózat szélességi és hosszúsági
  körökből áll. Ezekkel bármely pont helye megadható. A nevezetes szélességi körök (Egyenlítő,
  térítők, sarkkörök) a Föld ferde tengelyéből következnek (05). Magyarország tényleges fekvése a
  koordinátáival, viszonylagos fekvése a szomszédaival és a Kárpát-medencével adható meg. A telefon a
  műholdak jeleinek beérkezési idejéből számolja ki, hol vagyunk.
- **Kerettanterv:** (6.) „felismeri a földrészeket és az óceánokat a különböző méretarányú és
  ábrázolásmódú térképeken” · „felismeri a nevezetes szélességi köröket a térképen” · „megfogalmazza
  Európa és Magyarország tényleges és viszonylagos földrajzi fekvését” · „bejelöli a térképen
  Budapestet és a saját lakóhelyéhez közeli fontosabb nagyvárosokat és a szomszédos országokat” ·
  tevékenység: „Települések és egyéb térképi objektumok helymeghatározása a fokhálózat segítségével”
  · (7.) „tájékozódik a terepen térképvázlat, iránytű és GPS segítségével” · (7.) „használni tud
  néhány egyszerű térinformatikai alkalmazást”.
- **Tévhitek:** Grönland majdnem akkora, mint Afrika (a Mercator-térképen). A térkép „igaz kép”, a
  földgömb csak dísz. Európa a világ közepe (csak a mi térképeink közepe). A Ráktérítő és a sarkkör
  „csak vonalak a térképen” (csillagászati jelentésük van). A GPS „a telefon internetéből” tudja,
  hol vagyunk. Magyarország tengerparti ország volt, ezért „közel van a tengerhez”. *(Ez utóbbit
  csak akkor, ha a lektor jónak látja – inkább kihagyandó.)*
- **Kulcsvizuál:** 1. lépés: egy narancshéj (földgömb), amelyet lehámozunk és kiterítünk. Szakadások
  keletkeznek, majd egy Mercator-szerű kiterítés: Grönland felfúvódik. Egy „csúsztasd egymásra” gomb
  a valódi méretüket mutatja (gömbi felület, `TortProj.equalEarth`). 2. lépés: forgatható gömb
  (TortGlobe orbit), a kontinensek kirakóként a helyükre úsznak. 3–4. lépés: fokhálózat. A
  nevezetes szélességi köröket a 05-ös lecke ferde tengelyes Napja „rajzolja meg” (a térítő ott van,
  ahol a Nap delelhet a zenitben). 5–6. lépés: rázoom Európára, majd Magyarországra (TortMap). A
  szomszéd országok kiemelődnek (FoldChoro, `orszagok.js`, magyar nevek). 7. lépés: három műhold
  a Föld fölött, a jelük gömbhéjként terjed. Síkban három kör metszéspontja adja a telefon helyét.
- **Kipróbálom:** a gömb forgatása húzással. Kontinens- és óceánkirakó (TortCards, a gömb mellett a
  zónák). „Hol van?” kattintás a gömbön: a kód kiírja a szélességet és a hosszúságot, aztán fordítva:
  „keresd meg a 47,5° É, 19° K pontot!”. Szomszédkereső (kattints a 7 szomszédra). **GPS-játék:**
  a diák húzza a három műhold „távolságkörét”, és csak egy pont felel meg mindháromnak. Egy negyedik
  gomb mutatja, mi történik, ha egy műhold órája 0,001 s-ot késik (300 km-es hiba!).
- **Tippelj!** 1. lépés: „Melyik nagyobb: Grönland vagy Afrika? Grönland / kb. egyforma / Afrika
  sokkal”. 7. lépés: „Hány műhold kell a helymeghatározáshoz? 1 / 2 / 3–4”.
- **Lépések:** Gömbből sík? – a narancshéj · Földrészek és óceánok · Rács a gömbön · Nevezetes
  szélességi körök · Hol van Magyarország? – tényleges fekvés · Kik a szomszédaink? – viszonylagos
  fekvés · Honnan tudja a telefon, hol vagy? · Összefoglalás.
- **Adatok:** Grönland 2,166 millió km², Afrika 30,37 millió km² → kb. 14-szeres *(ellenőrizendő)*.
  Óceán a felszín kb. 71 %-a. A Csendes-óceán kb. 165 millió km², a szárazföld összesen kb. 149
  millió km² → „nagyobb, mint az összes szárazföld együtt” *(ellenőrizendő)*. Nevezetes szélességi
  körök: Ráktérítő és Baktérítő 23,44° (23° 26′), sarkkörök 66,56° (66° 34′); a 05-ös lecke
  tengelyferdeségéből számolva, ugyanazzal a konstanssal. Magyarország szélső pontjai kb. 45° 44′ –
  48° 35′ É és 16° 06′ – 22° 54′ K; területe kb. 93 000 km² *(ellenőrizendő: KSH, a pontos érték
  forrásonként 93 023–93 030 km²)*. Budapest 47,51° É, 19,03° K (`coord`; a `foldrajz-9-10/09` adatával egyezik). Szomszédok (7): Ausztria,
  Szlovákia, Ukrajna, Románia, Szerbia, Horvátország, Szlovénia. Földrészek száma: a magyar
  tankönyvek egy része hetet (Észak- és Dél-Amerika külön), más része hatot számol – a panel ezt
  kimondja *(ellenőrizendő: NKP Természettudomány 5–6.)*. Óceánok: Csendes-, Atlanti-, Indiai-,
  Északi-sarki (Jeges-tenger) és Déli-óceán *(a Déli-óceánt nem minden tankönyv különíti el –
  megjegyzésben)*. GPS: legalább 24 működő műhold kb. 20 200 km magasan, kb. 12 órás keringéssel. A
  jel útja kb. 20 200 km / 300 000 km/s ≈ 0,07 s. 1 ms órahiba → 300 km. Egy mobiltelefon szabad ég
  alatt kb. 5 m-re pontos *(ellenőrizendő: gps.gov)*. A valóságban térbeli gömbök metszenek, és a
  negyedik műhold az órát pontosítja – a panel kimondja, hogy a síkbeli körök egyszerűsítés.
- **Átfedés:** a tortenelem-5-6/13 (lapos Föld-tévhit, felfedezések) és a foldrajz-9-10/01 (helyi idő,
  időzónák) nem ismétlődik. A „nagy földrajzi felfedezések” kiselőadás-téma, megjegyzés hivatkozik
  a történelemleckére.
- **Építőkocka:** TortGlobe (`foldrajz-9-10/01-idozonak`, v1.1 – orbit, parallel), TortMap
  (`foldrajz-9-10/13`, v1.1), FoldChoro (`foldrajz-9-10/01-idozonak`, v1.1 – kiemelt országok a
  `shared/foldrajz/orszagok.js` adatából), TortCards (`tortenelem-5-6/07`), `TortProj.equalEarth` a
  `shared/tort/proj.js`-ből. Lecke-saját: narancshéj-kiterítés (gömbi gerezdek), GPS-körök.

### 08 · `08-noveny` – Mi kell a babnak? – a növény részei és életfeltételei

- **Tanulási cél:** A növény élőlény: táplálkozik, lélegzik, növekszik, fejlődik, szaporodik, és
  reagál a környezetére (életjelenségek). A csírázáshoz víz, levegő és megfelelő hőmérséklet kell,
  fény nem. A kis növény a fényt keresi, és fény nélkül sápadt, nyurga marad. Hogy mi kell a
  növénynek, azt *tisztességes kísérlettel* tudjuk meg: egyszerre csak egy feltételt változtatunk,
  és van kontroll. A gyökér vizet és ásványi anyagokat vesz fel, a szár szállít és tart, a levél a
  napfény segítségével a levegő szén-dioxidjából és vízből tápanyagot készít, közben oxigén szabadul
  fel. A virágból termés, a termésben mag lesz. A fás szárú növény törzse évről évre vastagszik:
  az évgyűrűkből a kora is leolvasható.
- **Kerettanterv:** (8.) „felismeri és megnevezi a növények életfeltételeit, életjelenségeit” ·
  „felismeri és megnevezi a növények részeit, megfigyeli jellemzőiket, megfogalmazza ezek
  funkcióit” · „azonosítja a lágy szárú és a fás szárú növények testfelépítése közötti
  különbségeket” · „A növények életfeltételeinek igazolása” · „Növényi részek (gyökér, szár, levél,
  virágzat, termés) és funkcióik megnevezése” · „Növények életciklusainak vizsgálata jellegzetes
  zöldségeink, gyümölcsféléink példáján” · (3.) „kísérletekkel igazolja a növények életfeltételeit”
  · (1.) „vizsgálat révén azonosítja a tipikus lágy szárú és fás szárú növények részeit”.
- **Tévhitek:** a növény a földből „eszik”, a tömege a talajból jön. A magnak a csírázáshoz fény
  kell. A növény nem lélegzik (éjjel-nappal lélegzik, nappal emellett fotoszintetizál is). Csak az
  zöldség, ami nem édes; a paradicsom „biztosan zöldség” (botanikailag termés – a konyhai és a
  botanikai csoportosítás más szempontú, mindkettő jogos). A fa a csúcsánál és a törzse
  közepén is nő (a törzs magassága egy adott ponton nem nő; a szög a fán nem emelkedik). Több
  víz mindig jobb.
- **Kulcsvizuál:** egy „kísérleti polc” négy-hat cserépből, mindegyik előtt címke a feltételekkel
  (fény, víz, hőmérséklet). Gyorsított időben (napok csúszkája) babszemek csíráznak: a kontroll
  zöld, a sötétben tartott sápadt és nyurga, a száraz nem csírázik, a hidegben lassú. A 4. lépésben
  egy átlátszó növény (lecke-saját rajz, TtIkon-stílusban). A gyökértől a levélig kék pöttyök
  áramlanak (BioFlow). Mellette a klasszikus kísérlet: színezett vízbe állított zellerszár vagy fehér
  virág, amely órák alatt elszíneződik. A 7. lépésben egy fatörzs-szelet, amelyre ráközelítünk, és
  látszanak az évgyűrűk.
- **Kipróbálom:** **„Tervezd meg a kísérletet!”** A diák minden cserépnél beállítja a fényt, a vizet
  és a hőmérsékletet. A lecke jelzi, ha egyszerre két dolgot változtatott („Így nem tudod, melyik
  számított!”). A növekedés zárt képletű *modell* (a feltételek minimuma szabja meg, Liebig-elv,
  „modell” bélyeggel). BioPlot-görbék: magasság–nap. Évgyűrűszámlálás: kattintsd végig a gyűrűket,
  a széles és keskeny évek mellé esős és száraz év címke kerül. Zöldség vagy gyümölcs? kártyák
  (TortCards), két szempont szerinti rendezéssel.
- **Tippelj!** 2. lépés: „Kicsírázik a bab a sötét szekrényben? igen / nem”. 5. lépés: „Honnan jön a
  fa tömegének nagy része? a földből / a vízből / a levegőből”.
- **Lépések:** Élő-e a babszem? · Csírázás: víz, levegő, meleg · Tisztességes kísérlet: egyszerre
  egyet · Gyökér, szár, levél: ki mit csinál? · A levél konyhája · Virágból termés – zöldség vagy
  gyümölcs? · Lágy szár, fás szár, évgyűrűk · Összefoglalás.
- **Adatok:** a bab csírázása kb. 20 °C-on kb. 7–10 nap; 10 °C alatt alig csírázik *(becslés,
  kertészeti forrással)*. Egy évgyűrű = egy év (a mérsékelt övben; tavaszi világos és nyári
  sötétebb pászta). Egy nagy lombos fa nyári napon több száz liter vizet párologtathat el *(becslés:
  100–400 l/nap, forrással)*. A színezett víz a zellerszárban órák alatt felér *(becslés)*.
  Életjelenségek felsorolása a tankönyv szerint *(ellenőrizendő: NKP Természettudomány 5.)*. Van
  Helmont fűzfája csak hivatkozásként: a számok a `biologia-7-8/06` adataival egyezzenek.
- **Átfedés:** a biologia-7-8/06 3. lépése (van Helmont) itt nem jön újra. Az 5. lépés tippje csak
  felveti a kérdést, és a `> megjegyzés:` mondja ki, hogy 8. osztályban bővebben lesz róla szó.
  A fotoszintézis szóegyenlete („szén-dioxid + víz → cukor + oxigén”) itt csak szavakkal szerepel.
- **Építőkocka:** TtIkon (`10-erdo`: bab fejlődési szakaszai, paradicsom, alma, tölgy), BioFlow
  (`biologia-7-8/11-verkor`, v1.1 – általános gráf: gyökér → szár → levél élek, `kind: 'él'`,
  áramlás pulzálás nélkül, `surge: 0`), BioPlot (`biologia-7-8/07`), TortCards (`tortenelem-5-6/07`).
- **Kísérlet-bélyeg:** a csíráztatás és a színezett víz „otthon is kipróbálhatod” (ételfestékkel).

### 09 · `09-allat` – Hogyan halad a giliszta, ha nincs lába? – gerinctelenek és gerincesek

- **Tanulási cél:** Az állatokat sokféle szempont szerint csoportosíthatjuk. Az egyik legfontosabb:
  van-e gerincük. A gerinces állatoknak belső csontváza van, amely velük együtt nő. A rovaroknak
  kemény külső vázuk van, ezért vedleniük kell, hogy nőhessenek. Sokuk teljes átalakulással fejlődik
  (pete, lárva, báb, kifejlett rovar). A testfelépítés és a mozgás összefügg: a giliszta két
  izomrétegével hullámszerűen tolja magát, a csiga a talpán végigfutó hullámokkal csúszik, a hal a
  testét és a farkát hajlítja, az úszóhólyagjával lebeg. A fogazat elárulja, ki mit eszik
  (ragadozó, növényevő, mindenevő).
- **Kerettanterv:** (9.) „felismeri és megnevezi az állatok testrészeit, megfigyeli jellemzőiket,
  megfogalmazza ezek funkcióit” · „az állatokat különböző szempontok szerint csoportosítja” ·
  „azonosítja a gerinctelen és a gerinces állatok testfelépítése közötti különbségeket” · „Házi és
  ház körüli vagy vadon élő állatok testfelépítése és mozgásuk kapcsolatának vizsgálata” · „Házi,
  ház körüli vagy vadon élő gerincesek és gerinctelen állatok életciklusának vizsgálata” · fogalmak:
  „gerinctelen, gerinces, egysejtű, ragadozó, mindenevő, növényevő” · (1.) „megkülönbözteti a hely-
  és helyzetváltoztatást, és példákat keres ezekre megadott szempontok alapján”.
- **Tévhitek:** a gerinctelenek „egyszerűbbek”, „kevesebben vannak” (a leírt állatfajok kb. 95 %-a
  gerinctelen). A pók rovar (8 lába van). A kettévágott gilisztából két giliszta lesz (általában
  nem). A csiga a házát „felveszi”, mint egy kabátot (a háza vele nő, hozzá van nőve). A hal a vizet
  „belélegzi” a tüdejébe. A rovar folyamatosan nő, mint a kutya.
- **Kulcsvizuál:** a lecke egy kertben és a kerti tóban játszódik (TtIkon). 2–3. lépés: egy bogár
  és egy kutya csontváza egymás mellett (sematikus), aztán egy növekedési görbe-páros. A kutyáé sima,
  a rovaré lépcsős (vedlés), mellette a lepke életciklus-köre. 4. lépés: giliszta-metszet, a
  körkörös izmok (cinóber) és a hosszanti izmok (kékeszöld) felváltva húzódnak össze, a serték
  megkapaszkodnak, a test hullámban halad. 5. lépés: a csiga talpa alulról, hullámcsíkokkal. 6.
  lépés: hal oldalnézetben S-hullámmal, benne az úszóhólyag. 7. lépés: koponyák fogakkal (róka,
  nyúl, sertés; sematikus, nem anatómiai illusztráció).
- **Kipróbálom:** a gilisztánál kapcsolók („csak körkörös izom”, „csak hosszanti izom”, „serték
  nélkül”): egyik sem elég egyedül, csak a kettő felváltva és a serték együtt viszik előre (zárt
  képletű hullám, *modell*). Úszóhólyag-csúszka: több gáz → a hal emelkedik, kevesebb → süllyed (a
  felhajtóerő kvalitatív, a fizika-7-8/07-re hivatkozva). Gerinces–gerinctelen kártyák (TortCards:
  földigiliszta, éti csiga, keresztes pók, katicabogár, rák, ponty, béka, gyík, cinege, sün, denevér).
  Fogazat-párosítás: koponya → táplálkozás.
- **Tippelj!** 1. lépés: „Melyikből van több faj: gerincesből vagy gerinctelenből?”. 4. lépés: „Melyik
  izom kell a giliszta haladásához? a körkörös / a hosszanti / mindkettő”.
- **Lépések:** Gerinces vagy gerinctelen? · Váz kívül, váz belül · Kinőtt páncél: vedlés és
  átalakulás · A giliszta két izomrétege · A csiga hullámzó talpa · A hal: farok, uszony,
  úszóhólyag · Fogakból kiderül: ki mit eszik? · Összefoglalás.
- **Adatok:** a leírt állatfajok kb. 95 %-a (forrásonként 95–97 %) gerinctelen *(becslés)*; leírt
  rovarfaj kb. 1 millió (a `biologia-7-8/04` adatával egyezzen). A rovar 6 lábú (3 pár), a pók 8
  lábú. A földigiliszta szelvényeinek száma kb. 110–180 *(ellenőrizendő)*. A széncinege fiókái
  kb. 2–3 hét alatt repülnek ki *(ellenőrizendő)* – opcionális életciklus-példa. A hely- és
  helyzetváltoztatás példái a 9. lépés helyett a 2. lépés megjegyzésében („a csiga helyet változtat,
  a kagyló kinyitja a héját: helyzetet”).
- **Átfedés:** a biologia-7-8/10 (emelő, kar) az emberi mozgásé. Itt csak a „váz kívül / belül”
  összevetés jön. A gerinces osztályok részletes jellemzése a biologia-7-8/04-torzsfa – ott a fa,
  itt csak a gerinc szempontja.
- **Építőkocka:** TtIkon (`10-erdo`), TortCards (`tortenelem-5-6/07`), BioPlot (`biologia-7-8/07` –
  sima és lépcsős növekedési görbe). Lecke-saját: giliszta-, csiga- és halmozgás (zárt képletű
  hullámok).
- **Ábrázolás:** a koponyák és a vázak sematikusak, vér és sérülés nélkül. Az állatkísérlet
  („gilisztavizsgálat”) a valóságban kíméletesen, rövid ideig, visszaengedéssel. A panel egy
  mondatban kimondja, ha a lecke ezt ajánlja.

### 10 · `10-erdo` – Miért siet a hóvirág? – az erdő szintjei és táplálékhálózata

- **Tanulási cél:** Az erdő életközösség: a növények, gombák és állatok egymásra vannak utalva, és
  az élettelen környezettől (fény, víz, hőmérséklet, talaj) függenek. Az erdőnek szintjei vannak
  (lombkorona, cserje, gyep, moha). Minden szintre kevesebb fény jut le. A sűrű bükkösben
  nyáron a napfénynek csak néhány százaléka ér az erdő aljára. Ezért virágzik a hóvirág és az odvas
  keltike kora tavasszal, mielőtt a fák kilombosodnak. A hazai erdők típusa a magasságtól és a
  csapadéktól függ (tölgyes lent, bükkös feljebb, fenyves természetesen csak kevés helyen). A
  táplálékláncokból háló lesz. Ha egy faj eltűnik, az sok más fajra hat. A holtfa és az avar is
  életet hordoz (lebontók). Az erdőgazdálkodás módja megszabja, mi marad az életközösségből.
- **Kerettanterv:** (10.) „életközösségként értelmezi az erdőt” · „felismeri és magyarázza az
  élőhely-életmód-testfelépítés összefüggéseit az erdők életközössége esetén” · „táplálékláncokat és
  azokból táplálékhálózatot állít össze a megismert erdei növény- és állatfajokból” · „példákon
  keresztül bemutatja az erdőgazdálkodási tevékenységek életközösségre gyakorolt hatásait” ·
  „Tölgy-, bükk- és fenyőerdők összehasonlítása” · „A növényzet környezeti igénye és előfordulása
  közti összefüggés” · „tisztában van az erdő természetvédelmi értékével, fontosnak tartja annak
  védelmét”.
- **Tévhitek:** az erdő csak fák összessége. Az erdő alján is ugyanannyi fény van, mint a réten. A
  hóvirág „fázós”, mégis télen virágzik – hogyan? (a fény miatt siet). A korhadó fa „szemét”, el
  kell takarítani. A ragadozó „rossz”, nélküle jobb lenne az erdőnek. Minden fenyves természetes. A
  gomba növény.
- **Kulcsvizuál:** egy hazai lomberdő **metszete** (FoldSection terepvonallal, a fák és lágyszárúak
  TtIkon-rajzai). Az emeletek színsávokkal jelöltek, a bal oldalon egy „fénymérő” oszlop (a lejutó
  fény %-a szintenként). 3. lépés: egy év forog le az erdő alján (dátumcsúszka). Februárban
  hóvirág, márciusban keltike, áprilisban kihajtanak a fák, és az erdő alja elsötétül. Mellette
  BioPlot: a lejutó fény % és a virágzás időszaka egy éven át. 4. lépés: egy hegyoldal-szelvény
  (Alföldtől a Bükkig), a magassággal váltakozik a tölgyes és a bükkös, a fenyves csak egy
  „telepített” címkés foltban. 5–6. lépés: BioNet-háló a lecke fajaival.
- **Kipróbálom:** dátumcsúszka (az év napja) a fénnyel és a virágzással. Erdőtípus-csúszka: tölgyes
  ↔ bükkös → lejutó fény (Beer–Lambert-szerű *modell*: I = I₀ · e^(−k · LAI), a levélfelület-index
  az erdőtípus és az évszak szerint). **Láncépítő:** a diák kattintással rak össze egy láncot (ki
  kit eszik?), a hibás lépés pirosan villan („a cinege nem eszik makkot”). „Vedd ki!” – egy faj
  kivétele a hálóból (BioNet `cascade`, ▲/▼ jelek, *kvalitatív modell*). Erdőgazdálkodás:
  „tarvágás / szálaló vágás” kapcsoló és 0–60 év időcsúszka – a fajszám és a holtfa mennyisége
  *(modell)*.
- **Tippelj!** 2. lépés: „Mennyi fény jut le nyáron a bükkös aljára? a fele / a tizede / a
  huszada”. 6. lépés: „Ha eltűnnek a cinegék, mi lesz a hernyókkal? kevesebb / több / ugyanannyi”.
- **Lépések:** Az erdő emeletei · Mennyi fény jut le? · Egy év az erdő alján – a hóvirág siet ·
  Tölgyes, bükkös, fenyves · Ki kit eszik? · Láncból háló · A holtfa is él · Összefoglalás: az
  ember és az erdő.
- **Adatok:** lejutó fény nyáron: bükkös kb. 2–5 %, tölgyes kb. 10–20 % *(becslés)*. A modell
  levélfelület-indexe (LAI): bükkös nyáron kb. 6, tölgyes kb. 4, lombtalanul kb. 0,5; k ≈ 0,5 →
  e^(−3) ≈ 5 %, e^(−2) ≈ 14 %, e^(−0,25) ≈ 78 % *(modell, becsült LAI)*. A bükk lombfakadása kb.
  április vége – május eleje, a hóvirág virágzása február–március *(becslés; évjárat- és
  helyfüggő)*. Hazai erdőtípusok magassága (tankönyvi közelítés): tölgyesek kb. 200–600 m, bükkösök
  kb. 600 m fölött; a fenyvesek nagy része telepített, őshonos erdeifenyves csak néhány tájon (pl.
  Őrség) *(ellenőrizendő: NKP Természettudomány 6., a kerettanterv-kísérő tankönyv beosztása)*.
  Magyarország erdősültsége kb. 22 % *(ellenőrizendő, frissítendő: NÉBIH Országos Erdőállomány
  Adattár)*. A szarvasbogár lárvája 3–5 évig fejlődik korhadó fában *(ellenőrizendő)*. A
  kikeleti hóvirág védett *(ellenőrizendő: a természetvédelmi rendelet aktuális listája)* – a panel
  „ne szedd le” üzenetet ad, nem tiltásként, hanem indoklással.
- **A lecke fajai** (mind TtIkon-kulcs): kocsánytalan tölgy, bükk, gyertyán, mogyoró, hóvirág, odvas
  keltike, moha, csiperke/vargánya (gomba), gyapjaslepke hernyója, szarvasbogár, földigiliszta,
  széncinege, nagy fakopáncs, szajkó, mókus, vaddisznó, őz, róka, héja, erdei egér.
- **Átfedés:** a biologia-7-8/06 energiapiramisa és „90 % elszáll” szabálya nem jön ide. Ott általános
  hálózat, itt a hazai erdő a szintjeivel és az évével.
- **Építőkocka:** **TtIkon (referencia, ebben épül)**; BioNet (`biologia-7-8/04-torzsfa`, v1.1 – háló,
  `cascade`, `badges`, `flow`), BioPlot (`biologia-7-8/07`), FoldSection (`foldrajz-9-10/03` – terep- és
  talajvonal, hegyoldal-szelvény). Az ikonkészlet kiindulópontja a `biologia-7-8/06` és `05` lecke-saját
  `IC` rajzai (tölgy, fű, nyúl, róka, cinege, héja, fűz, bükkfa, lucfenyő…): átrajzolva, a TtIkon
  API-jára igazítva.

### 11 · `11-ret-szanto` – Mi lenne a réttel kaszálás nélkül? – rét, szántóföld és a talaj

- **Tanulási cél:** A rét, a legelő és a szántóföld fátlan élőhely. A hazai rétek nagy része a
  kaszálásnak és a legeltetésnek köszönhetően marad meg: nélküle cserjés, majd erdő nőne a helyén.
  Ez kultúrtáj, az ember és a természet közös műve. A réten sokféle növény és állat él (ürge,
  kerecsensólyom, túzok, sáskák, lepkék), sűrű táplálékhálózattal. A búzatábla egyféle növény,
  kevesebb fajjal. A talaj élő rendszer: ásványi szemcsék, humusz, víz, levegő és rengeteg élőlény.
  A talaj lassan képződik, de gyorsan elhordhatja az eső, ha nincs rajta növénytakaró. Védi a
  komposzt (tápanyag-visszapótlás), a vetésforgó, a növénytakaró és a biológiai védekezés
  (katicabogár a levéltetű ellen).
- **Kerettanterv:** (11.) „megadott szempontok alapján összehasonlítja a rétek és a szántóföldek
  életközösségeit” · „táplálékláncokat és azokból táplálékhálózatot állít össze a megismert mezei
  növény- és állatfajokból” · „példákon keresztül mutatja be a mezőgazdasági tevékenységek
  életközösségre gyakorolt hatásait” · „A természeti és a kultúrtáj” · „tisztában van a fátlan
  társulások természetvédelmi értékével, fontosnak tartja azok védelmét” · (1.) „megfigyeli a talaj
  élő és élettelen alkotóelemeit, tulajdonságait, összehasonlít különböző típusú talajféleségeket,
  valamint következtetések révén felismeri a talajnak mint rendszernek a komplexitását” · (15.)
  „tisztában van azzal, hogy a talajpusztulás világméretű probléma” · (15.) „ismer olyan
  módszereket, melyek a talajpusztulás ellen hatnak (tápanyag-visszapótlás, komposztkészítés,
  ökológiai kertművelés)” · (8.) „Biológiai védekezés formái a kertekben”.
- **Tévhitek:** a rét „magától” rét marad. A kaszálás árt a rétnek (a túl korai igen, de nélküle
  eltűnik). A föld „csak kosz”, élettelen. A talaj gyorsan újraképződik. A gyom és a kártevő
  „rossz” élőlény (az ember szempontjából az). Minden mezőgazdaság egyforma hatású. A vegyszer az
  egyetlen védekezés.
- **Kulcsvizuál:** egy alföldi táj, kettévágva. Bal oldalt kaszálórét (sokféle virág, ürgelyuk,
  túzok, sólyom), jobb oldalt búzatábla (TtIkon). Alul egy kinyíló **talajszelvény-ablak** (FoldSection
  rétegek: humuszos feltalaj, altalaj, alapkőzet), a nagyító (KemLab.lens helyett a BioZoom egy
  szintje) giliszták, gombafonalak, baktériumpöttyök felé közelít. 4. lépés: időcsúszka (0–60 év),
  a rét képe kaszálás nélkül változik: magas fű, kökény, galagonya, végül fiatal erdő. 6. lépés:
  két lejtő eső alatt (csupasz szántó, füves): a lefolyó víz barna és tiszta, alatta egy
  „elhordott talaj” oszlop.
- **Kipróbálom:** „Rét / szántó” kapcsoló → két BioNet-háló és egy fajszám-oszlop (BioPlot). Szukcesszió-
  időcsúszka. Esőcsúszka (csapadék intenzitása) és borítás-csúszka (0–100 % növény) → elhordott
  talaj (*modell*, „modell” bélyeggel). Talaj-kördiagram (MatChart): a diák húzza a szeleteket,
  és megnézi a tankönyvi arányt. Komposzt-időcsúszka: a konyhai hulladékból humusz lesz.
- **Tippelj!** 4. lépés: „Mi lesz a kaszálatlan rétből 40 év alatt? ugyanilyen rét / bokros /
  erdő”. 6. lépés: „Melyik lejtőről visz el több földet az eső?”.
- **Lépések:** Rét, legelő, szántó – természeti és kultúrtáj · Ki él a réten? · A búzatábla:
  kevesebb faj · Kaszálás nélkül: bokor, aztán erdő · Mi van egy marék földben? · Eső a lejtőn ·
  Vissza a talajba: komposzt és katica · Összefoglalás.
- **Adatok:** a „tankönyvi” talaj térfogat szerint kb. 45 % ásványi anyag, 5 % szerves anyag (humusz),
  25 % víz, 25 % levegő *(idealizált arány, a panel kimondja)*. 1 cm talaj képződése akár 1000 év
  is lehet *(FAO, 2015, Nemzetközi Talajév)*. Egy gramm termőtalajban kb. 100 millió – 1 milliárd
  baktérium *(becslés)*. Szukcesszió: a felhagyott rét 5–15 év alatt bokrosodik, 30–60 év alatt
  fiatal erdő lehet *(becslés; termőhelyfüggő, az Alföld szárazabb részein lassabb)*. Magyarország
  területének kb. 40 %-a szántó *(ellenőrizendő, frissítendő: KSH)*. A túzok a legnehezebb repülni
  képes európai madár, a kakas 10–16 kg *(ellenőrizendő)*. A túzok és az ürge fokozottan védett
  *(ellenőrizendő)*. Egy katicabogár naponta több tucat levéltetűt is megehet *(becslés:
  forrásonként 20–50)*. A világrekord-fajgazdagságú gyepek a Kárpát-medence peremén is vannak (98 faj
  10 m²-en, Erdély) *(ellenőrizendő: Wilson és mtsai 2012, J. Veg. Sci.)* – csak ha a forrás
  megerősíti.
- **A lecke fajai:** fűfélék, réti here, pipacs, búzavirág, búza, sáska, lepke, házi méh, levéltetű,
  katicabogár, földigiliszta, mezei pocok, ürge, mezei nyúl, fürj, túzok, egerészölyv,
  kerecsensólyom, róka.
- **Átfedés:** a biologia-7-8/09-monokultura a kártevő terjedését és a génmegőrzést mutatja. Itt a
  rét fenntartása, a fajszám és a talaj kerül előtérbe. Ez a lecke a szukcessziót is pótolja, amely a
  biológia-sorozatból hiányzik (`pilot/biologia-7-8/terv.md`, 6. fejezet).
- **Építőkocka:** TtIkon (`10-erdo`), BioNet (`biologia-7-8/04`, v1.1), BioPlot (`biologia-7-8/07`),
  MatChart (`matematika-5-6/10`, v1.1 – kördiagram), FoldSection (`foldrajz-9-10/03` – talajszelvény,
  lejtő), BioZoom (`biologia-7-8/01-sejt` – talaj-nagyítás, két-három szint).

### 12 · `12-to` – Mi él egy csepp tóvízben? – vízi és vízparti életközösségek

- **Tanulási cél:** A tó a parttól a közepéig övekre tagolódik: ligeterdő (fűz, nyár, éger), nádas,
  hínárnövényzet, nyílt víz. Mindegyik a víz mélységéhez és a fényhez igazodik. A vízben élők a
  testükkel alkalmazkodnak: kopoltyú, úszóláb, gázlóláb, lemezes csőr. A vízben sokkal kevesebb az
  oxigén, mint a levegőben, és a meleg víz még kevesebbet tud oldani. Egy csepp tóvíz tele van
  szabad szemmel láthatatlan élőlényekkel (moszatok, papucsállatka, vízibolha). Ezek a vízi
  táplálékláncok alapjai. Ha túl sok tápanyag kerül a vízbe (műtrágya, szennyvíz), elszaporodnak az
  algák. Elhalásukkor a lebontók elhasználják az oxigént, és a halak elpusztulhatnak. A lecsapolt
  mocsarakkal és a szabályozott folyókkal élőhelyek tűntek el.
- **Kerettanterv:** (12.) „életközösségként értelmezi a vizes élőhelyeket” · „összehasonlítja a vízi
  és szárazföldi élőhelyek környezeti tényezőit” · „felismeri és magyarázza az
  élőhely-életmód-testfelépítés összefüggéseit a vízi és vízparti életközösségek esetén” ·
  „táplálékláncokat és ezekből táplálékhálózatot állít össze a megismert vízi és vízparti növény-
  és állatfajokból” · „példákon keresztül bemutatja a vízhasznosítás és a vízszennyezés
  életközösségre gyakorolt hatásait” · „A vízi növények környezeti igényei és térbeli
  elhelyezkedésük közti összefüggés” · fogalmak: „hínárnövényzet, ligeterdő, légzőgyökérzet,
  kopoltyú, úszóláb, gázlóláb, lemezes csőr” · (9.) „mikroszkóp segítségével megfigyel egysejtű
  élőlényeket”.
- **Tévhitek:** a tiszta, átlátszó víz „üres”. A hal a vízből a hidrogént vagy a „vizet lélegzi”. A
  vízben ugyanannyi oxigén van, mint a levegőben. A több tápanyag „jót tesz” a tónak. Nyáron
  azért döglenek a halak, mert „meleg a víz” (mert kevesebb benne az oxigén). A nád „gaz”. Minden
  mocsár „haszontalan”.
- **Kulcsvizuál:** egy tó keresztmetszete (FoldSection: part, sekély, mély; víz minta). A parttól
  befelé az övek TtIkon-rajzokkal, a mélységgel csökkenő fény sávosan. 2. lépés: **BioZoom** egy
  vízcseppbe: tó → csepp → 1 mm (vízibolha) → 0,2 mm (papucsállatka csillókkal) → moszatok, a
  sarokban léptékvonalzó. 3. lépés: kattintható madarak lábbal és csőrrel kinagyítva. 4. lépés: egy
  liter levegő és egy liter víz „oxigénpöttyei” egymás mellett. 5. lépés: BioNet-lánc. 6. lépés:
  tápanyag-csúszka, a víz zöldül, a fény a mélyben eltűnik, az oxigéngörbe éjjel leesik, a
  halikonok a felszínre jönnek, aztán elhalványulnak (nincs tetem-ábrázolás).
- **Kipróbálom:** BioZoom log-csúszka. Madárválasztó: láb és csőr → élőhely és táplálék (szürke gém,
  tőkés réce, kárókatona, nádirigó). Víz-hőmérséklet-csúszka (0–30 °C) → oldott oxigén mg/l (valódi
  oldhatósági görbe). Tápanyag-csúszka → algák, átlátszóság, hajnali oxigén (*modell*). A
  tápláléklánc összerakása (mint a 10-esben).
- **Tippelj!** 4. lépés: „Hányszor több oxigén van egy liter levegőben, mint egy liter vízben? 2 / 10
  / 30”. 6. lépés: „Jót tesz a tónak a sok tápanyag? igen / nem / egy ideig”.
- **Lépések:** A parttól a tó közepéig · Egy csepp tóvíz · Úszóláb, gázlóláb, lemezes csőr ·
  Lélegezni a víz alatt · A tó tápláléklánca · Túl sok tápanyag: algavirágzás · Lecsapolt mocsarak,
  szabályozott folyók · Összefoglalás.
- **Adatok:** oxigén a levegőben: a levegő sűrűsége (1,204 g/l) × az oxigén tömegaránya (23,1 %) ≈
  0,278 g/l = **278 mg/l**. Oldott oxigén telítésben: 0 °C 14,6 mg/l, 10 °C 11,3 mg/l, 20 °C
  9,1 mg/l, 30 °C 7,6 mg/l *(ellenőrizendő: USGS DO-táblázat, 1013 hPa, édesvíz)* → 20 °C-on
  278 / 9,1 ≈ **30-szoros**. A halak 4–5 mg/l alatt szenvednek, kb. 2 mg/l alatt pusztulnak
  *(becslés, fajfüggő)*. Papucsállatka 0,18–0,3 mm (a `biologia-7-8/01` adatával egyezik),
  vízibolha 1–5 mm, a zöldmoszatok néhány µm-esek, a kovamoszatok 20–200 µm-esek *(becslés)*.
  Balaton: kb. 594 km², átlagos mélysége kb. 3,2 m; az 1970–80-as évek algavirágzásai után épült a
  Kis-Balaton Vízvédelmi Rendszer (első ütem 1985) *(ellenőrizendő)*. A 19. századi lecsapolások és
  a folyószabályozás előtti vizes élőhelyek (pl. Ecsedi-láp, Hanság, Sárrét) – vázlatos réteg, a
  Tisza-szabályozásra a `foldrajz-9-10/08` hivatkozik.
- **A lecke fajai:** fehér fűz, fekete nyár, mézgás éger, nád, gyékény, sás, fehér tündérrózsa,
  békalencse, átokhínár, zöldmoszat, papucsállatka, vízibolha, szúnyoglárva, szitakötő és lárvája,
  kecskebéka, ponty, keszeg, csuka, szürke gém, tőkés réce, kárókatona, nádirigó. A „légzőgyökérzet”
  (mocsárciprus) idegenhonos parkfa – a panel egy mondatban kimondja.
- **Átfedés:** a kemia-7-8/12 a víztisztítást mutatja. Itt a szennyvíztisztító telep csak
  megjegyzésként szerepel („látogatás”, javasolt tevékenység).
- **Építőkocka:** TtIkon (`10-erdo`), BioZoom (`biologia-7-8/01-sejt`), BioNet (`biologia-7-8/04`,
  v1.1), FoldSection (`foldrajz-9-10/03`), BioPlot (`biologia-7-8/07` – oldott oxigén, napi görbe).
- **Biztonság:** vízparton csak felnőttel; a jégre lépni életveszélyes (a 01-es leckével közös
  mondat, ha a téli tó szóba kerül).

### 13 · `13-emberi-test` – Mi történik a testedben, ha futsz? – szervek együttműködése, egészség

- **Tanulási cél:** A test szervekből, a szervek szervrendszerekből állnak, és ezek *együtt*
  dolgoznak. Futáskor az izmoknak több oxigén és tápanyag kell. Ezért a szív gyorsabban ver, a
  légzés gyorsul és mélyül, a test felmelegszik, és az izzadás hűt. Pihenéskor minden visszaáll. A
  rendszeres mozgás erősíti a szívet. Kamaszkorban a test gyorsan nő és átépül. Ez mindenkinél
  máskor kezdődik, és ez így rendben van. Az egészséges életmódhoz mozgás, alvás, változatos étkezés
  és az érzékszervek védelme tartozik (pl. a hangos zene károsíthatja a hallást).
- **Kerettanterv:** (13.) „felismeri és megnevezi az emberi test fő részeit, szerveit” · „látja az
  összefüggéseket az egyes szervek működése között” · „érti a kamaszkori testi és lelki változások
  folyamatát, élettani hátterét” · „tisztában van az egészséges életmód alapelveivel, azokat
  igyekszik betartani” · „A mozgás és a fizikai, szellemi teljesítőképesség összefüggései” ·
  „Táplálékpiramis” · „Az érzékszervek védelmét biztosító módszerek és eszközök”.
- **Tévhitek:** a szív „pumpálja a levegőt”. A tüdő maga mozog (a rekeszizom és a bordaközi izmok
  mozgatják). Az izzadás „a gyengeség jele” (a hűtés módja). Aki lassabban nő, az „lemaradt”. A
  hallás károsodása fáj, tehát észrevesszük (nem, lassan és fájdalom nélkül jön). A fülhallgató
  nem árt, ha „csak egy kicsit hangos”. Van „tiltott” étel.
- **Kulcsvizuál:** a BioBody semleges alakja (álló póz), a rétegek kapcsolhatók (csont, izom,
  keringés, légzés, emésztés). 2–4. lépés: az alak „fut” (stilizált, a testrajz helyben marad, a
  háttér mozog). Mellette három élő műszer: pulzus, légzésszám, testhőmérséklet, alattuk BioPlot-
  idősor. A BioFlow egyszerűsített köre mutatja az oxigén útját a tüdőtől az izomig (oxigéndús
  `#c0392b`, oxigénszegény `#7b2440`, a biológia színkódja szerint). 5. lépés: két átlagos
  növekedési sebesség-görbe (lányok, fiúk) széles „mindenki más” sávval. Nincs nemi jelleg, nincs
  minősítés. 6. lépés: egy tányér (MatChart kördiagram) az OKOSTÁNYÉR® arányaival és mellette a
  tankönyvi táplálékpiramis. 7. lépés: egy hangerő-skála (dB) mindennapi hangokkal és mellette a
  biztonságos hallgatási idő.
- **Kipróbálom:** „Futás / séta / pihenés” kapcsoló és időcsúszka. A pulzus, a légzés és a hő zárt
  képlettel közelít a célértékhez, és pihenéskor visszaáll (*modell*, „modell” bélyeggel). Edzettség-
  csúszka: edzettebbnél a nyugalmi pulzus kisebb. Hangerő-csúszka (60–110 dB) → biztonságos idő
  (3 dB-enként felére esik). A tányér szeleteinek húzása, a végén összevetés az ajánlással
  (nincs pontozás, nincs „rossz” étel).
- **Tippelj!** 2. lépés: „Futáskor mi gyorsul? csak a szív / csak a légzés / mindkettő”. 7. lépés:
  „Mennyi ideig hallgathatsz biztonságosan 94 dB-es zenét naponta? 8 óra / 1 óra / 5 perc”.
- **Lépések:** Szervek és szervrendszerek · Indul a futás · Oxigén a tüdőtől az izomig ·
  Melegszel? Az izzadás hűt · Kamaszkor: a test átépül · Mit tegyél a tányérodra? · Védd a füled! ·
  Összefoglalás: egy egészséges nap.
- **Adatok:** nyugalmi pulzus 10–12 éveseknél kb. 70–100/perc *(ellenőrizendő: Fleming és mtsai
  2011, Lancet, életkori centilisek)*. Erős terhelésnél akár 180–200/perc *(becslés)*. Légzésszám
  nyugalomban kb. 15–20/perc, terheléskor kb. 40/perc *(becslés)*. Testhőmérséklet kb. 36–37 °C.
  Mozgás 5–17 éveseknek naponta átlagosan legalább 60 perc közepes vagy nagy intenzitással (WHO,
  2020). Alvás 6–12 éveseknek 9–12 óra (AASM, 2016) – a 05-ös leckével egyezzen. Növekedési ugrás: a
  legnagyobb növekedési sebesség lányoknál átlagosan kb. 11–12 évesen (kb. 8 cm/év), fiúknál kb.
  13–14 évesen (kb. 9–10 cm/év); egyénenként évekkel eltérhet *(becslés; forrás: növekedési
  referenciák)*. Hallás (ITU-T H.870 / WHO *Safe Listening*): heti 40 óra 80 dB-en felnőttnek, 75 dB-en
  gyerekeknek. A munkahelyi szabály: 85 dB napi 8 óra, minden +3 dB felezi az időt → 88 dB 4 óra,
  91 dB 2 óra, 94 dB 1 óra, 97 dB 30 perc, 100 dB 15 perc *(ellenőrizendő: NIOSH)*. A panel
  kimondja, hogy gyerekeknél a WHO szigorúbb határt ajánl. Táplálkozás: OKOSTÁNYÉR® (Magyar
  Dietetikusok Országos Szövetsége) *(ellenőrizendő: aktuális változat és arányok)*; a tankönyvi
  táplálékpiramis csak összevetésként.
- **Átfedés:** a vérkör (biologia-7-8/11), a gázcsere (12), a reflex (13) és az újraélesztés (17)
  részletei nem jönnek ide. A lecke azt mutatja, hogy a szervek összehangoltan működnek.
  Hivatkozás: „7–8. osztályban részletesen”.
- **Építőkocka:** BioBody (`biologia-7-8/10-mozgas` – álló póz, `build` váltakozva), BioFlow
  (`biologia-7-8/11-verkor`, v1.1 – egyszerűsített kör), BioPlot (`biologia-7-8/07`), MatChart
  (`matematika-5-6/10`, v1.1 – tányér). Spec: `"review": ["egészség"]`, `"sources": true`.
- **Ábrázolás:** lásd 7. fejezet: semleges testrajz, több alkat, egyik sem „ideális”. Nincs
  testsúly-, BMI- vagy kalóriacél. A kamaszkori lelki változásokról egy semleges mondat szól
  („hangulatváltozás, új érzések – természetes; beszélj róla valakivel, akiben megbízol”). A
  szenvedélybetegség (dohányzás) csak a lefedettségben, nem animálva.

### 14 · `14-energia` – Honnan jön az áram a konnektorba? – energiaforrások

- **Tanulási cél:** Az áram erőművekből jön, és az erőművek valamilyen energiaforrást
  használnak. Szinte minden energiaforrás a Napból ered: a szél, a víz körforgása, a növények, sőt
  a szén, a kőolaj és a földgáz is (régen élt élőlények elraktározott napfénye). A megújuló
  energiaforrás emberi léptékű idő alatt újratermelődik (nap, szél, víz, biomassza), a nem megújuló
  millió évek alatt képződött, és elfogy (szén, kőolaj, földgáz, urán). A bányászat és az égetés
  átalakítja a tájat és szennyezi a levegőt (szmog, savas eső, üvegházhatás). A szélkerék kétszer
  erősebb szélben nyolcszor annyi energiát termel. A napelem éjjel nem termel, ezért kell tárolás vagy
  más forrás. Takarékosan élni is energiaforrás.
- **Kerettanterv:** (14.) „csoportosítja az energiahordozókat különböző szempontok alapján” ·
  „példákat hoz a megújuló és a nem megújuló energiaforrások felhasználására” · „megismeri az
  energiatermelés hatását a természetes és a mesterséges környezetre” · „A bányászat környezeti
  hatásai” · „Légszennyező anyagok és hatásaik” · (3.) „megfigyeléseken és kísérleten keresztül
  megismeri az energiatermelésben szerepet játszó anyagokat és az energiatermelés folyamatát” · (3.)
  „Energiatakarékosság” · tevékenység: „Megújuló energiákat bemutató szélkerékmodellek készítése”.
- **Tévhitek:** az áram „a konnektorban van”. A megújuló energiának nincs környezeti hatása. A
  szén „kő”, nem élőlényből lett. A napelem felhős időben „semmit” nem termel (kevesebbet termel).
  Kétszer erősebb szél, kétszer annyi energia. Az energiatakarékosság „lemondás”.
- **Kulcsvizuál:** 1. lépés: egy lámpától visszafelé futó vezeték: falon át, transzformátor,
  távvezeték, erőmű. Az erőmű ikonja váltakozik (szén, gáz, atom, víz, szél, nap). 2. lépés: minden
  forrásból egy nyíl vezet vissza a Napig, a szénnél egy időspirál a 300 millió évvel ezelőtti
  mocsárerdőig (TtIkon-páfrányok). 4. lépés: külszíni bánya keresztmetszete, majd a rekultivált tó.
  6. lépés: szélkerék, szélsebesség-csúszkával. 7. lépés: **energiafalu** egy napon át: fogyasztási
  görbe (FoldChart), alatta a források halmozott területei.
- **Kipróbálom:** **szélkerék-csúszka** (2–12 m/s) → a teljesítmény oszlopa a v³ szerint, és „×8”
  felirat, ha a szél kétszeres. **Energiafalu-játék** (*modell*, kitalált falu): napelem-csúszka,
  szélkerék-csúszka, tároló-csúszka (akkumulátor) és egy „gázerőmű” tartalék. 24 órás időcsúszka. A
  hiány pirosan, a felesleg a tárolóba megy. Kijelzés: a gázerőmű üzemórái és egy füst-index.
  Megújuló vagy nem? kártyák (TortCards), két szempont szerint (megújuló/nem; a Napból ered/nem). LED
  ↔ izzó kapcsoló egy szobában: ugyanannyi fény, más fogyasztás.
- **Tippelj!** 6. lépés: „Ha kétszer erősebben fúj a szél, hányszor több áramot termel a szélkerék? 2 /
  4 / 8”. 7. lépés: „Elég-e éjjel a napelem, ha nappal sok van belőle?”.
- **Lépések:** Visszafelé a vezetéken · Szinte minden a Napból jön · Megújuló vagy nem megújuló? ·
  Bánya és táj · Füst a levegőben · A szélkerék titka · Napelem éjjel? – az energiafalu ·
  Összefoglalás: takarékosan.
- **Adatok:** a szél teljesítménye P = ½ · ρ · A · v³ → 2v → 8P (ρ = 1,2 kg/m³). A falu adatai
  *(kitalált példa, modell)*. Magyarország villamosenergia-termelése (2024): atom kb. 40–45 %,
  napenergia kb. 20–25 %, földgáz kb. 20 %, szén és lignit néhány %, a fogyasztás egy részét
  importáljuk *(ellenőrizendő, frissítendő: MAVIR 2024/2025; a panel csak kerekített arányt mond)*.
  Hazai szénféleségek: Mecsek – feketekőszén (jura, kb. 180–200 millió éves), Tatabánya–Dorog –
  barnakőszén (eocén, kb. 40–50 millió éves), Mátra–Bükkalja – lignit (pannon, kb. 6–8 millió éves)
  *(ellenőrizendő; a foldrajz-9-10/07 adataival egyeztetendő)*. A karbon kori mocsárerdők kb.
  300–360 millió évesek. LED kb. 8–9 W ≈ 60 W-os izzó fénye (kb. 800 lm) → kb. 85 %-kal kevesebb
  *(ellenőrizendő: termékcímke-adatok, átlag)*.
- **Átfedés:** az energiaátalakulási lánc (fizika-7-8/02), az üvegházhatás fizikája (fizika-7-8/14),
  a savas eső és a szmog kémiája (kemia-7-8/11), a kőolaj-lepárlás (kemia-7-8/14) nem ismétlődik. Itt a
  5. lépés egy-egy mondattal hivatkozik rájuk.
- **Építőkocka:** FoldChart (`foldrajz-9-10/10-nepesseg` – halmozott terület, idősor, forrássor),
  MatChart (`matematika-5-6/10`, v1.1 – arány-oszlop), TortCards (`tortenelem-5-6/07`), TtIkon
  (`10-erdo` – páfrány, zsurló, fa). Spec: `"sources": true` (a hazai arányok miatt).
- **Szerkesztési elv:** konkrét erőművet, céget, politikai vitát (pl. bővítés, bezárás) nem
  minősítünk. Minden forrásnak van előnye és hátránya, a lecke mindkettőt megmutatja (atom: nincs
  füst, de radioaktív hulladék; víz: megújuló, de átalakítja a folyót; nap: tiszta, de éjjel nem
  termel).

### 15 · `15-hegyek` – Hogyan kerül kagyló a hegytetőre? – kőzetek, gyűrődés, vetődés, vulkán

- **Tanulási cél:** Sok hazai hegység mészköve egykori tengerfenéken rakódott le, ezért van benne
  kagyló és csiga. A belső erők a rétegeket felemelik. Ha a kőzetrétegek oldalról összenyomódnak, és
  hajlékonyak, meggyűrődnek (gyűrt hegység, pl. Alpok, Kárpátok). Ha merevek, eltörnek, és a darabok
  (rögök) elmozdulnak: kiemelkedő rög, lesüllyedő árok (röghegység, pl. a Dunántúli-középhegység
  nagy része). A magma felszínre törve vulkánt épít (Mátra, Badacsony). A hirtelen elmozdulás
  földrengést okoz. A kőzetek egyszerű próbákkal megkülönböztethetők (szín, keménység, pezsgés). A
  tulajdonságuk szabja meg, mire használjuk őket.
- **Kerettanterv:** (15.) „megállapítja, összehasonlítja és csoportosítja néhány jellegzetes hazai
  kőzet egyszerűen vizsgálható tulajdonságait” · „példákat hoz a kőzetek tulajdonságai és a
  felhasználásuk közötti összefüggésekre” · „felismeri és összehasonlítja a gyűrődés, a vetődés, a
  földrengés és a vulkáni tevékenység hatásait” · „A gyűrődés és a vetődés folyamata” · „A gyűrt és
  a röghegységek alapvető formakincse” · „Belső és külső erők hatásai” · tevékenység: „A gyűrődés
  folyamatának modellezése textíliák, gyurma… felhasználásával”.
- **Tévhitek:** a hegyek „mindig is ott voltak”. A kagylót a hegyre „az özönvíz” vagy az ember vitte
  (a panel nem vitatkozik, csak a bizonyítékot mutatja: a kagyló a kőzet *belsejében* van, rétegben).
  A kő nem hajlik meg (lassan és mélyen, melegen igen). A vulkán „tűzhányó hegy”, amelyben tűz ég.
  A minivulkán (ecet + szódabikarbóna) ugyanaz, mint egy igazi kitörés. Magyarországon nincs
  földrengés.
- **Kulcsvizuál:** egy rétegsor-metszet (FoldSection, mészkő, homok, agyag, bazalt minta). 1. lépés:
  egy kirándulóösvény a Gerecsében (*vázlatos* rajz): a sziklafalban kagyló- és csigaházlenyomatok;
  „ráközelítés” és vissza az időben, a tengerfenékig. 2. lépés: üledék hull, rétegek épülnek
  (lent a régebbi). 3–4. lépés: oldalról egy „satu” nyomja a metszetet. A „rugalmas / merev” kapcsoló
  szerint a rétegek gyűrődnek (redők), vagy vetők mentén eltörnek, a rögök emelkednek, az árok
  süllyed. 5. lépés: a magma kürtőn feltör, lávatakaró, majd az idő lepusztítja körülötte a puhább
  réteget, és megmarad a tanúhegy (Badacsony-szerű forma). Rengésnél egy hirtelen elmozdulás
  hullámgyűrűi. 6. lépés: „kőzetpad” hat kőzettel.
- **Kipróbálom:** **„satu”-csúszka** (rövidülés 0–40 %) és **„rugalmas / merev”** kapcsoló: ugyanaz az
  erő, kétféle eredmény (zárt képletű redő- és vetőgeometria, *modell*). Kőzetvizsgálat: a diák
  kiválaszt egy kőzetet és egy próbát (köröm, rézpénz, acélszög, üveg karcolása; szín; „híg sósav”
  – ez csak tanári bemutató bélyeggel). Az eredmény egy táblázatba kerül, a végén a kőzet
  meghatározása. „Mire jó a kő?” párosítás (TortCards).
- **Tippelj!** 3. lépés: „Mi lesz a rétegekkel, ha oldalról összenyomjuk őket? eltörnek /
  meggyűrődnek / attól függ”. 6. lépés: „Melyik kőzet pezseg a sósavtól? gránit / mészkő / bazalt”.
- **Lépések:** Kagyló a hegytetőn · Réteg réteg hátán · Összenyomva meggyűrődik · Merev kő eltörik:
  rögök és árkok · Feltör a magma – és rezeg a föld · Kőzetvizsgálat: karc, szín, pezsgés · Mire jó a
  kő? · Összefoglalás.
- **Adatok** *(ellenőrizendő: a hazai földtani adatok a `foldrajz-9-10/07` lecke adataival
  egyeztetendők)*: Gerecse – jura mészkő ammoniteszekkel (kb. 200–145 millió éves); Budai-hegység –
  dolomit, mészkő; Badacsony és a Tapolcai-medence tanúhegyei – bazalt, kb. 3–8 millió éves; Mátra,
  Börzsöny – andezit, kb. 15 millió éves; Velencei-hegység – gránit, kb. 300 millió éves; lösz a
  Duna mentén (jégkorszak, szél hordta por). Mohs-féle keménység: köröm kb. 2,5, rézpénz kb. 3,5,
  üveg és acélkés kb. 5,5, kalcit (mészkő) 3, kvarc (a gránitban) 7. A mészkő késsel karcolható, a
  gránit kvarca az üveget karcolja. Felhasználás: mészkő → építőkő, mész, cement; bazalt → útépítés,
  zúzottkő; andezit → útburkolat, kőhíd; gránit → burkolat, emlékmű; agyag → tégla, cserép; homok →
  üveg, beton. Hazai rengések: 1763 Komárom (M kb. 6,3), 1911 Kecskemét (M kb. 5,6), 1956 Dunaharaszti
  (M kb. 5,6), 1985 Berhida (M kb. 4,9) *(ellenőrizendő: Kövesligethy Radó Szeizmológiai
  Obszervatórium; a `foldrajz-9-10/03` adataival egyeztetendő)*.
- **Átfedés:** a lemeztektonika (foldrajz-9-10/02) és a világ rengéskatalógusa (03) nem jön ide. A
  gyűrődés és a vetődés hétköznapi, „asztali” modell. Megjegyzés hivatkozik a 9–10.-es leckére: „hogy
  mi nyomja a kőzetet, azt 9. osztályban tanulod”.
- **Építőkocka:** FoldSection (`foldrajz-9-10/03`; `pattern`: mészkő, homok, agyag, bazalt, gránit,
  magma, láva, lösz; `poly` eltolással a rögökhöz), TortCards (`tortenelem-5-6/07`), KemGHS
  (`kemia-7-8/10` – „tanári bemutató” bélyeg a sósavhoz, GHS05), TortMap (`foldrajz-9-10/13`, v1.1 – a
  hazai helyek pöttyei).
- **Biztonság:** a sósavas próba csak „tanári bemutató”. Otthon a „kőzetpróba” köröm, pénz, szög:
  szemvédelem, felnőtt jelenléte a szögnél. A minivulkán „otthon is kipróbálhatod” (ecet +
  szódabikarbóna), a panel kimondja, hogy ez kémiai reakció, nem magma.

### 16 · `16-folyo` – Miért zavaros az árvíz? – a folyó munkája és vízjárása

- **Tanulási cél:** A folyó a forrásától a torkolatáig halad. A mellékfolyók a főfolyóba ömlenek, és a
  vízgyűjtő minden vize egy torkolat felé tart. Magyarország teljes területe a Duna vízgyűjtőjén
  van. A meredekebb lejtőn gyorsabban folyik a víz, a nagyobb vízhozamú folyó több vizet visz. A
  gyorsabb víz nagyobb munkát végez: többet és nagyobb darabokat szállít, és jobban vés. A víz
  sebessége kétszeresére nőve sokszor nagyobb követ is elgörget. Ahol a víz lelassul, ott lerakja a
  hordalékot. Ezért zavaros az árvíz, és ezért keletkezik a torkolatnál hordalékkúp vagy delta. A
  folyó vízjárása az éghajlattól függ: a Duna a hóolvadáskor és a kora nyári esőkkor árad.
- **Kerettanterv:** (15.) „magyarázza a felszín lejtése, a folyó vízhozama, munkavégző képessége és
  a felszínformálás közti összefüggéseket” · „magyarázza az éghajlat és a folyók vízjárása közötti
  összefüggéseket” · „A vízhozam, a munkavégző-képesség és a felszínformálás összefüggései” · „Az
  éghajlat és a vízjárás közti összefüggés” · tevékenység: „Vízhozammal kapcsolatos vizsgálatok
  elvégzése egy, az iskolához közeli természetes vízfolyáson vagy iskolai homokasztalon” · (6.)
  „ismeri a főfolyó, a mellékfolyó és a torkolat térképi ábrázolását” · (6.) „felismeri és
  megnevezi a legjelentősebb hazai álló- és folyóvizeket”.
- **Tévhitek:** a folyó azért folyik, mert „a tenger húzza”. A folyó dél felé folyik, mert a térképen
  lefelé van (észak felé is folyhat). A széles folyó mindig gyors. Kétszer gyorsabb víz kétszer
  nagyobb követ visz. A Duna Magyarországon ered. Az árvíz csak a sok esőtől van (a hóolvadás is
  számít). A Balaton a Duna része.
- **Kulcsvizuál:** 1–2. lépés: a Duna vízgyűjtője a térképen (TortMap, a `map-karpat.js` folyói, a
  D1 domborzati színezés). A Duna forrásától a deltáig egy kék „csepp” utazik, a mellékfolyók
  sorban bekapcsolódnak, a torkolat kiemelve. Kattintható hazai vizek (Duna, Tisza, Dráva, Rába,
  Szamos, Maros, Körösök, Zagyva, Sajó, Balaton, Velencei-tó, Fertő, Tisza-tó). 3–6. lépés: egy
  **virtuális homokasztal** (felülnézet és oldalnézet), a víz pöttyei FoldFlow-val áramlanak. A
  szemcsék (homok, kavics, kő) színkóddal mutatják, mit mozdít meg a víz, és hol rakja le. A végén
  egy kis hordalékkúp nő. 7. lépés: a Duna Budapestnél havi átlagos vízhozam-oszlopai (FoldChart),
  mellettük az Alpok hó-ikonja és a csapadék.
- **Kipróbálom:** **homokasztal:** lejtés-csúszka és vízhozam-csúszka. A kód kiírja a víz
  sebességét (*modell*), és megmutatja, melyik szemcseméret mozdul meg. A „hatodik hatvány” gomb
  ugyanannál a mederalaknál kétszerezi a sebességet, és 64-szer nagyobb tömegű kő is gurulni kezd
  (*egyszerűsített szabály*, a panel kimondja). Térképkvíz: „Kattints a Tiszára!”, „Melyik a
  mellékfolyó?”. Hónapkurzor a vízjárás-diagramon.
- **Tippelj!** 1. lépés: „Hová folyik végül a Tisza vize? a Balatonba / a Dunába / a Fekete-tengerbe
  (mindkettő igaz lehet!)”. 5. lépés: „Ha kétszer gyorsabb a víz, hányszor nehezebb követ görget? 2 /
  4 / 64”.
- **Lépések:** A forrástól a torkolatig · Hazai vizeink · Homokasztal: a lejtés · Homokasztal: a
  vízhozam · Kétszer gyorsabb víz, hatvannégyszer nehezebb kő · Hol vés, hol rak le? · Mikor árad a
  Duna? · Összefoglalás.
- **Adatok** *(ellenőrizendő: OVF/vízügyi igazgatóságok, HungaroMet; a `foldrajz-9-10/08` adataival
  egyeztetendő)*: a Duna hossza kb. 2850 km, vízgyűjtője kb. 817 000 km², magyarországi szakasza
  kb. 417 km; a Tisza hossza kb. 960 km. A Duna átlagos vízhozama Budapestnél kb. 2300–2400 m³/s; a
  2013-as rekordárvíz 891 cm-es vízállással *(ellenőrizendő)*. Vízhozam-arány a havi középértékekben:
  tavasz–kora nyár (április–június) a legnagyobb, ősz (szeptember–október) a legkisebb
  *(ellenőrizendő: havi átlagos vízhozam, Budapest, sokéves adat; forrás és licenc a `.md`-ben)*.
  Balaton kb. 594 km², Velencei-tó kb. 26 km², Fertő kb. 315 km² (ebből Magyarországon kb. 75 km²),
  Tisza-tó kb. 127 km² (mesterséges). „Hatodik hatvány” szabály (Airy, 19. század): a víz által
  elmozdítható szemcse tömege a sebesség hatodik hatványával arányos → 2⁶ = 64 *(egyszerűsített,
  közelítő szabály; a panel így nevezi)*. A homokasztal számai *(modell)*.
- **Átfedés:** a kanyarulat-vándorlás, a lefűződés és a Tisza-szabályozás (foldrajz-9-10/08) nem
  jön ide. Itt a lejtés–vízhozam–munkavégzés kapcsolat a fő gondolat, homokasztalon.
- **Építőkocka:** FoldFlow (`foldrajz-9-10/05` – sík mód, mező a meder alakjából), FoldSection
  (`foldrajz-9-10/03` – a homokasztal oldalnézete, lejtő), FoldChart (`foldrajz-9-10/10` – havi
  oszlop, forrássor), TortMap (`foldrajz-9-10/13`, v1.1 + `map-karpat.js` folyók), D1 (domborzati
  színezés). Lecke-saját: szemcse-mozgatás, hordalékkúp növekedése (zárt képlet az időből).
- **Ha a D1 nincs kész:** a térkép a TortMap alapstílusával készül, domborzat nélkül.

### 17 · `17-idojaras` – Esernyő kell holnap? – időjárás, éghajlat, éghajlati övezetek

- **Tanulási cél:** Az időjárás a légkör pillanatnyi állapota (ma délután esik). Az éghajlat egy hely
  sokéves (30 éves) átlagos időjárása (Budapesten a nyár meleg). Az éghajlat fő elemei a hőmérséklet
  és a csapadék, és ide tartozik a szél, a napsütés és a felhőzet is. Az időjárás-jelentés
  piktogramokkal, számokkal és szavakkal mondja el a várható időjárást. Az előrejelzés egyre
  pontosabb, de mindig valószínűséget mond. A forró övezet a térítők között, a mérsékelt a térítők
  és a sarkkörök között, a hideg a sarkkörökön túl van. A különbséget a napsugarak hajlásszöge
  okozza.
- **Kerettanterv:** (16.) „megnevezi az éghajlat fő elemeit” · „jellemzi és összehasonlítja az egyes
  éghajlati övezeteket (forró, mérsékelt, hideg)” · „értelmezi az időjárás-jelentést” · „piktogramok
  alapján megfogalmazza a várható időjárást” · „A forró, a mérsékelt és a hideg éghajlati övezet
  jellemzése” · (2.) „észleli, méri az időjárási elemeket, a mért adatokat rögzíti, ábrázolja”.
- **Tévhitek:** az időjárás és az éghajlat ugyanaz. Egy hideg nap „cáfolja” az éghajlatot. A „70 %
  eséllyel esik” azt jelenti, hogy a nap 70 %-ában esik. Az előrejelzés „mindig téved”. A forró
  övezetben mindenhol sivatag van. A hideg övezetben sok hó esik (kevés csapadék van). A sarkvidéken
  azért hideg van, mert messzebb van a Naptól.
- **Kulcsvizuál:** 1. lépés: ugyanaz a budapesti utca két képben. Az egyiken „ma” (eső, esernyő), a
  másikon egy 30 évet összegző „éghajlati” montázs (FoldClimate-diagram). 2. lépés: **műszerkert**
  (TtMuszer: hőmérő árnyékolt dobozban, csapadékmérő, szélzászló, szélmérő, napfénymérő), mind
  élő kijelzéssel. 3–4. lépés: Magyarország-térkép (TortMap) piktogramokkal (nap, felhő, eső, hó,
  zivatar, szél). 5. lépés: a földgömbön három pontra eső zseblámpafolt (Egyenlítő, Budapest,
  sarkkör). 6. lépés: TortGlobe a három övezettel, a 05-ös lecke tengelyéből számolt határokkal. 7.
  lépés: három éghajlati diagram egymás mellett, áttűnéssel (FoldClimate).
- **Kipróbálom:** **„Készíts időjárás-jelentést!”** – a diák egy adattáblából (városonként hőmérséklet,
  csapadék, felhőzet; *kitalált példa*) piktogramokat húz a térképre, és a lecke ellenőrzi.
  Fordítva is: piktogramos térkép → „mit vegyél fel holnap?” választás. Műszerkert: csapadékmérő
  töltése és leolvasása. Hónapkurzor a diagramokon. Valószínűség: „10 egyforma nap” rács, amelyből
  7 esős – így látszik a „70 %” jelentése.
- **Tippelj!** 1. lépés: „Budapesten tegnap 12 °C volt júliusban. Ez éghajlatváltozás? igen / nem
  – egy nap időjárás”. 8. lépés: „Mennyire bízhatsz az ötnapos előrejelzésben?”.
- **Lépések:** Időjárás vagy éghajlat? · Az időjárás elemei – a műszerkert · Olvasd le a
  piktogramokat! · Készíts időjárás-jelentést! · Miért meleg a trópus? · Három éghajlati övezet ·
  Három diagram: Manaus, Budapest, Utqiaġvik · Összefoglalás: mennyire bízhatsz az előrejelzésben?
- **Adatok:** éghajlati normál = 30 év átlaga (WMO). Budapest, Manaus (WMO 82331) és a hideg övezet
  állomása a WMO 1991–2020 klímanormákból (NOAA NCEI, ugyanaz a forrás és ugyanaz a jegyzet, mint a
  `foldrajz-9-10/09` leckében). Budapest és Manaus havi adatai onnan vehetők át (Budapest évi közép
  12,5 °C, csapadék 526,2 mm; Manaus évi közép kb. 27,4 °C, csapadék 2362,4 mm). **A hideg állomás**
  legyen sarkkörön túli, teljes csapadéksorral, pl. Utqiaġvik (Barrow, 71,3° É) vagy Tromsø (69,7° É)
  *(ellenőrizendő: van-e teljes sora az adatkészletben; az Iqaluit és a Narvik sora hiányos, és az
  Iqaluit 63,8° É a sarkkörön innen van)*. Az előrejelzés pontossága évtizedenként kb. egy nappal
  javul: a mai ötnapos kb. olyan jó, mint 1980 körül az egynapos *(ellenőrizendő: Bauer, Thorpe,
  Brunet 2015, Nature 525, 47–55)*. Napfénytartam Magyarországon évente kb. 1900–2100 óra
  *(ellenőrizendő: HungaroMet)*. A piktogramok jelentése a HungaroMet jelölései szerint *(saját
  rajz, nem másolat; a jelentést a `.md` adja)*.
- **Átfedés:** a felhőképződés (foldrajz-9-10/04), a légkörzés (05) és a valódi éghajlati
  övezetesség (09: Narvik, Arica) nem jön ide. A három övezet itt szándékosan a tankönyvi
  (csillagászati) beosztás. A panel egy mondatban kimondja: „a valóságban a tengerek, a szelek és a
  hegyek is alakítják” (hivatkozás a 9. osztályra).
- **Építőkocka:** TtMuszer (`03-meres` – hőmérő, csapadékmérő, szélzászló), FoldClimate
  (`foldrajz-9-10/09`), TortGlobe (`foldrajz-9-10/01`, v1.1), TortMap (`foldrajz-9-10/13`, v1.1),
  TortCards (`tortenelem-5-6/07` – a piktogramok húzásához). Spec: `"sources": true`.
- **Biztonság:** zivatar-piktogramnál egy mondat a 04-es lecke villámszabályából.

---

## 4. Közös modulok és gyártási sorrend

### 4.1 Mi jön változatlanul (bájtra azonosan, szerződés 16.)

Minden modul ma már egységes: a blokkok a leckék között bájtra azonosak (md5-tel ellenőrizve,
2026-11-24). Az „ajánlott forrás” csak egy példa; bármelyik átvevőből másolható.

| Modul | Ajánlott forrás (blokk) | Lecke ebben a sorozatban | Mire kell itt |
|---|---|---|---|
| **Reszecske** v1.1 | `kemia-7-8/01-reszecskemodell` | 01, 02 | párolgás, forrás, hőtágulás a nagyítóban |
| **KemLab** v1.1 | `kemia-7-8/01-reszecskemodell` | 01, 02, 03 | `lens` (nagyító), `beaker`, `cylinder`, `thermo` |
| **KemGHS** | `kemia-7-8/10-sav-bazis` | 02, 15 | GHS02/GHS05, „NE PRÓBÁLD KI” és „tanári bemutató” bélyeg |
| **BioNet** v1.1 | `biologia-7-8/04-torzsfa` | 10, 11, 12 | táplálékháló, `cascade`, `badges` |
| **BioFlow** v1.1 | `biologia-7-8/11-verkor` | 08, 13 | víz a növényben (általános gráf), oxigén útja |
| **BioBody** | `biologia-7-8/10-mozgas` | 02 (sziluett), 13 | semleges testrajz, alkatok |
| **BioZoom** | `biologia-7-8/01-sejt` | 11, 12 | talaj- és vízcsepp-nagyítás, léptékvonalzó |
| **BioPlot** | `biologia-7-8/03-szelekcio` | 03, 08, 09, 10, 11, 12, 13 | idősor, pontok, húzható pont |
| **DeepTime** (+ előtte **TortTimeline**) | `biologia-7-8/02-mely-ido` | 05 | logaritmikus időszalag |
| **TortCards** | `biologia-7-8/02-mely-ido` (a 7ab967 md5-változat, 12 leckében; a `tortenelem-5-6/18`-é eltér, ne onnan) | 01, 02, 03, 04, 06, 07, 08, 09, 14, 15, 17 | rendezés, párosítás |
| **TortMap** v1.1 | `foldrajz-9-10/13-magyarorszag` | 06, 07, 15, 16, 17 | Magyarország, Európa, folyók |
| **TortGlobe** v1.1 | `foldrajz-9-10/01-idozonak` | 04, 05, 07, 17 | földgömb, orbit, szélességi körök |
| **FoldSection** | `foldrajz-9-10/02-lemeztektonika` | 01, 06, 10, 11, 12, 15, 16 | táj-, talaj-, tó- és rétegmetszet, szelvény |
| **FoldFlow** | `foldrajz-9-10/02-lemeztektonika` | 02, 04, 16 | füstcsóva, mágneses mező (statikus `t`), vízáramlás |
| **FoldChart** | `foldrajz-9-10/02-lemeztektonika` | 03, 14, 16 | napi görbe, energiafalu, vízjárás, forrássor |
| **FoldClimate** | `biologia-7-8/05-biomok` | 03, 17 | éghajlati diagram |
| **FoldChoro** v1.1 | `foldrajz-9-10/01-idozonak` | 07 | szomszéd országok kiemelése |
| **MatChart** v1.1 | `matematika-5-6/10-szazalek` | 01, 05, 11, 13, 14 | kördiagram (napirend, talaj, tányér), szalag |
| **SKY** („ÉGBOLT-MODUL”) | `fizika-7-8/15-fold-forgasa` | 05 | napállás, nappalhossz a tengelyferdeség paraméterével |
| `shared/tort/*` (proj, map-vilag, map-karpat, map-orszaghatarok) | – | 04–07, 15–17 | változatlanul |
| `shared/foldrajz/orszagok.js`, `megyek.js`, `szelveny-alfold-bukk.js` | – | 06, 07 | változatlanul |

Függőségek, amelyekre figyelni kell: a **TortGlobe** a TortMapra és a TortProjra épül. A **DeepTime**
előtt a TortTimeline blokkja is kell. A **TortSource** idővonal nélkül csonkot kér
(`EJSZAKAI-GYARTAS.md`, 2. tanulság) – ebben a sorozatban nem használjuk. A „Honnan tudjuk?” helyett
itt a „Tippelj! → kísérlet” minta jön, nincs szükség forráskártyára. A **SKY** blokk jelölője
(`ÉGBOLT-MODUL` … `ÉGBOLT-MODUL VÉGE`) nem szabványos. Változtatás nélkül, a két jelölővel együtt
kell másolni. A szárazföld-maszkot (`fold-szarazfold.js`) nem kell betölteni, a gömböt a TortGlobe
rajzolja.

### 4.2 Új modulok (csak kettő)

A szerződés 16. fejezete szerint: a referencialeckében, külön MODUL-blokkban, `Tt…` névtérrel
(Természettudomány). Blokkhatár: `/* ── MODUL: <név> (<Névtér>) · forrás: termeszettudomany-5-6/NN-slug,
<dátum> ── */` és `/* ── MODUL VÉGE: <név> ── */` – egységesen, a 2. tanulság szerint. Később
(egyeztetve) a `shared/tt/` alá kerülhetnek.

#### TtIkon – hazai élőlények és tájelemek rajzai · referencia: `10-erdo`

**Miért kell?** A 08, 09, 10, 11, 12 és 14-es lecke mind hazai fajokat rajzol, összesen kb. 60 félét,
és sokat közülük több leckében is. Ma két lecke-saját `IC` készlet létezik (`biologia-7-8/06`, `05`),
eltérő hívással és stílussal. Egységes készlet nélkül minden lecke újrarajzolná a tölgyet és a
cinegét. Ez a legnagyobb ismétlődő munka a sorozatban (az `iskola` tanulsága: „mind nulláról írták a
saját rajzolókódjukat”).

```text
TtIkon.draw(c, id, x, y, s, o)  – rajzol egy ikont. (x, y): a TALPPONT közepe (fa: a törzs töve, madár: a
                                   láb, hal: a test közepe – id-nként a META adja); s: a magasság px-ben
   o = {a: 1 (alfa – a c.globalAlpha-t SZOROZZA), flip: false (tükrözés), t: 0 (mozgásfázis mp-ben:
        szárnycsapás, farokcsapás, fűszál hajladozása – zárt képlet), pose: 'alap' | 'repül' | 'úszik' |
        'ül', season: 0..1 (fáknál: 0 lombtalan, 1 teljes lomb; lágyszárúnál: 0 föld alatt, 1 virágzik),
        stage: 'mag' | 'csíra' | 'fiatal' | 'virágzó' | 'termős' (a 'bab', 'paradicsom', 'búza' kulcsnál),
        pale: 0..1 (sápadt, fény nélkül nevelt – 08), dim: false (halvány tinta), hl: null | szín (kiemelő
        gyűrű, nem kitöltés), outline: '#1c2440' (a sötét körvonal, alap tinta)}
TtIkon.box(id, s) → {w, h, ax, ay}   befoglaló doboz és talppont (feliratozáshoz, ütközéshez)
TtIkon.has(id) · TtIkon.IDS · TtIkon.META[id] → {group, foot: 'talp' | 'közép', size: 'kicsi' | …}
TtIkon.GROUPS  {fa, cserje, lágyszárú, vízinövény, gomba, egysejtű, rovar, egyéb gerinctelen, hal,
                kétéltű, hüllő, madár, emlős, táj}
TtIkon.node(id, k?) → (c, x, y, s, n) => …   adapter a BioNet `icon` mezőjéhez (az s ott szélesség)
TtIkon.scatter(c, ids, rect, o) → [{id, x, y, s}]   seedelt elszórás egy területen (rét, nádas, avar);
                                   o = {seed, n, sMin, sMax, ground(x) → y (terepvonal, pl. FoldSection-ből)}
```

Kulcsok (a lecke `.md`-je adja a nevüket, a modul csak rajzol): *fák, cserjék*: kocsánytalan tölgy,
bükk, gyertyán, erdeifenyő, lucfenyő, fehér fűz, fekete nyár, mézgás éger, mogyoró, kökény,
galagonya · *lágyszárúak*: fű, réti here, pipacs, búzavirág, búza, kukorica, bab, paradicsom,
hóvirág, odvas keltike, moha, páfrány, zsurló · *vízinövények*: nád, gyékény, sás, tündérrózsa,
békalencse, átokhínár, zöldmoszat · *gomba*: kalapos gomba, taplógomba · *egysejtű, apró*:
papucsállatka, vízibolha, baktérium (pötty) · *rovarok és más gerinctelenek*: gyapjaslepke-hernyó,
lepke, szarvasbogár, katicabogár, levéltetű, sáska, házi méh, szitakötő és lárvája, szúnyoglárva,
földigiliszta, éti csiga, keresztes pók · *gerincesek*: ponty, keszeg, csuka, kecskebéka, fürge gyík,
szürke gém, tőkés réce, kárókatona, nádirigó, széncinege, nagy fakopáncs, szajkó, héja, egerészölyv,
kerecsensólyom, túzok, fürj, mókus, vaddisznó, őz, gímszarvas, róka, mezei nyúl, ürge, mezei pocok,
erdei egér, vakond, sün · *táj*: nap, felhő, esőcsepp, kő, avar, korhadó tönk.

Stílus: lapos, természetes, de nem harsány kitöltés, a körvonal mindig a sötét változat (2,5–3 px
s = 100-nál), felismerhető sziluett. Nincs mosolygó arc, ruha vagy rajzfilmszem (7. fejezet). Az
arányok nem méretarányosak – ahol ez számít, a lecke „nem méretarányos” bélyeget tesz ki. A modul
szöveget nem ír. Minden rajzfüggvény maga állítja a vászonállapotot (`resetCtx`-barát), és a
`globalAlpha`-t szorozza (a 6. tanulság szerint).

#### TtMuszer – mérőeszközök és iránytű · referencia: `03-meres`

**Miért kell?** A 03, 04, 06 és 17-es lecke mérőeszközöket rajzol. A KemLab üvegeszközeit
(`cylinder`, `thermo`) használjuk, de a vonalzó, a mérleg, a stopper, az iránytű, a csapadékmérő és
a szélzászló hiányzik. Ezeknek egységes, *leolvasható* skála kell (≥ 22 px számok, nagyító a
leolvasáshoz). Az iránytű három leckében is szerepel.

```text
Minden függvény a lecke L-jét kapja; szöveget csak L.tx / L.pill útján ír, a feliratokat a hívó adja
{s, k} alakban (T objektum a .md-ből). o.a: alfa (szorzó). A rajz és a kiírt érték ugyanabból a
skálaobjektumból jön (szerződés 9.).

TtMuszer.ruler(L, x, y, len, o) → {X(v), inv(px), ppu}      vonalzó / mérőszalag
   o = {from: 0, to: 30, unit: {s: 'cm', k}, minor: 10 (osztás egységenként), major: 1, labelEvery: 1,
        tape: false (hajlékony szalag), vertical: false, a}
TtMuszer.thermo(L, x, yb, h, o) → {yOf(T), top}             leolvasható hőmérő (folyadékszál, °C-skála)
   o = {T, lo: −20, hi: 50, step: 1, major: 10, shade: false (árnyékoló doboz – műszerkert), a}
TtMuszer.balance(L, cx, by, w, o) → {plateL, plateR}        konyhai mérleg (o.mode 'digit': kijelző m-mel)
   vagy kétkarú mérleg ('karos': o.tilt a két oldal tömegéből, zárt képlettel)
TtMuszer.stopwatch(L, cx, cy, R, o)                         stopper (o.t mp, o.run, digitális + mutatós)
TtMuszer.compass(L, cx, cy, R, o) → {tip: [x, y]}           iránytű
   o = {needle: fok (a tű iránya, 0 = a vászon teteje, óramutató szerint), rose: 'fő' | 'mellék' | false,
        T: {É, ÉK, K, DK, D, DNy, Ny, ÉNy} (mind {s, k}), body: fok (a doboz elforgatása), decl: fok
        (elhajlás jelzése vékony vonallal), wobble: {t0, amp} (beálló lengés zárt képlettel), a}
TtMuszer.needleIn(field, x, y) → fok                       a tű iránya egy [u, v] mezőből (pl. a 04 dipólmezeje)
TtMuszer.rainGauge(L, x, yb, h, o)                          csapadékmérő (o.mm, o.max, skála mm-ben)
TtMuszer.vane(L, cx, by, o)                                 szélzászló + kanalas szélmérő (o.dir, o.v, o.t)
TtMuszer.lens(L, from, to, o)                               leolvasó nagyító a skálán – a KemLab.lens
   mintájára, de kör alakú, kis kúppal; ha a KemLab is be van töltve, ugyanazt a stílust adja
TtMuszer.parallax(L, scale, eyeY, o) → {read, err}          a szem magasságától függő leolvasás (03)
```

**Nem kell új modul** (lecke-saját marad, nem általánosítjuk): a kitalált település és a
szintvonal-szeletelés (06), a GPS-körök és a narancshéj (07), a növény-növekedési modell (08), a
giliszta-, csiga- és halmozgás (09), az erdei fény modellje (10), a szukcesszió és az erózió (11),
az eutrofizáció (12), a futás élettani modellje (13), az energiafalu (14), a redő- és
vetőgeometria (15), a homokasztal (16), a piktogramok (17). A „Tippelj!” minta sem modul: 2–4
`L.button` és a lecke saját változója (7. fejezet).

### 4.3 Új adat (egy fájl) – D1: a Kárpát-medence domborzata

`shared/foldrajz/domborzat-karpat.js` (`FOLD_DOMBORZAT`) a `tools/build_geodata.py` meglévő `etopo`
forrásából (NOAA ETOPO 2022, ERDDAP, közkincs). Új letöltési forrás nem kell, csak egy rácslekérés
lépésközzel (stride):

| rács | kivágat | felbontás | értékek | méret (becslés) |
|---|---|---|---|---|
| belső | 16,0–23,1° K, 45,7–48,6° É (Magyarország) | 1′ | 426 × 174 ≈ 74 ezer | ~150 KB |
| külső | 13–28° K, 43,5–50,5° É (Kárpát-medence) | 3′ | 300 × 140 = 42 ezer | ~90 KB |

Formátum: a `shared/foldrajz/README.md` szerint `{id, ver, src, lic, url, asOf, generated, …}`, rács:
`{lon0, lat0, step, w, h, z: [soronként delta-kódolt egész méter]}`. A lecke bilineáris
interpolációval színez (magassági színfokozat a 06-os `.md` határai szerint) és árnyékol.
Felhasználók: 06 (domborzati térkép), 07 (Magyarország helye a Kárpát-medencében), 16 (vízgyűjtő,
lejtés). Ezt a koordinátor (vagy egy G-feladat) generálja a 4. köteg előtt. Ha nem készül el, a
leckék a 06-os és a 16-os briefben leírt tartalékkal készülnek.

### 4.4 Referencialeckék – az első kör

| Lecke | Mit épít / próbál ki | Miért ez |
|---|---|---|
| **03-meres** | **TtMuszer** (minden eszköz, az iránytűvel együtt); a reakcióidő-mérés `pointer.events[].ts`-sel; FoldClimate és BioPlot együtt | a modul a 04, 06, 17 alapja; a lecke tartalmilag egyszerű és jól ellenőrizhető (valódi WMO-adat, kitalált nap) |
| **10-erdo** | **TtIkon** (a teljes kulcslista, nem csak az erdei fajok – a 08, 09, 11, 12 ezt örökli); BioNet + FoldSection együtt | ez a lecke használja a legtöbb fajt és a legtöbb ikonfunkciót (`season`, `scatter`, `node`) |
| **01-tocsa** | új modul nélkül: a kémiai (Reszecske, KemLab) és a földrajzi (FoldSection) modulok első közös használata; a sorozat stílusa: a „Tippelj!” minta, a kísérlet-bélyegek, a 45 szavas panel | ha itt a kész modulok bájtra azonosan működnek, a többi lecke is mehet; ez lesz a minta a 10–12 éves nyelvhez |

Az első kör után a koordinátor átnézi a két új modult (API, 22 px, `globalAlpha`), és csak utána
indul a 2. köteg. A TtIkon kulcslistája az első körben teljes legyen, hogy a 2–3. kötegben ne kelljen
bővíteni (párhuzamos változat-veszély).

### 4.5 Gyártási sorrend (legfeljebb 3 párhuzamos lecke kötegenként)

A párhuzamos magyar sorozattal együtt egyszerre legfeljebb 5 al-ügynök fut. Ebből ez a sorozat
legfeljebb 3 helyet foglal. Minden al-ügynök saját, egyedi scratchpad-almappát kap (8. tanulság).

| Köteg | Leckék (nehézség) | Új modul | Újrahasznosított |
|---|---|---|---|
| 1 | **03-meres** (3), **10-erdo** (3), **01-tocsa** (2) | TtMuszer (03) · TtIkon (10) | KemLab, Reszecske, FoldSection, FoldClimate, FoldChart, BioPlot, BioNet, MatChart, TortCards |
| 2 | **02-tuz** (2), **04-magnes** (2), **08-noveny** (2) | – | TtMuszer, TtIkon, KemLab, Reszecske, KemGHS, FoldFlow, TortGlobe, BioFlow, BioBody |
| 3 | **11-ret-szanto** (2), **12-to** (2), **05-ido** (3) | – | TtIkon, BioNet, BioZoom, FoldSection, SKY, TortGlobe, DeepTime, MatChart |
| 4 | **06-terkep** (3), **07-foldgomb** (2), **09-allat** (2) | – (D1 adat előtte) | TtMuszer, TtIkon, TortMap, FoldChoro, FoldSection, TortCards |
| 5 | **15-hegyek** (2), **16-folyo** (3), **17-idojaras** (2) | – | FoldSection, FoldFlow, FoldChart, FoldClimate, TortMap, TortGlobe, TtMuszer |
| 6 | **13-emberi-test** (3), **14-energia** (2) | – | BioBody, BioFlow, BioPlot, MatChart, FoldChart, TtIkon |

Indoklás: a **02-tuz** a 2. kötegben van, mert biztonsági lektorálást kér (`"review": ["tűzvédelem"]`).
Korán kell a visszajelzés, mielőtt a többi „biztonsági mondatos” lecke (04, 15) véglegesedik. A 05 a
3. kötegben van, mert a 07 (nevezetes szélességi körök) és a 17 (övezetek) a tengelyferdeség
konstansát és a zseblámpafolt rajzát tőle veszi át. A 06 és a 16 a D1-re vár, ezért késői. A
**13-emberi-test** az utolsó: egészségügyi lektorálást kér, és a biológia-sorozat egészség-szabályait
alkalmazza; addigra a 17-ujraelesztes visszajelzése is megvan. Becsült költség az
`EJSZAKAI-GYARTAS.md` alapján: 17 lecke × ~0,45 % ≈ **7–8 % heti keret**, kb. 17 × 36 perc ≈ 10 óra
al-ügynök-idő, 3 párhuzamos szálon kb. 4 óra falióra (a D1 és a review nélkül).

---

## 5. Build- és szerződés-kiegészítési igények

### 5.1 A helyzet (ellenőrizve, `tools/build_lesson.py` fejléce, 2026-11-24)

Minden, amire a sorozatnak szüksége van, **már megvan**:

| Igény | Megoldás a meglévő buildben |
|---|---|
| 45 szavas panel | spec `"maxWords": 45` |
| hossz, tömeg, térfogat, idő különböző egységekben (03, 05) | `"dim": "hosszúság" \| "tömeg" \| "térfogat" \| "idő"` („1 milliárd s”, „31,7 év”, „11,6 nap”) |
| tartomány („0,2–0,3 s”, „70–100/perc”, „2–5 %”) | `range` (+ `dim`) |
| mély idő (05: 4,54 milliárd év, 66 millió éve) | `ago` |
| méretarány (06: 1 : 10 000) | `ratio` (a kettőspont körül nem törő szóköz) |
| havi sorozat (03, 17: 12 érték) | `list` `"len": 12` |
| koordináta (07: Budapest) | `coord` + `"box"` |
| becslés, modell, frissítendő jelölés | a `TAG_WORDS` („becslés”, „modell”, „frissítendő”) → `est`, `model`, `upd` |
| forrás minden adathoz (03, 13, 14, 17) | spec `"sources": true` |
| lektorálás jelzése (02, 13) | spec `"review": ["tűzvédelem"]` / `["egészség"]` → a build kéri a `<!-- Szakmai ellenőrzés: … -->` blokkot |
| nagy adat hivatkozása (06, 16: D1) | `dataset` (`{"id": "domborzat-karpat"}`) |

**Új adattípus, build- vagy QA-funkció nem kell.** Az egyetlen új dolog a **D1** adatfájl (4.3), ami
a `tools/build_geodata.py` bővítése egy rácslekéréssel. A koordinátor feladata, a leckeügynökök a
`tools/`-hoz nem nyúlnak.

### 5.2 Kis, nem blokkoló javaslatok (a koordinátornak, ha a magyar sorozattal együtt érdemes)

1. **QA-állapot a „Tippelj!” mintához** – nincs új funkció, csak konvenció: minden tippes lépés
   `__qaStates`-ében legyen `tipp-jó` és `tipp-rossz` állapot (a választás után fotózva). A 7.
   fejezet ezt rögzíti.
2. **Kulcs-névtér:** a Feliratok és az Adatok kulcsai közös névtérben vannak (3. tanulság). A 7.
   fejezet névadási szabálya ezt megelőzi. Build-változás nem kell.
3. A `TtIkon` és a `TtMuszer` az első kör után a `shared/tt/` alá kerülhet (egyeztetve), mint a
   többi tantárgyi modul később.

### 5.3 A szerződés kiegészítése

A 7. fejezet kész szövege a `SZERZODES.md` új fejezeteként illeszthető be. Javasolt sorszám: 17. –
ha a párhuzamos „Magyar nyelv és irodalom” kiegészítés is 17-et kér, a koordinátor sorszámoz át
(a 16. „Közös modulok” fejezet maradhat a végén is, vagy elé kerülhetnek a tantárgyi fejezetek).

---

## 6. Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / fejlesztési feladat |
|---|---|---|
| 1. Anyagok és tulajdonságaik (12) | 01, 02, 11 (talaj), 08 (lágy és fás szár) | **„Természetes és mesterséges anyagok tulajdonságai, felhasználhatósága, környezetre gyakorolt hatásai”** (pl. a műanyag lebomlása) – csak a 11 komposzt-lépése érinti; **„Hely- és helyzetváltoztatás”** csak a 09 megjegyzésében; a talajféleségek összehasonlítása (homok, agyag, vályog) csak röviden a 11-ben |
| 2. Mérések, mértékegységek, mérőeszközök (7) | 03, (17: műszerkert) | **éghajlati térképek** leolvasása (a 03 diagramot, a 17 gömböt mutat; hazai éghajlati térképhez rácsadat kellene – tartalék) |
| 3. Megfigyelés, kísérletezés, tapasztalás (8) | 04, (08: életfeltételek, 01: csapadék, 14: energia) | a széntüzelés légszennyező hatásának tanári kísérlete (14 csak hivatkozik a kemia-7-8/11-re); szélkerék és vízimalom építése (kézműves) |
| 4. Tájékozódás az időben (6) | 05 | a Hold mozgása (fizika-7-8/16 – hivatkozás); helyi idő és zónaidő (foldrajz-9-10/01 – hivatkozás); a hetirend külön nem |
| 5. Alapvető térképészeti ismeretek (7) | 06, (04: iránytű) | iránytű készítése, tájékozódás iránytű nélkül (terep); **Magyarország nagytájainak bemutatása** csak a 06 utolsó lépésében, a D1-gyel |
| 6. Topográfiai alapismeretek (7) | 07, 16 (vizek) | „földrajzi legek” gyűjtése (a 03 és a 07 néhány adata); a nagy földrajzi felfedezések (tortenelem-5-6/13) |
| 7. Gyakorlati térképészet (7) | 06 (virtuális terepmunka), 07 (GPS) | valódi terepi tájékozódás, vetélkedő; **„térinformatikai alkalmazás” használata** csak elvben (a GPS működése), egy valódi app nem |
| 8. A növények testfelépítése (10) | 08, (11: biológiai védekezés) | növényhatározás, kerti kalendárium, vetésforgó részletesen, madárodú; a híres magyar zöldség- és gyümölcsfajták |
| 9. Az állatok testfelépítése (10) | 09, (12: egysejtűek) | állati eredetű anyagok vizsgálata; háziállat választása, gondozása; a gerinces osztályok összevetése (biologia-7-8/04) |
| 10. Az erdők életközössége (11) | 10 | a gombák részletesen (csak lebontóként); erdei madarak hangja; **„A környezetszennyezés és élőhelypusztulás következményei”** csak az erdőgazdálkodás-lépésben |
| 11. A mezők és a szántóföldek életközössége (9) | 11 | gyógynövények; gabonamagvak anyagainak kimutatása; a fűfélék testfelépítése |
| 12. Vízi és vízparti életközösségek (10) | 12 | szennyvíztisztító telep (kemia-7-8/12); papucsállatka-tenyészet; vízparti fák összehasonlítása; a költöző madarak (csak egy mondat) |
| 13. Az emberi szervezet, testi-lelki egészség (10) | 13 | **az életszakaszok jellemzői** (csak a kamaszkor); **adatok elemzése korcsoportok egészségi állapotáról**; **elhízás és kóros soványság** – szándékosan nem vizualizálva (testkép, 7. fejezet), csak egy semleges mondat; szenvedélybetegség és dohányzás; bőr- és szájápolás, tartásjavítás; elsősegély (biologia-7-8/17); járvány (biologia-7-8/16) |
| 14. Az energia (6) | 14 | egykori bányaterület felkeresése (Gánti Geológiai Tanösvény – terep) |
| 15. A Föld külső és belső erői (10) | 15, 16, (11: talaj, 01: fagyaprózódás) | „minicseppkő”, a magmaáramlás festett vízzel (csak megjegyzés a 15-ben); a szél felszínformáló munkája |
| 16. Alapvető légköri jelenségek (6) | 17, (05: évszakok) | időjárási mérőállomás építése (a 17 műszerkertje előkészít); állatok viselkedése időjárás-változás előtt |

**A forrásszöveg kinyerési hibái** (a `kerettanterv/termeszettudomany/5-6.md`-ben, javítás nélkül): az
1. témakör javasolt tevékenységei között „elvégezése” áll („Egyszerű kísérletek elvégezése a talaj
tulajdonságainak…”) – valószínűleg a forrás elírása. A 15. témakörben a tanulási eredmény
„munkavégző képessége” (különírva), a fejlesztési feladat és a fogalomlista „munkavégző-képesség”
(kötőjellel) – a forrás következetlensége, az idézetek így hagyják. A 7. témakör címe zárójeles
alcímmel hosszú („Gyakorlati jellegű térképészeti ismeretek (Az iskola környékének megismerése
során, terepi munkában)”). A leckék metaadat-sorában ez rövidíthető-e, azt a koordinátor dönti el; a
javaslat: teljes cím, mert a build nem korlátozza. A témakörök áttekintő táblázata kétszer szerepel
a fájlban (a konverzió és a forrás táblázata) – a tartalmat nem érinti. Az óraszámok összege 136,
egyezik a forrással.

**Tartalék-jelöltek**, ha a sorozat folytatódik (fontossági sorrendben):

1. `anyagok-sorsa` – természetes és mesterséges anyagok: mi bomlik le és mennyi idő alatt (1.;
   TtIkon, FoldChart). Óvatos számokkal, mert a lebomlási idők forrásonként nagyon eltérnek.
2. `eghajlati-terkep` – Magyarország éghajlati térképe (évi középhőmérséklet, csapadék) – rácsadat
   kellene (HungaroMet, licenc ellenőrizendő) (2.).
3. `hold-es-ido` – a Hold járása és a hónap, a 05 folytatásaként (4.; SKY, a fizika-7-8/16 HOLD-
   modulja).
4. `koltozo-madarak` – a gólya útja a gömbön (12., 10.; TortGlobe `route`).
5. `nagytajak` – Magyarország hat nagytája a D1-en (5., 6.).
6. `egeszseg-adatok` – korcsoportok egészségi adatai, grafikonolvasás (13.) – csak lektorral.

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): az NKP *Természettudomány 5.* és *6.*
digitális tankönyve; PhET *States of Matter: Basics*, *Balloons and Static Electricity*, *Magnet and
Compass*, *Energy Forms and Changes* (részben magyarul); a HungaroMet és a vízügy nyilvános
oktatóoldalai.

---

## 7. Javasolt szerződés-kiegészítés (kész szöveg a `leckek/SZERZODES.md`-hez)

A következő fejezet változtatás nélkül beilleszthető a `SZERZODES.md`-be (a sorszámot lásd 5.3).

```markdown
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
```
