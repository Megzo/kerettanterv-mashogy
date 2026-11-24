# Miért nem fagy be Narvik kikötője? – szoláris és valódi éghajlati övezetesség
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 5. A geoszférák kölcsönhatásai és összefüggései

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/09-ovezetesseg.md
  A számok az animációt is vezérlik: a klímadiagramok a havi értékekből rajzolódnak, a napmagasságot,
  a nappal hosszát és a besugárzást a lecke a tengelyferdeségből és a napállandóból számolja, a
  tengeráramlások vonala az itt megadott koordinátákon fut, a hegyek növényövei az itt megadott
  magasságok között vannak. Ha egy havi értéket javítasz, a lecke ellenőrzi, hogy a 12 hónap összege
  (csapadék) ill. átlaga (hőmérséklet) egyezik-e az évi értékkel.
-->

## Közös

### Feliratok
- modell: modell
- vázlatos: vázlatos
- becslés: becslés
- torzítás: függőleges torzítás #×
- méretarányos: méretarányos
- hónap-betűk: J, F, M, Á, M, J, J, A, Sz, O, N, D
- hónapnevek: január, február, március, április, május, június, július, augusztus, szeptember, október, november, december
- °C tengely: °C
- mm tengely: mm
- Egyenlítő: Egyenlítő
- Ráktérítő: Ráktérítő
- Baktérítő: Baktérítő
- északi sarkkör: északi sarkkör
- déli sarkkör: déli sarkkör
- forró övezet: forró övezet
- mérsékelt övezet: mérsékelt övezet
- hideg övezet: hideg övezet
- csúszka dátum: Dátum
- forrás klíma: Forrás: WMO klímanormák 1991–2020 (NOAA NCEI archívum)
- forrás klíma térkép: Forrás: WMO klímanormák 1991–2020 (NOAA NCEI archívum) · Made with Natural Earth
- Budapest: Budapest
- Bergen: Bergen
- Jakutszk: Jakutszk
- Narvik: Narvik
- Iqaluit: Iqaluit
- Arica: Arica
- Vitória: Vitória
- Manaus: Manaus
- Niamey: Niamey
- Asszuán: Asszuán
- Málaga: Málaga
- Utqiaġvik: Utqiaġvik
- érték °C: # °C
- érték mm: # mm

### Adatok
<!-- forrás: IERS/IAU, a fizika-7-8/15-fold-forgasa lecke adatával egyezik (2026-ban 23,436°) -->
- tengelyferdeség: 23,44°
<!-- forrás: Kopp & Lean 2011 (Geophys. Res. Lett. 38, L01706), a fizika-7-8/14-uveghaz lecke adatával egyezik -->
- napállandó: 1361 W/m²
<!-- forrás (az alábbiakra): WMO Climatological Normals 1991–2020, a NOAA NCEI archívumában (accession 0253808, v6.6, data-composite-primary-parameters: wmo_normals_9120_TAVG.csv és _PRCP.csv), https://www.ncei.noaa.gov/products/wmo-climate-normals, lekérdezve: 2026-11-24. A WMO 40. határozata szerinti alapadat, NOAA-archívum, szabad felhasználás forrásmegjelöléssel (ellenőrizendő). Hőmérséklet: havi középhőmérséklet (°C), csapadék: havi összeg (mm). A koordináták az állomásé. -->
- Budapest helye: 47,51° É, 19,03° K
- Budapest hőmérséklete: 1,3; 3,1; 7,5; 13,3; 17,6; 21,5; 23,3; 22,9; 17,8; 12,3; 7,2; 2,1 °C
- Budapest csapadéka: 33,0; 30,2; 31,2; 32,5; 57,3; 60,0; 53,7; 54,2; 46,1; 44,1; 46,2; 37,7 mm
- Budapest évi csapadéka: 526,2 mm
<!-- állomás: Budapest Belterület (WMO 12840) -->
- Bergen helye: 60,38° É, 5,33° K
- Bergen hőmérséklete: 2,6; 2,3; 3,8; 7,2; 10,7; 13,6; 15,6; 15,4; 12,6; 8,6; 5,3; 3,1 °C
- Bergen csapadéka: 256,3; 209,3; 201,7; 140,6; 108,5; 132,3; 157,5; 207,9; 248,5; 268,1; 275,1; 289,8 mm
<!-- állomás: Bergen-Florida (WMO 01317); évi összeg 2495,6 mm -->
- Jakutszk helye: 62,02° É, 129,72° K
- Jakutszk hőmérséklete: −36,9; −32,9; −19,1; −3,7; 8,0; 17,0; 19,9; 15,6; 6,4; −6,9; −25,9; −37,0 °C
- Jakutszk csapadéka: 9,7; 8,5; 6,3; 7,9; 20,1; 29,5; 40,1; 37,1; 29,6; 18,6; 16,9; 8,5 mm
<!-- állomás: Jakutszk (WMO 24959); évi összeg 232,8 mm -->
- Narvik helye: 68,44° É, 17,39° K
- Narvik hőmérséklete: −2,3; −2,7; −0,8; 2,9; 7,3; 11,4; 14,5; 13,5; 9,4; 4,5; 1,2; −0,8 °C
<!-- állomás: Narvik repülőtér (Framnes; norvég állomásszám 84700, WIGOS 0-578-0-84700); csapadékadata az adatkészletben nincs, a lecke nem is használja -->
- Iqaluit helye: 63,75° É, 68,54° Ny
- Iqaluit hőmérséklete: −26,0; −27,0; −22,3; −13,5; −3,2; 3,9; 8,1; 7,4; 2,9; −3,2; −11,1; −18,9 °C
<!-- állomás: Iqaluit Climate (WMO 71321), Baffin-sziget, Kanada; a csapadéksor hiányos, a lecke nem használja -->
- Arica helye: 18,36° D, 70,34° Ny
- Arica hőmérséklete: 22,5; 22,8; 22,0; 20,2; 18,4; 17,1; 16,1; 16,1; 16,6; 17,8; 19,4; 20,9 °C
- Arica csapadéka: 0,4; 0,3; 0,3; 0,0; 0,1; 0,2; 0,5; 0,1; 0,3; 0,0; 0,0; 0,1 mm
- Arica évi csapadéka: 2,2 mm
<!-- állomás: Arica, Chacalluta repülőtér (WMO 85406), Chile; a havi értékek összege kerekítés miatt 2,3 mm. A brief Limát (Peru) javasolta – a perui állomások nincsenek a WMO-adatkészletben; Arica ugyanazon a parton, ugyanabban a Humboldt-áramlás menti sivatagban fekszik. -->
- Vitória helye: 20,32° D, 40,32° Ny
- Vitória hőmérséklete: 27,1; 27,5; 27,1; 25,9; 24,0; 23,1; 22,5; 22,6; 23,4; 24,4; 25,0; 26,3 °C
- Vitória csapadéka: 131,2; 79,4; 139,5; 122,9; 92,4; 70,0; 67,5; 59,9; 63,1; 123,9; 233,6; 201,0 mm
- Vitória évi csapadéka: 1384,4 mm
<!-- állomás: Vitória (WMO 83648), Brazília, Atlanti-óceáni part -->
- Manaus helye: 3,10° D, 60,02° Ny
- Manaus hőmérséklete: 26,6; 26,6; 26,6; 26,7; 27,0; 27,3; 27,5; 28,2; 28,6; 28,5; 28,0; 27,2 °C
- Manaus csapadéka: 305,6; 296,8; 320,9; 331,0; 233,3; 117,2; 67,1; 56,1; 79,0; 113,9; 188,0; 253,5 mm
<!-- állomás: Manaus (WMO 82331), Brazília; évi összeg 2362,4 mm -->
- Niamey helye: 13,48° É, 2,17° K
- Niamey hőmérséklete: 24,6; 27,8; 31,9; 34,7; 34,5; 32,2; 29,5; 28,1; 29,6; 31,5; 29,0; 25,5 °C
- Niamey csapadéka: 0,0; 0,3; 0,2; 9,8; 25,3; 78,6; 145,6; 192,6; 85,1; 16,7; 0,0; 0,0 mm
<!-- állomás: Niamey repülőtér (WMO 61052), Niger; évi összeg 554,2 mm -->
- Asszuán helye: 23,97° É, 32,78° K
- Asszuán hőmérséklete: 16,3; 18,6; 22,9; 28,0; 32,2; 34,4; 35,1; 35,0; 32,7; 29,2; 22,7; 17,6 °C
- Asszuán csapadéka: 0,1; 0,0; 0,6; 0,3; 0,1; 0,0; 0,0; 0,0; 0,1; 0,7; 0,0; 0,1 mm
<!-- állomás: Asszuán (WMO 62414), Egyiptom; évi összeg 2,0 mm -->
- Málaga helye: 36,67° É, 4,48° Ny
- Málaga hőmérséklete: 12,7; 13,4; 15,1; 16,9; 19,9; 23,5; 26,0; 26,6; 23,8; 19,9; 15,9; 13,6 °C
- Málaga csapadéka: 62,3; 58,9; 66,1; 41,4; 23,1; 4,4; 0,1; 2,7; 25,2; 60,8; 79,3; 87,9 mm
<!-- állomás: Málaga repülőtér (WMO 08482), Spanyolország; évi összeg 512,2 mm. A brief Rómát nem kérte; a római állomások nyári csapadéka az adatkészletben hiányzik. -->
- Utqiaġvik helye: 71,28° É, 156,78° Ny
- Utqiaġvik hőmérséklete: −24,2; −24,4; −23,6; −15,5; −5,2; 2,2; 5,4; 4,3; 0,9; −6,0; −14,6; −21,3 °C
- Utqiaġvik csapadéka: 3,7; 5,4; 4,5; 4,5; 7,2; 10,9; 24,8; 27,6; 19,7; 13,8; 9,3; 5,7 mm
<!-- állomás: Utqiaġvik (korábban Barrow), Post–Rogers repülőtér (WMO 70026), Alaszka; évi összeg 137,1 mm -->

## 1. A napsugarak hajlásszöge
A napsugarak párhuzamosan érkeznek, de a Föld gömbölyű. Ahol a Nap magasan delel, ott a nyaláb kis felületre jut, ==ezért erősebben melegít==. Ferde sugárzásnál ugyanaz az energia nagyobb felületen oszlik el. A nappal hossza is számít.

> megjegyzés: Állítsd júniusra, és menj az Északi-sarkra! Ki kap egy nap alatt több napfényt: a sark vagy az Egyenlítő?

### Feliratok
- cím 1: Delel a Nap
- napfény: napfény
- tengely: forgástengely
- éjszaka: éjszaka
- nappal: nappal
- itt: itt
- napmagasság szög: #°
- nyaláb cím: Ugyanaz a nyaláb a talajon
- nyaláb felület: # m² felületen oszlik el
- nyaláb merőleges: 1 m²-es nyaláb
- delelés: Delelési napmagasság
- delelés érték: #°
- nincs delelés: a Nap nem kel fel
- nappal hossza: A nappal hossza
- nappal érték: # óra # perc
- besugárzás: Napi átlag a légkör tetején
- besugárzás érték: # W/m²
- grafikon 1 cím: Napi átlagos besugárzás a légkör tetején
- grafikon x: földrajzi szélesség
- grafikon y: W/m²
- csúszka szélesség: Földrajzi szélesség
- szélesség É: #° É
- szélesség D: #° D
- szélesség 0: 0° (Egyenlítő)
- forrás 1: Számolás a napállandóból és a tengelyferdeségből, légköri fénytörés és elnyelés nélkül (modell)

### Adatok
- kezdő szélesség: 47,5° (modell)
<!-- forrás: a csúszka kezdőértéke (Budapest szélessége kerekítve) -->
- kezdő nap: 172 (modell)
<!-- forrás: a csúszka kezdőértéke: az év 172. napja = június 21. (nem szökőévben) -->

## 2. Öt szoláris öv
A **térítők** között a Nap évente kétszer delel merőlegesen: ez a **forró övezet**. A **sarkkörökön** túl van sarki éjszaka és sarki nappal: ez a **hideg övezet**. Közöttük a **mérsékelt övezet** fekszik. Ez a **szoláris éghajlati övezetesség**: ==csak a napsugárzásból következik==.

> megjegyzés: Húzd a dátumot! Az övek határa a tengelyferdeségből adódik.

### Feliratok
- cím 2: Öt szoláris öv
- merőleges: itt delel merőlegesen a Nap
- sarki éj: sarki éjszaka
- sarki nap: sarki nappal
- skála cím: napi átlagos besugárzás (W/m²)
- grafikon 2 cím: Évi átlagos besugárzás
- évi átlag: évi átlag
- aznap: a kiválasztott napon
- egyenlítő érték: Egyenlítő: # W/m²
- sark érték: sark: # W/m²
- húzd: húzd a gömböt
- forrás 2: Számolás a napállandóból és a tengelyferdeségből, a légkör nélkül (modell) · Made with Natural Earth

## 3. Tenger és szárazföld
Bergen és Jakutszk szinte azonos szélességen fekszik, mégis más az éghajlatuk. A víz lassan melegszik és lassan hűl: nagy a hőkapacitása, és a hullámzás mélyre keveri a hőt. A nyugatias szél ==az óceán felől fúj Bergenbe==, Jakutszkba a kontinens felől.

> megjegyzés: Tévhit: az éghajlat csak a szélességtől függ. A **valódi éghajlati övezetesség** első módosító tényezője ez.

### Feliratok
- cím 3: Ugyanaz a szélesség, más éghajlat
- óceáni: óceáni éghajlat
- szárazföldi: szárazföldi éghajlat
- grafikon 3 cím: Havi középhőmérséklet (°C)
- hőingás: évi hőingás: # °C
- nyugatias szél: nyugatias szél
- óceán: Atlanti-óceán
- csúszka hónap: Hónap

### Adatok
- kezdő hónap: 1
<!-- forrás: a csúszka kezdőértéke (január) -->

## 4. Tengeráramlások: Narvik és Arica
A meleg **Golf-áramlás** és folytatása, az **Észak-atlanti áramlás** hőt visz észak felé. A nyugatias szél a part fölé hozza: ==ezért nem fagy be Narvik kikötője==. A hideg **Humboldt-áramlás** alulról hűti a levegőt, ami így nem száll fel, nem ad esőt: sivatag a part.

> megjegyzés: Az áramlások vonala vázlatos. A **Labrador-áramlás** hideg vizet hoz dél felé.

### Feliratok
- cím 4: Meleg és hideg tengeráramlások
- gomb Atlanti: Észak-Atlanti-óceán
- gomb Amerika: Dél-Amerika
- meleg áramlás: meleg áramlás
- hideg áramlás: hideg áramlás
- Golf-áramlás: Golf-áramlás
- Észak-atlanti áramlás: Észak-atlanti áramlás
- Labrador-áramlás: Labrador-áramlás
- Kanári-áramlás: Kanári-áramlás
- Humboldt-áramlás: Humboldt-áramlás
- Brazíliai-áramlás: Brazíliai-áramlás
- összevetés januári: Januári középhőmérséklet
- összevetés évi csapadék: Évi csapadék
- szélesség érték: #° É
- szélesség érték D: #° D
- jégmentes: jégmentes kikötő
- befagy: télen befagyó öböl
- sivatag: sivatag a hideg áramlás mellett
- esős: esős part a meleg áramlás mellett
- forrás 4: Tengeráramlások: vázlatos, tankönyvi ismeret alapján · klíma: WMO 1991–2020 (NOAA NCEI) · Made with Natural Earth

### Adatok
<!-- forrás (az alábbiakra): a tengeráramlások vonala VÁZLATOS, saját rajz a tankönyvi áramlástérképek alapján (nem mért áramlási adat; terv, Döntések 4.). Formátum: hosszúság; szélesség párok fokban, a nyugati hosszúság és a déli szélesség negatív. A sebesség csak a rajz kedvéért különbözik (modell). -->
- Golf-áramlás vonala: −80; 25; −79,5; 28; −79; 31; −76; 34; −72; 36,5; −66; 38,5; −58; 40; −50; 41,5
- Észak-atlanti áramlás vonala: −48; 43; −40; 46; −30; 50; −20; 54; −12; 58; −5; 61,5; 3; 64; 10; 67; 15; 69,5; 22; 71,5; 32; 72,5
- Labrador-áramlás vonala: −62; 66; −60; 62; −58; 58; −55; 54; −52; 50; −50; 46,5; −51; 43,5
- Kanári-áramlás vonala: −13; 42; −14,5; 37; −16,5; 32; −18; 27; −19; 22; −20; 17
- Humboldt-áramlás vonala: −76; −45; −75,5; −40; −74; −35; −72,5; −30; −72; −25; −72; −20; −74; −15; −78; −10; −81; −6; −84; −3; −88; −1
- Brazíliai-áramlás vonala: −34; −8; −35; −12; −37; −16; −39; −20; −41; −23,5; −45; −27; −48; −31; −51; −35; −53; −38

## 5. Az éghajlati diagram olvasása
Az **éghajlati diagram** egy hely 30 éves átlagát mutatja: a vonal a havi középhőmérséklet, az oszlop a havi csapadék. A tengelyek úgy állnak, hogy ==10 °C egy magasságban van 20 mm-rel==. Ha a vonal az oszlop fölé kerül, a párolgás több lehet a csapadéknál: az a hónap **száraz**.

> megjegyzés: Hasonlítsd össze Málagával! Hol van száraz időszak?

### Feliratok
- cím 5: Budapest éghajlati diagramja
- cím 5 Málaga: Málaga éghajlati diagramja
- gomb Málaga: Összevetés: Málaga
- gomb Budapest: Vissza: Budapest
- évi közép: évi középhőmérséklet
- évi hőingás: évi közepes hőingás
- évi csapadék: évi csapadék
- legcsapadékosabb: legcsapadékosabb hónap
- száraz hónapok: száraz hónapok száma
- skála: 10 °C ↔ 20 mm
- száraz időszak: száraz időszak
- hőmérséklet: havi középhőmérséklet
- csapadék: havi csapadék

## 6. Övek egymás után
Az övek az Egyenlítőtől a sarkok felé követik egymást, de ==határuk nem egy szélességi kör==. Párosítsd a diagramokat a városokkal: kattints egy diagramra, aztán a városra! Figyeld a hőingást, és azt, mikor esik az eső.

> megjegyzés: Tévhit: az Egyenlítőn a legmelegebb. Nézd meg Asszuán és Niamey nyarát!

### Feliratok
- cím 6: Melyik diagram melyik városé?
- gomb megoldás: Mutasd a megoldást
- gomb újra: Újrakezdés
- válassz: Válassz egy diagramot!
- most városra: Most kattints a városra!
- nem ez: Nem ez – próbáld újra!
- kész: Mind a hat stimmel!
- betűk: A, B, C, D, E, F
- öv Manaus: egyenlítői öv
- öv Niamey: átmeneti öv (szavanna)
- öv Asszuán: térítői öv (sivatag)
- öv Málaga: meleg mérsékelt öv (mediterrán)
- öv Jakutszk: hideg mérsékelt öv (tajga)
- öv Utqiaġvik: sarkköri öv (tundra)
- sűrítés: 100 mm fölött sűrítve

## 7. A talaj is övezetes
A **humusz** az elhalt növényi részekből képződik. Meleg, nedves éghajlaton gyorsan lebomlik, és az eső kimossa a tápanyagot. Ahol a nyár száraz, a tél hideg, ott felhalmozódik. Ezért a talaj az övekkel együtt változik: ez a **zonális talaj**.

> megjegyzés: Az **azonális talaj** helyi okból alakul, pl. a folyó árterén (öntéstalaj). Kattints egy talajra!

### Feliratok
- cím 7: Az öveket a talaj is követi
- humusz: humuszos réteg
- mély: kb. # cm
- talaj vörösföld: trópusi vörösföld
- talaj váztalaj: sivatagi váztalaj
- talaj csernozjom: mezőségi talaj (csernozjom)
- talaj barna: barna erdőtalaj
- talaj podzol: podzol
- talaj tundra: tundratalaj
- növ esőerdő: trópusi esőerdő
- növ sivatag: sivatag
- növ puszta: füves puszta
- növ lomberdő: lombhullató erdő
- növ tajga: tajga
- növ tundra: tundra
- miért vörösföld: Meleg és sok eső: a lomb gyorsan lebomlik, az eső kimossa. Vas-oxidtól vörös.
- miért váztalaj: Kevés a növény, kevés a humusz. Kőzettörmelék, a felszínen sók.
- miért csernozjom: A fű gyökere évente elhal; a száraz nyár és a hideg tél lassítja a lebomlást.
- miért barna: Az avar közepesen gyorsan bomlik, a csapadék kissé kilúgozza.
- miért podzol: A savanyú tűavar lassan bomlik; a víz kimossa alóla a vasat: szürke réteg marad.
- miért tundra: Rövid a nyár, alatta örökké fagyott a talaj, ezért vizenyős.
- kattints: Kattints egy talajszelvényre!
- talaj kártya humusz: humuszos réteg
- talaj kártya öv: öv
- örök fagy: örökké fagyott talaj
- kilúgozott: kilúgozott szürke réteg
- alapkőzet: alapkőzet
- forrás 7: Talajszelvények: vázlatos, tankönyvi ismeret alapján; a humuszréteg vastagsága tájanként változik

### Adatok
<!-- forrás (az alábbiakra): magyar tankönyvi értékek nagyságrendje (pl. Stefanovits P.: Talajtan; NKP Földrajz 9 – ellenőrizendő); a valódi vastagság tájanként és szelvényenként tág határok között változik, ezért mind becslés -->
- vörösföld humuszrétege: kb. 5–15 cm
- váztalaj humuszrétege: kb. 0–5 cm
- csernozjom humuszrétege: kb. 60–100 cm
- barna erdőtalaj humuszrétege: kb. 20–40 cm
- podzol humuszrétege: kb. 5–10 cm
- tundratalaj humuszrétege: kb. 5–10 cm

## 8. Függőleges övezetesség
Felfelé 100 méterenként {függőleges lehűlés}-ot hűl a levegő, ezért a hegyen is övek követik egymást: ez a **függőleges övezetesség**. Az **erdőhatár** fölött nem nő fa, a **hóhatár** fölött nyáron sem olvad el a hó. ==Az Egyenlítőhöz közel mindkettő magasabban van==.

> megjegyzés: Tévhit: a hóhatár mindenütt egyforma magasan van.

### Feliratok
- cím 8: Növényövek a hegyen
- gomb Kilimandzsáró: Kilimandzsáró
- gomb Alpok: Alpok
- gomb Tátra: Tátra
- Kilimandzsáró: Kilimandzsáró (Kibo, 3° D)
- Alpok: Alpok (Mont Blanc, 46° É)
- Tátra: Magas-Tátra (Gerlachfalvi-csúcs, 49° É)
- csúcs: # m
- erdőhatár: erdőhatár
- hóhatár: hóhatár
- nincs hóhatár: állandó hóhatár nincs: a csúcs alacsonyabb
- csúszka magasság: Hegymászó magassága
- csúszka m: # m
- hidegebb: a hegylábnál # °C-kal hidegebb
- most öv: itt: #
- magasság tengely: magasság
- összevetés cím: Erdőhatár és hóhatár
- öv K1: szavanna és ültetvények
- öv K2: hegyi esőerdő
- öv K3: hanga- és lápvidék
- öv K4: magashegyi sivatag
- öv K5: jég és hó
- öv A1: lombos erdő (bükk, tölgy)
- öv A2: tűlevelű erdő (luc, vörösfenyő)
- öv A3: törpecserjés, havasi rét
- öv A4: sziklás, örök hó
- öv T1: lombos erdő (bükk)
- öv T2: lucfenyves
- öv T3: törpefenyő
- öv T4: havasi rét
- öv T5: sziklás csúcsrégió
- forrás 8: Hegyprofil és övhatárok: vázlatos, tankönyvi és szakirodalmi kb.-értékek (NASA Earth Observatory, Kilimandzsáró)

### Adatok
- függőleges lehűlés: kb. 0,6 °C
<!-- forrás: tankönyvi átlagérték (a mért 0,5–0,65 °C/100 m között; a nemzetközi standard légkör 0,65 °C/100 m, lásd 04-felhokepzodes) -->
<!-- forrás (az alábbiakra): Kilimandzsáró – NASA Earth Observatory: „The Zones of Kilimanjaro” (2017; hegyi erdő kb. 1800–2800 m, hanga- és lápvidék kb. 4000 m-ig, fölötte magashegyi sivatag), UNESCO/IUCN World Heritage Outlook (öt növényöv); lekérdezve: 2026-11-24. A csúcs 5895 m (tanzániai hivatalos érték). A hóhatár „kb. 5000 m”: a terv irányértéke az Egyenlítő környékére (4800–5000 m); a Kibo gleccserei ma már csak a csúcsplatón maradtak meg és gyorsan fogynak – szakmai review! -->
- Kilimandzsáró csúcsa: 5895 m
- Kilimandzsáró lába: kb. 900 m
- Kilimandzsáró öv 1 felső: kb. 1800 m
- Kilimandzsáró erdőhatár: kb. 2800 m
- Kilimandzsáró öv 3 felső: kb. 4000 m
- Kilimandzsáró hóhatár: kb. 5000 m
<!-- forrás (az alábbiakra): Alpok, északi oldal – a terv irányértékei (erdőhatár kb. 1800–2200 m, hóhatár kb. 2700–3000 m), tankönyvi értékek; a Mont Blanc magassága a 2023-as francia mérés szerint 4805,59 m (évente változik a hósapka miatt), kerekítve. Ellenőrizendő a NKP Földrajz 9 tankönyvvel. -->
- Alpok csúcsa: 4806 m
- Alpok lába: kb. 500 m
- Alpok öv 1 felső: kb. 1400 m
- Alpok erdőhatár: kb. 2000 m
- Alpok hóhatár: kb. 2800 m
<!-- forrás (az alábbiakra): Magas-Tátra – Gerlachfalvi-csúcs 2655 m (szlovák hivatalos érték 2654,4 m); a felső erdőhatár kb. 1500–1550 m, a törpefenyő-öv felső határa kb. 1800–1850 m, a havasi (alpin) öv kb. 2300 m-ig, fölötte a szubnivális öv (IntechOpen-fejezet a Tátra növényöveiről; GLORIA-hálózat; lekérdezve: 2026-11-24 – ellenőrizendő). Gleccser és állandó hóhatár nincs. -->
- Tátra csúcsa: 2655 m
- Tátra lába: kb. 700 m
- Tátra öv 1 felső: kb. 1250 m
- Tátra erdőhatár: kb. 1550 m
- Tátra öv 3 felső: kb. 1800 m
- Tátra öv 4 felső: kb. 2300 m

## 9. Összefoglalás
A napsugárzás szélességenként és évszakonként más: ebből jön a **szoláris** övezetesség. A **valódi** éghajlatot a tenger és a szárazföld, a tengeráramlások, a szél és a domborzat módosítja. ==A növényzet és a talaj az éghajlatot követi==, a hegyeken pedig a magassággal ismétlődik az övsor.

> megjegyzés: Egy év adata időjárás, harminc év átlaga éghajlat.

### Feliratok
- honnan típus: Honnan tudjuk?
- honnan cím: Klímanormák: 30 év átlaga
- honnan mivel: Mit mérnek?
- honnan mivel v: hőmérséklet 2 m-en árnyékban, csapadék
- honnan mikor: Milyen gyakran?
- honnan mikor v: naponta, sok állomáson óránként
- honnan mit: Mit mutat a diagram?
- honnan mit v: az 1991–2020 közötti 30 év átlagát
- honnan ki: Ki gyűjti?
- honnan ki v: a WMO, az országok mérőhálózataiból
- ö 1: A napsugarak hajlásszöge szélességenként és évszakonként más.
- ö 2: Öt szoláris öv: forró, két mérsékelt, két hideg.
- ö 3: A tenger mérsékel: kisebb a hőingás.
- ö 4: Meleg áramlás enyhít, hideg áramlás mellett sivatag lehet.
- ö 5: A növényzet és a talaj követi az öveket.
- ö 6: A hegyen felfelé hasonló övsor ismétlődik.

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - Az övek rendszere (forró: egyenlítői, átmeneti, térítői öv; mérsékelt: meleg mérsékelt, valódi mérsékelt,
    hideg mérsékelt öv; hideg: sarkköri, sarki öv) a magyar tankönyvi felosztást követi – a NKP Földrajz 9
    tankönyvvel egyeztetendő. A 6. lépés hat diagramja egy-egy jellegzetes állomás, nem „az öv átlaga”.
  - A napsugárzás-számolás a légkör tetejére vonatkozik (nincs felhő, elnyelés, fénytörés, a Föld–Nap távolság
    változása), a nappal hossza a Nap középpontjára számolt csillagászati érték (a valódi kb. 5–10 perccel hosszabb).
    A napéjegyenlőség és a napforduló napja a modellben kerekített (március 21., június 21.).
  - A „száraz hónap” jelölése a Walter-féle hüvelykujjszabály (P < 2 · T, mm és °C); valódi vízmérleghez a
    párolgást kellene mérni.
  - A tengeráramlások vonala vázlatos; a „Golf-áramlás egyedül fűti Európát” tévhitet a panel a nyugatias szél
    szerepével árnyalja (a szakirodalomban vitatott az óceáni és a légköri hőszállítás aránya: Seager et al. 2002).
  - Iqaluit hidegségében a hideg tenger mellett a kanadai szárazföld felől fújó szél is szerepet játszik.
  - A talajszelvények vázlatosak; a magyar talajtani elnevezések (mezőségi talaj, barna erdőtalaj, podzol,
    vörösföld) tankönyvenként kissé eltérnek.
  - A hegyek övhatárai kb.-értékek, lejtőnként (északi/déli, nedves/száraz oldal) akár több száz méterrel
    eltérnek; a hegyprofil stilizált (nem valódi domborzati szelvény).
-->
