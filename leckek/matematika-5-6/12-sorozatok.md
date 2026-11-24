# Hány gyufa kell a 100. házhoz? – sorozatok és szabályok
tantárgy: Matematika · évfolyam: 5–6. · témakör: 12. Sorozatok (+ 11. A függvény fogalmának előkészítése)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/12-sorozatok.md
  Feliratban a # jel helyére a lecke számot ír (pl. „# ház” → „3 ház”).
  A számsorozatokat pontosvesszővel írjuk (1; 2; 4), mert a vessző tizedesvessző.
  Az eredményeket (gyufaszálak, pöttyök, a Gauss-összeg) a lecke a rajzból maga számolja ki, és piros
  sávval jelez, ha az Adatok alatt írt érték nem egyezik vele. A panelszöveg számait (6, 11, 16, 501…)
  kézzel írtuk: ha egy adatot átírsz, a szöveget is igazítsd.
-->

## Közös

### Feliratok
- tippelj: Tippelj előbb!
- a tipped: a te tipped: #
- házak: házak
- szálak: szálak
- ház sor: # ház
- szál: # szál

### Adatok
- gyufaszálak: 1: 6 · 2: 11 · 3: 16 · 4: 21 · 25: 126 · 100: 501
<!-- házak száma: gyufaszálak száma. A lecke a rajzolt házsorban megszámolja a szálakat (1 ház = 4 fal
     + 2 tetőszál = 6; a szomszédos házak egy falat közösen használnak, ezért minden új ház +5), és összeveti.
     Az első három pár az 1. lépés kész sorai, a 4. pár a kérdés. Az utolsó két pár a 3. lépés csapdája:
     a nagyobb házszám a kisebbik pontosan négyszerese legyen (25 → 100). -->
- négyszeres tipp: 504
<!-- 4 · 126 = 504 – a „×4 csapda” rossz eredménye; a lecke kiszámolja és összeveti. -->

## 1. Mi jön ezután?
Gyufából házsort rakunk. Egy ház **6** szál, két ház **11**, három ház **16**. Hány szál kell négy házhoz? ==Tippelj előbb!== Aztán nézd, ahogy felépül, és számold a szálakat!

> megjegyzés: Kérdezd meg: ki hogyan számolt?

### Feliratok
- kérdés 1: Hány szál kell # házhoz?
- tipp gomb: # szál
- magyarázat jó: Ügyes! Minden új ház +5 szál.
- magyarázat kevés: Kimaradt a bal szélső fal.
- magyarázat sok: A közös falakat kétszer számoltad!
- végeredmény: # ház: # szál

## 2. Mennyivel nő? – egyforma lépcsők
Írjuk táblázatba! Minden új ház **5** szállal több: alul és fölül egy-egy szál, egy fal és két tetőszál. A bal szélső fal csak egyszer kell. Oszlopba rakva ==egyforma lépcsők== jönnek. Ha egy sorozat mindig ugyanannyival nő, a neve **számtani sorozat**.

### Feliratok
- plusz öt: +5
- jelmagyarázat fal: bal szélső fal: 1 szál
- jelmagyarázat ház: minden új ház: 5 szál
- lépcső felirat: mindig +5: egyforma lépcsők
- csúszka 2: házak száma

## 3. A 100. ház – szabály és csapda
Nem kell megépíteni! A bal szélső fal 1 szál, utána minden ház 5. Tehát *n* házhoz `5 · n + 1` szál kell, 100 házhoz 501. ==Csapda:== 25 ház 126 szál, de 100 ház nem `4 · 126 = 504`! Miért? Nyomd meg a gombot!

### Feliratok
- szabály: `n` ház → `5 · n + 1` szál
- megszámolva: megszámolva: # szál
- csúszka 3: házak száma
- gomb csapda: ×4 csapda
- gomb sor: Vissza a házsorhoz
- negyed sor: # ház: # szál
- dupla fal: dupla fal
- csapda kérdés: Négy 25-ös sor: 4 · 126 = 504?
- csapda válasz: Összetolva 3 fal kétszer szerepel!

## 4. Pontok egy egyenesen – mégsem arányos
Tegyük a számpárokat a koordináta-rendszerbe! A pontok ==egy egyenesre esnek==, és lépcsőt rajzolnak: jobbra 1, fel 5. Mégsem egyenes arányosság! Az egyenes nem az origón megy át: 0 háznál 1-et mutat. Ez a bal szélső fal.

> megjegyzés: Nyomd meg: hol lenne az arányos?

### Feliratok
- lépcső jobbra: 1 ház
- lépcső fel: +5 szál
- első fal: 0 ház → 1 szál: a bal szélső fal
- arányos: `5 · n`: ez lenne arányos
- egyenes 4: `5 · n + 1`
- gomb arányos: Arányos lenne?
- csúszka 4: házak száma

## 5. Egy kezdet, két szabály
{kezdet} – mi jön ezután? ==Tippelj előbb!== Aztán nézd meg, hogyan folytatja a gép két különböző szabállyal. **Melyik a jó?** Néhány tagból nem mindig dől el, hogyan megy tovább egy sorozat. Ezért a feladatnak a **szabályt** is meg kell adnia.

### Feliratok
- kérdés 5: Mi jön ezután?
- tipp más: Más szám is lehet
- szabály duplázás: mindig duplázunk
- szabály növekmény: egyre többel nő
- két szabály: Mindkét szabály illik a kezdethez!
- a tipped jó: A tipped jó – de nem az egyetlen!

### Adatok
- kezdet: 1; 2; 4
- duplázva: 8; 16; 32
- egyre többel: 7; 11; 16
<!-- Duplázás: minden tag az előző kétszerese (1; 2; 4; 8; 16; 32).
     „Egyre többel”: a növekmény 1, 2, 3, 4, 5 (1; 2; 4; 7; 11; 16).
     A lecke mindkét folytatást a kezdetből számolja, és összeveti az itt írtakkal. -->

## 6. Háromszögszámok
Pöttyökből háromszögeket rakunk: 1; 3; 6; 10; 15 pötty. Minden új sor eggyel hosszabb az előzőnél, ezért a növekmény 2, 3, 4, 5. ==A lépcsők egyre magasabbak==, ez nem számtani sorozat. Ezek a **háromszögszámok**.

> megjegyzés: Húzd a csúszkát! Mennyi a 10. háromszögszám?

### Feliratok
- háromszög cím: háromszögszámok
- növekmény: növekmény:
- csúszka 6: sorok száma
- sor hossza: #
- n-edik háromszögszám: a #. háromszögszám

### Adatok
- háromszögszámok: 1: 1 · 2: 3 · 3: 6 · 4: 10 · 5: 15
<!-- sorszám: pöttyök száma. A lecke a kirajzolt pöttyöket számolja meg, és összeveti. -->

## 7. Négyzetszámok
Négyzetbe is rakhatunk pöttyöket: 1; 4; 9; 16; 25. Minden új szegély egy **L** alak: 3, 5, 7, 9 pötty – a páratlan számok! ==Az első *n* páratlan szám összege `n · n`.== Vágd ketté a négyzetet: két szomszédos háromszögszám lesz belőle!

### Feliratok
- négyzet cím: négyzetszámok
- csúszka 7: oldal hossza
- gomb ketté: Vágd ketté!
- gomb egész: Rakd össze!

### Adatok
- négyzetszámok: 1: 1 · 2: 4 · 3: 9 · 4: 16 · 5: 25
<!-- oldalhossz: pöttyök száma (n · n). A lecke a kirajzolt pöttyöket számolja meg, és összeveti.
     Ketté vágva: n · n = (1 + 2 + … + n) + (1 + 2 + … + (n − 1)), pl. 16 = 10 + 6. -->

## 8. Gauss trükkje: 1 + 2 + … + 100
A hagyomány szerint a kisiskolás Gauss pillanatok alatt összeadta a számokat 1-től 100-ig. A trükk: a lépcső mellé tegyünk egy fordított lépcsőt! Együtt téglalapot adnak: `100 · 101`. ==A lépcső ennek a fele: 5050.== Ez a 100. háromszögszám.

> megjegyzés: Párokban: `1 + 100 = 2 + 99 = … = 101`.

### Feliratok
- gauss kérdés: 1 + 2 + … + # = ?
- gauss oszlop: minden oszlop: # magas
- gauss téglalap: téglalap: # · # = #
- gauss fele: a lépcső a fele: # : 2 = #
- csúszka 8: meddig adjuk össze?
- gomb forgasd: Forgasd rá!
- gauss legenda: hagyomány

### Adatok
- Gauss-összegek: 10: 55 · 100: 5050
<!-- utolsó összeadandó: az összeg (1 + 2 + … + n). A lecke a csúszkát az első n-nel indítja, és mindkét
     összeget kiszámolja (a lépcső kockáinak száma = a téglalap fele) és összeveti.
     A Gauss-anekdota forrása: W. Sartorius von Waltershausen, „Gauss zum Gedächtniss” (1856). A történet
     hagyomány: az eredeti feladat számai nem ismertek biztosan (az 1–100 a későbbi, népszerű változat),
     ezért a vásznon „hagyomány” bélyeg áll. -->

## 9. Összefoglalás
- A **sorozat** tagjai egy **szabály** szerint követik egymást.
- Ha mindig ugyanannyival nő: egyforma lépcsők, a pontok egy egyenesen.
- A tagot a sorszámból is kiszámolhatod: `5 · n + 1`.
- ==Néhány tagból többféle szabály is kijöhet.==
- Háromszög- és négyzetszámok: egyre nagyobb lépcsők.

### Feliratok
- össz 1: szabály: `5 · n + 1`
- össz 2: két szabály, két folytatás
- össz 3: pöttyminták
- össz 4: Gauss: lépcső + lépcső = téglalap

<!-- Tanári megjegyzések:
  - A gyufaházas feladat (házsor, közös falak) klasszikus tankönyvi minta; a ház 4 fal + 2 tetőszál.
  - „Számtani sorozat”: a kerettanterv 5–6. fogalmai közt csak a sorozat, számsorozat, szabály szerepel;
    a lecke a nevet csak megemlíti (a 9–10. évfolyamon lesz tananyag).
  - A 4. lépés szaggatott egyenese csak azt mutatja, hogy a pontok egy egyenesre esnek; a pontokat nem
    kötjük össze, mert fél ház nincs.
  - A számsorozatokat pontosvesszővel írjuk (1; 2; 4), mert a vessző tizedesvessző; a tankönyvek egy része
    vesszőt használ.
  - Az 5. lépés két szabálya a kerettanterv „A tanár által megkezdett sorozat minél több szabályának
    gyűjtése” tevékenységéhez kapcsolódik: érdemes az osztállyal további szabályokat keresni
    (pl. 1; 2; 4; 1; 2; 4 – ismétlődés).
  - A Gauss-történet hagyomány (lásd a 8. lépés adatai alatti megjegyzést).
-->
