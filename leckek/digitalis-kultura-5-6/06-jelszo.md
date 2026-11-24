# Hány próbálkozás kell egy jelszóhoz? – online identitás és jelszó
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 2. Online kommunikáció

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/06-jelszo.md

  A „Tippelj!” lépésekben (3., 5. és 8.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A vásznon minden jelszó GÉPI PÉLDA (seedelt véletlen), mellette a „mostantól nem titok” bélyeg. A lecke
  nem mutat valódi vagy gyakori jelszót. Beviteli mező nincs: a diák saját jelszót nem ír be.
  Máté, Anna, a fiókok és az e-mail KITALÁLTAK. Hangnem (szerződés 19.): tájékoztat, nem ijesztget.
  Minden idő és lehetőségszám a lecke kódjából jön az alábbi adatokból – ha egy adatot átírsz, a vászon
  is változik.
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
- nem titok bélyeg: ezt ne használd – mostantól nem titok
- kisbetű felirat: kisbetű
- nagybetű felirat: nagybetű
- szám felirat: szám
- írásjel felirat: írásjel
- szó felirat: szó
- máté monogram felirat: M
- máté név felirat: Máté
- valaki monogram felirat: ?
- felhasználónév felirat: mate.k
- másodperc felirat: másodperc
- perc felirat: perc
- óra felirat: óra
- nap felirat: nap
- év felirat: év
- ezer év felirat: ezer év
- millió év felirat: millió év
- milliárd év felirat: milliárd év
- azonnal felirat: kevesebb mint 1 másodperc
- jegyű felirat: # jegyű szám
- szavak felirat: teve lámpa szivacs mókus gitár felhő zokni kalap répa tükör hajó csiga torta vonat sajt esernyő kréta bögre fóka sátor lufi kifli páva radír

### Adatok
- próbák másodpercenként: 1 milliárd próba/s (modell)
<!-- forrás: a lecke modellje, nagyságrendi becslés. Egy kiszivárgott, GYORSAN számolható jelszó-lenyomatlistán
     (MD5) egyetlen mai videokártya kb. 164 milliárd próbát tesz másodpercenként (hashcat-mérés, RTX 4090,
     hashcat.net fórum / Chick3nman benchmark; az RTX 5090-re 200 milliárd fölötti értékeket közölnek); LASSÚ
     tárolásnál (bcrypt, 10-es költség) 16 RTX 5090 együtt kb. 139 ezer próba/s (Hive Systems Password Table 2026,
     https://www.hivesystems.com/password). A valós sebesség tehát a tárolás módjától függően 10 ezerszer kisebb vagy
     százszor nagyobb is lehet. Lekérdezve: 2026-11-24. -->
- kisbetűk száma: 26
<!-- forrás: az angol ábécé 26 betűje (a jelszavakban jellemzően ékezet nélkül); az ASCII nyomtatható jelei -->
- nagybetűk száma: 26
<!-- forrás: ASCII A–Z -->
- számjegyek száma: 10
<!-- forrás: 0–9 -->
- írásjelek száma: 32
<!-- forrás: ASCII nyomtatható jelek: 95, ebből a szóköz 1, betű 52, számjegy 10 → 32 írásjel (! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~) -->
- szólista mérete: 7776 (modell)
<!-- forrás: a lecke modellje; a méret az EFF „dobókockás” szólistájáé (EFF Large Wordlist, 7776 = 6^5 szó,
     https://www.eff.org/dice). A szavakat a gép véletlenszerűen választja – ha az ember választ, kevésbé véletlen. -->

## 1. Ki vagy az interneten?
Belépéskor a **felhasználónév** mondja meg, ki vagy, a **jelszó** pedig bizonyítja. Együtt ez az **online identitásod**. A gép nem lát téged: ==csak azt ellenőrzi, egyezik-e a jelszó.== Aki tudja, a te nevedben léphet be.

> megjegyzés: A lecke jelszavai gépi példák.

### Feliratok
- belépés cím felirat: Belépés egy kitalált oldalra
- belépés felirat: Belépés
- felhasználónév címke felirat: felhasználónév
- jelszó címke felirat: jelszó
- belépés gomb felirat: Belépés
- szerver felirat: a weboldal gépe
- fiók felirat: fiók: mate.k
- egyezik felirat: Egyezik a jelszó?
- igen felirat: igen
- belépett felirat: belépett: Máté
- valaki felirat: valaki más
- tudja felirat: tudja Máté jelszavát
- gép csak felirat: A gép csak a jelszót ellenőrzi – nem azt, ki írta be.
- új jelszó gomb: Új példajelszó

## 2. Hány lehetőség van?
Egy **PIN-kód** minden jegye 10-féle lehet. A fán minden út egy lehetséges kód. ==Minden új jegy tízszer annyi utat ad.== Húzd a csúszkát: hány kód lesz 6 jegynél?

> megjegyzés: Ez a szorzási szabály: a matekórán is rajzolsz ilyen fát.

### Feliratok
- pin cím felirat: Hány # jegyű kód van?
- jegyek csúszka: jegyek száma
- jegy oszlop felirat: #. jegy
- jegy után felirat: # jegy:
- kódok felirat: lehetséges kód
- példa pin felirat: például:

### Adatok
- PIN hossza: 4
<!-- forrás: a bankkártyák és sok telefon alap PIN-kódja 4 jegyű (ISO 9564-1 4–12 jegyet enged); a lecke csak a
     fát rajzolja belőle -->

## 3. Hossz vagy bonyolultság?
Melyiket nehezebb kitalálni próbálgatással? ==Tippelj!==

Minden új jel **megszorozza** a lehetőségek számát. A vegyes jel nagyobb szorzó, de a rövid jelszó hamar véget ér. ==A hosszú utoléri, és messze lehagyja.== A **hossz** többet ér, mint a bonyolultság.

### Feliratok
- hossz kérdés felirat: Melyiket nehezebb kitalálni próbálgatással?
- rövid tipp: a rövid, vegyes
- hosszú tipp: a hosszú, csak kisbetűs
- egyforma tipp: egyformák
- rövid felirat: # jel – kis- és nagybetű, szám
- hosszú felirat: # jel – csak kisbetű
- szorzó felirat: jelenként × #
- sáv felirat: a sáv hossza: hány jegyű a lehetőségek száma
- bonyolult tévhit felirat: A bonyolult jelszó mindig erősebb?
- bonyolult válasz felirat: Nem: a hossz többet ér.

### Adatok
- rövid jelszó hossza: 8
<!-- forrás: a lecke példája (a 3. lépés tippje a terv szerint: 62^8 ≈ 2,2 · 10^14 vs 26^16 ≈ 4,4 · 10^22) -->
- hosszú jelszó hossza: 16
<!-- forrás: a lecke példája -->

## 4. A gép próbálgat
A **próbálgató gép** sorban végigpróbál minden lehetőséget. Állítsd a hosszt és a jelkészletet! Átlagosan a fele idő is elég. Belépéskor a **weboldal** pár rossz próba után letilt. De ha egy oldal jelszavai kiszivárognak, ==a gép korlát nélkül próbálgathat.==

### Feliratok
- gép cím felirat: A próbálgató gép
- sebesség felirat: # próba másodpercenként
- jelszó doboz felirat: a jelszó
- lehetőség felirat: lehetőség:
- próbál felirat: próbálgat…
- idő felirat: ennyi idő alatt próbál végig mindent:
- világegyetem felirat: a világegyetem kora
- online felirat: A weboldalon: pár rossz próba után letilt.
- hossz csúszka: jelek száma
- szavak csúszka: szavak száma
- kisbetű gomb: kisbetű
- nagybetű gomb: + nagybetű
- szám gomb: + szám
- írásjel gomb: + írásjel
- szavak gomb: véletlen szavak
- jelkészlet felirat: #-féle jel
- szólista felirat: #-féle szó

### Adatok
- világegyetem kora: 13,8 milliárd év
<!-- forrás: Planck Collaboration (2018/2020), Planck 2018 results VI, A&A 641, A6 – 13,787 ± 0,020 milliárd év -->

## 5. A szótár mindent előre próbál
Ez a jelszó megfelel a szabálynak: van benne nagybetű, szám és írásjel. ==Mennyi idő kell hozzá a gépnek? Tippelj!==

A gép nem vakon kezd. Előbb a gyakori jelszavakat és a **szótárat** próbálja: szavakat, neveket, évszámokat. A kutyanév + évszám + jel ==ilyen minta, ezért hamar sorra kerül.==

### Feliratok
- szótár kérdés felirat: Mennyi idő kell ehhez a jelszóhoz a gépnek?
- évek tipp: évek
- napok tipp: napok
- azonnal tipp: szinte azonnal
- minta szó felirat: Bodri
- minta évszám felirat: 2014
- minta jel felirat: !
- szabály felirat: megfelel a szabálynak:
- vakon felirat: Ha minden jelet sorban próbálna:
- szótár felirat: A szótár így próbál:
- szótár szavak felirat: szavak, nevek
- évszámok felirat: évszámok
- végjel felirat: jel a végén
- szótár példák felirat: Morzsa Cirmi Labda Csillag Mackó Pötty Bodri Szellő Maci Bogár
- végjelek felirat: ! ? . * # 1 + = $ @
- próba felirat: # próba
- elfogadta tévhit felirat: Elfogadta a weboldal, akkor jó?
- elfogadta válasz felirat: Nem: a szótár ismeri az ilyen mintát.

### Adatok
<!-- forrás (az alábbiakra): a lecke modellje, kitalált méretek. A valódi szótárak (kiszivárgott jelszólisták,
     névlisták, szólisták) ennél nagyobbak is lehetnek, de a minták (szó + évszám + jel) sorrendje ilyen. -->
- szótár szavai: 1 millió (modell)
- évszámok száma: 100 (modell)
- végjelek száma: 10 (modell)

## 6. Egy jelszó – sok fiók?
Máté öt fiókjában ugyanaz a jelszó. Egy játékoldal jelszavai kiszivárognak. ==Mi lesz a többi fiókkal?== Próbáld ki mindkét gombot! **Minden fiókhoz más jelszó** kell. Hogy jegyezd meg? Egy **jelszókezelő** program megőrzi őket – kérdezd a szüleidet.

### Feliratok
- fiókok cím felirat: Máté öt fiókja
- e-mail fiók felirat: e-mail
- iskola fiók felirat: iskola
- játék fiók felirat: játék
- videó fiók felirat: videó
- csevegő fiók felirat: csevegő
- szivárgás cím felirat: Adatszivárgás
- szivárgás felirat: Kiszivárogtak egy játékoldal jelszavai.
- nyitva felirat: nyitva
- zárva felirat: zárva
- ugyanaz gomb: mindenhol ugyanaz
- más gomb: mindenhol más
- nyitott fiókok felirat: kinyílt fiók: # / #
- mindenhova tévhit felirat: Egy jó jelszó elég mindenhova?
- mindenhova válasz felirat: Nem: ha kiszivárog, minden fiók nyitva.

## 7. Kétlépcsős azonosítás
A **kétlépcsős azonosítás** a jelszó mellé egy második lépést kér: egy kódot a telefonodra. Aki csak a jelszót tudja, ==a második lépésnél megakad.== Kapcsold ki és be! A kódot se add meg senkinek. Állítsd be szülővel együtt.

### Feliratok
- kétlépcsős cím felirat: Jelszó + kód a telefonodon
- kód címke felirat: kód a telefonodról
- kétlépcsős felirat: kétlépcsős azonosítás
- értesítés cím felirat: Belépési kód
- értesítés felirat: A kódod: #. Ne add meg senkinek!
- máté sor felirat: Máté: jelszó + kód
- valaki sor felirat: valaki más: csak a jelszó
- bejutott felirat: belépett
- megakadt felirat: megakadt: nincs meg a kód
- bejutott más felirat: belépett Máté nevében
- be gomb: bekapcsolva
- ki gomb: kikapcsolva
- felnőtt tévhit felirat: Csak a felnőtteknek kell?
- felnőtt válasz felirat: Neked is: kapcsold be egy szülővel.

### Adatok
- belépési kód jegyei: 6
<!-- forrás: a legtöbb hitelesítő alkalmazás és SMS-kód 6 jegyű (RFC 6238, TOTP: alapértelmezés 6 jegy) -->

## 8. Senkinek, még barátnak sem
Anna, a barátnőd, a jelszavadat kéri. ==Mit teszel? Tippelj!==

A jelszó csak a tiéd, ==még a legjobb barátodnak se add meg.== Jelszót senki nem kér üzenetben, a valódi szolgáltató sem. Ha valaki kéri, **ne válaszolj, és szólj egy felnőttnek**, akiben megbízol.

### Feliratok
- barát kérdés felirat: Anna, a barátnőd, a jelszavadat kéri. Mit teszel?
- megadom tipp: megadom, hiszen barátom
- nem adom tipp: nem adom meg
- később tipp: megadom, aztán megváltoztatom
- anna monogram felirat: A
- anna név felirat: Anna
- anna üzenet felirat: Szia! Add meg a jelszavad, felveszem helyetted a napi jutalmat a játékban!
- válasz üzenet felirat: Bocs, a jelszavam csak az enyém. De holnap segíthetek!
- levél feladó felirat: Feladó: ugyfelszolgalat@pelda.example
- levél tárgy felirat: Tárgy: Fiókod lejár! Írd meg a jelszavad!
- levél szöveg felirat: Válaszolj a jelszavaddal 24 órán belül, különben töröljük a fiókodat.
- gyanús bélyeg: gyanús
- senki nem kér felirat: Jelszót senki nem kér üzenetben – a valódi szolgáltató sem.
- biztonság felirat: Ha gyanús üzenetet kapsz, vagy valaki a jelszavadat kéri, ne válaszolj, és szólj egy felnőttnek, akiben megbízol.

## 9. Összefoglalás: hosszú, mindenhol más, kétlépcsős, titkos
Jó jelszó: **hosszú** és véletlen, például négy-öt véletlen szó. **Minden fiókhoz más.** Kapcsold be a **kétlépcsős azonosítást**. ==A jelszavad csak a tiéd.== Ha valaki kéri, szólj egy felnőttnek. Erős jelszóval is kell a többi lépés.

### Feliratok
- jó példa felirat: például 5 véletlen szó:
- hosszú cím felirat: Hosszú
- hosszú 1 felirat: 4–5 véletlen szó
- hosszú 2 felirat: nem a bonyolultság
- más cím felirat: Mindenhol más
- más 1 felirat: egy fiók, egy jelszó
- más 2 felirat: jelszókezelő segít
- kétlépcsős összegzés cím felirat: Kétlépcsős
- kétlépcsős 1 felirat: kód a telefonra
- kétlépcsős 2 felirat: szülővel állítsd be
- titok cím felirat: Csak a tiéd
- titok 1 felirat: barátnak sem
- titok 2 felirat: kérik? szólj!

<!-- Tanári megjegyzések és források:
  - Kitalált szereplők és adatok: Máté, Anna, a „mate.k” felhasználónév, a kitalált belépőoldal, az öt fiók, a
    játékoldal adatszivárgása, az e-mail (ugyfelszolgalat@pelda.example – foglalt példadomain, RFC 2606), a belépési
    kód. A vásznon „kitalált példa” bélyeg.
  - A vásznon minden jelszó a lecke által generált véletlen példa (seedelt), „ezt ne használd – mostantól nem titok”
    bélyeggel. Gyakori jelszólistát a lecke nem mutat. Ha az osztály rákérdez: az Egyesült Királyság kiberbiztonsági
    központja (NCSC) 2019-es elemzése szerint a kiszivárgott fiókok közt a „123456” volt a leggyakoribb jelszó (23,2
    millió fióknál), utána a „123456789” és a „qwerty” (NCSC, „Most hacked passwords revealed…”, 2019. április 21.,
    https://www.ncsc.gov.uk/news/most-hacked-passwords-revealed-as-uk-cyber-survey-exposes-gaps-in-online-security,
    lekérdezve: 2026-11-24). A „Bodri2014!” a lecke által kitalált MINTA (kutyanév + évszám + jel), nem listás jelszó.
  - Modell: a „próbálgató gép” másodpercenként 1 milliárd próbát tesz (modell). A valóságban a weboldalak a jelszót
    nem eredetiben, hanem „lenyomatként” (hash) tárolják; ha egy ilyen lista kiszivárog, a támadó gépe otthon,
    korlát nélkül próbálgat. A sebesség a tárolás módjától függ: gyors lenyomatnál (MD5) egyetlen videokártya kb. 164
    milliárd próba/s (hashcat-mérés, RTX 4090), lassú, erre tervezett lenyomatnál (bcrypt, 10-es költség) 16 csúcs-
    videokártya együtt is csak kb. 139 ezer próba/s (Hive Systems Password Table 2026, hivesystems.com/password,
    lekérdezve: 2026-11-24). A lecke számai tehát nagyságrendet mutatnak, nem pontos időt. A kiírt idő a TELJES keresésé
    (minden lehetőség); átlagosan a fele elég – ezt a panel a 4. lépésben kimondja.
  - Online próbálgatás: a belépőoldal korlátozza a hibás próbákat. A NIST SP 800-63B-4 (2025. július, 3.2.2) szerint
    legfeljebb 100 egymás utáni hibás próbát enged egy fióknál, utána letilt; sok szolgáltató ennél szigorúbb. A lecke
    ezért mondja: a veszély főleg a kiszivárgott adatoknál van.
  - Ajánlások (ellenőrizve a hivatalos forrásban, 2026-11-24):
    · NIST SP 800-63B-4, Digital Identity Guidelines: Authentication and Authenticator Management (2025. július,
      https://doi.org/10.6028/NIST.SP.800-63B-4, https://pages.nist.gov/800-63-4/sp800-63b.html), 3.1.1.2: ha a jelszó
      az egyetlen védelem, legalább 15 jel (többlépcsős azonosítás részeként legalább 8); legalább 64 jelet engedjenek;
      ne írjanak elő összetételi szabályt (kis-/nagybetű, szám keverését); NE kérjenek rendszeres jelszócserét (csak
      ha kiszivárgott); vessék össze a gyakori/kiszivárgott jelszavak tiltólistájával; engedjék a jelszókezelőt és a
      beillesztést.
    · NCSC (UK): „Three random words” (2021. december 21., https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/three-random-words)
      – három véletlen szó, vagy jelszókezelő; „Password policy: updating your approach” (2018,
      https://www.ncsc.gov.uk/collection/passwords/updating-your-approach) – a rendszeres kötelező jelszócsere inkább
      árt; nem javasolnak összetételi szabályt; javasolják a jelszókezelőt; kétlépcsős azonosítás (2-step
      verification) a fontos fiókokon, elsőként az e-mailen (NCSC Top tips, „Turn on 2-step verification”).
    A lecke „négy-öt véletlen szót” mond, mert a modellsebességen (1 milliárd próba/s, kiszivárgott lista) a 7776
    szavas listából 3 szó kb. 8 perc, 4 szó kb. 42 nap, 5 szó kb. 900 év. Az NCSC három szava belépőoldalon
    (korlátozott próbálgatásnál) bőven elég – a különbséget érdemes elmondani, ha egy diák rákérdez.
  - A rendszeres, kötelező jelszócserét a lecke nem tanítja (a NIST és az NCSC sem ajánlja); jelszót akkor kell
    cserélni, ha kitudódott vagy kiszivárgott.
  - Kétlépcsős azonosítás: a kódot a telefonra küldött üzenet vagy egy hitelesítő alkalmazás adja (RFC 6238, TOTP:
    6 jegy, 30 másodpercenként új). A 10–12 évesek fiókját jellemzően szülő kezeli – a lecke ezért mondja: „szülővel
    állítsd be”. Az új „belépőkulcs” (passkey) módszert a lecke nem tárgyalja.
  - Jelszókezelő: program, amely a jelszavakat titkosítva őrzi, és újakat generál. Márkanevet a lecke nem említ.
  - Adathalászat: a 8. lépés e-mailje kitalált, ártalmatlan példa. A részletek a 7–8. évfolyamon („internetes
    bűnözés”) jönnek.
  - Segítségkérés: szülő, tanár; Kék Vonal: 116-111 (ingyenes, névtelen, 0–24, https://kek-vonal.hu/, lásd a
    15-labnyom leckét). Életveszélyben 112.
  - A fa-diagram és a szorzási szabály a matematika-9-10/03-fa-diagram leckében részletesen; itt csak „ennyi út van”.
  - Az órán használt programban (iskolai fiók, e-mail) a kétlépcsős azonosítást a fiók biztonsági beállításainál
    találod; a lecke felülete kitalált, semleges.
-->
