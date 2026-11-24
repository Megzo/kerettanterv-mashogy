# Honnan tudja a robot, hogy fal jön? – robot, szenzor, vezérlés
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 3. Robotika

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/07-szenzor.md

  A blokkok felirata a „… blokk” kulcsokból jön; a # a paraméter helye (szám, irány, feltétel).
  A „Tippelj!” lépésekben (1., 5.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A számolt értékek (visszhangidő, fékút, megtett út, mérések száma másodpercenként) a kódban
  készülnek az alábbi adatokból – kézzel nincsenek kiírva.
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
- blokknyelv bélyeg: a lecke saját blokkjai
- program felirat: A PROGRAM
- asztal felirat: AZ ASZTAL FELÜLRŐL
- indításkor blokk: indításkor
- indításkor vége: program vége
- lépj blokk: lépj előre # cm-t
- menj blokk: menj #
- előre opció: előre
- megállj blokk: állj meg
- fordulj blokk: fordulj # # fokot
- jobbra opció: jobbra
- amíg blokk: ismételd, amíg #
- amíg vége: ismétlés vége
- mindig blokk: ismételd mindig
- mindig vége: ismétlés vége
- ha-különben blokk: ha # akkor
- ha-különben közép: különben
- ha-különben vége: elágazás vége
- > blokk: # > #
- < blokk: # < #
- vagy blokk: # vagy #
- ütközik? blokk: ütközik
- távolság opció: távolság
- fény opció: fény
- igaz felirat: IGAZ
- hamis felirat: HAMIS
- kör felirat: #. kör
- futtatás gomb: Futtatás
- mért felirat: mért: #
- nincs visszhang felirat: nincs visszhang
- koccanás felirat: koccanás!
- koccanások felirat: koccanás: #

### Adatok
- hangsebesség: 343 m/s
<!-- forrás: 20 °C-os levegőben 331 m/s + 0,6 m/s · 20 ≈ 343 m/s – ugyanez a szám a fizika-7-8/12-hullam-hang leckében -->
- robot sugara: 6 cm (modell)
<!-- forrás: modell – egy kis iskolai padlórobot mérete nagyságrendileg (a lecke saját robotja) -->
- robot sebessége: 20 cm/s (modell)
<!-- forrás: modell – nagyságrendileg egy kis iskolai robot haladási sebessége -->
- fordulás sebessége: 180 °/s (modell)
<!-- forrás: modell – helyben fordulás, a két kerék ellentétes irányban forog -->
- mérési ciklus: 60 ms (becslés)
<!-- forrás: becslés – elterjedt iskolai ultrahangos modulok adatlapja legalább 60 ms-ot ajánl két mérés között (különben az előző visszhang zavar); típusnév szándékosan nélkül -->
- legkisebb mérhető távolság: 2 cm (becslés)
<!-- forrás: becslés – ugyanezen adatlapok szerint kb. 2 cm – 4 m a mérési tartomány; ennél közelebb a mérés megbízhatatlan (a lecke modelljében: nincs érvényes visszhang) -->
- legnagyobb mérhető távolság: 400 cm (becslés)
<!-- forrás: becslés – ugyanezen adatlapok szerint kb. 4 m; a lecke modellje „nincs visszhang” esetén is ezt a legnagyobb értéket adja a programnak -->
- mérési kúp: 15° (becslés)
<!-- forrás: becslés – az adatlapok kb. 15°-os mérési szöget adnak meg; valójában a kúp széle nem éles -->
- visszhang határszöge: 10° (modell)
<!-- forrás: modell – ennél ferdébb beesésnél a visszavert hang a lecke modelljében elkerüli a szenzort; a valóságban a felület érdességétől is függ -->
- fékezési idő: 0,25 s (modell)
<!-- forrás: modell – a robot nem áll meg azonnal; a fékút a kódban: sebesség · fékezési idő (20 cm/s-nál kb. 5 cm). Valódi kis robotoknál a motortól, a súlytól és a padlótól függ -->
- mérési zaj: 2 cm (modell)
<!-- forrás: modell – a „Zaj” gombbal minden méréshez legfeljebb ±2 cm véletlen eltérés adódik (seedelt, ismételhető). A valódi modulok adatlapja néhány mm-es pontosságot ír, de ferde, puha vagy kicsi tárgynál ennél jóval nagyobb a szórás -->
- fehér padló értéke: 90 (modell)
<!-- forrás: modell – a fényérzékelő 0–100-as skáláján; a valódi érték érzékelőnként és megvilágításonként más -->
- fekete szalag értéke: 10 (modell)
<!-- forrás: modell – mint fent -->

## 1. Vakon
A program: **lépj előre {tervezett út}-t**. A próbán bevált. A falat {fal eltolása}-rel közelebb toltuk. ==Mit tesz a robot? Tippelj!==

**Nekimegy.** A program nem tudja, hol a fal: vakon megy. Ehhez **szenzor** kell: egy alkatrész, amely mér a környezetben.

> megjegyzés: A robot modell: súrlódás, kerékcsúszás, akkumulátor nincs benne.

### Feliratok
- vak kérdés felirat: A falat 10 cm-rel közelebb toltuk. Mit tesz a robot?
- megáll tipp: megáll a fal előtt
- nekimegy tipp: nekimegy
- visszafordul tipp: visszafordul
- régi fal felirat: itt volt a fal
- közelebb felirat: # cm-rel közelebb
- tervezett felirat: tervezett út: #
- megtett felirat: megtett út: #

### Adatok
- tervezett út: 50 cm
<!-- forrás: a lecke példaprogramja -->
- fal eredeti távolsága: 55 cm
<!-- forrás: a lecke példája – a robot elejétől mérve; a próbán a robot 5 cm-re állt meg előtte -->
- fal eltolása: 10 cm
<!-- forrás: a lecke példája (a megtett út a kódban: 55 − 10 = 45 cm) -->

## 2. Érzékel – dönt – cselekszik
A szenzoros robot nem vakon megy. **Érzékel**: a szenzor megméri a távolságot. **Dönt**: a program összeveti {megállási távolság}-rel. **Cselekszik**: a motor megy vagy megáll. Ez a kör újra és újra lefut. ==Húzd el a falat!==

### Feliratok
- érzékel felirat: ÉRZÉKEL
- dönt felirat: DÖNT
- cselekszik felirat: CSELEKSZIK
- szenzor felirat: a szenzor mér
- program dönt felirat: a program összevet
- motor felirat: a motor forog
- kör sebesség felirat: kb. #-szer másodpercenként
- fal csúszka: A fal távolsága
- húzd a falat felirat: húzd a falat

### Adatok
- megállási távolság: 20 cm
<!-- forrás: a lecke példaprogramja (a feltételben álló szám) -->
- fal kezdeti távolsága: 85 cm
<!-- forrás: a lecke példája – a robot elejétől mérve -->

## 3. Ütköző és fényérzékelő
Az **ütköző** egy kapcsoló: IGAZ, ha nekiment valaminek, különben HAMIS. Csak az ütközés *után* jelez. A **fényérzékelő** a padlóról visszavert fényt méri: fehéren sokat, feketén keveset. ==Váltogasd a kettőt!==

### Feliratok
- ütköző gomb: Ütköző
- fényérzékelő gomb: Fényérzékelő
- ütköző állapot felirat: ütköző: #
- fény állapot felirat: mért fény: #
- fehér felirat: fehér
- fekete felirat: fekete
- fény küszöb felirat: küszöb
- szalag felirat: fekete szalag

### Adatok
- fény küszöbe: 50 (modell)
<!-- forrás: modell – a fehér (90) és a fekete (10) érték közepe -->
- ütköző fordulása: 120°
<!-- forrás: a lecke példaprogramja -->
- szalag fordulása: 150°
<!-- forrás: a lecke példaprogramja -->

## 4. Ultrahang: visszhangból távolság
Az **ultrahangos** szenzor rövid, magas hangot küld ({ultrahang frekvenciája} – ezt nem halljuk). A hang a falról visszaverődik. A program méri az időt, és számol: ==távolság = hangsebesség · idő / 2==. Miért kell osztani 2-vel?

> megjegyzés: A denevér is visszhanggal tájékozódik.

### Feliratok
- oda felirat: oda
- vissza felirat: vissza
- idő felirat: idő: #
- út felirat: oda és vissza: 2 · # = #
- képlet felirat: távolság = # · # / 2
- eredmény felirat: = #
- nem halljuk felirat: # – ezt nem halljuk (mi kb. #-ig hallunk)
- lassítás felirat: #-szor lassítva
- távolság csúszka: A fal távolsága
- mérés gomb: Új mérés

### Adatok
- ultrahang frekvenciája: 40 kHz (becslés)
<!-- forrás: becslés – az iskolai ultrahangos modulok jellemzően kb. 40 kHz-en működnek (adatlapok) -->
- emberi hallás felső határa: 20 kHz (becslés)
<!-- forrás: becslés – fiataloknál kb. 20 kHz, korral csökken -->
- mérés kezdeti távolsága: 100 cm
<!-- forrás: a lecke példája (1 m → oda-vissza 2 m → 2 / 343 s ≈ 5,8 ms – a kód számolja) -->
- animáció lassítása: 500
<!-- forrás: a lecke beállítása – a visszhang a valóságban néhány ezredmásodperc, a vásznon ennyiszer lassabb -->

## 5. Mikor téved a szenzor?
A fal most ferde. ==Mit mér a szenzor? Tippelj!==

**Túl nagyot vagy semmit.** A hang a ferde falról elpattan, mint a labda, és nem ér vissza. A puha függöny elnyeli. Ilyenkor a program a legnagyobb értéket kapja: azt hiszi, előtte szabad az út.

### Feliratok
- ferde kérdés felirat: Mit mér a szenzor egy ferde falnál?
- pontos tipp: pontos távolságot
- túl nagy tipp: túl nagyot vagy semmit
- kisebb tipp: kisebbet
- merőleges gomb: merőleges fal
- ferde gomb: ferde fal
- puha gomb: puha függöny
- valójában felirat: valójában: #
- a program kap felirat: a program ezt kapja: #
- elpattan felirat: a hang elpattan
- elnyeli felirat: a függöny elnyeli

### Adatok
- ferde fal szöge: 40°
<!-- forrás: a lecke példája (a merőlegeshez képest) -->
- ferde fal távolsága: 60 cm
<!-- forrás: a lecke példája – a robot elejétől a fal tengelyen mért pontjáig -->

## 6. Küszöb: mikor forduljon?
A program **küszöb**bel dönt: ha a mért távolság kisebb, fordul. Túl kicsi küszöbnél nekimegy a falnak: a szenzor csak időnként mér, a mérés zajos, és a robot nem áll meg azonnal. ==Próbáld ki gyors robottal, 5 cm-rel!==

### Feliratok
- küszöb csúszka: Küszöb
- sebesség csúszka: A robot sebessége
- zaj gomb: Zaj be / ki
- zaj be felirat: zaj: ±#
- zaj ki felirat: zaj: nincs
- fékút felirat: fékút: kb. #
- idő tengely: idő (s)
- távolság tengely: mért távolság (cm)
- küszöb felirat: küszöb: #

### Adatok
- küszöb kezdőértéke: 20 cm
<!-- forrás: a lecke példája (a csúszka 5 és 40 cm között állítható) -->
- futás hossza: 20 s
<!-- forrás: a lecke beállítása (ennyi ideig fut a modell) -->

## 7. Az akadálykerülő robot
Ez már **akadálykerülő** robot: mér, dönt, fordul. A ferde falat és a függönyt nem érzékeli, ezért **ütköző** is van rajta. Kapcsold be: ==a robot szemével==! Térképet nem lát, csak egy számot: amit a szenzor éppen mér.

### Feliratok
- szemével gomb: A robot szemével
- csak ennyit felirat: a robot ennyit tud: #
- térkép felirat: mi látjuk a pályát – a robot nem

### Adatok
- kerülő fordulás: 90°
<!-- forrás: a lecke példaprogramja -->
- akadálypálya futása: 30 s
<!-- forrás: a lecke beállítása -->

## 8. Összefoglalás
- A **robot** érzékel, a program dönt, a motor cselekszik – újra és újra.
- A **szenzor** egy számot vagy IGAZ/HAMIS jelet ad: ütköző, ultrahang, fényérzékelő.
- A szenzor tévedhet (ferde fal, zaj), ezért ==a küszöböt bőven adjuk meg==.

> megjegyzés: Építsetek akadálykerülő robotot az órán használt készlettel!

### Feliratok
- ütköző kártya: ÜTKÖZŐ – IGAZ vagy HAMIS
- ultrahang kártya: ULTRAHANG – távolság cm-ben
- fény kártya: FÉNYÉRZÉKELŐ – világosság 0–100
- tartomány felirat: kb. # – #
- visszhang felirat: a visszhang idejéből
- csak ütközés felirat: csak ütközés után
- padló felirat: a padlóról visszavert fény
- összegzés felirat: A ROBOT NEM LÁT – MÉR

<!-- Tanári megjegyzések és források:
  - A robot, a pálya, a falak és minden program kitalált példa; a szimuláció „modell” bélyeget kap.
    Elhagyja: súrlódás, kerékcsúszás, akkumulátor, a motorok egyenetlensége. A fékút egyetlen
    modellszám (fékezési idő · sebesség).
  - Az ultrahangos szenzor modellje: egy keskeny kúpban 9 sugár; egy sugár akkor ad visszhangot, ha a
    felületet legfeljebb a „visszhang határszöge” szerinti ferdeségben éri. A puha függöny elnyeli a
    hangot. Érvénytelen mérésnél (nincs visszhang, túl közel, túl messze) a program a legnagyobb
    értéket kapja – sok valódi könyvtár hasonlóan „nagy számot” vagy 0-t ad; ez eszközönként eltér.
  - A visszhang a vásznon lassítva látszik; a visszavert hullám íveinek középpontja a szenzor tükörképe
    a falon (síkfelületű visszaverődés).
  - Hangsebesség: 343 m/s (20 °C) – a fizika-7-8/12-hullam-hang leckével egyezik.
  - A fényérzékelő 0–100-as értékei (fehér 90, fekete 10, küszöb 50) modellértékek; a
    08-vonalkoveto lecke ugyanezt a skálát használja.
  - A lecke blokknyelve saját: az órán használt környezetben a blokkok másképp néznek ki, és a
    szenzorblokkok neve is más lehet. A „menj előre” itt folyamatos mozgás: a program minden
    körben újra dönt.
-->
