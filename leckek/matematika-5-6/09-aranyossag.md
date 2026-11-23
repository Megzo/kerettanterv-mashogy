# Mennyibe kerül 7 kifli? – egyenes és fordított arányosság
tantárgy: Matematika · évfolyam: 5–6. · témakör: 9. Arányosság, százalékszámítás (+ 11. A függvény fogalmának előkészítése)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/09-aranyossag.md
  Feliratban a # jel helyére a lecke számot ír (pl. „#. sor” → „5. sor”).
  Az árak (kifli, sajt, taxi) kitalált példák, nem valós árak.
-->

## Közös

### Feliratok
- darab tengely: darab
- ár tengely: ár (Ft)
- kifli fejléc: kifli (db)
- ár fejléc: ár (Ft)
- hányados fejléc: ár : darab

### Adatok
- kifli ára: 80 Ft
- kiemelt darabszám: 7
- 7 kifli ára: 560 Ft
<!-- kitalált példa. A „7 kifli ára” eredmény: a lecke kiszámolja (7 · 80 Ft) és összeveti – eltérésnél piros hibasáv.
     Ha a kiemelt darabszámot átírod, a lecke címét és a 3. lépés első mondatát is írd át. -->

## 1. Két adat, egy hely
Hová ülj le a moziban? A jegyen két szám áll: hányadik **sor**, hányadik **szék**. A sakktáblán is két adat jelöl ki egy mezőt: egy betű és egy szám. ==Egy helyhez két adat kell.== A koordináta-rendszerben ezek neve: *x* és *y*.

### Feliratok
- mozijegy: MOZIJEGY
- jegy sor: #. sor
- jegy szék: #. szék
- vászon: VÁSZON
- sor: sor
- szék: szék
- sakktábla: sakktábla
- sakkmező: e4
- sakk magyarázat: e oszlop, 4. sor
<!-- A „sakkmező” egy betű (a–h) és egy szám (1–8): a lecke ezt a mezőt emeli ki a táblán.
     A „sakk magyarázat” ugyanezt szövegesen mondja – ha a mezőt átírod, ezt is írd át. -->

### Adatok
- jegy sora: 5
- jegy széke: 3

## 2. Torpedó a rácson
Egy pontot két szám ad meg: `P(3; 2)`. Az **első** az *x*: ennyit lépünk jobbra. A **második** az *y*: ennyit fölfelé. ==A sorrend számít:== a `(2; 3)` egészen máshol van! Lőj a hajókra: kattints egy rácspontra!

> megjegyzés: Párban papíron is játszható.

### Feliratok
- jobbra: # jobbra
- fel: # fel
- talált: talált!
- mellé: mellé
- sorrend: a sorrend számít
- te jössz: Te jössz: kattints egy rácspontra!
- találatok: találat: #
- elsüllyedt: Minden hajó elsüllyedt!
- x csúszka: x (jobbra)
- y csúszka: y (fölfelé)
- tűz gomb: Tűz!
- új játék gomb: Új játék

### Adatok
- első lövés: (3; 2)
- második lövés: (2; 3)
<!-- A két első lövést a lecke magától adja le; a hajókat úgy helyezi el, hogy az első talál, a második nem.
     A panelszöveg a két pontot szó szerint tartalmazza: ha átírod, azt is írd át. -->

## 3. Kifli: táblázat
Egy kifli {kifli ára}. Mennyibe kerül {kiemelt darabszám} kifli? Kétszer annyi kifli kétszer annyiba kerül, háromszor annyi háromszor annyiba. ==A hányados mindig ugyanannyi:== ár : darab = {kifli ára}. Ez az **egyenes arányosság**.

> megjegyzés: Húzd a csúszkát! Mennyi 10 kifli?

### Feliratok
- kérdés kifli: Mennyibe kerül # kifli?
- kifli csúszka: kifli (db)
- hányados állandó: a hányados mindig ugyanannyi

## 4. Pontok egy egyenesen, az origón át
Minden oszlop egy pont: `(darab; ár)`. A pontok **egy egyenesre** esnek, és az egyenes ==átmegy az origón==: 0 kifli 0 forintba kerül. Minden újabb kifli ugyanannyival, {kifli ára}-tal emeli az árat: a lépcsők egyformák.

### Feliratok
- origó: 0 kifli → 0 Ft
- egy kiflivel több: +1 db
- egyenes felirat: origón átmenő egyenes

## 5. Összekössük a pontokat?
`3,5` kiflit nem lehet venni, ezért a kifli pontjait ==nem kötjük össze==. Sajtból viszont bármennyit kérhetsz, akár töredék dekagrammot is. Itt minden közbülső érték értelmes, ezért a pontokat összekötjük: a grafikon **folytonos** egyenes.

> megjegyzés: Húzd a pontot a sajt egyenesén!

### Feliratok
- kifli cím: kifli – darabra
- sajt cím: sajt – dekagrammra
- fél kifli: 3,5 kifli?
- nem kötjük: csak pontok
- összekötjük: folytonos egyenes
- dkg tengely: tömeg (dkg)
- sajt csúszka: sajt (dkg)

### Adatok
- sajt ára: 400 Ft
- sajt mennyisége: 10 dkg
<!-- kitalált példa: 400 Ft / 10 dkg = 40 Ft/dkg. A lecke ebből számolja a sajt egyenesét. -->

## 6. Együtt nő, mégsem arányos
A taxiban {alapdíj} az **alapdíj**, és minden kilométerért {kilométerdíj} jön hozzá. 1 km {1 km ára}. ==Tippelj: 2 km kétszer ennyibe kerül?== A pontok egyenesre esnek, de ez az egyenes **nem megy át az origón**.

> megjegyzés: Az életkor és a testmagasság is együtt nő. Arányosak?

### Feliratok
- tipp kérdés: 2 km kétszer annyiba kerül, mint 1 km?
- tippelj: Tippelj előbb!
- tipp igen: Igen, kétszer annyiba
- tipp nem: Nem
- a tipped: a te tipped
- km tengely: út (km)
- arányos lenne: ha arányos lenne
- valójában: valójában
- alapdíj felirat: alapdíj
- km fejléc: út (km)
- taxi ár fejléc: ár (Ft)
- taxi hányados fejléc: ár : út
- nem állandó: a hányados nem állandó
- taxi ítélet: nem megy át az origón → nem egyenes arányosság

### Adatok
- alapdíj: 1000 Ft
- kilométerdíj: 400 Ft
- 1 km ára: 1400 Ft
- 2 km ára: 1800 Ft
<!-- kitalált tarifa (a valódi taxitarifában idődíj is van). Az „1 km ára” és a „2 km ára” eredmény:
     a lecke kiszámolja (alapdíj + kilométerdíj · km) és összeveti – eltérésnél piros hibasáv. -->

## 7. Fordított arányosság
Egy {út hossza} hosszú utat teszünk meg. Kétszer olyan gyorsan haladva ==fele annyi idő== kell. Itt a **szorzat** állandó: sebesség · idő = {út hossza}. Minden ponthoz egy téglalap tartozik, és mindegyik területe ugyanannyi.

> megjegyzés: Húzd a csúszkát! Ez a **fordított arányosság**.

### Feliratok
- sebesség tengely: sebesség (km/h)
- idő tengely: idő (óra)
- sebesség fejléc: km/h
- idő fejléc: óra
- szorzat fejléc: km/h · óra
- sebesség csúszka: sebesség (km/h)
- kétszer gyorsabb: 2-szer gyorsabb → fele annyi idő
- téglalap: terület = sebesség · idő

### Adatok
- út hossza: 60 km
- sebességek: 10; 15; 20; 30; 40; 60 km/h
- kiemelt sebesség: 20 km/h
<!-- Az idők (6; 4; 3; 2; 1,5; 1 óra) a lecke számolja: idő = út : sebesség. -->

## 8. Nem hiszem!
Négy grafikon – ==melyik az egyenes arányosságé?== Tippelj, aztán kattints! Ha a társad rosszat választ, mondd: „Nem hiszem!”, és indokold meg.

> megjegyzés: Mindegyiknél nézd meg: átmegy az origón? Állandó a hányados?

### Feliratok
- nem hiszem kérdés: Melyik grafikon mutat egyenes arányosságot?
- ítélet A: csökken, de a szorzat nem állandó
- ítélet B: nem megy át az origón
- ítélet C: egyenes arányosság
- ítélet D: fordított arányosság

## 9. Összefoglalás
- Egy pont két adat: `(x; y)`. Először *x*, aztán *y*.
- **Egyenes arányosság:** a hányados állandó, a grafikon ==origón átmenő egyenes==.
- Darabszámnál csak pontok vannak.
- Ami együtt nő, nem mindig arányos.
- **Fordított arányosság:** a szorzat állandó.

### Feliratok
- össz 1: egy pont = két adat, a sorrend számít
- össz 2: egyenes arányosság: a hányados állandó
- össz 3: grafikonja origón átmenő egyenes
- össz 4: együtt nő, mégsem arányos
- össz 5: fordított arányosság: a szorzat állandó
- mini egyenes: egyenes arányosság
- mini fordított: fordított arányosság

<!-- Tanári megjegyzések:
  - Kitalált példák: kifli 80 Ft/db, sajt 400 Ft / 10 dkg, taxi 1000 Ft alapdíj + 400 Ft/km (a valódi taxitarifában
    idődíj is van, és a díjat kilométer-részenként számolják). A lecke minden árat maga számol, és a .md eredményeit
    összeveti vele.
  - A torpedó rácspontokra lő (a koordináta-rendszer pontjaira), nem négyzetekre, mint a hagyományos papíros
    játék; a hajók a seedből determinisztikusan helyezkednek el, az „Új játék” új elrendezést ad.
  - A koordináta-rendszer itt csak az első síknegyedet mutatja (nemnegatív koordináták).
  - A 7. lépésben a 10, 15, 20, 30, 40, 60 km/h-hoz egész vagy fél óra tartozik; a csúszka köztes értékeinél
    (pl. 45 km/h) az idő kerekített, ezért ott „≈” áll.
  - A „Nem hiszem” játék a kerettanterv 11. témakörének javasolt tevékenysége; itt egyedül is játszható.
  - Tankönyvi jelölés: P(3; 2) pontosvesszővel, mert a vessző tizedesvessző.
-->
