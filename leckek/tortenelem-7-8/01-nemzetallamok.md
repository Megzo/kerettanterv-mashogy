# Miért akart minden nép saját államot? – nemzetállamok, nagyhatalmak, eszmék
tantárgy: Történelem · évfolyam: 7–8. · témakör: 1. A modern kor születése

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/tortenelem-7-8/01-nemzetallamok.md

  Kerettanterv (1. A modern kor születése): „A nemzeti eszme és a nemzetállamok Európája.” · „A világ
  nagyhatalmai és ellentéteik a 20. század kezdetén.” · „Gyarmatbirodalmak a világ térképén.” · „A liberalizmus.”
  · „A konzervativizmus.” · „A szocializmus és kommunizmus eszméje.” · „A keresztényszocializmus.” · Fogalmak:
  „nacionalizmus, liberalizmus, konzervativizmus, demokrácia, szocializmus, kommunizmus, keresztényszocializmus.” ·
  Személyek: „Bismarck, Marx.” · Kronológia: „1871 Németország egyesítése.” · Topográfia: „Németország,
  Olaszország, Brit Birodalom, Amerikai Egyesült Államok, Japán.” · Javasolt tevékenységek: „Németország területi
  egyesítés előtt és utáni térképének összehasonlítása, értékelése.” · „Ismerkedés nemzeti jelképekkel (zászlók,
  himnuszok).” · „Összehasonlító táblázat készítése a korszak politikai eszméiről.” A sorozat nyitó leckéje; a
  nagyhatalmak ellentéteit a 03-elso-vilaghaboru, a 20. századi diktatúrákat a 05-diktaturak viszi tovább.

  Szerkesztői elvek (terv 1.3, szerződés 20.):
  – Az 1. lépés nemzete, zászlaja és államai KITALÁLTAK („kitalált” bélyeg), hogy a fogalom legyen a lényeg, ne
    egy valódi ország.
  – Az eszméket (7. lépés) tárgyilagosan, a 19. századi szerzők gondolatainak PARAFRÁZISÁVAL mutatjuk, mai
    pártokra utalás nélkül. A „kommunizmus” itt 19. századi eszme (Marx–Engels, 1848); a 20. századi kommunista
    diktatúrákat a 05-diktaturak tanítja.
  – Színek: a hatalmak semleges kategória-színeket kapnak (nincs „jó” zöld, „rossz” piros); a szövetségi
    rendszerek a sorozat oldalszíneit (indigó, szilva).

  Térképek: Natural Earth (közkincs; „Made with Natural Earth”).
  – A 2–4. lépés történeti határai a shared/tort/map-torthatar.js egységeiből és csoportjaiból jönnek (de1871,
    eu1914; VÁZLATOS). A Német Szövetség (1815) körvonala és Poroszország, a porosz területszerzések (1866) és a
    többi német állam foltja MAI NÉMET TARTOMÁNYOKBÓL ÉS LENGYEL VAJDASÁGOKBÓL összerakott közelítés (a lecke
    kódjában, „mai tartományhatárokkal közelítve” felirattal): Poroszország 1815 = Brandenburg, Berlin,
    Szász-Anhalt, Észak-Rajna-Vesztfália, Rajna-vidék–Pfalz, Saar-vidék + a Lengyelországhoz és Oroszországhoz
    került volt porosz területek; 1866 = + Alsó-Szászország, Hessen, Schleswig-Holstein, Észak-Schleswig. Eltérés:
    Pfalz bajor, Rajna-Hessen és Felső-Hessen hesseni, Oldenburg és Braunschweig önálló, Előpomeránia porosz,
    Hohenzollern porosz volt. A Német Szövetség körvonala: a Német Császárság mai egységei Kelet- és
    Nyugat-Poroszország, Poznań és Schleswig nélkül, + az osztrák örökös tartományok, a cseh korona országai,
    Krajna, a Tengermellék, Dél-Tirol, Luxemburg és Liechtenstein (Limburg és Schleswig déli része a mai egységek
    miatt hibás).
  – Az 5., 6. és 9. lépés világtérképe a MAI országokat (shared/foldrajz/orszagok.js, 1:110m) színezi az 1914-es
    uralkodó hatalom szerint („mai határokkal közelítve”). Egy mai ország egy színt kap, ezért vegyes területeken
    téves: Lengyelország (orosz, német és osztrák részek – orosznak színezve), Pápua Új-Guinea (brit-ausztrál
    dél, német észak – britnek), Marokkó (francia és spanyol övezet – franciának), Szomália (olasz és brit),
    Kamerun és Togo (német), Egyiptom (brit megszállás 1882-től, protektorátus csak 1914 decemberétől – britnek),
    Szaúd-Arábia (a Hidzsáz oszmán, a belső területek függetlenek), az Arab-öböl kis államai (brit védnökség –
    csak az Egyesült Arab Emírségek és Kuvait színezett). A „befolyás alatt” (Lenin szóhasználatában
    „félgyarmat”) sraffozás: Perzsia (orosz és brit érdekszférák, 1907), Kína, az Oszmán Birodalom.
-->

## Közös

### Feliratok
- forrás jel: forrás
- rekonstrukció jel: rekonstrukció
- monda jel: hagyomány
- vázlatos: vázlatos
- becslés: becslés
- illusztráció: illusztráció
- kitalált bélyeg: kitalált
- Kr. e.: Kr. e.
- Kr. u.: Kr. u.
- század: század
- év sablon: # év
- tippelj felirat: Tippelj!
- kísérlet felirat: térkép
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- mai tartományok: mai tartományhatárokkal közelítve
- mai országok: mai határokkal közelítve
- h UK: Brit Birodalom
- h FR: Franciaország
- h RU: Orosz Birodalom
- h DE: Németország
- h AH: Osztrák–Magyar Monarchia
- h IT: Olaszország
- h US: Egyesült Államok
- h JP: Japán
- h MAS: más gyarmattartók
- h BEF: befolyás alatt
- h MAS sub: Hollandia, Belgium, Portugália, Spanyolország, Dánia
- h BEF sub: Perzsia, Kína, Oszmán Birodalom
- város Berlin: Berlin
- város Bécs: Bécs
- város Párizs: Párizs
- város London: London
- város Róma: Róma
- város Szentpétervár: Szentpétervár
- város Frankfurt: Frankfurt
- millió fő sablon: # millió fő
- hónapok: január, február, március, április, május, június, július, augusztus, szeptember, október, november, december

### Adatok
<!-- forrás (az alábbiakra): a városok helye kerekítve (Wikidata, CC0; Natural Earth populated places, közkincs). -->
- Berlin helye: 52,52° É, 13,40° K
- Bécs helye: 48,21° É, 16,37° K
- Párizs helye: 48,86° É, 2,35° K
- London helye: 51,51° É, 0,13° Ny
- Róma helye: 41,90° É, 12,50° K
- Szentpétervár helye: 59,94° É, 30,31° K
- Frankfurt helye: 50,11° É, 8,68° K

## 1. Mi a nemzet?
A **nemzetet** a közös nyelv, a közös múlt emlékezete és a jelképek (zászló, himnusz) tartják össze. A 19. század **nemzeti eszméje** (**nacionalizmus**) szerint ==minden nemzetnek saját állam jár: **nemzetállam**.== De a nyelvhatár nem éles vonal. Kattints a **Nemzetállam** gombra!

> megjegyzés: A nép, az államok és a zászló kitaláltak. Kérdés: ki maradt kívül, ki lett kisebbség?

### Feliratok
- n1 cím: Kitalált nép, három birodalom
- n1 nép: a lanai nép
- n1 állam A: Hegyi Birodalom
- n1 állam B: Folyóközi Királyság
- n1 állam C: Tengeri Birodalom
- n1 új állam: Lanaia (nemzetállam)
- n1 hozzávalók: Mi tartja össze?
- n1 nyelv: közös nyelv
- n1 nyelv sub: „lanai” anyanyelv
- n1 múlt: közös múlt
- n1 múlt sub: hősök, csaták, mondák
- n1 jelkép: jelképek
- n1 jelkép sub: zászló, himnusz
- n1 jel lanai: lanai nyelvű falu
- n1 jel más: más nyelvű falu
- n1 kisebbség: Az új államban: # más nyelvű falu
- n1 kívül: Az új határon kívül: # lanai falu
- n1 tévhit: „A nemzet = az állam.”
- n1 tévhit b: A nemzet közösség, az állam terület és hatalom.
- gomb nemzetállam: Nemzetállam

## 2. Egy nyelv, sok állam
Napóleon bukása után a **bécsi kongresszus** létrehozta a **Német Szövetséget** ({Német Szövetség}): {tagállamok 1815} laza szövetségét, közös kormány és közös hadsereg nélkül. Németül sokan beszéltek, de ==német állam nem egy volt, hanem sok.== A két legerősebb tag **Ausztria** és **Poroszország** volt.

> megjegyzés: A tagállamok száma változott (alapításkor 39, később 41, 1866-ra 34 – lásd a fájl végén).

### Feliratok
- n2 cím: A Német Szövetség, 1815
- n2 szövetség: a Német Szövetség határa
- n2 Poroszország: Poroszország
- n2 Ausztria: Ausztria (a Szövetségen belül)
- n2 többi: a többi tagállam
- n2 porosz kívül: porosz, a Szövetségen kívül
- n2 Bajorország: Bajorország
- n2 Szászország: Szászország
- n2 Hannover: Hannover
- n2 Württemberg: Württemberg
- n2 Frankfurt sub: a Szövetségi Gyűlés székhelye
- n2 csempék: # tagállam
- n2 csempe sor: 1 császárság, sok királyság, hercegség, szabad város
- n2 tévhit: „Németország mindig is egy ország volt.”
- n2 tévhit b: 1871 előtt nem volt egységes német állam.

### Adatok
<!-- forrás (az alábbiakra): a Német Szövetségi Okmány (Deutsche Bundesakte, 1815. június 8., a bécsi kongresszus
     záróokmányának része); a tagállamok száma: en.wikipedia „German Confederation” (lekérdezve: 2026-11-25): „Thirty-nine
     states participated in the Confederation's June 1815 founding, with two additions by September” (Baden,
     Württemberg); 1817: Hessen-Homburg, a szám később 34-re csökkent (1866). A városok helye: Wikidata (CC0). -->
- Német Szövetség: 1815. június 8.
- tagállamok 1815: 39 állam
- München helye: 48,14° É, 11,58° K
- Drezda helye: 51,05° É, 13,74° K
- Hannover helye: 52,37° É, 9,74° K
- Stuttgart helye: 48,78° É, 9,18° K

## 3. Vas és vér
Poroszország, **Bismarck** vezetésével, háborúkkal egyesítette Németországot. Königgrätznél ({Königgrätz}) legyőzte Ausztriát, Sedannál ({Sedan}) Franciaországot. ==Versailles-ban ({császárság}) kikiáltották a **Német Császárságot**.== Közben **Olaszország** is egyesült ({Olasz Királyság}: királyság, {Róma elfoglalása}: Róma).

> megjegyzés: Hasonlítsd össze a térképet 1815-ben és 1871-ben!

### Feliratok
- n3 cím: Németország egyesítése, 1815–1871
- n3 P: Poroszország
- n3 O: más német állam
- n3 NG: többi tagállam (1867-től)
- n3 AT: Ausztria
- n3 IT: Olaszország (1870)
- n3 határ DB: Német Szövetség
- n3 határ ÉNSZ: Északnémet Szövetség
- n3 határ NCS: Német Császárság
- n3 e szövetség: Német Szövetség
- n3 e olasz: Olasz Királyság
- n3 e königgrätz: Königgrätz
- n3 e annexió: porosz annexiók
- n3 e északnémet: Északnémet Szövetség
- n3 e sedan: Sedan
- n3 e róma: Róma olasz
- n3 e császárság: Német Császárság
- n3 e elzász: Elzász-Lotaringia
- n3 hely Königgrätz: Königgrätz
- n3 hely Sedan: Sedan
- n3 hely Versailles: Versailles
- n3 idézet cím: Bismarck beszéde, # (saját fordítás)
- n3 tagok: 1871: # tagállam + a Birodalmi Tartomány
- csúszka év: Dátum
- csúszka sablon: #. #

### Adatok
<!-- forrás (az alábbiakra): szokásos kronológia – Encyclopaedia Britannica „Unification of Germany”, „Seven Weeks'
     War”, „Franco-German War”, „Italy – The Kingdom of Italy” (britannica.com); en.wikipedia „Unification of
     Germany”, „Prussian annexations of 1866”, „Capture of Rome” (lekérdezve: 2026-11-25). Az olasz királyság
     kikiáltása 1861. március 17. (Torinó); Róma elfoglalása 1870. szeptember 20.; Velence (Venetó) 1866-ban lett
     olasz. Königgrätz (ma Hradec Králové, a csata Sadová és Chlum mellett) 1866. július 3.; a prágai béke 1866.
     augusztus 23. – ezzel szűnt meg a Német Szövetség; a porosz annexiós törvény (Hannover, Hessen-Kassel, Nassau,
     Frankfurt) 1866. szeptember 20., Schleswig-Holstein bekebelezése 1866. december 24. (a térkép egy napon
     mutatja); az Északnémet Szövetség alkotmánya 1867. július 1-jén lépett hatályba; Sedan 1870. szeptember 1.
     (III. Napóleon szeptember 2-án kapitulált); a császárság kikiáltása 1871. január 18., Versailles,
     Tükörterem; a frankfurti béke (Elzász-Lotaringia) 1871. május 10. A Német Császárság tagállamai: 4
     királyság, 6 nagyhercegség, 5 hercegség, 7 fejedelemség, 3 szabad város = 25 + a Birodalmi Tartomány
     (Elzász-Lotaringia). -->
- Olasz Királyság: 1861. március 17.
- Königgrätz: 1866. július 3.
- prágai béke: 1866. augusztus 23.
- porosz annexiók: 1866. szeptember 20.
- Északnémet Szövetség: 1867. július 1.
- Sedan: 1870. szeptember 1.
- Róma elfoglalása: 1870. szeptember 20.
- császárság: 1871. január 18.
- frankfurti béke: 1871. május 10.
- birodalom tagállamai: 25 állam
- Bismarck beszéde: 1862. szeptember 30.
- Königgrätz helye: 50,30° É, 15,80° K
- Sedan helye: 49,70° É, 4,94° K
- Versailles helye: 48,80° É, 2,13° K

<!-- idézet: Otto von Bismarck: beszéd a porosz képviselőház költségvetési bizottságában (1862. szeptember 30.) · szöveg: „Nicht durch Reden oder Majoritätsbeschlüsse werden die großen Fragen der Zeit entschieden – das ist der große Fehler von 1848 und 1849 gewesen –, sondern durch Eisen und Blut.” (Wikisource, német: „Eisen und Blut”); saját fordítás · szerző † 1898 · közkincs -->
### Idézet
- Bismarck 1862: „Nem beszédekkel és többségi határozatokkal dőlnek el a kor nagy kérdései – ez volt 1848 és 1849 nagy hibája –, hanem vassal és vérrel.”

## 4. A nagyhatalmak 1914-ben
1914-re Európában hat **nagyhatalom** versengett: Nagy-Britannia, Franciaország, Németország, Oroszország, az Osztrák–Magyar Monarchia és Olaszország. ==Két új nagyhatalom nőtt fel Európán kívül:== az **Egyesült Államok** és **Japán**. Az USA népessége negyven év alatt több mint kétszeresére nőtt, Japán pedig a Meidzsi-fordulat ({Meidzsi}) után európai mintára modernizált.

### Feliratok
- n4 cím: Európa nagyhatalmai, 1914
- n4 US cím: Egyesült Államok
- n4 US sor: népesség (népszámlálás)
- n4 US forrás: forrás: US Census Bureau
- n4 év 1870: 1870
- n4 év 1910: 1910
- n4 JP cím: Japán
- n4 JP sor 1: Meidzsi-fordulat: #
- n4 JP sor 2: gyárak, vasút, hadsereg európai mintára
- n4 JP sor 3: # legyőzi Oroszországot
- n4 tévhit: „A nagyhatalom = nagy terület.”
- n4 tévhit b: Ipar, hadsereg, népesség és szövetség is kell.

### Adatok
<!-- forrás (az alábbiakra): US Census Bureau, „Resident Population and Apportionment of the U.S. House of
     Representatives” (census.gov; 1870: 38 558 371 fő, 1910: 92 228 496 fő). Meidzsi-restauráció: 1868. január 3.
     (a császári hatalom visszaállításának kikiáltása; Britannica „Meiji Restoration”); az orosz–japán háborút a
     portsmouthi béke zárta, 1905. szeptember 5. (Britannica „Russo-Japanese War”). -->
- USA népessége 1870: 38 558 371 fő
- USA népessége 1910: 92 228 496 fő
- Meidzsi: 1868. január 3.
- portsmouthi béke: 1905. szeptember 5.

## 5. Gyarmatbirodalmak a világtérképen
A nagyhatalmak Afrikát és Ázsia nagy részét **gyarmattá** tették: idegen uralom alá hajtották, nyersanyagot és piacot nyertek belőle. Tippelj!

=={brit gyarmatok területe} volt a brit gyarmatbirodalom==, Nagy-Britannia Írországgal csak {Nagy-Britannia területe}. Kattints egy hatalomra!

### Feliratok
- tipp kérdés: Hányszor nagyobb volt 1914-ben a Brit Birodalom,
- tipp kérdés 2: mint maga Nagy-Britannia (Írországgal)?
- tipp 10: kb. 10×
- tipp 50: kb. 50×
- tipp 100: több mint 100×
- n5 arány 1: Brit Birodalom: #
- n5 arány 2: Nagy-Britannia Írországgal: #
- n5 arány 3: ≈ #-szoros
- n5 népesség cím: #: népesség
- n5 népesség gy: gyarmatok: #
- n5 népesség a: anyaország: #
- n5 grafikon cím: Terület, 1914 (millió km²)
- n5 grafikon jel gy: gyarmatok
- n5 grafikon jel a: anyaország
- n5 részesedés: a hat nagyhatalom a gyarmataival: a szárazföld # %-a
- n5 forrás: forrás: Hübner-táblák (1914), közli Lenin (1916)
- n5 tévhit: „A gyarmatok kis szigetek voltak.”
- n5 tévhit b: India, Afrika nagy része, Szibéria: kontinensnyi terület.
- gomb UK: brit
- gomb FR: francia
- gomb RU: orosz
- gomb DE: német
- gomb US: amerikai
- gomb JP: japán

### Adatok
<!-- forrás (az alábbiakra): „Colonial possessions of the great powers” táblázat, 1914-es oszlopok – Otto Hübner's
     Geographisch-statistische Tabellen aller Länder der Erde, 63. kiadás (az 1914. évre; KIT-katalógus:
     katalog.bibliothek.kit.edu/bib/704347); a táblázatot közli: V. I. Lenin: Az imperializmus mint a kapitalizmus
     legfelsőbb foka (1916), VI. fejezet – angol szöveg: marxists.org/archive/lenin/works/1916/imp-hsc/ch06.htm,
     lekérdezve: 2026-11-25. A szám a statisztikai táblázatból való, nem Lenintől; Lenin a 6 nagyhatalom adatait
     egy táblában adja. Millió km² és millió fő. A gyarmati népesség nagy része BECSLÉS (lásd 8. lépés).
     Számolás (Tippelj!): 33,8 millió km² : kb. 314 ezer km² ≈ 108 (Lenin anyaország-oszlopával: 33,8 : 0,3 ≈
     113) – mindkettő „több mint 100×”. Nagy-Britannia és Írország területe: Nagy-Britannia (Anglia, Skócia, Wales)
     229 848 km² + Írország szigete 84 421 km² ≈ 314 ezer km² (mai területadatok; Office for National Statistics,
     Central Statistics Office). A „kb. 61 %” = a 6 nagyhatalom anyaországokkal együtt 81,5 millió km² : a táblázat
     „Total for the world” sora 133,9 millió km² (a lecke számolja). -->
- brit gyarmatok területe: 33,5 millió km²
- brit gyarmatok népessége: 393,5 millió fő
- brit anyaország területe: 0,3 millió km²
- brit anyaország népessége: 46,5 millió fő
- brit birodalom területe: 33,8 millió km²
- Nagy-Britannia területe: kb. 314 ezer km²
- francia gyarmatok területe: 10,6 millió km²
- francia gyarmatok népessége: 55,5 millió fő
- francia anyaország területe: 0,5 millió km²
- francia anyaország népessége: 39,6 millió fő
- orosz gyarmatok területe: 17,4 millió km²
- orosz gyarmatok népessége: 33,2 millió fő
- orosz anyaország területe: 5,4 millió km²
- orosz anyaország népessége: 136,2 millió fő
- német gyarmatok területe: 2,9 millió km²
- német gyarmatok népessége: 12,3 millió fő
- német anyaország területe: 0,5 millió km²
- német anyaország népessége: 64,9 millió fő
- amerikai gyarmatok területe: 0,3 millió km²
- amerikai gyarmatok népessége: 9,7 millió fő
- amerikai anyaország területe: 9,4 millió km²
- amerikai anyaország népessége: 97 millió fő
- japán gyarmatok területe: 0,3 millió km²
- japán gyarmatok népessége: 19,2 millió fő
- japán anyaország területe: 0,4 millió km²
- japán anyaország népessége: 53 millió fő
- hat hatalom területe: 81,5 millió km²
- világ területe: 133,9 millió km²

## 6. Hol ütközött az érdekük?
A nagyhatalmak két szövetségbe rendeződtek: a **hármas szövetség** ({hármas szövetség}) és az **antant** ({antant 1904}, {antant 1907}) állt szemben. ==Három helyen ütközött a hatalmak érdeke: a Balkánon, Afrikában és a tengereken.== Kattints egy számra!

> megjegyzés: A 03-as lecke innen folytatja: 1914-ben a Balkánról indult a háború.

### Feliratok
- n6 cím: Két szövetség, három ütközőpont
- n6 HSZ: hármas szövetség
- n6 HSZ sub: Németország, Osztrák–Magyar Monarchia, Olaszország
- n6 ANT: antant
- n6 ANT sub: Nagy-Britannia, Franciaország, Oroszország
- n6 gyarmat: gyarmataik (halványabban)
- n6 1 cím: 1 · Balkán
- n6 1 sor: Ausztria–Magyarország és Oroszország
- n6 1 sor 2: # Bosznia annexiója
- n6 2 cím: 2 · Afrika
- n6 2 sor: Németország és Franciaország
- n6 2 sor 2: marokkói válságok: # és #
- n6 3 cím: 3 · tengerek
- n6 3 sor: Németország és Nagy-Britannia
- n6 3 sor 2: flottaverseny – # a Dreadnought csatahajó
- gomb 1: 1 Balkán
- gomb 2: 2 Afrika
- gomb 3: 3 tengerek

### Adatok
<!-- forrás (az alábbiakra): szokásos kronológia – Britannica „Triple Alliance” (1882. május 20., Bécs), „Entente
     Cordiale” (1904. április 8.), „Anglo-Russian Entente” (1907. augusztus 31.), „Bosnian crisis” (az annexió
     kihirdetése 1908. október 6.), „Moroccan crises” (Tanger 1905. március 31.; Agadir 1911. július 1.),
     „Dreadnought” (vízre bocsátás 1906. február 10.); lekérdezve: 2026-11-25. -->
- hármas szövetség: 1882. május 20.
- antant 1904: 1904. április 8.
- antant 1907: 1907. augusztus 31.
- Bosznia annexiója: 1908. október 6.
- tangeri válság: 1905. március 31.
- agadiri válság: 1911. július 1.
- Dreadnought: 1906. február 10.
- Balkán helye: 43,86° É, 18,41° K
- Marokkó helye: 33,50° É, 6,50° Ny
- Északi-tenger helye: 56,00° É, 3,00° K

## 7. Négy eszme: mi a jó társadalom?
A gyárak és városok új kérdéseket hoztak. A **liberalizmus** az egyén szabadságát, a **konzervativizmus** a hagyományt védte. A **szocializmus** közös tulajdont, a **kommunizmus** forradalmat akart. A **keresztényszocializmus** az egyház tanításából keresett választ. ==Húzd a kártyákat a helyükre!==

> megjegyzés: Ezek 19. századi eszmék, nem mai pártok. A kártyák szövege a szerzők gondolatainak összefoglalása, nem szó szerinti idézet.

### Feliratok
- n7 cím: Négy eszme – mi a jó társadalom?
- e LIB: liberalizmus
- e LIB sub: J. S. Mill: A szabadságról (#)
- e KON: konzervativizmus
- e KON sub: E. Burke: Töprengések… (#)
- e SZOC: szocializmus, kommunizmus
- e SZOC sub: Marx–Engels: Kiáltvány (#)
- e KSZ: keresztényszocializmus
- e KSZ sub: XIII. Leó: Rerum novarum (#)
- k LIB 1: Szólás-, sajtó- és vallásszabadság mindenkinek
- k LIB 2: Alkotmány korlátozza a király hatalmát
- k KON 1: Hagyomány és vallás tartja össze a társadalmat
- k KON 2: Csak lassan, óvatosan szabad változtatni
- k SZOC 1: A gyár és a föld legyen közös tulajdon
- k SZOC 2: A munkások forradalma dönti meg a régi rendet
- k KSZ 1: A munkásnak tisztes bér jár, a tulajdon marad
- k KSZ 2: Munkás-egyesületek igen, osztályharc nem
- n7 parafrázis: a kártyák szövege parafrázis
- n7 eredmény: # / # a helyén
- n7 demokrácia: demokrácia: a nép választja a vezetőit – a liberálisok egyre szélesebb választójogot követeltek
- gomb megoldás: Megoldás

### Adatok
<!-- forrás (az alábbiakra): John Stuart Mill: On Liberty (1859; † 1873); Edmund Burke: Reflections on the
     Revolution in France (1790; † 1797); Karl Marx – Friedrich Engels: Manifest der Kommunistischen Partei (1848;
     † 1883 / † 1895); XIII. Leó pápa: Rerum novarum enciklika (1891. május 15.; † 1903) – mind közkincs. A kártyák
     szövege saját parafrázis (nem idézet), ezért nincs ### Idézet blokk. -->
- Burke műve: 1790
- Kiáltvány: 1848
- Mill műve: 1859
- Rerum novarum: 1891

## 8. Honnan tudjuk?
A gyarmati számok korabeli **statisztikai évkönyvből** valók. ==Európában és Indiában népszámlálás volt, a gyarmatok nagy részén csak becslés.== Ugyanezt a táblát idézte **Lenin** 1916-ban, egy vitairatban – a szám nem tőle való. Ellenőrizd: egy összeg nem stimmel! Kattints az **Összeadom** gombra!

### Feliratok
- n8 cím: Honnan tudjuk a számokat?
- n8 típus: statisztikai évkönyv
- n8 mű: Hübner: Földrajzi-statisztikai táblázatok (1914)
- n8 ki l: Ki készítette?
- n8 ki v: Otto Hübner (†1877) alapította, Bécsben szerkesztették
- n8 mi l: Miből?
- n8 mi v: az államok hivatalos statisztikái, gyarmati becslések
- n8 idézi l: Ki idézte?
- n8 idézi v: Lenin vitairata (1916) – a számot érvként használja
- n8 létra cím: Mennyire pontos?
- n8 létra 1: népszámlálás – megszámolták az embereket
- n8 létra 1 sub: Európa, USA, Brit-India (1911)
- n8 létra 2: összeírás, adólista – részben számolt
- n8 létra 2 sub: sok ázsiai és észak-afrikai gyarmat
- n8 létra 3: becslés – a hivatalnok kerekített számot írt
- n8 létra 3 sub: Afrika belseje, Szibéria északi része
- n8 tábla cím: A brit sor a táblázatban (millió fő)
- n8 tábla gy: gyarmatok
- n8 tábla a: anyaország
- n8 tábla ö: összesen, a kiadás szerint
- n8 tábla jó: helyesen: #
- n8 tábla hiba: elírás a kiadásban (vagy a forrásban)
- n8 évek: # évvel később
- n8 lenin: Lenin idézi
- gomb összead: Összeadom

### Adatok
<!-- forrás (az alábbiakra): Hübner-táblák, 63. kiadás (1914) – lásd az 5. lépést; Lenin (1916), marxists.org
     angol kiadás (lekérdezve: 2026-11-25): a brit sorban „Total 1914 … Pop. 444.0”, holott 393,5 + 46,5 = 440,0; a
     hat hatalom összesen-sora (960,6) a 440,0-val jön ki (440,0 + 169,4 + 95,1 + 77,2 + 106,7 + 72,2 = 960,6), tehát
     elírás. Hogy a nyomtatott eredetiben vagy az online kiadásban van-e, nem ellenőriztük. Otto Hübner
     1818–1877; az 1911 utáni kiadásokat Bécsben szerkesztették (I. von Juraschek és mások; katalógusadat,
     oeaw.ac.at). Brit-India népszámlálása: 1911 (Census of India 1911). -->
- Hübner-táblák: 1914
- Lenin műve: 1916
- brit összesen a kiadásban: 444 millió fő

## 9. Összefoglalás: az 1914-es világ
A 19. században a **nemzeti eszme** új államokat hozott létre: 1871-re Németország és Olaszország egységes lett. A **nagyhatalmak** a világ nagy részét gyarmatként vagy befolyással uralták. ==A versengésük két szövetséget hozott létre – ebből lett 1914-ben a világháború.== Az eszmék vitája a 20. században folytatódott.

### Feliratok
- n9 cím: Az 1914-es világ egy képen
- n9 k1: nemzetállam
- n9 k1 sub: egy nemzet – egy állam (1871: Németország)
- n9 k2: nagyhatalom
- n9 k2 sub: hat európai + USA, Japán
- n9 k3: gyarmatbirodalom
- n9 k3 sub: a szárazföld kb. # %-a
- n9 k4: eszmék
- n9 k4 sub: liberalizmus, konzervativizmus, szocializmus
- n9 tovább: → tovább: a dualizmus kora (02), az első világháború (03)
- ö 1815: Német Szövetség
- ö 1848: Kommunista kiáltvány
- ö 1861: Olasz Királyság
- ö 1871: Német Császárság
- ö 1882: hármas szövetség
- ö 1907: antant
- ö 1914: világháború

### Adatok
<!-- forrás (az alábbiakra): az első világháború kitörése (Ausztria–Magyarország hadüzenete Szerbiának): 1914. július 28.
     (szokásos kronológia; a 03-elso-vilaghaboru lecke részletezi). -->
- világháború: 1914. július 28.

<!-- Vitatott / bizonytalan pontok:
  – A Német Szövetség tagjainak száma a dátumtól függ: 1815. június 8-án 39 állam írta alá, szeptemberre (Baden,
    Württemberg) 41, 1817-ben Hessen-Homburggal 41, később összeolvadások miatt csökkent (1866: 34; en.wikipedia
    „German Confederation”). A lecke az alapításkori 39-et mutatja.
  – A 2–3. lépés térképe vázlat: a Német Szövetség és Poroszország határa mai tartományokból összerakott
    közelítés (lásd a fejléc megjegyzését) – a tanár atlasszal vesse össze (Pfalz, Hessen, Oldenburg,
    Braunschweig, Mecklenburg, Előpomeránia, Schleswig). A schleswig-holsteini háború (1864) a térképen nem
    szerepel; Schleswig-Holstein a porosz annexióval (1866) együtt lesz porosz.
  – Olaszország egyesítése: a térkép csak a kész államot (1870, Rómával) mutatja; a fokozatos egyesítést (1859–60,
    1861, Velence 1866, Róma 1870) az idővonal adja. Trieszt, Trento és Dél-Tirol 1914-ben Ausztriáé.
  – Gyarmati adatok (Hübner 1914, Lenin közlésében): a gyarmati népesség nagyrészt becslés. A „gyarmat” kategória
    Oroszországnál vitatható (a táblázat Közép-Ázsiát, a Kaukázust és Szibéria egy részét veszi „gyarmatnak”), az
    USA-nál a Fülöp-szigetek, Puerto Rico, Hawaii és Alaszka a „gyarmat”. Más összesítésekben a német gyarmatok
    területe kb. 2,6–3,0 millió km² (nem ellenőriztük forrásonként).
  – „A szárazföld kb. 61 %-a” a táblázat saját összesítőjéből számolt (81,5 : 133,9). A szakirodalomban gyakori
    „84 %” (D. K. Fieldhouse) más kategóriát (befolyási övezeteket és volt gyarmatokat is) számol – a lecke nem
    használja.
  – A világtérkép mai országokkal közelít (lásd a fejlécet); a befolyási övezetek (Perzsia, Kína, az Oszmán
    Birodalom) sraffozással, Lenin „félgyarmat” kategóriája szerint.
  – Az eszme-kártyák parafrázisok, a 19. századi szerzők gondolatainak egyszerűsítései. Az eszmék ennél
    sokszínűbbek (pl. a liberalizmuson belül is vita volt a választójogról). A „kommunizmus” itt a Kiáltvány
    eszméje, nem a 20. századi diktatúrák (05-diktaturak).
  – A Brit Birodalom összesen-népességének „444,0” értéke a marxists.org angol kiadásában elírás (440,0 a helyes, a
    táblázat saját összesítője szerint) – hogy az eredeti Hübner-kiadásban vagy Lenin kéziratában is így áll-e,
    nem ellenőriztük.
-->
