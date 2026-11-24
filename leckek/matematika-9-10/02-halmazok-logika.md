# „Ha…, akkor…” – halmazok, logikai szita és a logika nyelve
tantárgy: Matematika · évfolyam: 9–10. · témakör: 1. Halmazok (+ 2. Matematikai logika)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/02-halmazok-logika.md
  Feliratban a # jel helyére a lecke számot vagy szöveget ír (pl. „# szám” → „16 szám”).
  A tulajdonságok (2-vel osztható, prím…) SZÖVEGE itt átírható, a JELENTÉSÜK (melyik szám prím) a kódban van.
  Az elemszámokat a lecke maga is megszámolja, és piros sávval jelez, ha a .md-ben írt érték nem egyezik.
  A halmazbetűk (A, B, C, H, F) és a táblázat oszlopainak műveleti jelei a vásznon kódban rögzítettek.
  Jelölés (tankönyvenként eltér): metszet ∩, unió ∪, különbség ∖, komplementer Ā, részhalmaz ⊆;
  az igazságtáblában i = igaz, h = hamis.
-->

## Közös

### Feliratok
- igaz jel: i
- hamis jel: h
- A név: 2-vel osztható
- B név: 3-mal osztható
- C név: 5-tel osztható
- A rövid: 2-vel
- B rövid: 3-mal
- C rövid: 5-tel
- igen: igen
- nem: nem
- szám sablon: # szám
- darab fej: db
- bizonyítás: bizonyítás
- alaphalmaz felirat: alaphalmaz: 1, 2, 3, …, 100

### Adatok
- alaphalmaz: 1–100
- A elemszáma: 50
- B elemszáma: 33
- C elemszáma: 20
- A és B elemszáma: 16
- A és C elemszáma: 10
- B és C elemszáma: 6
- mindhárom elemszáma: 3
- unió elemszáma: 74
- egyik sem elemszáma: 26
<!-- 1-től 100-ig: 2-vel osztható 50, 3-mal 33, 5-tel 20; 6-tal 16, 10-zel 10, 15-tel 6, 30-cal 3.
     Unió: 50 + 33 + 20 − 16 − 10 − 6 + 3 = 74; egyikkel sem osztható: 100 − 74 = 26.
     A nyolc tartomány: csak 2-vel 27, csak 3-mal 14, csak 5-tel 7, 2-vel és 3-mal (5-tel nem) 13,
     2-vel és 5-tel (3-mal nem) 7, 3-mal és 5-tel (2-vel nem) 3, mindhárommal 3, egyikkel sem 26 (összesen 100).
     Pythonnal ellenőrizve, 2026-11-24. -->

## 1. Száz szám, három kérdés
1-től 100-ig minden számról három kérdést teszünk fel: osztható-e 2-vel, 3-mal, 5-tel? A három halmaz a téglalapot **8 tartományra** bontja. ==Minden szám pontosan egy tartományba kerül==, ezért a nyolc számláló összege 100. Ez **osztályozás**: diszjunkt részhalmazokra bontás.

> megjegyzés: Kattints egy tartományra vagy egy számra a rácson!

### Feliratok
- cím 1: Hová kerül a 100 szám?
- kattints 1: Kattints egy tartományra vagy egy számra!
- összesen sablon: összesen: # szám

## 2. „És” = metszet, „vagy” = unió
Most csak A-t és B-t nézzük. A **metszet** (`A ∩ B`) elemeire igaz: „A **és** B”. Az **unió** (`A ∪ B`) elemeire: „A **vagy** B”. ==Az igazságtábla minden sora egy tartomány a Venn-diagramon.== Tévhit: a „vagy” kizáró. A matekban megengedő; a kizárót így mondjuk: „vagy…, vagy…”.

> megjegyzés: Kattints a táblázat egy sorára vagy egy tartományra!

### Feliratok
- cím 2: Mikor igaz az állítás?
- és sablon: # és #
- vagy sablon: # vagy #
- kizáró sablon: vagy #, vagy #
- és gomb: és
- vagy gomb: vagy
- kizáró gomb: vagy…, vagy…
- és fej: A és B
- vagy fej: A vagy B
- kizáró fej: vagy A, vagy B
- metszet képlet: `A ∩ B` – metszet
- unió képlet: `A ∪ B` – unió
- kizáró képlet: `(A ∪ B) ∖ (A ∩ B)`

## 3. Mi a tagadása?
Mi a tagadása: „páros **és** osztható 3-mal”? Tévhit: „nem páros **és** nem osztható 3-mal”. A {példaszám} cáfolja: rá az eredeti és ez is hamis. ==Egy állítás és a tagadása közül pontosan az egyik igaz.== A helyes tagadás: „nem páros **vagy** nem osztható 3-mal”.

> megjegyzés: Fordítva is igaz: „nem (A vagy B)” = „nem A és nem B”.

### Feliratok
- cím 3: Mi a tagadása?
- tagadás fej: nem (A és B)
- tévhit fej: nem A és nem B
- helyes fej: nem A vagy nem B
- tévhit gomb: nem A és nem B
- helyes gomb: nem A vagy nem B
- egyenlő: ugyanaz a tartomány
- nem egyenlő: más tartomány
- példa eredeti: # páros és osztható 3-mal.
- példa tévhit: # nem páros és nem osztható 3-mal.
- példa helyes: # nem páros vagy nem osztható 3-mal.
- mindkettő hamis: mindkettő hamis – ez nem a tagadása!
- pontosan egy: pontosan az egyik igaz – ez a tagadása

### Adatok
- példaszám: 4
<!-- A 4 páros, de 3-mal nem osztható. „A 4 páros és osztható 3-mal” hamis; „a 4 nem páros és nem osztható 3-mal”
     is hamis (mert páros) → a kettő nem lehet egymás tagadása. „A 4 nem páros vagy nem osztható 3-mal” igaz.
     Ha átírod, olyan szám kell, amely pontosan az egyik feltételnek felel meg (pl. 2, 3, 8, 9) – a lecke szól, ha nem.
     A feliratokban a # helyére „A 4” / „a 4” (ill. „Az 5”, „az 50”…) kerül; a névelőt a lecke választja. -->

## 4. A logikai szita
Tévhit: az unió elemszáma a három elemszám összege. De {A elemszáma} + {B elemszáma} + {C elemszáma} több, mint 100! A metszeteket többször számoltuk. Vonjuk le a páronkénti metszeteket, majd adjuk vissza a hármasat: ez a **logikai szita**. ==Minden tartomány pontosan egyszer számít.==

> megjegyzés: Kimarad az 1, a 7 és 97 közötti 22 prím, meg a 49, 77, 91 – Eratoszthenész szitája.

### Feliratok
- cím 4: Hány szám osztható 2-vel, 3-mal vagy 5-tel?
- tovább gomb: Következő tag →
- újra gomb: Szita elölről
- száz vonal: összesen 100 szám
- túl sok: Több, mint 100! A metszeteket többször számoltuk.
- túl kevés: A közepét most egyszer sem számoltuk.
- pont jó: Minden tartomány pontosan egyszer számít.
- unió oszlop: unió
- 1 halmazban: 1 halmazban: `1`
- 2 halmazban: 2 halmazban: `2 - 1 = 1`
- 3 halmazban: 3 halmazban: `3 - 3 + 1 = 1`
- kimaradt: Egyikkel sem osztható:

## 5. „Ha…, akkor…” = részhalmaz
„Ha egy szám osztható 4-gyel, akkor páros.” Azaz: A **részhalmaza** B-nek (`A ⊆ B`). Csak akkor hamis, ha van **ellenpélda**: A-beli, de nem B-beli elem. ==A „ha…, akkor…” csak az (i; h) sorban hamis.==

> megjegyzés: Nyomd meg a Megfordítás gombot is!

### Feliratok
- cím 5: Mikor igaz a „ha…, akkor…”?
- ha sablon: Ha egy szám #, akkor #.
- osztható 4-gyel: osztható 4-gyel
- páros: páros
- osztható 6-tal: osztható 6-tal
- osztható 3-mal: osztható 3-mal
- 5-re végződik: 5-re végződik
- osztható 5-tel: osztható 5-tel
- prím: prím
- páratlan: páratlan
- négyzetszám: négyzetszám
- A csúszka: A tulajdonság
- B csúszka: B tulajdonság
- megfordítás gomb: Megfordítás ⇄
- ha fej: ha A, akkor B
- igaz részhalmaz: igaz: `A ⊆ B`
- hamis ellenpélda: hamis – ellenpélda: #
- ellenpélda felirat: ellenpélda

### Adatok
- ellenpélda: 6
<!-- A megfordítás („Ha egy szám páros, akkor osztható 4-gyel.”) ellenpéldája; minden páros, 4-gyel nem osztható szám
     jó (2, 6, 10…). A lecke ezt mutatja, ha valóban ellenpélda; más tulajdonságpárnál a legkisebbet. -->

## 6. Igaz-e a megfordítás?
„Ha `x > 3`, akkor `x^2 > 9`” igaz: a piros félegyenes a kék halmazon belül van. A **megfordítás**: „ha `x^2 > 9`, akkor `x > 3`” – hamis, ellenpélda: {ellenpélda x}. Tévhit: ha egy állítás igaz, a megfordítása is az. ==Ha mindkét irány igaz, ezt mondjuk: **akkor és csak akkor**.==

> megjegyzés: Húzd az x-et! Próbáld ki az `x^3 > 27` feltételt is.

### Feliratok
- cím 6: Igaz-e a megfordítás?
- A képlet: `x > 3`
- B képlet 1: `x^2 > 9`
- B képlet 2: `x^3 > 27`
- állítás sablon: Ha #, akkor #.
- állítás: állítás
- megfordítás: megfordítás
- mindig igaz: igaz minden x-re
- hamis itt: hamis – ellenpélda: `x = #`
- ekvivalencia: akkor és csak akkor: `x > 3 <=> x^3 > 27`
- x csúszka: x értéke
- csere gomb: x² > 9 ↔ x³ > 27
- megfordítás fej: ha B, akkor A
- húzd: húzd az x-et!
- x most: `x = #`

### Adatok
- ellenpélda x: −4
<!-- (−4)² = 16 > 9, de −4 nem nagyobb 3-nál. Minden x < −3 ellenpélda. Az x³ > 27 ⇔ x > 3, mert az x³ szigorúan nő.
     A 3-as küszöb és a két feltétel a kódban van; az ellenpéldát a lecke ellenőrzi. -->

## 7. „Minden” és „van olyan”
„Minden hattyú fehér” – Európában sokáig így hitték, aztán Ausztráliában **fekete hattyút** találtak. ==Egyetlen ellenpélda cáfolja a „minden”-t.== A tagadás: „**van olyan** hattyú, amely nem fehér”. Tévhit: „minden hattyú fekete”. Ez is hamis lehet az eredetivel együtt, ezért nem tagadás.

### Feliratok
- cím 7: Minden hattyú fehér?
- hattyúk: H: hattyúk
- fehér: F: fehér dolgok
- fekete gomb: Fekete hattyú (Ausztrália)
- állítás 1 gomb: „Minden hattyú fehér.”
- állítás 2 gomb: „Van fekete hattyú.”
- á1: Minden hattyú fehér.
- á1 tévhit: Minden hattyú fekete.
- á1 tagadás: Van olyan hattyú, amely nem fehér.
- á2: Van olyan hattyú, amely fekete.
- á2 tévhit: Van olyan hattyú, amely nem fekete.
- á2 tagadás: Egyik hattyú sem fekete.
- állítás címke: állítás
- tévhit címke: tévhit
- tagadás címke: tagadás
- egyik sem igaz: mindkettő hamis – nem tagadás!
- mindkettő igaz: mindkettő igaz – nem tagadás!
- jó tagadás: pontosan az egyik igaz
- szabály 1: „minden … igaz” tagadása: „van olyan, amelyre nem igaz”
- szabály 2: „van olyan, amelyre igaz” tagadása: „egyikre sem igaz”
- fekete hattyú: fekete hattyú
<!-- A fekete hattyú (Cygnus atratus) Ausztrália őshonos madara; európai utazók a 17. század végén írták le
     (Willem de Vlamingh, 1697 – ellenőrizendő). A „fekete hattyú” a logikában és a tudományfilozófiában a cáfoló
     ellenpélda klasszikus példája. A rajz stilizált illusztráció. -->

## 8. A végtelen szálloda
Hilbert szállodájában végtelen sok szoba van, mind foglalt. Új vendég jön? Mindenki átköltözik a következő szobába. Végtelen busz jön? Az n-es szoba lakója a `2n`-esbe költözik: minden páratlan szoba felszabadul. Tévhit: páros szám „feleannyi van”. ==A páros számok párba állíthatók a pozitív egészekkel: ugyanannyian vannak.==

> megjegyzés: A szálloda David Hilbert egyik 1924-es előadásából ered.

### Feliratok
- cím 8: A végtelen szálloda
- megtelt: minden szoba foglalt
- egy gomb: Jön 1 új vendég
- busz gomb: Jön egy végtelen busz
- egy szabály: `n -> n + 1`
- busz szabály: `n -> 2n`
- régi sor: régi szoba
- új sor: új szoba
- párba: Minden n-nek pontosan egy párja van: ugyanannyian vannak.
- új vendég: új vendég
- busz: végtelen busz
- szabad: szabad!
- válassz: Ki költözik hová? Nyomd meg a gombot!
<!-- A „Grand Hotel” gondolatkísérletet Hilbert 1924–25-ös téli előadásaihoz kötik (az előadásjegyzetek később jelentek
     meg); George Gamow „Egy, kettő, három… végtelen” (1947) című könyve tette közismertté – ellenőrizendő. -->

## 9. Összefoglalás
- „és” = **metszet**, „vagy” = **unió**, „nem” = **komplementer**.
- „Ha A, akkor B” = `A ⊆ B`; a **megfordítást** külön kell vizsgálni.
- A „minden” tagadása: „**van olyan**, amelyre nem”.
- **Logikai szita:** minden tartomány pontosan egyszer számít.
- ==Végtelen halmazoknál párba állítással hasonlítunk.==

### Feliratok
- cím 9: A logika nyelve = halmazok nyelve
- ö és: „A és B”
- ö és h: `A ∩ B` – metszet
- ö vagy: „A vagy B”
- ö vagy h: `A ∪ B` – unió
- ö kizáró: „vagy A, vagy B”
- ö kizáró h: `(A ∪ B) ∖ (A ∩ B)`
- ö nem: „nem A”
- ö nem h: `Ā` – komplementer
- ö ha: „ha A, akkor B”
- ö ha h: `A ⊆ B` – részhalmaz
- ö akkor: „A akkor és csak akkor, ha B”
- ö akkor h: `A = B`
- ö szita: `|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|`
- logika fej: logika
- halmaz fej: halmazok
- szita fej: logikai szita
- ö végtelen: végtelen halmazok: „ugyanannyi”
- ö végtelen h: párba állítás, pl. `n ↔ 2n`

<!-- Matematikai ellenőrzés (2026-11-24, Pythonnal):
  - 1–100: |A| = 50, |B| = 33, |C| = 20, |A ∩ B| = 16, |A ∩ C| = 10, |B ∩ C| = 6, |A ∩ B ∩ C| = 3, |A ∪ B ∪ C| = 74,
    egyikkel sem osztható 26: 1; 7; 11; 13; 17; 19; 23; 29; 31; 37; 41; 43; 47; 49; 53; 59; 61; 67; 71; 73; 77; 79; 83;
    89; 91; 97 (az 1, 22 prím 7 és 97 között, valamint 49 = 7 · 7, 77 = 7 · 11, 91 = 7 · 13). A lecke mindet maga is
    megszámolja.
  - 2. lépés (A: 2-vel, B: 3-mal osztható): |A ∩ B| = 16, |A ∪ B| = 67, kizáró vagy 51; a sorok elemszáma
    (i; i) 16, (i; h) 34, (h; i) 17, (h; h) 33.
  - Szita-bizonyítás: a pontosan k halmazban lévő szám a képletben k − C(k; 2) + C(k; 3) = 1-szer számít (k = 1, 2, 3).
  - De Morgan: nem (A és B) = nem A vagy nem B; nem (A vagy B) = nem A és nem B (mind a négy sorban ellenőrizve).
  - „Ha A, akkor B” logikai értéke hamis ⇔ A igaz és B hamis; a „minden A-beli elem B-beli” állítás ⇔ A ⊆ B.
    4-gyel osztható ⇒ páros igaz, megfordítása hamis (ellenpélda 2, 6, 10…); prím ⇒ páratlan hamis (ellenpélda 2);
    5-re végződik ⇒ osztható 5-tel igaz, megfordítása hamis (10).
  - x > 3 ⇒ x² > 9 igaz (x > 3 ≥ 0 ⇒ x² > 9); megfordítása hamis (x = −4: 16 > 9); x > 3 ⇔ x³ > 27.
  - Végtelen szálloda: n ↦ n + 1 és n ↦ 2n kölcsönösen egyértelmű (injektív) hozzárendelés; az n ↦ 2n a pozitív
    egészeket a pozitív párosokra képezi le, kölcsönösen egyértelműen.
  Tankönyvi jelölés: a részhalmaz jele több tankönyvben ⊂ (a ⊆ helyett), a komplementeré A′ vagy A̅; a tanár
  igazítsa a saját tankönyvéhez (a feliratok itt átírhatók). -->
