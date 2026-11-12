# Miért melegszik a Föld? – az üvegházhatás
tantárgy: Fizika · évfolyam: 7–8. · témakör: 9. Környezetünk globális problémái

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/14-uveghaz.md

  ÉVENTE FRISSÍTENDŐ: „CO₂ ma”, „CO₂ éves növekedése”, a „CO₂ <év>” és a „melegedés <évtized>”
  sorok, valamint a „tengerszint-emelkedés 1900 óta”. A mostani értékek kerekítettek, a lecke
  készítésekor (2026) ismert adatokból: CO₂ – NOAA Mauna Loa éves átlagok (1958 előtt jégfuratok);
  hőmérséklet – a HadCRUT5 / IPCC AR6 tízéves átlagai az 1850–1900-as átlaghoz képest,
  0,1 °C-ra kerekítve; tengerszint – IPCC AR6 (1901–2018: kb. 0,20 m). Frissítés előtt a
  forrásból ellenőrizd!

  A modell egyszerűsítései (a panel is kimondja):
  - Légkör nélküli Föld: a bejövő napfény átlaga a napállandó negyede (gömb, éjszaka, ferde
    beesés), a fényvisszaverést (albedó, 30 %) változatlannak vesszük. Az egyensúlyi
    hőmérsékletet a Stefan–Boltzmann-törvény adja (kisugárzás = σ·T⁴). 1361 W/m²-rel és
    30 %-kal ez −18,6 °C; a tankönyvi „−18 °C (255 K)” ugyanez, kissé más albedóval.
  - Üvegházhatás: egyrétegű légkör, amely a felszín infravörös sugárzásának egy részét elnyeli,
    és fele-fele arányban fel és le sugározza ki. Az elnyelt hányadot úgy állítjuk be, hogy a
    felszín átlaga a „mai átlaghőmérséklet” legyen. A valódi légkörben a hőt a felhők, a
    párolgás és a légáramlás is szállítja – ezt a modell nem tartalmazza.
  - Több CO₂: a sugárzási többlet ΔF = 5,35 W/m² · ln(C / C₀) (Myhre és mtsai., 1998),
    az egyensúlyi melegedés ΔT = (melegedés duplázásonként) · log₂(C / C₀). A „duplázásonként
    3 °C” (IPCC AR6 legjobb becslés, valószínű tartomány 2,5–4 °C) a visszacsatolásokat
    (vízgőz, jég, felhők) is tartalmazza. Ez EGYENSÚLYI érték: a valódi Föld az óceán miatt
    évtizedekig „késik”, és a szennyező por (aeroszol) részben hűt – ezért a mért melegedés
    (≈ 1,3 °C) kisebb, mint a 427 ppm-hez tartozó egyensúlyi érték (≈ 1,8 °C).
    A rajzon a CO₂-molekulák száma és az elnyelt fotonok aránya csak jelképes.
  - Fényvisszaverés: tipikus, kerekített értékek (friss hó 80–90 %, tengeri jég 50–70 %,
    homoksivatag 30–40 %, erdő 8–15 %, nyílt óceán kb. 6 %).
  - Tengerszint: az úszó jég olvadása édesvízben pontosan nem változtat a szinten; sós
    tengervízben az édes olvadékvíz miatt elhanyagolhatóan keveset. A hőtágulást a pohárban
    a valódi együtthatóval (20 °C körül) számoljuk, de felnagyítva rajzoljuk.
-->

## Közös

### Feliratok
- világűr: VILÁGŰR
- légkör: LÉGKÖR
- felszín: FELSZÍN
- napfény: napfény
- be: be: elnyelt napfény
- ki: ki: infravörös az űrbe
- ki felszín: ki: a felszín sugároz
- melegszik: be > ki → melegszik
- hűl: ki > be → hűl
- egyensúly: ki = be → egyensúly
- hőmérő cím: a felszín átlaga
- légkör nélküli modell: légkör nélküli modell

### Adatok
- napállandó: 1361 W/m²
- albedó: 30 %
- Stefan–Boltzmann-állandó: 0,0000000567 W/(m²·K⁴)
- mai átlaghőmérséklet: 15 °C

## 1. Napfény be
Minden a Napból indul. A légkör tetején a napfény **{napállandó}** teljesítményt ad négyzetméterenként.

A Föld gömb, és éjszaka is van: átlagosan csak ennek ==a negyede== jut egy m²-re. Ennek {albedó}-a visszaverődik (felhők, jég), a többit a felszín elnyeli.

> megjegyzés: A napfény nagy része látható fény. A légkör ezt szinte akadálytalanul átengedi.

### Feliratok
- rövid hullám: főleg látható fény (rövid hullám)
- napállandó felirat: a légkör tetején
- átlag felirat: átlagosan, egy m²-re
- negyede: ÷ 4
- visszavert: visszaverődik
- elnyelt: elnyeli a felszín
- felhő: felhő
- jég: jég, hó

## 2. A Föld infravöröset sugároz
Minden meleg test sugároz – a Föld felszíne is. Ez ==infravörös== fény, amit a szemünk nem lát.

Minél melegebb a felszín, annál **sokkal több** energiát sugároz ki. {mai átlaghőmérséklet} esetén többet, mint amennyit a Napból kap!

Húzd a csúszkát: hol lesz ki = be?

> megjegyzés: Te is sugárzol infravöröset – ezt látja a hőkamera.

### Feliratok
- hőmérséklet csúszka: A felszín hőmérséklete
- hosszú hullám: infravörös (hosszú hullám)
- láthatatlan: a szemünk nem látja

## 3. Légkör nélkül: jéghideg
Ha több megy ki, mint be, a felszín **hűl** – és hűlve egyre kevesebbet sugároz. Végül ==ki = be==: beáll az **egyensúly**.

Légkör nélkül ez mélyen fagypont alatt van (nézd a grafikont). A valódi átlag mégis {mai átlaghőmérséklet}. Mi melegít?

> megjegyzés: Bárhonnan indulsz, ugyanoda érsz – próbáld ki! Modell: a fényvisszaverés változatlan.

### Feliratok
- kezdő csúszka: Kezdő hőmérséklet
- egyensúlyi vonal: egyensúly, ki = be: #
- valódi vonal: a valódi átlag: #
- különbség: #
- idő tengely: idő →
- hőmérséklet tengely: hőmérséklet (°C)
- modell felirat: modell: kisugárzás = σ · T⁴

## 4. Az üvegházgázok
A levegő 99 %-a (nitrogén, oxigén) átengedi az infravöröset. A **vízgőz**, a **szén-dioxid (CO_2)** és a **metán** elnyeli, majd ==minden irányba== kisugározza: egy része visszajut a felszínre.

A felszín ettől melegebb lesz, amíg az űrbe újra annyi jut ki, amennyi bejön.

> megjegyzés: Ez az **üvegházhatás**. Természetes, és nélküle a Föld befagyna.

### Feliratok
- légkör nélkül gomb: Üvegházgázok nélkül
- légkörrel gomb: Üvegházgázokkal
- átengedi: átengedi: N₂, O₂
- elnyeli: elnyeli: H₂O, CO₂, CH₄
- tükör tévhit: Tükörként visszaveri?
- tükör helyes: elnyeli, és minden irányba kisugározza

## 5. Több CO_2: új egyensúly
Szén, kőolaj és földgáz elégetésekor **szén-dioxid** keletkezik. Az iparosodás előtt {CO₂ iparosodás előtt} volt a levegőben, ma {CO₂ ma} körül.

Több CO_2 → kevesebb infravörös jut ki → ==be > ki==, a Föld melegszik, amíg új egyensúly nem áll be.

> megjegyzés: Modell: CO_2-duplázásonként kb. {melegedés duplázásonként}. A valóságban ez évtizedekig tart.

### Feliratok
- CO₂ csúszka: CO₂ a levegőben
- égetés: szén, kőolaj, földgáz elégetése
- különbség mérő: be − ki (nagyítva)
- melegedés hőmérő: melegedés (modell)
- melegedés alap: 280 ppm-hez képest

### Adatok
- CO₂ iparosodás előtt: 280 ppm
- CO₂ ma: 427 ppm
- melegedés duplázásonként: 3 °C
- CO₂-hatás együtthatója: 5,35 W/m²

## 6. Világos és sötét felszín
A hó és a jég a napfény nagy részét **visszaveri**, a sötét óceán szinte mindet **elnyeli**.

Ha a melegedés miatt olvad a jég, sötétebb felszín kerül elő. Az több napfényt nyel el, és ez ==tovább melegít==: önerősítő kör.

> megjegyzés: Húzd a csúszkát! Hová kerül a jobb oldali felszín?

### Feliratok
- albedó csúszka: A jobb oldali felszín fényvisszaverése
- 100 egység: 100 egység napfényből
- visszaver: visszaver #
- elnyel: elnyel #
- friss hó: friss hó
- tengeri jég: tengeri jég
- sivatag: homoksivatag
- erdő: erdő
- óceán: nyílt óceán
- skála cím: fényvisszaverés (albedó)
- kör melegedés: melegedés
- kör olvad: olvad a jég
- kör sötét: sötétebb felszín
- kör elnyel: több elnyelt napfény

### Adatok
- friss hó fényvisszaverése: 85 %
- tengeri jég fényvisszaverése: 60 %
- sivatag fényvisszaverése: 35 %
- erdő fényvisszaverése: 12 %
- óceán fényvisszaverése: 6 %

## 7. Mit mutatnak a mérések?
A levegő CO_2-tartalma {CO₂ iparosodás előtt}-ről {CO₂ ma}-re nőtt, és most is évente kb. {CO₂ éves növekedése}-mel nő.

Az átlaghőmérséklet az utóbbi években már kb. ==1,3 °C-kal== magasabb, mint 1850–1900-ban.

Egy hideg tél ezt nem cáfolja: az **időjárás** napról napra változik, az **éghajlat** sok év átlaga.

> megjegyzés: Tízéves átlagok, kerekítve.

### Feliratok
- CO₂ grafikon: CO₂ a levegőben (ppm)
- hőmérséklet grafikon: melegedés 1850–1900-hoz képest (°C)
- iparosodás előtt: iparosodás előtt: #
- mérés forrása: jégfuratok, majd mérések (Mauna Loa)
- évtized: tízéves átlagok
- alapidőszak: 1850–1900 átlaga = 0
- hideg tél tévhit: Egy hideg tél cáfolja?
- hideg tél helyes: időjárás ≠ éghajlat

### Adatok
- CO₂ éves növekedése: 2,5 ppm
- adatok éve: 2025
- CO₂ 1850: 285 ppm
- CO₂ 1900: 296 ppm
- CO₂ 1950: 311 ppm
- CO₂ 1960: 317 ppm
- CO₂ 1970: 326 ppm
- CO₂ 1980: 339 ppm
- CO₂ 1990: 354 ppm
- CO₂ 2000: 369 ppm
- CO₂ 2010: 390 ppm
- CO₂ 2020: 414 ppm
- melegedés 1900-as évek: −0,1 °C
- melegedés 1910-es évek: −0,1 °C
- melegedés 1920-as évek: 0,1 °C
- melegedés 1930-as évek: 0,2 °C
- melegedés 1940-es évek: 0,3 °C
- melegedés 1950-es évek: 0,3 °C
- melegedés 1960-as évek: 0,3 °C
- melegedés 1970-es évek: 0,3 °C
- melegedés 1980-as évek: 0,5 °C
- melegedés 1990-es évek: 0,7 °C
- melegedés 2000-es évek: 0,9 °C
- melegedés 2010-es évek: 1,1 °C
- melegedés 2020–2024: 1,3 °C

## 8. A tengerszint emelkedése
Két ok emeli a tengert: a melegedő víz **kitágul**, és olvad a **szárazföldi** jég (gleccserek, Grönland, Antarktisz) – az olvadékvíz a tengerbe folyik.

Az ==úszó tengeri jég== olvadása viszont szinte nem emeli: a jég már most annyi vizet szorít ki, amennyi lesz belőle.

> megjegyzés: 1900 óta kb. {tengerszint-emelkedés 1900 óta}.

### Feliratok
- újra gomb: Olvaszd meg újra!
- úszó jég: úszó jég
- szárazföldi jég: jég a szárazföldön
- hőtágulás: melegedő víz
- nem emelkedik: nem emelkedik
- emelkedik: emelkedik
- olvadékvíz: olvadékvíz
- vízszint: vízszint
- felnagyítva: a tágulást # × felnagyítottuk
- tengerszint mérés: tengerszint 1900 óta: + #

### Adatok
- jég sűrűsége: 0,92 g/cm³
- víz hőtágulási együtthatója: 0,00021 1/°C
- melegítés a pohárban: 10 °C
- tágulás nagyítása: 100
- tengerszint-emelkedés 1900 óta: 20 cm

## 9. Összefoglalás
- A Föld hőmérsékletét a **bejövő napfény** és a **kimenő infravörös** egyensúlya szabja meg.
- Az üvegházgázok elnyelik és minden irányba kisugározzák az infravöröset. ==Ez természetes==; a gond a **felerősödése**.
- Több CO_2 → magasabb egyensúlyi hőmérséklet.
- Az ózonlyuk más jelenség: az UV-sugárzásról szól.

### Feliratok
- igaz: IGAZ
- hamis: HAMIS
- állítás káros: Az üvegházhatás káros, jobb lenne nélküle.
- válasz káros: a modell szerint nélküle # lenne az átlag
- állítás ózon: Az ózonlyuk okozza a melegedést.
- válasz ózon: az ózonréteg a Nap UV-sugárzását szűri – más jelenség
- állítás tükör: A gázok tükörként verik vissza a hőt.
- válasz tükör: elnyelik, és minden irányba kisugározzák
- állítás CO₂: Több CO₂ → melegebb egyensúly.
- válasz CO₂: duplázásonként kb. #
- állítás úszó jég: Az úszó jég olvadása emeli a tengert.
- válasz úszó jég: a szárazföldi jég és a hőtágulás emeli
- állítás tél: Egy hideg tél cáfolja a melegedést.
- válasz tél: az időjárás nem az éghajlat
