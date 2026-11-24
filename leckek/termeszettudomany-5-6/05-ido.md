# Mitől van nap, év és évszak? – a Föld mozgásai és az idő skálái
tantárgy: Természettudomány · évfolyam: 5–6. · témakör: 4. Tájékozódás az időben

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/termeszettudomany-5-6/05-ido.md

  A „Tippelj!” lépésekben (5., 7.) a panel első bekezdése a kérdés; a többi bekezdés
  elmosódva látszik, és csak a tipp után válik olvashatóvá (a megoldás addig rejtve marad).
  A ## Közös feliratai: a „Tippelj! → kísérlet → magyarázat” sáv, a tipp-visszajelzés és a
  kísérlet-bélyegek (szerződés 17.) – a sorozat minden leckéjében ugyanígy szerepelnek.
  A tengelyferdeség, Budapest szélessége és a Nap–Föld távolság az animációt is vezérli
  (a napállás, a nappal hossza, a pálya alakja ezekből számolódik).
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kísérlet
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- otthon bélyeg: otthon is kipróbálhatod
- modell bélyeg: modell
- kitalált bélyeg: kitalált példa
- nem méretarányos bélyeg: nem méretarányos
- Nap felirat: Nap
- Budapest felirat: Budapest
- Sydney felirat: Sydney
- nappal felirat: nappal
- éjjel felirat: éjjel
- északi felirat: É
- hónapok felirat: január; február; március; április; május; június; július; augusztus; szeptember; október; november; december
- évszakok felirat: tavasz; nyár; ősz; tél
- óra perc felirat: # óra # perc
- napba felirat: Soha ne nézz a Napba – napszemüveggel, távcsővel, telefonnal sem!

### Adatok
- tengelyferdeség: 23,44°
<!-- forrás: IAU/IERS – a Föld tengelyferdesége 2026-ban 23,436°; ugyanez: fizika-7-8/15-fold-forgasa -->
- Budapest szélessége: 47,5°
<!-- forrás: Budapest földrajzi koordinátái (kb. 47,50° É, 19,04° K); ugyanez: fizika-7-8/15-fold-forgasa -->
- Budapest hosszúsága: 19,04°
<!-- forrás: mint fent (Budapest, kb. 19,04° K) -->
- Sydney szélessége: −33,87°
<!-- forrás: Sydney földrajzi koordinátái (kb. 33,87° D, 151,21° K); a déli szélesség itt negatív szám -->
- napközelpont: 147,1 millió km
<!-- forrás: NASA, Earth Fact Sheet (perihelion 147,1 millió km); ugyanez: fizika-7-8/15-fold-forgasa.
     2026-ban: január 3. (kb. 17:15 UTC) – US Naval Observatory, lekérdezve: 2026-11-24 -->
- naptávolpont: 152,1 millió km
<!-- forrás: NASA, Earth Fact Sheet (aphelion 152,1 millió km); 2026-ban: július 6. (kb. 17:30 UTC) – US Naval Observatory,
     lekérdezve: 2026-11-24. Évről évre július 3–6. közé esik, ezért a lecke „július eleje” feliratot használ. -->
- napkelte magassága: −0,83°
<!-- forrás: csillagászati évkönyvek szokásos értéke – napkeltekor a Nap KÖZEPE 0,83°-kal a látóhatár alatt van
     (a napkorong sugara kb. 0,27° + a légköri fénytörés kb. 0,57°). Ezzel a nappal kb. 12 perccel hosszabb a mértani értéknél. -->

## 1. Egy nap: egyszer megfordul a Föld
A Föld forog a saját **tengelye** körül. Egy fordulat kb. 24 óra: ez egy **nap**. Mindig csak az egyik fele néz a Nap felé: ott **nappal** van, a másikon **éjjel**. ==Budapest {forgási sebesség Budapesten} sebességgel forog körbe!== Húzd a csúszkát!

### Feliratok
- forgás csúszka: Az idő Budapesten
- forgás gomb: Forogjon magától
- most felirat: Budapesten most: #
- tavaszi nap felirat: március 20-án
- sebesség felirat: Budapest sebessége: #
- repülő felirat: gyorsabb, mint egy utasszállító repülő (#)
- útja felirat: Budapest útja egy nap alatt
- egyenlítő felirat: Egyenlítő
- napfény felirat: napfény

### Adatok
- Föld egyenlítői sugara: 6378 km
<!-- forrás: NASA, Earth Fact Sheet (egyenlítői sugár 6378,1 km), lekérdezve: 2026-11-24 -->
- egy fordulat a csillagokhoz képest: 23,934 óra
<!-- forrás: csillagnap = 23 óra 56 perc 4 mp (NASA, Earth Fact Sheet: sidereal rotation period 23,9345 h) -->
- forgási sebesség Budapesten: kb. 1130 km/h
<!-- forrás: a lecke számolja és ellenőrzi: 2 · π · 6378 km / 23,934 óra = 1674 km/h az Egyenlítőn,
     ennek cos 47,5° = 0,676-szorosa Budapesten = 1131 km/h -->
- repülő sebessége: kb. 900 km/h
<!-- forrás: becslés – nagy utasszállító repülőgépek utazósebessége kb. 830–950 km/h (típustól függ; pl. Airbus A320 kb. 830 km/h,
     Boeing 777 kb. 900 km/h; gyártói adatlapok), lekérdezve: 2026-11-24 -->

## 2. Merre kel a Nap?
A Föld **nyugatról keletre** forog. Ezért a Nap keleten kel, nyugaton nyugszik. ==Nem a Nap kering körülöttünk: mi fordulunk felé.== Pontosan keleten csak tavasszal és ősszel kel. Nyáron északkeleten, télen délkeleten.

> megjegyzés: Figyeld meg egy héten át, hol kel a Nap a házak fölött!

### Feliratok
- felülről felirat: a Föld felülről, az Északi-sark fölül
- forgásirány felirat: nyugatról keletre forog
- napkelte itt felirat: itt kel fel a Nap
- napnyugta itt felirat: itt nyugszik le
- kelet felirat: kelet: a Nap felé
- látóhatár cím felirat: Budapest, kelet felé nézve
- égtájak felirat: É; ÉK; K; DK; D
- június kel felirat: június 21.
- március kel felirat: március 20., szeptember 23.
- december kel felirat: december 21.
- kering tévhit felirat: A Nap kering a Föld körül?
- kering válasz felirat: Nem: a Föld forog, mi fordulunk a Nap felé

## 3. Egy év: egy kör a Nap körül
A Föld a Nap körül is kering. Egy kör kb. 365 és negyed nap: ez egy **év**. A negyed napokból négyévente lesz egy plusz nap, február 29.: ez a **szökőév**. ==Amikor nálunk nyár van, Ausztráliában tél.== Húzd a dátumot!

> megjegyzés: Zseblámpával és naranccsal otthon is kipróbálhatod.

### Feliratok
- dátum csúszka: Dátum
- lámpa felirat: lámpa = Nap
- földgömb felirat: földgömb = Föld
- pálya felirat: a Föld útja egy év alatt
- évszak Budapest felirat: Budapest: #, nappal #
- évszak Sydney felirat: Sydney (Ausztrália): #, nappal #
- napfordulók felirat: márc. 20.; jún. 21.; szept. 23.; dec. 21.
- évszak tévhit felirat: Az egész Földön egyszerre van nyár?
- évszak válasz felirat: Nem: amikor nálunk nyár van, Ausztráliában tél
- szökőév felirat: 4 × negyed nap = 1 nap: február 29.
- pályasebesség felirat: a Föld száguld: #, Budapestről Debrecenig # alatt
- ugyanarra felirat: a tengely mindig ugyanarra dől

### Adatok
- év hossza: 365,2422 nap
<!-- forrás: a tropikus év hossza (IAU; kb. 365 nap 5 óra 49 perc). A Gergely-naptár: 4 évente szökőév, a 100-zal osztható évek
     közül csak a 400-zal oszthatók (2000 szökőév volt, 2100 nem lesz) – ezt a lecke csak a megjegyzésben említi -->
- Föld pályasebessége: kb. 30 km/s
<!-- forrás: NASA, Earth Fact Sheet (átlagos pályasebesség 29,78 km/s), lekérdezve: 2026-11-24 -->
- Budapest–Debrecen távolsága: kb. 195 km
<!-- forrás: a két városközpont légvonalbeli távolsága (47,50° É, 19,04° K – 47,53° É, 21,63° K) kb. 194 km; a lecke számolja:
     195 km / 30 km/s = 6,5 s -->

## 4. A ferde tengely – mi lenne, ha nem dőlne?
A Föld tengelye {tengelyferdeség}-ot dől, mindig ugyanarra. Júniusban az északi félteke a Nap felé hajlik: ==magasabban jár a Nap, és tovább van fent.== A meredek napfény kis foltra jut, jobban melegít. Húzd a csúszkát: mi lenne, ha nem dőlne?

### Feliratok
- dőlés csúszka: A tengely dőlése
- június oszlop felirat: június 21.
- december oszlop felirat: december 21.
- delelés felirat: délben: #
- nappal hossz felirat: nappal: #
- le sem nyugszik felirat: a Nap le sem nyugszik
- fel sem kel felirat: a Nap fel sem kel
- folt felirat: a folt: #
- folt felülről felirat: felülről
- folt arány felirat: decemberben ugyanaz a fény #-szer akkora foltra jut
- egyforma felirat: nincs évszak: egész évben egyforma a nappal
- zseblámpa felirat: zseblámpa = a déli Nap
- nappali ív felirat: Budapest nappali útja
- dél tévhit felirat: Délben a Nap pont fölöttünk áll?
- dél válasz felirat: Budapesten soha: legfeljebb kb. #

### Adatok
- déli napmagasság júniusban: kb. 66°
<!-- forrás: a lecke számolja és ellenőrzi: 90° − 47,5° + 23,44° = 65,94° (június 21.); decemberben 90° − 47,5° − 23,44° = 19,06°,
     napéjegyenlőségkor 42,5° (a fénytörés nélkül) -->
- déli napmagasság decemberben: kb. 19°
<!-- forrás: mint fent -->
- nappal hossza júniusban: kb. 16 óra
<!-- forrás: a lecke számolja és ellenőrzi (cos H = (sin h₀ − sin φ · sin δ) / (cos φ · cos δ), h₀ = −0,83°): 15 óra 58 perc;
     a mértani érték (h₀ = 0) 15 óra 46 perc. Budapest, június 21.: napkelte 4:46, napnyugta 20:44 (nyári időszámítás;
     a lecke a 6. lépésben 4:47 / 20:45-öt számol, az időegyenlet közelítése miatt ±1 perc) -->
- nappal hossza decemberben: kb. 8,4 óra
<!-- forrás: mint fent: 8 óra 26 perc (mértanilag 8 óra 13 perc). Budapest, december 21.: napkelte 7:29, napnyugta 15:55 -->
- nyaláb szélessége: 10 cm
<!-- forrás: kitalált példa – egy 10 cm széles fénynyaláb (zseblámpa); a folt hossza = 10 cm / sin(napmagasság), a lecke számolja -->

## 5. Tévhit: nyáron közelebb vagyunk?
Sokan azt hiszik: nyáron azért meleg van, mert közelebb vagyunk a Naphoz. ==Mikor vagyunk a legközelebb? Tippelj!==

**Januárban** ({napközelpont}), júliusban a legtávolabb ({naptávolpont}). A pálya szinte kör. ==Az évszakot a ferde tengely okozza, nem a távolság.==

### Feliratok
- távolság kérdés felirat: Mikor vagyunk a legközelebb a Naphoz?
- július tipp: júliusban
- január tipp: januárban
- mindig tipp: mindig ugyanolyan messze
- napközel felirat: napközel: január eleje
- naptávol felirat: naptávol: július eleje
- távolság felirat: Nap–Föld: #
- különbség felirat: a különbség: # (kb. # %)
- kör felirat: szaggatott: egy pontos kör
- pálya méretarányos felirat: a pálya alakja méretarányos
- januári fény felirat: januárban kb. # %-kal több napfény ér minket…
- mégis tél felirat: …mégis tél van nálunk!
- Budapesten felirat: Budapesten: #
- Sydney-ben felirat: Sydney-ben: #

### Adatok
- januári napfénytöbblet: kb. 7 %
<!-- forrás: a lecke számolja és ellenőrzi: a napfény erőssége a távolság négyzetével fordítva arányos,
     (152,1 / 147,1)² = 1,069 → kb. 7 %-kal több napközelben. A távolság-különbség 5 millió km, kb. 3 %. -->

## 6. A te napod 24 órája
Egy nap 24 óra. Hogyan osztod be? Húzd a pöttyöket a kör szélén: mennyit alszol, tanulsz, mozogsz? ==Az összeg mindig 24 óra.== A külső gyűrű mutatja, mikor világos Budapesten. Decemberben ez csak kb. 8 és fél óra.

### Feliratok
- napirend cím felirat: Egy napom 24 órája
- tevékenységek felirat: alvás; reggeli, készülődés; iskola; mozgás; tanulás; játék, barátok; vacsora, család; képernyő; tisztálkodás, olvasás
- összeg felirat: összesen: #
- alvás ajánlás felirat: ajánlás 6–12 éveseknek: #
- mozgás ajánlás felirat: ajánlás: átlagosan legalább # naponta
- világos felirat: világos: # – #
- június gomb: június 21.
- december gomb: december 21.
- nyári idő felirat: nyári időszámítás
- téli idő felirat: téli időszámítás
- húzd felirat: fogd meg és húzd a pöttyöket!

### Adatok
- példa napirend: 9,5; 1; 6; 1,5; 1,5; 1,5; 1; 1; 1 óra
<!-- forrás: kitalált példa (a csúszkák kezdőállása; a sorrend a tevékenységek felirat sorrendje). Összege 24 óra – a lecke ellenőrzi. -->
- lefekvés időpontja: 21,5 óra
<!-- forrás: kitalált példa – 21,5 óra = 21:30 (este fél tíz); innen indul a napirend köre -->
- alvásigény 6–12 éveseknek: 9–12 óra
<!-- forrás: Paruthi S. és mtsai: Recommended Amount of Sleep for Pediatric Populations (American Academy of Sleep Medicine), J Clin Sleep Med 2016;12(6):785–786 – 6–12 éveseknek 9–12 óra; lekérdezve: 2026-11-24 -->
- napi mozgás: 60 perc
<!-- forrás: WHO Guidelines on Physical Activity and Sedentary Behaviour (2020) – 5–17 éveseknek naponta átlagosan legalább 60 perc közepes vagy nagy intenzitású mozgás; lekérdezve: 2026-11-24 -->
- téli időszámítás: UTC+1
<!-- forrás: közép-európai idő (CET); Magyarországon október utolsó vasárnapjától március utolsó vasárnapjáig -->
- nyári időszámítás: UTC+2
<!-- forrás: közép-európai nyári idő (CEST). A napkelte és a napnyugta időpontját a lecke számolja
     (a Nap helyzete + időegyenlet + Budapest hosszúsága), és a csillagászati évkönyvek értékeivel ellenőrzi (lásd a 4. lépést). -->

## 7. Millió vagy milliárd másodperc?
Egymillió másodperc {egymillió másodperc}. ==Mennyi idő egymilliárd másodperc? Tippelj!==

Egymilliárd másodperc **{egymilliárd másodperc}**! A milliárd ezerszer annyi, mint a millió. ==Egy 11 éves kb. {11 év másodpercben} másodperce él.==

> megjegyzés: Számold ki a saját korodat másodpercben!

### Feliratok
- milliárd kérdés felirat: Mennyi idő egymilliárd másodperc?
- hónap tipp: kb. 1 hónap
- három év tipp: kb. 3 év
- harmincegy év tipp: kb. 31 év
- háromszáz év tipp: kb. 300 év
- millió sáv felirat: 1 millió másodperc = #
- milliárd sáv felirat: 1 milliárd másodperc = #
- nap osztás felirat: # nap
- év osztás felirat: # év
- életkor felirat: 11 éves vagy: # másodperc
- nagyítás felirat: ezerszeres nagyítás
- itt van felirat: itt az 1 millió!

### Adatok
- egymillió másodperc: kb. 11,6 nap
<!-- forrás: a lecke számolja és ellenőrzi: 1 000 000 s / 86 400 s = 11,57 nap -->
- egymilliárd másodperc: kb. 31,7 év
<!-- forrás: a lecke számolja és ellenőrzi: 1 000 000 000 s / 31 557 600 s (365,25 nap) = 31,69 év -->
- példa életkor: 11 év
<!-- forrás: kitalált példa (egy ötödikes / hatodikos) -->
- 11 év másodpercben: 347 millió
<!-- forrás: a lecke számolja és ellenőrzi: 11 · 31 557 600 s = 347 133 600 s ≈ 347 millió -->

## 8. Összefoglalás: a pislogástól a Föld koráig
**Nap**: a Föld egyszer megfordul. **Év**: egyszer megkerüli a Napot. **Évszak**: a tengely ferde. A szalagon ==minden osztás tízszer annyi idő==, így elfér a pislogás és a Föld kora is. Kapcsolj egyenletes skálára!

> megjegyzés: 7. osztályban a fizikában folytatjuk: égbolt, Hold, holdfázisok.

### Feliratok
- nap össz felirat: nap = egy forgás
- év össz felirat: év = egy kör a Nap körül
- évszak össz felirat: évszak = a ferde tengely
- szalag cím felirat: Mennyi idő? Ennyi ideig tart – vagy ennyi ideje volt.
- pislogás felirat: egy pislogás
- szívverés felirat: egy szívverés
- nap esemény felirat: egy nap
- év esemény felirat: egy év
- emberélet felirat: egy emberélet
- honfoglalás felirat: a honfoglalás
- piramis felirat: Kheopsz piramisa
- jégkorszak felirat: a jégkorszak vége
- sapiens felirat: az első mai emberek
- dinó felirat: a dinoszauruszok kihalása
- Föld kora felirat: a Föld születése
- log osztások felirat: 1 milliárd év; 1 millió év; 10 ezer év; 100 év; 1 év; 1 nap; 1 óra; 1 perc; 1 s
- lin osztások felirat: 4 milliárd éve; 3 milliárd éve; 2 milliárd éve; 1 milliárd éve; ma
- log gomb: tízszeres lépések
- lin gomb: egyenletes skála
- log skála felirat: tízszeres lépések (log. skála)
- szorul felirat: minden más ide szorul, az utolsó pixelbe!
- éve felirat: éve
- milliárd felirat: milliárd
- millió felirat: millió
- ezer felirat: ezer
- ma felirat: ma

### Adatok
<!-- forrás (az alábbiakra): a kerettanterv „időszalag” tevékenységéhez; az egyes értékek forrása a sorok alatt -->
- mai év: 2026
<!-- forrás: a lecke éve – ebből számolja, hány éve volt a honfoglalás és a piramis (frissítendő, ha a lecke évet vált) -->
- pislogás ideje: 0,1–0,4 s
<!-- forrás: becslés – egy pislogás kb. 100–400 ezredmásodperc (pl. Schiffman: Sensation and Perception; UCL/Harvard ismeretterjesztő
     adatai) -->
- szívverés ideje: kb. 1 s
<!-- forrás: becslés – nyugalomban kb. 60–100 szívverés percenként (10–12 éveseknél kb. 70–110) → egy szívverés kb. 0,6–1 s -->
- egy nap: 24 óra
<!-- forrás: közismert (közepes napidő) -->
- emberélet: kb. 77 év
<!-- forrás: KSH, születéskor várható átlagos élettartam 2024: férfiak 73,6 év, nők 79,6 év → kb. 77 év (kerekítve, becslés;
     frissítendő), lekérdezve: 2026-11-24 -->
- honfoglalás: 895
<!-- forrás: ugyanez: tortenelem-5-6/09-honfoglalas (a honfoglalás 895 körül kezdődött, több évig tartott) -->
- Kheopsz piramisa: Kr. e. 2560 körül
<!-- forrás: ugyanez: tortenelem-5-6/02 (becslés; a források Kr. e. 2600–2560 közé teszik) -->
- jégkorszak vége: 11 700 éve
<!-- forrás: ICS International Chronostratigraphic Chart (a holocén kezdete 11 700 éve), lekérdezve: 2026-11-24 -->
- első mai emberek: kb. 315 ezer éve
<!-- forrás: ugyanez: biologia-7-8/02-mely-ido (Homo sapiens, Dzsebel Irhúd, Marokkó, kb. 315 ezer év; Hublin és mtsai 2017, Nature) -->
- dinoszauruszok kihalása: 66 millió éve
<!-- forrás: ugyanez: biologia-7-8/02-mely-ido (ICS: a kréta–paleogén határ 66,0 millió éve) -->
- Föld kora: 4,54 milliárd éve
<!-- forrás: ugyanez: biologia-7-8/02-mely-ido (Dalrymple 2001; USGS „Age of the Earth”: 4,54 ± 0,05 milliárd év) -->

<!-- Tanári megjegyzések és források:
  - Modell-egyszerűsítések: a földgömbök, a lámpa és a pálya nem méretarányos (a pálya alakja az 5. lépésben az, ott a Nap és a
    Föld mérete nem). A napállást a fizika-7-8/15 ÉGBOLT-moduljának képlete adja (a Nap helyzete ±0,1°, 2026-os évre);
    a napmagasság fénytörés nélküli, a nappal hossza a napkorong szélével és a fénytöréssel számolt (h₀ = −0,83°).
  - Az 1. lépés márciusi napéjegyenlőségkor mutatja a Földet (12 óra nappal, 12 óra éjjel); az idő „napidő”: délben jár
    legmagasabban a Nap. A 6. lépés órája a hivatalos (zónaidő + nyári időszámítás), ezért ott a dél kb. 11:44 (télen) és
    12:46 (nyáron).
  - A „Mi lenne, ha…?” csúszka (4. lépés) képzeletbeli kísérlet: a Föld tengelyének dőlése a valóságban évezredek alatt is csak
    kb. 22,1° és 24,5° között ingadozik. 0°-nál a nappal mindenhol kb. 12 óra (a fénytörés miatt Budapesten 12 óra 10 perc).
  - Az évszakok neve a csillagászati beosztás szerint (tavasz: márc. 20-tól, nyár: jún. 21-től, ősz: szept. 23-tól,
    tél: dec. 21-től). A meteorológia a teljes hónapokat számolja (a tél: december–február) – mindkettő használatos.
  - Napkelte iránya Budapesten (a lecke számolja): júniusban kb. 52°-nál (északkelet), decemberben kb. 128°-nál (délkelet),
    napéjegyenlőségkor kb. 90°-nál (kelet), északtól mérve.
  - A szökőév szabálya teljesen: 4 évente szökőév, kivéve a 100-zal osztható éveket, de a 400-zal oszthatók mégis azok.
  - A 6. lépés napirendje kitalált példa, nem ajánlás; a lecke nem minősít. Az alvás és a mozgás ajánlása forrással szerepel
    (AASM 2016, WHO 2020). Ha valakinek a napirendje gondot okoz, ne az osztály előtt beszéljétek meg.
  - Az időszalag (8. lépés) két dolgot mutat egy tengelyen: mennyi ideig tart valami (pislogás, nap, év, emberélet), és mennyi
    ideje történt (honfoglalás, piramis, kihalás, a Föld születése). A honfoglalás és a piramis „éve” a mai év alapján számolódik.
  - A Hold mozgása (kerettantervi tevékenység) a fizika-7-8/16-holdfazisok leckében van; a csillagos ég és az árnyékbot a
    fizika-7-8/15-fold-forgasa leckében.
  - A 4. lépés zseblámpája és felülnézeti fényfoltja a 17-idojaras lecke rajza (ugyanaz a tengelyferdeség-adat is).
  - Biztonság: a Napba soha nem nézünk (napszemüveggel, távcsővel, telefonnal sem) – a 2. és a 4. lépés vásznán.
-->
