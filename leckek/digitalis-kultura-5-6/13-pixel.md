# Miért kockás a felnagyított fénykép? – pixel, vektor, felbontás, RGB
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 6. Multimédiás elemek készítése

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/13-pixel.md

  A „Tippelj!” lépésekben (3. és 5.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A feliratokban a # jel helyére a lecke számot ír (a számokat a lecke az Adatokból számolja).
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- rajzolt kép bélyeg: számítógéppel rajzolt kép
- sematikus bélyeg: sematikus rajz
- vörös felirat: vörös
- zöld felirat: zöld
- kék felirat: kék

### Adatok
- csatorna bitjei: 8 bit
<!-- forrás: 8 bit/színcsatorna (24 bites „valódi szín”) – IEC 61966-2-1:1999 (sRGB) 8 bites kódolása; W3C PNG Specification (3rd ed., 2025), „bit depth 8” RGB-képek; 2^8 = 256 fokozat (0–255), a lecke számolja -->
- színcsatornák száma: 3
<!-- forrás: RGB – vörös, zöld, kék (IEC 61966-2-1, sRGB) -->

## 1. Nagyíts bele!
Ez egy rajzolt „fénykép” egy almafáról. Nagyíts rá egy almára! A kép apró, egyszínű kockákból áll: ezek a **pixelek** (képpontok). Az ilyen kép a **rasztergrafika**. ==Nagyítva nem lesz több részlet, csak nagyobbak a kockák.==

> megjegyzés: Kapcsold át simítottra: kockák helyett elmosódott foltok lesznek.

### Feliratok
- célpont felirat: ide nagyítunk
- nagyítás felirat: nagyítás: #×
- kocka felirat: minden kocka egy pixel: egyetlen szín
- három szám felirat: minden pixel három szám: vörös, zöld, kék
- kockás mód felirat: kockás nagyítás
- simított mód felirat: simított nagyítás – elmosódik
- nagyítás csúszka: Nagyítás
- kockás gomb: Kockás
- simított gomb: Simított

### Adatok
- legnagyobb nagyítás: 40
<!-- forrás: a lecke beállítása (a terv 13-as briefje: 1× → 40×); 40×-nél egy pixel 100 képpont széles, elfér benne a három szám -->

## 2. Egy pixel = három szám
Minden pixel színe három szám: mennyi **vörös**, **zöld** és **kék** fény világít benne (**RGB**). Mindegyik 0 és 255 között van: 1 bájt. ==Húzd a csúszkákat, vagy kattints a lámpákra!==

> megjegyzés: Erős nagyítóval a képernyőn is látod a három kis fényt.

### Feliratok
- pixel cím felirat: Az alma egyik pixele
- közelről felirat: közelről: három kis fény
- messziről felirat: messziről: egy szín
- csatorna érték felirat: #: #
- csatorna felirat: 1 szám = # bit = 1 bájt → # fokozat (0–255)
- pixel bitjei felirat: 1 pixel = 3 · # bit = # bit = 3 bájt
- színek száma felirat: # · # · # = # féle szín
- vörös csúszka: Vörös (R)
- zöld csúszka: Zöld (G)
- kék csúszka: Kék (B)

## 3. Fényből keverve
A képernyő fényeket kever, nem festéket. ==Mi lesz a vörös és a zöld fényből együtt? Tippelj!==

**Sárga!** A fények összeadódnak: a sárga pixel vörös 255, zöld 255, kék 0. Mind a három teljes erővel: **fehér** – nem a színek hiánya.

> megjegyzés: Festéknél másképp megy – erről fizikából tanulsz.

### Feliratok
- fény kérdés felirat: Vörös fény + zöld fény = ?
- barna tipp: barna
- sárga tipp: sárga
- fehér tipp: fehér
- vörös fény felirat: vörös fény
- zöld fény felirat: zöld fény
- kék fény felirat: kék fény
- kijelző felirat: sötét kijelző
- fények összege felirat: A fények összeadódnak:
- sárga keverék felirat: vörös + zöld = sárga
- cián keverék felirat: zöld + kék = ciánkék
- bíbor keverék felirat: vörös + kék = bíbor
- fehér keverék felirat: mind a három = fehér
- most felirat: most: #
- fekete név: fekete
- vörös név: vörös
- zöld név: zöld
- kék név: kék
- sárga név: sárga
- cián név: ciánkék
- bíbor név: bíbor
- fehér név: fehér
- barna tévhit felirat: Vörös + zöld = barna.
- barna válasz felirat: Festéknél talán – fénynél sárga!
- fehér tévhit felirat: A fehér a színek hiánya.
- fehér válasz felirat: A fehér: mind a három fény teljes erővel.
- vörös fény gomb: Vörös fény ki/be
- zöld fény gomb: Zöld fény ki/be
- kék fény gomb: Kék fény ki/be

## 4. Felbontás és fájlméret
A **felbontás** a pixelek száma: szélesség × magasság. Több pixel → több részlet, de nagyobb fájl: pixelenként 3 bájt. ==Válts felbontást, és figyeld a fájlméretet!== Próbáld ki: a felnagyított 8 × 8-as kép sem lesz részletesebb.

> megjegyzés: A fényképet a gép tömöríti, ezért kisebb a fájl.

### Feliratok
- felbontás felirat: # × # pixel
- pixelszám felirat: # pixel
- fájlméret felirat: # · # · 3 bájt = #
- felnagyított felirat: a 8 × 8-as kép felnagyítva
- összevetés felirat: pixelek száma
- full hd felirat: Full HD képernyő: # × # = # pixel ≈ # megapixel
- full hd méret felirat: egy Full HD kép tömörítetlenül: #
- telefonfotó felirat: telefonfotó: # × # = # megapixel → #, tömörítve #
- nagyobb tévhit felirat: A nagyobb fájl mindig szebb kép.
- nagyobb válasz felirat: Felnagyítva nagy a fájl, de a részlet nem jön vissza.
- felbontás gomb: # × #
- felnagyít gomb: 8 × 8 → 128 × 128

### Adatok
- felbontások: 8; 32; 128
<!-- forrás: a lecke beállítása (a terv 13-as briefje: 8 × 8 / 32 × 32 / 128 × 128) -->
- Full HD szélessége: 1920 pixel
<!-- forrás: ITU-R BT.709-6 (2015), HDTV-képformátum: 1920 × 1080 aktív képpont; 1920 · 1080 = 2 073 600 ≈ 2,07 megapixel (a lecke számolja) -->
- Full HD magassága: 1080 pixel
<!-- forrás: ITU-R BT.709-6 (2015) -->
- telefonfotó szélessége: 4000 pixel
<!-- forrás: becslés – egy tipikus 12 megapixeles telefonkamera 4:3-as képe 4000 × 3000 pixel (a terv 13-as briefje) -->
- telefonfotó magassága: 3000 pixel
<!-- forrás: becslés, lásd fent -->
- tömörített fotó mérete: kb. 3 MB
<!-- forrás: becslés – egy 12 megapixeles telefonfotó JPEG-ben tipikusan 2–5 MB; ugyanez a szám a 17-szamitogep leckében („egy telefonfotó mérete”) -->

## 5. Raszter vagy vektor?
Balra fénykép: pixelek. Jobbra **vektoros** rajz: alakzatok leírása. ==Melyik marad éles {próbanagyítás}-szeres nagyításban? Tippelj!==

A **vektorgrafika** csomópontokat, görbéket, színeket tárol. Nagyításkor a gép újrarajzolja őket: élesek maradnak. A raszterkép kockás lesz.

### Feliratok
- éles kérdés felirat: Melyik marad éles #-szeres nagyításban?
- fotó tipp: a fénykép
- vektor tipp: a vektoros rajz
- egyik sem tipp: egyik sem
- fotó panel felirat: fénykép (raszter)
- vektor panel felirat: vektoros rajz
- fotó leírás felirat: # × # pixel → # szám
- alma alakzat felirat: alma: görbe, # csomópont, vörös
- levél alakzat felirat: levél: görbe, # csomópont, zöld
- szár alakzat felirat: szár: sokszög, # csúcs, barna
- vektor tévhit felirat: A vektoros kép is pixelekből áll a fájlban.
- vektor válasz felirat: A fájlban alakzatok vannak – pixel csak a képernyőn lesz belőle.
- nagyítás 5 csúszka: Nagyítás

### Adatok
- próbanagyítás: 10
<!-- forrás: a lecke beállítása (a terv 13-as briefje: „10× nagyítva”) -->

## 6. Mikor melyik?
A **fénykép** és a festett kép raszter: minden pixel más színű lehet. A **logó**, a **diagram** és a térképvázlat vektoros: bármekkorára nagyítható. ==Kattints a kártyákra: raszter vagy vektor?==

> megjegyzés: A bemutatókészítő rajzeszközei vektoros alakzatokat rajzolnak, a festőprogram ecsetje pixeleket színez.

### Feliratok
- kártya kérdés felirat: Raszter vagy vektor? Kattints a kártyákra!
- fénykép kártya: fénykép
- logó kártya: az iskola logója
- festmény kártya: festőprogramban festett kép
- diagram kártya: oszlopdiagram
- szkennelt kártya: beszkennelt rajz
- térkép kártya: térképvázlat
- fénykép ok felirat: minden pixel más színű lehet
- logó ok felirat: plakáton és kitűzőn is éles
- festmény ok felirat: az ecset pixeleket színez
- diagram ok felirat: téglalapok és vonalak
- szkennelt ok felirat: a szkenner pixelenként mér
- térkép ok felirat: vonalak és görbék
- raszter címke: raszter
- vektor címke: vektor
- kattints felirat: Kattints rá!
- mind gomb: Mutasd mindet!
- elrejt gomb: Elölről

## 7. Szerkesztés = számolás
A képszerkesztő a pixelek számait írja át. **Tükrözés**: a sorok számai fordított sorrendbe kerülnek. **Világosítás**: minden számhoz hozzáad {világosítás mértéke}-et. **Retusálás**: a folt pixelei a szomszédok számait kapják. ==Rajzolj, és próbáld ki a gombokat!==

### Feliratok
- számtábla felirat: a kijelölt rész számai
- pozíció felirat: oszlop #, sor #
- pad méret felirat: # × # pixel = # bájt
- rajzolj felirat: Rajzolj: kattints vagy húzd az egeret!
- ceruza eszköz: ceruza
- kitöltés eszköz: kitöltés
- radír eszköz: radír
- ceruza szabály felirat: ceruza: a pixel új számokat kap
- kitöltés szabály felirat: kitöltés: az egybefüggő, egyszínű folt új számokat kap
- radír szabály felirat: radír: a pixel fehér lesz (255, 255, 255)
- tükrözés szabály felirat: tükrözés: minden sor számai fordított sorrendben
- forgatás szabály felirat: forgatás: a sorokból oszlopok lesznek
- világosítás szabály felirat: világosítás: minden számhoz + # (legfeljebb 255)
- kivágás szabály felirat: kivágás: csak a középső rész marad – kisebb a fájl
- retusálás szabály felirat: retusálás: a folt helyére a szomszéd pixelek számai
- retusálás nincs felirat: retusálás: nincs már folt a képen
- alaphelyzet szabály felirat: alaphelyzet: az eredeti kép
- példa felirat: pl. # → #
- tükrözés gomb: Tükrözés
- forgatás gomb: Forgatás 90°
- világosítás gomb: Világosítás + #
- kivágás gomb: Kivágás
- retusálás gomb: Retusálás
- alaphelyzet gomb: Alaphelyzet

### Adatok
- világosítás mértéke: 40
<!-- forrás: a lecke beállítása (a terv 13-as briefje: „+40 minden számhoz”) -->

## 8. Összefoglalás
A **raszterkép** pixelekből áll; minden pixel három szám (**RGB**, 0–255). Több pixel: nagyobb **felbontás** és nagyobb fájl. A **vektoros** kép alakzatokból áll, élesen nagyítható. A képszerkesztés: számolás a pixelek számaival.

> megjegyzés: Feladat: rajzolj füzetbe 8 × 8-as pixelképet, és írd mellé a számait!

### Feliratok
- összefoglaló cím felirat: Ami a kép mögött van
- összegzés pixel felirat: raszterkép = pixelek rácsa
- összegzés rgb felirat: 1 pixel = 3 szám (R, G, B), mindegyik 0–255
- összegzés fény felirat: a fények összeadódnak: vörös + zöld = sárga
- összegzés felbontás felirat: több pixel → több részlet, nagyobb fájl
- összegzés vektor felirat: vektoros kép = alakzatok → élesen nagyítható
- összegzés szerkesztés felirat: képszerkesztés = számolás a pixelekkel

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a „fénykép” (almafa a réten), a vektoros alma, a kártyák képei (logó, diagram, térképvázlat,
    festmény, beszkennelt rajz) és a 16 × 16-os pixelkép a lecke saját, kódból rajzolt képei; valódi fotó nincs a
    leckében. A „fénykép” egy rejtett vásznon élsimítva rajzolt kép, enyhe, seedelt „szemcsézettséggel” – a vásznon
    „számítógéppel rajzolt kép” bélyeg.
  - RGB: 8 bit/csatorna → 2^8 = 256 fokozat (0–255); 3 · 8 = 24 bit = 3 bájt pixelenként; 256 · 256 · 256 =
    16 777 216 szín (a lecke számolja; a gyakran idézett „16,7 millió” csonkolt érték, kerekítve 16,8 millió – ezért
    a vászon a pontos számot írja). Vannak 10, 12, 16 bites csatornák is (HDR, nyers fotó) – ezt a lecke nem említi.
  - A képernyő pixele: a „közelről” rajz sematikus (három függőleges csík); a valódi alpixel-elrendezés
    kijelzőnként eltér (csíkos, PenTile stb.). A fények keverése (additív) a fizika-7-8/13-szinek 6. lépésében is
    szerepel (ugyanaz a három szín), a festékek kivonó keverése ott, a 7. lépésben.
  - A fényeket a lecke a böngésző „lighter” (összeadó) kompozíciójával keveri: az átfedésben a számok összeadódnak,
    255-nél levágva – ez a valódi additív keverés egyszerű, de becsületes modellje (a szem érzékelése nemlineáris, ezt
    nem részletezzük). A „ciánkék” (cián) és a „bíbor” (magenta) a tankönyvi elnevezés; tankönyvenként eltérhet.
  - Felbontás, fájlméret: a lecke a tömörítetlen méretet számolja (szélesség · magasság · 3 bájt). Full HD (ITU-R
    BT.709): 1920 · 1080 = 2 073 600 pixel ≈ 2,07 megapixel → 6 220 800 bájt ≈ 6,2 MB; egy 12 megapixeles
    telefonfotó (4000 × 3000) tömörítetlenül 36 MB, JPEG-ben kb. 2–5 MB (becslés; a lecke a 17-szamitogep kb. 3 MB-os
    értékét használja). A tömörítés (JPEG, PNG) és a veszteséges tömörítés a 7–8. évfolyam anyaga – itt csak
    megnevezzük. 1 kB = 1000 bájt (SI).
  - A felnagyított 8 × 8-as kép (128 × 128) „legközelebbi szomszéd” módszerrel készül: minden pixel 16 × 16-szor
    ismétlődik – a fájl 256-szor nagyobb, a kép ugyanaz. A „simított” nagyítás (bilineáris) csak elmossa a
    kockákat, új részletet ez sem hoz (a „krimis nagyítás” mítosza). A mesterséges intelligenciás „felskálázás”
    kitalál részleteket – az nem a valóság visszahozása; a lecke nem említi.
  - Vektorgrafika: a rajz alakzatok listája (görbe csomópontokkal és vezérlőpontokkal, kör, sokszög, szín); a gép
    megjelenítéskor, a pillanatnyi méretben alakítja pixelekké (raszterizálás). A csomópontok és a Bézier-görbék
    részletei a 7–8. évfolyam (6. témakör) anyaga. A vonalvastagság nagyításkor a valódi vektorgrafikában is nő.
  - Képszerkesztés: a lecke műveletei egyszerű modellek. A „világosítás” minden számhoz ugyanannyit ad (a valódi
    programok görbével dolgoznak); a „retusálás” itt bélyegző-szerű másolás a folt mellől (a valódi programok a
    szomszédság alapján simítanak is). A kivágás a középső részt hagyja meg.
  - Az órán használt rajzolóprogramban a ceruza, a kitöltés (festékes vödör), a radír és a tükrözés/forgatás a
    menüben vagy az eszköztáron van; a lecke a mögöttes számolást mutatja.
-->
