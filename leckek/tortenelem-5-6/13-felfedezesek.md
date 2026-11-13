# Tényleg lapos Földben hittek? – Kolumbusz tévedése és a felfedezések
tantárgy: Történelem · évfolyam: 5–6. · témakör: 7. Új látóhatárok

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/tortenelem-5-6/13-felfedezesek.md

  Kerettanterv (7. Új látóhatárok, „A földrajzi felfedezések”): „A felfedezők útjai.” ·
  „A világkereskedelem kialakulása.” · „Gyarmatosítás Amerikában: az őslakosság sorsa, ültetvények
  és rabszolgák.” · Fogalmak: „gyarmat” · Személyek: „Kolumbusz Kristóf, Magellán” · Kronológia:
  „1492 Amerika felfedezése” · Topográfia: „Spanyolország, India, Kína” · Fejlesztési feladat:
  „A nagy felfedezők útjainak bemutatása térképen.”, „A világkereskedelem útvonalainak bemutatása
  térkép segítségével.” · Javasolt tevékenység: „Olyan termékek gyűjtése, amelyek a földrajzi
  felfedezéseknek köszönhetően kerültek a világkereskedelembe.” · Tanulási eredmény: „tisztában van
  a középkor és újkor világképének fő vonásaival”.

  Formátum-megjegyzések:
  – A földgömb a Natural Earth közkincs adataiból készül („Made with Natural Earth”), 1:110m.
    A partvonal mai állapotú. Országhatárt a lecke nem rajzol.
  – Az útvonalak VÁZLATOSAK: a kódban csak néhány töréspont van, köztük főkörív (a gömbön a
    legrövidebb út). A hajók valódi útja kanyargósabb volt. Az itt megadott helyek és dátumok
    mozgatják őket: a hajó két dátumos pont között egyenletes sebességgel halad.
  – A 2. lépés ábrája nem méretarányos: a szöget háromszorosára nagyítja (bélyeg jelzi).
  – A 3. lépés modellje: a Föld a Kanári-szigetek (La Gomera) szélességi körén, felülről nézve.
    Japán nyugati távolsága = a kör hossza − Európa és Ázsia hossza (keletre, Japánig).
    Kolumbusz Ázsia-hosszát a kód a két Kolumbusz-féle adatból számolja; a valódit a La Gomera és
    Japán koordinátáiból. A két csúszka e két érték között mozog.
  – A 7. lépés kártyáinak helyes oszlopa a kódban van (kukorica, burgonya, paradicsom, kakaó,
    paprika, dohány → Amerikából; ló, búza, szarvasmarha, cukornád, himlő → Amerikába).
  – A 8. lépés 100 alakja jelkép (1 alak = az őslakosok 1 %-a 1492 előtt), nem létszám.
    A fogyás tartományát a halványan csíkozott alakok jelzik (bizonytalan sáv).
  – A felirat-sablonokban a # jel helyére a lecke számot ír.
-->

## Közös

### Feliratok
- forrás jel: forrás
- rekonstrukció jel: rekonstrukció
- monda jel: monda
- vázlatos: vázlatos
- becslés: becslés
- illusztráció: illusztráció
- Kr. e.: Kr. e.
- Kr. u.: Kr. u.
- század: század
- év sablon: # év
- január: január
- február: február
- március: március
- április: április
- május: május
- június: június
- július: július
- augusztus: augusztus
- szeptember: szeptember
- október: október
- november: november
- december: december
- km sablon: # km
- húzd: húzd meg a gömböt!
- Európa: EURÓPA
- Afrika: AFRIKA
- Ázsia: ÁZSIA
- Amerika: AMERIKA
- Atlanti-óceán: Atlanti-óceán
- Csendes-óceán: Csendes-óceán
- Indiai-óceán: Indiai-óceán
- Spanyolország: Spanyolország
- Portugália: Portugália
- India: India
- Kína: Kína
- Japán: Japán
- Kanári-szigetek: Kanári-szigetek
- Lisszabon: Lisszabon
- Jóreménység foka: Jóreménység foka
- Zöld-foki-szigetek: Zöld-foki-szigetek
- Kolumbusz útja: Kolumbusz, 1492
- da Gama útja: da Gama, 1497–1498
- Magellán útja: Magellán és Elcano, 1519–1522
- csúszka dátum: Dátum

### Adatok
- Föld kerülete: 40 075 km
- La Gomera helye: 28,09° É, 17,11° Ny
- Japán helye: 35,7° É, 139,7° K
- Lisszabon helye: 38,72° É, 9,14° Ny
- Jóreménység foka helye: 34,36° D, 18,47° K
- Zöld-foki-szigetek helye: 14,92° É, 23,51° Ny
- Kína helye: 34° É, 108° K
- India helye: 21° É, 78° K

## 1. Tényleg lapos Földben hittek?
Sokan ma is azt hiszik, hogy a középkorban mindenki lapos Földben hitt. ==Ez tévhit.==

A művelt európaiak tudták, hogy a Föld **gömb**. Egyetemi tankönyvekből tanulták, és a királyok gömböt tartottak a kezükben. A tévhit a 19. században terjedt el.

> megjegyzés: Forgasd meg a földgömböt!

### Feliratok
- tévhit: tévhit
- tévhit szöveg: „A középkorban azt hitték,
- tévhit szöveg 2: hogy a Föld lapos.”
- Sacrobosco cím: Sacrobosco: A gömbről
- Sacrobosco sor: egyetemi tankönyv, # körül
- országalma cím: Az országalma
- országalma sor: a király kezében, a világ jelképe
- Behaim cím: Behaim földgömbje, #
- Behaim sor: a legrégebbi ma is meglévő földgömb
- Behaim sor 2: Amerika még nincs rajta
- Irving cím: Honnan jön a tévhit?
- Irving sor: Washington Irving regényes könyvéből
- Irving sor 2: Kolumbuszról (#) és követőitől

### Adatok
- Sacrobosco könyve: 1230 körül
- Behaim földgömbje: 1492
- Irving könyve: 1828

## 2. Eratoszthenész megméri a Földet
**Eratoszthenész** görög tudós {Eratoszthenész mérése}-ben megmérte a Földet. A nyári napforduló delén Szüénében a Nap a kutak aljáig sütött. Alexandriában ugyanekkor a bot árnyéka {árnyék szöge}-os szöget mutatott: ez a kör ötvened része. ==A kerület tehát 50 × 5000 sztadion.==

> megjegyzés: Húzd a csúszkát!

### Feliratok
- Nap: a Nap
- napsugarak: párhuzamos napsugarak
- Szüéné: Szüéné
- Szüéné ma: ma Asszuán
- Alexandria: Alexandria
- kút: kút: nincs árnyék
- bot: bot: van árnyék
- középpont: a Föld középpontja
- ív: # sztadion
- felnagyítva: a szög felnagyítva
- számítás cím: Eratoszthenész számítása
- sor kör: 360° ÷ # = 50
- sor kerület: 50 × # sztadion
- sor eredmény: = # sztadion
- sztadion: 1 sztadion = # m
- eredmény km: ≈ # km
- valódi km: valójában: #
- sztadion vita: Nem tudjuk biztosan, milyen
- sztadion vita 2: hosszú sztadiont használt.
- forrás cím: Honnan tudjuk?
- forrás sor: Eratoszthenész könyve elveszett.
- forrás sor 2: Kleomédész görög tudós írta le,
- forrás sor 3: évszázadokkal később.
- csúszka sztadion: Egy sztadion hossza

### Adatok
- Eratoszthenész mérése: Kr. e. 240 körül
- árnyék szöge: 7,2°
- Alexandria–Szüéné távolság: 5000 sztadion
- rövid sztadion: 157,5 m
- hosszú sztadion: 185 m

## 3. Kolumbusz számítása
Kolumbusz is tudta, hogy a Föld gömb. De **kisebbnek** hitte: kerületét {Kolumbusz Földjének kerülete}-re becsülte. Ázsiát pedig hosszabbnak gondolta. ==Ezért Japán szerinte csak {Japán távolsága Kolumbusz szerint}-re volt nyugatra a Kanári-szigetektől.== Valójában több mint négyszer ilyen messze van.

### Feliratok
- felülnézet: felülnézet: az Északi-sark fölül
- Kolumbusz Földje: Kolumbusz Földje
- valódi Föld: a valódi Föld
- Eurázsia: Európa és Ázsia
- óceán: óceán
- Japán K: Japán – Kolumbusz szerint
- Japán valódi: Japán valójában
- kártya Kolumbusz: Kolumbusz becslése
- kártya modell: Ha így lenne
- kártya valóság: A valóság
- kerület sor: a Föld kerülete:
- Japán sor: Japán nyugatra:
- amerika kérdés: Mi van az óceán közepén?
- csúszka kerület: A Föld kerülete
- csúszka Ázsia: Európa és Ázsia hossza

### Adatok
- Kolumbusz Földjének kerülete: kb. 30 000 km
- Japán távolsága Kolumbusz szerint: kb. 4400 km

## 4. 1492: partot értek
{indulás Palosból} **Kolumbusz Kristóf** három hajóval indult el a spanyol uralkodók megbízásából. A Kanári-szigetektől a **passzátszél** egyenletesen vitte nyugat felé. {partraszállás} hajnalán partot értek. ==Kolumbusz azt hitte, Ázsiába ért.== De ott már emberek éltek: a **taínók**.

> megjegyzés: Húzd a dátum-csúszkát!

### Feliratok
- s4 cím: Kolumbusz első útja
- Palos: Palos
- Guanahani: Guanahani
- Guanahani ma: ma San Salvador
- Hispaniola: Hispaniola
- Azori-szigetek: Azori-szigetek
- passzátszél: passzátszél
- passzátszél sor: egész évben északkeletről fúj
- nyugati szél: nyugati szelek
- odaút: odaút
- hazaút: hazaút
- Ázsia hitte: „Ez Ázsia!” – hitte Kolumbusz
- taínók: taínók
- aztékok: aztékok
- maják: maják
- inkák: inkák
- vikingek: vikingek, #
- vikingek sor: régészeti lelet
- napló típus: írott forrás
- napló cím: Kolumbusz naplója
- napló ki: Ki írta?
- napló ki v: Kolumbusz, napról napra
- napló mi: Megvan?
- napló mi v: Csak Las Casas kivonata; az eredeti elveszett.
- napló kortárs: Kortárs?
- napló kortárs v: Las Casas igen, de az első úton nem volt ott.
- esemény út: az első út
- kivonat: kivonat
- később év: kb. # évvel később

### Adatok
- indulás Palosból: 1492. augusztus 3.
- érkezés La Gomerára: 1492. augusztus 12.
- indulás La Gomeráról: 1492. szeptember 6.
- partraszállás: 1492. október 12.
- Hispaniola elérése: 1492. december 5.
- indulás haza: 1493. január 16.
- Azori-szigetek elérése: 1493. február 18.
- Lisszabon elérése: 1493. március 4.
- hazaérkezés: 1493. március 15.
- Las Casas kivonata: 1530 körül
- vikingek Amerikában: 1000 körül
- Palos helye: 37,23° É, 6,89° Ny
- Guanahani helye: 24,05° É, 74,50° Ny
- Hispaniola helye: 19,75° É, 72,20° Ny
- Azori-szigetek helye: 36,97° É, 25,10° Ny
- L'Anse aux Meadows helye: 51,60° É, 55,53° Ny
- taínók helye: 20,5° É, 76,0° Ny
- aztékok helye: 19,43° É, 99,13° Ny
- maják helye: 18,5° É, 89,0° Ny
- inkák helye: 13,53° D, 71,97° Ny

## 5. Afrika körül Indiába
A portugálok kelet felé, Afrika megkerülésével keresték az utat Indiába. **Vasco da Gama** Lisszabonból indult ({da Gama indulása}). Megkerülte a **Jóreménység fokát**, és elérte Indiát ({Calicut elérése}). ==Megnyílt a tengeri út a fűszerekhez.== A bors addig sok kereskedő kezén át, drágán jutott Európába.

> megjegyzés: Húzd a dátum-csúszkát!

### Feliratok
- s5 cím: Vasco da Gama útja
- Malindi: Malindi
- Calicut: Calicut
- Calicut ma: ma Kozhikode
- Velence: Velence
- Dias: Bartolomeu Dias már járt itt: #
- fűszerek: bors, fahéj, szegfűszeg
- régi út: a régi út: sok kereskedő kezén át
- új út: az új, tengeri út
- da Gama hazaút: hazaút, #

### Adatok
- Dias a fokon: 1488
- da Gama indulása: 1497. július 8.
- Jóreménység foka megkerülése: 1497. november 22.
- Malindi elérése: 1498. április 14.
- Calicut elérése: 1498. május 20.
- da Gama hazaérkezése: 1499
- Malindi helye: 3,22° D, 40,12° K
- Calicut helye: 11,25° É, 75,78° K
- Aden helye: 12,80° É, 45,03° K
- Alexandria helye: 31,20° É, 29,92° K
- Velence helye: 45,44° É, 12,33° K

## 6. Magellán: körbe a Földön
**Magellán** öt hajóval indult nyugatnak ({Magellán indulása}), hogy Amerikát megkerülve érje el a Fűszer-szigeteket. A Csendes-óceán sokkal nagyobb volt, mint hitték. Magellán a Fülöp-szigeteken harcban meghalt. **Elcano** vezette haza az utolsó hajót. =={hazatérők száma} tért vissza: ők kerülték meg először a Földet.==

### Feliratok
- s6 cím: Magellán és Elcano útja
- Sanlúcar: Sanlúcar
- Rio: Rio de Janeiro-öböl
- San Julián: San Julián: telelés
- Magellán-szoros: Magellán-szoros
- Guam: Guam
- Mactan: Mactan
- Mactan sor: Magellán halála
- Mactan sor 2: Lapu-Lapu harcosai győztek
- Fűszer-szigetek: Fűszer-szigetek
- hajók: hajók: #
- emberek indult: indult: #
- emberek hazatért: hazatért: #
- Victoria név: Victoria
- Victoria: csak a Victoria ért haza
- Pigafetta cím: Pigafetta naplója
- Pigafetta sor: résztvevő volt, a hazatérők egyike

### Adatok
- Magellán indulása: 1519. szeptember 20.
- Rio elérése: 1519. december 13.
- San Julián elérése: 1520. március 31.
- San Julián elhagyása: 1520. augusztus 24.
- Santiago hajótörése: 1520. május
- San Antonio visszafordulása: 1520. november
- szoros vége: 1520. november 28.
- Guam elérése: 1521. március 6.
- Magellán halála: 1521. április 27.
- Concepción felégetése: 1521. május
- Tidore elérése: 1521. november 8.
- Tidore elhagyása: 1521. december 21.
- Trinidad lemaradása: 1521. december
- Jóreménység foka Elcano: 1522. május
- Zöld-foki-szigetek Elcano: 1522. július 9.
- Elcano hazaérkezése: 1522. szeptember 6.
- hajók száma: 5
- indulók száma: kb. 240–270 fő
- hazatérők száma: 18 fő
- Sanlúcar helye: 36,78° É, 6,35° Ny
- Rio helye: 22,90° D, 43,17° Ny
- San Julián helye: 49,31° D, 67,73° Ny
- Magellán-szoros helye: 53,50° D, 70,90° Ny
- Guam helye: 13,44° É, 144,79° K
- Mactan helye: 10,30° É, 123,97° K
- Tidore helye: 0,68° É, 127,40° K

## 7. Mi utazott a hajókon?
A hajók nemcsak embereket vittek. Amerikából új növények jutottak az **Óvilágba**: Európába, Ázsiába, Afrikába. Amerikába lovat, búzát, szarvasmarhát vittek – és betegségeket. Ez a **kolumbuszi csere**. ==Húzd a kártyákat a helyükre!==

> megjegyzés: Melyik lepett meg?

### Feliratok
- zóna Amerikából: Amerikából az Óvilágba
- zóna Amerikából sub: Európába, Ázsiába, Afrikába
- zóna Amerikába: Az Óvilágból Amerikába
- zóna Amerikába sub: Európából és Afrikából
- kukorica: kukorica
- burgonya: burgonya
- paradicsom: paradicsom
- kakaó: kakaó
- paprika: paprika
- dohány: dohány
- ló: ló
- búza: búza
- szarvasmarha: szarvasmarha
- cukornád: cukornád
- himlő: himlő (betegség)
- kész számláló: # / # jó helyen
- paprika cím: A paprika is Amerikából jött!
- paprika sor: Magyarországon a 16. században jelent meg.
- gomb megoldás: Megoldás
- gomb újra: Újra

## 8. Az őslakosok és a rabszolgák
Az amerikai **őslakosok** közül nagyon sokan meghaltak. Főleg a behurcolt betegségek pusztítottak, például a himlő: ezek ellen nem volt védettségük. Ehhez jött a háború és a kényszermunka. A **gyarmatokon**, az európaiak uralta földeken ültetvények épültek. ==A munkára afrikai embereket hurcoltak oda rabszolgának.==

### Feliratok
- s8 cím: Az őslakosok
- előtte: 1492 előtt
- utána: kb. 100 évvel később
- jelkép: 1 alak = az őslakosok 1 %-a
- fogyás: sok vidéken # kevesebben
- bizonytalan: bizonytalan
- ok 1: főleg himlő, kanyaró és más járványok
- ok 2: és háború, kényszermunka, éhezés
- Brazília: Brazília
- Karib-szigetek: Karib-szigetek
- iparcikkek: iparcikkek, fegyverek
- elhurcoltak: elhurcolt afrikaiak
- termények: cukor, dohány, gyapot
- ültetvények: ültetvények
- rabszolgák sor: # ember, a 16–19. században
- gomb előtte: 1492 előtt
- gomb utána: 100 évvel később

### Adatok
- őslakosok fogyása: 80–90 % (becslés)
- elhurcolt afrikaiak: kb. 12,5 millió fő
- Nyugat-Afrika helye: 6,36° É, 2,08° K
- Brazília helye: 12,97° D, 38,50° Ny

## 9. Összefoglalás
A művelt európaiak tudták, hogy a Föld gömb. Kolumbusz a **méretét** becsülte alá, ezért hitte közelinek Ázsiát – és Amerikába ért. Da Gama Afrika körül jutott Indiába, Magellán és Elcano hajója megkerülte a Földet. ==A kontinensek összekapcsolódtak: növények, állatok, betegségek és emberek indultak útnak.==

### Feliratok
- ö cím: Új látóhatárok
- ö gömb: A Föld gömb: ezt a művelt európaiak tudták.
- ö méret: Kolumbusz kicsinek hitte a Földet, nagynak Ázsiát.
- ö csere: Növények, állatok, betegségek és emberek
- ö csere 2: indultak útnak – két irányba.
- ö Dias: Dias a fokon
- ö Kolumbusz: Kolumbusz Amerikában
- ö da Gama: da Gama Indiában
- ö Magellán: az első Föld körüli út

<!-- Vitatott / bizonytalan pontok (tanári és szakmai review-hoz):
  – Eratoszthenész (Kr. e. 240 körül; a pontos év ismeretlen): az eljárást Kleomédész „Az égitestek
    körkörös mozgásáról” című munkája írja le; Kleomédész kora bizonytalan (Kr. e. 1. – Kr. u. 2.
    század között), ezért „évszázadokkal később”. A 7,2° (a kör 1/50-e), az 5000 sztadion és a
    250 000 sztadion Kleomédésznél szerepel; más források 252 000 sztadiont írnak. A sztadion hossza
    vitatott: kb. 157,5 m („egyiptomi”) és 185 m („attikai”) a két leggyakoribb érték → kb. 39–46 ezer km.
    A valódi kerület az Egyenlítőn 40 075 km (a délkörön 40 008 km).
  – Kolumbusz becslése: Alfraganus (al-Fargháni) 56⅔ mérföldes fokát római mérföldnek vette, ebből kb.
    30 ezer km-es kerület jön ki (kb. 25 %-kal kevesebb a valódinál). Japánt (Cipangut) kb. 2400 tengeri
    mérföldre (kb. 4400 km) gondolta a Kanári-szigetektől (S. E. Morison feldolgozása); a valódi távolság
    nyugat felé kb. 10 600 tengeri mérföld (kb. 19 600 km). A lecke a 28. szélességi körön, a koordinátákból
    kb. 20 000 km-t számol. Mindhárom szám becslés; a források kissé eltérnek.
  – A „lapos Föld” mítosz: a középkori tudósok (pl. Beda, Sacrobosco „De sphaera”, kb. 1230) gömbnek
    tudták a Földet. A tévhitet Washington Irving 1828-as, részben kitalált Kolumbusz-életrajza és
    19. századi szerzők (Letronne, Draper, White) terjesztették (J. B. Russell: Inventing the Flat
    Earth, 1991). Az egyszerű emberek világképéről kevés forrásunk van – ezért „a művelt európaiak”.
  – Az országalma a magyar koronázási jelvények része, a 14. század első feléből (Anjou-címerrel); a
    gömb a világ (a földkerekség) jelképe, nem földrajzi térkép.
  – Behaim „Erdapfel”-je (Nürnberg, 1490–1492) a legrégebbi fennmaradt földgömb.
  – Guanahani azonosítása a mai San Salvador-szigettel a legelfogadottabb, de vitatott (pl. Samana Cay).
    A naplót Las Casas kivonatából ismerjük; a kivonat keltezése bizonytalan (az 1530-as évek körül,
    mások későbbre teszik), ezért „kb.”.
  – A vikingek (Leif Eriksson) Új-Fundlandon, L'Anse aux Meadows-nál jártak; a régészeti lelet kb.
    1000 körüli (egy faévgyűrű-vizsgálat 1021-et adott).
  – Da Gama hazaérkezésének napja forrásonként eltér (1499. augusztus vége – szeptember), ezért csak az év.
    Malindi elérése: 1498. április 14. (ellenőrizendő).
  – Magellán: az indulók száma forrásonként 237 és kb. 270 között van; a Victoria 18 emberrel érkezett
    Sanlúcarba (néhány forrás szerint 3 molukkai is volt a fedélzeten); később további túlélők is
    hazajutottak. A hajók elvesztésének hónapjai: Santiago (hajótörés) 1520. május, San Antonio
    (visszafordult) 1520. november, Concepción (felégették) 1521. május, Trinidad (Tidorén maradt)
    1521. december. A Jóreménység fokát 1522 májusában kerülték meg (a nap forrásonként eltér).
    Pigafetta résztvevő volt, naplója a fő forrás.
  – Kolumbuszi csere: a paprika (Capsicum) Amerikából származik; Magyarországon a 16. század második
    felében tűnt fel („törökbors” néven) – hogy pontosan milyen úton (török vagy délszláv közvetítéssel),
    vitatott. A cukornád eredetileg Új-Guineából/Ázsiából való, az európaiak vitték Amerikába.
  – Az őslakosok fogyása: az Amerika 1492 előtti népességére adott becslések nagyon eltérnek (kb. 8 és
    100 millió között). Sok vidéken (Karib-szigetek, Mexikó középső része, Andok) egy évszázad alatt
    kb. 80–90 %-os fogyást becsülnek, a Karib-szigeteken még nagyobbat. A legtöbb halált a járványok
    (himlő, kanyaró, influenza) okozták; ehhez jött a háború, a kényszermunka (encomienda) és az éhezés.
    A szám becslés, vitatott; a lecke tartományt mutat.
  – Atlanti rabszolga-kereskedelem: a Trans-Atlantic Slave Trade Database (slavevoyages.org) szerint
    kb. 12,5 millió embert hurcoltak hajóra 1501 és 1866 között, kb. 10,7 millió érkezett meg élve.
    A 8. lépés nyilai vázlatosak (Európa → Nyugat-Afrika → Amerika → Európa), a legfőbb célterület
    Brazília és a Karib-térség volt.
  – Dátumok: a 15–16. századi dátumok a Julián-naptár szerintiek (ahogy a források írják).
  – Térképadat: Natural Earth 1:110m, közkincs („Made with Natural Earth”).
-->
