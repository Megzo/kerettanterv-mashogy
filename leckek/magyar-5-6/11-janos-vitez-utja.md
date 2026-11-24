# Határos-e India és Franciaország? – János vitéz útja
tantárgy: Magyar nyelv és irodalom · évfolyam: 5–6. · témakör: 10. Petőfi Sándor: János vitéz

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/magyar-5-6/11-janos-vitez-utja.md

  A mű 27 fejezete (1–27) a lecke „egységei”: a fejezet-csúszka, a sáv és a görbe is ezekre épül.
  Fejezettartomány így írható: 8–17 (nagykötőjel).
  „Jancsi útja”: hol van a hős az egyes fejezetek VÉGÉN (1–27), vesszővel. Csak ezek a helynevek állhatnak benne:
    falu, puszta, erdő, huszárok, Tatárország, Taljánország, Lengyelország, India, Franciaország, tenger,
    Óriásország, Sötétség, temető, Óperencia, Tündérország
  Az idézett sorok (### Idézet) betűhűen a MEK 01010 szövegéből valók; a | a sormetszet helye (a leckében nem
  látszik). A build megszámolja a szótagokat, és hibát ad, ha egy „jv” sor nem 12 szótagos.
  Feliratban a # jel helyére a lecke számot (vagy szót) ír.
  Ha a lecke egy sort nem tud értelmezni, a vászon alján piros sáv jelzi.

  A valódi útvonal: az állomások egy-egy jellemző pontja (alább, koordinátával) között légvonalban (gömbi főkörön)
  mérve. Az „út hossza” és a két másik távolság becslés: a lecke a koordinátákból újraszámolja, és szól, ha a
  szám nem egyezik (3 % tűrés). A mesetérkép saját rajz; az állomások helye rajta a kódban van.
  Térképadat: Natural Earth (közkincs, „Made with Natural Earth”).
-->

## Közös

### Feliratok
- fejezet csúszka: Fejezet
- mese csúszka: Valóság → mese
- valóság felirat: valóság
- mese felirat: mese
- mérő cím: Mennyire mesés?
- olvasat bélyeg: egy lehetséges olvasat
- vázlatos bélyeg: vázlatos
- becslés bélyeg: becslés
- mai határok bélyeg: mai határok
- régi írásmód bélyeg: régi írásmód
- adathiba felirat: Ellenőrizd a .md-t: #
- fejezet felirat: #. fejezet
- megtett út felirat: a huszárok útja légvonalban
- km felirat: # km
- mesetérkép cím: A MESE TÉRKÉPE
- Jancsi név: Kukoricza Jancsi
- János név: János vitéz
- falu név: a falu
- falu sub: a műben nincs neve
- puszta név: puszta
- erdő név: erdő
- huszárok név: huszárok
- Tatárország név: Tatárország
- Tatárország sub: a Krím? A hely bizonytalan.
- Taljánország név: Taljánország
- Taljánország sub: Itália (Róma)
- Lengyelország név: Lengyelország
- Lengyelország sub: Varsó
- India név: India
- India sub: Delhi
- Franciaország név: Franciaország
- Franciaország sub: Párizs
- tenger név: tenger
- Óriásország név: Óriások országa
- Sötétség név: a sötétség országa
- temető név: temető
- Óperencia név: Óperenciás-tenger
- Tündérország név: Tündérország
<!-- A fejezetek rövid tartalma: saját összefoglaló (a fejezeteknek nincs címe, csak sorszáma). -->
- fejezet 1: Jancsi és Iluska a patakparton
- fejezet 2: A mostoha szidja Iluskát
- fejezet 3: Elvész a nyáj, a gazda elkergeti Jancsit
- fejezet 4: Búcsú Iluskától, Jancsi elindul
- fejezet 5: A pusztán vihar éri
- fejezet 6: Zsiványtanya az erdőben
- fejezet 7: Jancsi huszárnak áll
- fejezet 8: Tatárország, kutyafejű tatárok
- fejezet 9: Taljánország, örökös tél
- fejezet 10: Lengyelország, India, Franciaország
- fejezet 11: A bujdosó francia király
- fejezet 12: Csata a törökkel, a királylány
- fejezet 13: Lakoma; az új név: János vitéz
- fejezet 14: János elmeséli élete történetét
- fejezet 15: Búcsú, egy zsák arany, hajóra száll
- fejezet 16: Hajóúton, gondolatban otthon
- fejezet 17: Vihar, felhő, griffmadár – haza
- fejezet 18: Iluska sírja, a rózsa
- fejezet 19: Az óriások földjének csősze
- fejezet 20: Az óriások királya
- fejezet 21: A sötétség országa, boszorkányok
- fejezet 22: Éjjel a temetőben
- fejezet 23: Az Óperenciás-tenger partján
- fejezet 24: Egy óriás átviszi a tengeren
- fejezet 25: Tündérország három kapuja
- fejezet 26: Tündérország, az örök tavasz
- fejezet 27: Az élet vize, Iluska
<!-- Hol van a hős az egyes fejezetek végén (1–27). A 7. fejezet: „hetedhét országon túl” találkozik a huszárokkal. -->
- Jancsi útja: falu, falu, falu, puszta, puszta, erdő, huszárok, Tatárország, Taljánország, Franciaország, Franciaország, Franciaország, Franciaország, Franciaország, tenger, tenger, falu, falu, Óriásország, Óriásország, Sötétség, temető, Óperencia, Tündérország, Tündérország, Tündérország, Tündérország

### Adatok
<!-- A mű terjedelme: MEK 01010, gépi számolással: 27 fejezet, 370 versszak, 1480 sor (lásd a 10-janos-vitez-vers leckét). -->
- fejezetek száma: 27
<!-- Az állomások jellemző pontjai (becslés, a mű nem ad helyet). A falu: a Kiskunság (Kiskunfélegyháza, ahol Petőfi
     gyermekkorát töltötte) – csak jelképes hely, a műben a falunak nincs neve. Tatárország: a Krím közepe (a krími
     tatárok földje; a mű „Tatárországa” mesei ország, a hely bizonytalan). Taljánország: Róma. Lengyelország: Varsó.
     India: Delhi. Franciaország: Párizs. Koordináták: kerekítve, a városközpontok (hu.wikipedia). -->
- falu helye: 46,71° É, 19,85° K
- Tatárország helye: 45,00° É, 34,10° K
- Taljánország helye: 41,90° É, 12,50° K
- Lengyelország helye: 52,23° É, 21,01° K
- India helye: 28,61° É, 77,21° K
- Franciaország helye: 48,86° É, 2,35° K
<!-- Gömbi főkörön, R = 6371 km: falu → Krím 1118 km, Krím → Róma 1772 km, Róma → Varsó 1315 km, Varsó → Delhi
     5264 km, Delhi → Párizs 6587 km; összesen 16 056 km. A lecke ugyanezt számolja a koordinátákból. -->
- az út hossza: kb. 16 000 km
<!-- A két ország legközelebbi pontja (Natural Earth 1:110m országhatárok, a Kasmír északnyugati csücske és Elzász
     között): kb. 5510 km. A lecke a térképadatból számolja. -->
- India és Franciaország távolsága: kb. 5500 km
<!-- falu (Kiskunfélegyháza) → Párizs légvonalban: 1326 km (Budapest → Párizs: 1244 km). -->
- falu és Párizs távolsága: kb. 1300 km
<!-- Az Egyenlítő hossza: 40 075 km. -->
- a Föld kerülete: kb. 40 000 km
<!-- Mennyire mesés a fejezet? 0 = minden a valóságban is lehetne, 10 = tündérmese. EGY LEHETSÉGES OLVASAT, nem mérés
     (a lecke is így jelöli). Fejezetenként, 1–27. -->
- mese-fok: 0; 0; 0; 0; 1; 2; 3; 7; 7; 9; 5; 5; 4; 1; 3; 3; 7; 1; 8; 9; 10; 9; 9; 10; 10; 10; 10

## 1. Egy falu, egy patak
A *János vitéz* **elbeszélő költemény**: versben mesél el egy történetet, {fejezetek száma} fejezetben. Egy falu szélén kezdődik. Minden ismerős: juhász, nyáj, patak, mostoha, puszta. Jancsi elveszti a nyáj felét, és a gazdája elkergeti. ==Hová vezet az útja?==

<!-- idézet: Petőfi Sándor: János vitéz (1844), 1. fejezet 6. sor, 5. fejezet 2. sor · szöveg: MEK 01010 (mek.oszk.hu/01000/01010), letöltve 2026-11-24; összevetve: Petőfi Sándor összes költeményei, Athenaeum, negyedik népies kiadás (Project Gutenberg 41504) – ott: „fekütt” · szerző † 1849 · közkincs -->
### Idézet
- jv 1/6: Ugy legelteti a | nyájt a faluvégen.
- jv 5/2: A puszta, mint tenger, | feküdt körülötte;

### Feliratok
- jelképes felirat: A helyek jelképesek: a mű nem nevezi meg őket.

## 2. Huszárnak áll
Jancsi **huszárnak** áll. A sereg a franciák segítségére indul, mert a török megtámadta őket. Merre van Franciaország? Nyugatra. A huszárok mégis **keletre**, Tatárország felé indulnak! ==Itt válik el a mű földrajza a valóságtól.==

<!-- idézet: Petőfi Sándor: János vitéz (1844), 7. fejezet 23–24. sor (a 23–24. sor a huszárvezér szavai; a záró idézőjelet a lecke elhagyja) · szöveg: MEK 01010, letöltve 2026-11-24; összevetve: Athenaeum, negyedik népies kiadás (Project Gutenberg 41504) – ott: „Rá rontott”, „franczia”, „Francziáknak” · szerző † 1849 · közkincs -->
### Idézet
- jv 7/23: Rárontott a török | a francia népre;
- jv 7/24: Franciáknak megyünk | mi segedelmére.

### Feliratok
- légvonal felirat: Párizs légvonalban: #
- kelet felirat: A huszárok keletnek indulnak!
- hetedhét felirat: „hetedhét országon túl”: mesei kifejezés

## 3. Tatárország, Taljánország
**Tatárországban** kutyafejű tatárok élnek, **Taljánországban** (Itáliában) örökös tél van. A nevek valódiak, a leírás mesés. Kattints két állomásra, és mérd le, milyen messze vannak! ==A számláló a megtett utat mutatja.==

> megjegyzés: A *talján* régi szó: olasz.

<!-- idézet: Petőfi Sándor: János vitéz (1844), 8. fejezet 4. sor, 9. fejezet 7. sor · szöveg: MEK 01010, letöltve 2026-11-24; összevetve: Athenaeum, negyedik népies kiadás (Project Gutenberg 41504), egyezik · szerző † 1849 · közkincs -->
### Idézet
- jv 8/4: Látott érkezni sok | kutyafejű tatárt.
- jv 9/7: Mert Taljánországban | örökös tél vagyon;

### Feliratok
- a műben felirat: a műben:
- valóságban felirat: valójában:
- Tatárország műben: kutyafejű tatárok
- Tatárország valóság: a krími tatárok földje
- Taljánország műben: örökös tél
- Taljánország valóság: enyhe, mediterrán tél
- mérd le felirat: Kattints két állomásra: lemérem!
- mérés felirat: # légvonalban

## 4. India és Franciaország határos?
A mű szerint **„Franciaország és India határos”**. A valóságban legközelebbi pontjaik is {India és Franciaország távolsága}-re vannak. Az egész út légvonalban {az út hossza} lenne. Húzd a csúszkát a **mese térképe** felé!

> értelmezés: Petőfi nem tévedett: játszik. A valódi nevek a mese földjére kerülnek.

<!-- idézet: Petőfi Sándor: János vitéz (1844), 10. fejezet 3. és 20. sor · szöveg: MEK 01010, letöltve 2026-11-24; összevetve: Athenaeum, negyedik népies kiadás (Project Gutenberg 41504) – ott: „Francziaország” · szerző † 1849 · közkincs -->
### Idézet
- jv 10/3: Franciaország és | India határos,
- jv 10/20: Hát a csillagokban | a ló meg-megbotlott.

### Feliratok
- határos felirat: a műben: határos
- távolság felirat: a valóságban legalább #
- kerület felirat: a Föld kerületének kb. #-a
- hegyek felirat: a hegyek az égig érnek

## 5. Hősként haza – a griffmadár hátán
Jancsi legyőzi a törököket, és megmenti a francia királylányt. Itt kapja új nevét: **János vitéz**. A 14. fejezetben elmeséli élete történetét: ez **visszatekintés**. Hazaindul, de hajója elsüllyed. Egy felhő, majd egy **griffmadár** viszi haza.

<!-- idézet: Petőfi Sándor: János vitéz (1844), 17. fejezet 24. és 38. sor · szöveg: MEK 01010, letöltve 2026-11-24; összevetve: Athenaeum, negyedik népies kiadás (Project Gutenberg 41504), egyezik („grifmadár” mindkettőben) · szerző † 1849 · közkincs -->
### Idézet
- jv 17/24: Megkapta a felhőt | mind a két kezével.
- jv 17/38: És a grifmadárra | hirtelen rápattan,

### Feliratok
- csata felirat: csata a törökkel
- hajó felirat: hajó, vihar
- griff felirat: felhő, griffmadár
- visszatekintés felirat: visszatekintés: a 14. fejezet a múltról mesél
- új név felirat: 13. fejezet: új név

## 6. Iluska rózsája
Otthon szomorú hír várja: Iluska meghalt. Ez a történet nagy **fordulópontja**. János leszakítja a rózsát, amely a sírján nőtt, és magával viszi. ==Innen már nincs valódi hely a térképen.== Merre visz az út?

<!-- idézet: Petőfi Sándor: János vitéz (1844), 18. fejezet 38. és 43. sor · szöveg: MEK 01010, letöltve 2026-11-24; összevetve: Athenaeum, negyedik népies kiadás (Project Gutenberg 41504), egyezik · szerző † 1849 · közkincs -->
### Idézet
- jv 18/38: Egyszerű kis rózsa|bokor nevelkedett.
- jv 18/43: Vándorlok, vándorlok, | a világ végeig,

### Feliratok
- sír felirat: Iluska sírja
- rózsa felirat: a rózsa elkíséri
- fordulópont felirat: fordulópont

## 7. Óriások, boszorkányok, Óperencia
Az óriások földje, a sötétség országa, az **Óperenciás-tenger** és **Tündérország** csak a mese térképén létezik. Húzd a csúszkát a valóság felé: ezek a helyek eltűnnek! A tündérek tavában a rózsából újra Iluska lesz: ez az **élet vize**.

<!-- idézet: Petőfi Sándor: János vitéz (1844), 23. fejezet 30. sor, 27. fejezet 29. sor · szöveg: MEK 01010, letöltve 2026-11-24; összevetve: Athenaeum, negyedik népies kiadás (Project Gutenberg 41504) – ott: „óperencziás” · szerző † 1849 · közkincs -->
### Idézet
- jv 23/30: Az óperenciás | tenger ez, tudod-e?
- jv 27/29: Hát az élet vize | volt ez a tó itten,

### Feliratok
- nincs felirat: A valódi térképen nincs ilyen hely.
- élet vize felirat: az élet vize
- mese km felirat: itt már nincs mit lemérni

## 8. Összefoglaló: a valóságtól a meséig
Az út a valóságból indul, valódi nevű, de mesés országokon át vezet, és a mesében ér véget. Húzd a fejezet-csúszkát! Jelöld a görbén a **fordulópontokat**, aztán vesd össze! ==Szerinted hol kezdődik a mese?==

> megjegyzés: Más olvasó máshol látja a határt.

### Feliratok
- valóság név: valóság
- mesés földrajz név: valódi nevek, mesés földrajz
- otthon név: otthon
- tündérmese név: tündérmese
<!-- Egy lehetséges besorolás (fejezetek). Más is védhető: pl. a mese már a 7. fejezetben kezdődik („hetedhét
     országon túl”), vagy csak a 19.-ben (óriások). A lecke a diák jelölését nem pontozza. -->
- valóság fejezetei: 1–7
- mesés földrajz fejezetei: 8–17
- otthon fejezetei: 18
- tündérmese fejezetei: 19–27
<!-- A fordulópontok egy lehetséges olvasata: fejezet, majd a rövid név. -->
- fordulópont 1: 3
- fordulópont 1 név: elkergetik
- fordulópont 2: 13
- fordulópont 2 név: János vitéz lesz
- fordulópont 3: 18
- fordulópont 3 név: Iluska sírja
- fordulópont 4: 27
- fordulópont 4 név: az élet vize
- összevet gomb: Összevetem
- újra gomb: Újrakezdem
- jelöld felirat: Kattints a görbén a fordulópontokra!
- egyezik felirat: Egyezik: # – egy lehetséges olvasat is így látja.
- más felirat: Te ezt is jelölted: # – mi szól mellette?
- kimaradt felirat: Egy lehetséges olvasat ezt is jelöli: #
- hiányzik felirat: Előbb jelölj legalább egy fejezetet!
- mesefok felirat: mennyire mesés? (egy olvasat)

<!-- Vitatott / bizonytalan pontok (tanári review):
  - Szövegforrás: MEK 01010 (a mai iskolai kiadásoktól eltérő, régies írásmód: Ugy, Kukoricza, grifmadár). Második kiadás:
    Petőfi Sándor összes költeményei, Athenaeum, negyedik népies kiadás (Project Gutenberg 41504); eltérések az idézett
    sorokban: „fekütt” (5/2), „Rá rontott”, „franczia”, „Francziáknak” (7/23–24), „Francziaország” (10/3), „óperencziás”
    (23/30). A kritikai kiadást nem néztük.
  - A 7/23–24. sor a huszárvezér szavai; a MEK-ben a 24. sor végén záró idézőjel áll, a lecke ezt elhagyja (a lecke a
    sort saját idézőjelbe teszi).
  - A falu neve a műben nem szerepel (a teljes szövegben keresve). A térképen jelképes hely az Alföldön (Kiskunság);
    a puszta, az erdő és a huszárokkal való találkozás helye is jelképes („vázlatos” bélyeg).
  - Tatárország helye bizonytalan: a lecke a Krímet veszi (a krími tatárok földje); a mű kutyafejű tatárjai és a
    szerecsen király (8. fejezet) mesei elemek. Taljánország = Itália (talján: régi szó, olasz). A lecke az állomásokat
    egy-egy városhoz köti (Róma, Varsó, Delhi, Párizs) – ez becslés, a mű városokat nem nevez meg.
  - A valódi országok foltjai MAI határok („mai határok” bélyeg). 1844-ben Lengyelország nem volt önálló állam
    (felosztva), Itália nem volt egységes, Indiát a brit Kelet-indiai Társaság uralta – a lecke ezt nem mondja ki.
  - A távolságok gömbi főkörön, R = 6371 km: 16 056 km (falu → Krím → Róma → Varsó → Delhi → Párizs); a lecke
    „kb. 16 000 km”-t mond, „becslés” bélyeggel. A valódi lovas út ennél jóval hosszabb volna. India és Franciaország
    legközelebbi pontja a Natural Earth 1:110m határai szerint kb. 5510 km (a vitatott Kasmír Indiához számítva; nélküle
    több). A Föld kerülete (Egyenlítő): 40 075 km → az út kb. 40%-a.
  - Taljánország a valóságban: „enyhe, mediterrán tél” – Itália nagy része mediterrán éghajlatú; az Alpokban van
    tartós hó. A Krím: a krími tatárok földje volt (Krími Kánság, 1783-tól orosz uralom alatt).
  - A „mennyire mesés?” értékek (0–10) és a szerkezeti szakaszok (valóság / mesés földrajz / otthon / tündérmese)
    értelmezés, nem mérés: a lecke „egy lehetséges olvasat” bélyeggel mutatja, a diák jelölését nem pontozza.
  - A fordulópontok (3., 13., 18., 27. fejezet) egy lehetséges olvasat; a brief az elűzést, a francia királylányt,
    Iluska halálát, a rózsát és az élet vizét nevezi meg. Iluska halálhírét János a 17. fejezet végén hallja, a sír
    és a rózsa a 18.-ban van.
  - A 14. fejezet visszatekintés: János a francia királynak meséli el gyermekkorát és Iluskát (13. fejezet vége – 14.).
  - Jankovics Marcell rajzfilmje (1973) védett: a lecke nem mutat belőle képet, és nem említi.
  - A fejezetösszefoglalók saját szövegek. A mesetérkép saját rajz, nem méretarányos.
-->
