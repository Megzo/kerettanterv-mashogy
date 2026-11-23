# Miért zöld a sáska a fűben? – változatosság, kiválasztódás, véletlen
tantárgy: Biológia · évfolyam: 7–8. · témakör: 3. Az élővilág fejlődése

## Közös
### Feliratok
- zöld: zöld
- barna: barna
- átmeneti: átmeneti
- színskála: a sáska színe
- sáskák tengely: sáskák száma
- nemzedék tengely: nemzedék
- átlagszín tengely: átlagos szín
- modell bélyeg: modell – egyszerűsít
- honnan tudjuk: HONNAN TUDJUK?
- újra gomb: Újrasorsolás
- kihaltak: kihaltak
### Adatok
- sáskák száma: 60
- utódok egyedenként: 5
- kezdő átlagszín: 50
- kezdő színszórás: 18
- öröklődési eltérés: 8
- zöld fű színe: 15
- száraz fű színe: 85
- ragadozás erőssége: 60 %
<!-- A modell (1–6. lépés) didaktikus: a szín egyetlen, folytonos tulajdonság egy 0 (zöld) – 100 (barna) skálán; a fű színe ugyanezen a skálán áll. Ivartalan öröklés: minden utód egyetlen szülő színét kapja, plusz egy kis véletlen eltérést (normális eloszlás, szórása az „öröklődési eltérés”). A valódi sáskák ivarosan szaporodnak, és a színüket több gén és a környezet (pl. páratartalom, hőmérséklet) is befolyásolja – a lecke ezt nem modellezi. Egy nemzedékben: minden felnőtt „utódok egyedenként” utódot hagy; a madár mindegyiket a színkülönbségtől függő eséllyel kapja el (túlélési esély = 1 − ragadozás · (0,15 + 0,85 · (1 − e^(−(d/35)²))), ahol d = szín − fű; a 0,15 azt jelenti, hogy a rejtőzőt is elkaphatja); a túlélők közül véletlenszerűen legfeljebb „sáskák száma” lesz felnőtt (eltartóképesség). Minden véletlen seedelt (U.rng-gel azonos xorshift), a QA az alapseeddel fotóz. -->

## 1. Nincs két egyforma
Nézd meg a réten a sáskákat: ==nincs két egyforma==. A színük a zöldtől a barnáig folyamatosan változik – ez a **változatosság**. A különbség egy része **öröklődik**: az utód a szülőjére hasonlít, de kicsit eltér tőle. Az alsó grafikon mutatja, melyik színből hány sáska van.

> megjegyzés: A modell egyszerűsít: itt minden utódnak egy szülője van.

### Feliratok
- kérdés 1: Miért zöld a sáska a fűben?
- szülő: szülő
- utódai: hasonlók, de nem egyformák
- változatos: Egy szülő és az utódai

## 2. Több születik, mint ahány felnő
Egy nőstény sáska általában {peték száma} petét rak. Ha mind felnőne, a rét hamar megtelne. A táplálék és a hely azonban korlátozott: ==a legtöbb utód elpusztul==, mielőtt felnőne. A modellben minden sáskának {utódok egyedenként} utóda van, de csak {sáskák száma} fér el a réten.

> megjegyzés: Darwin kiszámolta: egy elefántpár utódaiból 750 év alatt kb. 19 millió elefánt lenne.

### Feliratok
- kérdés 2: Felnőhet-e minden utód?
- felnőttek: felnőtt sáska
- utódok: utód született
- felnő: felnő belőlük
- véletlen pusztulás: itt még a véletlen dönt
- minden utód: minden utód
- felnőtt utód: felnőtt
### Adatok
- peték száma: 100–200
<!-- Peték száma: a sáskanőstény petecsomókat rak (fajonként 4–40, ill. akár 150 pete egy csomóban, 4–25 csomó); az összes pete jellemzően 100–200, 500 sem ritka (University of Wyoming: Grasshoppers of Wyoming and the West – Life cycle, lekérdezve 2026-11-23). Fajonként erősen eltér; ellenőrizendő a hazai fajokra. Darwin elefántszámítása: A fajok eredete (1859), 3. fejezet: kb. 740–750 év alatt majdnem 19 millió elefánt egyetlen pártól. -->

## 3. A madár választ
A **tövisszúró gébics** sáskákra is vadászik, és szemmel keresi a zsákmányt. Azt veszi észre könnyebben, amelyik ==elüt a fűtől==: a zöld fűben a barnás sáskák tűnnek el gyakrabban. A jobb oldali görbe mutatja, melyik szín milyen eséllyel éli túl. Állítsd a ragadozás erősségét!

### Feliratok
- kérdés 3: Kit kap el a madár?
- gébics: tövisszúró gébics
- túlélési esély: túlélési esély
- túlélte: túlélte: # / #
- elpusztult: a madár elkapta: #
- megette: a madár elkapta
- ragadozás csúszka: a ragadozás erőssége
- megmaradt: megmaradt
<!-- A tövisszúró gébics (Lanius collurio) hazai, nyílt, bokros élőhelyeken élő madár; táplálékának jelentős része nagy rovar (bogarak, egyenesszárnyúak – sáskák, szöcskék). A rajz stilizált (felülnézet). A ragadozás jelzésszerű: a sáska eltűnik. -->

## 4. Nemzedékről nemzedékre
A túlélők utódokat hagynak, és azok rájuk hasonlítanak. Így ==nemzedékről nemzedékre nő a zöldek aránya==: ez a **természetes kiválasztódás**. Amelyik sáska színe jobban illik a fűhöz, az átlagosan több utódot hagy – ő a **rátermettebb**. Tévhit, hogy a rátermett a legerősebb: az, amelyik több utódot hagy.

### Feliratok
- kérdés 4: Mi történik sok nemzedék alatt?
- nemzedék felirat: #. nemzedék
- új nemzedék gomb: Új nemzedék
- tíz nemzedék gomb: 10 nemzedék
- fű csúszka: a fű színe
- átlag vonal: a sáskák átlagos színe
- fű vonal: a fű színe
- rátermettség: rátermettség (túlélési esély)

## 5. Változik a környezet
Jön az **aszály**: a fű megbarnul. Most a zöld sáskák ütnek el, őket kapja el a madár, és ==a hisztogram visszavándorol==. Az evolúciónak **nincs célja**: a populáció ahhoz igazodik, ami éppen van. Próbáld ki: hozz esőt vagy újabb aszályt!

### Feliratok
- kérdés 5: Mi lesz, ha megbarnul a fű?
- aszály gomb: Aszály
- eső gomb: Eső
- aszály: aszály: száraz, barna fű
- eső: eső: zöld fű
- lepke cím: nyírfaarasztó (Anglia)
- lepke 1: #: az első sötét lepke Manchesterben
- lepke 2: #: a lepkék kb. # %-a sötét a kormos fákon
- lepke 3: # után tisztult a levegő – a sötét lepke megritkult
- világos kéreg: zuzmós, világos kéreg
- kormos kéreg: kormos, sötét kéreg
### Adatok
- aszály nemzedéke: 3
- első sötét lepke: 1848
- sötét lepkék éve: 1895
- sötét lepkék aránya: 98 %
- tiszta levegő törvény: 1956
<!-- Nyírfaarasztó (Biston betularia): a sötét (carbonaria) változatot 1848-ban jegyezték fel először Manchesterben (R. S. Edleston, közölve 1864); 1895-re a manchesteri lepkék kb. 98 %-a sötét volt (korabeli becslés, gyakran idézett szám). A brit Clean Air Act 1956-ban született; a sötét változat aránya az 1960–70-es évektől országszerte csökkent, a 2000-es évekre sok helyen ritka lett (Cook 2003; Cook és mtsai 2012, Biology Letters 8: 609–612 – M. Majerus kísérlete a madarak válogató ragadozását igazolta). A „csökkenés kezdete” forrásonként eltér; ellenőrizendő. Az aszály–esős év váltakozás a sáskáknál didaktikus példa (egy nemzedék = egy év). -->

## 6. A véletlen is dönt
Most nincs madár: a szín semmit sem számít. Mégis változik! Hogy ki marad életben, azt a véletlen is eldönti. Ez a **sodródás**. Nézd: ==20 sáskánál minden futás másfelé visz==, 500-nál sokkal kisebb a különbség. Kis populációban a véletlen erősebb, akár a kiválasztódást is felülírhatja.

> megjegyzés: Kapcsold be a madarat is, és hasonlítsd össze a két méretet!

### Feliratok
- kérdés 6: Számít-e a szerencse?
- kicsi gomb: 20 sáska
- nagy gomb: 500 sáska
- madár gomb: Madár be / ki
- populáció: # sáska a réten
- madár van: van madár: a szín számít
- madár nincs: nincs madár: a szín nem számít
- futások: # futás ugyanabból a kezdetből
- végén: a #. nemzedékben az átlagszín: #
- futás 1: 1. futás
### Adatok
- kis populáció: 20
- nagy populáció: 500
- futások száma: 8
<!-- A sodródás (genetikai sodródás) itt egy tulajdonság (szín) véletlen ingadozása; a valóságban génváltozatok gyakoriságának véletlen változása. A modell ugyanaz, mint a 3–5. lépésben, „madár nincs” állásban a ragadozás 0. Az átlagszín (0 = zöld, 100 = barna) a futások végén kis populációban szélesebb sávban szóródik, mint nagyban (a lecke L.checks-e ezt ellenőrzi: ≥ 2×). -->

## 7. Nem akarat: a lamarcki tévedés
Régi tévhit (Lamarck, {Lamarck könyve}): az élőlény **szükségből** változik, és amit élete során szerez, azt örökíti. A sáska színe azonban ==egész életében ugyanaz==. Nem az egyed változik, hanem a populáció: a jobban rejtőzők több utódot hagynak. Darwin ezt {Darwin könyve}-ben írta le.

### Feliratok
- kérdés 7: Megzöldülhet-e a sáska, mert kell neki?
- tévhit: TÉVHIT
- valóság: VALÓSÁG
- tévhit cím: „Szükségből változik, és örökíti”
- valóság cím: A populáció változik, nem az egyed
- t1: barna, zöld fűben
- t2: megzöldül?
- t3: zöld utódok?
- nem így: Nem így történik!
- 1. nemzedék: 1. nemzedék
- 2. nemzedék: 2. nemzedék
- 3. nemzedék: 3. nemzedék
- ugyanaz marad: Minden sáska színe egész életében ugyanaz marad.
- Lamarck könyv: Lamarck: Philosophie zoologique
- Darwin könyv: Darwin: A fajok eredete
- elmélet: Az evolúció elmélete: sok bizonyítékkal alátámasztott magyarázat.
### Adatok
- Lamarck könyve: 1809
- Darwin könyve: 1859
<!-- Lamarck: Philosophie zoologique (1809) – a szükséglet → szokás → a szerv használata/nem használata gondolatmenet; a szerzett tulajdonságok öröklődését nem ő találta ki, a korban általános nézet volt (Darwin is részben elfogadta). Darwin: On the Origin of Species (1859); vele egy időben Wallace is eljutott a természetes kiválasztódás gondolatához (1858). Az „elmélet” szó tudományos értelemben: bizonyítékokkal alátámasztott magyarázó rendszer, nem „feltevés”. A 3 nemzedékes sor rögzített, kitalált példa. Ma tudjuk, hogy a környezet egyes génműködéseket átmenetileg befolyásolhat (epigenetika), de ez nem teszi igazzá a lamarcki elképzelést. -->

## 8. Ellenálló baktériumok
A baktérium nem „szokik hozzá” az antibiotikumhoz: a telepben eleve van néhány **ellenálló** sejt. A gyógyszer az érzékenyeket pusztítja el, ==az ellenállók elszaporodnak==.

> megjegyzés: Antibiotikumot csak orvos rendelhet; vírusra (nátha, influenza) nem hat.

### Feliratok
- kérdés 8: Miért nem hat egyszer csak a gyógyszer?
- antibiotikum: antibiotikum: # egység
- nincs antibiotikum: nincs antibiotikum
- adag csúszka: adag
- hossz csúszka: a kezelés hossza
- újra adag gomb: Újabb kezelés
- baktériumok: baktériumok: #
- idő tengely: idő (óra)
- darab tengely: baktériumok száma
- log skála: log. skála
- ellenállóság tengely: ennyi adagot még kibír
- osztály tengely: ellenállóság
- elpusztul: ← elpusztul
- túléli: túléli →
- adag jel: adag: #
- mind elpusztult: mind elpusztult
- visszanőtt: visszanőtt – # %-uk kibírja ezt az adagot
- kóli: E. coli: # percenként osztódik → # óra alatt 1-ből #
- Fleming: Fleming: penicillin #; # – óvott a túl kis adagtól
- millió: millió
- milliárd: milliárd
- egység: egység
- óra: óra
- érzékeny: érzékeny
- ellenálló: ellenálló
- pötty: 1 pötty = sok baktérium (log. skála szerint)
### Adatok
- osztódási idő: 20 perc
- számolt idő: 8 óra
- kezdő baktériumok: 1 millió
- eltartóképesség a csészében: 1 milliárd
- ellenállók ritkulása: 10
- antibiotikum kezdete: 1 óra
- kezelés hossza: 6 óra
- adag: 16 egység
- penicillin felfedezése: 1928
- Fleming figyelmeztetése: 1945
<!-- E. coli osztódási ideje ideális laboratóriumi körülmények között kb. 20 perc: 8 óra = 24 osztódás → 2^24 = 16 777 216 sejt (a lecke kiszámolja). Penicillin: Alexander Fleming, 1928. Fleming 1945-ös Nobel-előadásában figyelmeztetett, hogy aki túl kis adagot szed, nem halálos mennyiségnek teszi ki a mikrobáit, és ellenállóvá teheti őket (szabad fordítás; mai szóhasználattal: az ellenállókat válogatja ki). Modell (didaktikus, Petri-csésze, immunrendszer nélkül): 6 ellenállósági szint, a szint 1, 2, 4, 8, 16, 32 egységnyi adagot bír ki; a kezdetben minden szint tízszer ritkább az előzőnél; logisztikus növekedés (r = ln 2 / osztódási idő, eltartóképesség); a pusztulás az adag/szint arányától függ (Hill-görbe, max. 6/óra). 1 sejtnél kevesebb = kipusztult. Fontos: a „kezelés hossza” itt csak azt mutatja, hogy rövid kezelés után a túlélők visszanőnek. Hogy a valódi kezelés optimális hossza mennyi, az fertőzésenként más, és a szakirodalomban vita tárgya (pl. Llewelyn és mtsai 2017, BMJ) – ezért a lecke nem ad szedési tanácsot, csak azt mondja: orvos rendeli. -->

## 9. Összefoglalás
- Az egyedek **különböznek**, a különbség egy része **öröklődik**, és több utód születik, mint ahány felnő.
- A környezet ==válogat==: aki jobban illik hozzá, több utódot hagy (**rátermettség**).
- Kis populációban a **véletlen** is dönt (sodródás).
- Az antibiotikum is válogat: az ellenállók maradnak meg.

### Feliratok
- összegzés cím: Amit megtanultunk
- ö1: különbözők és öröklődik
- ö2: a környezet válogat
- ö3: a véletlen is dönt
- ö4: az antibiotikum is válogat

<!-- Vitatott / bizonytalan pontok:
- A modell ivartalan öröklést és egyetlen, folytonos színtulajdonságot használ; a valódi sáskák színét több gén és a környezet is befolyásolja (egyes fajoknál a zöld/barna szín a nimfakori környezettől, pl. a páratartalomtól is függ – ez fenotípusos plaszticitás, NEM lamarcki öröklés). A tanár érdemes kimondja, hogy a példa egyszerűsít.
- Sáskapete-szám: fajonként nagyon eltér (University of Wyoming); a 100–200 tájékoztató érték.
- Nyírfaarasztó: az 1895-ös 98 % korabeli becslés; a csökkenés kezdete forrásonként eltér (1956-os törvény vs. 1960–70-es évek).
- Fleming 1945-ös idézete szabad fordítás.
- Antibiotikum: a „kezelés hossza” csúszka modellhatást mutat, nem orvosi ajánlást; a kezelés ajánlott hossza fertőzésenként más és vitatott (Llewelyn és mtsai 2017). Egyéni tanácsot a lecke nem ad.
- A sodródást a lecke egy tulajdonság véletlen ingadozásaként mutatja; a pontos fogalom génváltozatok gyakoriságára vonatkozik.
-->
