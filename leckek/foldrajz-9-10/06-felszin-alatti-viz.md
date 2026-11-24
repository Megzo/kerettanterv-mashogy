# Hol van a Föld vize? – felszín alatti vizek, hévíz, karszt, belvíz
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 4. A vízburok

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/06-felszin-alatti-viz.md
  A számok az animációt is vezérlik: a vízgömbök átmérőjét és az 1000 literes tartály rekeszeit a
  vízkészlet-táblázatból (km³) számolja a lecke; a hőmérséklet a mélységgel a geotermikus gradiensből; a
  belvíz a csapadéktöbbletből és a hézagtérfogatból. A metszet domborzata valódi (ETOPO 2022), a rétegek
  rajza vázlatos (lásd a végén).
-->

## Közös

### Feliratok
- modell: modell
- vázlatos: vázlatos
- becslés: becslés
- torzítás: függőleges torzítás #×
- méretarányos: méretarányos
- magasság m: magasság (m)
- magasság km: magasság (km)
- km lépték: # km
- dél: D
- észak: É
- talaj: talaj
- homok: homok, kavics (víztartó)
- agyag: agyag (vízfogó)
- mészkő: mészkő
- üledék: homokos-agyagos medenceüledék
- talajvízszint: talajvízszint
- talajvíz: talajvíz
- rétegvíz: rétegvíz
- karsztvíz: karsztvíz
- hévíz: hévíz
- beszivárgás: beszivárgás
- folyó: folyó
- Alföld: Alföld
- Bükkalja: Bükkalja
- Bükk-fennsík: Bükk-fennsík
- forrás szelvény: Domborzat: NOAA ETOPO 2022, k. h. 20,5° (közkincs) · a rétegek vázlatosak
- forrás víz: Forrás: USGS Water Science School · Shiklomanov (1993), in: Gleick (szerk.): Water in Crisis

### Adatok
- domborzati szelvény: NOAA ETOPO 2022
<!-- forrás: NOAA NCEI ETOPO 2022 15″, shared/foldrajz/szelveny-alfold-bukk.js – délkör menti szelvény k. h. 20,5°-on, é. sz. 46,5° → 48,3° (lekérdezve: 2026-11-23, közkincs). A lecke a 96–200. km közötti részét mutatja (kb. é. sz. 47,4° – 48,3°: Tisza-vidék, Bükkalja, Bükk-fennsík). -->
- a talaj évi középhőmérséklete: kb. 11 °C
<!-- forrás: Magyarország évi középhőmérséklete kb. 10–11 °C (HungaroMet, éghajlati normál 1991–2020), közismert; a talaj néhány méter mélyen ehhez közeli, egész évben állandó hőmérsékletű – ellenőrizendő -->

## 1. Mennyi víz van a Földön?
Űrből nézve a Föld kék: a felszín {óceánok borítása}-át víz borítja. Mégis, ha ==a Föld összes vizét egy gömbbe gyűjtenénk==, az átmérője csak {összes víz gömbje} lenne. Az édes, folyékony vízé {édes folyékony víz gömbje}, a tavak és folyók édesvizéé {tavak és folyók gömbje}.

> megjegyzés: Forgasd meg a gömböt! Melyik gömb a mi vizünk?

### Feliratok
- kérdés 1: Mekkora gömb lenne a Föld összes vize?
- gömb összes: a Föld összes vize
- gömb édes: édes, folyékony víz
- gömb tavak: tavak és folyók édesvize
- átmérő: átmérő: #
- nagyítás: nagyítás: #×
- Magyarország fölött: Magyarország fölött
- borítás: a felszín #-a víz

### Adatok
<!-- forrás (az alábbiakra): USGS Water Science School, „Where is Earth's Water?” (táblázat), lekérdezve: 2026-11-24, közkincs (USA szövetségi mű); adatforrása: I. Shiklomanov (1993): World fresh water resources, in: P. H. Gleick (szerk.): Water in Crisis, Oxford University Press -->
- óceánok borítása: 71 %
<!-- forrás: közismert (a Föld felszínének kb. 70,8 %-a óceán és tenger) -->
- összes víz gömbje: kb. 1385 km
<!-- forrás: USGS Water Science School, „How much water is there on Earth?” – a teljes vízkészlet gömbje kb. 1385 km átmérőjű; a lecke a vízkészletből (1 386 000 000 km³) számolja és ellenőrzi: (6V/π)^(1/3) ≈ 1383 km -->
- édes folyékony víz gömbje: kb. 273 km
<!-- forrás: USGS (mint fent): a folyékony édesvíz (felszín alatti édesvíz + édesvizű tavak + folyók + mocsarak, kb. 10,6 millió km³) gömbje kb. 273 km; a lecke számolja és ellenőrzi -->
- tavak és folyók gömbje: kb. 56 km
<!-- forrás: USGS (mint fent): az édesvizű tavak és a folyók vize (93 120 km³) gömbje kb. 56 km; a lecke számolja és ellenőrzi -->
- Föld sugara: 6371 km
<!-- forrás: közepes Föld-sugár, közismert -->

## 2. Hol van az édesvíz?
Öntsük a Föld vizét egy **1000 literes** tartályba! Ebből {óceán literben} sós tengervíz. Az **édesvíz** csak {édesvíz literben}, és ennek kétharmada jég. ==A tavak és folyók édesvize alig 67 ml, a folyóké csak 1,5 ml.== Az édesvíz tehát nem kifogyhatatlan: a könnyen elérhető része parányi.

> megjegyzés: Tippeljetek előbb: hány liter édesvíz van az 1000 literben?

### Feliratok
- tartály cím: Ha a Föld összes vize 1000 liter lenne…
- oszlop 1: 1000 liter
- oszlop 2: nagyítva: ami nem tenger
- oszlop 3: nagyítva: a maradék
- oszlop 4: folyók cseppekben
- tenger: tenger, óceán
- jég: jég, állandó hó
- felszín alatti édes: felszín alatti (édes)
- felszín alatti sós: felszín alatti (sós)
- örök fagy: fagyott talaj
- édes tó: édesvizű tó
- sós tó: sós tó
- talajnedvesség: talajnedvesség
- légkör: légkör (pára)
- mocsár: mocsár
- folyók: folyók
- élőlények: élőlények
- liter: # l
- milliliter: # ml
- édesvíz zárójel: édesvíz: #
- csepp: # csepp ≈ #
- egy csepp: 1 csepp ≈ #

### Adatok
<!-- forrás (az alábbiakra): USGS Water Science School, „Where is Earth's Water?” – Shiklomanov (1993) táblázata, lekérdezve: 2026-11-24, közkincs. A literértékeket a lecke számolja: térfogat / összes × 1000 l. -->
- Föld vízkészlete: 1 386 000 000 km³
- óceánok vize: 1 338 000 000 km³
- jég és állandó hó: 24 064 000 km³
- felszín alatti édesvíz: 10 530 000 km³
- felszín alatti sós víz: 12 870 000 km³
- talajnedvesség térfogata: 16 500 km³
- fagyott talaj vize: 300 000 km³
- édesvizű tavak: 91 000 km³
- sós tavak: 85 400 km³
- légköri víz: 12 900 km³
- mocsarak vize: 11 470 km³
- folyók vize: 2120 km³
- élőlények vize: 1120 km³
- tartály: 1000 l
- óceán literben: kb. 965 l
<!-- forrás: 1 338 000 000 / 1 386 000 000 × 1000 = 965,4 l; a lecke számolja és ellenőrzi -->
- édesvíz literben: kb. 25 l
<!-- forrás: az USGS-táblázat édesvíz-részei (jég, felszín alatti édesvíz, talajnedvesség, fagyott talaj, édesvizű tavak, légkör, mocsár, folyók, élőlények) összesen 35 029 210 km³ = 2,5 % → 25,3 l; a lecke számolja és ellenőrzi -->
- egy csepp térfogata: 0,05 ml
<!-- forrás: közismert közelítés (kb. 20 csepp = 1 ml) -->

## 3. Talajvíz: víz a pórusokban
A föld alatt ==többnyire nincsenek tavak és folyók==: a víz a homokszemek közötti **pórusokban** van, mint a szivacsban. Fent a pórusokban levegő és víz van, lejjebb minden pórust víz tölt ki: ez a **talajvíz**. Felső határa a **talajvízszint** – az ásott kútban itt áll meg a víz.

> megjegyzés: Húzd lejjebb a nagyítót! Hol telnek meg a pórusok?

### Feliratok
- tévhit 3: föld alatti tó? Nem: vizes homok
- csúszka nagyító: A nagyító mélysége
- csúszka méter: # m
- nagyító cím: # m mélyen
- levegő: levegő
- víz: víz
- homokszem: homokszem
- agyagszemcse: agyagszemcse
- telítetlen: pórusokban levegő és víz
- telített: minden pórus tele vízzel
- ásott kút: ásott kút
- pórus arány: pórus a homokban: kb. #
- köbméter: 1 m³ vizes homokban kb. # víz

### Adatok
- talajvízszint mélysége: kb. 3 m
<!-- forrás: az alföldi talajvíz jellemzően 2–4 m mélyen van (OVF/HungaroMet talajvízszint-figyelő kutak; tankönyvi érték, közismert); a lecke ezt a szelvény egészén használja – modell -->
- homok hézagtérfogata: kb. 30 %
<!-- forrás: R. A. Freeze, J. A. Cherry: Groundwater (Prentice-Hall, 1979), 2.4 táblázat: homok 25–50 %, kavics 25–40 %, agyag 40–70 % – közismert tankönyvi értékek -->
- kezdő nagyítómélység: 1,5 m (modell)
<!-- forrás: a csúszka kezdőértéke -->

## 4. Víztartó és vízfogó réteg
A homok és a kavics jól átengedi a vizet: ez a **víztartó réteg**. Az agyag pórusai aprók, ==a víz alig jut át rajta==: ez a **vízfogó** (vízzáró) **réteg**. A két vízfogó réteg közé zárt víz a **rétegvíz**. Mit véd az agyag?

> megjegyzés: Engedd el a szennyezést! A mély kút az agyagréteg alól szív.

### Feliratok
- gomb szennyezés: Szivárog a szennyezés!
- gomb újra: Vissza: tiszta víz
- szennyezés: szivárgó szennyezés
- sekély kút: kút a talajvízből
- mély kút: kút a rétegvízből
- szennyezett: szennyezett
- tiszta: tiszta
- pórus agyag: agyag: kb. # pórus, mégis vízfogó
- vezetés: a homok kb. #-szor jobban vezeti a vizet
- áramlás: lassú áramlás a pórusokban

### Adatok
- agyag hézagtérfogata: kb. 50 %
<!-- forrás: Freeze–Cherry (1979), 2.4 táblázat: agyag 40–70 % -->
- homok és agyag vízvezetése: kb. 1 000 000
<!-- forrás: Freeze–Cherry (1979), 2.2 táblázat: a hidraulikus vezetőképesség homokban kb. 10⁻⁶–10⁻² m/s, agyagban kb. 10⁻¹²–10⁻⁹ m/s; tipikus értékekkel (10⁻⁴ és 10⁻¹⁰ m/s) kb. milliószoros a különbség – nagyságrendi becslés -->

## 5. Artézi kút: nyomás alatt
Az artézi kút alatt nincs forrás. A rétegvíz a magasabb **beszivárgási területen** jut a földbe, és a vízfogó rétegek között ==nyomás alá kerül==, mint a közlekedőedényben. Ha a nyomásszint a felszín fölött van, a víz feltör: ez az **artézi víz**.

> megjegyzés: Mozgasd a kutat, és növeld a vízkivételt! Sok régi kút ma már nem folyik magától.

### Feliratok
- nyomásszint: nyomásszint
- kút: fúrt kút
- feltör: a nyomásszint # m-rel a felszín fölött: magától feltör
- nem tör fel: a nyomásszint # m-rel a felszín alatt: szivattyú kell
- közlekedőedény: közlekedőedény
- egyforma szint: a víz mindkét ágban egy szintre áll
- csúszka kút: A kút helye
- csúszka vízkivétel: Vízkivétel (sok kút)
- km: # km
- százalék: # %
- Zsigmondy: Zsigmondy Vilmos, Városliget, #:
- Zsigmondy 2: # mélyről # víz tört fel

### Adatok
- nyomásszint esése: 0,5 m/km (modell)
<!-- forrás: modellparaméter – a nyomásszint a beszivárgási területtől távolodva a súrlódás miatt lassan csökken; a valódi érték rétegenként és helyenként eltér -->
- legnagyobb nyomásszint-süllyedés: 20 m (modell)
<!-- forrás: modellparaméter. Az Alföldön a 20. század második felében a sok kút miatt a rétegvíz nyomásszintje helyenként méterekkel–tíz méterekkel süllyedt, és sok korábban magától folyó artézi kút elapadt (vízügyi szakirodalom, pl. Rónai A.: Az Alföld negyedidőszaki földtana, 1985) – a pontos értékek helyenként eltérnek, ellenőrizendő -->
- kezdő kúthely: 112 km (modell)
<!-- forrás: a csúszka kezdőértéke (a szelvény 112. kilométere, a Tisza-vidéken) -->
- Zsigmondy-kút éve: 1878
<!-- forrás: Széchenyi fürdő története (szechenyibath.hu, „History”), en.wikipedia „Széchenyi thermal bath”: Zsigmondy Vilmos fúrása 1868-ban kezdődött, 1878-ban érte el a 970 m-t, 74–74,5 °C-os víz; lekérdezve: 2026-11-24 -->
- Zsigmondy-kút mélysége: 970 m
<!-- forrás: mint fent (Zsigmondy-kút) -->
- Zsigmondy-kút vize: kb. 74 °C
<!-- forrás: mint fent (Zsigmondy-kút) -->

## 6. Lefelé melegszik: hévíz
Lefelé a kőzet melegszik: átlagosan {átlagos geotermikus gradiens}-rel, nálunk {Pannon-medence gradiense}-rel. Itt ugyanis ==vékony a földkéreg==, közelebb a forró köpeny. A legalább {hévíz határa}-os víz a **hévíz** – nem vulkáni eredetű! Fúrj kutat!

> megjegyzés: Kapcsold méretarányosra: a legmélyebb kút is csak karcolás a kérgen.

### Feliratok
- csúszka hely: A fúrás helye
- csúszka mélység: A fúrás mélysége
- gomb méretarányos: Méretarányos nézet: a földkéreg
- gomb vissza: Vissza a fúráshoz
- kútnapló: Kútnapló
- napló mélység: mélység: #
- napló kőzet: kőzet: #
- napló üledék: medenceüledék
- napló víz: víz: #
- napló hő: hőmérséklet: #
- nincs víz: nincs (a vízszint fölött)
- nem ad vizet: vízfogó, vizet nem ad
- artézi víz: artézi víz
- hévíz is: # – hévíz
- izoterma: # °C
- grafikon cím: Hőmérséklet a mélységben
- grafikon x: hőmérséklet (°C)
- grafikon y: mélység (m)
- nálunk: Pannon-medence
- átlag: világátlag
- forrás hő: Modell: egyenletes melegedés a mélységgel · a valóságban helyenként eltér
- kéreg: földkéreg
- köpeny: köpeny
- kéreg itt: a kéreg alja itt: #
- kéreg átlag: átlagos kontinentális kéreg: #
- legmélyebb kút: a fúrás (#)

### Adatok
<!-- forrás (az alábbiakra): Magyarország térképekben – Földtan (hungarian-geography.hu): a Pannon-medence kérge kivételesen vékony (22–32 km), a geotermikus gradiens nagy (41–56 °C/km), a hőáram 80–120 mW/m²; L. Lenkey et al. (2002): Geothermics of the Pannonian basin, EGU SMSPS 3, 29–40; lekérdezve: 2026-11-24 -->
- Pannon-medence gradiense: kb. 5 °C/100 m
- átlagos geotermikus gradiens: kb. 3 °C/100 m
<!-- forrás: a kontinentális kéreg átlagos geotermikus gradiense kb. 25–30 °C/km, közismert tankönyvi érték („33 méterenként 1 °C”) -->
- kéreg vastagsága itt: 22–32 km
- átlagos kéregvastagság: kb. 35–40 km
<!-- forrás: a kontinentális kéreg átlagos vastagsága kb. 35–40 km (pl. Christensen–Mooney 1995: 39 km), közismert -->
- hévíz határa: 30 °C
<!-- forrás: 101/2007. (XII. 22.) KvVM rendelet 2. § e): hévíz a kútfejen (forrásnál a kifolyásnál) mért 30 °C-os vagy annál melegebb felszín alatti víz; lekérdezve: 2026-11-24 (njt.jog.gov.hu) -->
- kezdő fúrási hely: 140 km (modell)
- kezdő fúrási mélység: 1200 m (modell)
<!-- forrás: a csúszkák kezdőértékei -->
- legnagyobb fúrási mélység: 3000 m (modell)
<!-- forrás: a csúszka tartománya; a hazai geotermikus kutak jellemzően 1–2,5 km mélyek -->

## 7. Karsztvíz és barlang
A szén-dioxidos esővíz lassan oldja a mészkövet. A repedések **barlanggá** tágulnak, bennük ==föld alatti patakok== is folynak. A **karsztvíz** egy része hidegen fakad. Más része mélyre jut, felmelegszik, és langyos forrásként tör fel. A **Hévízi-tó** vize is ilyen meleg karsztvíz.

> megjegyzés: Húzd az időt! A mélyről jövő hévíz sok oldott anyagot hoz: ásványvíz, gyógyvíz is lehet.

### Feliratok
- oldódás: oldódás (a barlang tágul)
- kiválás: kiválás (cseppkő nő)
- egyenlet oldás: CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂
- egyenlet kiválás: Ca(HCO₃)₂ → CaCO₃ + H₂O + CO₂
- víznyelő: víznyelő
- barlang: barlang
- cseppkő: cseppkő
- föld alatti patak: föld alatti patak
- hideg forrás: hideg karsztforrás: #
- langyos forrás: langyos forrás: #
- csúszka idő: Idő
- ezer év: # ezer év
- Hévíz cím: Hévízi-tó
- Hévíz terület: terület: #
- Hévíz forrás: forrásbarlang: # mélyen
- Hévíz hő: a feltörő víz: kb. #
- Hévíz hozam: hozam: #
- Hévíz keveredés: meleg és hideg karsztvíz keveredik
- Baradla: Baradla–Domica-barlang: #

### Adatok
- hideg karsztforrás: kb. 9 °C
<!-- forrás: Lénárt L.: Hol van termálkarsztvíz a Bükk-térségben? (Multidiszciplináris Tudományok, Miskolci Egyetem), lekérdezve: 2026-11-24 – a leszálló (beszivárgó vizű) hideg karsztforrások vize hazánkban kb. 9 °C körüli -->
- langyos karsztforrás: 20–30 °C
<!-- forrás: Lénárt L. (mint fent): a Bükk déli peremén Egerben 19–23 °C-os, Miskolctapolcán 29,9–30,8 °C-os langyos források fakadtak; a mélyből feláramló víz a felszín közelében hideg karsztvízzel keveredik -->
- barlang kialakulása: 500 ezer év (modell)
<!-- forrás: modellparaméter (az idő-csúszka vége); a barlangok kora jellemzően százezer–millió év nagyságrendű, ellenőrizendő -->
- Hévízi-tó területe: kb. 4,4 ha
<!-- forrás (Hévíz): hu.wikipedia.org „Hévízi-tó” (4,44 ha; 38–38,5 m mély forrásbarlang; 410 l/s, 2012-ben 450 l/s; a forrásvíz kb. 38 °C, meleg és hideg forrásvizek keveréke), lekérdezve: 2026-11-24; a Hévízgyógyfürdő 2025-ös közleménye (spaheviz.hu): a forrásbarlangban mért kevert víz évi átlaga 37,3–37,5 °C (2022–2024), a meleg rész a Zalai-medence, a hűvösebb a Keszthelyi-hegység felől érkezik -->
- Hévíz forrásbarlangja: 38 m
<!-- forrás: mint fent (Hévízi-tó) -->
- Hévíz forrásvize: 38 °C
<!-- forrás: mint fent (Hévízi-tó, spaheviz.hu) -->
- Hévíz hozama: kb. 410 l/s
<!-- forrás: mint fent (Hévízi-tó); újabb közlésekben 450 l/s -->
- Baradla–Domica hossza: kb. 25 km
<!-- forrás: hu.wikipedia.org „Baradla-barlang”: a Baradla és a szlovákiai Domica együtt kb. 25,1–25,5 km (ebből a Domica 5,3 km), lekérdezve: 2026-11-24 -->

## 8. Belvíz: amikor feljön a talajvíz
Tévhit, hogy a belvíz a kiöntött folyó. Csapadékos télen és tavasszal ==a talajvíz megemelkedik==, és a sík terület mélyedéseiben a felszínre bukkan. Az agyagos talaj alig nyeli el, a sík vidékről lassan folyik le: ez a **belvíz**. A folyó közben a gátak között marad.

> megjegyzés: Növeld a csapadéktöbbletet! Hol jelenik meg először a víz?

### Feliratok
- csúszka csapadék: Csapadéktöbblet (télen–tavasszal)
- mm: # mm
- gát: gát
- mentett oldal: mentett ártér (szántó)
- folyó medrében: a folyó a gátak között marad
- belvíz: belvíz
- emelkedés: a talajvíz # m-t emelkedik
- elöntés: a sík terület #-a víz alatt
- agyagos talaj: agyagos talaj
- nem árvíz: nem a folyó öntött ki!
- forrás belvíz: Modell: egy réteg, párolgás és lefolyás nélkül · a felszín vázlatos

### Adatok
- talajvíz kezdő mélysége: 2 m (modell)
<!-- forrás: modellparaméter (az alföldi talajvíz tavasszal jellemzően 1–3 m mélyen van) -->
- talaj víztelíthető része: 15 % (modell)
<!-- forrás: modellparaméter (fajlagos vízleadás, homokos-agyagos talajban kb. 5–25 %, Freeze–Cherry 1979); a talajvíz emelkedése = csapadéktöbblet / 0,15 -->
- kezdő csapadéktöbblet: 100 mm (modell)
<!-- forrás: a csúszka kezdőértéke -->
- legnagyobb csapadéktöbblet: 300 mm (modell)
<!-- forrás: a csúszka kezdőértéke és tartománya -->

## 9. Védett kincs: az ivóvíz
Magyarország ivóvizének ==több mint {ivóvíz felszín alatti vízből}-a felszín alatti vízből== jön. A talajvíz könnyen szennyeződik. A mély rétegvíz és a karsztvíz védettebb, de lassan pótlódik: a mély rétegvíz néhány ezer, sőt tízezer éves is lehet. Ezért védjük a beszivárgási területeket és a kutak környékét.

> megjegyzés: Nézzetek utána: honnan jön a ti csapvizetek?

### Feliratok
- ö talajvíz: talajvíz – sekély, könnyen szennyeződik
- ö rétegvíz: rétegvíz – vízfogó rétegek között
- ö artézi: artézi kút – nyomás alatt feltör
- ö hévíz: hévíz – mélyen, legalább #
- ö karszt: karsztvíz – a mészkő repedéseiben
- ö belvíz: belvíz – a felszínre bukkanó talajvíz
- ivóvíz: ivóvizünk több mint #-a felszín alatti víz
- víz kora: a mély rétegvíz kora: #
- honnan típus: Honnan tudjuk?
- honnan cím: Fúrás és kútnapló
- honnan mivel: Mivel?
- honnan mivel v: fúrással: a kőzetmintákból kútnapló készül
- honnan mit: Mit mérnek?
- honnan mit v: vízszint, hőmérséklet, vízminőség
- honnan hol: Hol?
- honnan hol v: országos kúthálózat figyeli a talajvíz szintjét
- honnan pontos: Pontos?
- honnan pontos v: a kutak között a rétegeket becsülik
- forrás ivóvíz: Forrás: Állami Számvevőszék; OKI Ivóvízminőség 2013 · a metszet vázlatos

### Adatok
- ivóvíz felszín alatti vízből: 90 %
<!-- forrás: Országos Környezetegészségügyi Intézet: Ivóvízminőség 2011 és 2013 (nnk.gov.hu): az ivóvíz 92 %-a felszín alatti vízből, 8 %-a felszíni vízből; Állami Számvevőszék (asz.hu, 24004. sz. dokumentum): közel 95 %; lekérdezve: 2026-11-24. A lecke „több mint 90 %”-ot mond. -->
- mély rétegvíz kora: 2–30 ezer év (becslés)
<!-- forrás: M. Stute, J. Deák (1989): Environmental isotope study (14C, 13C, 18O, D, noble gases) on deep groundwater circulation systems in Hungary with reference to paleoclimate. Radiocarbon 31(3), 902–918: a 100–1000 m mély rétegvíz kora gyakran néhány ezer – több tízezer év; lekérdezve: 2026-11-24 -->

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - A metszet domborzata valódi (ETOPO 2022, k. h. 20,5°, a Tisza-vidéktől a Bükk-fennsíkig), a felszín alatti
    rétegek rajza viszont VÁZLATOS, didaktikus: két homok/kavics víztartó, két agyagos vízfogó, alatta homokos-
    agyagos medenceüledék, a Bükk mészköve délen a medence alá bukik. A valódi alföldi rétegsor sokkal tagoltabb
    (sok vékony, lencseszerű réteg), a Bükkalján vulkáni tufák is vannak. A mélységek nem egy konkrét fúrásból valók.
  - Az artézi nyomásszint lineáris modell (beszivárgás a Bükkalján, 0,5 m/km esés); a valódi alföldi
    rétegvíz-áramlási rendszer regionális, több beszivárgási területtel. A „vízkivétel” csúszka a 20. századi
    nyomásszint-süllyedést szemlélteti, a 20 m-es maximum modellérték.
  - A hőmérséklet a mélységgel egyenletes gradiensű modell (felszín 11 °C + 5 °C/100 m); a karsztos területeken a
    beszivárgó hideg víz miatt lent hidegebb lehet, a fúrás-csúszka ezért csak a medencében és a Bükkalján fúr.
  - A kéregvastagság a Pannon-medencében 22–32 km (a rajz a sáv közepét, 27 km-t mutatja); az Alföld alatt
    jellemzően 24–27 km.
  - Hévízi-tó: a vízhozam forrásonként eltérő (410 l/s, újabban 450 l/s is szerepel; a hozam közvetlenül nem
    mérhető), a forrásvíz kb. 37–38,5 °C. A tó felszíne nyáron kb. 33–35, télen kb. 24–26 °C (hu.wikipedia).
  - A barlang tágulásának üteme és a cseppkőnövekedés a csúszkán didaktikus (500 ezer év, gyökös tágulás).
  - Belvíz-modell: egy homogén réteg, a talajvíz a csapadéktöbblet / 0,15 értékkel emelkedik; párolgás,
    lefolyás, fagyott talaj nincs benne. A gát és a mélyedések vázlatosak.
  - A magyar ivóvíz felszín alatti aránya forrásonként 92–95 % (OKI 2011/2013, ÁSZ); az OECD 2026-os jelentése
    az OVF-re hivatkozva 40 %-ot ír a közüzemi vízellátásra – ez ellentmond a többinek, ellenőrizendő.
  - A „több ezer éves” rétegvíz a 100–1000 m-es mélységre vonatkozik (Stute–Deák 1989); a sekély talajvíz
    néhány hónapos–néhány éves.
-->
