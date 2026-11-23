# Milyen hosszú a négyzet átlója? – a √2 és az irracionális számok
tantárgy: Matematika · évfolyam: 9–10. · témakör: 4. Számhalmazok, műveletek (+ 5. Hatvány, gyök)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/01-gyok-ketto.md
  Képlet a szövegben `…` között (x^2 → x², * → ·, - → −, √(…)). Feliratban a # jel helyére a lecke számot ír.
  A vásznon megjelenő számokat (négyzetek, maradékok, tizedesjegyek, különbségek) a lecke számolja ki
  az alábbi adatokból; a panelszöveg képleteiben a számok szó szerint állnak – ha egy adatot átírsz,
  a hozzá tartozó szöveget is írd át.
-->

## Közös

### Feliratok
- gyök 2: `√2`
- mérés: mérés
- bizonyítás: bizonyítás

### Adatok
<!-- √2 = 1,41421356…; a lecke ellenőrzi, hogy ez a kerekítés 0,0005-ön belül van. -->
- gyök kettő: 1,414

## 1. Négyzet átlója: hány egység?
Az egységnégyzet átlója hosszabb az oldalánál, de rövidebb kettőnél – mérve kb. 1,4. Pontosan mennyi? Rajzoljunk négyzetet az átlóra! Két egységnégyzetet átlósan félbevágunk, és a négy fél éppen kitölti. ==Az átlóra rajzolt négyzet területe 2, tehát az átló `d = √2`.==

> megjegyzés: Pitagorasz-tétellel ugyanez: `1^2 + 1^2 = d^2`.

### Feliratok
- kérdés 1: Milyen hosszú az egységnégyzet átlója?
- mérve: vonalzóval mérve:
- két egységnégyzet: két egységnégyzet: `1 + 1 = 2`
- átló négyzete: az átlóra rajzolt négyzet:
- négy fél: `d^2 = 4 · 1/2 = 2`
- átló: `d = √2`
- pitagorasz: Pitagorasz-tétellel:
- pitagorasz képlet: `1^2 + 1^2 = d^2`
- újra 1 gomb: Rakd össze újra!

## 2. Körzővel a számegyenesre
Szúrd a körzőt a 0-ba, nyisd az átló hosszára, és forgasd le az egyenesre! A metszéspont **pontosan** a √2. ==Az irracionális szám is „igazi”: megszerkeszthető.== Ha az új átlóra 1 egység magas derékszögű háromszöget rajzolunk, jön a √3, a 2, a √5…

> megjegyzés: Ez a „Theodórosz-csiga”. Nyomd meg a gombot többször!

### Feliratok
- tévhit szerkeszt: „Az irracionális szám nem igazi – nem lehet megszerkeszteni.”
- cáfolat szerkeszt: Körzővel pontosan felmérhető!
- csiga szabály: Minden új átló négyzete 1-gyel nagyobb:
- gyök 3: `√3`
- gyök 4: `√4 = 2`
- gyök 5: `√5`
- következő gomb: Következő gyök
- csak gyök 2 gomb: Vissza a √2-höz

## 3. Tizedesjegyek: nagyítás
Nagyíts rá a pontra! Minden nagyításnál egy újabb tizedesjegy derül ki, és a √2 mindig két szomszédos osztás közé esik: `1,41^2 < 2 < 1,42^2`. ==Akárhány jegyet írunk le, csak közelítést kapunk.== A számológép is kerekít.

> megjegyzés: Kérdezd meg: hányadik jegynél áll meg? (Sehol – ezt a 6. lépés bizonyítja.)

### Feliratok
- nagyítás: nagyítás:
- tévhit kerekít: „A √2 pontosan 1,41 – csak a gép kerekít.”
- alsó határ: alsó határ
- felső határ: felső határ
- négyzete: négyzete
- nagyíts gomb: Nagyíts!
- kicsinyíts gomb: Kicsinyíts

### Adatok
<!-- Ha átírod, a tévhit felirata (fent) is változzon. A cáfoló négyzetet a lecke számolja. -->
- kerekített érték: 1,41

## 4. Törtek: véges vagy szakaszos
Osszuk el az 1-et 7-tel! A maradék csak 0, 1, …, 6 lehet. Ha 0 jön, vége; ha nem, legkésőbb a hetedik maradék már ismétlődik – és vele a jegyek is. ==Egy tört tizedes alakja véges vagy szakaszos.== Fordítva is igaz. Ha a √2 tört volna, a jegyei ismétlődnének.

> megjegyzés: Visszafelé: `x = 0,3636…` esetén `100x - x = 36`, így `x = 36/99 = 4/11`.

### Feliratok
- maradék: maradék
- kezdet: kezdet
- osztás lépései: Az osztás lépései
- lehetséges maradékok: lehetséges maradékok:
- véges: A maradék 0 lett: véges tizedes tört.
- szakaszos: Visszajött egy maradék: innen minden ismétlődik.
- nem ismétlődik: – sosem ismétlődik (6. lépés)

### Adatok
- tört 1: 3/8
- tört 2: 1/7
- tört 3: 5/12
<!-- A √2 kiírt tizedesjegyeinek száma; a jegyeket a lecke pontos egész számolással (BigInt) állítja elő. -->
- √2 jegyei: 24

## 5. Vadásszunk törtet!
Keress törtet, amelynek a négyzete 2! `(p/q)^2 = 2` azt jelenti: `p^2 = 2q^2`. A legjobb párokra a különbség csak 1. ==De sosem 0 – legalábbis eddig.== Ez csak **sejtés**: végtelen sok törtet nem nézhetünk végig.

> megjegyzés: A `q√2` oldalú négyzet területe `2q^2`.

### Feliratok
- kérdés 5: Van olyan p/q, amelynek a négyzete 2?
- p csúszka: számláló (p)
- q csúszka: nevező (q)
- legjobb p gomb: Legjobb p ehhez a q-hoz
- mutasd gomb: Mutasd a legjobbakat
- négyzet p: p oldalú négyzet
- négyzet q: `q√2` oldalú négyzet
- látszat: A rajzon egyformák – a számok nem!
- találatok: Legközelebbi párok (eltérés ±1):
- még nincs: Állítsd be valamelyiket!
- sejtés: Eddig sosem lett 0. Ez sejtés, nem bizonyíték.
- kívül: kívül esik

### Adatok
- p kezdőérték: 7
- q kezdőérték: 5

## 6. Két négyzet, amely sosem egyforma
Tegyük fel, hogy `p^2 = 2q^2` (a legkisebb ilyen egészekkel). Akkor a két *q* oldalú négyzet együtt akkora, mint a *p* oldalú. Toljuk be őket két sarokba! A kétszer fedett rész annyi, mint a két üres sarok: ==kisebb egész megoldást kaptunk – ellentmondás.== A √2 tehát **irracionális**.

> megjegyzés: A „Csökkentés” ugyanezt teszi a 99/70 „majdnem-megoldással”.

### Feliratok
- biz cím: Bizonyítás (Tennenbaum)
- biz 1: Tegyük fel: van ilyen p és q egész – vegyük a legkisebbet!
- biz 2: `p^2 = 2q^2`
- biz 3: Két q oldalú négyzet = egy p oldalú. Ami kétszer fedett, annyi, mint ami üres:
- biz 4: `(2q - p)^2 = 2(p - q)^2`
- biz 5: Ez kisebb megoldás – pedig a legkisebbel kezdtünk. Ellentmondás!
- próba fej: Próba egy majdnem-megoldáson:
- lánc vége: Vége: a következő q már 0 lenne.
- csökkentés gomb: Csökkentés
- kezdés gomb: Vissza a kezdéshez

### Adatok
<!-- 99^2 = 9801, 2 · 70^2 = 9800. A lánc (p; q) → (2q − p; p − q): (99; 70) → (41; 29) → (17; 12) → (7; 5) → (3; 2) → (1; 1). -->
- majdnem-megoldás: 99; 70

## 7. A valós számok kitöltik az egyenest
Bármely két tört között van harmadik, mégis maradnak lyukak: a √2 helyén nincs tört, akármekkora nevezőt engedünk. ==A racionális és az irracionális számok együtt, a valós számok töltik ki a számegyenest.== Minden pontnak egy valós szám felel meg, és fordítva.

> megjegyzés: Irracionális például a √3, a √5 és a π is.

### Feliratok
- tévhit lyuk: „A törtek mindent kitöltenek – bármely kettő között van harmadik.”
- cáfolat lyuk: Sűrűn vannak, de a √2 helyén nincs tört.
- nevező csúszka: legnagyobb nevező
- ennyi tört: # tört van 1 és 2 között
- legközelebbi: legközelebbi tört:
- racionális: racionális (tört)
- racionális példák: `1/2; −3; 0,75; 0,(3)`
- irracionális: irracionális
- irracionális példák: `√2; √3; π`
- valós: valós számok
- valós példa: `RR` – a teljes egyenes

### Adatok
- nevező kezdőérték: 12

## 8. Az A4-es lap titka
Ha egy A4-es lapot félbehajtasz, A5-öt kapsz, és az **ugyanolyan alakú**. A hosszabb és a rövidebb oldal aránya legyen *r*; a fél lapé `2/r`. Ez csak akkor *r*, ha `r^2 = 2`. ==Az A4 297 mm × 210 mm, és 297 : 210 = 99 : 70== – ismerős?

> megjegyzés: Az A0 területe kb. 1 m²; minden hajtás felezi.

### Feliratok
- A4 név: A4
- A5 név: A5
- r csúszka: oldalarány (r)
- pontos gomb: Pontosan √2
- lap aránya: a lap aránya:
- fél aránya: a fél lap aránya:
- feltétel: `2/r = r <=> r^2 = 2`
- fedik: Pontosan fedik egymást!
- nem fedik: Nem fedik: más az alakja.
- sorozat fej: A-sorozat (mm):
- terület A0: az A0 területe:

### Adatok
<!-- ISO 216: A0 841 × 1189 mm (területe ≈ 1 m²); minden következő méret a hosszabb oldal felezésével,
     lefelé kerekítve (A1 594 × 841, A2 420 × 594, A3 297 × 420, A4 210 × 297, A5 148 × 210).
     A lecke az A4-et az A0-ból számolja, és eltérésnél hibasávot mutat. -->
- A0 rövid oldala: 841 mm
- A0 hosszú oldala: 1189 mm
- A4 rövid oldala: 210 mm
- A4 hosszú oldala: 297 mm
- A4 aránya: 99 : 70

## 9. Összefoglaló
- Az egységnégyzet átlója `√2`, mert `d^2 = 2`.
- A √2 körzővel pontosan a számegyenesre vihető.
- Tizedes alakja végtelen és nem szakaszos: csak közelítjük.
- Egy tört tizedes alakja véges vagy szakaszos.
- A √2 nem írható fel törtként – ezt bizonyítottuk.
- Racionális + irracionális = valós számok: kitöltik az egyenest.

### Feliratok
- össz 1 cím: Az átló
- össz 1: `d^2 = 1^2 + 1^2 = 2`, így `d = √2`
- össz 2 cím: Megszerkeszthető
- össz 2: körzővel a számegyenesre: `√2; √3; √5`
- össz 3 cím: Végtelen tizedes tört
- össz 3: `√2 = 1,41421356…` – csak közelítés
- össz 4 cím: Tört: véges vagy szakaszos
- össz 4: `1/7 = 0,(142857)`
- össz 5 cím: A √2 nem tört
- össz 5: `p^2 = 2q^2` nem lehet (Tennenbaum)
- össz 6 cím: Valós számok
- össz 6: racionális + irracionális = valós

<!-- Matematikai ellenőrzés (2026-11-23, Python 3, egész aritmetika: math.isqrt, fractions.Fraction):
  √2 = 1,41421356237309504880… (isqrt(2·10^40)); 1,414² = 1,999396; 1,415² = 2,002225; 1,41² = 1,9881;
  1,42² = 2,0164; 1,4142² = 1,99996164; 1,4143² = 2,00024449; 1,414213² = 1,999998409369;
  1,414214² = 2,000001237796.
  A q ≤ 100, p ≤ 150 párok közül pontosan ezekre |p² − 2q²| = 1: 1/1, 3/2, 7/5, 17/12, 41/29, 99/70
  (9801 − 9800 = 1); a különbség váltakozik: (2q − p)² − 2(p − q)² = −(p² − 2q²).
  1/7 = 0,(142857), maradékok 1, 3, 2, 6, 4, 5; 3/8 = 0,375; 5/12 = 0,41(6).
  Theodórosz-csiga: az n-edik átfogó √n (√4 = 2); a szögek összege √5-ig ≈ 136,9°.
  A4: 297/210 = 99/70 = 1,4142857…; ISO 216 méretek az A0-ból felezéssel (lásd fent); A0 területe 999 949 mm².
  Tennenbaum-bizonyítás: ha p² = 2q², akkor q < p < 2q, és (2q − p)² = 2(p − q)², ahol 0 < p − q < q –
  kisebb pozitív egész megoldás; végtelen csökkenés nincs a pozitív egészek között.
  Történeti megjegyzés (a leckében nem szerepel): Stanley Tennenbaum bizonyítása az 1950-es évekből való,
  J. H. Conway tette ismertté (ellenőrizendő). A √2 irracionalitásának felfedezését a hagyomány a
  püthagoreusokhoz köti – ez hagyomány, nem forrás. Theodórosz (Kr. e. 5. sz.) √17-ig igazolta
  az irracionalitást (Platón: Theaitétosz); a „csiga” elnevezés későbbi (ellenőrizendő). -->
