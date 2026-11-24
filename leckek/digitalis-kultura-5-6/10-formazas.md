# Miért csúszik szét a szóközzel igazított cím? – karakter, bekezdés, oldal, stílus
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 4. Szövegszerkesztés

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/10-formazas.md

  A „Tippelj!” lépésekben (5., 7.) a panel első bekezdése a kérdés; a többi bekezdés
  elmosódva látszik, és csak a tipp után válik olvashatóvá.
  A plakát és a tudnivalók szövegét a vásznon a lecke tördeli (mért szélességgel), ezért a
  hosszuk szabadon változtatható – csak a kijelölt mintaszó („újságokat”) maradjon egy szó.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- kitalált bélyeg: kitalált plakát
- nagyítás bélyeg: nagyítás · szemléltetés
- sematikus bélyeg: sematikus rajz – nem a te programod
- plakát cím: Őszi papírgyűjtés
- plakát alcím: október 14–16., az iskolaudvaron
- plakát bekezdés 1: Hozd el a régi újságokat, füzeteket, könyveket és kartondobozokat az iskolaudvarra!
- plakát bekezdés 2: Kötegeld össze őket, és kösd át zsinórral.
- plakát bekezdés 3 eleje: A legtöbbet gyűjtő osztály
- plakát bekezdés 3 kiemelés: kirándulást nyer.
- plakát lábléc: Szervező: a diákönkormányzat
- karakter felirat: karakter
- szó felirat: szó
- sor felirat: sor
- bekezdés felirat: bekezdés
- oldal felirat: oldal
- igazítás sor: igazítás: #
- balra felirat: balra
- középre felirat: középre
- jobbra felirat: jobbra
- sorkizárt felirat: sorkizárt

### Adatok
- pont mm-ben: 0,353 mm
<!-- forrás: a tipográfiai (DTP-) pont = 1/72 hüvelyk = 25,4 mm / 72 = 0,3528 mm (a lecke L.checks()-e ellenőrzi). A régi európai Didot-pont (0,376 mm) ma a szövegszerkesztőkben nem használatos. -->
<!-- forrás (az alábbiakra): ISO 216 (MSZ EN ISO 216): A4 = 210 mm × 297 mm; az A0 1 m², minden következő méret a felezése. -->
- A4 szélessége: 210 mm
- A4 magassága: 297 mm
- margó: 25 mm
<!-- forrás: kitalált példa – sok szövegszerkesztő alapértéke 2,5 cm körül van, de programonként eltér. -->
<!-- forrás (az alábbiakra): kitalált példa (egy iskolai A4-es plakát). -->
- plakátcím mérete: 48 pont
- plakátszöveg mérete: 22 pont

## 1. Mit látsz egy plakáton?
Ez egy kitalált iskolai plakát. A szövegszerkesztő számára a szöveg **szövegegységekből** áll: karakter, szó, sor, bekezdés, oldal. ==Egymásba ágyazódnak, mint a dobozok.== Kattints rájuk!

> megjegyzés: Hozzatok be egy szórólapot, és keressétek meg rajta az egységeket!

### Feliratok
- karakter gomb: karakter
- szó gomb: szó
- sor gomb: sor
- bekezdés gomb: bekezdés
- oldal gomb: oldal
- egymásban felirat: egymásba ágyazva
- karakter magyarázat: betű, szám, írásjel – vagy szóköz
- szó magyarázat: karakterek két szóköz között
- sor magyarázat: amennyi kifér – a gép tördeli
- bekezdés magyarázat: a következő Enterig tart
- oldal magyarázat: a papírlap a margókkal

## 2. A karakter cédulája
A **karakter** egy betű, szám, írásjel vagy szóköz. A kijelölt karakterek **formázása**: betűtípus, méret, stílus, szín. A méret mértékegysége a **pont**: 1 pont ≈ {pont mm-ben}. Próbáld ki! ==Kiemelni egy eszközzel elég.==

> megjegyzés: Könyvben a betű {folyó szöveg mérete}. Az órán használt programban ezt a karakterformázásnál találod.

### Feliratok
- minta eleje: Hozd el a régi
- minta szó: újságokat
- minta vége: is!
- méret csúszka: A kijelölt szó betűmérete
- félkövér gomb: félkövér
- dőlt gomb: dőlt
- aláhúzott gomb: aláhúzott
- piros gomb: piros szín
- karakter cédula: a kijelölt karakterek
- betűtípus sor: betűtípus: #
- méret sor: méret: # pont ≈ # mm
- stílus sor: stílus: #
- szín sor: szín: #
- talpatlan érték: talpatlan
- normál érték: normál
- félkövér érték: félkövér
- dőlt érték: dőlt
- aláhúzott érték: aláhúzott
- tinta érték: sötétkék
- piros érték: piros
- kijelölés felirat: kijelölés
- túl sok felirat: Minden kiemelés egyszerre?
- egy elég felirat: Egy kiemelés elég!
- pontméret felirat: # pont

### Adatok
- folyó szöveg mérete: kb. 10–12 pont
<!-- forrás: tipográfiai gyakorlat (becslés) – könyvek, tankönyvek folyó szövege jellemzően 10–12 pontos; a betűtípustól is függ. -->
- mintaszöveg mérete: 22 pont
<!-- forrás: kitalált példa (a plakát folyó szövegének mérete). -->

## 3. Talpas, talpatlan, egyenlő szélességű
A **talpas** betű szárainak végén kis talpak vannak, a **talpatlan** sima. Az **egyenlő szélességű** betűben ==minden karakter ugyanolyan széles: az i, az m és a szóköz is.== A másik kettőben nem. Válts mintát!

> megjegyzés: Keressetek mindháromra példát tankönyvben, újságban, csomagoláson!

### Feliratok
- talpas felirat: talpas
- talpatlan felirat: talpatlan
- egyenlő felirat: egyenlő szélességű
- i minta gomb: i és m betűk
- szóköz minta gomb: szóközök és m betűk
- egyforma felirat: egyforma hosszú
- nem egyforma felirat: nem egyforma
- tíz i felirat: 10 i
- tíz m felirat: 10 m
- tíz szóköz felirat: 10 szóköz
- hossz felirat: # mm

### Adatok
- mintabetű mérete: 36 pont
<!-- forrás: kitalált példa (szemléltető méret). -->

## 4. A bekezdés cédulája
A **bekezdés** a következő **Enter**ig tart. ==A sor végén a gép magától új sort kezd.== A bekezdés formázása: **igazítás**, **behúzás**, térköz. Válts igazítást, és húzd a vonalzón a behúzás jelét!

> megjegyzés: Az órán használt programban ezt a bekezdésformázásnál találod.

### Feliratok
- balra gomb: balra
- középre gomb: középre
- jobbra gomb: jobbra
- sorkizárt gomb: sorkizárt
- behúzás csúszka: Az első sor behúzása
- bekezdés cédula: bekezdés
- behúzás sor: első sor behúzása: # mm
- térköz sor: térköz utána: # pont
- vége sor: a vége: egy Enter
- húzd felirat: húzd!

### Adatok
- térköz a bekezdés után: 6 pont
<!-- forrás: kitalált példa (gyakori beállítás). -->

## 5. Szóközzel igazítva?
A felső címet valaki **szóközökkel** tolta középre. ==Most betűtípust váltunk. Mi történik? Tippelj!==

Elcsúszik! A szóköz is karakter, és a talpas betűben keskenyebb. Az alsó cím igazítása: ==középre== – ezt a gép minden változás után újraszámolja.

> megjegyzés: Próbáld ki a cím átírását is!

### Feliratok
- csúszás kérdés felirat: Betűtípust váltunk. Mi lesz a szóközökkel középre tett címmel?
- marad tipp: középen marad
- elcsúszik tipp: elcsúszik
- eltűnik tipp: eltűnik
- szóközzel felirat: szóközökkel „középre”
- igazítással felirat: igazítás: középre
- lap közepe felirat: a lap közepe
- elcsúszott felirat: # mm-rel elcsúszott
- középen felirat: középen maradt
- talpas gomb: talpas
- talpatlan gomb: talpatlan
- egyenlő gomb: egyenlő szélességű
- címméret csúszka: A cím betűmérete
- átírás gomb: Írd át a címet!
- átírt cím: Tavaszi papírgyűjtés
- szóközök felirat: # szóköz

### Adatok
- cím mérete: 28 pont
<!-- forrás: kitalált példa – ennél a méretnél az egyenlő szélességű betűvel a cím pontosan 5 szóközzel kerül középre (a lecke kiszámolja). -->

## 6. Rejtett jelek
A **rejtett jelek** megmutatják a láthatatlant: a pötty a szóköz, a ¶ a bekezdés vége. Bal oldalt valaki minden sor végén Entert nyomott. ==Húzd keskenyebbre a hasábot!== Melyik marad rendben?

> megjegyzés: Nyomtatáskor a rejtett jelek nem látszanak.

### Feliratok
- hasáb csúszka: A hasáb szélessége
- rejtett jelek gomb: Rejtett jelek be/ki
- enterrel felirat: Enter minden sor végén
- bekezdéssel felirat: Enter csak a bekezdés végén
- enter tévhit felirat: Az Enter a sor vége?
- enter válasz felirat: Nem: a bekezdés vége!
- szóköz jel felirat: szóköz
- bekezdés jel felirat: bekezdés vége (Enter)
- hasáb bekezdés 1: Hozd el a régi újságokat, füzeteket, könyveket és kartondobozokat az iskolaudvarra!
- hasáb bekezdés 2: Kötegeld össze őket, és kösd át zsinórral, hogy könnyű legyen hordani.

### Adatok
<!-- forrás (az alábbiakra): kitalált példa (szemléltető beállítások). -->
- hasábszélesség: 100 mm
- hasábszöveg mérete: 14 pont
- első sor behúzása: 8 mm

## 7. A stílus: egy helyen javítasz
A **stílus** elnevezett formázás. Három cím „Címsor” stílusú. ==A stílus mérete {címsor mérete} helyett {új címsor mérete} lesz. Hány cím változik? Tippelj!==

Csak a három „Címsor” stílusú! A negyediket kézzel formázták, az nem változik. ==Egy helyen javítasz, és mindenhol változik.==

### Feliratok
- stílus kérdés felirat: A „Címsor” stílus mérete # pontról # pontra nő.
- stílus kérdés 2 felirat: Hány cím változik?
- egy tipp: csak egy
- stílusú tipp: mind, ami „Címsor” stílusú
- félkövér tipp: mind, ami félkövér
- dokumentum cím: Papírgyűjtés – tudnivalók
- címsor 1: Mit hozhatsz?
- szöveg 1: Újságot, füzetet, könyvet, kartondobozt – kötegelve.
- címsor 2: Mit ne hozz?
- szöveg 2: Zsíros papírt, fóliát, matricás lapot, ragasztószalagot.
- címsor 3: Mikor és hol?
- szöveg 3: Október 14–16-án reggel, az iskolaudvaron.
- címsor 4: Ki nyer?
- szöveg 4: A legtöbbet gyűjtő osztály kirándulást nyer.
- stílus cédula: „Címsor” stílus
- stílus betű sor: betűtípus: talpas, félkövér
- stílus méret sor: méret: # pont
- kézzel felirat: kézzel formázva – nem változott
- stílusos felirat: Címsor stílusú
- címsor csúszka: A „Címsor” stílus mérete
- legyen címsor gomb: Ez is legyen Címsor!
- kék címsor gomb: Címsor színe: kék / sötétkék

### Adatok
<!-- forrás (az alábbiakra): kitalált példa (iskolai dokumentum szokásos méretei; a folyó szöveg 10–12 pontos). -->
- címsor mérete: 18 pont
- új címsor mérete: 24 pont
- szövegtörzs mérete: 12 pont

## 8. Az oldal – és a rétegek egymásban
Az **oldal** beállítása a **lapméret** (A4: {A4 szélessége} × {A4 magassága}) és a **margó**. Húzd a margót, fordítsd fekvőre a lapot! ==A plakát rétegei: oldal, bekezdés, karakter – mindegyiknek saját cédulája van.==

> megjegyzés: Az órán használt programban ezt az oldalbeállításnál találod.

### Feliratok
- margó csúszka: Margó (bal és jobb)
- tájolás gomb: Álló / fekvő lap
- rétegek gomb: Rétegek szét / össze
- oldal cédula: oldal
- lapméret sor: lapméret: A4, #
- álló érték: álló
- fekvő érték: fekvő
- méret mm sor: # × # mm
- margó sor: margó: # mm
- bekezdés cédula 8: bekezdés (a cím)
- igazítás 8 sor: igazítás: középre
- térköz 8 sor: térköz utána: # pont
- karakter cédula 8: karakter (a cím)
- betű 8 sor: talpas, félkövér
- méret 8 sor: # pont

### Adatok
- térköz a cím után: 6 pont
<!-- forrás: kitalált példa. -->

## 9. Összefoglalás
- Középre **igazítással** teszünk, nem szóközzel.
- Az **Enter** a bekezdés vége, nem a sor vége.
- A **stílust** egy helyen javítod, és mindenhol változik.
- ==Egy kiemelés elég.==
- A **rejtett jelek** megmutatják, mi van a szövegben.

### Feliratok
- összefoglaló cím: Amit megtanultunk
- tévhit 1: Középre szóközzel is lehet.
- válasz 1: Középre: igazítással!
- tévhit 2: Az Enter a sor vége.
- válasz 2: Az Enter a bekezdés vége.
- tévhit 3: Minden címet egyesével formázok.
- válasz 3: Stílus: egy helyen javítasz.
- tévhit 4: Félkövér + dőlt + aláhúzott + piros.
- válasz 4: Egy kiemelés elég.

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a plakát („Őszi papírgyűjtés”), a tudnivalók és a diákönkormányzat mint szervező
    kitalált, szemléltető szöveg; valódi iskola, személy nincs benne.
  - A vásznon a lap és a vonalzó sematikus: nem egy valódi szövegszerkesztő felülete (nincs menü,
    eszköztár, gyorsbillentyű). A betűtípusok a lecke három betűcsaládja (Fraunces = talpas,
    Bricolage Grotesque = talpatlan, JetBrains Mono = egyenlő szélességű); az órán használt
    programban más betűtípusok vannak, de a három csoport ugyanez. A dőlt változatot a talpatlan és az
    egyenlő szélességű betűnél a böngésző ferdíti (nincs külön dőlt betűkészlet).
  - A tördelés a valódi szövegszerkesztők elvét követi (mért betűszélesség, a sor végén a szóköz
    „kilóg”, sorkizártnál a bekezdés utolsó sora balra áll), de egyszerűsít: nincs elválasztás, nincs
    özvegy- és fattyúsor-kezelés, a sortávolság a legnagyobb betűhöz igazodik.
  - Pont: a szövegszerkesztők a tipográfiai (DTP-) pontot használják, 1 pont = 1/72 hüvelyk ≈ 0,353 mm.
    A betűméret a betű „dobozának” (em) magassága, nem a nagybetű magassága; ezért egy 22 pontos
    nagybetű betűtípustól függően csak kb. 5–6 mm magas, nem 7,8 mm.
  - 6. lépés: a bal oldali hasáb úgy készült, hogy a jobb oldali, 100 mm-es hasáb sorait a gép minden
    sor végén Enterrel lezárt bekezdéssé alakítja, az első sor behúzását pedig szóközökkel pótolja
    (a lecke számolja ki, hány szóköz kell). Kiinduláskor ezért a két hasáb egyforma.
  - 7. lépés: a negyedik címet kézzel formázták ugyanúgy (talpas, félkövér, 18 pont) – ránézésre nem
    különbözik, csak a stílus változtatásakor derül ki.
  - Tévhitek, amelyeket a lecke cáfol: „Az Enter a sor vége.” „Középre szóközzel is lehet.” „Az első
    sor behúzása = öt szóköz.” „A kiemelés: félkövér + dőlt + aláhúzott + piros egyszerre.” „Minden
    címet egyesével formázok.” A „nagyobb betű mindig jobban olvasható” tévhitet a 2. lépés csúszkája
    érinti (nagy méretnél a sor kevés szót bír el) – a 12. lecke (bemutató) folytatja.
  - Kapcsolódás: a 11. lecke (kép, elválasztás, helyesírás-ellenőrző) és a 12. lecke (diakocka)
    ugyanezt a „lapot” használja.
-->
