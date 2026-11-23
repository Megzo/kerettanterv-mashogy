# Honnan fúj a passzát? – a földi légkörzés és a monszun
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 3. A légkör

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/05-legkorzes.md
  A számok az animációt is vezérlik (pl. a cellahatárok, az esőöv helyzete, Mumbai csapadéka,
  a trópusi ciklon feltételei). A szélmező IDEALIZÁLT MODELL (nem mért adat): a háromcellás kép
  zárt képletből számolódik, az esőöv helyzetét az alábbi „esőöv …” adatok adják.
-->

## Közös

### Feliratok
- modell: modell
- vázlatos: vázlatos
- becslés: becslés
- torzítás: függőleges torzítás #×
- lassú: gyenge szél
- gyors: erős szél
- forrás gömb: Szélmező: idealizált háromcellás modell, nem mért adat · Made with Natural Earth
- M: M
- A: A
- magas nyomás: magas nyomás
- alacsony nyomás: alacsony nyomás
- Egyenlítő: Egyenlítő

### Adatok
<!-- forrás (az alábbiakra): közismert -->
- átlagos légnyomás: 1013 hPa
<!-- forrás: a tengerszinti normál légnyomás 1013,25 hPa (ISO 2533 standard légkör), közismert -->
- egy fordulat ideje: 86 164 s
<!-- forrás: csillagnap = 23 óra 56 perc 4 s, közismert; ebből Ω = 2π / 86 164 s = 7,292 · 10⁻⁵ 1/s (a terv adata) -->
- Budapest helye: 47,50° É, 19,04° K
<!-- forrás: közismert (Budapest belváros); a lecke a szélességet használja (Coriolis-paraméter) és a térképen jelöli -->
- Hadley-cella határa: 30° (modell)
<!-- forrás: idealizált háromcellás modell (terv 05-ös brief, „Adatok”); a valódi térítői magasnyomású öv évszakonként kb. 25–35° között van -->
- sarki front helye: 60° (modell)
<!-- forrás: idealizált modell (terv); a valódi sarki front naponta és évszakonként 40–70° között hullámzik -->
- troposzféra az Egyenlítőnél: kb. 16 km
<!-- forrás: tankönyvi érték (a troposzféra vastagsága az Egyenlítő fölött 16–18 km, a sarkok fölött 8–9 km), közismert -->
- troposzféra a sarkoknál: kb. 8 km
<!-- forrás: lásd fent, közismert -->
<!-- forrás (az alábbiakra): az esőöv (egyenlítői összeáramlási öv, ITCZ) a modellben; a terv briefje: „júliusban Dél-Ázsia fölött 20–25° É-ig is feljut, januárban a déli félgömbi kontinensek fölött kb. 10–15° D-ig húzódik (kb.)”; a zonális átlag évi középhelyzete kb. 6° É (Schneider, Bischoff, Haug 2014, Nature 513, 45–53). A közbülső hónapokban a modell koszinuszosan interpolál (április és október a középhelyzet). -->
- esőöv júliusban az óceánok fölött: 10° (modell)
- esőöv januárban az óceánok fölött: 3° (modell)
- esőöv júliusban Afrika és Közép-Amerika fölött: 15° (modell)
- esőöv júliusban Dél-Ázsia fölött: 25° (modell)
<!-- a brief 20–25° É-t ad; a monszunvályú júliusban nagyjából Északnyugat-Indiától a Bengáli-öböl északi részéig, kb. 22–28° É között húzódik (IMD monszun-klimatológia, tankönyvi ábrák) – a modell a felső értéket használja, hogy Mumbai (19° É) a délnyugati áramlásba essen. -->
- esőöv januárban a déli kontinensek fölött: 13° (modell)

## 1. Miért fúj a szél?
Ahol a levegő felmelegszik és felszáll, ott a felszínen kisebb a nyomás. A **szél** a nagyobb nyomású hely felől a kisebb felé áramlik. Az **izobár** az azonos nyomású pontokat köti össze.

==Minél sűrűbbek az izobárok, annál erősebb a szél.==

> megjegyzés: Mélyítsd a csúszkával az „A” központot! Modell: itt a Föld még nem forog.

### Feliratok
- térkép cím: Vázlatos időjárási térkép
- izobár: izobár (# hPa-onként)
- nyomáskülönbség: nyomáskülönbség: # hPa
- középnyomás: # hPa
- csúszka A nyomás: Az „A” központ nyomása
- csúszka hPa: # hPa
- forrás térkép: Modell: kitalált nyomásmező, nem valódi időjárási helyzet
- felszáll: itt a levegő felszáll

### Adatok
<!-- forrás (az alábbiakra): modellparaméterek a kitalált térképhez; a valódi anticiklonok jellemzően 1020–1040 hPa, a mérsékelt övi ciklonok 970–1005 hPa középnyomásúak (közismert) -->
- anticiklon középnyomása: 1030 hPa (modell)
- kezdő A nyomás: 990 hPa (modell)
- legsekélyebb A nyomás: 1005 hPa (modell)
- legmélyebb A nyomás: 975 hPa (modell)
- izobárköz: 4 hPa
<!-- forrás: a szinoptikus (időjárási) térképek szokásos 4 vagy 5 hPa-os izobárköze, közismert -->

## 2. A körhinta és a lefolyó
Kívülről nézve a labda egyenesen gurul, de a forgó körhintáról nézve ==jobbra kanyarodik==. A Föld is forog alattunk: ez a **Coriolis-hatás**. Az északi félgömbön jobbra, a délin balra térít.

Tévhit: ettől örvénylik a lefolyó? Nem! A víz {lefolyó ideje} alatt ér a nyílásig, ennyi idő alatt alig fordul. A szél órákig fúj.

### Feliratok
- kívülről: kívülről nézve
- körhintáról: a körhintáról nézve
- egyenes: egyenes pálya
- kanyarodik: jobbra kanyarodik
- nem kanyarodik: nem kanyarodik
- forgásirány: így forog az északi félgömb is, felülről nézve
- csúszka körhinta: A körhinta forgása
- csúszka °/s: # °/s
- lefolyó cím: Mennyit fordít a Coriolis-hatás az irányon? (Budapest)
- időtengely: 1 s; 10 s; 1 perc; 10 perc; 1 óra; 12 óra
- lefolyó: lefolyó
- szél: szél
- elfordulás: elfordulás: #°
- eredeti irány: eredeti irány
- csúszka idő: Mennyi ideig mozog?
- forrás körhinta: Számolás: elfordulás = 2 · Ω · sin φ · t (Ω: a Föld forgási szögsebessége, φ: szélesség)

### Adatok
- körhinta kezdő forgása: 30 °/s (modell)
<!-- forrás: modellparaméter (a rajz kedvéért gyors körhinta) -->
- lefolyó ideje: kb. 3 s
<!-- forrás: becslés – ennyi idő alatt ér a víz a mosdó széléről a lefolyóig; a hatás ennyi idő alatt 2 · Ω · sin 47,5° · 3 s ≈ 0,02°. A Coriolis-hatás gondos kísérletben, egy napig nyugalomban hagyott nagy kádban kimutatható (A. H. Shapiro, Nature 196, 1080–1081, 1962), a hétköznapi mosdóban nem: ott a víz maradék mozgása és a medence alakja dönt. -->
- szél ideje: 1 óra
<!-- forrás: példa; 1 óra alatt 2 · Ω · sin 47,5° · 3600 s ≈ 0,387 rad ≈ 22° (a lecke számolja) -->
- leghosszabb idő: 12 óra
<!-- forrás: a tengely vége (példa) -->

## 3. Ciklon és anticiklon
A Coriolis-hatás miatt a szél nem egyenesen fúj be az alacsony nyomású **ciklon** közepébe: az északi félgömbön ==az óramutatóval ellentétesen örvénylik be==. A magas nyomású **anticiklon** közepéből az óramutató járásával egyezően áramlik ki.

> megjegyzés: Válts déli félgömbre! A súrlódás miatt a szél ferdén metszi az izobárokat; tengeren kisebb a szög.

### Feliratok
- északi félgömb: északi félgömb
- déli félgömb: déli félgömb
- gomb déli: Déli félgömb
- gomb északi: Északi félgömb
- ciklon: ciklon
- anticiklon: anticiklon
- ciklon forgás É: befelé, az óramutatóval ellentétesen
- ciklon forgás D: befelé, az óramutató járásával egyezően
- anticiklon forgás É: kifelé, az óramutató járásával egyezően
- anticiklon forgás D: kifelé, az óramutatóval ellentétesen
- szög: #° az izobárhoz
- csúszka súrlódás: A súrlódás szöge (tenger ↔ szárazföld)
- csúszka szög: #°

### Adatok
- ciklon középnyomása: 990 hPa (modell)
<!-- forrás: modellparaméter -->
- legkisebb súrlódási szög: 10°
<!-- forrás: a terv briefje: a súrlódás miatt a felszíni szél kb. 10–45°-os szögben metszi az izobárokat, tengeren kisebb, szárazföldön nagyobb szögben (kb.); tankönyvi érték -->
- legnagyobb súrlódási szög: 45°
<!-- forrás: lásd fent -->
- kezdő súrlódási szög: 30° (modell)
<!-- forrás: modellparaméter -->

## 4. Ha a Föld nem forogna
A Nap az Egyenlítő környékét melegíti a legjobban. Ott a levegő felszáll, a hideg sarkokon lesüllyed. Ha a Föld nem forogna, félgömbönként ==egyetlen nagy körforgás== volna: a felszínen a szél egyenesen a sarkoktól az Egyenlítő felé fújna.

> megjegyzés: Indítsd el a forgást! A modellben a körforgás három cellára bomlik.

### Feliratok
- gomb forgás be: Forogjon a Föld!
- gomb forgás ki: Álljon meg a Föld!
- felszáll meleg: meleg levegő felszáll
- leszáll hideg: hideg levegő leszáll
- északi szél: északi szél
- déli szél: déli szél
- egy cella: forgás nélkül: egy cella
- három cella: forgással: három cella
- troposzféra teteje: a troposzféra teteje

## 5. Passzát, nyugatias és sarki szél
A felszálló levegő kb. {Hadley-cella határa}-nál leszáll: itt száraz, magas nyomású öv húzódik, sivatagokkal. Innen fúj a **passzátszél** az Egyenlítő felé, és a **nyugatias szél** a sarkok felé. A sarkok felől a **sarki szél** fúj.

==A felszálló levegő hűl: felhő és eső lesz belőle.==

> megjegyzés: Modell: a szárazföldek és az évszakok hatását itt elhagytuk.

### Feliratok
- Hadley-cella: Hadley-cella
- Ferrel-cella: Ferrel-cella
- sarki cella: sarki cella
- gomb Hadley: Hadley-cella
- gomb Ferrel: Ferrel-cella
- gomb sarki: Sarki cella
- gomb mind: Mind
- ÉK passzát: északkeleti passzát
- DK passzát: délkeleti passzát
- nyugatias: nyugatias szelek
- sarki szél: sarki szél
- öv esőöv: egyenlítői esőöv
- öv száraz: térítői száraz öv
- öv front: sarki front
- Szahara: Szahara
- Kalahári: Kalahári
- Arab-sivatag: Arab-sivatag
- húzd: húzd a gömböt

## 6. Miért változékony nálunk az idő?
Magyarország a nyugatias szelek övében fekszik, ahol a hideg sarki és a meleg trópusi levegő találkozik. A határukon ciklonok születnek, és a széllel ==keletre vonulnak==. Ahol a hideg levegő nyomul előre, ott **hidegfront** van, ahol a meleg, ott **melegfront**. Ezért pár naponta változik az idő.

> megjegyzés: Figyeld Budapestet!

### Feliratok
- hideg levegő: hideg sarki levegő
- meleg levegő: meleg trópusi levegő
- hidegfront: hidegfront
- melegfront: melegfront
- Budapest: Budapest
- Budapest hideg: Budapest: hideg levegő
- Budapest meleg: Budapest: meleg levegő
- nap: #. nap
- napok: nap
- idősor: Budapest, napról napra
- vonulás: a ciklonok kb. # km/h-val vonulnak keletre
- gomb szünet: Megállítás
- gomb tovább: Tovább
- forrás front: Mérsékelt övi ciklonok: idealizált modell (egyetlen frontrendszer-hullám) · Made with Natural Earth

### Adatok
<!-- forrás (az alábbiakra): modellparaméterek, a tankönyvi nagyságrendhez igazítva (a mérsékelt övi ciklonok jellemzően 30–50 km/h-val vonulnak, egy-egy hullám néhány ezer km; a frontok Budapesten átlagosan néhány naponta követik egymást) -->
- ciklonok vonulási sebessége: kb. 30 km/h (modell)
- hullámhossz: kb. 3000 km (modell)
- nyugatias szél sebessége: kb. 10 m/s (modell)

## 7. A vándorló esőöv és a monszun
Az esőöv a Nappal együtt vándorol. Nyáron Dél-Ázsia szárazföldje jobban felmelegszik, mint a tenger, ezért az esőöv itt {esőöv júliusban Dél-Ázsia fölött}-ig húzódik. A déli passzát átkel az Egyenlítőn, jobbra térül, és ==délnyugatról nedves óceáni levegőt hoz==: ez a nyári **monszunszél**. Télen a szél megfordul.

### Feliratok
- hónapnevek: január, február, március, április, május, június, július, augusztus, szeptember, október, november, december
- hónap-betűk: J, F, M, Á, M, J, J, A, Sz, O, N, D
- csúszka hónap: Hónap
- esőöv: esőöv
- Mumbai: Mumbai
- nyári monszun: nyári monszun (délnyugati)
- téli monszun: téli monszun (északkeleti)
- meleg szárazföld: felmelegedett szárazföld
- hideg szárazföld: kihűlt szárazföld
- grafikon cím: Mumbai havi csapadéka
- grafikon évi: évi # mm, ebből jún.–szept. # %
- mm érték: # mm
- forrás monszun: Csapadék: IMD, Mumbai (Santacruz), 1991–2020 · szélmező: idealizált modell · Made with Natural Earth

### Adatok
- Mumbai helye: 19,09° É, 72,85° K
<!-- forrás: Santacruz meteorológiai állomás (Mumbai repülőtér), közismert koordináta -->
- Mumbai havi csapadéka: 0,2; 0,2; 0,1; 0,1; 7,3; 526,3; 919,9; 560,8; 383,5; 91,3; 11,0; 1,6 mm
<!-- forrás: India Meteorological Department (IMD), Climatological Normals 1991–2020, Mumbai (Santacruz) – az en.wikipedia.org/wiki/Climate_of_Mumbai táblázata alapján (IMD-re hivatkozik), lekérdezve: 2026-11-23; az eredeti IMD-kiadvánnyal egyeztetendő. A terv „kb. 90 %” értéke helyett az adatból jún.–szept. 95,5 % jön ki (Colaba: 95,0 %). -->
- Mumbai évi csapadéka: 2502,3 mm
<!-- forrás: ugyanott (a havi értékek összege; a lecke ellenőrzi) -->
- kezdő hónap: 7
<!-- forrás: a csúszka kezdőértéke (július) -->

## 8. Hurrikán, tájfun, ciklon
A **hurrikán**, a **tájfun** és a trópusi ciklon ugyanaz: hatalmas örvény a trópusi óceán fölött, csak más-más néven. Legalább {trópusi ciklon vízhőmérséklete}-os vízen alakul ki, és ==az Egyenlítőtől {legkisebb távolság az Egyenlítőtől}-on belül szinte soha==: ott nincs eltérítés, ami megforgatná.

> megjegyzés: A **tornádó** más: néhány száz méteres forgószél zivatarfelhő alatt.

### Feliratok
- hurrikán: hurrikán
- tájfun: tájfun
- trópusi ciklon: ciklon
- nincs eltérítés: nincs eltérítés
- kialakulás helye: a trópusi ciklonok fő kialakulási területei
- itt: itt próbáljuk
- feltétel víz: a víz legalább # °C-os
- feltétel szélesség: legalább #°-ra az Egyenlítőtől
- most víz: most: # °C
- most szélesség: most: #
- kialakul: Kialakul a trópusi ciklon
- nem alakul ki: Nem alakul ki
- ok hideg: túl hideg a víz: kevés a párolgás
- ok Egyenlítő: nincs eltérítés, ami megforgatná
- forog É: az óramutatóval ellentétesen forog
- forog D: az óramutató járásával egyezően forog
- szem: a ciklon szeme
- csúszka szélesség: Földrajzi szélesség
- szélesség É: #° É
- szélesség D: #° D
- szélesség 0: 0° (Egyenlítő)
- csúszka víz: A tengervíz hőmérséklete
- csúszka °C: # °C
- forrás hurrikán: Kialakulási területek: vázlatos, tankönyvi ismeret alapján · az örvény: modell · Made with Natural Earth

### Adatok
- trópusi ciklon vízhőmérséklete: 26,5 °C
<!-- forrás: NOAA AOML Hurricane Research Division, Tropical Cyclone FAQ (aoml.noaa.gov/hrd-faq), a W. M. Gray (1968) óta használt küszöb: legalább 26,5 °C-os tengervíz kb. 50 m mélységig; lekérdezve: 2026-11-23 (ellenőrizendő URL) -->
- legkisebb távolság az Egyenlítőtől: kb. 5°
<!-- forrás: a terv briefje; tankönyvi érték. Kivétel ritkán akad: a Vamei tájfun 2001-ben é. sz. 1,4°-nál alakult ki (NOAA/JTWC), ezért a panel „szinte soha”-t mond -->
- kezdő szélesség: 15° (modell)
<!-- forrás: a csúszka kezdőértéke -->
- kezdő vízhőmérséklet: 28 °C (modell)
<!-- forrás: a csúszka kezdőértéke -->

## 9. Összefoglalás
A szél a magas nyomás felől az alacsony felé fúj, és a Coriolis-hatás eltéríti. Így áll össze a három cella: passzát, nyugatias és sarki szél. ==Az egész rendszer a Nappal együtt vándorol==: ebből lesz a monszun.

> megjegyzés: A háromcellás kép a sokéves mérések átlagából kirajzolódó modell. Egy adott napon a szél sokban eltér tőle.

### Feliratok
- honnan típus: Honnan tudjuk?
- honnan cím: Mérőhálózat és modell
- honnan mivel: Mivel mérik?
- honnan mivel v: állomások, hajók, rádiószondák, műholdak
- honnan mikor: Milyen gyakran?
- honnan mikor v: óránként; szondák naponta kétszer (00 és 12 UTC)
- honnan mit: Mit mutat a lecke?
- honnan mit v: a sokéves átlagot, egyszerűsítve
- ö 1: A szél a magas nyomás felől az alacsony felé fúj.
- ö 2: A Coriolis-hatás északon jobbra, délen balra téríti.
- ö 3: Három cella: passzát, nyugatias szél, sarki szél.
- ö 4: A felszálló levegőből eső, a leszállóból sivatag lesz.
- ö 5: Az esőöv vándorol: ebből lesz a monszun.
- ö 6: Nálunk a nyugatias szelek ciklonokat és frontokat hoznak.

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - A szélmező idealizált, zárt képletű modell (három cella, szinuszos meridionális komponens, a szélességgel
    növekvő eltérítés, kb. 65° az eredeti iránytól); NCEP/NCAR valódi szél nincs a leckében (a shared/foldrajz/README
    szerint csak netCDF-ben érhető el). A szélsebességek (passzát kb. 7, nyugatias kb. 8, sarki kb. 4 m/s) kódban
    rögzített modellparaméterek.
  - A „forgás nélkül egy cella, forgással három” a tankönyvi idealizált kép; a valóságban a Ferrel-cella csak az
    átlagban létezik, a mérsékelt övben a ciklonok és anticiklonok szállítják a hőt.
  - Az esőöv hónapról hónapra koszinuszosan vándorol a modellben; valójában a monszun hirtelen, júniusban „tör be”.
  - Mumbai csapadéka a Wikipédia IMD-táblázatából (1991–2020, Santacruz) – az IMD eredeti kiadványával egyeztetendő.
  - A 6. lépés frontrendszere egyetlen, állandó amplitúdójú hullám; a valódi ciklonok kialakulnak, mélyülnek és
    feltöltődnek, a frontok összezáródnak (okklúzió) – ezt a lecke nem mutatja.
  - A trópusi ciklon „kialakulási területei” vázlatosak (kézzel rajzolt foltok); a hurrikán-csúszka csak a két
    tankönyvi feltételt modellezi (vízhőmérséklet, eltérítés), a szélnyírást és a nedvességet nem.
  - A Coriolis-elfordulás képlete (2 · Ω · sin φ · t) a tehetetlenségi mozgásra érvényes (nyomási erő nélkül);
    nagyságrendi összevetésre jó.
-->
