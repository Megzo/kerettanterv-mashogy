# Hol tartja számon a gép a szavazatokat? – változó, adattípus, esemény
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 1. Algoritmizálás és blokkprogramozás

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/04-valtozo.md

  A blokkok felirata a „… blokk” kulcsokból jön; a # a paraméter helye (szám, változó, szöveg, kifejezés).
  A változók felirata a „… változó” kulcsokból jön (a doboz címkéje). A program szerkezete a kódban van.
  A „Tippelj!” lépésekben (3., 6.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A gép minden kiírt eredményt (összeg, összefűzés, „jövőre” értéke, a teszttábla) a programból számol.
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
- kitalált bélyeg: kitalált példa
- blokknyelv bélyeg: a lecke saját blokkjai
- program felirat: A PROGRAM
- változók felirat: A VÁLTOZÓK
- gép felirat: A SZAVAZÓGÉP
- indításkor blokk: indításkor
- indításkor vége: program vége
- kattintáskor blokk: ha rákattintanak erre: #
- kattintáskor vége: esemény vége
- legyen blokk: legyen # értéke #
- növeld blokk: növeld # értékét ennyivel: #
- + blokk: # + #
- összefűz blokk: # és # összefűzve
- kérdezd blokk: kérdezd meg: #
- válasz blokk: válasz
- mondd blokk: írd ki: #
- ha-különben blokk: ha # akkor
- ha-különben közép: különben
- ha-különben vége: elágazás vége
- és blokk: # és #
- ≥ blokk: # ≥ #
- ≤ blokk: # ≤ #
- vár változó: vár
- erdő változó: erdő
- szám változó: szám
- szöveg változó: szöveg
- válasz változó: válasz
- jövőre változó: jövőre
- hossz változó: hossz
- vár opció: vár gomb
- erdő opció: erdő gomb
- típus hiba: hiba: a + csak számmal számol
- igaz felirat: IGAZ
- hamis felirat: HAMIS
- futtatás gomb: Futtatás
- egy lépés gomb: Egy lépés
- alaphelyzet gomb: Alaphelyzet
- sebesség csúszka: Sebesség
- lassú felirat: lassú
- normál felirat: normál
- gyors felirat: gyors
- azonnal felirat: azonnal
- gép kérdés felirat: Hová menjünk kirándulni?
- vár gomb felirat: Várlátogatás
- erdő gomb felirat: Erdei túra
- szám típus: típusa: szám
- szöveg típus: típusa: szöveg
- kor kérdés: Hány éves vagy?
- jövőre szöveg: Jövőre ennyi éves leszel:
- bemenet felirat: bemenet
- kimenet felirat: kimenet
- képernyő felirat: a gép képernyője

### Adatok
- egy lépés hossza: 5 mm (modell)
<!-- forrás: modell – ugyanaz, mint a 02-ciklus lecke robotjáé (a blokkprogramozó környezetekben a „lépés” rendszerint képpont vagy a robot saját egysége) -->
- robot sebessége: 25 cm/s (modell)
<!-- forrás: modell – ugyanaz, mint a 02-ciklus leckében; a futás a Sebesség csúszkával gyorsítható -->
- fordulás sebessége: 180 °/s (modell)
<!-- forrás: modell – ugyanaz, mint a 02-ciklus leckében -->

## 1. A szavazógép: esemény
Hová menjen az osztály kirándulni? Kattints a gombokra! A kattintás egy **esemény**: elindítja a hozzá tartozó blokksort. Kattintás nélkül a program csak **vár** – magától semmit nem számol. ==Figyeld, melyik blokk fut!==

> megjegyzés: A szavazás és a szavazatszámok kitaláltak.

### Feliratok
- vár felirat: a program vár egy eseményre
- fut felirat: esemény történt: fut a blokksor
- kattintás felirat: kattintások: #
- osztály gomb: Szavaz az osztály
- nullázás gomb: Új szavazás
- kattints felirat: kattints!

### Adatok
- várra szavazók: 14 fő
<!-- forrás: kitalált példa (egy 25 fős osztály szavazatai) -->
- erdőre szavazók: 11 fő
<!-- forrás: kitalált példa -->

## 2. A változó: felcímkézett doboz
A **változó** egy felcímkézett doboz: a címke a neve, a tartalma az **értéke**. Egyszerre egy értéket tárol. Az új érték **felülírja** a régit. A „vár ← vár + 1” nem egyenlet: ==vedd ki, adj hozzá egyet, tedd vissza!==

### Feliratok
- doboz felirat: A „vár” DOBOZ
- kidobva felirat: a régi érték elvész
- nyíl alak felirat: # ← #
- matek felirat: matekórán: x = x + 1
- matek ítélet felirat: nincs megoldása
- program alak felirat: programban: x ← x + 1
- program ítélet felirat: x eggyel nő
- változódoboz felirat: így látod a programban:

### Adatok
- doboz kezdőértéke: 3
<!-- forrás: kitalált példa (a program első értékadása) -->

## 3. Szám vagy szöveg?
A gép kétféle adatot különböztet meg: **számot** és **szöveget**. Ez az adat **típusa**. ==Mi kerül a „szöveg” dobozba? Tippelj!==

**„55”.** Az összefűzés egymás mellé teszi a jeleket. A számokat a + összeadja: 5 + 5 = 10. Az „5” és az 5 nem ugyanaz! Kattints a számokra!

### Feliratok
- típus kérdés felirat: Mi kerül a „szöveg” dobozba?
- tíz tipp: 10
- ötvenöt tipp: 55
- hiba tipp: hibát jelez
- összead felirat: SZÁMOK
- összefűz felirat: SZÖVEGEK

## 4. Bemenet és kimenet
A program **bemenetet** kap – itt a válaszodat –, és **kimenetet** ad: kiírja az eredményt. A „kérdezd meg” válasza mindig **szöveg**: „11”. ==A + számmá alakítja, és hozzáad egyet.== Válassz másik választ!

### Feliratok
- válasz gombok felirat: válassz:

### Adatok
- próbaválaszok: 11; 10; 12 év
<!-- forrás: kitalált példa (5–6. osztályos diákok életkora) -->

## 5. Mi lesz a „tizenegy”-gyel?
És ha valaki betűvel írja: „tizenegy”? A + csak **számmal** tud számolni. Neked ez szám, a gépnek csak betűk sora: a program **hibával** megáll. ==A „11 év” is hibát ad – miért?==

> megjegyzés: Az órán használt környezet ezt másképp is kezelheti.

### Feliratok
- tizenegy válasz: tizenegy
- év válasz: 11 év
- jelek felirat: A VÁLASZ JELENKÉNT
- számjegy felirat: csak számjegy: szám
- nem szám felirat: nem csak számjegy: nem szám

## 6. Tesztelés szélsőséges bemenettel
Valaki ezt válaszolja: −3. ==Mit ír ki a program? Tippelj!==

**„−2”.** A gép kiszámolja, nem tudja, hogy értelmetlen. A **tesztelés**: szélsőséges bemenettel is kipróbáljuk (0, −3, 200). Javítsd egy feltétellel!

### Feliratok
- teszt kérdés felirat: A válasz: −3. Mit ír ki a program?
- hiba teszt tipp: hibát jelez
- mínusz kettő tipp: −2
- semmit tipp: semmit
- tábla felirat: TESZTTÁBLA
- bemenet oszlop: bemenet
- eredeti oszlop: eredeti
- javított oszlop: javított
- javítás gomb: Javítás: feltétellel
- rossz kor szöveg: Nem lehet a korod!
- értelmes felirat: zöld pipa: értelmes · piros X: hibás

### Adatok
- tesztbemenetek: 11; 0; −3; 200 év
<!-- forrás: kitalált példa (egy szokásos és három szélsőséges bemenet) -->
- legkisebb életkor: 6 év
<!-- forrás: kitalált példa – a javított program elfogadott tartománya (iskolás kor) -->
- legnagyobb életkor: 18 év
<!-- forrás: kitalált példa -->

## 7. Változó a ciklusban: spirál
Minden körben **nő** a hossz változó, így a robot egyre hosszabb szakaszt rajzol: spirál lesz. ==Kapcsold ki a „növeld” blokkot, vagy fordíts 91°-ot!==

### Feliratok
- ismételd blokk: ismételd #-szor
- ismételd vége: ismétlés vége
- lépj blokk: lépj előre # lépést
- fordulj blokk: fordulj # # fokot
- jobbra opció: jobbra
- balra opció: balra
- kör felirat: #. kör
- asztal felirat: AZ ASZTAL FELÜLRŐL
- növekmény csúszka: Növekmény (lépés)
- fordulás csúszka: Fordulás (fok)
- növeld gomb: „növeld” blokk ki/be
- nincs növeld felirat: „növeld” nélkül: mindig ugyanaz a négyzet

### Adatok
- spirál köreinek száma: 24
<!-- forrás: a lecke példaprogramja -->
- spirál kezdőhossza: 40 lépés
<!-- forrás: a lecke példaprogramja -->
- spirál növekménye: 5 lépés
<!-- forrás: a lecke példaprogramja -->
- spirál fordulása: 90°
<!-- forrás: a lecke példaprogramja (négyzetes spirál) -->

## 8. Összefoglalás
A **változó** felcímkézett doboz; az értékét a program írja át. Az adat **típusa** szám vagy szöveg. Az **esemény** indít el egy blokksort. A program **bemenetet** kap, **kimenetet** ad. Teszteld szélsőséges bemenettel is!

### Feliratok
- eredmény felirat: A SZAVAZÁS EREDMÉNYE
- változó kártya: változó: felcímkézett doboz, egy értékkel
- értékadás kártya: értékadás: az új érték felülírja a régit
- típus kártya: adattípus: 5 + 5 = 10, de „5” és „5” = „55”
- esemény kártya: esemény: a kattintás elindít egy blokksort
- be-ki kártya: bemenet → program → kimenet
- teszt kártya: tesztelés: 0, −3, 200 és „tizenegy” is

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a kirándulási szavazás (14 : 11 egy 25 fős osztályban), a válaszok (11, 10, 12,
    „tizenegy”, „11 év”, 0, −3, 200), az elfogadott életkor (6–18 év) és minden program a lecke saját példája.
  - Az „osztály szavazása” gomb 25 kattintást játszik le (a sorrendjük seedelt véletlen, a végeredmény a fenti
    két adat) – minden szavazat egy esemény, a gép egyszerre egy eseménykezelőt futtat, a többi sorban vár.
  - Adattípus: a lecke blokknyelvében a „+” csak számmal számol; a számjegyekből álló szöveget („11”, „−3”)
    számmá alakítja, más szövegre („tizenegy”, „11 év”) hibát ad. Az összefűzés mindig szöveget ad.
    Az órán használt környezetek ebben eltérnek: van, ahol a nem szám szöveg 0-nak számít (így a „tizenegy”-re
    „1” lenne az eredmény), van, ahol a „+” két szöveget összefűz („5” + „5” = „55”), és van, ahol hibát ad.
    Érdemes kipróbálni az órán használt programban.
  - A „kérdezd meg” válaszát itt csempéről választod (nincs billentyűzetes bevitel); a válasz mindig szöveg.
  - A változót a matematikai ismeretlennel szokás összekeverni: az x = x + 1 egyenletnek nincs megoldása,
    a programban a „legyen x értéke x + 1” (pszeudokódban x ← x + 1) értékadás: kiolvassa, hozzáad, visszaírja.
  - A tesztelés javított programja „és”-sel köti össze a két feltételt (≥ legkisebb, ≤ legnagyobb) – az
    elágazás a 03-elagazas lecke anyaga; a „tizenegy” bemenetre a javított program is hibát ad (ehhez a
    számmá alakíthatóság ellenőrzése kellene, ez a 7–8. évfolyam anyaga).
  - Modell-egyszerűsítések: a robot (7. lépés) pontosan annyit lép és fordul, amennyit a program mond; nincs
    súrlódás, kerékcsúszás, gyorsulás. A lépés 5 mm, a sebesség 25 cm/s, 180 °/s (modell, mint a 02-ben).
  - Spirál: a k-adik szakasz hossza kezdőhossz + (k − 1) · növekmény; 24 kör, 40 lépés kezdőhossz és 5 lépés
    növekmény mellett az utolsó szakasz 155 lépés (77,5 cm), a teljes út 2340 lépés (11,7 m) – a kód számolja.
    A 40 lépéses kezdőhossz azért kell, hogy „növeld” nélkül a négyzet (20 cm) ne bújjon a robot (12 cm) alá.
  - A blokknyelv a lecke saját nyelve (papír blokk, bal oldali kategóriasáv, behúzott törzs, „… vége” záró
    sáv). Az órán használt blokkprogramozó környezetben a blokkok színe, alakja és felirata eltér (pl. ott a
    változó értékét „legyen”, „változtasd” blokk állítja, az esemény „ha rákattintanak a szereplőre” lehet), a
    fogalmak (változó, értékadás, adattípus, esemény, bemenet, kimenet) ugyanazok.
-->
