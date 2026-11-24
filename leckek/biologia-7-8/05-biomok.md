# Miért nő esőerdő az Egyenlítőn? – biomok, tűrőképesség, alkalmazkodás
tantárgy: Biológia · évfolyam: 7–8. · témakör: 5. Bolygónk élővilága

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/biologia-7-8/05-biomok.md
  A számok az animációt is vezérlik: a klímadiagramok a havi értékekből rajzolódnak, a tenyészidőt, a Whittaker-diagram
  pontjait, a nyári szárazságot (és a térkép színeit), a hegyi lehűlés egyenesét a lecke ezekből számolja.
  Kapcsolódó lecke: Földrajz 9–10., 09-ovezetesseg (napsugárzás, éghajlati övek, talajok, függőleges övezetesség
  részletesen). Ez a lecke a biológiai oldalt mutatja: élőlények, tűrőképesség, alkalmazkodás, táplálékhálózat.
-->

## Közös
### Feliratok
- esőerdő: trópusi esőerdő
- szavanna: szavanna
- sivatag: forró sivatag
- lombhullató: lombhullató erdő
- tajga: tajga
- tundra: tundra
- hely esőerdő: Belém, Brazília
- hely szavanna: Mfuwe, Zambia
- hely sivatag: In Salah, Algéria
- hely lombhullató: Kékestető, Mátra
- hely tajga: Arhangelszk, Oroszország
- hely tundra: Utqiaġvik, Alaszka
- modell: modell
- illusztráció: illusztráció
- honnan tudjuk: HONNAN TUDJUK?
- forrás klíma: Forrás: WMO klímanormák 1991–2020 (NOAA NCEI)
- hónap-betűk: J, F, M, Á, M, J, J, A, Sz, O, N, D
- °C tengely: °C
- mm tengely: mm
- érték fok: # °C
- érték mm: # mm

### Adatok
<!-- Forrás (a havi adatokra): WMO Climatological Normals 1991–2020, a NOAA NCEI archívumában (accession 0253808, wmo_normals_9120_TAVG.csv és _PRCP.csv), https://www.ncei.noaa.gov/products/wmo-climate-normals, lekérdezve: 2026-11-24 (ugyanaz az adatkészlet, mint a Földrajz 9–10. 09-ovezetesseg leckében). Hőmérséklet: havi középhőmérséklet (°C), csapadék: havi összeg (mm). -->
<!-- állomás: Belém (WMO 82191), Brazília, az Amazonas torkolatvidéke, 7 m; évi átlag 26,8 °C, évi összeg 3308,3 mm. Manaus (82331) helyett: Manaus évi 2362 mm-e a Whittaker-diagram esőerdő-mezőjének határára esik. -->
- Belém hőmérséklete: 26,3; 26,1; 26,3; 26,5; 26,8; 26,9; 26,8; 27,1; 27,3; 27,3; 27,4; 27,0 °C
- Belém csapadéka: 393,8; 437,8; 506,3; 465,5; 323,6; 205,8; 156,0; 128,7; 120,1; 135,8; 151,4; 283,5 mm
<!-- állomás: Mfuwe (WMO 67577), Zambia, 570 m, a Dél-Luangwa Nemzeti Park bejárata (szavanna, miombo- és mopane-erdő); évi átlag 25,4 °C, évi összeg 804,4 mm -->
- Mfuwe hőmérséklete: 26,4; 26,5; 26,4; 25,4; 23,3; 21,1; 20,7; 22,9; 26,4; 28,9; 29,6; 27,5 °C
- Mfuwe csapadéka: 219,0; 169,2; 121,6; 30,7; 4,0; 0,0; 0,1; 0,1; 0,4; 9,9; 77,1; 172,3 mm
<!-- állomás: In Salah (WMO 60630), Algéria, Szahara, 268 m; évi átlag 26,7 °C, évi összeg 14,0 mm -->
- In Salah hőmérséklete: 14,4; 17,1; 21,6; 26,2; 31,2; 35,7; 38,2; 37,5; 34,3; 28,1; 20,4; 15,8 °C
- In Salah csapadéka: 2,9; 1,0; 1,4; 1,3; 0,8; 1,2; 0,1; 0,6; 1,4; 1,4; 1,4; 0,5 mm
<!-- állomás: Kékestető (WMO 12851), 1012 m, bükkös; évi átlag 6,4 °C, évi összeg 814,0 mm. Alföldi állomás (pl. Budapest, 526 mm) a Whittaker-diagramon a „ligetes erdő, bozót” mezőbe esik – a Kárpát-medence síkvidéke erdőssztyepp. Lombhullató erdő-állomásnak ezért a Kékes került ide; a panel kimondja. -->
- Kékestető hőmérséklete: −3,4; −2,7; 0,6; 6,3; 10,9; 14,5; 16,3; 16,4; 11,3; 6,6; 1,9; −2,5 °C
- Kékestető csapadéka: 41,5; 50,0; 47,9; 58,9; 94,3; 82,2; 105,7; 80,5; 67,6; 66,2; 67,2; 52,0 mm
<!-- állomás: Arhangelszk (WMO 22550), Oroszország, 8 m, tajga; évi átlag 1,9 °C, évi összeg 633,3 mm. Jakutszk (−8,0 °C, 233 mm) vörösfenyő-tajgája a Whittaker-diagramon a tundra mezőjébe esne (a permafroszt nyári olvadékvize pótolja a kevés csapadékot) – ezért nem az került ide. -->
- Arhangelszk hőmérséklete: −11,6; −10,7; −5,5; 0,8; 7,5; 13,1; 16,5; 13,6; 8,8; 2,5; −4,2; −8,2 °C
- Arhangelszk csapadéka: 41,4; 31,5; 31,3; 31,6; 47,5; 64,6; 74,6; 81,8; 62,3; 67,9; 51,2; 47,6 mm
<!-- állomás: Utqiaġvik (korábban Barrow), Post–Rogers repülőtér (WMO 70026), Alaszka, 9 m; évi átlag −10,2 °C, évi összeg 137,1 mm -->
- Utqiaġvik hőmérséklete: −24,2; −24,4; −23,6; −15,5; −5,2; 2,2; 5,4; 4,3; 0,9; −6,0; −14,6; −21,3 °C
- Utqiaġvik csapadéka: 3,7; 5,4; 4,5; 4,5; 7,2; 10,9; 24,8; 27,6; 19,7; 13,8; 9,3; 5,7 mm

## 1. Miért más az élet máshol?
Esőerdő, szavanna, sivatag, lombhullató erdő, tajga, tundra: a Föld nagy életközösségei, a **biomok**. Mindegyikben más növények és állatok élnek. Tippelj, aztán nyomd meg a gombot: hol terem több növény egy év alatt, a forró sivatagban vagy a hideg tundrán? ==A meleg önmagában nem elég.==

### Feliratok
- kérdés 1: Hol terem több növény egy év alatt?
- termés: 1 m²-en évente terem:
- termés érték: # g
- termés ismeretlen: ? g
- mutasd gomb: Mutasd a termést!
- tippelj: Tippelj: sivatag vagy tundra?
- szárazanyag: szárazanyag, átlag
### Adatok
<!-- Forrás (a nettó elsődleges termelésre, átlagérték, száraz növényi anyag): H. Lieth: From the computer: biological productivity of tropical lands. Unasylva 114 (FAO), táblázat: „Net primary productivity of major vegetation units of the world”, https://www.fao.org/4/k1100e/k1100e04.htm, lekérdezve: 2026-11-24. Az ottani kg/m²/év átlagok: trópusi esőerdő 2,8; trópusi füves terület, szavanna 0,8; lombhullató („summergreen”) erdő 1,0; tajga 0,65; tundra 0,16; sivatagi bozót 0,07 (a szélsőséges sivatag 0,003). A tankönyvekben gyakori Whittaker–Likens-féle (1975) értékek kissé eltérnek (pl. esőerdő 2,2; tajga 0,8; tundra 0,14 kg/m²/év) – a sorrend ugyanaz. A „sivatag” itt a sivatagi bozót átlaga; In Salah környéke ennél is kopárabb. -->
- termés esőerdő: 2800 g/m²
- termés szavanna: 800 g/m²
- termés sivatag: 70 g/m²
- termés lombhullató: 1000 g/m²
- termés tajga: 650 g/m²
- termés tundra: 160 g/m²

## 2. Mikor nőhet a növény?
A **klímadiagram** 30 év átlaga: a vonal a havi hőmérséklet, az oszlop a havi csapadék. A növény akkor nő, ha elég meleg és nedves van. Ez a **tenyészidő**. ==Ahol hosszú a tenyészidő, ott sok növény terem.== Kattints a többi helyre!

> megjegyzés: Itt egyszerűsítünk: meleg = legalább {tenyészidő küszöbe}, nedves = a vonal nem kerül az oszlop fölé.

### Feliratok
- kérdés 2: Mikor nőhet a növény?
- kattints hely: Kattints egy helyre!
- tenyészidő: tenyészidő: # hónap
- évi átlag: évi középhőmérséklet: # °C
- évi összeg: évi csapadék: # mm
- jel hő: havi középhőmérséklet
- jel eső: havi csapadék
- jel meleg: elég meleg és nedves hónap
- jel száraz: száraz hónap
- szöveg esőerdő: egész évben meleg és nedves
- szöveg szavanna: esős és száraz évszak váltakozik
- szöveg sivatag: szinte soha nem esik
- szöveg lombhullató: hideg tél, enyhe, nedves nyár
- szöveg tajga: hosszú, hideg tél, rövid nyár
- szöveg tundra: a nyár is hűvös és rövid
### Adatok
<!-- forrás: didaktikus küszöb (a „tenyészidő” meteorológiai definíciói 5 °C és 10 °C közötti napi középhőmérsékletet használnak; itt havi átlag) – modell -->
- tenyészidő küszöbe: 5 °C

## 3. Két szám dönti el
Tedd a helyeket egy grafikonra: vízszintesen az évi középhőmérséklet, függőlegesen az évi csapadék. A biomok saját mezőt kapnak: ez a **Whittaker-diagram**. ==Két számból nagyjából kitalálható, milyen élet lesz ott.== A Góbi sivatag hideg, mégis sivatag: kevés az eső. Húzd a pontot!

> megjegyzés: Budapest a „ligetes erdő” mezőbe esik: az Alföld eredeti növényzete erdőssztyepp.

### Feliratok
- kérdés 3: Két szám: hőmérséklet és csapadék
- x tengely: évi középhőmérséklet (°C)
- y tengely: évi csapadék (mm)
- húzd: Húzd a pontot!
- itt: itt:
- mező tundra: tundra
- mező tajga: tajga
- mező puszta: füves puszta, hideg sivatag
- mező ligetes: ligetes erdő, bozót
- mező lombhullató: lombhullató erdő
- mező mérsékelt esőerdő: mérsékelt övi esőerdő
- mező esőerdő: trópusi esőerdő
- mező szavanna: szavanna, száraz erdő
- mező sivatag: forró sivatag
- nincs mező: a diagramon kívül
- Budapest: Budapest
- Góbi: Góbi: hideg sivatag!
- forrás whittaker: Mezők: Whittaker (1975) nyomán, Ricklefs (2008) rajza; pontok: WMO 1991–2020
### Adatok
<!-- forrás: WMO klímanormák 1991–2020 (NOAA NCEI, mint fent): Budapest Belterület (WMO 12840) évi átlag 12,49 °C, évi összeg 526,2 mm; Dalanzadgad (WMO 44373), Mongólia, Góbi, 1462 m: 5,66 °C, 132,7 mm. A mezők határai: R. H. Whittaker: Communities and Ecosystems (1975) biomdiagramja, R. E. Ricklefs: The Economy of Nature (2008) 5.5. ábrájának digitalizálása (plotbiomes R-csomag, V. Ștefan és S. Levin, MIT-licenc) – a lecke kódjában, geometriaként. -->
- Budapest évi középhőmérséklete: 12,5 °C
- Budapest évi csapadéka: 526 mm
- Góbi évi középhőmérséklete: 5,7 °C
- Góbi évi csapadéka: 133 mm

## 4. Tűrőképesség: meddig bírja?
Minden fajnak van **tűrőképessége**: egy környezeti tényező tartománya, amelyben megél. A bükknek hűvös, csapadékos nyár kell. A **nyári szárazság** a nyári meleg és a nyári eső aránya. ==Ahol nagyobb, ott a bükk helyett tölgy, aztán erdőssztyepp jön.== Húzd a csúszkát: mi lesz, ha melegebb a nyár?

### Feliratok
- kérdés 4: Hol nőhet bükkös Magyarországon?
- görbe x: nyári szárazság
- görbe y: mennyire jól nő
- bükk: bükk
- cser: cser, kocsánytalan tölgy
- optimum: optimum
- tűrés: tűrőképesség
- szűk: szűk tűrésű
- tág: tág tűrésű
- képlet szárazság: 100 · júl–aug. hőmérséklet ÷ (máj–júl + júl–aug. eső)
- öv bükkös: bükkös
- öv gyertyános: gyertyános-tölgyes
- öv cseres: cseres-tölgyes
- öv erdőssztyepp: erdőssztyepp
- öv sztyepp: sztyepp
- darab: # állomás
- csúszka meleg: Melegebb nyár
- csúszka fok: +# °C
- térkép cím: Mérőállomások klímája
- forrás szárazság: Forrás: Führer és mtsai (2011); WMO 1991–2020
- áll Kékestető: Kékestető
- áll Szentgotthárd: Szentgotthárd
- áll Budapest: Budapest
- áll Szeged: Szeged
- áll Debrecen: Debrecen
- áll Pécs: Pécs
### Adatok
<!-- forrás: erdészeti aridítási index (FAI) = 100 · T(júl–aug) / (P(máj–júl) + P(júl–aug)) – Führer E., Horváth L., Jagodics A., Machon A., Szabados I. (2011): Application of a new aridity index in Hungarian forestry practice. Időjárás 115(3): 205–216. A kategóriahatárok (bükkös < 4,75 ≤ gyertyános-tölgyes < 6 ≤ kocsánytalan tölgyes-cseres < 7,25 ≤ erdőssztyepp < 8,5 ≤ sztyepp) Pongrácz R., Kis A., Szabó P., Bartholy J.: Projected changes of the forestry aridity index… (AMS 104. éves ülés, 2024, kiterjesztett összefoglaló, 2. táblázat) alapján, lekérdezve: 2026-11-24. A panel a képletet „nyári meleg ÷ nyári eső”-ként mondja ki; a vásznon a képlet egyszerűsített szövege áll (a júliusi eső a nevezőben kétszer szerepel). -->
- bükkös határa: 4,75
- gyertyános határa: 6
- cseres határa: 7,25
- erdőssztyepp határa: 8,5
<!-- Az állomások nyári adatai: júl–aug. középhőmérséklet (°C); máj–júl. csapadékösszeg (mm); júl–aug. csapadékösszeg (mm). Forrás: WMO klímanormák 1991–2020 (NOAA NCEI, mint fent; zárójelben a WMO-szám). A lecke ezekből számolja a nyári szárazságot (FAI). -->
- Kékestető nyara: 16,35; 282,2; 186,2
- Szentgotthárd nyara: 19,85; 260,4; 184,5
- Nagykanizsa nyara: 20,60; 230,0; 155,7
- Zalaegerszeg nyara: 20,75; 217,5; 141,1
- Szombathely nyara: 20,80; 215,3; 153,3
- Miskolc nyara: 21,35; 243,1; 155,7
- Jósvafő nyara: 19,85; 254,7; 160,0
- Eger nyara: 21,55; 217,3; 147,3
- Szécsény nyara: 20,00; 204,3; 137,0
- Pécs nyara: 22,00; 233,5; 132,9
- Kaposvár nyara: 21,50; 215,6; 138,5
- Keszthely nyara: 21,10; 200,4; 140,9
- Pápa nyara: 20,80; 194,8; 126,9
- Győr nyara: 21,35; 187,0; 123,2
- Mosonmagyaróvár nyara: 21,20; 194,5; 122,9
- Tata nyara: 21,15; 199,9; 132,0
- Budapest nyara: 23,10; 171,0; 107,9
- Paks nyara: 21,70; 192,8; 126,8
- Baja nyara: 21,60; 205,4; 120,8
- Szeged nyara: 22,35; 197,7; 105,1
- Kecskemét nyara: 21,95; 194,6; 107,9
- Szolnok nyara: 22,45; 189,8; 117,7
- Siófok nyara: 22,70; 169,8; 119,9
- Debrecen nyara: 21,85; 193,8; 114,1
- Nyíregyháza nyara: 21,35; 190,1; 113,9
- Békéscsaba nyara: 22,05; 192,0; 118,6
- Záhony nyara: 21,35; 210,3; 128,3
<!-- WMO-számok: Kékestető 12851, Szentgotthárd-Farkasfa 12910, Nagykanizsa 12925, Zalaegerszeg-Nagykutas 12915, Szombathely 12812, Miskolc-Diósgyőr 12772, Jósvafő 12766, Eger 12870, Szécsény 12756, Pécs-Pogány 12942, Kaposvár 12930, Keszthely 12920, Pápa 12824, Győr-Likócs 12822, Mosonmagyaróvár 12815, Tata 12836, Budapest Belterület 12840, Paks 12950, Baja 12960, Szeged Külterület 12982, Kecskemét 12970, Szolnok 12860, Siófok 12935, Debrecen 12882, Nyíregyháza-Napkor 12892, Békéscsaba 12992, Záhony 12786. A görbék alakja (optimum, szélesség) didaktikus modell; a mért adat az állomások helye a tengelyen és a kategóriahatárok. -->

## 5. Ki hol él?
Az élőlények testfelépítése és életmódja illik a biomjukhoz: ez az **alkalmazkodás**. Kattints egy élőlényre, aztán a biomjára! A sivatagi **fennek** nagy füle sok hőt ad le, a sarki róka kicsi füle és dús bundája hőt tart meg. ==A test formája a környezetről árulkodik.==

### Feliratok
- kérdés 5: Ki hol él? Párosítsd!
- válassz: Kattints egy élőlényre, aztán a biomjára!
- most: most a biomja jön
- nem jó: Nem ott él – próbáld újra!
- kész: Mind a hat a helyén!
- megoldás gomb: Megoldás
- újra gomb: Újra
- fennek: fennek
- sarki róka: sarki róka
- lucfenyő: lucfenyő
- bükkfa: bükk
- akácia: ernyőakácia
- liána: liána
- a fennek: nagy fül: sok hőt ad le
- a sarki róka: kicsi fül, dús bunda: hőt tart
- a lucfenyő: kúp alak, tűlevél: lecsúszik a hó
- a bükkfa: télre lehullatja a levelét
- a akácia: tövis, mély gyökér
- a liána: a fák törzsén kúszik a fényre
- fül arány: fennek: # cm-es fül, # cm-es test
### Adatok
<!-- forrás: Fennec fox – Wikipedia (Asa és mtsai 2014; Larivière 2002, Mammalian Species 714 alapján): fej-törzs hossza hím kb. 39–39,5 cm, nőstény 34,5–39,5 cm; fül hím kb. 10 cm, nőstény 9–9,5 cm; lekérdezve: 2026-11-24. A sarki róka fülhosszára megbízható számot nem találtunk (rövid, kerek fül, a test kompakt – Wikipedia „Arctic fox”), ezért a vásznon csak a fennek számai állnak; a rókarajzok „illusztráció”. -->
- fennek füle: 10 cm
- fennek teste: 39 cm

## 6. Esőerdő: sok élet, sovány talaj
Az esőerdőben terem a legtöbb növény, mégis sovány a talaja. A meleg, nedves avarban a lebontók gyorsan dolgoznak, a gyökerek pedig rögtön visszaveszik a tápanyagot. ==A tápanyag nagy része a fákban van, nem a talajban.== Vágd ki az erdőt: mi marad a szántónak?

### Feliratok
- kérdés 6: Hol van a tápanyag?
- tápanyag: tápanyag
- fában: a növényekben
- talajban: az avarban, talajban
- avar bomlik: az avar lebomlik: kb. # év alatt
- kivág gomb: Kivágjuk az erdőt
- visszaáll gomb: Visszaállít
- kimossa: az eső kimossa
- maradt: a talajban maradt: # %
- talaj: talaj
- avar: avar
### Adatok
<!-- forrás: az avar (erdei alom) szerves anyagának átlagos tartózkodási ideje: trópusi esőerdő kb. 0,4 év (Edwards és Grubb 1982 alapján); mérsékelt övi lombhullató erdő kb. 4 év; boreális tűlevelű erdő több száz év – W. H. Schlesinger: Biogeochemistry (Cole és Rapp 1981 adataiból összesített táblázat); a 0,4 év és a trend ellenőrizve (UC Davis SSC219 kurzus 8. táblázat, keresési összefoglaló alapján), a 4 év ellenőrizendő – szakmai review! A tápanyag-pöttyök eloszlása ebből számolt modell (a talajban töltött idő aránya); az irtás utáni kimosódás sebessége és az, hogy a lombhullató erdő humuszos, agyagos talaja a tápanyag kb. 70%-át megtartja, szemléltető modell, nem mért adat. -->
- avar lebomlása esőerdőben: 0,4 év
- avar lebomlása lombhullató erdőben: 4 év

## 7. Ki kit eszik a szavannán és a tundrán?
A biomok élőlényei is **táplálékhálózatot** alkotnak. A szavannán sok nagy növényevő legel, őket nagyragadozók eszik. A tundrán kevés a faj: a kicsi **lemming** sok ragadozót tart el. ==Kevés fajú hálózatban egy faj eltűnése mindenkit érint.== Kattints egy fajra!

> megjegyzés: A táplálékhálózatról bővebben: 6. lecke.

### Feliratok
- kérdés 7: Ki kit eszik?
- váltás gomb: Szavanna ↔ tundra
- vissza gomb: Mindenki vissza
- kattints faj: Kattints egy fajra!
- több lesz: több lesz
- kevesebb lesz: kevesebb lesz
- fű: fűfélék
- akáciafa: ernyőakácia
- zebra: zebra
- gnú: gnú
- zsiráf: zsiráf
- oroszlán: oroszlán
- hiéna: foltos hiéna
- lebontók: lebontók
- zuzmó: zuzmó
- sás: sás
- törpefűz: törpefűz
- lemming: lemming
- rénszarvas: rénszarvas
- hóbagoly: hóbagoly
- róka tundra: sarki róka
- farkas: farkas
- termelők: termelők
- növényevők: növényevők
- ragadozók: ragadozók
- tundra cím: Tundra (Alaszka, Lappföld)
- szavanna cím: Szavanna (Kelet- és Dél-Afrika)
- bagoly tény: Lemmingszegény években a hóbagoly alig költ.
<!-- A hálózatok egyszerűsítettek (8–9 faj). Szavanna: a gnú és a zebra füvet legel, a zsiráf az akácia lombját eszi; az oroszlán és a foltos hiéna is vadászik és dögöt is eszik; a zsiráfot főleg az oroszlán ejti el. Tundra: a lemming sással, fűfélékkel és mohával táplálkozik; a rénszarvas télen főleg zuzmót, nyáron sást és törpefüzet eszik; a hóbagoly és a sarki róka fő zsákmánya a lemming; a rénszarvast a farkas zsákmányolja. A hóbagoly költése és fészekaljmérete a lemmingek számától függ (pl. Therrien és mtsai 2014, Ecology 95: 56–67) – szakmai review. -->

## 8. Hegyre fel = sark felé
Felfelé hűl a levegő: a svájci mérőállomások szerint 100 méterenként kb. {mért lehűlés}. Ezért a hegyen is övek követik egymást: lomberdő, tűlevelű erdő, havasi rét, hó – mint az Egyenlítőtől a sark felé. Ez a **függőleges övezetesség**. ==A hegyre mászva biomokon mész át.== Húzd a csúszkát!

> megjegyzés: Humboldt 1802-ben a Chimborazón rajzolt először ilyen növényöveket.

### Feliratok
- kérdés 8: Hegyre fel, mint a sark felé
- magasság tengely: magasság (m)
- hőmérséklet tengely: évi középhőmérséklet (°C)
- csúszka hegy: Hegymászó magassága
- csúszka m: # m
- öv lomb: lomberdő
- öv tű: tűlevelű erdő
- öv rét: havasi rét
- öv hó: hó és jég
- mint lomb: mint a lombhullató erdő
- mint tű: mint a tajga
- mint rét: mint a tundra
- mint hó: mint a sarki jég
- itt fok: itt kb. # °C
- svájci pontok: svájci mérőállomások
- egyenes: 100 m-enként # °C-kal hidegebb
- erdőhatár: erdőhatár
- hóhatár: hóhatár
- Alpok: Alpok, északi oldal
- Humboldt: Alexander von Humboldt
- Humboldt szöveg: 1802: Chimborazo, 6263 m
- forrás hegy: Forrás: WMO 1991–2020, 25 svájci állomás
### Adatok
<!-- forrás: WMO klímanormák 1991–2020 (NOAA NCEI, mint fent), 25 svájci állomás évi középhőmérséklete a magasság szerint (WMO 06770 Lugano, 06601 Basel-Binningen, 06700 Genf-Cointrin, 06660 Zürich-Fluntern, 06650 Luzern, 06720 Sion, 06631 Bern-Zollikofen, 06786 Chur, 06681 St. Gallen, 06675 Einsiedeln, 06655 Engelberg, 06617 La Brévine, 06784 Davos, 06748 Zermatt, 06695 Andermatt, 06785 Arosa, 06792 Samedan, 06744 Grimsel Hospiz, 06659 Pilatus, 06750 Gütsch, 06717 Col du Grand St-Bernard, 06680 Säntis, 06780 Weissfluhjoch, 06791 Piz Corvatsch, 06730 Jungfraujoch). A lecke legkisebb négyzetes egyenest illeszt; a „mért lehűlés” ezzel egyezik (a lecke ellenőrzi). A tankönyvi érték 0,5–0,65 °C / 100 m (a szabad légkörben 0,65); az évi átlag a hegyoldalon kisebb. La Brévine (hideg katlan) és Samedan (Engadin, hideg völgy) kilóg – a helyi domborzat is számít. -->
- svájci állomások magassága: 273; 316; 411; 556; 454; 482; 553; 556; 776; 911; 1036; 1050; 1594; 1638; 1435; 1878; 1709; 1980; 2105; 2286; 2472; 2501; 2691; 3294; 3571 m
- svájci állomások hőmérséklete: 13,0; 10,9; 11,0; 9,8; 10,1; 10,7; 9,3; 10,3; 8,7; 7,2; 6,8; 5,3; 3,9; 4,7; 3,9; 3,7; 2,3; 2,3; 2,3; 0,9; −0,1; −0,7; −1,5; −5,0; −6,7 °C
- mért lehűlés: 0,54 °C
<!-- forrás (az övhatárokra, az Alpok északi oldala, tájanként eltér): a lomberdő (bükk) felső határa kb. 1200–1600 m, az erdőhatár kb. 1800–2200 m, a hóhatár kb. 2700–3100 m (a pilot terv irányértékei; tankönyvi értékek, a Földrajz 9–10. 09-ovezetesseg lecke Alpok-adataival egyezően) – ellenőrizendő, szakmai review. Humboldt és Bonpland 1802. június 23-án jutott kb. 5600 m-ig a Chimborazón; a „Naturgemälde” (a növényövek ábrája) 1807-ben jelent meg (Essai sur la géographie des plantes). A Chimborazo magassága 6263 m (tankönyvi érték; újabb mérés 6263,47 m). -->
- lomberdő határa: 1200–1600 m
- erdőhatár magassága: 1800–2200 m
- hóhatár magassága: 2700–3100 m
- hegymászó kezdete: 500 m

## 9. Összefoglalás
Egy hely biomját főleg két szám dönti el: az évi **hőmérséklet** és a **csapadék**, és hogy mikor esik. Minden fajnak megvan a **tűrőképessége**, ezért él ott, ahol él. ==Az élőlények alakja, életmódja és táplálékhálózata a biomhoz illik.== A hegyen ugyanezek az övek ismétlődnek.

### Feliratok
- összegzés cím: Biomok: éghajlat → élővilág
- ö1: Két szám: hőmérséklet és csapadék
- ö2: Tenyészidő: meleg és nedves hónapok
- ö3: Tűrőképesség: meddig bírja a faj?
- ö4: Alkalmazkodás: a forma a környezethez illik
- ö5: Táplálékhálózat minden biomban
- ö6: Hegyre fel = sark felé

<!--
  Vitatott / bizonytalan pontok, egyszerűsítések (tanári / szakértői review):
  - A hat jellegzetes állomás egy-egy példa, nem „a biom átlaga”. A Whittaker-diagram mezőinek határa elmosódott;
    a „ligetes erdő, bozót” mező az ember és a tűz hatására, talajtól függően erdő, bozót vagy füves puszta is lehet.
  - A tenyészidő-szabály (≥ 5 °C havi átlag és nem száraz hónap) didaktikus egyszerűsítés; a tundra növényei
    0 °C körül is nőnek, a tajga fái a permafroszt olvadékvizét is használják.
  - A nyári szárazság (FAI) a magyar erdészet mutatója, a kategóriák a klímazonális (az adott klímában uralkodó)
    erdőtípust jelzik – a bükk egyes példányai, szurdokokban, északi oldalon ennél szárazabb klímájú helyen is élnek.
    A „+°C” csúszka csak a nyári hőmérsékletet emeli, a csapadékot nem változtatja (egyszerűsítés).
  - A tűrőképességi görbék alakja modell (a bükk szűkebb, a cser tágabb tűrésű a nyári szárazságra).
  - Az alkalmazkodás-párosításban az ernyőakácia a kelet-afrikai szavanna jellegzetes fája; a szárazság idején
    részben lombhullató. A „kúp alak – lecsúszik a hó” közismert magyarázat; a tűlevél a fagyos, „fiziológiailag
    száraz” télen a vízvesztést is csökkenti.
  - Esőerdő: a tápanyag-eloszlás pöttyei modell (a talajban töltött idő aránya a bomlási időből); az irtás utáni
    kimosódás gyorsasága szemléltető.
  - A svájci egyenes évi átlagra illesztett; a szabad légkör 0,65 °C / 100 m-es értéke ennél nagyobb.
-->
