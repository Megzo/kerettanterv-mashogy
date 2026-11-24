# Hány óra van most Tokióban? – helymeghatározás, helyi idő, időzónák
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 1. Tájékozódás a kozmikus térben és az időben

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/01-idozonak.md
  A számok az animációt is vezérlik: a koordinátákból számolja a lecke a helyi időt és a delelést,
  a zónaidőkből (UTC±…) az órákat és a repülés érkezési idejét, a fénysebességből a GPS-hibát.

  Egyszerűsítések (a panel kimondja, ahol számít):
  – a helyi idő itt helyi KÖZÉPidő: 15° = 1 óra; az időegyenlítést (az év során −14 … +16 perc)
    a lecke nem számolja, csak a 3. lépés megjegyzése említi;
  – a gömbön mindig napéjegyenlőség van (a Nap az Egyenlítő fölött delel, március 20. körül);
  – a zónatérkép normálidőt (téli időt) mutat, nyári időszámítás nélkül.
  Kapcsolódás: a Föld forgását és az évszakokat a fizika 7–8. „Miért van nappal és éjszaka?”
  (15-fold-forgasa) lecke magyarázza el; ez a lecke a következményekre megy tovább.
-->

## Közös

### Feliratok
- vázlatos: vázlatos
- modell: modell
- példa: példa
- forrás gömb: Időzónák: Natural Earth (2012-es állapot) + IANA tz javítások (2026) · normálidő, nyári időszámítás nélkül · Made with Natural Earth
- forrás térkép: Megyehatárok: Natural Earth 1:10m · helyi középidő (az időegyenlítés nélkül) · Made with Natural Earth
- Egyenlítő: Egyenlítő
- kezdő délkör: kezdő délkör (Greenwich)
- Greenwich: Greenwich
- Budapest: Budapest
- Debrecen: Debrecen
- Szombathely: Szombathely
- Tokió: Tokió
- New York: New York
- Sydney: Sydney
- Peking: Peking
- Újdelhi: Újdelhi
- Katmandu: Katmandu
- Kasgar: Kasgar
- Kiritimati: Kiritimati (Kiribati)
- Honolulu: Honolulu (Hawaii)
- csúszka UTC: Világidő (UTC)
- húzd: húzd a gömböt!
- másnap: másnap
- előző nap: előző nap
- óra perc: # óra # perc
- gomb nyári: Nyári időszámítás be / ki
- csak óra: # óra
- csak perc: # perc
- É: É
- D: D
- K: K
- Ny: Ny

### Adatok
<!-- forrás (az alábbiakra): közismert -->
- egy fordulat a Naphoz képest: 24 óra
- teljes kör: 360°
<!-- forrás (az alábbiakra): koordináták – közismert városközpont-értékek (Wikipédia / GeoNames), lekérdezve: 2026-11-24; Greenwich: a Királyi Csillagvizsgáló (Royal Observatory) délköre -->
- Budapest helye: 47,50° É, 19,04° K
- Debrecen helye: 47,53° É, 21,63° K
- Szombathely helye: 47,23° É, 16,62° K
- Greenwich helye: 51,48° É, 0,00° K
- Tokió helye: 35,68° É, 139,69° K
- New York helye: 40,71° É, 74,01° Ny
- Sydney helye: 33,87° D, 151,21° K
- Peking helye: 39,90° É, 116,40° K
- Újdelhi helye: 28,61° É, 77,21° K
- Katmandu helye: 27,72° É, 85,32° K
- Kasgar helye: 39,47° É, 75,99° K
- Kiritimati helye: 1,87° É, 157,40° Ny
- Honolulu helye: 21,31° É, 157,86° Ny
<!-- forrás (az alábbiakra): IANA tz database (tzdata, a 2026-os kiadás; Europe/Budapest, Asia/Tokyo, America/New_York, Asia/Shanghai, Asia/Kolkata, Asia/Kathmandu, Pacific/Kiritimati, Pacific/Honolulu), lekérdezve: 2026-11-24, közkincs; normálidő (téli idő). A lecke ellenőrzi, hogy a városok a zónatérképen (shared/foldrajz/idozonak.js) is ugyanebbe a zónába esnek. -->
- közép-európai idő: UTC+1
- nyári időszámítás: UTC+2
- Tokió zónaideje: UTC+9
- New York zónaideje: UTC−5
- Peking zónaideje: UTC+8
- Újdelhi zónaideje: UTC+5:30
- Katmandu zónaideje: UTC+5:45
- Kiritimati zónaideje: UTC+14
- Honolulu zónaideje: UTC−10
- időzóna-adat: Natural Earth, IANA tz (2026)
<!-- forrás: shared/foldrajz/idozonak.js – Natural Earth ne_10m_time_zones (2012-es állapot, közkincs) + a build_geodata.py javítótáblája az IANA tz database szerint (2026; pl. Kazahsztán 2024. március 1-jétől egységesen UTC+5), lekérdezve: 2026-11-23 -->

## 1. Hol vagy? A fokhálózat
A helyet két szöggel adjuk meg. A **földrajzi szélesség** az Egyenlítőtől mért szög észak vagy dél felé. A **földrajzi hosszúság** a greenwichi kezdő délkörtől mért szög kelet vagy nyugat felé. Ez a **helymeghatározás**.

Budapest: =={Budapest helye}==.

> megjegyzés: Válts várost, vagy forgasd meg a gömböt!

### Feliratok
- szélesség: szélesség
- hosszúság: hosszúság
- északi: északi szélesség (É)
- déli: déli szélesség (D)
- keleti: keleti hosszúság (K)
- nyugati: nyugati hosszúság (Ny)
- gomb Budapest: Budapest
- gomb Tokió: Tokió
- gomb New York: New York
- gomb Sydney: Sydney

## 2. Hosszúság = idő: 15° egy óra
A Föld {egy fordulat a Naphoz képest} alatt fordul egyet a Naphoz képest: ==óránként 15°-ot, fokonként 4 percet==. Ahol épp delel a Nap, ott **helyi** dél van. Ez a **helyi idő**.

Ami keletebbre van, ott előbb delel a Nap, ott „később” van.

> megjegyzés: A forgást a fizika „Miért van nappal és éjszaka?” leckéje mutatja be.

### Feliratok
- felülnézet: az Északi-sark fölül nézve
- napfény: napfény
- helyi napidő: helyi idő
- dél: dél
- éjfél: éjfél
- napkelte: napkelte
- napnyugta: napnyugta
- fok óra: 15° = 1 óra · 1° = 4 perc
- különbség cím: Mennyivel van előrébb Budapest?
- különbség fok: # − # = #
- különbség perc: # × 4 perc = #

## 3. Tévhit: délben 12 órakor delel a Nap?
**Tévhit:** délben 12:00-kor delel a Nap. Magyarország a 15° K délkör **zónaidejét** használja ({közép-európai idő}). Budapest ennél keletebbre van, ezért ==nálunk kb. negyedórával korábban delel==. Debrecenben még korábban.

> megjegyzés: Nyáron ({nyári időszámítás}) egy órával később. Az év során ±15 percet ingadozik (időegyenlítés) – ezt a lecke nem számolja.

### Feliratok
- tévhit: Délben 12:00-kor delel a Nap?
- 15 fok: 15° K – itt delel 12:00-kor
- delelés vonala: most itt delel a Nap
- delel: delel: #
- óra cím: közép-európai idő (CET)
- óra cím nyári: nyári idő (CEST)
- csúszka idő: Időpont
- Magyarország: Magyarország

## 4. Miért zónaidő? A vasút és Greenwich
Régen minden város a saját **helyi idejét** használta. A vasút menetrendjében ez zűrzavart okozott: ahány állomás, annyi idő.

{Délkör-konferencia}-ben Washingtonban Greenwich lett a kezdő délkör. Magyarország {CET bevezetése} napján tért át a közép-európai időre. ==Egy zónában mindenhol ugyanannyi az óra.==

> megjegyzés: Váltogasd: helyi idő vagy zónaidő? Melyikkel könnyebb menetrendet írni?

### Feliratok
- gomb helyi: Helyi idő
- gomb zóna: Zónaidő
- helyi cím: Helyi idő: mindenhol más
- zóna cím: Zónaidő: mindenhol ugyanannyi
- eltérés: Debrecen és Szombathely között: # perc
- vasút: vasútvonal
- konferencia sor: # – Washington: Greenwich a kezdő délkör
- bevezetés sor: # – Magyarországon közép-európai idő

### Adatok
- Délkör-konferencia: 1884
<!-- forrás: International Meridian Conference, Washington, 1884. október (közismert) -->
- CET bevezetése: 1890. november 1.
<!-- forrás: IANA tz database, Europe/Budapest (az 1890. november 1-jei átállás: a budapesti középidő → CET, kb. 16 perccel vissza), lekérdezve: 2026-11-24. Egy múzeumi katalógus (Sári Zsolt: A vasút fénykora, Szentendre, 2011) a vasúti bevezetést 1891-re teszi – ellenőrizendő a korabeli rendeletben. -->

## 5. Időzónák a gömbön
Az **időzóna** az a terület, ahol ugyanazt a **zónaidőt** használják. A tengereken szabályos 15°-os sávok, a szárazföldön ==országhatárokat követnek: politikai döntés szabja meg őket==.

Kína kb. {Kína kiterjedése}-ot fog át, mégis egyetlen zónát használ. India és Nepál fél-, illetve negyedórás eltéréssel számol.

> megjegyzés: Kattints egy zónára, húzd a csúszkát!

### Feliratok
- egész órás: egész órás eltérés
- nem egész: fél vagy negyed órás eltérés
- jelmagyarázat cím: Időzónák (normálidő)
- kattints: kattints egy zónára!
- kártya most: helyi idő most
- kártya Budapesthez: Budapesthez képest
- órák cím: Városok, most
- Kína: Kína: 1 zóna (UTC+8)
- Kasgar delel: Kasgarban a Nap kb. #-kor delel

### Adatok
- Kína kiterjedése: 62°
<!-- forrás: Kína szárazföldi része kb. 73° 33′ K és 135° 05′ K között (közismert; Wikipédia: Geography of China) → kb. 61,5°; Kína 1949 óta egyetlen hivatalos zónát (UTC+8, pekingi idő) használ (IANA tz: Asia/Shanghai). -->

## 6. A dátumválasztó vonal
Keletre haladva óránként előre kell állítani az órát. Körbeérve egy teljes napot nyernénk – ezért van a **dátumválasztó vonal**. ==Nyugat felé átlépve egy nappal előre ugrik a naptár, kelet felé egy nappal vissza.==

Nem pontosan a 180°-os délkör: kikerüli a szigetországokat.

> megjegyzés: Szamoa {Szamoa dátumugrása} napját kihagyta: átkerült a vonal túloldalára.

### Feliratok
- dátumnevek: március 19.; március 20.; március 21.
- 180 fok: 180° délkör
- dátumválasztó: Dátumválasztó vonal
- éjfél vonal: itt most éjfél van (helyi idő)
- jelmagyarázat dátum: Milyen nap van?
- azonos: ugyanannyi az óra – de más a nap!
- ugrás nyugat: nyugatra: +1 nap
- ugrás kelet: keletre: −1 nap

### Adatok
- Szamoa dátumugrása: 2011. december 30.
<!-- forrás: Szamoa 2011. december 29. után közvetlenül december 31-re ugrott (UTC−11 → UTC+13); IANA tz: Pacific/Apia, lekérdezve: 2026-11-24 -->

## 7. Utazás Tokióba
Budapestről indulsz, a repülés {repülési idő}. Mikor érsz Tokióba helyi idő szerint? ==Számolj világidőben (UTC)!== Az indulást váltsd át UTC-re, add hozzá a repülési időt, majd váltsd át Tokió zónaidejére ({Tokió zónaideje}).

> megjegyzés: Nyári időszámításkor Budapest UTC+2, Tokió marad UTC+9. A járat kitalált példa.

### Feliratok
- indulás: Indulás, Budapest
- érkezés: Érkezés, Tokió
- számolás cím: Számolás
- sz indulás: indulás (#)
- sz UTC: = világidőben
- sz repülés: + repülés
- sz érkezés UTC: = érkezés világidőben
- sz Tokió: érkezés Tokióban (#)
- főkör: legrövidebb út (főkör)
- gépen: eltelt a gépen: #
- csúszka indulás: Indulás (budapesti idő)
- gomb repül: Repülés újra

### Adatok
- repülési idő: 11,5 óra
<!-- forrás: kitalált példa (a terv briefje). Budapest–Tokió főköri távolsága kb. 9050 km (a lecke számolja); a menetrend szerinti Európa–Tokió járatok 11–14 órásak, az útvonaltól függően. -->
- kezdő indulás: 14 óra
<!-- forrás: kitalált példa -->

## 8. A GPS az időt méri
**Tévhit:** a GPS-műhold „lát” minket. Csak sugároz: a pontos atomórája idejét. A telefon a jel futásidejéből számol távolságot. =={órahiba} órahiba {órahiba távolságban} tévedést okoz.==

A telefon órája pontatlan. Úgy igazítja, hogy a körök egy pontban messék egymást – ehhez kell még egy műhold.

> megjegyzés: Térben négy műhold kell: három a helyhez, egy az órához.

### Feliratok
- műhold: műhold
- telefon: telefon
- Föld: Föld
- magasság: kb. # magasan
- futásidő: a jel kb. # alatt ér le
- nagyítás cím: nagyítás a telefon körül
- 100 m: 100 m
- valódi hely: valódi hely
- távolsághiba: minden kör # m-rel nagyobb
- távolsághiba kisebb: minden kör # m-rel kisebb
- egy pontban: a három kör egy pontban metszi egymást
- nem egy pontban: a körök nem egy pontban metszik egymást
- csúszka órahiba: A telefon órájának hibája
- gomb óra: Óra igazítása
- honnan típus: Honnan tudjuk?
- honnan cím: Az óra méri a helyet
- honnan régen: Régen
- honnan régen v: a hajón pontos óra (kronométer): a helyi dél és a greenwichi idő különbsége adja a hosszúságot
- honnan ma: Ma
- honnan ma v: a műholdak atomórái és a jel futásideje adják a távolságot
- honnan pontosság: Pontosság
- honnan pontosság v: 4 perc órahiba = 1° hosszúság; 1 µs = 300 m

### Adatok
- GPS-műholdak magassága: kb. 20 200 km
<!-- forrás: GPS.gov, „Space Segment” (közepes Föld körüli pálya, kb. 20 200 km, keringési idő kb. 12 óra; névlegesen 24 műhold), lekérdezve: 2026-11-24, közkincs -->
- GPS-műholdak száma: 24
<!-- forrás: GPS.gov, Space Segment – a névleges (alap)konstelláció 24 műhold; ténylegesen 30 körül működik -->
- fénysebesség: 299 792 km/s
<!-- forrás: közismert (299 792,458 km/s, SI-definíció) -->
- órahiba: 1 µs
<!-- forrás: a terv példája -->
- órahiba távolságban: 300 m
<!-- forrás: 1 µs · 299 792 km/s ≈ 300 m (a lecke kiszámolja és ellenőrzi) -->

## 9. Összefoglalás
- A helyet **két szög** adja meg: szélesség és hosszúság.
- 15° = 1 óra: ==keletebbre később van==.
- A **helyi idő** a Nap járásához igazodik, a **zónaidő** megállapodás.
- A zónák határait politikai döntések szabják meg.
- A dátumválasztó vonalon a naptár ugrik egy napot.
- A GPS is időt mér: a futásidőből számol helyet.

### Feliratok
- ö 1: A hely két szög: szélesség és hosszúság.
- ö 2: 15° = 1 óra, 1° = 4 perc: keletebbre később van.
- ö 3: A helyi idő a Naphoz, a zónaidő megállapodáshoz igazodik.
- ö 4: Az időzónák határai politikai döntések.
- ö 5: A dátumválasztó vonalon ugrik a naptár.
- ö 6: A GPS időt mér, és abból számol helyet.

<!-- Vitatott / bizonytalan pontok (tanári review):
  – A közép-európai idő hazai bevezetése: az IANA tz 1890. november 1-jét adja, egy vasúttörténeti katalógus
    1891-et (lásd a 4. lépés adatát). A pontos jogforrás (rendelet) ellenőrizendő.
  – A zónatérkép a Natural Earth 2012-es rétegéből és egy javítótáblából készül; néhány régió egyszerűsítve
    (Szaha egészében UTC+9, Grönland egészében UTC−2, Chihuahua határmenti községei nincsenek külön) –
    lásd shared/foldrajz/README.md. A Krím az adatban de facto moszkvai idővel, vitatott területként szerepel; a lecke gömbjén ez nincs külön jelölve (a zónák határa raszteres, a vitatott határ nem szaggatott).
  – A nyári időszámítás EU-s eltörléséről szóló 2018-as bizottsági javaslat a lecke készítésekor (2026) nem
    lépett hatályba – a lecke ezért nem említi; frissítendő, ha változik.
  – A repülési idő kitalált példa; a valódi útvonal (pl. az orosz légtér elkerülése) a főkörnél hosszabb lehet.
  – A GPS-ábra nem méretarányos („vázlatos”), és síkban (2D) mutatja a helymeghatározást: síkban 3 műhold kell
    (2 a helyhez, 1 az órához), térben 4.
-->
