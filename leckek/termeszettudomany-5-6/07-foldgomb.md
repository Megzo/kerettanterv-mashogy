# Hol vagyunk a Földön? – földgömb, fokhálózat, fekvés, GPS
tantárgy: Természettudomány · évfolyam: 5–6. · témakör: 6. Topográfiai alapismeretek

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/termeszettudomany-5-6/07-foldgomb.md

  A „Tippelj!” lépésekben (1., 7.) a panel első bekezdése a kérdés; a többi bekezdés
  elmosódva látszik, és csak a tipp után válik olvashatóvá (a megoldás addig rejtve marad).
  A ## Közös feliratai: a „Tippelj! → kísérlet → magyarázat” sáv, a tipp-visszajelzés és a
  kísérlet-bélyegek (szerződés 17.) – a sorozat minden leckéjében ugyanígy szerepelnek.
  A tengelyferdeségből számolja a lecke a térítők és a sarkkörök helyét (4. és 8. lépés);
  Magyarország szélső értékei és a városok koordinátái a térképet is vezérlik.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kísérlet
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- otthon bélyeg: otthon is kipróbálhatod
- modell bélyeg: modell
- vázlatos bélyeg: vázlatos határok
- forgasd felirat: Húzd: forgasd meg a földgömböt!
- Budapest felirat: Budapest
- Egyenlítő felirat: Egyenlítő
- Ráktérítő felirat: Ráktérítő #
- Baktérítő felirat: Baktérítő #
- északi sarkkör felirat: északi sarkkör #
- déli sarkkör felirat: déli sarkkör #
- északi fok felirat: # É
- déli fok felirat: # D
- keleti fok felirat: # K
- Északi-sark felirat: Északi-sark
- forrás térkép felirat: Térkép: Natural Earth (közkincs)
- forrás domborzat felirat: Térkép: NOAA ETOPO 2022 domborzat, Natural Earth határok (közkincs)

### Adatok
- tengelyferdeség: 23,44°
<!-- forrás: IAU/IERS – a Föld tengelyferdesége 2026-ban 23,436°; átvéve a 05-ido és a 17-idojaras leckéből (ugyanez a kulcs) -->
- Budapest helye: 47,50° É, 19,04° K
<!-- forrás: Budapest földrajzi koordinátái két tizedesre kerekítve (pl. GeoNames, Wikipédia: 47° 29′ 33″ É, 19° 03′ 05″ K
     a városközpont); ugyanez: foldrajz-9-10/01-idozonak, 13-magyarorszag, termeszettudomany-5-6/17-idojaras -->
- domborzat: NOAA ETOPO 2022
<!-- forrás: shared/foldrajz/domborzat-karpat.js (NOAA NCEI ETOPO 2022 15″, közkincs) – az 5–7. lépés árnyékolt domborzata -->

## 1. Gömbből sík? – a narancshéj
A falitérképen Grönland majdnem akkora, mint Afrika. ==Melyik nagyobb valójában? Tippelj!==

A gömb héja nem terül ki simán: szétszakad, mint a narancshéj. A falitérkép a réseket **nyújtással** tölti ki, ezért északon mindent felfúj. ==Minden térkép torzít valamit.==

### Feliratok
- méret kérdés felirat: Melyik nagyobb valójában?
- Grönland tipp: Grönland
- egyforma tipp: kb. egyforma
- Afrika tipp: Afrika, sokkal
- falitérkép felirat: a falitérkép: a réseket nyújtással tölti ki
- narancshéj felirat: kiterítve: szétszakad, de a méretek igazak
- kiterítés csúszka: Nyújtsd ki a narancshéjat!
- Grönland felirat: Grönland
- Afrika felirat: Afrika
- Grönland terület felirat: Grönland: #
- Afrika terület felirat: Afrika: #
- arány felirat: Afrika kb. #-szer nagyobb!
- csúsztatott felirat: Grönland valódi mérete

### Adatok
- Grönland területe: 2,166 millió km²
<!-- forrás: Encyclopaedia Britannica, „Greenland” (2 166 086 km²), lekérdezve: 2026-11-24 -->
- Afrika területe: 30,37 millió km²
<!-- forrás: Encyclopaedia Britannica, „Africa” (kb. 30 365 000 km², a szigetekkel), lekérdezve: 2026-11-24 -->
- Afrika és Grönland aránya: kb. 14
<!-- forrás: a lecke számolja és ellenőrzi: 30,37 / 2,166 = 14,0 -->

## 2. Földrészek és óceánok
A Föld felszínének {óceánok aránya}-a **óceán**. A szárazföldet hét **földrészre** osztjuk. ==A Csendes-óceán nagyobb, mint az összes szárazföld együtt!== Forgasd a gömböt, és kattints rá: melyik földrész vagy óceán?

> megjegyzés: Van, aki hat földrészt számol: Amerikát egynek veszi. A Déli-óceánt sem minden könyv különíti el.

### Feliratok
- Európa felirat: Európa
- Ázsia felirat: Ázsia
- Afrika földrész felirat: Afrika
- Észak-Amerika felirat: Észak-Amerika
- Dél-Amerika felirat: Dél-Amerika
- Ausztrália felirat: Ausztrália és Óceánia
- Antarktisz felirat: Antarktisz
- Csendes-óceán felirat: Csendes-óceán
- Atlanti-óceán felirat: Atlanti-óceán
- Indiai-óceán felirat: Indiai-óceán
- Északi-sarki-óceán felirat: Északi-sarki-óceán
- Déli-óceán felirat: Déli-óceán
- kattints felirat: Kattints a gömbre! Megtaláltad: # / #
- földrészek felirat: hét földrész
- óceánok felirat: öt óceán
- óceán arány felirat: óceán: #
- szárazföld arány felirat: szárazföld: #
- Csendes-óceán gomb: Fordítsd a Csendes-óceán felé!
- Csendes terület felirat: Csendes-óceán: kb. #
- szárazföld terület felirat: összes szárazföld: kb. #

### Adatok
- óceánok aránya: kb. 71 %
<!-- forrás: CIA World Factbook, „World – Geography” (víz 70,9 %, szárazföld 29,1 %), lekérdezve: 2026-11-24 -->
- Csendes-óceán területe: kb. 165 millió km²
<!-- forrás: Encyclopaedia Britannica, „Pacific Ocean” (a peremtengerekkel kb. 165 250 000 km²), lekérdezve: 2026-11-24;
     más források 155–169 millió km² között adják (a peremtengerektől függ) -->
- szárazföld területe: kb. 149 millió km²
<!-- forrás: CIA World Factbook, „World – Geography” (szárazföld 148,94 millió km²), lekérdezve: 2026-11-24 -->

## 3. Rács a gömbön
A gömbre rajzolt rács a **fokhálózat**. A **szélességi körök** párhuzamosak az Egyenlítővel. A **hosszúsági körök** a két sarkot kötik össze. Két szám adja meg a helyet: szélesség és hosszúság. ==Keresd meg a {keresett pont} pontot!==

### Feliratok
- szélességi kör felirat: szélességi kör
- hosszúsági kör felirat: hosszúsági kör (délkör)
- kezdő délkör felirat: kezdő délkör: 0°
- Greenwich felirat: Greenwich (London)
- itt vagy felirat: itt: #
- feladat felirat: Keresd meg ezt a pontot!
- messze felirat: Még kb. # km-re vagy tőle.
- megvan felirat: Megtaláltad: ez Budapest!
- segítség gomb: Segítség: mutasd a két kört!
- szélesség felirat: szélesség (É vagy D)
- szélesség magyarázat felirat: hány fokkal van északra vagy délre?
- hosszúság felirat: hosszúság (K vagy Ny)
- hosszúság magyarázat felirat: hány fokkal van keletre vagy nyugatra?

### Adatok
- keresett pont: 47,5° É, 19° K
<!-- forrás: Budapest kerekített koordinátái (lásd: Budapest helye) – a feladat célpontja -->
- találati távolság: 150 km
<!-- forrás: a játék tűrése (választott érték): ennél közelebbi kattintás „megtalálta” -->

## 4. Nevezetes szélességi körök
A Föld tengelye {tengelyferdeség}-ot dől. Ezért a Nap délben csak a két **térítő** között kerülhet pontosan a fejünk fölé. A **sarkkörökön** túl nyáron le sem nyugszik, télen fel sem kel. ==Ezeket a köröket a Nap járása jelöli ki.==

> megjegyzés: Az évszakokról a 05-ös leckében tanultál.

### Feliratok
- zseblámpa felirat: zseblámpa = Nap
- nyár gomb: június 21.
- napéj gomb: március 20.
- tél gomb: december 21.
- dátum felirat: dátum: #
- zenit felirat: itt delel a Nap a fejünk fölött
- éjféli nap felirat: nem nyugszik le a Nap
- sarki éj felirat: fel sem kel a Nap
- tengely felirat: a Föld tengelye
- folt cím felirat: A napfény foltja délben
- folt zenit felirat: merőleges fény: kis, erős folt
- folt Budapest felirat: Budapesten: nagyobb, gyengébb
- napsugarak felirat: napsugarak
- vonal tévhit felirat: Csak vonalak a térképen?
- vonal válasz felirat: Nem: a Nap járása jelöli ki őket

## 5. Hol van Magyarország? – tényleges fekvés
A **tényleges fekvés** a fokhálózatban adja meg a helyet. Magyarország az északi és a keleti félgömbön van, {déli szélső pont} és {északi szélső pont} északi szélesség között. Budapest: =={Budapest helye}==. Kattints a térképre: hol laksz?

> megjegyzés: Keresd meg a lakóhelyedhez legközelebbi nagyvárost!

### Feliratok
- félút felirat: 45°: félúton
- skála Egyenlítő felirat: Egyenlítő 0°
- skála sark felirat: Északi-sark 90°
- skála ország felirat: Magyarország
- kattintás felirat: Kattints: kiírom a helyét!
- kattintott felirat: #
- terület felirat: területe kb. #
- Debrecen felirat: Debrecen
- Szeged felirat: Szeged
- Pécs felirat: Pécs
- Győr felirat: Győr
- Miskolc felirat: Miskolc
- északi félgömb felirat: északi félgömb
- keleti félgömb felirat: keleti félgömb

### Adatok
- déli szélső pont: 45° 44′
<!-- forrás: Magyarország szélső pontjai (Füzér/Nagy-Milic, Beremend, Felsőszölnök, Garbolc).
     A KSH STADAT 6.6.1.1 (Földrajzi alapadatok, lekérdezve: 2026-11-24) 45° 48′ – 48° 35′ É és 16° 05′ – 22° 58′ K
     értéket közöl; a Natural Earth 1:10m országhatárából mért szélsők (a lecke L.checks-e ezt ellenőrzi):
     45° 44,5′ É (Beremendtől délre), 48° 34,1′ É, 16° 05,6′ K, 22° 52,7′ K. A Beremend falu koordinátája 45° 44′ 13″ É
     (Wikipédia). A lecke értékei: déli 45° 44′ (Beremend alatt, határvonal), északi 48° 35′ (KSH; a 1:10m határon
     48° 34,1′), nyugati 16° 06′ (határvonal), keleti 22° 53′ (határvonal) – a KSH déli és keleti értéke ettől 4–5 percre
     eltér (ellenőrizendő: Nemzeti Atlasz / Lechner Tudásközpont). -->
- északi szélső pont: 48° 35′
<!-- forrás: mint a déli szélső pontnál (Natural Earth 1:10m határvonal, percre kerekítve; KSH STADAT 6.6.1.1) -->
- nyugati szélső pont: 16° 06′
<!-- forrás: mint a déli szélső pontnál (Natural Earth 1:10m határvonal, percre kerekítve; KSH STADAT 6.6.1.1) -->
- keleti szélső pont: 22° 53′
<!-- forrás: mint a déli szélső pontnál (Natural Earth 1:10m határvonal, percre kerekítve; KSH STADAT 6.6.1.1) -->
- Magyarország területe: kb. 93 000 km²
<!-- forrás: KSH STADAT 6.6.1.1 Földrajzi alapadatok (93 025 km²), lekérdezve: 2026-11-24 -->
- Debrecen helye: 47,53° É, 21,63° K
<!-- forrás: közismert – a városközpont koordinátája két tizedesre kerekítve (GeoNames / Wikipédia); ugyanez: termeszettudomany-5-6/17-idojaras -->
- Szeged helye: 46,25° É, 20,15° K
<!-- forrás: közismert – a városközpont koordinátája két tizedesre kerekítve (GeoNames / Wikipédia); ugyanez: termeszettudomany-5-6/17-idojaras -->
- Pécs helye: 46,07° É, 18,23° K
<!-- forrás: közismert – a városközpont koordinátája két tizedesre kerekítve (GeoNames / Wikipédia); ugyanez: termeszettudomany-5-6/17-idojaras -->
- Győr helye: 47,69° É, 17,65° K
<!-- forrás: közismert – a városközpont koordinátája két tizedesre kerekítve (GeoNames / Wikipédia); ugyanez: termeszettudomany-5-6/17-idojaras -->
- Miskolc helye: 48,10° É, 20,78° K
<!-- forrás: közismert – a városközpont koordinátája két tizedesre kerekítve (GeoNames / Wikipédia); ugyanez: termeszettudomany-5-6/17-idojaras -->

## 6. Kik a szomszédaink? – viszonylagos fekvés
A **viszonylagos fekvés** azt mondja meg, mihez képest hol vagyunk. Magyarország Közép-Európában, a **Kárpát-medence** közepén fekszik. Körben hegyek: Kárpátok, Alpok, Dinári-hegység. ==Hét szomszédunk van – kattints rájuk!==

### Feliratok
- szomszéd felirat: Megtalált szomszédok: # / #
- nem szomszéd felirat: nem szomszédunk
- Ausztria felirat: Ausztria
- Szlovákia felirat: Szlovákia
- Ukrajna felirat: Ukrajna
- Románia felirat: Románia
- Szerbia felirat: Szerbia
- Horvátország felirat: Horvátország
- Szlovénia felirat: Szlovénia
- Magyarország felirat: Magyarország
- Kárpátok felirat: Kárpátok
- Alpok felirat: Alpok
- Dinári felirat: Dinári-hegység
- Alföld felirat: Alföld
- medence felirat: Kárpát-medence: körben hegyek, középen síkság
- Duna felirat: Duna
- Tisza felirat: Tisza
- Balaton felirat: Balaton
- Kékes felirat: Kékes #
- Gerlach felirat: Gerlach-csúcs #
- megoldás gomb: Mutasd mind a hetet!

### Adatok
- Kékes magassága: 1014 m
<!-- forrás: KSH STADAT 6.6.1.1 Földrajzi alapadatok (Kékes, 1014 m), lekérdezve: 2026-11-24 -->
- Gerlach-csúcs magassága: 2655 m
<!-- forrás: a Kárpátok legmagasabb csúcsa (Gerlachfalvi-csúcs, Magas-Tátra, Szlovákia), közismert: 2654,4 m ≈ 2655 m
     (pl. Szlovák Földmérési Hivatal adata; ellenőrizendő a tankönyvi kerekítés: 2655 m) -->
- szomszédok száma: 7
<!-- forrás: közismert – Ausztria, Szlovákia, Ukrajna, Románia, Szerbia, Horvátország, Szlovénia; a lecke a felsorolt
     kulcsokból számolja és ellenőrzi -->

## 7. Honnan tudja a telefon, hol vagy?
A telefon a **GPS**-műholdak jeléből számolja ki a helyét. ==Hány műhold kell hozzá? Tippelj!==

Minden műholdtól tudjuk, milyen messze vagyunk: ez egy kör. Két kör két pontban metsződik, a harmadik dönt. Egy negyedik műhold az órát igazítja: ==ha {órahiba}-ot késik, a hiba {órahiba távolságban}!==

### Feliratok
- műhold kérdés felirat: Hány műhold kell, hogy tudd, hol vagy?
- egy tipp: 1 műhold
- kettő tipp: 2 műhold
- három tipp: 3–4 műhold
- műhold felirat: #. műhold
- távolság felirat: # km
- itt vagy gps felirat: Itt vagy: #
- egy kör felirat: 1 műhold: valahol ezen a körön
- két kör felirat: 2 műhold: a két metszéspont egyike
- három kör felirat: 3 műhold: egyetlen pont!
- húzd felirat: Húzd el a telefont!
- késik gomb: Késik az 1. műhold órája
- pontos gomb: Pontos az óra
- késik felirat: # késés → # hiba!
- műhold magasság felirat: a műholdak kb. # magasan
- jel ideje felirat: a jel kb. # alatt ér le
- műholdak felirat: legalább # műhold kering
- gps tévhit felirat: Az internetből tudja?
- gps válasz felirat: Nem: a műholdak jeléből, net nélkül is
- műhold alatt felirat: a műhold e pont fölött jár

### Adatok
<!-- forrás (az alábbiakra): GPS.gov, „Space Segment” (közepes Föld körüli pálya kb. 20 200 km magasan, naponta két
     kör; legalább 24 működő műhold) lekérdezve: 2026-11-24, közkincs -->
- GPS-műholdak magassága: kb. 20 200 km
- GPS-műholdak száma: 24
- fénysebesség: 299 792 km/s
<!-- forrás: közismert (299 792,458 km/s, SI-definíció); ugyanez: foldrajz-9-10/01-idozonak -->
- órahiba: 0,001 s
<!-- forrás: a terv példája (1 ezredmásodperc) -->
- órahiba távolságban: kb. 300 km
<!-- forrás: 0,001 s · 299 792 km/s = 299,8 km (a lecke kiszámolja és ellenőrzi) -->
- jel útja: kb. 0,07 s
<!-- forrás: 20 200 km / 299 792 km/s = 0,067 s, a műhold alatt állva (a lecke kiszámolja és ellenőrzi) -->

## 8. Összefoglalás
A Föld gömb, ezért **minden térkép torzít**. A **fokhálózat** két számmal megadja bármely pont helyét. A térítőket és a sarkköröket a ferde tengely jelöli ki. ==Magyarország a Kárpát-medencében, az északi félgömb mérsékelt övezetében fekszik.==

> megjegyzés: 9. osztályban a földrajzban az időzónákkal folytatod.

### Feliratok
- összefoglaló 1 felirat: Minden térkép torzít: a gömb nem terül ki.
- összefoglaló 2 felirat: 7 földrész, 5 óceán – 71 % víz
- összefoglaló 3 felirat: fokhálózat: szélesség + hosszúság
- összefoglaló 4 felirat: térítők, sarkkörök: a ferde tengely
- összefoglaló 5 felirat: Kárpát-medence, 7 szomszéd
- összefoglaló 6 felirat: GPS: 3 kör + 1 műhold az órához
- forró övezet felirat: forró övezet
- mérsékelt övezet felirat: mérsékelt övezet

<!-- Tanári megjegyzések és források:
  - Földrészek: a lecke hét földrészt mutat (Európa, Ázsia, Afrika, Észak-Amerika, Dél-Amerika, Ausztrália és Óceánia,
    Antarktisz); a panel kimondja, hogy van, aki hatot számol (Amerika egyben). Ellenőrizendő a használt tankönyv
    (NKP Természettudomány 5–6.) beosztása. Óceánok: Csendes-, Atlanti-, Indiai-, Északi-sarki- (Jeges-tenger) és
    Déli-óceán – a Déli-óceánt nem minden tankönyv különíti el.
  - A gömbön a földrészek határa vázlatos: a Natural Earth 1:110m országaiból színezve, Oroszország az Urál vonalát
    közelítő 60. hosszúsági körnél kettévágva; a Kaukázus és a Szuezi-csatorna menti határ nincs külön jelölve. Az
    óceánok határa a kattintásnál durva közelítés (hosszúsági és szélességi sávok) – a határ közelében téved.
  - 1. lépés: a narancshéj-kiterítés 12 darab, 30°-os „gerezd” (megszakított szinuszos vetület – területtartó); a
    falitérkép a Mercator-vetület, a térkép széle é. sz. 82° és d. sz. 58°. A csúsztatott Grönland a gömbön forgatva kerül
    Afrikára (alak és terület megmarad). A gyerekek otthon narancshéjjal kipróbálhatják.
  - 4. lépés: oldalnézet; a napsugarak párhuzamosak. A dátumgombok a napfordulók és a tavaszi napéjegyenlőség (2026)
    napját mutatják; az évszakok napja évről évre 1–2 napot változhat. A zseblámpafolt a 17-idojaras lecke rajza.
  - 5–6. lépés: a domborzat a NOAA ETOPO 2022 rácsából (átlagolt cellák, a csúcsok alacsonyabbak: ezért a Kékes és a
    Gerlach magasságát a lecke az adatsorból írja ki). Az országhatárok a Natural Earth 1:10m (Magyarország) és 1:50m
    (mai határok) rétegéből, a kattintható országterületek 1:110m-esek (vázlatos).
  - 7. lépés: síkbeli modell – a műholdakat egy-egy pont fölé képzeljük, a távolságköröket a térképre rajzoljuk.
    A valóságban kb. 20 200 km magasan keringenek, a távolságok gömbhéjak, és a negyedik műhold a telefon pontatlan
    óráját igazítja. A telefon helye (Szeged) és a műholdak talppontja kitalált példa.
  - A GPS internet nélkül is működik; a telefon a hálózatot csak a gyorsabb indításhoz használhatja (ezt 10–12 éveseknek
    nem részletezzük).
  - A „tengerparti Magyarország” tévhitet a terv javaslata szerint kihagytuk.
  - Kapcsolódás: tortenelem-5-6/13-felfedezesek (lapos Föld-tévhit, felfedezések – kiselőadás-téma);
    foldrajz-9-10/01-idozonak (helyi idő, időzónák, GPS-órahiba mikroszekundumban).
-->
