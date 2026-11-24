# Hogyan lesz a faluból térkép? – alaprajz, méretarány, jelek, domborzat
tantárgy: Természettudomány · évfolyam: 5–6. · témakör: 5. Alapvető térképészeti ismeretek (és 7. Gyakorlati jellegű térképészeti ismeretek)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/termeszettudomany-5-6/06-terkep.md

  A „Tippelj!” lépésekben (3., 5.) a panel első bekezdése a kérdés; a többi bekezdés
  elmosódva látszik, és csak a tipp után válik olvashatóvá (a megoldás addig rejtve marad).
  A ## Közös feliratai: a „Tippelj! → kísérlet → magyarázat” sáv, a tipp-visszajelzés és a
  bélyegek (szerződés 17.) – ezek a sorozat minden leckéjében ugyanígy szerepelnek.
  Tóvölgy kitalált falu: a házak, az utak, a domb helye a kódban van (geometria), a domb
  magassága és a szintköz itt, az Adatok alatt – ha átírod, a térkép és a számolás is változik.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kísérlet
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- kitalált bélyeg: kitalált példa
- modell bélyeg: modell
- iskola felirat: iskola
- templom felirat: templom
- patak felirat: patak
- híd felirat: híd
- tó felirat: tó
- kilátó felirat: kilátó
- erdő felirat: erdő
- sportpálya felirat: sportpálya
- Tóvölgy felirat: Tóvölgy
- méretarány felirat: méretarány: #
- egy cm felirat: 1 cm = #

## 1. Felülről nézve: alaprajz
Ez Tóvölgy, egy kitalált falu. Húzd a csúszkát: emelkedj a falu fölé! Felülről a házakból téglalapok lesznek: ez az **alaprajz**. ==A térkép felülnézeti kép.== Az autót, a felhő árnyékát nem rajzoljuk rá.

> megjegyzés: Rajzold le felülről az osztálytermet: hol a tábla, az ajtó, a padok?

### Feliratok
- nézőpont csúszka: Nézőpont
- ferde érték felirat: ferdén
- felülről érték felirat: felülről
- alaprajz érték felirat: alaprajz
- ferde felirat: ferdén, madártávlatból
- felülről felirat: felülről nézve
- alaprajz felirat: alaprajz: a házak körvonala felülről
- fénykép tévhit felirat: A térkép olyan, mint egy fénykép?
- fénykép válasz felirat: Nem: csak a tartós, fontos dolgok

### Adatok
- első méretarány: 1 : 1000
<!-- forrás: a lecke választása – az 1. lépés rajzán 1 cm (a vásznon 40 képpont) 10 m-nek felel meg -->

## 2. Kicsinyítés: a méretarány
A térkép a valóság **kicsinyített** képe. A **méretarány** megmutatja, hányszor kisebb. Az 1 : 10 000 azt jelenti: ==1 cm a térképen 10 000 cm, vagyis 100 m a valóságban.== Húzd a mérőszalag végeit! A **vonalas aránymérték** rajzban mutatja ugyanezt.

### Feliratok
- húzd felirat: Húzd a mérőszalag két végét!
- cm felirat: cm
- térképen felirat: a térképen: #
- valóságban felirat: a valóságban: #
- számolás felirat: # cm · # = # cm = # m
- aránymérték felirat: vonalas aránymérték

### Adatok
- térkép méretaránya: 1 : 10 000
<!-- forrás: a lecke választása (a 2., 4. lépés térképe) -->
- százezres méretarány: 1 : 100 000
<!-- forrás: példa a táblázatba -->
- milliós méretarány: 1 : 1 000 000
<!-- forrás: példa a táblázatba -->
- egy cm a tízezres térképen: 100 m
<!-- forrás: számolás – 1 cm · 10 000 = 10 000 cm = 100 m; a lecke a méretarányból is kiszámolja és ellenőrzi -->
- egy cm a százezres térképen: 1 km
<!-- forrás: számolás – 1 cm · 100 000 = 100 000 cm = 1000 m = 1 km (a lecke ellenőrzi) -->
- egy cm a milliós térképen: 10 km
<!-- forrás: számolás – 1 cm · 1 000 000 = 10 km (a lecke ellenőrzi) -->

## 3. Nagyobb terület, kevesebb részlet
Két egyforma lap, ugyanaz a hely. ==Melyiken látszik több részlet: az 1 : 10 000-esen vagy az 1 : 100 000-esen? Tippelj!==

Az 1 : 10 000-esen! A másikra tízszer szélesebb táj fér, a falu csak egy folt. ==Nagyobb szám a kettőspont után: nagyobb terület, kevesebb részlet.==

### Feliratok
- részlet kérdés felirat: Melyik térkép mutat több részletet?
- tízezres tipp: az 1 : 10 000-es
- százezres tipp: az 1 : 100 000-es
- egyforma tipp: egyformán
- méretarány csúszka: A jobb oldali lap méretaránya
- lap felirat: a lap szélessége: # cm = #
- házak szint felirat: minden ház, minden fa
- utcák szint felirat: házsorok, utcák
- folt szint felirat: a falu egy folt
- város szint felirat: csak a városok, a folyók
- Tóvölgy kitalált felirat: Tóvölgy (kitalált)
- Eger felirat: Eger
- Miskolc felirat: Miskolc
- Tisza felirat: Tisza
- forrás alaptérkép felirat: Térkép: Natural Earth (vizek, határok), NOAA ETOPO 2022 (domborzat)

### Adatok
- Tóvölgy helye: 47,92° É, 20,55° K
<!-- forrás: kitalált példa – a kitalált falut a Bükkalja környékére tettük; a jel nem valódi települést jelöl -->
- Eger helye: 47,90° É, 20,38° K
<!-- forrás: átvéve a foldrajz-9-10/13-magyarorszag leckéből (megyeszékhelyek) -->
- Miskolc helye: 48,10° É, 20,78° K
<!-- forrás: átvéve a 07-foldgomb leckéből -->

## 4. Jelek és égtájak
A térkép nyelve a **jelkulcs**. A térkép teteje általában észak. A főégtájak közé jönnek a **mellékégtájak**, például az északkelet (ÉK). ==Kattints arra, ami az iskolától északkeletre van!== A terepen tájold a térképet az iránytűvel!

> megjegyzés: Keresd meg az iskolád udvarán, merre van észak!

### Feliratok
- jelkulcs cím: Jelkulcs
- ház jel felirat: ház
- főút jel felirat: főút
- földút jel felirat: földút
- kattints felirat: Kattints: mi van az iskolától ÉK-re?
- jó kattintás felirat: Igen! A templom az iskolától északkeletre van.
- rossz kattintás felirat: # → az iskolától #. Próbáld újra!
- É irány felirat: északra
- ÉK irány felirat: északkeletre
- K irány felirat: keletre
- DK irány felirat: délkeletre
- D irány felirat: délre
- DNy irány felirat: délnyugatra
- Ny irány felirat: nyugatra
- ÉNy irány felirat: északnyugatra
- É felirat: É
- ÉK felirat: ÉK
- K felirat: K
- DK felirat: DK
- D felirat: D
- DNy felirat: DNy
- Ny felirat: Ny
- ÉNy felirat: ÉNy
- iránytű felirat: iránytű
- itt állsz felirat: itt állsz, a templom felé nézel
- tájold gomb: Tájold a térképet!
- tájolatlan felirat: tájolatlan: a két É nem egyezik
- tájolt felirat: tájolva: a két É egy irányba mutat

## 5. A domb szeletei: szintvonalak
Szeleteljük fel a dombot {szintköz}-enként, és nézzük a vágásokat felülről! ==Hol meredekebb: ahol sűrűk, vagy ahol ritkák a vonalak? Tippelj!==

Ahol sűrűk! A **szintvonal** az egyforma magasságú pontokat köti össze. ==Sűrű vonalak: meredek lejtő. Ritkák: lankás.== Próbáld ki a csúszkát!

### Feliratok
- meredek kérdés felirat: Hol meredekebb a domb?
- sűrű tipp: ahol sűrűk a vonalak
- ritka tipp: ahol ritkák a vonalak
- mindegy tipp: mindegy
- szintköz csúszka: Szintköz
- szelet felirat: vágás: # m
- felülről nézve felirat: felülről nézve: szintvonalak
- metszet felirat: oldalnézet: nyugat → kelet
- meredek felirat: sűrű vonalak: meredek
- lankás felirat: ritka vonalak: lankás
- kilátó magasság felirat: kilátó: #
- torzítás felirat: függőleges torzítás #×
- méretarányos felirat: méretarányos
- szintvonal tévhit felirat: A szintvonal egy út a dombon?
- szintvonal válasz felirat: Nem: egyforma magasságú pontok

### Adatok
- szintköz: 10 m
<!-- forrás: a lecke választása (kitalált példa); a csúszka 5–25 m között állítja. Turistatérképen jellemzően 10 m. -->
- Kilátó-domb magassága: 312 m
<!-- forrás: kitalált példa – a domb modelljét a lecke úgy méretezi, hogy a teteje ennyi legyen (ellenőrzi) -->

## 6. Zöld, sárga, barna: a domborzati térkép
A **domborzati térkép** színei a magasságot mutatják. ==Zöld az alföld ({alföld felső határa} alatt), sárga a dombság, barna a hegység ({hegység alsó határa} fölött).== A zöld tehát nem rét! Hazánk {alföld aránya}-a alföld. Húzd a pontot a vonal mentén!

> megjegyzés: Legmagasabb pontunk a Kékes ({Kékes magassága}).

### Feliratok
- alföld kategória felirat: alföld: # alatt
- dombság kategória felirat: dombság: # – #
- hegység kategória felirat: hegység: # fölött
- száz négyzet felirat: 100 négyzetből
- négyzet zöld felirat: # zöld
- négyzet sárga felirat: # sárga
- négyzet barna felirat: # barna
- szelvény csúszka: Utazz a vonal mentén (dél → észak)
- szelvény felirat: oldalnézet: Alföld → Bükk (k. h. 20,5°)
- pont felirat: itt kb. #: #
- alföld szó felirat: alföld
- dombság szó felirat: dombság
- hegység szó felirat: hegység
- Kékes felirat: Kékes #
- Alföld tájnév felirat: Alföld
- Bükk tájnév felirat: Bükk
- Mátra tájnév felirat: Mátra
- zöld tévhit felirat: A zöld szín rétet jelent?
- zöld válasz felirat: Nem: alacsony vidéket
- dél felirat: dél
- észak felirat: észak
- magasság felirat: magasság (m)
- forrás domborzat felirat: Forrás: NOAA ETOPO 2022 (domborzat), Natural Earth (vizek, határ)

### Adatok
- alföld felső határa: 200 m
<!-- forrás: a hazai tankönyvi beosztás (alföld 200 m alatt, dombság 200–500 m, hegység 500 m fölött); a határok tankönyvenként
     eltérhetnek – ellenőrizendő a használt tankönyvben (NKP Természettudomány 5.) -->
- hegység alsó határa: 500 m
<!-- forrás: mint fent -->
- alföld aránya: kb. 82 %
<!-- forrás: Magyarország Nemzeti Atlasza (MTA CSFK, 2021), 2.1. fejezet: a terület 82,4 %-a 200 m alatt, 0,6 %-a 500 m fölött
     (https://nemzetiatlasz.hu/MNA/MNA_2_1_atdolg.pdf, lekérdezve: 2026-11-24). Más forrás 84 %-ot ad (KSH, régebbi táblázat).
     A lecke a NOAA ETOPO 2022 rácsából is kiszámolja (kb. 82,3 %) és ellenőrzi. -->
- hegység aránya: kb. 0,6 %
<!-- forrás: Magyarország Nemzeti Atlasza (2021), mint fent; a rácsból számolva kb. 0,7 % -->
- Kékes magassága: 1014 m
<!-- forrás: KSH STADAT 6.6.1.1 Földrajzi alapadatok, lekérdezve: 2026-11-24; ugyanez: 03-meres, 07-foldgomb -->
- Kékes helye: 47,87° É, 20,01° K
<!-- forrás: átvéve a 15-hegyek leckéből (Mátra helye, OSM: 47,872° É, 20,009° K) -->
- domborzat: NOAA ETOPO 2022
<!-- forrás: shared/foldrajz/domborzat-karpat.js (NOAA NCEI ETOPO 2022 15″, közkincs) – a térkép színei és szintvonalai -->
- szelvény: NOAA ETOPO 2022
<!-- forrás: shared/foldrajz/szelveny-alfold-bukk.js (NOAA NCEI ETOPO 2022 15″, közkincs) – az oldalnézet -->

## 7. Útvonalterv: rövidebb vagy laposabb?
Az iskolától két út visz a kilátóig. Válassz! Az **A** rövidebb, de sűrűn keresztezi a szintvonalakat: meredek. A **B** hosszabb, de lankás. ==Felfelé mindkettőn ugyanannyit kell menni.== A légvonal bármelyik útnál rövidebb.

> megjegyzés: Melyiket választanád babakocsival? És ha sietsz?

### Feliratok
- A út gomb: Az A úton megyek
- B út gomb: A B úton megyek
- A út felirat: A út
- B út felirat: B út
- hossz felirat: hossz: #
- emelkedés felirat: emelkedés: #
- meredekség felirat: legmeredekebb: 100 m alatt # fel
- légvonal felirat: légvonalban: #
- válassz felirat: Válassz utat a gombokkal!
- profil cím felirat: magasság az út mentén
- távolság felirat: megtett út (m)
- légvonal tévhit felirat: A légvonal olyan hosszú, mint az út?
- légvonal válasz felirat: Nem: a légvonal mindig a legrövidebb

## 8. Összefoglalás: négy térkép, egy táj
- A **térkép** felülnézeti, kicsinyített, jelekkel egyszerűsített kép.
- A **méretarány**: 1 : 10 000 → 1 cm = 100 m.
- Jelkulcs, égtájak, szintvonalak, magassági színek.
- ==Ugyanarról a tájról más célra más térkép készül.== Kattints egy térképre!

> megjegyzés: Rajzold le az iskolád környékét jelkulccsal, égtájjal!

### Feliratok
- domborzati kártya felirat: domborzati térkép
- közigazgatási kártya felirat: közigazgatási térkép
- autós kártya felirat: autós térkép
- turista kártya felirat: turistatérkép
- domborzati cél felirat: Milyen magas, hol meredek?
- közigazgatási cél felirat: Melyik település, melyik megye?
- autós cél felirat: Merre visz az autóút, hány km?
- turista cél felirat: Melyik jelzés visz a kilátóhoz?
- jellemző méretarány felirat: jellemzően #
- községhatár felirat: községhatár
- megyehatár felirat: megyehatár
- szomszéd község felirat: szomszéd község
- parkoló felirat: P
- piros jelzés felirat: piros jelzés
- kék jelzés felirat: kék jelzés
- forrás jel felirat: forrás
- kattints kártya felirat: Kattints egy térképre!

### Adatok
- turistatérkép méretaránya: 1 : 40 000
<!-- forrás: jellemző érték, nem szabály – pl. Cartographia: A Bükk turistatérképe, M. 1:40 000 (2003, 2005, 2012), Hungaricana
     HTI Térképtár B XV c 1154, lekérdezve: 2026-11-24 -->
- autóatlasz méretaránya: 1 : 250 000
<!-- forrás: jellemző érték – pl. Cartographia: Magyarország autóatlasza, M. 1:250 000 (2002, 2006), Hungaricana HTI Térképtár
     B XV c 1134, lekérdezve: 2026-11-24 (más kiadások 1 : 200 000 és 1 : 360 000 is) -->

<!-- Tanári megjegyzések és források:
  - Kitalált példa: Tóvölgy (a házak, utak, a patak, a tó, a domb, a két útvonal, a község- és megyehatár a 8. lépés térképein),
    a helye a valódi térképen (3. lépés: a Bükk déli lábánál), a Kilátó-domb magassága (312 m) és a szintköz. A vásznon
    „kitalált példa” bélyeg. A domb egy egyszerű matematikai felület (két „harang” alakú domb összege, a nyugati oldala
    meredekebb); a falu kb. 150 m magasan van.
  - A vásznon 1 cm = 40 képpont (a térképlap centimétere; kivetítve nagyobb). A 3. lépés jobb oldali lapja 15,5 cm széles.
  - Az 1. lépés madártávlati rajza nem méretarányos (a fák, a magasságok rajzosak); a 3. lépés valódi térképén a folyók
    Natural Earth 1:10m adatból vannak – 1 : 100 000 körül ez durva, a kis patakok hiányoznak.
  - 5. lépés: a domb 3D-s rajzán és az oldalnézetben a magasság nagyítva látszik („függőleges torzítás” bélyeg).
  - 6. lépés: a domborzat a NOAA ETOPO 2022 rácsából (1′ ≈ 1,25 × 1,85 km cellák átlaga) – a csúcsok lapítottak (a Kékes
    a rácson kb. 830 m), ezért a Kékes magasságát a lecke a fenti adatból írja ki. A felszínmodell erdő és város fölött néhány
    méterrel magasabb. A 200 és az 500 m-es szintvonalat a lecke a rácsból számolja. A „100 négyzetből” számai a rácsból
    számoltak (kb. 82 / 17 / 1). Az oldalnézet a k. h. 20,5° mentén fut (Tisza-vidék – Mátraalja – Bükk-fennsík), 0,25 km-es
    átlagokból (legmagasabb pont 841 m), erős függőleges torzítással.
  - A magassági színek határai (200 és 500 m) a hazai tankönyvi beosztás; egyes atlaszok több fokozatot használnak
    (pl. 0–100, 100–200, 200–300, 300–500, 500–1000 m), ezért a lecke a sávokon belül is enyhén árnyal.
  - 7. lépés: a hossz és az emelkedés a kitalált domb felületéből számolt; a „legmeredekebb” a 100 m-es szakaszok legnagyobb
    emelkedése. A légvonal az iskola és a kilátó távolsága.
  - 8. lépés: a négy térkép ugyanazt a kitalált tájat mutatja; a valóságban a turistatérkép jellemzően 1 : 40 000-es, az
    autóatlasz 1 : 250 000-es (kiadónként eltér), a közigazgatási és a domborzati térkép bármilyen méretarányú lehet.
  - Az iránytű tájolása (4. lépés): a mágneses és a földrajzi észak közötti kb. 6°-os eltérést (04-magnes) itt elhanyagoljuk.
  - Folytatás: a GPS és a fokhálózat a 07-foldgomb leckében; a hegyek keletkezése a 15-hegyek leckében.
  - Térképadat: Natural Earth (közkincs, „Made with Natural Earth”), NOAA NCEI ETOPO 2022 (közkincs).
-->
