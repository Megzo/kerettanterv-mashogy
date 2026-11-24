# Hová kerül a 15? – halmazok, „és”, „vagy”
tantárgy: Matematika · évfolyam: 5–6. · témakör: 1. Halmazok

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/01-halmazok.md
  Feliratban a # jel helyére a lecke számot vagy szöveget ír (pl. „Hová kerül a #?” → „Hová kerül a 15?”).
  A tulajdonságok (páros, prím…) SZÖVEGE itt átírható, a JELENTÉSÜK (melyik szám páros) a kódban van.
  Az eredményeket (elemszámok, elemek listája) a lecke kiszámolja, és piros sávval jelez,
  ha a .md-ben írt érték nem egyezik a számolásával.
-->

## Közös

### Feliratok
- alaphalmaz felirat: alaphalmaz: az egész számok 1-től 20-ig
- páros: páros
- páratlan: páratlan
- 3-mal osztható: 3-mal osztható
- 10-nél nagyobb: 10-nél nagyobb
- prím: prím
- 5-re végződik: 5-re végződik
- 4-gyel osztható: 4-gyel osztható
- igen: igen
- nem: nem
- tippelj: Tippelj előbb!
- a tipped: a te tipped
- és sablon: # és #
- vagy sablon: # vagy #
- nem sablon: nem #
- pontosan sablon: vagy #, vagy #
- egyik sem sablon: se nem #, se nem #
- elemszám: # elem
- üres halmaz: üres halmaz

### Adatok
- alaphalmaz: 1–20
- páros számok száma: 10
- 3-mal oszthatók száma: 6
- közös rész elemei: 6; 12; 18
- egyesítés elemszáma: 13
- egyik sem elemei: 1; 5; 7; 11; 13; 17; 19
<!-- Az alaphalmaz 1-től 20-ig. Páros: 2; 4; …; 20 (10 elem). 3-mal osztható: 3; 6; 9; 12; 15; 18 (6 elem).
     Közös rész: 6; 12; 18 (3 elem). Egyesítés: 10 + 6 − 3 = 13. Egyik sem: 20 − 13 = 7 elem.
     Ha az alaphalmazt átírod (legfeljebb 1–20), ezeket is át kell írni – a lecke szól, ha nem egyeznek. -->

## 1. Válogassunk!
Itt van húsz számkártya, 1-től 20-ig: ez az **alaphalmaz**. A páros számokat egy körbe tesszük. Ők alkotják a páros számok **halmazát**. A 4 **eleme** a halmaznak, a 7 nem eleme. ==Minden számról eldönthető: benne van, vagy nincs.==

> megjegyzés: Válassz más tulajdonságot is a gombokkal!

### Feliratok
- válogatás cím: Melyik szám kerül a körbe?

## 2. Két szempont egyszerre
Most két kör van: **A** a páros számok, **B** a 3-mal osztható számok halmaza. A két kör egymásba lóg. ==Tippelj előbb!== Hová kerül a {vizsgált szám}? Gondold végig: páros? Osztható 3-mal?

> megjegyzés: Kattints egy kártyára: megmutatja, melyik feltétel igaz rá.

### Feliratok
- hová cím: Hová kerül a #?
- tipp csak A: csak az A-ba
- tipp közös: a közös részbe
- tipp csak B: csak a B-be
- tipp egyik sem: egyik körbe sem

### Adatok
- vizsgált szám: 15
<!-- A 15 páratlan, de osztható 3-mal → a B-be kerül, a közös részen kívülre. Ha átírod (1–20), a lecke a jó
     választ magától kiszámolja. -->

## 3. „És”: a közös rész
A két kör **közös részébe** azok a számok kerülnek, amelyek párosak **és** 3-mal oszthatók. ==Az „és” azt jelenti: mindkét feltétel igaz.== Ezek: \{{közös rész elemei}\}. A 15 csak az egyik feltételnek felel meg, ezért nincs itt.

### Feliratok
- és cím: Melyik szám páros és 3-mal osztható is?

## 4. „Vagy”: az egyesítés
Az **egyesítésbe** azok kerülnek, amelyek párosak **vagy** 3-mal oszthatók. Tévhit: a „vagy” kizárja, hogy mindkettő igaz legyen. ==A matekban a „vagy” megengedő: mindkettő is jó!== Így a 6, a 12 és a 18 is benne van.

> megjegyzés: Hasonlítsd össze: „vagy…, vagy…”!

### Feliratok
- vagy cím: Melyik szám páros vagy 3-mal osztható?
- vagy gomb: vagy
- vagyvagy gomb: vagy…, vagy…
- mindkettő jó: mindkettő is jó!
- kimarad: kimarad: mindkettő igaz

## 5. Hányan vannak?
==Tippelj előbb!== Hány szám van az egyesítésben? Csábító összeadni: {páros számok száma} + {3-mal oszthatók száma}. De így a közös rész számait **kétszer** számolnánk! Az egyesítés elemszáma: a két elemszám összege, **mínusz** a közös rész elemszáma.

### Feliratok
- hány cím: Hány szám van az egyesítésben?
- tipp szám: # szám
- kétszer: kétszer számoltuk!
- egyesítésben: az egyesítésben # szám van

## 6. „Nem”: a kiegészítő halmaz
Melyik szám **nem** páros? Az alaphalmaz többi eleme: ez az A **kiegészítő halmaza**. Tévhit: ami egyik körben sincs, az „nem tartozik sehova”. ==Pedig ezek is az alaphalmaz elemei!==

> megjegyzés: Nézd meg a „se nem…, se nem…” gombot is!

### Feliratok
- nem cím: Ami kimaradt, az is a téglalapban van!
- nem A gomb: nem A
- nem B gomb: nem B
- egyik sem gomb: se nem A, se nem B
- alaphalmaz elemei: ezek is az alaphalmaz elemei!

## 7. Részhalmaz
A 4-gyel osztható számok mind párosak. Így a B minden eleme benne van A-ban: B **részhalmaza** A-nak. A kör belecsúszik a másikba. ==Egyetlen ellenpélda elég, és már nem részhalmaz.== Minden halmaz önmagának is részhalmaza.

> megjegyzés: Próbáld ki a gombokat!

### Feliratok
- rész cím: Benne van-e B minden eleme A-ban?
- üres rész: ez a rész üres!
- részhalmaz igen: B részhalmaza A-nak
- részhalmaz nem: B nem részhalmaza A-nak
- ellenpélda: ellenpélda: #
- önmaga: B = A: önmagának is részhalmaza

## 8. Halmaz a számegyenesen
„**Legalább** {legalább érték}”: ez is jó, és minden nagyobb. „**Legfeljebb** {legfeljebb érték}”: ez is jó, és minden kisebb. ==Az „és” itt is a közös rész.== A teli karika: a szám benne van. Az üres karika: már nincs benne.

> megjegyzés: A vastag vonal a köztes törteket is jelöli.

### Feliratok
- legalább sablon: legalább #
- legfeljebb sablon: legfeljebb #
- kisebb sablon: kisebb, mint #
- és szó: és
- vagy szó: vagy
- legalább csúszka: legalább …
- legfeljebb csúszka: legfeljebb / kisebb, mint …
- kisebb gomb: legfeljebb ↔ kisebb, mint
- és vagy gomb: és ↔ vagy
- egész számok: # egész szám
- minden szám: minden szám benne van!

### Adatok
- legalább érték: 3
- legfeljebb érték: 8
- egész számok száma: 6
<!-- A számegyenes 0-tól 12-ig. „Legalább 3 és legfeljebb 8”: 3; 4; 5; 6; 7; 8 → 6 egész szám
     (8 − 3 + 1 = 6). „Kisebb, mint 8” esetén a 8 kimarad (üres karika) → 5 egész szám.
     „Legalább 3 vagy legfeljebb 8”: minden szám 0 és 12 között. Az „egész számok száma” eredményt a lecke összeveti. -->

## 9. Összefoglalás
- **Közös rész** („és”): mindkettő igaz.
- **Egyesítés** („vagy”): legalább az egyik igaz.
- **Kiegészítő halmaz** („nem”): a többi elem.
- **Részhalmaz:** minden eleme a másikban is benne van.
- ==Válassz két tulajdonságot!==

### Feliratok
- A csúszka: A halmaz
- B csúszka: B halmaz
- és gomb: és
- vagy gomb 9: vagy
- nem A gomb 9: nem A
- pontosan gomb: pontosan az egyik
- játék cím: Válassz két tulajdonságot!
- A része B: A részhalmaza B-nek
- nincs közös: nincs közös elemük

<!-- Tanári megjegyzések:
  - A lecke a kerettanterv szavait használja: halmaz, elem, alaphalmaz, halmazábra, közös rész, egyesítés,
    kiegészítő halmaz, részhalmaz. A ∩, ∪ jeleket szándékosan nem mutatja (tankönyvenként eltér, mikor vezetik be);
    a halmazt kapcsos zárójellel, pontosvesszővel írja: {6; 12; 18}.
  - Az alaphalmaz jele tankönyvenként U vagy H; a lecke csak szóval írja („alaphalmaz”).
  - A 2. lépésben a 15 a két kör határán vár a tippre; a jó választ a lecke a számból számolja.
  - A 7. lépés ellenpéldája mindig a B legkisebb olyan eleme, amely nincs A-ban (3-mal osztható: 3; páratlan: 1).
  - A 9. lépés kísérletező ábrája az elemek alapján rendezi el a köröket: ha nincs közös elem, a körök
    szétválnak; ha az egyik halmaz részhalmaza a másiknak, a kör belecsúszik; ha ugyanaz a két halmaz, a körök fedik
    egymást. Az elrendezés mindig az 1–20 alaphalmazra vonatkozik (pl. a „prím” és a „4-gyel osztható” itt nem fed át).
  - A prímek 20-ig: 2; 3; 5; 7; 11; 13; 17; 19 (8 db). Az 1 nem prím.
  - A számegyenesen a pöttyök az egész számok, a vastag vonal a köztes (tört) számokat is jelöli; ezt a tanár
    kihagyhatja, ha az osztály még nem tanulta a törteket.
-->
