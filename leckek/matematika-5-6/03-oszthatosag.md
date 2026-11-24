# Miért nem lehet 7 sütit téglalapba rakni? – osztók, prímek, maradékok
tantárgy: Matematika · évfolyam: 5–6. · témakör: 3. Természetes számok halmaza, számelméleti ismeretek

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/03-oszthatosag.md
  Feliratban a # jel helyére a lecke számot ír (pl. „A # osztói” → „A 12 osztói”). Az „osztható #” és a
  „nem osztható #” feliratban a lecke a toldalékot is odateszi (9-cel, 4-gyel, 10-zel).
  Az eredményeket (osztók, prímek száma, prímtényezők, jegyösszeg, lkkt, lnko) a lecke maga számolja,
  és piros sávval jelez, ha a .md-ben írt érték nem egyezik a számolásával.
-->

## Közös

### Feliratok
- tippelj: Tippelj előbb!
- a tipped: a te tipped
- jó tipp: jó tipp!
- rossz tipp: nem talált
- prím: prím
- összetett: összetett
- forgasd: Forgasd egérrel!
- osztható: osztható #
- nem osztható: nem osztható #, maradék: #

## 1. Sütik téglalapban
Van {sütik száma} sütid. Sorokba rakod őket, hézag nélkül, **téglalap** alakban. ==Tippelj előbb!== Hányféle téglalap jön ki? A téglalap oldalai a szám **osztói**: `3 * 4 = 12`. Az elforgatott téglalap ugyanaz.

> megjegyzés: Húzd a csúszkát! Melyik számból jön ki csak egy sor?

### Feliratok
- kérdés 1: Hányféle téglalapba rakható # süti?
- tipp téglalap: # téglalap
- sütik csúszka: sütik száma
- osztói: A # osztói:
- osztók száma: # osztó
- csak egy sor: csak egy sor: prím!
- egy osztó: az 1: csak egy osztója van
- maradék sor: # sorokba? # marad
- négyzet: négyzet (# · #): páratlan sok osztó

### Adatok
- sütik száma: 12
- téglalapok száma: 3
- a 12 osztói: 1; 2; 3; 4; 6; 12
<!-- 12 = 1 · 12 = 2 · 6 = 3 · 4 → 3 téglalap, 6 osztó. A 36 osztói 1; 2; 3; 4; 6; 9; 12; 18; 36 (9 osztó,
     páratlan sok, mert 6 · 6 négyzet). A lecke a téglalapokat és az osztókat a „sütik száma” adatból számolja. -->

## 2. Prímek: csak egy sor
Amiből csak egy sor jön ki, az **prím**: pontosan két osztója van, az 1 és önmaga. Az 1 nem prím. Eratoszthenész **szitája** sorra kihúzza a 2, 3, 5, 7 többszöröseit. ==100-ig {prímek száma 100-ig} prím marad.==

> megjegyzés: Kattints egy számra! Miért elég a 7-ig szitálni?

### Feliratok
- kérdés 2: Melyik szám prím 100-ig?
- többszörösei: a # többszörösei
- kihúzva: # kihúzva
- az 1: 1: nem prím, nem összetett
- a 2: 2: páros, mégis prím
- a 9: 9 = 3 · 3: páratlan, mégsem prím
- elég: 11 · 11 = 121 > 100: kész!
- maradt: 100-ig # prím maradt
- kattints: Kattints egy számra!
- prím sablon: #: prím, csak 1 · #
- szorzat sablon: # = # · #

### Adatok
- prímek száma 100-ig: 25
<!-- A prímek 100-ig: 2; 3; 5; 7; 11; 13; 17; 19; 23; 29; 31; 37; 41; 43; 47; 53; 59; 61; 67; 71; 73; 79; 83;
     89; 97 – 25 darab. Elég a 7-ig szitálni: minden 100-nál kisebb összetett számnak van 10-nél kisebb
     prímosztója (különben legalább 11 · 11 = 121 lenne). -->

## 3. Prímtényezős felbontás
Bontsd a számot két szám szorzatára, és a darabokat is, amíg csak prímek maradnak! Kezdheted bárhogy, például `36 * 10` vagy `8 * 45`. ==A végén mindig ugyanazok a prímek jönnek ki.==

képlet: 360 = 2^3 * 3^2 * 5

> megjegyzés: Próbálj másik fát és másik számot!

### Feliratok
- kérdés 3: Bontsd fel a #-at prímek szorzatára!
- másik fa: Másik fa
- másik szám: Másik szám
- ugyanaz: ugyanazok a prímek!
- egyik fa: egyik fa
- másik fa felirat: másik fa

### Adatok
- felbontandó számok: 360; 840
- a 360 prímtényezői: 2; 2; 2; 3; 3; 5
- a 840 prímtényezői: 2; 2; 2; 3; 5; 7
<!-- 360 = 2 · 2 · 2 · 3 · 3 · 5 = 2³ · 3² · 5; 840 = 2³ · 3 · 5 · 7. A „képlet:” sor a 360-ra vonatkozik –
     ha a felbontandó számokat átírod, azt is írd át. A lecke a fákat maga bontja, és összeveti a listákkal.
     Felbontandó szám legfeljebb 1000 (a kerettanterv számköre). -->

## 4. A felcsavart számegyenes
Tekerd a számegyenest egy hasábra, amelynek {hasáb oldalai} oldallapja van! Minden szám arra a lapra kerül, amennyi a **maradéka** {hasáb oldalai}-tal osztva. ==Az azonos maradékú számok egy lapon sorakoznak.== A 6 többszörösei egy, a 3 többszörösei két lapra esnek.

> megjegyzés: Próbáld ki a 4-et és az 5-öt is!

### Feliratok
- kérdés 4: Tekerjük fel a számegyenest!
- oldalak csúszka: a hasáb oldallapjai
- kiemelt csúszka: kiemelt többszörösök
- lapon sablon: a # többszörösei: # lapon
- minden lapon: a # többszörösei: minden lapon
- lap = maradék: a lap száma = a maradék

### Adatok
- hasáb oldalai: 6
- kiemelt szám: 3
<!-- 6 oldalú hasábon a szám a (szám : 6) maradékának lapjára kerül. A d többszörösei 6 : lnko(6; d) lapra esnek:
     a 6-éi 1, a 3-éi 2, a 2-éi és a 4-éi 3, az 5-éi mind a 6 lapra. A „{hasáb oldalai}-tal” toldalék a 6-hoz
     illik – ha átírod, a mondatot is igazítsd. A kerettanterv javasolt tevékenysége: „Oszthatósági tulajdonságok
     megfigyelése 3, 4, 5, … oldalú hasábra felcsavart számegyenes segítségével”. -->

## 5. Elég ránézni?
A tízes rúd, a százas lap és az ezres kocka osztható 2-vel, 5-tel, 10-zel: ==csak az utolsó jegy dönt.== A 100 osztható 4-gyel: az utolsó két jegy dönt. 9-nél minden elemből 1 marad (`10 = 9 + 1`): a **jegyek összege** dönt.

> megjegyzés: 6-tal osztható, ami 2-vel és 3-mal is.

### Feliratok
- kérdés 5: #: osztható #?
- szám csúszka: a vizsgált szám
- kész: biztosan osztható
- marad: ez dönt
- csoportok: # csoport, maradék: #
- ezres: ezres
- százas: százas
- tízes: tízes
- egyes: egyes
- jegyösszeg felirat: jegyösszeg

### Adatok
- vizsgált szám: 4527
- jegyösszeg: 18
- hányados 9-cel: 503
<!-- 4527 = 4 · 1000 + 5 · 100 + 2 · 10 + 7 = 4 · 999 + 5 · 99 + 2 · 9 + (4 + 5 + 2 + 7); 4 + 5 + 2 + 7 = 18,
     ami osztható 9-cel (és 3-mal) → 4527 : 9 = 503. 4527 = 452 · 10 + 7 → nem osztható 2-vel, 5-tel, 10-zel.
     4527 = 45 · 100 + 27 → 27 : 4 = 6, maradék 3 → nem osztható 4-gyel. A lecke számolja és összeveti. -->

## 6. Mikor szól a kettő együtt?
„**Bumm**” játék: az egyik csapat a {ritmus 1} többszöröseinél tapsol, a másik a {ritmus 2} többszöröseinél dobbant. Sokan a két szám szorzatára tippelnek. ==Pedig már a {legkisebb közös többszörös}-nél!== Ez a **legkisebb közös többszörös**. A többi közös többszörös ennek többszöröse.

> megjegyzés: Próbáld ki az 5-öt és a 7-et!

### Feliratok
- kérdés 6: Mikor tapsolnak és dobbantanak együtt?
- taps: taps: a # többszörösei
- dobbantás: dobbantás: a # többszörösei
- bumm: BUMM!
- ritmus 1 csúszka: tapsolók száma
- ritmus 2 csúszka: dobbantók száma
- közös többszörösök: közös többszörösök:
- lkkt sablon: legkisebb közös többszörös: #
- tévhit szorzat: # · # = #? Előbb is találkoznak!
- szorzat jó: itt épp a szorzat a legkisebb

### Adatok
- ritmus 1: 4
- ritmus 2: 6
- legkisebb közös többszörös: 12
<!-- A 4 többszörösei: 4; 8; 12; 16; 20; 24 …; a 6 többszörösei: 6; 12; 18; 24 …; közös: 12; 24; 36 … → lkkt = 12.
     A kerettanterv példája (5 és 7) a csúszkákkal kipróbálható: lkkt(5; 7) = 35 = 5 · 7. A lecke számolja és összeveti. -->

## 7. Miért 13 vagy 17 év?
Észak-Amerikában egyes **kabócák** 13 vagy 17 évig élnek a föld alatt, aztán egyszerre bújnak elő. Egy **hipotézis** (feltevés) szerint a prím hosszúságú ciklus ritkán esik egybe a ragadozók rövidebb ciklusával. ==Prímnél a közös többszörös messze van.== Bizonyítva nincs.

> megjegyzés: Állítsd 12 évre, aztán 13-ra!

### Feliratok
- kérdés 7: Mikor találkozik a kabóca a ragadozóval?
- kabóca csúszka: a kabóca ciklusa
- ragadozó csúszka: a ragadozó ciklusa
- kabóca: kabócák előbújása: # évente
- ragadozó: ragadozók csúcsa: # évente
- találkozás: találkozás
- találkozás sablon: # évente találkoznak
- ragadozó ciklusai: ha a ragadozó ciklusa …
- év sablon: # év
- hipotézis: hipotézis
- év: év

### Adatok
- kabóca ciklusa: 13 év
- másik kabóca ciklusa: 17 év
- kezdő ciklus: 12 év
- ragadozó ciklusa: 4 év
<!-- Periodikus kabócák (Magicicada nem): Észak-Amerika keleti része, 13 és 17 éves életciklus; a lárvák a föld
     alatt fejlődnek, a kifejlett rovarok egyszerre, tömegesen bújnak elő. A prím ciklust magyarázó ragadozó-hipotézist
     S. J. Gould népszerűsítette (Ever Since Darwin, 1977); más feltevés szerint a prím ciklus a különböző ciklusú
     csoportok kereszteződését ritkítja (Yoshimura, 1997). Egyik sem bizonyított – a lecke „hipotézis” bélyeggel jelzi.
     A ragadozók 2–6 éves ciklusa didaktikus feltevés, nem mért adat. A „kezdő ciklus” (12 év) kitalált összehasonlítás.
     Ellenőrizendő forrás: Williams & Simon (1995), Annual Review of Entomology 40: 269–295. -->

## 8. A legnagyobb közös csempe
Egy {téglalap egyik oldala} × {téglalap másik oldala}-as téglalapot fednél le négyzetcsempékkel, vágás nélkül. A csempe oldala mindkét számnak osztója: **közös osztó**. ==A legnagyobb közös osztó {legnagyobb közös osztó}.== Ezzel a csempével {csempék száma} darab elég.

> megjegyzés: Melyik csempe hagy rést?

### Feliratok
- kérdés 8: Mekkora a legnagyobb négyzetcsempe?
- egyik csúszka: a téglalap egyik oldala
- másik csúszka: a téglalap másik oldala
- csempe csúszka: a csempe oldala
- osztói halmaz: a # osztói
- közös osztók: közös osztók
- lnko sablon: legnagyobb közös osztó: #
- csempe jó: # csempe, nincs rés
- csempe rossz: a # nem közös osztó: rés marad

### Adatok
- téglalap egyik oldala: 12
- téglalap másik oldala: 18
- legnagyobb közös osztó: 6
- csempék száma: 6
<!-- A 12 osztói: 1; 2; 3; 4; 6; 12; a 18 osztói: 1; 2; 3; 6; 9; 18; közös osztók: 1; 2; 3; 6 → lnko(12; 18) = 6.
     A 12 × 18-as téglalap 2 · 3 = 6 darab 6 × 6-os csempével fedhető le. A lecke számolja és összeveti. -->

## 9. Összefoglalás
- **Osztó:** a téglalap oldala. **Prím:** csak egy sor.
- **Felbontás:** mindig ugyanazok a prímek.
- **Maradék:** a hasáb lapja.
- 2, 5, 10: utolsó jegy · 4, 100: utolsó két jegy · 3, 9: jegyösszeg.
- **Közös többszörös**, **közös osztó**.
- ==Vizsgálj meg egy számot!==

### Feliratok
- vizsgáld csúszka: a vizsgált szám
- vizsgálat cím: Mit tudunk erről a számról?
- felbontás: felbontás:
- prím felbontás: csak önmaga: #
- szabály 2: utolsó jegy páros
- szabály 3: jegyösszeg osztható 3-mal
- szabály 4: utolsó két jegy osztható 4-gyel
- szabály 5: utolsó jegy 0 vagy 5
- szabály 6: 2-vel és 3-mal is
- szabály 9: jegyösszeg osztható 9-cel
- szabály 10: utolsó jegy 0
- szabály 100: utolsó két jegy 00
- osztó oszlop: osztó
- szabály oszlop: szabály
- igen nem oszlop: osztható?

### Adatok
- összefoglaló szám: 360

<!-- Tanári megjegyzések:
  - A lecke a kerettanterv szavait használja: osztó, többszörös, közös osztó, közös többszörös, prímszám, összetett
    szám, prímtényezős felbontás. A legkisebb közös többszörös és a legnagyobb közös osztó rövidítése (lkkt, lnko)
    és jele ([12; 18], (12; 18)) tankönyvenként eltér – a lecke kiírja a nevüket.
  - A 0 osztóiról és a 0 oszthatóságáról a lecke nem beszél; a számegyenes a hasábon a 0-tól indul (a 0 minden
    szám többszöröse – ezért van a 0 minden kiemelésben).
  - Tévhitek, amelyekre a lecke ellenpéldát mutat: az 1 prím (2. lépés); minden páratlan szám prím (9 = 3 · 3);
    a 2 nem prím, mert páros; a legkisebb közös többszörös a két szám szorzata (4 · 6 = 24, de már 12).
    Kimaradt (szóban érdemes): „ami osztható 2-vel és 4-gyel, az 8-cal is” – ellenpélda: 12.
  - Az 5. lépés Dienes-készlete arányos (egy kis kocka = 1); az „ez dönt” korongok a maradék-jelöltek, a
    méretük nem arányos. A 25-tel való oszthatóság (az utolsó két jegy) nem szerepel a kerettantervben, kimaradt.
  - A kabócás lépés hipotézis, nem bizonyított tény (lásd a 7. lépés megjegyzését).
  - A sütik, a csempék és a „Bumm” számai didaktikai példák.
-->
