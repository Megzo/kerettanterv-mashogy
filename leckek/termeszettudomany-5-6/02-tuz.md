# Miért kell lehajolni a füstben? – a levegő tulajdonságai és a tűz
tantárgy: Természettudomány · évfolyam: 5–6. · témakör: 1. Anyagok és tulajdonságaik

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/termeszettudomany-5-6/02-tuz.md

  A „Tippelj!” lépésekben (2., 7.) a panel első bekezdése a kérdés; a többi bekezdés
  elmosódva látszik, és csak a tipp után válik olvashatóvá (a megoldás addig rejtve marad).
  A ## Közös feliratai: a „Tippelj! → kísérlet → magyarázat” sáv, a tipp-visszajelzés és a
  kísérlet-bélyegek (szerződés 17.) – a sorozat minden leckéjében ugyanígy szerepelnek.

  A lecke tűzvédelmi tartalma szakmai lektorálást kér (lásd a fájl végét).
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kísérlet
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- nagyítás felirat: nagyítás · szemléltetés
- otthon bélyeg: otthon is kipróbálhatod
- felnőtt bélyeg: felnőttel együtt
- tilos bélyeg: NE PRÓBÁLD KI
- modell bélyeg: modell
- kitalált bélyeg: kitalált példa
- levegő felirat: levegő
- víz felirat: víz

### Adatok
- légnyomás: 1013 hPa
<!-- forrás: közismert – a normál légnyomás a tengerszinten 1013,25 hPa; átvéve: fizika-7-8/06-halmazallapot („normál légnyomás: 1013 hPa”) -->
- nehézségi gyorsulás: 9,81 m/s²
<!-- forrás: közismert (Magyarországon kb. 9,81 m/s²); a lecke ezzel számolja a légnyomás „kilogrammját” és a víz nyomását -->

## 1. Üres-e az üres pohár?
A pohár alján papírzsebkendő van. Szájával lefelé a víz alá nyomjuk. ==Bemegy a víz?==

Alig! A pohárban **levegő** van, és az helyet foglal. A zsebkendő száraz marad. Billentsd meg a poharat: a levegő buborékban kiszáll, és a helyére víz megy.

> megjegyzés: Próbáld ki egy tál vízben!

### Feliratok
- mélység csúszka: Ennyire nyomd le
- billentés gomb: Billentsd meg
- újra pohár gomb: Újra
- zsebkendő felirat: papírzsebkendő
- száraz felirat: száraz
- vizes felirat: elázott
- bejut felirat: a víz csak # mm-re megy be
- mélység felirat: a pohár szája # cm mélyen
- buborék felirat: kiszáll a levegő
- üres tévhit felirat: Üres a pohár?
- üres válasz felirat: Nem: levegő van benne!

### Adatok
- pohár magassága: 10 cm
<!-- forrás: kitalált példa (egy szokásos vizespohár) -->
- víz sűrűsége: 1000 kg/m³
<!-- forrás: közismert (szobahőmérsékletű víz: 998 kg/m³, kerekítve) -->
- legnagyobb mélység: 20 cm
<!-- forrás: kitalált példa (egy mély tál, a csúszka felső értéke). A lecke a Boyle–Mariotte-törvénnyel
     számolja, mennyi víz megy be: 20 cm mélyen kb. 1,9 mm (10 cm-es pohár, 1013 hPa) – L.checks. -->

## 2. Mennyit nyom a terem levegője?
A levegő könnyű, de egy tanteremben sok van belőle. ==Mennyi lehet a tömege? Tippelj!==

1 m³ levegő tömege kb. {köbméternyi levegő tömege}. Húzd a csúszkákat! A levegő ránk is nehezedik: ez a **légnyomás**. ==Minden cm²-ünkre kb. 1 kg-nyi levegő nyom.==

### Feliratok
- tömeg kérdés felirat: Mennyi a tanterem levegőjének tömege?
- kettő tipp: kb. 2 kg
- húsz tipp: kb. 20 kg
- kétszáz tipp: kb. 200 kg
- hossz csúszka: A terem hossza
- szélesség csúszka: A terem szélessége
- magasság csúszka: A terem magassága
- méret felirat: # m
- térfogat felirat: térfogat: # m³
- tömeg felirat: a levegő tömege: kb. # kg
- titok felirat: a levegő tömege: ? kg
- zsák felirat: annyi, mint # zsák krumpli
- zsák alcím felirat: egy zsák: #
- négyzetcenti felirat: 1 cm²
- légoszlop felirat: a levegő a légkör tetejéig
- nyomás felirat: kb. # kg-nyi levegő nyomja

### Adatok
- köbméternyi levegő tömege: 1,20 kg
<!-- forrás: közismert táblázati érték – a levegő sűrűsége 20 °C-on, 1013 hPa-n 1,204 kg/m³; vö. fizika-7-8/01-suruseg (1,2 kg/m³) -->
- terem hossza: 9 m
<!-- forrás: kitalált példa (egy átlagos tanterem) -->
- terem szélessége: 7 m
<!-- forrás: kitalált példa -->
- terem magassága: 3 m
<!-- forrás: kitalált példa. 9 · 7 · 3 = 189 m³ → 189 · 1,20 = 227 kg; a lecke számolja (L.checks) -->
- krumpliszsák tömege: 25 kg
<!-- forrás: közismert – a burgonyát gyakran 25 kg-os zsákban árulják (10 kg-os is van) -->

## 3. Melegen kitágul
A palack nyakára lufit húztunk, és meleg vízbe tesszük. Húzd a csúszkát! A levegő **melegen kitágul**: több helyet foglal, ezért felfújja a lufit. A nagyítóban a részecskék gyorsabban mozognak, és távolabb kerülnek egymástól.

> megjegyzés: Forró vízhez kérj meg egy felnőttet!

### Feliratok
- vízhőmérséklet csúszka: A víz hőmérséklete
- palack felirat: palack
- lufi felirat: lufi
- meleg víz felirat: meleg víz: #
- térfogat lufi felirat: a levegő térfogata: #
- nőtt felirat: # %-kal több
- lufi gumi felirat: a lufi gumija enged

### Adatok
- levegő a palackban: 500 cm³
<!-- forrás: kitalált példa (fél literes palack, 20 °C-on) -->
- kiinduló hőmérséklet: 20 °C
<!-- forrás: kitalált példa (szobahőmérséklet) -->
- legmelegebb víz: 60 °C
<!-- forrás: kitalált példa (a csúszka felső értéke). Állandó nyomáson a gáz térfogata a kelvinben mért
     hőmérséklettel arányos: 333,15 / 293,15 = 1,137 → kb. 14 %-kal több, 500 cm³ → 568 cm³ (L.checks) -->
- abszolút nulla fok: −273,15 °C
<!-- forrás: közismert (0 K); a diákok nem látják, a lecke ezzel számol (7. osztályban tanulják) -->

## 4. A meleg levegő felszáll
Egy köbméter meleg levegő könnyebb, mint egy köbméter hideg. Ezért a meleg levegő **felszáll**, a hideg lesüllyed. A radiátor fölött felszáll, az ablaknál lehűl és leszáll. ==Fent melegebb van, mint lent.== Kapcsold ki a fűtést!

### Feliratok
- fűtés ki gomb: Kapcsold ki a fűtést
- fűtés be gomb: Kapcsold be a fűtést
- radiátor felirat: radiátor
- ablak felirat: hideg ablak
- mennyezet felirat: a mennyezet alatt: #
- padló felirat: a padlónál: #
- köbméter felirat: 1 m³ levegő, #
- köbméter tömeg felirat: #
- könnyebb felirat: a meleg levegő könnyebb
- melegebb felirat: meleg levegő
- hidegebb felirat: hideg levegő

### Adatok
- hőmérséklet a mennyezet alatt: 24 °C
<!-- forrás: kitalált példa (fűtött szoba; a valóságban a fűtéstől, a szoba magasságától függ) -->
- hőmérséklet a padlónál: 19 °C
<!-- forrás: kitalált példa -->
- meleg levegő hőmérséklete: 60 °C
<!-- forrás: kitalált példa (a radiátor fölött felszálló levegő). A lecke a 20 °C-os levegő tömegéből
     számolja: 1,20 kg · 293,15 / 333,15 = 1,06 kg (L.checks) -->

## 5. Mi kell a tűzhöz?
Az égéshez három dolog kell: **éghető** anyag, oxigén és elég nagy hő. Az oxigén a levegő kb. ötöde. Ami nem ég el, az **éghetetlen**. Húzd a kártyákat a helyükre!

> megjegyzés: A láng jelű címke jelentése: tűzveszélyes.

### Feliratok
- háromszög cím felirat: Ez a három kell a tűzhöz
- éghető anyag felirat: éghető anyag
- oxigén felirat: oxigén (a levegőből)
- hő felirat: elég nagy hő
- összetétel cím felirat: Miből áll a levegő?
- nitrogén sáv felirat: nitrogén: #
- oxigén sáv felirat: oxigén: #
- egyéb sáv felirat: egyéb: #
- ötöd felirat: az oxigén a levegő kb. ötöde
- tűzveszélyes felirat: tűzveszélyes anyag jele
- éghető zóna felirat: éghető
- éghető alcím felirat: meggyulladhat
- éghetetlen zóna felirat: éghetetlen
- éghetetlen alcím felirat: nem ég el
- papír kártya: papír
- fa kártya: fa
- gyertya kártya: gyertya
- benzin kártya: benzin
- homok kártya: homok
- kő kártya: kő
- üveg kártya: üveg
- víz kártya: víz
- szög kártya: vasszög
- megoldás tűz gomb: Mutasd a megoldást
- jó helyen felirat: # / # jó helyen

### Adatok
<!-- forrás (az alábbiakra): száraz levegő összetétele térfogat szerint, a tengerszinten – NOAA / CRC Handbook
     („U.S. Standard Atmosphere”); átvéve: kemia-7-8/11-levego. A CO₂: NOAA GML, Mauna Loa, 2025. évi átlag
     427,35 ppm (lekérdezve: 2026-11-24), ugyanott. -->
- nitrogén aránya: 78,08 %
- oxigén aránya: 20,95 %
- argon aránya: 0,93 %
- szén-dioxid aránya: 0,0427 % (2025, frissítendő)

## 6. Veszély a konyhában
Ha ég az olaj a serpenyőben, ==soha ne önts rá vizet!== A víz lesüllyed, és a forró olajban egy pillanat alatt **gőzzé** válik. A gőz {gőz térfogataránya}-szor több helyet foglal, és kifröccsenti az égő olajat. Helyette: fedőt rá!

### Feliratok
- víz gomb: Mi lesz, ha víz kerül rá?
- fedő gomb: Mit tegyél helyette?
- olaj felirat: forró olaj
- csepp felirat: vízcsepp
- gőz felirat: gőz
- olaj lépés 1 felirat: 1. a víz lesüllyed: nehezebb az olajnál
- olaj lépés 2 felirat: 2. gőzzé válik: kb. #-szor több hely
- olaj lépés 3 felirat: 3. kifröccsenti az égő olajat
- helyette felirat: Helyette:
- helyes 1 felirat: fedőt rá – nem jut hozzá levegő
- helyes 2 felirat: kapcsold le a tűzhelyet
- helyes 3 felirat: szólj egy felnőttnek
- helyes 4 felirat: ha nem alszik el: ki, és 112
- olaj tévhit felirat: Égő olajat vízzel oltsunk?
- olaj válasz felirat: Soha! A gőz szétszórja az égő olajat.
- vázlat felirat: vázlat – a valóságban sokkal veszélyesebb

### Adatok
- gőz térfogataránya: kb. 1700
<!-- forrás: átvéve a kemia-7-8/09-eges-korrozio leckéből: 1 g víz 100 °C-os, 1013 hPa nyomású gőzként
     kb. 1,70 dm³ (ideális gáz) → kb. 1700-szoros térfogat (becslés: 1600–1700-szoros, a kiinduló víz
     hőmérsékletétől függ); vö. fizika-7-8/06-halmazallapot („1 liter vízből kb. 1700 L vízgőz”).
     A helyes cselekvés forrása: BM Országos Katasztrófavédelmi Főigazgatóság, „A lakástüzekkel kapcsolatos
     tennivalók és lakástüzek megelőzésének lehetőségei” (csongrad.katasztrofavedelem.hu, 2019-09,
     lekérdezve: 2026-11-24): „Sok esetben az égő olajat vízzel próbálják oltani az emberek, mivel a víz
     sűrűbb az olajnál, az az edény aljára süllyed. A forró olaj hatására a vízből pillanatok alatt gőz
     keletkezik […] és robbanásszerűen »kivetődik« az edényből. Ilyenkor a megoldás, hogy egy fedővel kell
     letakarni az edényt és ki kell várni, amíg a tűz magától elalszik.” -->
- olaj sűrűsége: 0,92 g/cm³
<!-- forrás: közismert táblázati érték (étolaj kb. 0,91–0,93 g/cm³); a víz (1 g/cm³) ennél nehezebb, ezért süllyed le -->

## 7. Ha tűz van: lehajolva ki!
Füstös a szoba. ==Hol tisztább a levegő? Tippelj!==

A forró füst felszáll, és felülről tölti meg a szobát. Lent tovább marad tisztább levegő. Ezért **lehajolva** menj ki! Csukd be magad mögött az ajtót: a füst nem jut utánad.

> megjegyzés: Modell: a valódi tűz gyorsabb is lehet.

### Feliratok
- füst kérdés felirat: Hol tisztább a levegő a füstös szobában?
- fent tipp: fent
- középen tipp: középen
- lent tipp: lent
- idő csúszka: Eltelt idő (modell)
- állva gomb: Állva
- lehajolva gomb: Lehajolva
- ajtó nyitva gomb: Ajtó nyitva
- ajtó csukva gomb: Ajtó becsukva
- füstforrás felirat: füstforrás
- szoba felirat: szoba
- folyosó felirat: folyosó, a kijárat felé
- forró füst felirat: forró füst
- eltelt felirat: eltelt: # másodperc
- belélegzett felirat: amit belélegzel:
- tiszta felirat: tisztább levegő
- füstös felirat: füstös levegő
- sűrű felirat: sűrű füst – veszélyes!
- fejmagasság felirat: fejmagasság: #
- eléri felirat: a füst eléri a fejed – állva: # múlva, lehajolva: # múlva
- ajtó felirat: ajtó

### Adatok
- szoba magassága: 2,6 m
<!-- forrás: kitalált példa (lakószoba belmagassága) -->
- ajtó magassága: 2,0 m
<!-- forrás: kitalált példa (szokásos beltéri ajtó kb. 2,0–2,1 m) -->
- fej magassága állva: 1,4 m
<!-- forrás: becslés – egy 10–12 éves gyerek kb. 1,4–1,55 m magas, az orra–szája kb. 10–15 cm-rel lejjebb van -->
- fej magassága lehajolva: 0,5 m
<!-- forrás: becslés (négykézláb, lehajtott fejjel) -->
- füst süllyedési ideje: 60 s (modell)
<!-- forrás: modell – a füstréteg alja ennyi idő alatt teszi meg az út kb. kétharmadát (exponenciális
     közeledés; a valódi tűzben a bútorok, a szellőzés, az ablak és az ajtó mindent megváltoztat).
     Katasztrófavédelmi tájékoztató: „Lakástűz esetén csak percek állnak a lakók rendelkezésére” (Fejér
     Vármegyei Katasztrófavédelmi Igazgatóság, Lakástüzes kiállítás 2025, lekérdezve: 2026-11-24). -->
- legalsó füstszint: 0,3 m (modell)
<!-- forrás: modell – a lecke idősávjában (3 perc) a füst nem éri el teljesen a padlót; a valóságban végül
     az egész szobát megtöltheti -->

## 8. Összefoglalás: levegő, tűz, menekülés
A levegő helyet foglal, tömege van, melegen kitágul és felszáll – a forró füst is. ==Ha tűz van: szólj, lehajolva menj ki, csukd be az ajtót, kint hívd a 112-t!== Ne bújj el, ne lifttel menj!

> megjegyzés: 7. osztályban a kémiában az oltásról is tanulsz.

### Feliratok
- levegő cím felirat: A levegő…
- tulajdonság 1 felirat: helyet foglal
- tulajdonság 2 felirat: tömege van, nyom
- tulajdonság 3 felirat: melegen kitágul
- tulajdonság 4 felirat: melegen felszáll
- teendő cím felirat: Ha tűz van
- teendő 1 felirat: Kiabálj, szólj mindenkinek!
- teendő 2 felirat: Lehajolva menj ki!
- teendő 3 felirat: Csukd be magad mögött az ajtót!
- teendő 4 felirat: Lépcsőn menj, ne lifttel!
- teendő 5 felirat: Kint hívd a 112-t!
- teendő 6 felirat: Ne menj vissza!
- segélyhívó felirat: 112
- segélyhívó alcím felirat: ingyenes segélyhívó
- bújás tévhit felirat: Elbújjak az ágy alá?
- bújás válasz felirat: Ne! Oda is beér a füst – menj ki!

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a 10 cm-es pohár és a tál (1.), a 9 m × 7 m × 3 m-es tanterem (2.), az 500 cm³-es palack
    (3.), a szoba hőmérsékletei (4.), a szoba és az ajtó mérete (7.). A vásznon „kitalált példa” bélyeg.
  - Modell-egyszerűsítések: a lufi (3.) nem feszül – a valóságban a gumi kicsit visszanyom, ezért a lufi
    kevésbé nő. A nagyítóban a részecskék sebességének különbsége felnagyított (szemléltetés): 20 és 60 °C
    között a valódi átlagsebesség csak kb. 7 %-kal nő. A szoba áramlása (4.) egy zárt örvény, a pöttyök
    csak díszítik. A füst (7.) a mennyezet alatt réteget alkot, amelynek alja egyenletesen közelít a padlóhoz
    (zárt képlet); az ajtó állása a modellben az egész idő alatt ugyanaz. A valódi tűz gyorsabb is lehet.
  - Az 1. lépésben a pohárba bejutó víz magasságát a lecke a Boyle–Mariotte-törvénnyel számolja (a levegő
    kicsit összenyomódik). Ezt 7–8. osztályban tanulják; itt csak az számít, hogy alig megy be víz.
  - A gyertyás kísérlet (pohár alá zárt gyertya) itt nem szerepel: az a tévhit, hogy a víz azért emelkedik,
    mert „elfogyott az oxigén”, a kemia-7-8/11-levego leckében cáfolódik.
  - A vasszög nem ég el a gyertyalángban, de a finom vasforgács vagy vaspor igen: a csillagszóró szikrái is
    égő vasszemcsék. Jó kérdés az osztálynak: miért számít, mennyire apróra van törve?
  - Kísérlet-bélyegek: üres pohár a víz alatt – „otthon is kipróbálhatod”; lufi a palackon, meleg vízben –
    „felnőttel együtt” (forró víz); víz az égő olajon – „NE PRÓBÁLD KI” (csak vázlat, a veszély oka).
  - Tűz esetén (források, lekérdezve: 2026-11-24):
    · BM OKF, „A lakástüzekkel kapcsolatos tennivalók…” (csongrad.katasztrofavedelem.hu): a tűzoltóságot a
      112-n kell értesíteni; tűz esetén a liftet ne használjuk, a menekülés mindig a lépcsőházon át
      történik (áramtalanításkor a lift megáll); égő olaj: fedő, víz soha.
    · BM OKF, „Tűzjelzés és alapvető tűzoltási tennivalók” (otb.katasztrofavedelem.hu, 2024-11): „lakástűz
      esetén a helyiségek és a lakás ajtóit, ablakait, lehetőleg csukjuk be távozáskor. Ez jelentős mértékben
      csökkenti a tűz, és a füst továbbterjedését” – a bejárati ajtót csukjuk be, de lehetőleg ne zárjuk
      kulcsra.
    · Fejér Vármegyei Katasztrófavédelmi Igazgatóság, Lakástüzes kiállítás 2025: „csak percek állnak a lakók
      rendelkezésére”; „A tűz kezdeti szakaszában általában először füst keletkezik. Ez a füst jelenti a
      legnagyobb veszélyt.” A füstérzékelő ezért életet menthet.
    · Lehajolva a füst alatt: U.S. Fire Administration (FEMA), gyerekeknek szóló tájékoztatók („get low and
      go”, „do not hide”, „once you are outside, do not go back inside”); Bundesamt für Bevölkerungsschutz
      (BBK, Németország): füstös helyiségben a padló mentén haladjunk. Magyar hivatalos, gyerekeknek szóló
      megfogalmazást a lektor adjon meg, ha van.
    · Segélyhívó: 112 (egységes, ingyenes), a tűzoltóság közvetlen száma: 105.
  - Nem szerepel (szándékosan): láng, égő ember, sérült; oltókészülék használata (felnőtt feladat); a
    tűzháromszög oltási oldalai (kemia-7-8/09-eges-korrozio).
-->

<!-- Szakmai ellenőrzés: tűzoltó vagy katasztrófavédelmi oktató (lektor), dátum: –, ajánlás verziója: – (még nincs lektorálva) -->
