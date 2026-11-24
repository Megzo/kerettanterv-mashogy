# Mi van a levegőben, és mi kerül bele? – légkör, savas eső, ózon, szmog
tantárgy: Kémia · évfolyam: 7–8. · témakör: 5. Kémia a természetben

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/kemia-7-8/11-levego.md

  ÉVENTE FRISSÍTENDŐ: „CO₂ a levegőben” és a „CO₂ Mauna Loa” sor (NOAA GML, Mauna Loa éves átlag:
  https://gml.noaa.gov/ccgg/trends/ – co2_annmean_mlo.txt), valamint az ózonréteg helyreállásának
  becsült éve (WMO/UNEP ózon-értékelés, négyévente). A „frissítendő” sorokat a
  `python3 tools/build_lesson.py --stale` listázza.
  Az üvegházhatás fizikáját a fizika 7–8. `14-uveghaz` lecke mutatja; ez a lecke csak a
  kémiai oldalt (honnan jön a CO₂) és a megkülönböztetést (≠ ózonlyuk) adja.
-->

## Közös

### Feliratok
- nagyítás: nagyítás · szemléltetés
- modell: modell
- ne próbáld: NE PRÓBÁLD KI
- tanári bemutató: tanári bemutató
- nitrogén: N₂ nitrogén
- oxigén: O₂ oxigén
- argon: Ar argon
- szén-dioxid: CO₂ szén-dioxid
- vízgőz: H₂O vízgőz
- kén-dioxid: SO₂ kén-dioxid
- ózon: O₃ ózon
- nitrogén-oxidok: NO, NO₂ nitrogén-oxidok

### Adatok
- nitrogén aránya: 78,08 %
- oxigén aránya: 20,95 %
- argon aránya: 0,93 %
- CO₂ a levegőben: 427 ppm (2025, frissítendő)
- vízgőz aránya: 0–4 %
<!-- Száraz levegő összetétele (térfogat%, a tengerszinten): N₂ 78,08 · O₂ 20,95 · Ar 0,93 · CO₂ ≈ 0,04 –
     NOAA / CRC Handbook („U.S. Standard Atmosphere”); a vízgőz helytől és időtől függően 0–4 % (a száraz
     levegőhöz adva). CO₂: NOAA GML, Mauna Loa, 2025. évi átlag 427,35 ppm (lekérdezve: 2026-11-24);
     a globális tengerfelszíni átlag ettől néhány tized ppm-mel tér el. 427 ppm = 0,0427 % → 10 000
     részecskéből kb. 4. -->

## 1. Miből áll a levegő?
A levegő **keverék**. Ha 100 részecskét kiválasztanánk belőle, 78 nitrogén-, 21 oxigénmolekula és 1 argonatom lenne köztük.

==A szén-dioxid ebbe a 100-ba bele sem fér.== Nagyíts rá 10 000 részecskére, és keresd meg!

> megjegyzés: A vízgőz mennyisége változó ({vízgőz aránya}), ezért a száraz levegőt adjuk meg.

### Feliratok
- ablak 100: 100 részecske a levegőből
- ablak 10000: 10 000 részecske a levegőből
- nagyít gomb: Nagyíts: 10 000 részecske
- vissza gomb: Vissza: 100 részecske
- darab: # db
- keresd: Keresd meg a # CO₂-t!
- co2 itt: CO₂
- összetétel cím: száraz levegő, térfogat%
- vízgőz megjegyzés: + vízgőz: 0–4 % (változó)
- tévhit levegő: A levegő nagy része oxigén.
- helyes levegő: Majdnem 4/5-e nitrogén!

## 2. Mennyi az oxigén? – két kísérlet
A gyertyánál a víz kicsit emelkedik, de ==a gyertya kialszik, amikor még sok oxigén van körülötte== ({gyertya kialszik}).

A nedves vasgyapot lassan az összes oxigént megköti: itt a víz **egyötödnyit** emelkedik.

> megjegyzés: A gyertyás kísérlet tanári bemutató. Nyomd meg a „Miért?” gombokat!

### Feliratok
- gyertya cím: gyertya
- vas cím: nedves vasgyapot
- gyertya miért gomb: Miért? – gyertya
- vas miért gomb: Miért? – vasgyapot
- újra gomb: Újra
- idő csúszka: idő (vasgyapot)
- nap: # nap
- oxigén maradt: oxigén: # %
- kialudt: kialudt
- emelkedés: a víz emelkedése: # %
- ötöd: 1/5
- gyertya ok 1: A meleg gáz kitágult, egy része kibuborékolt.
- gyertya ok 2: Kihűlve összehúzódik – a víz benyomul.
- gyertya ok 3: Kb. 16 % oxigénnél kialszik.
- gyertya ok 4: A CO₂ egy része elnyelődik a vízben.
- vas ok 1: A vas lassan, de az összes oxigént megköti.
- vas ok 2: Nem melegszik, nem keletkezik gáz.
- vas ok 3: Ami marad: főleg nitrogén.
- tévhit gyertya: Elfogy az oxigén, ezért emelkedik a víz.
- helyes gyertya: A gyertya kialszik, mielőtt elfogyna.

### Adatok
- gyertya kialszik: kb. 16 %
- gyertyás vízemelkedés: kb. 10 % (modell)
<!-- A gyertya lángja kb. 15–16 % oxigénnél kialszik (a pontos érték a kanóctól, a gyertya anyagától
     függ; pl. RSC Education, „The candle and the jar” / J. Chem. Educ. 2014, 91, 2075–2078 – Vera,
     Rivera, Núñez: „Burning a candle in a vessel, a simple experiment with a long history”). A víz
     emelkedését főként a gáz hőtágulása és lehűlése okozza (a henger leengedésekor a meleg gáz egy része
     kibuborékol), a CO₂-nek csak kis része oldódik; az emelkedés a kivitelezéstől függően 5–20 % – a
     lecke 10 %-kal rajzolja (modell). A vasgyapotos kísérlet (nedves, ecettel zsírtalanított acélgyapot)
     a valódi oxigéntartalmat adja, kb. 1/5-öt (20,95 %); az időtartam a gyapot finomságától függ
     (órák – néhány nap), a lecke időtengelye modell. -->

## 3. Mi kerül a levegőbe égéskor?
Égéskor a tüzelőanyag a levegő oxigénjével egyesül. Válassz tüzelőanyagot!

A szénből és a földgázból **szén-dioxid** és víz lesz. Ha kén is van a szénben, ==kén-dioxid== is keletkezik. A forró motorban még a levegő nitrogénje is reagál: **nitrogén-oxidok** lesznek.

> megjegyzés: 12 g szén elégetésekor 44 g szén-dioxid keletkezik – az oxigén is beépül!

### Feliratok
- gáz gomb: földgáz
- szén gomb: szén (kénes)
- motor gomb: autómotor
- gáz cím: földgáz a tűzhelyen
- szén cím: kéntartalmú szén a kályhában
- motor cím: benzin a forró motorban
- termékek: Mi kerül a levegőbe?
- gáz szóegyenlet: metán + oxigén → szén-dioxid + víz
- szén szóegyenlet: szén + oxigén → szén-dioxid
- kén szóegyenlet: kén + oxigén → kén-dioxid
- motor szóegyenlet: nitrogén + oxigén → nitrogén-monoxid
- motor megjegyzés: a benzinből CO₂ és víz is lesz
- forró: csak nagyon forró lángban
- tömeg cím: Miért nehezebb a CO₂, mint a szén?
- tömeg sor: # g szén + # g oxigén → # g szén-dioxid
- korom: korom, por
- válassz: Válassz tüzelőanyagot!

### Adatok
- metán égése: CH4 + 2 O2 -> CO2 + 2 H2O
- szén égése: C + O2 -> CO2
- kén égése: S + O2 -> SO2
- nitrogén és oxigén: N2 + O2 -> 2 NO
<!-- A nitrogén-monoxid a levegőben tovább oxidálódik nitrogén-dioxiddá (2 NO + O₂ → 2 NO₂); a
     „nitrogén-oxidok” (NOₓ) a kettő együtt. A benzin főleg szénhidrogén; tökéletes égésekor CO₂ és
     H₂O lesz belőle (lásd 09-eges-korrozio). A tömegek a közös elemtábla atomtömegeiből: 12,01 g C +
     32,00 g O₂ → 44,01 g CO₂ (a lecke számolja). -->

## 4. Savas eső: oxidok + víz
Már a tiszta eső is enyhén savas: a levegő szén-dioxidjából **szénsav** lesz benne, a pH-ja kb. {tiszta eső pH-ja}.

Ha a levegőben kén-dioxid is van, abból vízzel **kénessav** lesz, a nitrogén-oxidokból salétromsav. ==Ez a savas eső.== Húzd a csúszkát!

### Feliratok
- szennyezés csúszka: kén-dioxid a levegőben
- tiszta: tiszta
- szennyezett: szennyezett
- esőcsepp: esőcsepp
- indikátor: indikátorral színezve
- szénsav szóegyenlet: szén-dioxid + víz → szénsav
- kénessav szóegyenlet: kén-dioxid + víz → kénessav
- eső ph: az eső pH-ja: #
- tiszta eső jel: tiszta eső
- savas eső jel: savas eső
- paradicsomlé jel: paradicsomlé
- ecet jel: ételecet
- citromlé jel: citromlé
- több H: # × több H⁺, mint a tiszta esőben
- hidrogénion: H⁺
- tévhit savas: A savas eső maró, mint a sósav.
- helyes savas: Inkább paradicsomlé-savas – de évek alatt követ old, tavat savanyít.

### Adatok
- tiszta eső pH-ja: 5,6
- savas eső pH-ja: 4–4,5
- paradicsomlé pH-ja: 4,3
- ecet pH-ja: 2,5
- citromlé pH-ja: 2,3
- szénsav keletkezése: CO2 + H2O -> H2CO3
- kénessav keletkezése: SO2 + H2O -> H2SO3
<!-- Tiszta (szennyezetlen) esővíz pH-ja ≈ 5,6: a légköri CO₂-vel egyensúlyban lévő víz (US EPA
     „What is Acid Rain?”; USGS „pH and Water”). Savas esőnek az 5,6 alatti pH-jú csapadékot nevezzük;
     szennyezett ipari területeken a 4–4,5 (sőt 4 alatti) érték volt jellemző (US EPA; Európában az
     1970–80-as években). Paradicsomlé 4,1–4,6 (US FDA „Approximate pH of foods”), ecet és citromlé:
     lásd 10-sav-bazis. A csúszka modell: a csepp hidrogénion-koncentrációja a tiszta eső értékétől
     (5,6) a legszennyezettebb értékig (4,0, a tartomány alja) lineárisan nő a kén-dioxiddal;
     pH = −lg [H⁺]. A „× több H⁺” = 10^(5,6 − pH). A kénessav a levegőben tovább oxidálódik
     kénsavvá – ezt a 7–8. évfolyam nem részletezi. -->

## 5. A márványszobor
A márvány és a mészkő **kalcium-karbonát**. A sav hidrogénionjai kiszakítják a kristályból: ==szén-dioxid-buborék== és oldódó kalciumvegyület lesz belőle.

Állítsd az eső pH-ját és az éveket! Egy pH-lépés tízszer több H^+-t jelent – a savas eső sokkal gyorsabban koptat.

> megjegyzés: Kísérlet: márványdarab ecetben. Figyeld a buborékokat!

### Feliratok
- év csúszka: eltelt idő
- ph csúszka: az eső pH-ja
- év: # év
- szobor: márványszobor
- szóegyenlet: kalcium-karbonát + sav → kalciumion + víz + szén-dioxid
- kalciumion: Ca²⁺ kalciumion
- karbonátion: CO₃²⁻ karbonátion
- buborék: CO₂-buborék
- kopás: kopás (modell)
- sebesség: # × gyorsabb, mint tiszta esőben
- lemosva: lemosva: # ion
- tévhit kő: A kő örök, az esőnek nem árt.
- helyes kő: A savas eső lassan feloldja a mészkövet.

### Adatok
- márvány oldódása: CaCO3 + 2 H^+ -> Ca^2+ + H2O + CO2
<!-- Modell: a kopás sebessége a lecke modelljében az eső hidrogénion-koncentrációjával arányos
     (10^(5,6 − pH)-szoros a tiszta esőhöz képest), az idővel lineárisan nő. A valóságban a tiszta eső
     szénsava is old egy keveset (ez a karsztosodás oka), és a műemlékek kőpusztulásában nagy szerepe van
     a kőre közvetlenül lerakódó kén-dioxidnak is (gipszkéreg, ami lepattogzik) – lásd Lipfert (1989),
     Atmos. Environ. 23, 415–429; UNECE ICP Materials. A szobor rajza és a „kopás” mértéke szemléltető.
     A márvány valódi kopása szennyezett városi levegőben évtizedek alatt néhány tized mm-től mm-ig
     terjed. A részecskeablakban a kalcium-karbonát kristályt ionok rétegeként rajzoltuk (egyszerűsítve). -->

## 6. Ózon: fent pajzs, lent méreg
Az **ózon** (O_3) három oxigénatomból álló molekula. 15–35 km magasan sok van belőle: ez az ==ózonréteg==, amely elnyeli a Nap káros UV-sugárzásának nagy részét.

A felszín közelében viszont **szennyező**: köhögést, szemirritációt okoz. Húzd a csúszkát!

> megjegyzés: Az egész ózonréteg a felszínre hozva csak {ózonréteg vastagsága} vastag lenne.

### Feliratok
- magasság csúszka: magasság
- km: # km
- uv: a Nap UV-sugárzása
- ózonréteg: ózonréteg
- ózon mennyisége: ózon mennyisége
- felszín: felszín
- pajzs cím: Itt pajzs
- pajzs szöveg: Elnyeli a káros UV-sugarak nagy részét.
- méreg cím: Itt szennyező
- méreg szöveg: Nyári szmog: köhögés, szemirritáció.
- kevés cím: Itt kevés ózon van
- kevés szöveg: Az ózon nagy része 15–35 km magasan van.
- keletkezés: UV-fényben oxigénből ózon lesz
- repülő: utasszállító
- léggömb: mérőballon
- tévhit ózon: Minden ózon jó.
- helyes ózon: Fent véd – lent a tüdőt károsítja.

### Adatok
- ózonréteg magassága: 15–35 km
- ózonréteg vastagsága: kb. 3 mm
- ózon keletkezése: 3 O2 -> 2 O3
<!-- Ózonréteg: a sztratoszférában kb. 15–35 km között (NOAA / NASA „Ozone Facts”; WMO). A teljes
     ózonoszlop átlagosan kb. 300 Dobson-egység: normál nyomáson és 0 °C-on ez 3 mm vastag réteg. Az
     ózon az UV-B nagy részét és az UV-C-t teljesen elnyeli. A keletkezés valójában két lépés (O₂ + UV →
     2 O; O + O₂ → O₃) – a lecke az összesített egyenletet mutatja. Felszíni ózon: nitrogén-oxidokból és
     illékony szerves anyagokból napfényben keletkezik (nyári, fotokémiai szmog). A profil görbéje
     szemléltető (a csúcs kb. 20–25 km-en). -->

## 7. Üvegházhatás ≠ ózonlyuk
Sokan összekeverik, pedig ==két külön jelenség==.

Az **ózonlyukat** a hűtőkből, spraydobozokból kikerült **freonok** okozták: több UV jut le. A **melegedést** az égésből származó szén-dioxid erősíti.

Kattints egy állításra: melyik oszlopba tartozik?

> megjegyzés: Az üvegházhatás fizikája: fizika 7–8., „Miért melegszik a Föld?” lecke.

### Feliratok
- ózonlyuk oszlop: ÓZONLYUK
- üvegház oszlop: ERŐSÖDŐ ÜVEGHÁZHATÁS
- kattints: Kattints egy állításra!
- állítás 1: oka: freonok (hűtők, spray-k)
- állítás 2: több UV-sugárzás jut le
- állítás 3: tiltás: montreali egyezmény
- állítás 4: lassan gyógyul
- állítás 5: oka: az égésből származó CO₂
- állítás 6: melegszik a Föld
- állítás 7: CO₂: 280 → 427 ppm
- állítás 8: a hőt tartja vissza, nem az UV-t
- klór: 1 klóratom akár 100 000 ózonmolekulát is elbont
- grafikon cím: CO₂ a levegőben (ppm)
- évszám: év
- felfedezték: felfedezték: #
- egyezmény: egyezmény: #
- gyógyul: helyreáll: #
- tévhit uh: Az ózonlyuk okozza a felmelegedést.
- helyes uh: Két külön jelenség, más okkal.
- jó: jó helyen!

### Adatok
- CO₂ Mauna Loa: 1960: 317 · 1970: 326 · 1980: 339 · 1990: 354 · 2000: 370 · 2010: 390 · 2020: 414 · 2025: 427 ppm
- CO₂ iparosodás előtt: 280 ppm
- ózonlyuk felfedezése: 1985
- montreali jegyzőkönyv: 1987
- ózonréteg helyreállása: 2066 körül (előrejelzés)
<!-- CO₂: NOAA GML, Mauna Loa éves átlagok (1960: 316,91 · 1970: 325,68 · 1980: 338,76 · 1990: 354,45 ·
     2000: 369,71 · 2010: 390,10 · 2020: 414,21 · 2025: 427,35 ppm; lekérdezve: 2026-11-24), egészre
     kerekítve; iparosodás előtt kb. 280 ppm (jégfuratok, IPCC AR6). Ózonlyuk: Farman, Gardiner,
     Shanklin, Nature 315 (1985) 207–210. Montreali jegyzőkönyv: 1987. szeptember 16. Helyreállás: az
     antarktiszi ózonréteg várhatóan 2066 körül éri el az 1980-as szintet (WMO/UNEP Scientific Assessment
     of Ozone Depletion 2022) – a következő értékelés után frissítendő. „Egy klóratom akár 100 000
     ózonmolekulát elbonthat”: US EPA, „Basic Ozone Layer Science” (nagyságrendi becslés, a klór
     katalizátorként újra és újra reagál). Az üvegházhatás fizikája: leckek/fizika-7-8/14-uveghaz. -->

## 8. Téli és nyári szmog
A **téli szmog** hideg, szélcsendes időben jön: a fűtés füstje, korom és kén-dioxid gyűlik meg a köd alatt. ==A meleg levegőréteg fedőként zár.==

A **nyári szmog** napsütésben keletkezik: az autók nitrogén-oxidjaiból ózon lesz. A szél mindkettőt elfújja. Próbáld ki!

> megjegyzés: Londonban ({londoni szmog}) néhány nap alatt {londoni halálozás} halt meg.

### Feliratok
- téli gomb: téli szmog
- nyári gomb: nyári szmog
- szél csúszka: szél
- szélcsend: szélcsend
- erős szél: erős szél
- meleg réteg: melegebb levegőréteg – fedő
- hideg: hideg, nyirkos levegő
- napfény: erős napsütés
- téli cím: TÉLI (LONDONI) SZMOG
- nyári cím: NYÁRI SZMOG
- téli összetevő: korom, por, kén-dioxid, köd
- nyári összetevő: ózon, nitrogén-oxidok
- téli forrás: fűtés (szén, fa, szemét)
- nyári forrás: autók kipufogógáza + napfény
- london: London, 1952: kb. 4000 halott
- később: későbbi becslés: #
- határérték: PM10 napi határérték: #
- ózon küszöb: ózon: tájékoztatás # fölött
- levegő minőség: a por mennyisége
- tévhit szmog: A szmog csak a gyárak bűne.
- helyes szmog: A fűtés és a forgalom is okozza.
- ne égess: Szemetet, avart soha ne égess!

### Adatok
- londoni szmog: 1952. december
- londoni halálozás: kb. 4000 fő
- későbbi becslés: 10–12 ezer fő
- PM10 határérték: 50 µg/m³
- ózon tájékoztatási küszöb: 180 µg/m³
<!-- Londoni szmog, 1952. december 5–9.: az akkori statisztika kb. 4000 többlethalálozást mutatott, a
     későbbi becslések (Bell és Davis, Environ. Health Perspect. 2001) 10–12 ezret. PM10 napi
     határérték: 50 µg/m³ (2008/50/EK irányelv; a 2024/2881/EU irányelv szerint 2030-tól 45 µg/m³ –
     frissítendő). Ózon: tájékoztatási küszöb 180 µg/m³, riasztási 240 µg/m³ (1 órás átlag, 2008/50/EK).
     A hazai szmogriadó fokozatait a helyi önkormányzatok szmogriadó-terve és a 306/2010. Korm. rendelet
     szabályozza (ellenőrizendő a hatályos szöveg szerint – a lecke nem közöl riasztási küszöböt).
     A rajz szemléltető: a hőmérsékleti inverzió (a felszín közelében hidegebb, fölötte melegebb levegő)
     megakadályozza a füst felszállását. -->

## 9. Összefoglalás: mit tehetsz?
A levegő főleg nitrogén és oxigén. Égéskor CO_2, kén-dioxid és nitrogén-oxidok kerülnek bele; ezekből ==savas eső, szmog és erősödő üvegházhatás== lesz. Az ózon fent véd, lent árt.

**Te is tehetsz:** gyalogolj, bringázz, utazz közösségi közlekedéssel, takarékoskodj az energiával, és soha ne égess szemetet!

### Feliratok
- összegzés 1: A levegő keverék: 78 % N₂, 21 % O₂, 1 % Ar.
- összegzés 2: Égéskor: CO₂, víz, SO₂, nitrogén-oxidok, korom.
- összegzés 3: Oxid + víz → sav: savas eső, mészkő oldódik.
- összegzés 4: Ózon: fent pajzs, lent szennyező.
- összegzés 5: Ózonlyuk ≠ üvegházhatás – két külön jelenség.
- tehetsz cím: Mit tehetsz?
- tehetsz 1: gyalog, bringával
- tehetsz 2: közösségi közlekedés
- tehetsz 3: kevesebb energia
- tehetsz 4: nem égetünk szemetet

<!-- Modell-egyszerűsítések és források:
  - A részecskeablakok 2D-sek; a méret, a távolság és a sebesség nem arányos (a levegőben a részecskék
    között kb. tízszer akkora a távolság, mint az átmérőjük). Az 1. lépés 100-as ablakában a darabszámok
    a térfogat%-ok kerekítései (78 + 21 + 1 = 100), a 10 000-es rácsban 7808 + 2095 + 93 + 4 = 10 000
    (a CO₂ a ppm-értékből: 427 ppm → 4,27 → 4).
  - 2. lépés: a vízszintek és az időtengely modell (lásd a lépés megjegyzését).
  - 3. lépés: a molekulák átrendeződése egy lépésben animálva; a valóságban sok lépésben megy végbe.
  - 4–5. lépés: a pH-csúszka és a kopás modellje a lépések megjegyzésében. A hidrogéniont a 7–8. évfolyam
    szóhasználatával H⁺-nak rajzoljuk.
  - 6. lépés: az ózonprofil és a sugárnyilak szemléltetők.
  - 8. lépés: a szmogjelenetek szemléltetők, a szél hatása minőségi.
  - Biztonság: a gyertyás kísérlet tanári bemutató (nyílt láng, forró viasz); a vasgyapotos és a
    márvány–ecet kísérlet tanári felügyelettel tanulókísérlet. Szemetet, avart égetni tilos és
    egészségkárosító.
-->
