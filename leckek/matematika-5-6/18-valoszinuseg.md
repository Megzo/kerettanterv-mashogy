# Melyik összeg a legszerencsésebb? – valószínűségi kísérletek
tantárgy: Matematika · évfolyam: 5–6. · témakör: 18. Valószínűség-számítás

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/18-valoszinuseg.md
  Feliratban a # jel helyére a lecke számot ír (pl. „# fej után” → „5 fej után”).
  A kísérletek (pénzérme, kocka, korong) a gépen „dobódnak”: rögzített kezdőértékből (seed) számolt
  véletlen sorozat, ezért minden megnyitáskor ugyanaz jön ki. Az „Új kísérlet” gomb új sorozatot kér.
  Az eseménykártyák SZÖVEGE itt átírható, de hogy melyik dobásnál „nyernek”, azt a kód dönti el
  (pl. „páros számot dobunk” = 2, 4, 6). Ha egy kártya értelmét változtatod, szólj a fejlesztőnek.
-->

## Közös

### Feliratok
- tippelj: Tippelj előbb!
- a tipped: a te tipped
- biztos: biztos
- lehetséges: lehetséges
- lehetetlen: lehetetlen
- fej: fej
- írás: írás
- fej betű: F
- írás betű: I
- dobás gomb 1: Dobj 1-et!
- dobás gomb 10: Dobj 10-et!
- dobás gomb 100: Dobj 100-at!
- dobás gomb 1000: Dobj 1000-et!
- új kísérlet: Új kísérlet
- dobások: dobások száma
- gyakoriság tengely: gyakoriság
- várható: szaggatott: amennyi várható

### Adatok
- kísérletek legfeljebb: 10 000
<!-- Ennyi dobásig mehet egy kísérlet (a gombokkal). -->

## 1. Biztos, lehetséges, lehetetlen
Dobunk egy kockával. Egy esemény lehet **biztos** (mindig bekövetkezik), **lehetetlen** (soha nem következik be), vagy **lehetséges, de nem biztos**. Tévhit: a „lehetséges” fele-fele esélyt jelent. ==A lehetséges események esélye nagyon különböző.== Dobj, és figyeld a kártyákat!

### Feliratok
- kérdés 1: Mi történhet egy kockadobásnál?
- dobj gomb: Dobj a kockával!
- hetest dobunk: 7-est dobunk
- hatost dobunk: 6-ost dobunk
- párosat dobunk: páros számot dobunk
- kisebbet dobunk: 6-nál kisebbet dobunk
- legfeljebb hat: legfeljebb 6-ot dobunk
- lehetséges sáv: lehetséges, de nem biztos
- esély tengely: esély
- kedvező esetek: # eset a 6-ból
- a dobás: a dobás

## 2. Három korong: az összes eset
Feldobunk három korongot. Mindegyik **piros** vagy **kék** lesz. Hány különböző eredmény lehet? Az **ágrajz** minden esetet megmutat: az első korong 2 ágra bomlik, mindkét ág újra 2-re, és még egyszer. ==2 · 2 · 2 = {korong esetek} eset.==

> megjegyzés: Dobd fel a korongokat: melyik ágon jártál?

### Feliratok
- korong 1: 1. korong
- korong 2: 2. korong
- korong 3: 3. korong
- piros betű: P
- kék betű: K
- esetek: # eset
- dobd fel gomb: Dobd fel a korongokat!
- dobás eredménye: a dobás

### Adatok
- korong esetek: 8
<!-- 2 · 2 · 2 = 8. A lecke az ágrajz leveleit megszámolja, és összeveti ezzel. -->

## 3. Melyik a jó kártya?
==Tippelj előbb!== A „van két egyforma szín” kártya biztos, lehetséges vagy lehetetlen? A táblázat mind a 8 esetet mutatja. Egy kártya annyi esetben nyer, ahány pipa van a sorában. ==A 8 pipás kártya biztos, a pipa nélküli lehetetlen.==

> megjegyzés: Melyik két kártya jelenti ugyanazt?

### Feliratok
- a 8 eset: a 8 eset
- mindhárom kék: mindhárom kék
- több kék: több a kék, mint a piros
- nincs piros: nincs piros
- van kék: van kék
- két egyforma: van két egyforma szín
- egyik sincs kettő: egyik színből sincs legalább kettő
- legjobb kártya: a legjobb kártya: mind a 8 esetben nyer

## 4. Dobjunk sokszor!
Feldobunk egy pénzérmét. A **gyakoriság**: hányszor lett fej. A **relatív gyakoriság**: a dobások hányad része lett fej (gyakoriság : dobások száma). 10 dobásnál még bármi kijöhet. ==Sok dobásnál a relatív gyakoriság egyre kevésbé ingadozik, és 1/2 közelében marad.==

### Feliratok
- fej gyakorisága: fej (gyakoriság)
- relatív gyakoriság: relatív gyakoriság
- utolsó dobások: az utolsó # dobás
- fej relatív tengely: a fej relatív gyakorisága
- log megjegyzés: a tengelyen minden osztás 10-szeres

## 5. Jár már az írás?
==Tippelj előbb!== {sorozat hossza} fej jött egymás után. Mire nagyobb az esély a következő dobásnál? Kikerestük a {kísérletek legfeljebb} dobásból az összes ilyen helyet, és megnéztük, mi jött utána. ==Az érme nem emlékszik:== utána is fele-fele.

### Feliratok
- kérdés 5: Mi jön # fej után?
- tipp írás: inkább írás
- tipp fej: inkább fej
- tipp egyforma: egyforma az esély
- sorozatok: # helyen jött # fej egymás után
- utána jött: ami utána jött
- fej aránya: fej utána
- sorozat felirat: # fej egymás után

### Adatok
- sorozat hossza: 5
<!-- Hány fej után nézzük a következő dobást. 2 és 8 között átírható; a lecke átszámolja.
     Az átfedő sorozatok külön számítanak (6 fej egymás után = 2 hely). 10 000 dobásban 5 fejes hely
     kb. 10 000 : 32 ≈ 310 van; ezek után a fej és az írás nagyjából fele-fele. -->

## 6. Két kocka: 36 eset
==Tippelj előbb!== Két kockával dobunk, és összeadjuk a dobott számokat. Melyik összeg jön ki a leggyakrabban? A táblázatban mind a {két kocka esetei} eset benne van. Az egyforma összegek egy átlón sorakoznak. Tévhit: ==minden összeg egyformán gyakori.==

> megjegyzés: Húzd a csúszkát!

### Feliratok
- kérdés 6: Melyik összeg jön ki a leggyakrabban?
- tipp 2: 2
- tipp 7: 7
- tipp 12: 12
- tipp mind egyforma: mind egyforma
- első kocka: 1. kocka
- második kocka: 2. kocka
- esetek tengely: esetek száma
- összeg tengely: összeg
- összeg csúszka: összeg
- összeg esetei: összeg #: # eset a 36-ból
- összeg lehetetlen: összeg #: lehetetlen
- tizenhárom: az összeg 13: lehetetlen
- legfeljebb tizenkettő: az összeg legfeljebb 12: biztos

### Adatok
- két kocka esetei: 36
- hetes esetek: 6
<!-- 6 · 6 = 36 eset. Összeg 7: (1; 6), (2; 5), (3; 4), (4; 3), (5; 2), (6; 1) = 6 eset; 6 és 8: 5–5; 2 és 12: 1–1.
     A lecke mindkettőt kiszámolja és összeveti. -->

## 7. Szimuláció: a 7 nyer
Dobjunk sokszor két kockával! Az oszlopok a gyakoriságot mutatják, a szaggatott keret azt, amennyi a 36 eset alapján várható. Kevés dobásnál nagy az eltérés. ==Sok dobásnál a 7 nyer: a dobások kb. {hetes esély} részében jön ki.==

### Feliratok
- hetes gyakoriság: a 7 gyakorisága
- hetes relatív: relatív gyakorisága
- 36 alapján: a 36 eset alapján

### Adatok
- hetes esély: 1/6
<!-- 6/36 = 1/6 ≈ 0,17 (16,7 %). A lecke kiszámolja és összeveti. -->

## 8. Lépegetés: válassz 4 számot!
Feldobunk 10 korongot. A 0-ból annyit lépünk jobbra, ahány piros, aztán annyit balra, ahány kék. Kattints 4 számra: nyersz, ha ezek egyikére érkezel! Játssz 100 kört! ==Miért nem nyer soha egy páratlan szám?==

### Feliratok
- kérdés 8: Hová érkezel? Válassz 4 számot!
- piros darab: piros: #
- kék darab: kék: #
- egy kör gomb: Dobj egyszer!
- száz kör gomb: Játssz # kört!
- legjobb gomb: A legjobb 4 szám
- törlés gomb: Kártyák törlése
- válassz: kattints 4 számra a számegyenesen!
- nyertél: nyertél: # kör a #-ből
- páratlan soha: páratlanra soha!
- legjobb esély: 1024 esetből # nyer
- érkezések: érkezések

### Adatok
- körök gombonként: 100
- legjobb négy esélye: 77 %
<!-- 10 korong: 2^10 = 1024 eset. A végpont = piros − kék = 2 · piros − 10, ezért mindig páros.
     Esetszámok: 0 → 252, ±2 → 210, ±4 → 120, ±6 → 45, ±8 → 10, ±10 → 1 (binomiális együtthatók).
     A legjobb 4 kártya: 0, 2, −2 és 4 (vagy −4): 252 + 210 + 210 + 120 = 792 eset, 792 : 1024 ≈ 77 %.
     A lecke kiszámolja és összeveti (±0,5 %). -->

## 9. Összefoglalás
- **Biztos:** mindig. **Lehetetlen:** soha. **Lehetséges:** néha – az esélye kicsi is, nagy is lehet.
- **Az összes eset:** ágrajz, táblázat.
- **Relatív gyakoriság** = gyakoriság : kísérletek száma. Sok kísérletnél alig ingadozik.
- ==Az érme és a kocka nem emlékszik.==

### Feliratok
- össz esély: biztos, lehetséges, lehetetlen
- össz esetek: összes eset: ágrajz, táblázat
- össz relatív: sok dobásnál beáll
- össz kocka: két kocka: a 7 a leggyakoribb

<!-- Tanári megjegyzések:
  - A kísérletek „gépi dobások”: egy rögzített kezdőértékből (seed) számolt álvéletlen sorozat (minden
    megnyitáskor ugyanaz). Az „Új kísérlet” gomb új sorozatot ad – érdemes megmutatni, hogy 10 dobásnál
    nagyon eltérhet, 10 000-nél alig.
  - A „valószínűség” szót a lecke szándékosan nem használja (5–6.: „esély”, „kisebb/nagyobb eséllyel
    lehetséges”). Az 1. lépés esélyskálája 0-tól 1-ig a „hány eset a 6-ból” arányt mutatja – ez a 7–8.
    klasszikus valószínűségét készíti elő; elhagyható.
  - A 3. lépés hat kártyája a kerettanterv „3 korong” eseménykártyás játékából való (szó szerint).
    A „mindhárom kék” és a „nincs piros” ugyanaz az esemény – erre kérdez rá a megjegyzés.
  - A 4. lépés grafikonjának vízszintes tengelye logaritmikus (1, 10, 100, 1000, 10 000) – a felirat
    kimondja („minden osztás 10-szeres”). Így a kezdeti nagy ingadozás és a késői beállás is látszik.
  - Az 5. lépés a „szerencsejátékos tévedés”: a sorozat után az esély ugyanaz. Az átfedő sorozatok
    külön számítanak (6 fej egymás után = két 5 fejes hely).
  - A 8. lépés a kerettanterv „10 korong” lépegetős játéka: előbb a pirosak száma szerint jobbra, aztán a
    kékek száma szerint balra. A korong-színek: piros = pozitív irány (cinóber), kék = negatív irány.
  - Átfedés meglévő anyaggal: PhET „Plinko Probability” (nincs ellenőrizve) – ott a golyók, itt a
    lépegetés mutatja ugyanazt az eloszlást.
-->
