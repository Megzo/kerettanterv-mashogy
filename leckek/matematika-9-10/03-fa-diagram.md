# Hányféleképpen? – fa-diagram, szorzási elv, gráfok
tantárgy: Matematika · évfolyam: 9–10. · témakör: 3. Kombinatorika, gráfok

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/03-fa-diagram.md
  Feliratban a # jel helyére a lecke számot vagy szöveget ír (pl. „# öltözék” → „12 öltözék”).
  Az eredményeket (12, 24, 336, 56, 648, 328, 15, 132 …) a lecke maga is kiszámolja / megszámolja,
  és piros sávval jelez, ha a .md-ben írt érték nem egyezik.
  A vásznon kódban rögzített: a műveleti jelek és a számok a képletekben, a versenyzők sorszáma,
  a kézfogás-gráf csúcsainak betűi (A, B, C …), a Pascal-háromszög számai.
-->

## Közös

### Feliratok
- bizonyítás: bizonyítás

## 1. Hányféleképpen öltözhetsz fel?
Van 3 pólód, 2 nadrágod és 2 cipőd. Hány öltözéket állíthatsz össze? Sokan összeadnak: `3 + 2 + 2 = 7`. Nézd a **fa-diagramot**: minden pólóhoz mindkét nadrág, minden ilyen párhoz mindkét cipő jár. ==Egy öltözék = egy út a gyökértől egy levélig.== Számold meg a leveleket!

> megjegyzés: Kattints egy levélre: melyik öltözék az?

### Feliratok
- cím 1: Hány öltözéket állíthatsz össze?
- póló fej: póló
- nadrág fej: nadrág
- cipő fej: cipő
- póló 1: piros póló
- póló 2: zöld póló
- póló 3: sárga póló
- nadrág 1: farmer
- nadrág 2: rövidnadrág
- cipő 1: tornacipő
- cipő 2: csizma
- öltözék sablon: # öltözék
- tévhit összeadás: összeadás?
- helyes szorzás: szorzás
- kattints levélre: Kattints egy levélre!
- választott: a választott öltözék

### Adatok
- öltözékek száma: 12
<!-- 3 · 2 · 2 = 12; a lecke a fa leveleit is megszámolja. -->

## 2. A szorzási elv
Minden póló után **ugyanaz** a `2 * 2 = 4` ágú részfa nő ki – annyiszor, ahány póló van. ==Az utak száma a lépésenkénti lehetőségek szorzata:== ez a **szorzási elv**. Ismétlődéssel is igaz: négyjegyű PIN-kód {PIN-kódok száma} van, régi rendszám (ABC-123) {rendszámok száma}.

### Feliratok
- cím 2: Miért szorzás?
- a csúszka: póló
- b csúszka: nadrág
- c csúszka: cipő
- saját gomb: saját
- PIN gomb: PIN-kód
- rendszám gomb: rendszám
- döntés sablon: #. döntés
- részfa sablon: mindegyik után ugyanaz a # ágú részfa
- ág sablon: # ág
- út sablon: # út
- PIN magyarázat: 4 számjegy, mindegyik 10-féle (ismétlődhet)
- rendszám magyarázat: 3 betű (26-féle) és 3 számjegy (10-féle)
- köteg felirat: kötegben rajzolva

### Adatok
- PIN-kódok száma: 10 000
- rendszámok száma: 17 576 000
<!-- PIN: 10 · 10 · 10 · 10 = 10 000. Rendszám (régi magyar formátum, 3 betű + 3 számjegy): 26 · 26 · 26 · 10 · 10 · 10 = 17 576 000,
     ha minden betű (az angol ábécé 26 betűje) és számjegy megengedett. A valóságban nem minden kombinációt adtak ki
     (fenntartott betűcsoportok) – ez modellszámolás, nem a kiadott rendszámok száma. A lecke mindkettőt maga is kiszámolja. -->

## 3. Sorba rendezés: négy könyv a polcon
Négy könyvet teszel a polcra. Az első helyre 4 közül választhatsz, a másodikra már csak 3 maradt, aztán 2, végül 1. A fa szintenként ritkul: `4 * 3 * 2 * 1 = 24` sorrend. ==Ahány levél, annyi sorrend.== Ennek a szorzatnak neve is van: 4! („négy faktoriális”) – később tanulod.

> megjegyzés: Húzd a csúszkát: a polcon sorra kerül mind a {sorrendek száma} sorrend.

### Feliratok
- cím 3: Hányféle sorrendben állhat négy könyv?
- könyv 1: A
- könyv 2: B
- könyv 3: C
- könyv 4: D
- hely sablon: #. hely
- sorrend csúszka: sorrend
- sorrend sablon: #. sorrend a 24-ből

### Adatok
- sorrendek száma: 24

## 4. Dobogó: számít a sorrend
8 versenyző közül hányféle lehet a dobogó? Az arany 8 versenyzőé lehet, az ezüst a maradék 7-é, a bronz 6-é: `8 * 7 * 6 = 336`. Itt ==számít a sorrend==: ha Anna arany és Bence ezüst, az más dobogó, mint fordítva. A nagy fát kötegekben rajzoljuk.

> megjegyzés: Változtasd a versenyzők és a helyek számát!

### Feliratok
- cím 4: Hányféle lehet a dobogó?
- n csúszka: versenyzők száma
- k csúszka: díjazott helyek
- érem 1: arany
- érem 2: ezüst
- érem 3: bronz
- érem 4: 4. hely
- dobogó sablon: # dobogó
- példa felirat: egy lehetséges eredmény

### Adatok
- versenyzők: 8
- díjazott helyek: 3
- dobogók száma: 336
<!-- 8 · 7 · 6 = 336; a csúszkák kezdőértéke a versenyzők és a díjazott helyek száma. -->

## 5. Bizottság: nem számít a sorrend
Most 3 tagú bizottságot választunk, rangok nélkül. Négy emberből (A, B, C, D) `4 * 3 * 2 = 24` sorrendet kapunk, de az {A; B; C} csapat ebből 6-szor szerepel: ennyi a tagjainak sorrendje, `3 * 2 * 1 = 6`. ==Minden csapatot pontosan 6-szor számoltunk==, ezért osztunk: 8 főből `336 : 6 = 56` bizottság.

### Feliratok
- cím 5: Hány bizottság lehet?
- összevonás gomb: Összevonás
- szétbontás gomb: Szétbontás
- sorrend fej: sorrendek
- csapat fej: bizottságok
- hatszor sablon: # sorrendben
- bizonyítás szöveg: minden csapat ugyanannyiszor, 3 · 2 · 1 = 6-szor szerepel
- nyolc sablon: # főből:
- ember 1: A
- ember 2: B
- ember 3: C
- ember 4: D

### Adatok
- bizottság létszáma: 8
- bizottságok száma: 56
<!-- 8 · 7 · 6 / (3 · 2 · 1) = 56; 4 főből 4 · 3 · 2 / 6 = 4 bizottság (A, B, C, D közül mindig egy marad ki). -->

## 6. Háromjegyű számok: esetszétválasztás
Hány háromjegyű szám áll három különböző jegyből? Tévhit: `10 * 9 * 8 = 720` – de 0 nem állhat elöl! Elöl 9 jegy lehet, középen a maradék 9, a végén 8: `9 * 9 * 8 = 648`. Páros számnál a végén álló 0 mindent megváltoztat: ==két esetre bontunk==, és mivel kizárják egymást, **összeadjuk** őket.

> megjegyzés: Mindhárom gombot próbáld ki!

### Feliratok
- cím 6: Hány háromjegyű szám van?
- mód különböző: különböző
- mód tévhit: tévhit: 0 elöl
- mód páros: páros
- százas: százas
- tízes: tízes
- egyes: egyes
- lehetőség: lehetőség
- sorrend jel: #.
- eset 1: 1. eset: 0 a végén
- eset 2: 2. eset: 2, 4, 6 vagy 8 a végén
- nem háromjegyű: # – nem háromjegyű!
- nullás sablon: ebből 0-val kezdődik: #
- példa: példa:
- szám sablon: # szám
- rács felirat: egy négyzet = egy szám, sorban 000-tól 999-ig

### Adatok
- különböző jegyű: 648
- tévhit eredménye: 720
- páros különböző jegyű: 328
- 0 a végén: 72
- 2-4-6-8 a végén: 256
<!-- Pythonnal, 100–999 végigszámolva: 648 különböző jegyű; ebből 328 páros (72 végződik 0-ra: 9 · 8;
     256 végződik 2-re, 4-re, 6-ra vagy 8-ra: 4 · 8 · 8). 10 · 9 · 8 = 720 jegyhármasból 72 kezdődik 0-val: 720 − 72 = 648.
     A lecke mindet maga is megszámolja. -->

## 7. Kézfogások gráfja
Hat ember mind kezet fog egymással. A **gráf** **csúcsai** az emberek, **élei** a kézfogások. Az első 5 új kezet ráz, a második 4-et… `5 + 4 + 3 + 2 + 1 = 15`. Mindenki 5-ször fog kezet, de `6 * 5 = 30`-ban ==minden kézfogás kétszer szerepel==: `30 : 2 = 15`.

> megjegyzés: Bajnokságban a két irány két meccs (oda-vissza): 12 csapatnál {mérkőzések száma}.

### Feliratok
- cím 7: Hány kézfogás lesz?
- emberek csúszka: emberek száma
- kétszer gomb: kétszer
- egyszer gomb: egyszer
- bajnokság gomb: bajnokság
- kézfogás sablon: # kézfogás
- nyíl sablon: # nyíl
- mérkőzés sablon: # mérkőzés
- kétszer magyarázat: minden élen két nyíl: kétszer számoltuk
- bajnokság magyarázat: itt a két nyíl két különböző meccs
- új kézfogások: új kézfogások:

### Adatok
- emberek: 6
- kézfogások száma: 15
- csapatok: 12
- mérkőzések száma: 132
<!-- 6 · 5 / 2 = 15 = 5 + 4 + 3 + 2 + 1; 12 · 11 = 132 (minden csapat minden másikkal egyszer otthon, egyszer idegenben). -->

## 8. Hol a hiba?
Három megoldás, mindegyikben egy tipikus hiba. Keresd meg, mielőtt megnézed! Mindig kérdezd meg: ==számít-e a sorrend, ismétlődhet-e egy elem, és van-e tiltott eset== (például 0 elöl)? Ha mindent kétszer számoltál, oszd el 2-vel; a tiltott eseteket vond le.

> megjegyzés: Kattints a gombokra egyenként!

### Feliratok
- cím 8: Hol a hiba?
- hiba 1 gomb: 1. hiba
- hiba 2 gomb: 2. hiba
- hiba 3 gomb: 3. hiba
- feladat 1: 5 fős osztálybizottság elnököt és titkárt választ. Hányféleképpen?
- feladat 2: Hány háromjegyű szám írható a 0, 1, 2, 3 jegyekből, ha minden jegy különböző?
- feladat 3: 10 ember mindegyike kezet fog a többivel. Hány kézfogás lesz?
- rossz 1: `5 * 4 : 2 = 10`
- rossz 2: `4 * 3 * 2 = 24`
- rossz 3: `10 * 9 = 90`
- jó 1: `5 * 4 = 20`
- jó 2: `3 * 3 * 2 = 18`
- jó 3: `10 * 9 : 2 = 45`
- ok 1: Az elnök és a titkár más szerep: itt számít a sorrend.
- ok 2: Elöl nem állhat 0: az első helyre csak 3 jegy jut.
- ok 3: Így minden kézfogást kétszer számoltunk.
- megoldás: megoldás:
- javítás: javítás:

### Adatok
- jó eredmény 1: 20
- jó eredmény 2: 18
- jó eredmény 3: 45
<!-- 1: 5 · 4 = 20 rendezett (elnök, titkár) pár. 2: elöl 1, 2 vagy 3 → 3, középen a maradék 3 (a 0 is), a végén 2 → 18
     (Pythonnal végigszámolva). 3: 10 · 9 / 2 = 45. A lecke mindhármat végigszámolással ellenőrzi. -->

## 9. Összefoglaló
- **Szorzási elv:** egymás utáni döntéseknél a lehetőségek száma szorzódik.
- **Számít a sorrend:** `8 * 7 * 6 = 336` dobogó.
- **Nem számít:** osztunk a sorrendek számával: `336 : 6 = 56` bizottság.
- **Esetszétválasztás:** a kizáró esetek összeadódnak.

==A kiválasztások száma mind ott van a Pascal-háromszögben.== Ötöslottó (5 szám 90-ből): {lottószelvények} szelvény.

> megjegyzés: Kitekintés: minden szám a fölötte lévő kettő összege.

### Feliratok
- cím 9: Hogyan számoljunk?
- ö szorzás: szorzási elv
- ö szorzás h: póló · nadrág · cipő: 3 · 2 · 2 = 12
- ö sorrend: számít a sorrend
- ö sorrend h: dobogó: 8 · 7 · 6 = 336
- ö kiválasztás: nem számít a sorrend
- ö kiválasztás h: bizottság: 336 : 6 = 56
- ö eset: esetszétválasztás
- ö eset h: páros: 72 + 256 = 328
- ö gráf: gráf: élek száma
- ö gráf h: kézfogás: 6 · 5 : 2 = 15
- pascal fej: Pascal-háromszög
- pascal kézfogás: kézfogás
- pascal bizottság: bizottság
- lottó felirat: ötöslottó:
- lottó képlet: [[90 · 89 · 88 · 87 · 86 / 5 · 4 · 3 · 2 · 1]]
- szelvény sablon: = # szelvény

### Adatok
- lottószelvények: 43 949 268
<!-- 90 · 89 · 88 · 87 · 86 / (5 · 4 · 3 · 2 · 1) = 5 273 912 160 / 120 = 43 949 268 (Pythonnal: math.comb(90, 5)).
     A Pascal-háromszög n. sorának k. eleme az n elemből k elemű kiválasztások száma: a 6. sor 2. eleme 15,
     a 8. sor 3. eleme 56 (a sorokat és az elemeket 0-tól számozzuk). -->

<!-- Matematikai ellenőrzés (2026-11-24, Pythonnal: itertools.permutations / combinations, math.comb, math.perm,
     a háromjegyű számoknál 100–999 végigszámolva):
  - öltözék: 3 · 2 · 2 = 12; 3 + 2 + 2 = 7 (tévhit).
  - PIN: 10⁴ = 10 000; régi rendszám-modell: 26³ · 10³ = 17 576 000.
  - 4 könyv: 4 · 3 · 2 · 1 = 24 (permutations('ABCD') = 24).
  - dobogó: 8 · 7 · 6 = 336 = perm(8, 3); bizottság: comb(8, 3) = 56 = 336 / 6; 4 főből 3: 24 sorrend, 4 csapat.
  - különböző jegyű háromjegyű szám: 648 = 9 · 9 · 8; páros: 328 = 72 + 256; 10 · 9 · 8 = 720, ebből 72 kezdődik 0-val.
  - kézfogás 6 főből: 15 = comb(6, 2) = 5 + 4 + 3 + 2 + 1; 12 csapat oda-vissza: 132 = 12 · 11.
  - hibák: perm(5, 2) = 20 (comb(5, 2) = 10 a hibás); 0, 1, 2, 3 jegyekből különböző jegyű háromjegyű: 18 (24 a hibás);
    10 ember kézfogása: comb(10, 2) = 45 (90 a hibás).
  - ötöslottó: comb(90, 5) = 43 949 268.
  - Pascal-háromszög 8. sora: 1, 8, 28, 56, 70, 56, 28, 8, 1.
  A faktoriális (n!) és a C(n; k) jelölés a 11–12. évfolyam anyaga: a lecke csak említi, szorzatként számol.
  Az öltözékek, a könyvek, a versenyzők és a bizottság kitalált példák. -->
