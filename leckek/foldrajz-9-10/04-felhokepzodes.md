# Miért hidegebb a hegytetőn, ha közelebb van a Naphoz? – a légkör szerkezete, felhő és csapadék
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 3. A légkör

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/04-felhokepzodes.md
  A számok az animációt is vezérlik: a standard légkör görbéje, a hűlési ütemek (száraz, nedves,
  harmatpont), a frontok lejtése, a fagypont magassága mind innen számolódik. A főn-szimulátor és a
  felhőképződés egyszerűsített MODELL (állandó hűlési ütemek), a panel ezt kimondja.
-->

## Közös

### Feliratok
- modell: modell
- vázlatos: vázlatos
- becslés: becslés
- torzítás: függőleges torzítás #×
- méretarányos: méretarányos
- magasság km: magasság (km)
- magasság m: magasság (m)
- hőmérséklet tengely: hőmérséklet (°C)
- fok: # °C
- forrás standard: Forrás: standard légkör (ISO 2533, US Standard Atmosphere 1976) · átlagos állapot, nem egy adott nap
- forrás modell: Modell: állandó hűlési ütemek (száraz # és nedves # °C/100 m) · nem mért adat
- talaj: talaj
- felhő: felhő

### Adatok
<!-- forrás (az alábbiakra): standard légkör – ISO 2533:1975, ill. U.S. Standard Atmosphere 1976 (NOAA/NASA/USAF), közismert; a nemzetközi egyezményes átlaglégkör (mérsékelt öv, évi átlag) -->
- tengerszinti hőmérséklet: 15 °C
- tengerszinti légnyomás: 1013,25 hPa
- átlagos hőmérséklet-csökkenés: 0,65 °C/100 m
- standard légkör: 0 km: 15 · 11 km: −56,5 · 20 km: −56,5 · 32 km: −44,5 · 47 km: −2,5 · 51 km: −2,5 · 71 km: −58,5 · 86 km: −86,3 · 91 km: −86,3 · 100 km: −78,1 °C
<!-- forrás: U.S. Standard Atmosphere 1976, rétegenkénti hőmérséklet-gradiensek (−6,5; 0; +1,0; +2,8; 0; −2,8; −2,0 K/km) a geopotenciális magasságban; a 86–100 km közötti szakasz a táblázat értékeiből (186,87 K és 195,08 K), köztük a lecke lineárisan interpolál. A geometriai és a geopotenciális magasság különbségét (100 km-en kb. 1,5 km) a lecke elhanyagolja. -->
- száraz adiabatikus hűlés: 0,98 °C/100 m
<!-- forrás: g / c_p = 9,81 / 1005 K/m ≈ 9,8 K/km, közismert (minden meteorológiai tankönyv) -->
- nedves adiabatikus hűlés: 0,5 °C/100 m (modell)
<!-- forrás: a valódi érték a hőmérséklettől és a nyomástól függ, kb. 0,4–0,7 °C/100 m (meleg, nedves levegőben kisebb, hidegben a szárazhoz közelít) – közismert; a lecke egyetlen értékkel számol, és ezt kimondja -->
- harmatpont csökkenése: 0,18 °C/100 m (modell)
<!-- forrás: emelkedő, telítetlen levegőben a harmatpont kb. 0,17–0,2 °C/100 m-rel csökken (a gőznyomás a nyomással együtt csökken), közismert közelítés; a 0,98 − 0,18 = 0,80 °C/100 m különbségből adódik a felhőalap „125 m fokonként” szabálya -->

## 1. Fent közelebb a Nap?
Ha hegyet mászol, ==közelebb kerülsz a Naphoz – mégis hidegebb lesz==. Miért? Sokan azt hiszik, fent a hideg világűr van közelebb, vagy messzebb a Föld meleg belseje.

Húzd fel a hegymászót, és figyeld a hőmérőt!

> megjegyzés: Mielőtt továbblépsz, gyűjtsetek tippeket: miért hideg a csúcson?

### Feliratok
- kérdés: Közelebb a Naphoz – mégis hidegebb?
- Mount Everest: Mount Everest
- hegymászó: # m-en
- lent: lent
- naptávolság cím: Mennyivel kerültél közelebb a Naphoz?
- Föld: Föld
- Nap: Nap
- távolság: távolság: #
- közelebb: közelebb: # km
- arány: ez a távolság # %-a
- napfény erősebb: a napfény ennyivel erősebb: # %
- léptéken: ezen a vonalon a hegy # px magas
- hidegebb: a csúcson # °C-kal hidegebb
- tévhit 1: közelebb a hideg világűr?
- tévhit 2: messzebb a Föld meleg belseje?
- tévhit 3: közelebb a Nap, melegebb kéne?
- csúszka magasság: A hegymászó magassága
- csúszka m: # m

### Adatok
- Mount Everest magassága: 8849 m
<!-- forrás: Nepál és Kína közös mérése, 2020 (8848,86 m), közismert -->
- Nap távolsága: 149,6 millió km
<!-- forrás: csillagászati egység, 149 597 870,7 km (IAU 2012), közismert -->
- kezdő magasság: 5000 m (modell)
<!-- forrás: a csúszka kezdőértéke -->

## 2. A légkör: vékony héj
A légkör alsó rétege a **troposzféra**: itt van a felhő és az időjárás. Fölötte a **sztratoszféra**, benne az **ózonréteg**. Az ózon elnyeli a Nap UV-sugárzását, ezért ott ==felfelé újra melegszik==. A levegő fele {légnyomás feleződése} alatt van.

> megjegyzés: Kapcsold át méretarányosra! A légkör olyan vékony, mint az alma héja.

### Feliratok
- troposzféra: troposzféra
- sztratoszféra: sztratoszféra
- mezoszféra: mezoszféra
- termoszféra: termoszféra
- ózonréteg: ózonréteg (legsűrűbb: #)
- időjárás: felhő, időjárás
- repülő: utasszállítók: #
- ISS: Nemzetközi Űrállomás: # ↑
- űrhatár: # – a világűr határa (megállapodás szerint)
- tropo vastagság: a troposzféra vastagsága:
- tropo sark: a sarkoknál #,
- tropo egyenlítő: az Egyenlítőnél #
- görbe: a hőmérséklet a magassággal
- gomb méretarányos: A légkör méretarányosan
- gomb nagyítva: Vissza a nagyított nézetre
- gömb légkör: légkör (# km)
- gömb tropo: troposzféra
- alma: Ha a Föld egy # átmérőjű alma lenne:
- alma légkör: a légkör # vastag héj,
- alma tropo: a troposzféra csak # mm.
- forrás gömb: Méretarányos rajz · Made with Natural Earth

### Adatok
- tropopauza magassága: 11 km
<!-- forrás: standard légkör (lásd fent); a valódi tropopauza a sarkoknál kb. 8, az Egyenlítőnél kb. 16–18 km magasan van -->
- troposzféra a sarkoknál: kb. 8 km
<!-- forrás: tankönyvi érték, közismert (a 05-legkorzes leckével egyezően) -->
- troposzféra az Egyenlítőnél: kb. 16–18 km
<!-- forrás: tankönyvi érték, közismert; a 05-legkorzes modellje 16 km-rel számol -->
- sztratoszféra teteje: kb. 50 km
<!-- forrás: standard légkör: a sztratopauza 47–51 km között, közismert -->
- mezoszféra teteje: kb. 86 km
<!-- forrás: standard légkör (mezopauza, 86 km, kb. −86 °C); a valódi mezopauza 80–100 km között van, nyáron a sarkok fölött −130 °C alá is hűl -->
- ózon legnagyobb sűrűsége: 20–25 km
<!-- forrás: WMO/UNEP Scientific Assessment of Ozone Depletion (2022), „Twenty Questions and Answers about the Ozone Layer”, Q1: az ózon kb. 90 %-a a sztratoszférában, a legnagyobb koncentráció kb. 15–35 km között; a csúcs a mérsékelt övben kb. 20–25 km; lekérdezve: 2026-11-24 (emlékezetből, ellenőrizendő) -->
- utasszállítók magassága: kb. 10–12 km
<!-- forrás: közismert (utazómagasság kb. 33 000–40 000 láb) -->
- Nemzetközi Űrállomás magassága: kb. 400 km
<!-- forrás: NASA – a pálya magassága kb. 400–420 km, közismert -->
- világűr határa: 100 km
<!-- forrás: Kármán-vonal, a Nemzetközi Repülőszövetség (FAI) megállapodása, közismert -->
- légnyomás feleződése: kb. 5,5 km
<!-- forrás: standard légkör: 5,5 km-en kb. 505 hPa ≈ a tengerszinti fele; a nyomás a fölötte lévő levegő súlya, így a légkör tömegének fele van alatta (a lecke a görbéből ellenőrzi) -->
- Föld sugara: 6371 km
<!-- forrás: közepes Föld-sugár, közismert -->
- légkör a gömbön: 100 km
<!-- forrás: a rajzolt légkör vastagsága = a világűr határa (Kármán-vonal) -->
- alma átmérője: 8 cm (modell)
<!-- forrás: példa – egy közepes alma; 100 km / 6371 km × 4 cm ≈ 0,63 mm (a lecke számolja) -->

## 3. Alulról melegszik
A napfény nagy része ==átmegy a levegőn==, és a felszínt melegíti. A meleg talaj melegíti a fölötte lévő levegőt: a légkör alulról fűtött, mint a padlófűtéses szoba. Éjjel a talaj kihűl, és alulról hűti a levegőt.

> megjegyzés: Húzd a napszakot éjszakára! Az üvegházhatás: fizika, „Miért melegszik a Föld?”

### Feliratok
- átmegy: a napfény nagy része átmegy a levegőn
- melegíti: a meleg talaj alulról melegíti a levegőt
- hűti: éjjel a kihűlő talaj alulról hűti a levegőt
- termik: felszálló meleg levegő
- kisugárzás: a talaj hőt sugároz ki
- inverzió: lent hidegebb, mint fölötte
- átlag: átlagos állapot
- most: most
- talaj hőmérséklete: a talaj: # °C
- csúszka napszak: Napszak
- óra: # óra
- napfény cím: A beérkező napfény 100 %-ából
- visszaverődik: # % visszaverődik
- levegő elnyeli: # % a levegő
- felszín elnyeli: # % a felszín
- forrás napfény: Napfény: NASA, a Föld energiamérlege (CERES-mérések, 2000-es évek átlaga) · a napi menet: modell

### Adatok
<!-- forrás (az alábbiakra): NASA Earth Observatory, „Climate and Earth’s Energy Budget” (2009, CERES-adatok): a beérkező napfény kb. 29 %-a visszaverődik, 23 %-át a légkör (felhők, vízgőz, ózon, por) nyeli el, 48 %-át a felszín; earthobservatory.nasa.gov/features/EnergyBalance, lekérdezve: 2026-11-24 (emlékezetből, ellenőrizendő); Trenberth és mtsai. (2009) hasonló arányokat ad -->
- napfény visszaverődik: 29 %
- napfény a levegőben: 23 %
- napfény a felszínen: 48 %
<!-- forrás (az alábbiakra): modellparaméterek a napi menethez (derült nyári nap, szárazföld); a talaj közeli levegő napi ingása Magyarországon nyáron kb. 10–15 °C -->
- nappali melegedés: 8 °C (modell)
- éjszakai hűlés: 6 °C (modell)
- kezdő napszak: 13 óra (modell)

## 4. A felszálló levegő hűl
Fent kisebb a légnyomás, ezért a felszálló **légcsomag** kitágul. Tágulás közben munkát végez a környező levegőn, ezt a saját energiájából fedezi: ==lehűl, kb. 1 °C-ot 100 méterenként==. Lefelé fordítva: az összenyomott levegő melegszik.

> megjegyzés: Ezért melegszik a biciklipumpa is pumpáláskor.

### Feliratok
- légcsomag: légcsomag
- légnyomás: légnyomás (hPa)
- feleződés: a légnyomás fele
- sűrűség: a levegő ritkul felfelé
- kártya magasság: magasság
- kártya nyomás: légnyomás
- kártya hőmérséklet: hőmérséklet
- kártya térfogat: térfogat
- érték m: # m
- érték hPa: # hPa
- érték térfogat: #-szoros
- ütem: # °C hűlés 100 m-enként
- pumpa: pumpa: összenyomva melegszik
- tágul: felszálló levegő: kitágul és hűl
- csúszka csomag: A légcsomag magassága
- forrás csomag: Légnyomás: standard légkör · hűlés: száraz adiabatikus · modell

### Adatok
- csomag kezdő hőmérséklete: 20 °C (modell)
<!-- forrás: példa (nyári délután); a hűlés üteme nem függ a kezdő hőmérséklettől -->
- csomag legnagyobb magassága: 6000 m (modell)
<!-- forrás: a csúszka felső határa -->

## 5. Harmatpont: megszületik a felhő
Hűlés közben a levegő telítetté válik (**harmatpont**): a vízgőz cseppekké csapódik le, ==megszületik a felhő== (**felhőképződés**). Fokonként (hőmérséklet − harmatpont) {felhőalap fokonként} emelkedés. A felhőben lassabban hűl: a lecsapódó víz hőt ad le.

> megjegyzés: A felhő nem gőz, hanem vízcsepp (fizika: halmazállapotok).

### Feliratok
- csomag T: a csomag hőmérséklete
- csomag Td: harmatpontja
- felhőalap: felhőalap: # m
- köd: köd: a felhő a talajon ül
- száraz szakasz: száraz: −# °C/100 m
- nedves szakasz: felhőben: −# °C/100 m
- páratartalom: relatív páratartalom: # %
- csúszka hőmérséklet: A levegő hőmérséklete lent
- csúszka harmatpont: A harmatpont lent
- telített: telített: itt lecsapódik a vízgőz

### Adatok
- felhőalap fokonként: kb. 125 m
<!-- forrás: 100 m / (0,98 − 0,18) °C = 125 m, közismert ökölszabály (a lecke a fenti ütemekből ellenőrzi) -->
- kezdő hőmérséklet: 24 °C (modell)
<!-- forrás: a csúszka kezdőértéke (nyári délután) -->
- kezdő harmatpont: 12 °C (modell)
<!-- forrás: a csúszka kezdőértéke; 24 és 12 °C → felhőalap 1500 m -->

## 6. Főn: a hegy két oldala
A hegynek ütköző levegő felemelkedik és hűl. A szél felőli oldalon felhő és ==eső== lesz belőle, a víz ott marad. A túloldalon a levegő leereszkedik, és 100 m-enként kb. 1 °C-ot melegszik: ==melegebb és szárazabb==, mint indulás előtt. Ez a **főn**.

> megjegyzés: Modell: a lecsapódott víz mind kiesik.

### Feliratok
- szél iránya: szél
- szél felőli: szél felőli oldal
- szél alatti: szél alatti oldal
- indulás: indulás
- csúcson: a csúcson
- túloldalon: a túloldalon
- főn: főn: meleg, száraz szél
- eső: eső
- nincs felhő: nincs felhő: a két oldal egyforma
- melegebb: # °C-kal melegebb
- páratartalom rövid: páratartalom: # %
- útközben: a légcsomag hőmérséklete útközben
- távolság km: távolság (km)
- csúszka hegy: A hegy magassága

### Adatok
<!-- forrás (az alábbiakra): modell – a csúszkák tartománya és kezdőértékei a terv briefje szerint (500–4000 m); a hegy lába a modellben tengerszinten van -->
- legalacsonyabb hegy: 500 m (modell)
- legmagasabb hegy: 4000 m (modell)
- kezdő hegymagasság: 3000 m (modell)
- főn kezdő hőmérséklete: 20 °C (modell)
- főn kezdő harmatpontja: 12 °C (modell)
<!-- megjegyzés: a csúszkák kezdőértékei; 3000 m-es hegyen 20/12 °C-ból a túloldalon kb. 29,6 °C lesz (a lecke számolja és ellenőrzi) -->

## 7. Front: a hideg levegő ékként emel
A levegő frontnál is felemelkedik. A **hidegfront** sűrű, hideg levegője ékként nyomul a meleg alá, és meredeken emeli: zivatarfelhő, zápor jön. A **melegfront** esetén a meleg levegő lankás lejtőn csúszik fel a hidegre: ==réteges felhők, órákig tartó csendes eső==.

> megjegyzés: Méretarányosan a front szinte vízszintes!

### Feliratok
- hideg levegő: hideg levegő
- meleg levegő: meleg levegő
- hidegfront: hidegfront
- melegfront: melegfront
- zivatarfelhő: zivatarfelhő
- zápor: zápor, zivatar
- réteges: réteges felhők
- fátyolfelhő: fátyolfelhők
- csendes eső: csendes eső, órákig
- lejtés: lejtés: #
- mozgás: a front mozgása
- gomb melegfront: Melegfront
- gomb hidegfront: Hidegfront
- gomb méretarányos front: Méretarányosan
- gomb torzított: Torzítva
- méretarányos front: méretarányosan: # km széles, # km magas szelet

### Adatok
- hidegfront lejtése: kb. 1 : 70
<!-- forrás: tankönyvi érték: hidegfront kb. 1 : 50 – 1 : 100, melegfront kb. 1 : 150 – 1 : 300 (pl. Ahrens: Meteorology Today; a terv briefje), közismert; a lecke egy-egy középértékkel rajzol -->
- melegfront lejtése: kb. 1 : 200
<!-- forrás: lásd fent -->
- szelet szélessége: 1200 km
<!-- forrás: a rajzolt metszet szélessége (modell) -->
- szelet magassága: 11 km
<!-- forrás: a rajzolt metszet magassága (a troposzféra, standard légkör) -->

## 8. Eső, hó, jégeső
A **csapadék** akkor hull, ha a felhőcseppek összeütközve megnőnek: egy esőcseppben kb. egymillió van. A **csapadékfajták**: a fagyos felhőrészben ==hópehely== nő; ha meleg rétegen esik át, elolvad: eső lesz. **Jégeső** erős feláramlásnál lesz: a jégszem fel-le jár, és rétegenként hízik.

### Feliratok
- fagypont: 0 °C-os szint: # m
- hópehely: hópehely
- esőcsepp: esőcsepp
- olvad: itt olvad el
- feláramlás: erős feláramlás
- jégszem: jégszem
- talajra ér: a talajra ér:
- hó: hó
- jégeső: jégeső
- csepp cím: Mekkora egy csepp?
- felhőcsepp méret: felhőcsepp: #
- esőcsepp méret: esőcsepp: #
- egymillió: egy esőcseppben # felhőcsepp vize van
- nagyítás: nagyítva, méretarányosan
- csúszka talaj: A talaj menti levegő hőmérséklete
- gomb jégeső: Erős feláramlás (zivatar)
- gomb jégeső ki: Gyenge feláramlás
- forrás csapadék: Modell: a fagypont magassága az átlagos 0,65 °C/100 m-es hűlésből · a felhő vázlatos

### Adatok
- felhőcsepp átmérője: kb. 0,02 mm
<!-- forrás: a felhőcseppek jellemző átmérője kb. 10–20 µm, az esőcseppeké kb. 0,5–5 mm (közismert, pl. Ahrens: Meteorology Today); (2 / 0,02)³ = 1 000 000 – a lecke számolja -->
- esőcsepp átmérője: kb. 2 mm
<!-- forrás: lásd fent -->
- olvadási sáv: 300 m (modell)
<!-- forrás: modellparaméter: a hópehely a 0 °C-os szint alatt kb. 300 m-en olvad el; ökölszabály: ha a fagypont a talaj fölött ennél alacsonyabban van (kb. +2 °C alatt), hó esik. A valóságban a páratartalom is számít (száraz levegőben +4 °C-on is eshet hó). -->
- kezdő talajhőmérséklet: 12 °C (modell)
<!-- forrás: a csúszka kezdőértéke -->

## 9. Összefoglalás
Fent azért hideg, mert a légkör ==alulról, a felszíntől melegszik==, és a felszálló levegő tágul és hűl. A harmatpontnál felhő születik. A levegő háromféleképpen emelkedik fel: melegedéssel, hegyen átkelve és frontnál.

> megjegyzés: Honnan tudjuk? Rádiószondás léggömbök mérik minden nap.

### Feliratok
- honnan típus: Honnan tudjuk?
- honnan cím: Rádiószonda
- honnan mivel: Mivel mérik?
- honnan mivel v: léggömbbel felszálló mérőműszerrel
- honnan mit: Mit mér?
- honnan mit v: hőmérséklet, páratartalom, nyomás, szél
- honnan mikor: Milyen gyakran?
- honnan mikor v: naponta, főleg 00 és 12 UTC-kor
- honnan hol: Hol?
- honnan hol v: nálunk Budapest-Pestszentlőrincen is
- szonda: rádiószonda
- szétpattan: kb. # km-en szétpattan
- léggömb tágul: a léggömb fent kitágul
- ö 1: A légkör vékony: tömegének fele # alatt van.
- ö 2: Alulról, a napsütötte felszíntől melegszik.
- ö 3: A felszálló levegő tágul és hűl: kb. 1 °C / 100 m.
- ö 4: A harmatpontnál felhő születik.
- ö 5: Hegy, front, melegedés: így emelkedik a levegő.
- ö 6: A főn a hegy túloldalán meleg és száraz.
- forrás szonda: Görbe: standard légkör · a rádiószonda emelkedése gyorsítva

### Adatok
- szonda szétpattanása: kb. 30–35 km
<!-- forrás: a rádiószondás léggömbök jellemzően 25–35 km-en pattannak szét (WMO CIMO Guide, WMO-No. 8, Vol. I, 12. fejezet; Vaisala RS41 ismertetők), közismert; a felbocsátás a világhálózatban főleg 00 és 12 UTC-kor (WMO), a HungaroMet Budapest-Pestszentlőrincről naponta indít szondát (met.hu; a pontos időpontok ellenőrizendők) -->
- szonda emelkedési sebessége: kb. 5 m/s
<!-- forrás: WMO CIMO Guide: a szokásos emelkedési sebesség kb. 5–6 m/s (30 km kb. 1,5 óra), közismert -->

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - A „miért hideg fent” magyarázat két része: (1) a légkör nagyrészt alulról, a felszíntől kap hőt (érintkezés,
    feláramlás, a felszín hősugárzása – üvegházhatás), (2) a feláramló levegő tágulva hűl. A troposzféra átlagos
    0,65 °C/100 m-es hőmérséklet-csökkenése e kettő és a sugárzási hűlés egyensúlya; a lecke ezt egyszerűsíti.
  - A standard légkör mérsékelt övi évi átlag; egy adott napon a görbe jelentősen eltér (inverzió, trópusi
    vagy sarki légkör).
  - A nedves adiabatikus ütem a modellben állandó 0,5 °C/100 m; a valóságban 0,4–0,7 (hidegben ennél is nagyobb).
  - A főn-modellben a lecsapódott víz mind kiesik, a hegy lába mindkét oldalon tengerszinten van, és a levegő a
    csúcson át egyenesen leereszkedik. A valódi főn (Alpok, Kárpátok) hőmérséklet-többlete jellemzően 5–15 °C.
  - A napi menet (3. lépés) didaktikus modell: a talaj menti hőmérséklet-eltérés exponenciálisan csökken
    felfelé (nappal kb. 1,5 km-es, éjjel kb. 0,25 km-es keveredési réteggel).
  - Front: a lejtés tankönyvi tartomány egy középértéke; a felhőzet sematikus (Cb a hidegfrontnál, Ns–As–Ci a
    melegfrontnál), okklúzió nincs.
  - A csapadékfajtáknál a „hó, ha a 0 °C-os szint 300 m-nél alacsonyabban van” ökölszabály; ónos esőt, havas esőt,
    a páratartalom hatását a lecke nem mutatja. A jégeső mechanizmusa (fel-le járás) a tankönyvi kép; ma a
    kutatók szerint a jégszem inkább egy-két hosszabb utat tesz meg a feláramlásban.
  - A rádiószonda magyarországi felbocsátási időpontjai (00 / 12 UTC) a HungaroMettel egyeztetendők.
-->
