# Mit tud a véletlen? – valószínűség, szimuláció, meglepetések
tantárgy: Matematika · évfolyam: 9–10. · témakör: 17. Valószínűség-számítás

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/15-valoszinuseg.md
  Feliratban a # jel helyére a lecke számot vagy szöveget ír (pl. „# kedvező eset” → „11 kedvező eset”).
  A kísérletek a gépen „dobódnak”: rögzített kezdőértékből (seed) számolt álvéletlen sorozat, ezért
  minden megnyitáskor ugyanaz jön ki; az „új sorozat” gomb új sorozatot kér.
  Az eredményeket (11/36, 7/16, 253, 50,7 %, 27 Ft …) a lecke maga is kiszámolja, és piros sávval
  jelez, ha az itt írt érték nem egyezik.
  Az eseménykártyák SZÖVEGE átírható, de hogy melyik mező kedvező, azt a kód dönti el
  (pl. „van hatos” = legalább az egyik kocka 6). Ha egy esemény értelmét változtatod, szólj a fejlesztőnek.
  A vásznon kódban rögzített: a tengelyszámok, a képletek számai, az ajtók és a rulettmezők számai.
  Az 5–6. évfolyam „18-valoszinuseg” leckéje (biztos / lehetetlen, ágrajz, két kocka összege, relatív
  gyakoriság, „jár már az írás?”) az előzmény; ez a lecke arra épít, nem ismétli.
-->

## Közös

### Feliratok
- bizonyítás: bizonyítás
- mérés: mérés
- modell: modell
- kitekintés: kitekintés
- plusz 10: +10
- plusz 100: +100
- plusz 1000: +1000
- új sorozat: új sorozat
- dobások sablon: # dobás

## 1. Klasszikus valószínűség
Két kockával dobunk. Az **eseménytér** (Ω) mind a {összes eset} lehetséges kimenetel: ezek az **elemi események**. Egy **esemény** ezek egy része, pl. „van hatos”. Ha az elemi események egyformán valószínűek: ==`P(A) =` kedvező esetek : összes eset.== Az **ellentett** esemény (`Ā`) a többi eset: `P(Ā) = 1 - P(A)`.

### Feliratok
- cím 1: Mekkora az esély?
- első kocka: 1. kocka
- második kocka: 2. kocka
- esemény A: az összeg legalább 10
- esemény B: van hatos
- esemény C: a két szám egyenlő
- esemény D: a szorzat páros
- gomb A: összeg ≥ 10
- gomb B: van hatos
- gomb C: dupla
- gomb D: páros szorzat
- ellentett gomb: ellentett
- ellentett sablon: nem igaz, hogy # (Ā)
- omega sablon: Ω: # elemi esemény
- kedvező sablon: # kedvező eset a 36-ból
- összeg jel: összeg
- szorzat jel: szorzat

### Adatok
- összes eset: 36
- van hatos esetei: 11
<!-- 6 · 6 = 36. „Van hatos”: 6 + 6 − 1 = 11 (a (6; 6) egyszer számít), ellentettje „nincs hatos”: 5 · 5 = 25,
     11 + 25 = 36. Összeg ≥ 10: (4; 6), (5; 5), (6; 4), (5; 6), (6; 5), (6; 6) = 6. Dupla: 6. Páros szorzat:
     36 − 9 = 27 (páratlan szorzat csak páratlan · páratlan: 3 · 3 = 9). A lecke mindet megszámolja. -->

## 2. Tévhit: három eset, mindegyik 1/3?
Két érmét dobunk. A fejek száma 0, 1 vagy 2 – akkor mindegyik `1/3`? ==Nem: ez a három kimenetel nem egyformán valószínű.== Ha megkülönböztetjük az érméket, 4 egyforma esélyű elemi esemény van: FF, FI, IF, II. Az „1 fej” kettőt is lefed: `P = 2/4 = 1/2`. Dobj, és figyeld az oszlopokat!

### Feliratok
- cím 2: Hány fej lesz két érmén?
- fej betű: F
- írás betű: I
- első érme: 1. érme
- második érme: 2. érme
- fej csoport: # fej: # eset a 4-ből
- fej oszlop: # fej
- tévhit egyharmad: tévhit: 1/3
- négy eset alapján: a 4 eset alapján
- rel tengely: relatív gyakoriság
- utolsó dobások: az utolsó dobások

### Adatok
- egy fej esélye: 1/2
<!-- FF, FI, IF, II egyformán 1/4: P(0 fej) = 1/4, P(1 fej) = 2/4 = 1/2, P(2 fej) = 1/4. A lecke kiszámolja és összeveti.
     A „0, 1, 2 fej egyformán 1/3” tévedést d’Alembert-nek tulajdonítják (Encyclopédie, „Croix ou pile”, 1754) –
     a lecke név nélkül mutatja (ellenőrizendő, ha név is kerülne bele). -->

## 3. A nagy számok törvénye
Egy érmét dobunk sokszor. A fejek **relatív gyakorisága** egyre kisebb kilengéssel ingadozik `1/2` körül: ez a **nagy számok törvénye**, és ezért mondjuk, hogy `P(fej) = 1/2`. De nézd a táblázatot: ==a fejek száma és a várt n/2 közti eltérés nem tűnik el, sőt nőhet.== Az érme nem „egyenlít ki”, csak a sok dobás felhígítja az eltérést.

### Feliratok
- cím 3: Mit jelent, hogy P(fej) = 1/2?
- dobás tengely: dobások száma
- fej rel tengely: a fejek relatív gyakorisága
- log megjegyzés: a tengelyen minden osztás 10-szeres
- sáv felirat: sáv: ± 1/√n
- oszlop n: dobás
- oszlop fej: fej
- oszlop várt: várt: n/2
- oszlop eltérés: eltérés
- oszlop rel: rel. gyakoriság
- más sorozatok: további 4 sorozat

## 4. Végtelen sok eset: területek aránya
Anna és Bence 17 és 18 óra között, véletlen időpontban érkezik, és {várakozás}ig vár a másikra. Minden érkezéspár egy pont a négyzetben. Az esetek száma végtelen, ezért a **területeket** osztjuk (**geometriai valószínűség**): ==P = a sáv területe : a négyzet területe.== {várakozás}nél `1 - (45/60)^2 =` {találkozás esélye} `~= 0,44`.

### Feliratok
- cím 4: Találkoznak?
- Anna tengely: Anna érkezése (perc)
- Bence tengely: Bence (perc)
- találkoznak: találkoznak
- nem találkoznak: nem találkoznak
- várakozás csúszka: várakozás (perc)
- pontok sablon: # pontból # a sávban
- terület arány: P = sáv : négyzet
- mért arány: mért arány

### Adatok
- várakozás: 15 perc
- időszak: 60 perc
- találkozás esélye: 7/16
<!-- A két érkezés egymástól független és egyenletes eloszlású a 60 percben (modell). A sávon kívüli két
     háromszög együtt (60 − 15)² = 45², ezért P = 1 − (45/60)² = 1 − 9/16 = 7/16 = 0,4375. Pontosan 1/2-nél:
     (1 − w/60)² = 1/2 → w = 60 · (1 − 1/√2) ≈ 17,6 perc. A geometriai valószínűség a kerettanterv szerint
     11–12. évfolyamos anyag – itt kitekintés. A lecke a sáv sokszögének területét is kiszámolja. -->

## 5. Monty Hall: maradj vagy válts?
Három ajtó: egy mögött autó, kettő mögött kecske. Választasz egyet. A műsorvezető, aki tudja, hol az autó, kinyit egy **másik** ajtót, mögötte kecske. Maradsz vagy váltasz? Tévhit: ==„két ajtó maradt, fele-fele”.== Játssz néhányat, aztán futtasd a gépet: minden játékot mindkét stratégiával lejátszik.

### Feliratok
- cím 5: Maradj vagy válts?
- válassz: Kattints egy ajtóra!
- maradsz: Maradsz? Kattints a te ajtódra! Váltasz? A másikra!
- nyertél: Autó! Nyertél.
- vesztettél: Kecske. Most nem nyertél.
- te választod: te
- új játék gomb: új játék
- te játékaid: a te játékaid
- maradtál sablon: maradtál: # játék, # autó
- váltottál sablon: váltottál: # játék, # autó
- gépi játékok: gépi játékok
- gépi sablon: # gépi játék
- nyerési arány: nyerési arány
- vált: vált
- marad: marad

## 6. Miért 2/3? Fa-diagram
Az 1. ajtót választod. Az autó `1/3` eséllyel áll bármelyik ajtó mögött. Ha az 1. mögött, a műsorvezető fele-fele eséllyel nyit; ha nem, csak egy ajtót nyithat. Egy út esélye az ágak szorzata. ==Váltva csak akkor veszítesz, ha elsőre eltaláltad (`1/3`). Tehát váltva {váltva nyer}.== ∎

> megjegyzés: Gondold el 100 ajtóval: te egyet választasz, ő 98-at kinyit. Maradnál?

### Feliratok
- cím 6: Miért nyer a váltás?
- autó helye: az autó helye
- kinyitja: kinyitja
- út esélye: az út esélye
- te: 1. ajtó
- marad gomb: ha maradsz
- vált gomb: ha váltasz
- nyer: nyer
- veszít: veszít

### Adatok
- váltva nyer: 2/3
<!-- Az 1. ajtó választása után: autó az 1. mögött (1/3) → nyit 2 vagy 3 (1/2–1/2) → 1/6 + 1/6; autó a 2. mögött (1/3) →
     csak a 3.-at nyithatja → 1/3; autó a 3. mögött → csak a 2.-at → 1/3. Marad: 1/6 + 1/6 = 1/3; vált: 1/3 + 1/3 = 2/3.
     Feltétel (a szokásos modell): a műsorvezető MINDIG kinyit egy kecskés ajtót, és felajánlja a cserét; ha választhat,
     véletlenszerűen nyit. A lecke a fa leveleiből kiszámolja és összeveti. -->

## 7. Születésnap-paradoxon
Hány ember közt valószínűbb, mint nem, hogy kettőnek egy napon van a születésnapja? Sokan 183-at tippelnek. ==Már {emberek} embernél 50 % fölött van!== Mert nem a *te* napodat keressük: {emberek} embernek {párok száma} párja van. Hogy *senkinek* ne egyezzen: `365/365 * 364/365 * ... * 343/365 ~= 0,49`.

### Feliratok
- cím 7: Közös születésnap?
- fő sablon: # fő
- egyezés sablon: # közös születésnap
- nincs egyezés: nincs közös születésnap
- emberek csúszka: emberek száma
- új osztály gomb: új osztály
- ezer osztály gomb: 1000 osztály
- emberek tengely: emberek száma
- valószínűség tengely: P(van közös nap)
- párok sablon: # pár
- elmélet sablon: számolva: #
- szimuláció sablon: # osztályból #-ban volt
- modell felirat: 365 egyforma esélyű nap

### Adatok
- emberek: 23
- napok: 365
- párok száma: 253
- egyezés esélye: 50,7 %
<!-- P(van közös nap) = 1 − 365 · 364 · … · (365 − n + 1) / 365^n; n = 23: 0,5073 (Pythonnal, pontos törtekkel ellenőrizve,
     2026-11-24); n = 30: 0,706; n = 50: 0,970; n = 70: 0,9992. Párok: 23 · 22 : 2 = 253. Modell: 365 egyforma esélyű
     nap, szökőnap nélkül, független születésnapok – a valóságban a születések nem egyenletesek, ez az esélyt
     kicsit növeli. „Valakinek az ÉN napomon”: 1 − (364/365)^22 ≈ 5,9 %. A lecke kiszámolja és összeveti. -->

## 8. Szerencsejáték: ki nyer hosszú távon?
Az európai rulettkeréken {mezők} mező van: {piros mezők} piros, {piros mezők} fekete és a zöld 0. Pirosra {tét} a tét: 18 esetben nyersz {tét}, 19 esetben elveszted. ==37 körből átlagosan {tét} a veszteség: körönként kb. {várható veszteség}.== Egy számra (35-szörös nyeremény) ugyanennyi, nagyobb kilengéssel.

> megjegyzés: Rövid távon bárki nyerhet. Hosszú távon a nagy számok törvénye a bankot segíti.

### Feliratok
- cím 8: Ki nyer hosszú távon?
- pirosra gomb: pirosra
- egy számra gomb: egy számra (17)
- plusz 100 kör: +100 kör
- 500 kör gomb: 500 kör
- kör tengely: körök száma
- egyenleg tengely: egyenleg (ezer Ft)
- átlag felirat: 20 játékos átlaga
- várható felirat: körönként −1/37 tét
- feltéve sablon: feltéve: # Ft
- egyenleg sablon: a játékosok összesen: # Ft
- arány sablon: arányban: #
- nyerő sablon: most pluszban: # játékos
- kör sablon: # kör, 20 játékos

### Adatok
- mezők: 37
- piros mezők: 18
- tét: 1000 Ft
- egy szám szorzó: 35
- várható veszteség: 27 Ft
<!-- Európai rulett: 0–36, 18 piros, 18 fekete, 1 zöld (0). Pirosra: nyerés 18/37 (+1 tét), vesztés 19/37 (−1 tét) →
     körönként (18 − 19)/37 = −1/37 tét ≈ −2,7 %, 1000 Ft-nál ≈ −27,03 Ft. Egy számra: 1/37 (+35 tét), 36/37 (−1 tét) →
     (35 − 36)/37 = −1/37 tét, ugyanannyi. Az amerikai rulettnek két zöld mezője van (0 és 00): ott −2/38 ≈ −5,3 %.
     A kerék számsorrendje az európai keréké. A lecke kiszámolja és összeveti (egész Ft-ra kerekítve). -->

## 9. Összefoglalás
- **Klasszikus modell:** `P(A) =` kedvező : összes – de csak egyformán valószínű elemi eseményekkel.
- **Ellentett:** `P(Ā) = 1 - P(A)`.
- **Nagy számok törvénye:** a relatív gyakoriság beáll, az eltérés darabszámban nem tűnik el.
- **Geometriai valószínűség:** terület : terület.
- ==A meglepő eredményt is számolással ellenőrizd==: Monty Hall, születésnap, rulett.

### Feliratok
- össz klasszikus: klasszikus modell
- össz klasszikus sor: kedvező : összes
- össz egyforma: csak egyforma esélyű esetekkel
- össz nagy számok: nagy számok törvénye
- össz nagy számok sor: a relatív gyakoriság beáll
- össz geometria: geometriai valószínűség
- össz geometria sor: terület : terület
- össz monty: Monty Hall
- össz monty sor: váltva 2/3
- össz születésnap: születésnap
- össz születésnap sor: 23 főnél már 50 % fölött
- össz rulett: rulett
- össz rulett sor: körönként −1/37 tét

<!-- Matematikai ellenőrzés (Pythonnal, pontos törtekkel, 2026-11-24):
  - Két kocka: 36 eset; „van hatos” 11, „nincs hatos” 25; összeg ≥ 10: 6; dupla: 6; páros szorzat: 27.
  - Két érme: P(0; 1; 2 fej) = 1/4; 1/2; 1/4.
  - Érme, seed 1: 10 dobásnál 7 fej (eltérés 2), 100-nál 58 (8), 1000-nél 512 (12), 10 000-nél 5062 (62);
    a relatív gyakoriság 0,7 → 0,58 → 0,512 → 0,5062. A ± 1/√n sáv a relatív gyakoriság szórásának (1/(2√n)) kétszerese.
  - Találkozás: 1 − (1 − w/60)², w = 15: 7/16; 1/2-nél w ≈ 17,57 perc.
  - Monty Hall: marad 1/3, vált 2/3 (fa és 1000 seedelt gépi játék).
  - Születésnap: n = 23: 0,5073; párok 253.
  - Rulett: −1/37 tét körönként mindkét fogadásnál; 1000 Ft-nál −27,03 Ft.
  Tanári megjegyzések: a geometriai valószínűség (4. lépés) a kerettanterv szerint 11–12.-es, itt kitekintés;
  az 5–6.-os lecke két kocka összegét, a „jár már az írás?” kérdést és a 10 korongos lépegetést már tárgyalta.
-->
