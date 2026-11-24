# Hányszor hajtható félbe egy papír? – hatványok és normálalak
tantárgy: Matematika · évfolyam: 9–10. · témakör: 5. Hatvány, gyök

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/04-hatvany-normalalak.md
  Képlet a szövegben `…` között (2^3 → 2³, 10^-4 → 10⁻⁴, * → ·, - → −, <= → ≤).
  Feliratban a # jel helyére a lecke számot ír.
  A vásznon megjelenő hatványokat, normálalakokat, hajtásszámokat és vastagságokat a lecke számolja
  ki az alábbi méretadatokból. Az „eredmény” jellegű adatokat (hányadik hajtás ér el valameddig,
  hány atom fér el valamiben) a lecke újraszámolja, és eltérésnél piros hibasávot mutat. A panelszöveg
  képleteiben a számok szó szerint állnak: ha egy adatot átírsz, a hozzá tartozó szöveget is írd át.
-->

## Közös

### Feliratok
- bizonyítás: bizonyítás
- vázlat: vázlat
- log skála: log. skála: minden osztás tízszeres
- egység méter: méter
- tárgy atom: hidrogénatom
- tárgy DNS: a DNS-csavar vastagsága
- tárgy papír: a papírlap vastagsága
- tárgy ember: ember
- tárgy Everest: Mount Everest
- tárgy Föld: a Föld átmérője
- tárgy Hold: Föld–Hold távolság
- tárgy Nap: Föld–Nap távolság
- tárgy fényév: 1 fényév
- tárgy Tejút: a Tejút átmérője

### Adatok
<!-- Méretadatok (a lecke ebből számolja a normálalakot és a szalagon a helyet):
  - irodai papír (80 g/m²) vastagsága kb. 0,1 mm (gyártói adatlapok: 0,10–0,11 mm);
  - hidrogénatom: a Bohr-sugár 0,0529 nm, az átmérő kb. 0,1 nm (az atomnak nincs éles határa – nagyságrendi érték);
  - DNS kettős csavar átmérője kb. 2 nm (Watson–Crick-modell, B-DNS: 2,0 nm);
  - ember: 1,7 m (felnőtt, kerekítve);
  - Mount Everest: 8848,86 m (2020-as kínai–nepáli közös mérés), kerekítve 8849 m;
  - Föld közepes átmérője 12 742 km (közepes sugár 6371 km);
  - Föld–Hold közepes távolság 384 400 km (a középpontok között; NASA Moon Fact Sheet);
  - Föld–Nap közepes távolság 1 CSE = 149 597 870,7 km ≈ 149,6 millió km (IAU 2012);
  - 1 fényév = 9,4607 · 10¹⁵ m ≈ 9,461 billió km (billió = 10¹²);
  - a Tejút korongjának átmérője kb. 100 ezer fényév – a becslések 100–200 ezer fényév között szórnak
    (a csillagok korongja kb. 100 ezer, a halvány külső korong több). Ellenőrizve: 2026-11-24. -->
- papír vastagsága: 0,1 mm
- hidrogénatom átmérője: kb. 0,1 nm
- DNS átmérője: kb. 2 nm
- ember magassága: 1,7 m
- Everest magassága: 8849 m
- Föld átmérője: 12 742 km
- Hold távolsága: 384 400 km
- Nap távolsága: 149 600 000 km
- fényév: 9 461 000 000 000 km
- Tejút átmérője: kb. 100 ezer fényév

## 1. Hajtsuk félbe!
Egy irodai lap kb. **{papír vastagsága}** vastag. Minden félbehajtás ==megduplázza a rétegeket==, a lap felülnézetből viszont feleakkora lesz. Kézzel kb. {kézi hajtások} hajtás után elakadsz: a kis köteg vastag és merev. Tippelj: milyen vastag lenne 42 hajtás után?

> megjegyzés: A rekord 12 hajtás egy kb. 1,2 km hosszú papírcsíkkal (Britney Gallivan, 2002).

### Feliratok
- cím 1: Hányszor hajtható félbe egy papír?
- felülnézet: felülnézet
- oldalnézet: oldalnézet – a vastagság #× nagyítva
- A4: A4-es lap
- rétegek sablon: rétegek: #
- vastagság sablon: vastagság: #
- hajtás csúszka: hajtások száma
- kézi határ: kézzel kb. # hajtás a határ
- tipp kérdés: 42 hajtás után a köteg…
- tipp 1: …vastag, mint egy könyv
- tipp 2: …magas, mint egy felhőkarcoló
- tipp 3: …elér a Holdig

### Adatok
<!-- A4: 210 × 297 mm (ISO 216). Kézzel egy irodai lapot jellemzően 7-szer lehet félbehajtani (a „7-szer” közismert
     állítás, kísérleti tapasztalat, nem tétel). A rekord: Britney Gallivan, 2002. január, Pomona (Kalifornia), egy kb. 4000
     láb (kb. 1,2 km) hosszú vécépapír-csíkot hajtott félbe 12-szer, mindig ugyanabban az irányban (Guinness World
     Records: „Most times to fold a piece of paper”). A tanterv javasolt projektje: „hányszor lehet félbehajtani egy
     nagyméretű papírt? … például egy teljes guriga vécépapírral”. -->
- A4 rövid oldala: 210 mm
- A4 hosszú oldala: 297 mm
- kézi hajtások: 7

## 2. Duplázás: a kettő hatványai
Minden hajtás megduplázza a rétegeket: `n` hajtás után `2 · 2 · … · 2` réteg van, `n` tényezővel. Ez a **hatvány**: `2^n`, a 2 a *hatványalap*, az `n` a *hatványkitevő*. Tévhit: „minden hajtás egy lappal vastagít” – az csak `n + 1` lap lenne. ==Tíz hajtás: `2^10` = {tíz hajtás rétegei} réteg.==

> megjegyzés: `2^10 ≈ 10^3`: tíz duplázás kb. ezerszeres.

### Feliratok
- cím 2: Hány réteg lesz n hajtás után?
- tengely n: hajtások (n)
- tengely rétegek: rétegek
- görbe duplázás: duplázás: `2^n`
- görbe tévhit: tévhit: `n + 1` lap
- n csúszka: hajtások száma (n)
- táblázat n: n
- táblázat réteg: `2^n`
- táblázat vastagság: vastagság
- most sablon: `2^#` = # réteg
- tévhit sablon: tévhit: # lap

### Adatok
- tíz hajtás rétegei: 1024

## 3. A kitevők összeadódnak
Három hajtás, majd még négy: hét hajtás. `2^3 · 2^4`: három kettes szorzó, majd még négy, ==tehát a kitevők összeadódnak:== `2^3 · 2^4 = 2^7`. A `2^12` tévedés: az tizenkét szorzó lenne. Próbáld ki az osztást és a hatvány hatványát is!

### Feliratok
- cím 3: Hány kettes szorzó van?
- mód szorzás: Szorzás
- mód osztás: Osztás
- mód hatvány: Hatvány hatványa
- m csúszka: első kitevő (m)
- n csúszka 3: második kitevő (n)
- hajtás magyarázat: # hajtás, majd még #: # hajtás
- szorzás sablon: `2^# · 2^# = 2^#`
- osztás sablon: `2^# : 2^# = 2^#`
- osztás nevező sablon: `2^# : 2^# = 1 : 2^#`
- hatvány sablon: `(2^#)^# = 2^#`
- érték sablon: = #
- tévhit szorzás: tévhit: a kitevők szorzata
- tévhit képlet: `2^# · 2^# = 2^#`
- tévhit érték: # szorzó lenne: #
- biz szorzás: m darab szorzó, majd még n darab: m + n darab.
- biz osztás: Minden közös szorzópár kiesik (2 : 2 = 1).
- biz hatvány: n csoport, mindegyikben m szorzó: m · n darab.
- azonosság szorzás: `2^m · 2^n = 2^(m+n)`
- azonosság osztás: `2^m : 2^n = 2^(m-n)`
- azonosság hatvány: `(2^m)^n = 2^(mn)`
- minden m n: bármely pozitív egész m-re és n-re
- számláló: számláló
- nevező: nevező

## 4. Visszafelé: nulla és negatív kitevő
Lépj visszafelé! Balra minden lépés **feloszt** az alappal: `2^3 = 8`, `2^2 = 4`, `2^1 = 2`, tehát `2^0 = 1`, `2^-1 = 1/2`. ==A `2^0` nem 0, hanem 1; a `2^-3` nem negatív, hanem `1/8`.== Az osztás szabálya is ezt adja: `2^3 : 2^3 = 2^0 = 1`.

> megjegyzés: Ez definíció: így maradnak érvényesek az azonosságok. Az alap nem lehet 0.

### Feliratok
- cím 4: Mi jön, ha tovább felezünk?
- alap csúszka: hatványalap (a)
- balra osztás: balra: osztás #-vel
- jobbra szorzás: jobbra: szorzás #-vel
- tévhit nulla: tévhit: `3^0 = 0`
- tévhit negatív: tévhit: `2^-3 < 0`
- cáfolat oszlop: Minden oszlop pozitív – csak egyre kisebb.
- szabály nulla: `a^0 = 1`
- szabály negatív: `a^-n = [[1/a^n]]`
- osztás próba: `a^3 : a^3 = a^0 = 1`
- nem nulla: (a ≠ 0)

## 5. Hányadik hajtás ér el a Holdig?
Húzd a csúszkát! A köteg vastagsága 0,1 mm · `2^n`. {asztal-hajtás} hajtás után az asztal fölé ér, {Everest-hajtás} után az Everest fölé. ==A {Hold-hajtás}. hajtás után túlnő a Holdon!== Rakással ehhez kb. 3,8 billió lap kellene – duplázással csak 42 lépés.

> megjegyzés: A rajzon a magasság méretarányos, a köteg szélessége nem.

### Feliratok
- cím 5: Milyen magas a köteg n hajtás után?
- hajtás csúszka 5: hajtások száma (n)
- vastagság képlet: 0,1 mm · 2^#
- táblázat hajtás: hányadik hajtás?
- kb: ≈ #
- asztal: íróasztal
- ház: tízemeletes ház
- űrállomás: Nemzetközi Űrállomás
- Hold: Hold
- Nap: Nap
- Föld: Föld
- elérte: elérte: #
- szélesség: a köteg szélessége nem méretarányos

### Adatok
<!-- Asztal: íróasztal-magasság kb. 72–76 cm. Ház: tízemeletes lakóház kb. 30 m (11 szint · kb. 2,8 m) – becslés.
     Az ISS pályamagassága 370–460 km között változik (2020-as évek: kb. 410–420 km), a lecke kb. 400 km-rel rajzol.
     Hold átmérője 3474 km; Nap átmérője kb. 1,39 millió km (IAU névleges sugár 695 700 km).
     Hajtásszámok (a lecke számolja, a log₂ felfelé kerekítve): 0,75 m → log₂(7500) ≈ 12,87 → 13 (0,82 m);
     8849 m → log₂(88 490 000) ≈ 26,40 → 27 (13,4 km); 384 400 km → log₂(3,844 · 10¹²) ≈ 41,81 → 42
     (0,1 mm · 2⁴² = 439 804,65 km). Lapok egymásra rakva: 384 400 km : 0,1 mm = 3,844 · 10¹² ≈ 3,8 billió lap. -->
- asztal magassága: kb. 75 cm
- ház magassága: kb. 30 m
- ISS magassága: kb. 400 km
- Hold átmérője: 3474 km
- Nap átmérője: 1 390 000 km
- asztal-hajtás: 13
- Everest-hajtás: 27
- Hold-hajtás: 42
- Hold lapokban: kb. 3,8 billió

## 6. Normálalak: a · 10ⁿ
A nagyon nagy és a nagyon kicsi számot **normálalakban** írjuk: `a · 10^n`, ahol `1 <= a < 10` és `n` egész. A tizedesvesszőt addig léptetjük, amíg egyetlen nem nulla jegy marad előtte. ==Ahány lépés, annyi a kitevő: balra lépve pozitív, jobbra negatív.== Válassz számot!

> megjegyzés: A `45 · 10^3` nem normálalak, mert `45 >= 10`. Helyesen: `4,5 · 10^4`.

### Feliratok
- cím 6: Hová kerül a tizedesvessző?
- gomb Hold: Föld–Hold
- gomb papír: papírlap
- gomb atom: hidrogénatom
- gomb Nap: Föld–Nap
- balra sablon: # lépés balra
- jobbra sablon: # lépés jobbra
- szabály a: `1 <= a < 10`
- normálalak felirat: normálalakban:
- méterben: méterben:
- tévhit normál: `45 · 10^3`: nem normálalak, mert `45 >= 10`
- javítás normál: helyesen: `4,5 · 10^4`

## 7. Az atomtól a galaxisig
Ezen a szalagon ==minden osztás tízszeres==: egy lépés jobbra szorzás 10-zel. Így fér el egy ábrán az atom és a Tejút. Válassz két méretet! Normálalakban könnyű osztani: `(a · 10^n) : (b · 10^k) = (a : b) · 10^(n-k)`. A papír vastagságában {atomok a papírban} hidrogénatom fér el egymás mellett.

### Feliratok
- cím 7: Az atomtól a Tejútig
- A csúszka: első méret (A)
- B csúszka: második méret (B)
- hányados cím: A : B – hányszorosa A a B-nek?
- nagyságrend nagyobb: A kb. # nagyságrenddel nagyobb
- nagyságrend kisebb: A kb. # nagyságrenddel kisebb
- nagyságrend egyenlő: A és B azonos nagyságrendű
- kattints: Kattints egy tárgyra: A, majd B!

### Adatok
<!-- 0,1 mm : 0,1 nm = 10⁻⁴ m : 10⁻¹⁰ m = 10⁶ (a lecke számolja). -->
- atomok a papírban: kb. 1 millió

## 8. Mekkora hiba egy nagyságrend?
Becsüld meg! Húzd a jelölőt oda, ahol szerinted a méret van, majd nyomd meg: Mutasd! Egy **nagyságrend** eltérés tízszeres hiba. ==A `10^-6` m kicsi, de nem „majdnem nulla”:== {atomok egy mikronban} hidrogénatom fér el benne.

<!-- Tanári tipp: egy cikk számánál először a nagyságrendet ellenőrizzük. -->

### Feliratok
- cím 8: Hová esik a szalagon?
- gomb homok: homokszem
- gomb ország: Magyarország
- gomb Nap átmérő: a Nap
- kérdés homok: Mekkora egy homokszem?
- kérdés ország: Milyen hosszú Magyarország kelet–nyugat?
- kérdés Nap: Mekkora a Nap átmérője?
- tipp csúszka: a tipped
- tipp: tipp
- mutasd gomb: Mutasd!
- eltérés sablon: eltérés: # nagyságrend
- szoros sablon: ≈ #-szoros hiba
- talált: Talált! Egy nagyságrenden belül vagy.
- mikron: 10^-6 m : 10^-10 m = 10^4
- mikron atom: # hidrogénatom fér el egymás mellett

### Adatok
<!-- Homok: a „homok” szemcsemérete 0,063–2 mm (szemcseméret-osztályozás); a közepes homok kb. 0,25–0,5 mm, a lecke
     kb. 0,5 mm-rel számol (nagyságrendi becslés). Magyarország legnagyobb kelet–nyugati kiterjedése 528 km, észak–déli
     268 km (Magyarország Nemzeti Atlasza, MTA CSFK; a Wikipédia más módszerrel 524 km-t ír). A Nap átmérője kb.
     1,39 millió km (lásd fent). 10⁻⁶ m : 10⁻¹⁰ m = 10⁴. -->
- homokszem: kb. 0,5 mm
- Magyarország szélessége: 528 km
- atomok egy mikronban: 10 000

## 9. Összefoglalás
- `a^m · a^n = a^(m+n)`, `a^m : a^n = a^(m-n)`, `(a^m)^n = a^(mn)`
- `a^0 = 1` és `a^-n = [[1/a^n]]`, ha `a != 0`
- normálalak: `a · 10^n`, ahol `1 <= a < 10`

==Duplázás: egy hajtás. Tízszerezés: egy nagyságrend.== {Világegyetem-hajtás} hajtás után a köteg hosszabb lenne, mint a látható Világegyetem átmérője!

### Feliratok
- cím 9: Hatványok – összefoglalás
- össz azonosságok: azonosságok (a ≠ 0)
- össz normálalak: normálalak
- össz példa: 384 400 km = 3,844 · 10^8 m
- össz 1: `a^m · a^n = a^(m+n)`
- össz 2: `a^m : a^n = a^(m-n)`
- össz 3: `(a^m)^n = a^(mn)`
- össz wow: # hajtás:
- össz wow 2: több, mint a látható Világegyetem (≈ #)
- hajtás rövid: hajtás
- Világegyetem: a látható Világegyetem

### Adatok
<!-- A megfigyelhető (látható) Világegyetem átmérője kb. 93 milliárd fényév ≈ 8,8 · 10²⁶ m (együttmozgó távolság).
     0,1 mm · 2¹⁰³ ≈ 1,01 · 10²⁷ m ≈ 1,07 · 10¹¹ fényév > 9,3 · 10¹⁰ fényév; 2¹⁰² · 0,1 mm ≈ 5,1 · 10²⁶ m még kevesebb.
     A lecke számolja. -->
- Világegyetem átmérője: kb. 93 milliárd fényév
- Világegyetem-hajtás: 103

<!-- Matematikai ellenőrzés (2026-11-24, Pythonnal, egész/lebegőpontos számolással):
  - 2¹⁰ = 1024; 2⁷ = 128 (0,1 mm · 128 = 12,8 mm); A4 hétszer felezve: 26,25 × 37,125 mm (A11 közelítőleg).
  - 2³ · 2⁴ = 2⁷ = 128; 2¹² = 4096 (tévhit); 2⁷ : 2³ = 2⁴; (2³)² = 2⁶ = 64; a csúszkák minden m, n ∈ {1, …, 6}
    párjára a csempék száma = a kitevő (L.checks).
  - 2⁰ = 1, 2⁻¹ = 1/2, 2⁻³ = 1/8; 3⁰ = 1; 10⁻³ = 1/1000.
  - 0,1 mm · 2¹³ = 0,8192 m > 0,75 m > 2¹² · 0,1 mm = 0,4096 m; 0,1 mm · 2²⁷ = 13 421,8 m > 8849 m > 6710,9 m;
    0,1 mm · 2⁴² = 439 804,65 km > 384 400 km > 219 902,3 km (2⁴¹); a Nap (149,6 millió km): 51 hajtás.
  - normálalak: 384 400 000 m = 3,844 · 10⁸ m; 0,0001 m = 1 · 10⁻⁴ m; 0,000 000 000 1 m = 1 · 10⁻¹⁰ m;
    149 600 000 000 m = 1,496 · 10¹¹ m; 45 · 10³ = 4,5 · 10⁴.
  - hányadosok: 10⁻⁴ : 10⁻¹⁰ = 10⁶; 10⁻⁶ : 10⁻¹⁰ = 10⁴; Föld–Nap : Föld-átmérő = 1,496 · 10¹¹ : 1,2742 · 10⁷ ≈ 1,17 · 10⁴.
  - 103 hajtás: 0,1 mm · 2¹⁰³ ≈ 1,014 · 10²⁷ m > 8,8 · 10²⁶ m; 102 hajtás ≈ 5,07 · 10²⁶ m < 8,8 · 10²⁶ m.
  A „hány nagyságrend” a két méret hányadosának tízes alapú logaritmusa, egy tizedesre kerekítve; a lg szót a lecke
  nem használja (a logaritmus a 11. évfolyam anyaga). -->
