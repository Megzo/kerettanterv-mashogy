# Hogyan jut el az üzenet a barátodhoz? – csomag, cím, e-mail, felhő
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 2. Online kommunikáció

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/05-csomagok.md

  A „Tippelj!” lépésekben (1., 2. és 8.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  Anna, Bence, Csilla, a címek (…@pelda.example, RFC 2606), az IP-címek (dokumentációs tartomány,
  RFC 5737), a szerver helye és a városok közti hálózat KITALÁLT (valószerű) példa.
  A ## Közös feliratai: a „Tippelj! → kísérlet → magyarázat” sáv, a tipp-visszajelzés és a bélyegek
  (szerződés 17. és 19.) – a sorozat minden leckéjében ugyanígy szerepelnek.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- modell bélyeg: modell
- lassítva bélyeg: lassítva
- kitalált bélyeg: kitalált példa
- vázlatos bélyeg: vázlatos
- nem méretarányos bélyeg: nem méretarányos
- anna monogram felirat: An
- anna név felirat: Anna
- bence monogram felirat: Be
- bence név felirat: Bence
- csilla monogram felirat: Cs
- csilla név felirat: Csilla
- szerver felirat: szerver
- szerver alcím felirat: a szolgáltató gépe
- budapest felirat: Budapest
- bécs felirat: Bécs
- prága felirat: Prága
- zágráb felirat: Zágráb
- münchen felirat: München
- nürnberg felirat: Nürnberg
- frankfurt felirat: Frankfurt
- new york felirat: New York
- fotó felirat: fotó

### Adatok
- Budapest helye: 47,50° É, 19,04° K
<!-- forrás: Budapest (Lánchíd környéke), 47° 29′ 52″ É, 19° 02′ 25″ K – kerekítve; a térkép és a távolságszámítás pontja -->
- Frankfurt helye: 50,11° É, 8,68° K
<!-- forrás: Frankfurt am Main belvárosa, 50° 06′ 39″ É, 8° 40′ 55″ K – kerekítve. A szerver helye kitalált, valószerű példa
     (Frankfurt környékén sok adatközpont és internetes csomópont van). -->
- New York helye: 40,71° É, 74,01° Ny
<!-- forrás: New York (Manhattan déli csücske), 40° 42′ 46″ É, 74° 00′ 22″ Ny – kerekítve -->
- csomag legnagyobb adatmérete: 1500 bájt
<!-- forrás: IEEE 802.3 (Ethernet) – egy keret adatmezője legfeljebb 1500 bájt (MTU). Ebből a csomag saját fejlécei
     (IPv4: 20 bájt, TCP: 20 bájt) még levonódnak, ezért a valódi csomagszám valamivel több: 3 000 000 / 1460 ≈ 2055.
     A lecke „kb.”-t ír. -->

## 1. Merre megy a fotó?
Anna fotót küld Bencének, aki a szomszéd utcában lakik. ==Merre megy a fotó? Tippelj!==

Nem egyenesen! Először a szolgáltató **szerverére** megy – ez egy mindig bekapcsolt gép, akár másik országban. Útközben **útválasztók** adják tovább. Onnan jut el Bencéhez.

> megjegyzés: A szerver helye itt kitalált, de valószerű.

### Feliratok
- útvonal kérdés felirat: Anna fotót küld Bencének a szomszéd utcába. Merre megy?
- egyenesen tipp: egyenesen Bence telefonjára
- szerveren tipp: szerveren át, akár külföldön
- műholdon tipp: műholdon át
- szomszéd felirat: szomszéd utca
- oda felirat: oda
- vissza felirat: vissza
- egyenesen tévhit felirat: Egyenesen Bence telefonjára megy?
- egyenesen válasz felirat: Nem: szerveren át, akár külföldön.
- megérkezett felirat: megérkezett!

## 2. Csomagokra bontva
A fotó nem egyben utazik. ==Hány csomag lesz egy {fotó mérete}-os fotóból? Tippelj!==

A gép **csomagokra** vágja: egybe legfeljebb kb. {csomag legnagyobb adatmérete} fér. Minden csomagon ott a **cím** (honnan, hová) és a **sorszám**. A cím négy szám 0 és 255 között: négy bájt.

> megjegyzés: Próbáld ki a gombokat!

### Feliratok
- csomagszám kérdés felirat: Egy #-os fotó hány csomag?
- kettő tipp: kb. 2
- kétszáz tipp: kb. 200
- kétezer tipp: kb. 2000
- üzenet gomb: „Szia!” üzenet (#)
- kis kép gomb: kis kép (#)
- fotó gomb: fotó (#)
- méret felirat: # = # bájt
- osztás felirat: # bájt : # bájt ≈ #
- csomagok felirat: # csomag
- egy csomag felirat: egy csomag nagyítva
- feladó felirat: feladó
- feladó alcím felirat: Anna telefonja
- címzett felirat: címzett
- címzett alcím felirat: a szerver
- sorszám felirat: sorszám
- adat felirat: adat
- adat méret felirat: # bájt
- négy bájt felirat: a cím 4 bájt:
- szia felirat: Szia!

### Adatok
- Anna telefonjának címe: 198; 51; 100; 23
<!-- forrás: kitalált példa – IPv4-cím a dokumentációs tartományból (RFC 5737: 198.51.100.0/24); a lecke pontokkal
     írja ki: 198.51.100.23. Négy szám 0 és 255 között = 4 bájt. -->
- a szerver címe: 203; 0; 113; 80
<!-- forrás: kitalált példa – IPv4-cím a dokumentációs tartományból (RFC 5737: 203.0.113.0/24) → 203.0.113.80 -->
- fotó mérete: 3 MB
<!-- forrás: becslés – egy 12 megapixeles telefonfotó JPEG-ben tipikusan 2–5 MB; a sorozatban (17-szamitogep) is 3 MB -->
- kis kép mérete: 100 kB
<!-- forrás: kitalált példa – egy kicsinyített, üzenetbe küldött kép nagyságrendje -->
- üzenet mérete: 5 bájt
<!-- forrás: számolt – a „Szia!” 5 jel, mind ASCII → 5 bájt UTF-8-ban (a sorozat 17-szamitogep leckéje szerint) -->

## 3. Ha elvágják az utat
A csomagok nem egy úton mennek: minden **útválasztó** maga küldi tovább. ==Összekeverve érkeznek==, de a cél a **sorszám** szerint sorba rakja őket. Kattints egy kábelre, és vágd el! Az elveszett csomagot a gép **újra kéri**.

> megjegyzés: A hálózat kitalált modell.

### Feliratok
- vágás felirat: Kattints egy kábelre, és vágd el!
- érkezés felirat: így érkeztek:
- sorrend felirat: sorba rakva:
- újrakérés felirat: hiányzik a #. – újra kéri
- elveszett felirat: elveszett
- nincs út felirat: Nincs út! A csomagok várnak.
- összeállt felirat: A fotó összeállt!
- küldés gomb: Küldd újra a fotót!
- javítás gomb: Minden kábel helyre
- hálózat tévhit felirat: Az internet egyetlen nagy kábel?
- hálózat válasz felirat: Nem: kábelek hálója – van kerülőút.

## 4. Milyen gyors?
Az adat **üvegszálban**, fényként halad: {fény sebessége üvegszálban}. Az óceán alatt **tenger alatti kábel** viszi át. Válassz célt, és figyeld az órát! ==1 ms (ezredmásodperc) a másodperc ezredrésze.==

> megjegyzés: A valódi út hosszabb a légvonalnál, ezért a mért idő több.

### Feliratok
- frankfurt gomb: Frankfurt
- new york gomb: New York
- műhold gomb: műholdon át
- légvonal felirat: légvonalban: # km
- számítás felirat: # km : # km/s ≈ # ms
- műhold számítás felirat: fel és le: 2 · # km : # km/s ≈ # ms
- egy irányban felirat: egy irányban
- tengeri kábel felirat: tenger alatti kábelek
- műhold felirat: távközlési műhold
- műhold sáv felirat: műholdon át
- műhold tévhit felirat: Az internet műholdon megy?
- műhold válasz felirat: Főleg kábelen: földön és tenger alatt.
- térkép forrás felirat: a kábelek helye vázlatos – forrás: TeleGeography kábeltérkép

### Adatok
- fény sebessége üvegszálban: kb. 200 000 km/s
<!-- forrás: becslés – a fény sebessége légüres térben 299 792 km/s; az üvegszál törésmutatója kb. 1,46–1,5, így
     299 792 / 1,47 ≈ 204 000 km/s → kerekítve kb. 200 000 km/s (ITU-T G.652 szálak, tankönyvi érték) -->
- fény sebessége légüres térben: kb. 300 000 km/s
<!-- forrás: SI – c = 299 792 458 m/s, kerekítve -->
- távközlési műhold magassága: 35 786 km
<!-- forrás: a geostacionárius pálya magassága az Egyenlítő fölött kb. 35 786 km (NASA / ESA). A számítás a földfelszíntől
     egyenesen fel és le méri (a valódi ferde út kicsit hosszabb). -->

## 5. Hol marad másolat?
Az **e-mail** és a csevegőüzenet is a szolgáltató **szerverén** át megy, és ott **másolat** marad. ==Ha Anna törli, csak a saját példánya tűnik el.== Bencénél és a szerveren megmarad. Próbáld ki!

> megjegyzés: A szerveren is törölhető – de amit Bence elmentett, továbbküldött, az megmarad.

### Feliratok
- levél feladó felirat: Feladó: anna@pelda.example
- levél címzett felirat: Címzett: bence@pelda.example
- levél tárgy felirat: Tárgy: Kirándulás képei
- levél szöveg felirat: Szia Bence! Küldöm a képeket a kirándulásról. Anna
- levél melléklet felirat: kirandulas.jpg
- elküldött felirat: Anna: elküldött levelek
- beérkezett felirat: Bence: beérkezett levelek
- csilla beérkezett felirat: Csilla: beérkezett
- másolat felirat: másolat
- másolatok felirat: másolatok száma: #
- törölve felirat: törölve
- törlés gomb: Anna törli a levelet
- továbbküldés gomb: Bence továbbküldi Csillának
- újra gomb: Újra az elejéről
- törlés tévhit felirat: A törölt üzenet mindenhonnan eltűnik?
- törlés válasz felirat: Nem: csak a te példányod.

## 6. A felhő – ki éri el?
A **felhő** nem az égen van: egy **adatközpont** gépein tárolt mappa. Anna megosztja Bencével. A **jogosultság** dönti el, ki mit tehet. ==A link annak is működhet, akinek továbbküldték!== Próbáld ki a gombokat!

### Feliratok
- felhő mappa felirat: Osztálykirándulás
- adatközpont felirat: adatközpont
- adatközpont alcím felirat: sok szerver egy épületben
- megtekintés gomb: Bence csak megtekintheti
- szerkesztés gomb: Bence szerkesztheti
- link gomb: bárki, akinél a link van
- tulajdonos felirat: tulajdonos
- meghívott felirat: meghívott
- továbbküldve felirat: Bence továbbküldte neki a linket
- ismeretlen név felirat: ismeretlen
- ismeretlen alcím felirat: a link egy csoportba került
- megnézheti felirat: megnézheti
- szerkesztheti felirat: szerkesztheti
- nem éri el felirat: nem éri el
- felhő tévhit felirat: A felhő a levegőben van?
- felhő válasz felirat: Nem: egy adatközpont gépein.
- link tévhit felirat: A link csak annak működik, akinek küldtem?
- link válasz felirat: Nem: akinél ott van, annak is működhet.

## 7. Futártól az ezredmásodpercig
Régen a levelet **futár** vagy **posta** vitte, napokig. A **távíró** {távíró éve} óta villanyárammal küldünk jelet. ==Az internet őse {ARPANET éve}-ben indult==, az e-mail {első e-mail éve}-ben, a **web** {web javaslat éve}-ben.

> megjegyzés: Frankfurt mellett, Mainzban nyomtatott Gutenberg 1450 körül.

### Feliratok
- idővonal cím felirat: Üzenetküldés régen és ma
- bc felirat: Kr. e.
- ad felirat: Kr. u.
- század felirat: század
- év felirat: # év
- távíró kártya: távíró (Morse)
- távíró megjegyzés felirat: Washington–Baltimore
- kábel kártya: tengeri távírókábel
- kábel megjegyzés felirat: Európa–Amerika, tartósan
- telefon kártya: telefon
- telefon megjegyzés felirat: Bell szabadalma
- hírmondó kártya: Telefonhírmondó
- hírmondó megjegyzés felirat: Puskás Tivadar, Budapest
- arpanet kártya: ARPANET – az internet őse
- arpanet megjegyzés felirat: négy gép kapcsolódott össze
- email kártya: e-mail – a @ jel
- email megjegyzés felirat: Ray Tomlinson
- web kártya: a web (WWW)
- web megjegyzés felirat: Tim Berners-Lee, CERN; nyilvános: #
- okostelefon kártya: érintőképernyős okostelefon
- okostelefon megjegyzés felirat: gyorsan elterjedt
- futár felirat: futár, posta: napok
- távíró sáv felirat: távíró: percek
- internet sáv felirat: internet: ezredmásodpercek

### Adatok
- távíró éve: 1844
<!-- forrás: Samuel Morse első nyilvános távíróüzenete Washington és Baltimore között, 1844. május 24. (Library of Congress) -->
- tengeri kábel éve: 1866
<!-- forrás: az első tartósan működő atlanti távírókábel, 1866 (az 1858-as kábel csak néhány hétig működött) – Britannica,
     „Atlantic cable”. Az első atlanti üvegszálas kábel (TAT-8) 1988-ban indult. -->
- telefon éve: 1876
<!-- forrás: Alexander Graham Bell telefonszabadalma, 1876. március 7. (US 174 465) -->
- Telefonhírmondó éve: 1893
<!-- forrás: Puskás Tivadar Telefonhírmondója Budapesten 1893. február 15-én indult (Magyar Elektrotechnikai Múzeum;
     Britannica) -->
- ARPANET éve: 1969
<!-- forrás: az ARPANET első üzenete 1969. október 29. (UCLA → SRI); 1969 végére négy csomópont (UCLA, SRI, UCSB, Utah) –
     Computer History Museum, Internet Society „Brief History of the Internet” -->
- első e-mail éve: 1971
<!-- forrás: Ray Tomlinson 1971-ben küldött először e-mailt két ARPANET-gép között, ő vezette be a @ jelet
     (Internet Hall of Fame; Raytheon BBN) -->
- web javaslat éve: 1989
<!-- forrás: Tim Berners-Lee javaslata a CERN-ben, 1989. március; a web 1991. augusztusban vált nyilvánossá (CERN,
     „A short history of the Web”) -->
- web nyilvános éve: 1991
<!-- forrás: CERN – az első weboldal és a web nyilvános bejelentése, 1991. augusztus 6. -->
- okostelefonok éve: 2007
<!-- forrás: becslés – az érintőképernyős okostelefonok 2007 után terjedtek el gyorsan (márkanév szándékosan nincs) -->

## 8. Netikett: mit, kinek, hogyan?
Az elküldött üzenet másolatként él tovább. Számít, mit, kinek és hogyan írsz. ==Melyik levelet küldenéd el? Tippelj!==

A **netikett** az online illem. A CSUPA NAGYBETŰ kiabálásnak hat. Legyen **tárgy** és megszólítás. Más fotóját csak engedéllyel küldd tovább!

> megjegyzés: Bántó üzenetnél szólj egy felnőttnek, akiben megbízol.

### Feliratok
- netikett kérdés felirat: Melyik levelet küldenéd el Bencének?
- a tipp: A
- b tipp: B
- c tipp: C
- a levél tárgy felirat: (nincs tárgy)
- a levél szöveg felirat: HOLNAP HOZD EL A KÖNYVEMET!!!
- b levél tárgy felirat: Tárgy: A könyvem
- b levél szöveg felirat: Szia Bence! Holnap el tudnád hozni a könyvemet? Köszönöm! Anna
- c levél tárgy felirat: (nincs tárgy)
- c levél szöveg felirat: könyv holnap
- a hiba felirat: csupa nagybetű – kiabálásnak hat
- b jó felirat: tárgy, megszólítás, kérés, köszönet
- c hiba felirat: nincs tárgy – mit akar?
- mit felirat: Mit? – amit szemtől szemben is mondanál
- kinek felirat: Kinek? – csak akire tartozik
- hogyan felirat: Hogyan? – tárgy, megszólítás, kisbetű
- nagybetű tévhit felirat: A CSUPA NAGYBETŰ csak kiemelés?
- nagybetű válasz felirat: Nem: online kiabálásnak olvassák.

## 9. Összefoglalás
Az üzenet **csomagokra** bomlik, mindegyiken **cím** és **sorszám**. Az **útválasztók** adják tovább, főleg **kábeleken**. A **szerveren** **másolat** marad, a **felhő** pedig egy másik gép mappája. ==Gondold át, mit, kinek és hogyan küldesz!==

### Feliratok
- összefoglaló cím felirat: Az üzenet útja
- össz csomag felirat: csomagokra bomlik
- össz cím felirat: cím és sorszám mindegyiken
- össz út felirat: útválasztók, főleg kábelen
- össz gyors felirat: fényként, ezredmásodpercek alatt
- össz másolat felirat: a szerveren másolat marad
- össz felhő felirat: felhő: más gépen, jogosultsággal
- össz netikett felirat: netikett: mit, kinek, hogyan

<!-- Tanári megjegyzések és források:
  - Kitalált példák: Anna, Bence, Csilla, az e-mail-címek (pelda.example, RFC 2606), az IP-címek (198.51.100.x és
    203.0.113.x – dokumentációs tartomány, RFC 5737), a levelek szövege, a „kirandulas.jpg”, az „Osztálykirándulás” mappa.
    A szerver helye (Frankfurt) és a városok közti hálózat kitalált, valószerű példa; a vásznon „kitalált példa” és
    „modell” bélyeg.
  - Modell-egyszerűsítések: a 3. lépés hálózata hét csomópont; a valódi internetben sok ezer útválasztó van, és az
    útvonalat útválasztási szabályok (protokollok) döntik el. A lecke „minden csomag a három legrövidebb szabad út egyikén
    megy” szabálya csak szemléltetés. A valóságban a sorba rakást és az újrakérést a TCP végzi (7–8. évfolyam:
    protokollok). A csomagok mérete: az Ethernet adatmezője 1500 bájt; a fejlécek (IP, TCP) után kb. 1460 bájt hasznos adat
    marad, ezért a 3 MB-os fotó valójában kb. 2050 csomag – a lecke „kb. 2000”-et mond.
  - A cím: IPv4-cím = 4 bájt (0–255), pl. 198.51.100.23. Ma terjed az IPv6 (16 bájt) – csak a megjegyzésben.
    A valóságban Anna telefonja a szervernek címzi a csomagot, a szerver pedig új csomagokban küldi tovább Bencének.
  - Sebesség: üvegszálban kb. 200 000 km/s (c / 1,47 ≈ 204 000 km/s). Budapest–Frankfurt légvonalban kb. 810 km →
    kb. 4 ms; Budapest–New York kb. 7000 km → kb. 35 ms egy irányban – a lecke a koordinátákból számolja (gömb,
    R = 6371 km). A valódi kábelút hosszabb, és az útválasztók is késleltetnek, ezért a mért idő (ping) ennek kb. a
    kétszerese-háromszorosa oda-vissza: Budapest–Frankfurt kb. 10–25 ms, Budapest–New York kb. 90–120 ms (becslés,
    nem mért érték). A geostacionárius műholdon át: fel és le 2 · 35 786 km / 300 000 km/s ≈ 0,24 s egy irányban.
    Ma alacsony pályás műholdas internet is van (néhány száz km magasan, sokkal kisebb késéssel); a lecke csak a
    hagyományos távközlési műholdat hasonlítja.
  - „Az internet főleg kábeleken megy”: a nemzetközi adatforgalom túlnyomó része tenger alatti üvegszálas kábeleken
    halad (a TeleGeography „több mint 99 %”-ot ír – arányszámot a lecke szándékosan nem mond). A 4. lépés térképén a
    kábelek vonala vázlatos, valódi kábelnév nélkül; a pontos térkép: TeleGeography, Submarine Cable Map
    (submarinecablemap.com), megtekintve 2026-11-24.
  - Másolat: a törölt e-mail a feladó postafiókjából tűnik el; a címzett postafiókjában, a szolgáltatók szerverein, és
    ha valaki továbbküldte vagy képernyőképet készített, ott is megmaradhat. Egyes csevegőalkalmazásokban „mindenkinél
    törölhető” az üzenet – de ami addig elmentve, továbbküldve, lefotózva lett, az ott marad.
  - Felhő: a megosztás beállításai szolgáltatónként másképp néznek ki; a lecke három tipikus jogosultságot mutat
    (megtekintés, szerkesztés, „bárki, akinél a link van”). Az órán használt felhőszolgáltatásban ezt a megosztás
    beállításainál találod. A sorozat 17-szamitogep leckéje a fájl/mappa fogalmát adja.
  - Idővonal: távíró 1844 (Morse, Washington–Baltimore), atlanti távírókábel 1866 (az 1858-as csak hetekig működött),
    telefon 1876 (Bell), Telefonhírmondó 1893 (Puskás Tivadar, Budapest), ARPANET 1969, e-mail 1971 (Ray Tomlinson), web
    1989 (javaslat) / 1991 (nyilvános), okostelefonok 2007 után (becslés, márkanév nélkül). A tortenelem-5-6/14
    könyvnyomtatás-leckéje szerint Gutenberg műhelye 1450 körül működött Mainzban, Frankfurt mellett.
  - Netikett: a CSUPA NAGYBETŰ online kiabálásnak számít; a tárgy és a megszólítás segít a címzettnek. A bántó üzenetről
    a sorozat 15-labnyom leckéje szól (Kék Vonal: 116-111).
  - A magyar 5–6. sorozat 01-kommunikacio leckéje a kommunikáció tényezőit (feladó, címzett, csatorna) mutatja; itt a
    „csatorna” a hálózat.
-->
