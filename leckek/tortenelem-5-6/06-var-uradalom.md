# Kik laktak a várban? – vár, uradalom és jobbágyfalu
tantárgy: Történelem · évfolyam: 5–6. · témakör: 4. A középkor világai

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/tortenelem-5-6/06-var-uradalom.md

  Kerettanterv (4. A középkor világai): „Élet a várban – egy magyar vár (pl. Visegrád) és uradalom
  bemutatásával” · „Egy uradalom működése, a falvak világa (a jobbágyok élete).” · „A középkori és
  a mai életforma néhány jellegzetességének összehasonlítása.” · „Az egyes középkori társadalmi
  rétegek életformája közti eltérések összehasonlítása.” Fogalmak: földesúr, lovag, nemes,
  uradalom, jobbágy, robot. Topográfia: Visegrád.

  Formátum-megjegyzések:
  – A képek (vár, falu, telek, Visegrád) stilizált, saját rajzú illusztrációk, nem egy konkrét
    hely pontos képe. A helyek (hol a vár, hol a malom) a kódban vannak.
  – Listás feliratokban az elemeket vessző választja el (a napirendben pontosvessző); az elemek
    száma nem változhat. A napirend órái a feliratban vannak („5–7 …”), a rajz ezekből készül.
  – A naptár-feliratok elején álló dátum („április 24.”, „augusztus”) a kerék pontjának helye.
  – A nyomások bevetett része: (n − 1)/n, a lecke a rajzolt táblák területéből számolja
    (2 nyomás → 50 %, 3 nyomás → 67 %).

  Vitatott / bizonytalan pontok (tanári és szakmai review-hoz):
  – A vár lakóinak száma (kb. 20–50 fő) szemléltető becslés. Váranként nagyon eltérő: kis
    magánvárban gyakran 10-nél kevesebb fegyveres szolgált, királyi várban több.
    (Engel Pál: Szent István birodalma, 2001; Fügedi Erik: Vár és társadalom, 1977.)
  – A háromnyomásos gazdálkodás a 13–14. században terjedt el Magyarországon, de sok helyen
    tovább élt a kétnyomásos rend (domborzat, talaj). A lecke a két rendszert hasonlítja össze.
  – A tized az egyházé (a nagyobb rész a püspöké), a kilenced a földesúré: az 1351-es törvény
    (Nagy Lajos) tette kötelezővé minden földesúrnak, és megerősítette a szabad költözést.
  – A földbért (cenzust) sok helyen Szent György és Szent Mihály napján fizették; az
    ajándékot nagy ünnepeken (karácsony, húsvét, pünkösd) adták. Helyenként más volt a rend.
  – A robot a 14. században kevés volt: évente néhány nap (vidékenként, birtokonként eltérő,
    sok helyen pénzzel megváltották). A „kb. 3–12 nap” szemléltető becslés, ellenőrizendő.
    Az 1514-es törvény heti 1 napot írt elő; Mária Terézia úrbéri rendelete (1767) egész telek
    után évi 52 nap igás vagy 104 nap gyalogrobotot.
  – A hozam (a vetőmag kb. 3–5-szöröse) a korabeli Európára szokásos becslés; a „100 zsák” csak
    szemléltető szám, nem egy valódi telek termése.
  – Várható élettartam: a születéskori kb. 30 év a nagy gyermekhalandóság miatt alacsony;
    aki felnőtt, gyakran 50–60 évig élt (becslés). Ma Magyarországon kb. 77 év (KSH, 2023
    körül; nőknél több, férfiaknál kevesebb).
  – A jobbágygyerek napirendje rekonstrukció (illusztráció), nem forrásból vett órarend.
  – Visegrád: a Fellegvár és az alsóvár (Salamon-torony) a tatárjárás után, 1247-től épült
    (IV. Béla és Laszkarisz Mária). Károly Róbert 1323-ban tette székhelyévé; a királytalálkozó
    1335-ben volt (Károly Róbert, III. Kázmér lengyel és Luxemburgi János cseh király).
  – A palota „350 szobája” Oláh Miklós Hungaria című művéből (1536, Brüsszel) való: emlékezetből
    írt, valószínűleg túlzás. A palota romjait Schulek János ásatásai (1934-től) tárták fel.
  – A Salamon-torony neve hagyomány: Salamon királyt a krónikák szerint I. László Visegrádon
    tartotta fogva (1080-as évek), de a mai torony csak a 13. században épült.
-->

## Közös

### Feliratok
- illusztráció bélyeg: illusztráció
- becslés bélyeg: becslés
- réteg forrás: forrás
- réteg rekonstrukció: rekonstrukció
- réteg monda: monda
- kattints: kattints a pontokra!
- pont vár: A vár
- pont vár szöveg: Az uradalom központja. Veszély idején menedék a falvaknak is.
- pont falu: A jobbágyfalu
- pont falu szöveg: Utca mentén sorakozó házak, mögöttük kert, csűr, istálló.
- pont templom: A templom
- pont templom szöveg: Vasárnap az egész falu itt gyűlt össze. Az egyház a tizedet kapta.
- pont malom: A malom
- pont malom szöveg: Gyakran a földesúré volt: az őrlésért fizetni kellett.
- pont erdő: Az erdő
- pont erdő szöveg: Tűzifa, épületfa, makk a disznóknak – az úr engedélyével.
- pont földek: A szántóföldek
- pont földek szöveg: Nagy táblák, keskeny csíkokra osztva: minden családnak jutott.
- pont rét: A rét és a legelő
- pont rét szöveg: Széna télire, közös legelő a falu jószágának.

## 1. Az uradalom
Ez egy **uradalom**: egy **földesúr**, vagyis a föld urának birtoka. Középen a vár, körülötte falvak, földek, erdők.

A falvak ==terménnyel, pénzzel és munkával== tartották el az urat. Cserébe ő **védelmet** és **bíráskodást** adott.

> megjegyzés: Kattints a képen a pontokra!

### Feliratok
- jelenet cím: Egy uradalom
- nyíl szolgáltatás: termény, pénz, munka
- nyíl védelem: védelem, bíráskodás

## 2. Ki lakik a várban?
**Tévhit:** a várban sok lovag élt. Békeidőben a **várnagy** vezette a várat, az úr helyett. Vele néhány tucat őr, szolga és mesterember élt.

A **lovag** páncélos, lóháton harcoló katona volt. A vár lakóinak többsége nem lovag volt.

### Feliratok
- vár metszet cím: A vár metszete
- várlakók: lakói békeidőben: {várlakók száma}
- tévhit vár: lovagok tömege?
- pont őrség: őrség
- pont őrség szöveg: Őrködnek a falon és a kapuban: íjászok, lándzsások.
- pont istálló: istálló, kovács
- pont istálló szöveg: Lovak, patkolás, a fegyverek és szerszámok javítása.
- pont ciszterna: ciszterna
- pont ciszterna szöveg: Esővizet gyűjtött. Ostromkor ez volt a vár vize.
- pont konyha: konyha
- pont konyha szöveg: Szakácsok, szolgálók – a falvak terményéből főztek.
- pont kamra: kamra
- pont kamra szöveg: Gabona, bor, só, fegyver: a falvak szolgáltatásai és tartalék ostromra.
- pont terem: a földesúr terme
- pont terem szöveg: Sokszor üres: az úrnak több birtoka volt, gyakran máshol járt.
- pont várnagy: várnagy
- pont várnagy szöveg: Az úr embere: ő parancsol az őrségnek, ő gondoskodik a várról.
- pont kápolna: kápolna
- pont kápolna szöveg: A vár papja itt misézett. Gyakran ő írta a leveleket is.

### Adatok
<!-- Szemléltető becslés, váranként nagyon eltérő (lásd fent). -->
- várlakók száma: kb. 20–50 fő

## 3. A jobbágytelek
A falu lakói **jobbágyok**: parasztok, akik a földesúr földjén gazdálkodtak. Egy család **telke**: ház, udvar, kert, és csíkok a szántóföldeken.

**Tévhit:** a jobbágy rabszolga volt. Nem: ==saját háza, jószága, szerszáma volt==, és ha fizetett, el is költözhetett.

### Feliratok
- telek cím: Egy jobbágytelek
- pont ház: ház
- pont ház szöveg: Szoba kemencével, pitvar, kamra. Sárral tapasztott fal, nádtető.
- pont kert: kert
- pont kert szöveg: Káposzta, hagyma, borsó, mák; gyümölcsfák.
- pont ól: istálló, ól
- pont ól szöveg: Ökör az eke elé, tehén, disznó, tyúkok, libák.
- pont csűr: csűr
- pont csűr szöveg: Ide hordták a learatott gabonát, itt csépelték ki.
- pont kút: kút
- pont kút szöveg: A vízhordás gyakran a gyerekek dolga volt.
- pont szerszám: szerszámok
- pont szerszám szöveg: Eke, borona, kasza, sarló – a család saját tulajdona.
- összevetés cím: Rabszolga vagy jobbágy?
- összevetés rabszolga: rabszolga
- összevetés jobbágy: jobbágy
- összevetés sor 1: saját háza, családja
- összevetés sor 2: saját szerszáma, jószága
- összevetés sor 3: a termés nagy része az övé
- összevetés sor 4: elköltözhet ({1351-es törvény})

### Adatok
- 1351-es törvény: 1351

## 4. Kettő vagy három nyomás?
A falu szántóját nagy táblákra, **nyomásokra** osztották. Egy nyomás mindig **ugar** volt: pihent, és a jószág legelt rajta.

Két nyomásnál a szántó fele termett, háromnál ==a két harmada==.

> megjegyzés: Kapcsolj át, és léptesd az éveket!

### Feliratok
- nyomás cím: A falu szántója
- növény őszi: őszi gabona: búza, rozs
- növény tavaszi: tavaszi gabona: zab, árpa
- növény ugar: ugar: pihen, legel a jószág
- kétnyomásos gomb: két nyomás
- háromnyomásos gomb: három nyomás
- következő év gomb: következő év ▸
- kétnyomásos: két nyomás
- háromnyomásos: három nyomás
- bevetett rész: bevetett rész
- év számláló: #. év
- több föld: egyharmaddal több: +# %
- család csíkjai: egy család csíkjai

### Adatok
- nyomások száma régen: 2
- nyomások száma később: 3

## 5. Egy év a faluban
Húzd az évszak-csúszkát! Tavasszal szántottak és vetettek, nyáron arattak, ősszel újra vetettek.

A szolgáltatásoknak is megvolt a napja: Szent György és Szent Mihály napján fizették a **földbért**, aratás után adták a termés részét.

### Feliratok
- évszak csúszka: Évszak
- hónapok: január, február, március, április, május, június, július, augusztus, szeptember, október, november, december
- hónap rövid: jan., febr., márc., ápr., máj., jún., júl., aug., szept., okt., nov., dec.
- naptár cím: a falu éve
- munka szántás: március 20. | szántás, tavaszi vetés
- munka kaszálás: június 10. | kaszálás: széna télire
- munka aratás: június 29. | Péter-Pál: kezdődik az aratás
- munka őszi vetés: október | őszi vetés: búza, rozs
- munka tél: január | cséplés, fonás, favágás
- szolgáltatás György: április 24. | Szent György-nap: földbér
- szolgáltatás tized: augusztus | tized és kilenced a gabonából
- szolgáltatás Mihály: szeptember 29. | Szent Mihály-nap: földbér
- szolgáltatás karácsony: december 25. | karácsony: ajándék az úrnak
- jelmagyarázat munka: munka
- jelmagyarázat szolgáltatás: szolgáltatás

## 6. Mit kell beszolgáltatni?
Aratás után a termés tizedét az egyház kapta: ez a **tized**. A maradék kilencedét a földesúr: ez a **kilenced**. Vetőmagot is félre kellett tenni: ==rossz évben alig maradt==.

**Tévhit:** a **robot** (ingyen munka az úrnak) a középkorban is nehéz volt. Nem: évente néhány nap volt.

### Feliratok
- termés cím: Ha # zsák gabona termett…
- termés csúszka: Milyen volt a termés?
- termés minősége: nagyon rossz, rossz, átlagos, jó, nagyon jó
- tized: tized – az egyháznak
- kilenced: kilenced – a földesúrnak
- vetőmag: vetőmag – jövőre
- család része: a családnak marad
- zsák: # zsák
- más tartozás cím: Ezen felül:
- földbér: földbér: pénz, évente kétszer
- ajándék: ajándék: tyúk, tojás, sajt
- robot cím: Robot évente, egy egész telek után
- robot 14: 14. század
- robot 1514: {robot törvény éve} után
- robot 1767 igás: {úrbéri rendelet éve} után, igával
- robot 1767 gyalog: {úrbéri rendelet éve} után, gyalog
- nap: # nap

### Adatok
<!-- A hozam és a 100 zsák szemléltető (lásd fent). A tized: minden 10. zsák; a kilenced:
     a tized utáni rész minden 9. zsákja (így a teljes termés újabb tizede). -->
- tized osztója: 10
- kilenced osztója: 9
- vetőmag mennyisége: 25 zsák
- hozam: kb. 4
- robot a 14. században: kb. 3–12 nap
- robot törvény éve: 1514
- robot 1514 után: 52 nap
- úrbéri rendelet éve: 1767
- robot 1767 után igás: 52 nap
- robot 1767 után gyalog: 104 nap

## 7. Akkor és most
Húzd a csúszkákat: egy jobbágygyerek napja és a tiéd. Ő többnyire nem járt iskolába: libát őrzött, vizet hordott, aratáskor segített.

**Tévhit:** régen mindenki 30 évesen meghalt. Az átlag azért alacsony, mert ==sok kisgyerek meghalt==. Aki felnőtt, gyakran 50–60 évig élt.

### Feliratok
- akkor most csúszka: Akkor ↔ most
- akkor: akkor: 14. század
- most: most: ma
- napszak csúszka: Napszak
- napirend akkor cím: egy jobbágygyerek napja
- napirend most cím: a te napod
- napirend akkor: 0–5 alvás; 5–7 állatetetés, vízhordás; 7–12 libák a legelőn; 12–13 ebéd; 13–19 segít a földeken; 19–20 vacsora; 20–24 alvás
- napirend most: 0–7 alvás; 7–8 reggeli, indulás; 8–14 iskola; 14–15 ebéd; 15–17 lecke; 17–20 sport, játék; 20–21 vacsora; 21–24 alvás
- éppen: most éppen: #
- élettartam cím: Várható élettartam
- élettartam akkor: születéskor, akkor: {várható élettartam akkor}
- élettartam felnőtt: aki felnőtt: {felnőttek élettartama}
- élettartam ma: születéskor, ma: {várható élettartam ma}
- év egység: év

### Adatok
- várható élettartam akkor: kb. 30 év
- felnőttek élettartama: kb. 50–60 év
- várható élettartam ma: kb. 77 év

## 8. Visegrád: vár és palota
A tatárjárás után, {Fellegvár építése} után épült a **Fellegvár**. Károly Róbert {udvar Visegrádra}-ban ide költöztette a királyi udvart.

==Honnan tudjuk==, milyen volt a palota? Oláh Miklós {Oláh Miklós műve}-ban {palota szobái} szobát írt – valószínűleg túlzás. Romjait {ásatás kezdete}-től ásták ki.

### Feliratok
- visegrád cím: Visegrád
- akkor gomb: akkor
- ma gomb: ma
- pont fellegvár: Fellegvár
- pont fellegvár szöveg: A hegytetőn: a legbiztosabb menedék, itt őrizték a koronát is.
- pont salamon: Salamon-torony
- pont salamon szöveg: Az alsóvár tornya a Duna partján: a folyót és az utat őrizte.
- pont palota: királyi palota
- pont palota szöveg: Károly Róbert, Nagy Lajos, Zsigmond és Mátyás építtette.
- idő fellegvár: {Fellegvár építése}: Fellegvár
- idő udvar: {udvar Visegrádra}: királyi székhely
- idő találkozó: {királytalálkozó}: királytalálkozó
- idő oláh: {Oláh Miklós műve}: Oláh Miklós
- idő ásatás: {ásatás kezdete}: ásatás
- oláh cím: Oláh Miklós: Hungaria, {Oláh Miklós műve}
- oláh szöveg 1: „{palota szobái} szoba” – külföldön,
- oláh szöveg 2: emlékezetből írta, # évvel Mátyás után
- ásatás cím: ásatás, {ásatás kezdete} óta
- ásatás szöveg: falak, kályhacsempék, a Herkules-kút
- rekonstrukció felirat: a palota képe – a romok alapján
- monda szöveg 1: a hagyomány szerint itt raboskodott
- monda szöveg 2: Salamon király (11. század)
- monda szöveg 3: de a torony csak {Fellegvár építése} után épült

### Adatok
<!-- Visegrád: lásd a fenti megjegyzést. A Fellegvár 1247 után épült, ezért a felirat „1247 után”. -->
- Fellegvár építése: 1247
- udvar Visegrádra: 1323
- királytalálkozó: 1335
- Mátyás halála: 1490
- Oláh Miklós műve: 1536
- palota szobái: 350
- ásatás kezdete: 1934

## 9. Összefoglalás
- A vár egy **uradalom** központja volt.
- A jobbágyok a telkükön gazdálkodtak, és ==szolgáltatásokkal tartoztak== az úrnak.
- Három nyomással több föld termett.
- A középkori robot még kevés volt.

Honnan tudjuk? Oklevelekből, **urbáriumokból** (a tartozások listáiból) és falvak ásatásaiból.

### Feliratok
- összefoglaló forrás: oklevelek, urbáriumok
- összefoglaló lelet: falvak ásatásai
- összefoglaló rajz: ez a kép
