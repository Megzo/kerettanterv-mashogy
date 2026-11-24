# Hány Földre volna szükségünk? – ökológiai lábnyom és biokapacitás
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 10. Helyi problémák, globális kihívások, a fenntartható jövő dilemmái

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/15-okologiai-labnyom.md

  Adatok és licenc. A lábnyom- és biokapacitás-számlák (National Ecological Footprint and Biocapacity
  Accounts, NEFBA) nyilvános adatcsomagja CC BY-SA 4.0 licencű. A szerződés szerint CC BY-SA adatot csak a
  felhasználó jóváhagyásával veszünk át adatkészletként, ezért a lecke NEM tartalmaz adatfájlt: csak az
  alábbi, kerekített, forrással jelölt értékeket (világösszesítés, túllépési napok, országonkénti
  „Föld-szám”). Ha a jóváhagyás megvan, egy shared/foldrajz/labnyom-nefba.js adatfájl az összes országra
  és évre kiválthatja őket.
  A két forrás két kiadás: a világadatok és a túllépési napok a 2026-os kiadásból (az adatok 2023-ig
  teljesek), az országonkénti „Föld-szám” a GFN „Country Overshoot Days 2026” oldaláról (az a 2025-ös
  kiadásból, főleg 2024-es adatból számol). Minden kiadás az egész idősort újraszámolja, ezért a régebbi
  sajtóban más dátumok szerepelnek – ezeket ne keverd ezekkel (7. lépés).
-->

## Közös

### Feliratok
- modell: modell
- becslés: becslés
- log. skála: log. skála
- hónapok: jan.;febr.;márc.;ápr.;máj.;jún.;júl.;aug.;szept.;okt.;nov.;dec.
- hónapnevek: január;február;március;április;május;június;július;augusztus;szeptember;október;november;december
- nap formátum: # #.
- Föld: # Föld
- gha: # gha
- napok: # nap
- c szántó: szántó
- c legelő: legelő
- c erdő: erdő
- c fa: fa, papír
- c halászóvíz: halászóvíz
- c hal: hal
- c beépített: beépített
- c CO₂: CO₂-elnyelés
- keret: a Föld idei kerete
- túllépés: túllépés: a készletből élünk
- túllépés napja: túllépés napja

## 1. Mennyit ad a Föld egy évben?
A Föld termékeny területei – szántó, legelő, erdő, halászóvíz – évente újranövesztik a növényt, a fát, a halat, az erdők pedig CO₂-t is elnyelnek. Ez a **biokapacitás**. A felszínnek csak kb. negyede ilyen. ==Egy emberre {biokapacitás fejenként} jut== – nagyjából két focipályányi.

> megjegyzés: 1 globális hektár (gha) = egy világátlagos termőképességű hektár.

### Feliratok
- cím 1: Mennyit terem a Föld egy év alatt?
- felszín: a Föld felszíne: # milliárd ha
- nem termékeny: nem termékeny: mélytenger, sivatag, jég
- termékeny: termékeny: # milliárd ha
- milliárd ha: termékeny terület, milliárd hektár
- osztva: ÷ # milliárd ember =
- fejenként: jut egy emberre
- négyzet: # gha: egy # m oldalú négyzet
- focipálya: focipálya (105 m × 68 m)
- pálya szorzó: ≈ # focipálya
- forrás 1: Forrás: NEFBA 2026 (Footprint Data Foundation, York University), 2023-as adat

### Adatok
<!-- forrás (az alábbiakra): Lo, K. et al. 2026. National Ecological Footprint and Biocapacity Accounts, Edition 2026 (1961–2025), v1.0, Footprint Data Foundation / York University / University of Iceland, https://fodafo.org/data/ (world_data munkalap, 2023), lekérdezve: 2026-11-24, CC BY-SA 4.0 – néhány kerekített érték, forrásmegjelöléssel; a biokapacitás fejenként = 12,14 milliárd gha / 8,09 milliárd fő -->
- a Föld felszíne: 510 millió km²
<!-- forrás: közismert (kb. 510,1 millió km²) -->
- termékeny terület: 12,1 milliárd hektár (2023)
- szántó területe: 1,43 milliárd hektár (2023)
- legelő területe: 3,37 milliárd hektár (2023)
- erdő területe: 4,04 milliárd hektár (2023)
- halászóvíz területe: 2,97 milliárd hektár (2023)
- beépített terület: 0,33 milliárd hektár (2023)
- világ népessége 2023: 8,09 milliárd fő (2023)
- biokapacitás fejenként: 1,5 gha (2023, frissítendő)
- focipálya területe: 0,714 hektár
<!-- forrás: 105 m × 68 m, a FIFA ajánlott pályamérete (Stadium Guidelines); a pályák mérete eltérhet -->

## 2. Mit mér az ökológiai lábnyom?
**Tévhit:** a lábnyom a szemetünk. Az **ökológiai lábnyom** azt méri, mennyi termékeny terület kellene mindahhoz, amit egy év alatt elhasználunk – élelem, fa, hal, beépített föld –, és a kibocsátott CO₂ elnyeléséhez. ==Az emberiség lábnyomának {CO₂ aránya}-a CO₂-elnyelő erdő.== Egy főre {lábnyom fejenként} jut, a biokapacitás csak {biokapacitás fejenként}.

### Feliratok
- cím 2: Mennyi kellene – és mennyi van?
- sor ad: Amit a Föld ad (biokapacitás)
- sor használ: Amit használunk (lábnyom)
- egy Föld: 1 Föld
- többlet: +# %: túllépés
- tévhit 2: a lábnyom = a szemét?
- cáfolat 2: nem: termékeny területet mér, globális hektárban
- tengely 2: globális hektár / fő (gha), 2023
- forrás 2: Forrás: NEFBA 2026 (Footprint Data Foundation, York University), 2023-as adat

### Adatok
<!-- forrás (az alábbiakra): NEFBA 2026 (lásd az 1. lépést), world_data 2023: a lábnyom és a biokapacitás összetevői milliárd gha-ban, elosztva a népességgel (8,09 milliárd), két tizedesre kerekítve; lekérdezve: 2026-11-24, CC BY-SA 4.0. A szántó és a beépített terület lábnyoma a számlákban definíció szerint egyenlő a biokapacitásukkal. A CO₂ aránya: 12,51 / 20,75 milliárd gha = 60,3 % (a GFN 2026-os sajtóanyaga a 2026-os becslésre 61 %-ot ír). -->
- biokapacitás részei: 0,44; 0,18; 0,64; 0,13; 0,10 gha (2023)
<!-- sorrend: szántó; legelő; erdő; halászóvíz; beépített – összesen 1,50 gha -->
- lábnyom részei: 0,44; 0,13; 0,26; 0,08; 0,10; 1,55 gha (2023)
<!-- sorrend: szántó; legelő; fa, papír (erdő); hal (halászóvíz); beépített; CO₂-elnyelés – összesen 2,56 gha -->
- lábnyom fejenként: 2,56 gha (2023, frissítendő)
- CO₂ aránya: 60 % (2023)

## 3. A túllépés napja
Ha a lábnyom nagyobb a biokapacitásnál, **túlfogyasztás** van: az év egy napján elfogy a Föld idei kerete. Ez a **túllépés napja** (365 × biokapacitás ÷ lábnyom). ==A túllépés napja {túllépés napja 1972} helyett {túllépés napja 2025}: öt hónappal korábbra került.== Utána a készletből élünk: fogy az erdő, a hal, gyűlik a CO₂.

> megjegyzés: Húzd az év-csúszkát! Mi történt 2020-ban?

### Feliratok
- cím 3: Mikor fogy el a Föld idei kerete?
- hány Föld: Hány Föld kellene?
- y 3: a túllépés napja
- járvány: 2020: járvány
- csúszka év: Év
- gomb lejátszás: Lejátszás
- forrás 3: Forrás: Global Footprint Network, Past Earth Overshoot Days (NEFBA 2026-os kiadás), 2026

### Adatok
<!-- forrás (az alábbiakra): Global Footprint Network, „Past Earth Overshoot Days” (https://overshoot.footprintnetwork.org/newsroom/past-earth-overshoot-days/), a 2026-os kiadás (NEFBA 2026) szerint újraszámolt dátumok, lekérdezve: 2026-11-24. A napot a GFN így számolja: biokapacitás ÷ lábnyom × 365 (szökőévben 366). A régebbi sajtóhírekben szereplő dátumok (más kiadás) ezekkel nem összevethetők. A dátum tény, nem szerzői mű; a forrást megjelöljük. -->
- túllépés napja 1972: 1972. december 31.
- túllépés napja 1975: 1975. december 12.
- túllépés napja 1980: 1980. november 29.
- túllépés napja 1985: 1985. november 17.
- túllépés napja 1990: 1990. október 23.
- túllépés napja 1995: 1995. október 17.
- túllépés napja 2000: 2000. szeptember 23.
- túllépés napja 2005: 2005. szeptember 1.
- túllépés napja 2010: 2010. augusztus 15.
- túllépés napja 2015: 2015. augusztus 12.
- túllépés napja 2019: 2019. augusztus 6.
- túllépés napja 2020: 2020. augusztus 18.
- túllépés napja 2021: 2021. augusztus 5.
- túllépés napja 2025: 2025. augusztus 1.
- túllépés napja 2026: 2026. július 30. (becslés)
<!-- forrás: GFN, „Earth Overshoot Day 2026 falls on July 30” (2026. jún. 5.) és „How the Date of Earth Overshoot Day 2026 Was Calculated”: a 2026-os nap előrejelzett becslés („nowcast”) a 2023-ig teljes adatokból, lekérdezve: 2026-11-24 -->
- Föld-szám 2026: 1,73 Föld (2026, frissítendő)
<!-- forrás: GFN, Earth Overshoot Day 2026 sajtóközlemény: „equivalent to using 1.73 Earths”, lekérdezve: 2026-11-24 -->

## 4. Mi tolná el a napot?
Kísérletezz a **modellel**: szorozd meg a 2023-as világátlagos lábnyom három részét! ==Ha a CO₂-lábnyom feleződne, a túllépés napja kb. {CO₂ felezése} késéssel jönne.== A modell a biokapacitást állandónak veszi.

### Feliratok
- cím 4: Mi tolná el a túllépés napját?
- csúszka CO₂: CO₂ (energia)
- csúszka élelem: élelem (szántó, legelő, hal)
- csúszka fa: fa, papír, beépített terület
- g CO₂: CO₂
- g élelem: élelem
- g fa: fa + beépített
- tengely 4: lábnyom egy főre (gha) – modell
- kiinduló: 2023: #
- eltolás: # nappal később
- eltolás korábban: # nappal korábban
- nincs túllépés: nincs túllépés
- Föld-szám: Föld-szám
- túllépés napja 4: a túllépés napja
- gomb alaphelyzet: Alaphelyzet
- forrás 4: Modell a NEFBA 2026 világadataiból (2023) · a GFN számítása a CO₂ felezésére: #

### Adatok
- modell alapéve: 2023
<!-- forrás: a 2. lépés világadatai (NEFBA 2026, 2023) -->
- túllépés napja 2023: 2023. augusztus 2.
<!-- forrás: GFN, Past Earth Overshoot Days (NEFBA 2026), lekérdezve: 2026-11-24 – a modell alapállása ezt adja ki (a lecke ellenőrzi) -->
- CO₂ felezése: 93 nap
<!-- forrás: GFN, overshoot.footprintnetwork.org/solutions/energy/: „Reducing the carbon component of humanity's Ecological Footprint by 50% would move Earth Overshoot Day by 93 days”, lekérdezve: 2026-11-24; a 2026-os sajtóanyag: „cutting CO2 emissions from fossil fuels by 50% would #MoveTheDate by three months”. A modell ugyanezt adja (a lecke ellenőrzi). -->

## 5. Országonként más
Hány Föld kellene, ha mindenki úgy élne, mint egy átlagos lakos az adott országban? ==Katarban {Föld-szám QAT}, Magyarországon {Föld-szám HUN}, Indiában {Föld-szám IND} kellene.== Az 1 alatti érték többnyire alacsony jövedelemmel jár együtt – erről szól a következő lépés.

> megjegyzés: Kattints egy országra!

### Feliratok
- cím 5: Hány Föld kellene, ha mindenki így élne?
- leg 5: Föld-szám (ha mindenki így élne)
- leg <1: 1 alatt
- leg 1–2: 1–2
- leg 2–3: 2–3
- leg 3–5: 3–5
- leg ≥5: 5 vagy több
- nincs a válogatásban: nincs a válogatásban
- kártya Föld: ha mindenki így élne:
- kártya gha: lábnyom fejenként:
- kártya gha érték: kb. # gha
- kattints: Kattints egy országra!
- ország USA: Egyesült Államok
- ország CAN: Kanada
- ország MEX: Mexikó
- ország BRA: Brazília
- ország ARG: Argentína
- ország PER: Peru
- ország DEU: Németország
- ország FRA: Franciaország
- ország GBR: Egyesült Királyság
- ország ITA: Olaszország
- ország POL: Lengyelország
- ország HUN: Magyarország
- ország AUT: Ausztria
- ország ROU: Románia
- ország RUS: Oroszország
- ország CHN: Kína
- ország IND: India
- ország JPN: Japán
- ország KAZ: Kazahsztán
- ország MNG: Mongólia
- ország SAU: Szaúd-Arábia
- ország IRN: Irán
- ország IDN: Indonézia
- ország QAT: Katar
- ország BGD: Banglades
- ország NGA: Nigéria
- ország ETH: Etiópia
- ország KEN: Kenya
- ország EGY: Egyiptom
- ország ZAF: Dél-afrikai Köztársaság
- ország DZA: Algéria
- ország AUS: Ausztrália
- forrás 5: Forrás: Global Footprint Network, Country Overshoot Days 2026 (NFA 2025), főleg 2024-es adat · Natural Earth

### Adatok
<!-- forrás (az alábbiakra): Global Footprint Network, „Country Overshoot Days 2026” (https://overshoot.footprintnetwork.org/newsroom/country-overshoot-days/), lekérdezve: 2026-11-24. A GFN az ország túllépési napját közli (az a nap, amelyen a túllépés napja lenne, ha mindenki úgy élne, mint az ország lakói); a Föld-szám ebből saját számítás: 365 ÷ a nap sorszáma, egy tizedesre kerekítve (pl. Magyarország: június 24. = 175. nap → 2,09). Ahol nincs túllépési nap (a lábnyom a világ biokapacitása alatt van), ott a GFN „a Föld hány %-a kellene” értékét írtuk át (India: 75 % → 0,75). A dátumok a 2025-ös NFA-kiadásból, többnyire 2024-es helyzetre vonatkoznak. Csak egy válogatás – a térképen a többi ország sraffozott. -->
- Föld-szám USA: 5,0 Föld (2024, frissítendő)
<!-- 2026. március 14. -->
- Föld-szám CAN: 5,4 Föld (2024, frissítendő)
<!-- március 8. -->
- Föld-szám MEX: 1,7 Föld (2024, frissítendő)
<!-- július 31. -->
- Föld-szám BRA: 1,6 Föld (2024, frissítendő)
<!-- augusztus 14. -->
- Föld-szám ARG: 2,2 Föld (2024, frissítendő)
<!-- június 13. -->
- Föld-szám PER: 1,6 Föld (2024, frissítendő)
<!-- augusztus 12. -->
- Föld-szám DEU: 2,8 Föld (2024, frissítendő)
<!-- május 10. -->
- Föld-szám FRA: 3,2 Föld (2024, frissítendő)
<!-- április 24. -->
- Föld-szám GBR: 2,6 Föld (2024, frissítendő)
<!-- május 22. -->
- Föld-szám ITA: 3,0 Föld (2024, frissítendő)
<!-- május 3. -->
- Föld-szám POL: 3,1 Föld (2024, frissítendő)
<!-- április 28. -->
- Föld-szám HUN: 2,1 Föld (2024, frissítendő)
<!-- június 24. -->
- Föld-szám AUT: 4,0 Föld (2024, frissítendő)
<!-- április 2. -->
- Föld-szám ROU: 2,1 Föld (2024, frissítendő)
<!-- június 19. -->
- Föld-szám RUS: 4,2 Föld (2024, frissítendő)
<!-- március 28. -->
- Föld-szám CHN: 2,5 Föld (2024, frissítendő)
<!-- május 27. -->
- Föld-szám IND: 0,75 Föld (2024, frissítendő)
<!-- nincs túllépési nap: „75 %” -->
- Föld-szám JPN: 2,7 Föld (2024, frissítendő)
<!-- május 14. -->
- Föld-szám KAZ: 3,4 Föld (2024, frissítendő)
<!-- április 18. -->
- Föld-szám MNG: 5,7 Föld (2024, frissítendő)
<!-- március 5. -->
- Föld-szám SAU: 4,1 Föld (2024, frissítendő)
<!-- március 31. -->
- Föld-szám IRN: 2,4 Föld (2024, frissítendő)
<!-- május 30. -->
- Föld-szám IDN: 1,3 Föld (2024, frissítendő)
<!-- október 18. -->
- Föld-szám QAT: 10,4 Föld (2024, frissítendő)
<!-- február 4. -->
- Föld-szám BGD: 0,46 Föld (2024, frissítendő)
<!-- „46 %” -->
- Föld-szám NGA: 0,53 Föld (2024, frissítendő)
<!-- „53 %” -->
- Föld-szám ETH: 0,60 Föld (2024, frissítendő)
<!-- „60 %” -->
- Föld-szám KEN: 0,61 Föld (2024, frissítendő)
<!-- „61 %” -->
- Föld-szám EGY: 0,88 Föld (2024, frissítendő)
<!-- „88 %” -->
- Föld-szám ZAF: 2,0 Föld (2024, frissítendő)
<!-- július 4. -->
- Föld-szám DZA: 1,6 Föld (2024, frissítendő)
<!-- augusztus 16. -->
- Föld-szám AUS: 4,9 Föld (2024, frissítendő)
<!-- március 16. -->
- világ biokapacitása 2024: 1,48 gha (2024)
<!-- forrás: GFN, Country Overshoot Days 2026: „1.48 gha per person” (2024, NFA 2025) – ezzel szorozva a Föld-szám az ország egy főre jutó lábnyomát adja (kb.) -->
- osztályközök: 1; 2; 3; 5 Föld
<!-- forrás: saját választás – az 1 Föld a fenntartható szint, ezért ott vált a színskála -->
- országhatárok: Natural Earth
<!-- forrás: Natural Earth 1:110m (közkincs, „Made with Natural Earth”), shared/foldrajz/orszagok.js -->

## 6. Gazdagabb = nagyobb lábnyom?
Minden buborék egy ország: vízszintesen az egy főre jutó GDP (log. skála), függőlegesen a Föld-szám, a méret a népesség. ==A jövedelemmel a lábnyom is nő==: több energia, hús, utazás, áru. Azonos jövedelemnél is nagy a különbség: számít például az energia forrása, az éghajlat és a közlekedés módja.

> megjegyzés: Kattints egy buborékra!

### Feliratok
- cím 6: Gazdagabb = nagyobb lábnyom?
- x 6: egy főre jutó GDP vásárlóerőn ($, 2021-es árakon), 2024
- y 6: Föld-szám
- vonal 1 Föld: 1 Föld: ennyi jut
- méret 6: buborék területe ~ népesség
- kártya GDP: GDP/fő (PPP):
- érték dollár: # $
- forrás 6: Forrás: GFN, Country Overshoot Days 2026 · Világbank WDI (GDP/fő PPP, népesség), 2024

### Adatok
- WDI adatkészlet: Világbank WDI, 2026
<!-- forrás: World Bank, World Development Indicators (API v2, frissítve: 2026-11-11), shared/foldrajz/fejlettseg-wdi.js, lekérdezve: 2026-11-23, CC BY 4.0 -->
- GDP-adat éve: 2024
<!-- forrás: a WDI 2024-es GDP/fő PPP- és népességadata (NY.GDP.PCAP.PP.KD, SP.POP.TOTL) – a Föld-szám többnyire szintén 2024-es helyzetet mutat -->

## 7. Honnan tudjuk? – becslés, nem mérés
A lábnyomot nem mérik, hanem statisztikákból **számolják**. Minden kiadás az egész idősort újraszámolja: a 2025-ös túllépés napja először {túllépés napja 2025 régi} volt, most {túllépés napja 2025} – a különbség {adatjavítás hatása}. ==Nem méri az édesvizet, a biológiai sokféleséget és a mérgező szennyezést.== Az édesvízre külön mutató van: a **vízlábnyom**.

> megjegyzés: Egy pamutpóló vízlábnyoma {póló vízlábnyoma} – főleg a gyapot öntözése.

### Feliratok
- cím 7: Becslés, nem mérés
- honnan típus: Honnan tudjuk?
- honnan cím: Nemzeti lábnyomszámlák (NEFBA)
- honnan 1: Alapadat:
- honnan 1 v: ENSZ (FAO), IEA, kereskedelmi statisztika
- honnan 2: Átváltás:
- honnan 2 v: hozam- és egyenértékszorzó → gha
- honnan 3: Évente:
- honnan 3 v: az egész idősort újraszámolják
- honnan 4: Hibahatár:
- honnan 4 v: nincs teljes körű becslése
- cím 7b: Ugyanaz a nap, két kiadás
- gomb régi: 2025-ös számítás
- gomb új: 2026-os számítás
- régi: 2025-ös kiadás
- új: 2026-os kiadás
- ok 7: főleg: az óceán több CO₂-t nyel el, mint hitték
- nem méri: Amit nem mér:
- nem 1: édesvíz
- nem 2: biológiai sokféleség
- nem 3: mérgező szennyezés
- vízlábnyom: vízlábnyom: külön mutató
- póló: 1 pamutpóló
- póló liter: # víz
- forrás 7: Forrás: GFN, NEFBA 2026 kiadási jegyzet, GFN GYIK · vízlábnyom: Chapagain és mtsai 2006 (becslés)

### Adatok
- túllépés napja 2025 régi: 2025. július 24.
<!-- forrás: GFN, a 2025-ös Earth Overshoot Day (2025. júl. 24.), és a 2026-os számítási oldal: „The 2025 date was 24 July 2025”; a 2026-os kiadás ugyanerre az évre augusztus 1-jét ad; lekérdezve: 2026-11-24 -->
- adatjavítás hatása: 8 nap
<!-- forrás: GFN, „How the Date of Earth Overshoot Day 2026 Was Calculated”: az óceáni szén-elnyelés felfelé javított becslése (Global Carbon Budget 2025) kb. 8 nappal későbbre tolta a napot, a valós romlás kb. 2 nappal korábbra; lekérdezve: 2026-11-24 -->
- póló vízlábnyoma: kb. 2500–2700 liter
<!-- forrás: Chapagain, A. K. et al. (2006): The water footprint of cotton consumption, Ecological Economics 60(1) – egy 250 g-os pamutpóló kb. 2700 l (Water Footprint Network); más becslések kb. 2500 l; a GFN GYIK: „The Ecological Footprint does not, and is not intended to measure freshwater flows”, lekérdezve: 2026-11-24 -->

## 8. Mit lehet tenni?
**Tévhit:** ha mindenki szelektíven gyűjt, eltűnik a lábnyom. A nagyobbik része energia és élelem. Válassz egy lépést: mennyivel tolná későbbre a túllépés napját? ==A legnagyobb hatású a CO₂ felezése: kb. {CO₂ felezése}.== A **tudatos fogyasztói magatartás** (étrend, pazarlás) az egyénen múlik, az energiarendszer inkább az államon és a cégeken.

### Feliratok
- cím 8: Mennyit tolna a túllépés napján?
- szint egyén: egyén, háztartás
- szint település: település, közösség
- szint állam: állam, cégek
- lépés hús: a hús felét növényi étel váltja
- lépés pazarlás: feleannyi élelmiszer-pazarlás
- lépés autó: felére csökkenő autózás
- lépés hatékonyság: ma kapható hatékony technológia
- lépés CO₂: a fosszilis CO₂ felezése
- gomb hús: Étrend
- gomb pazarlás: Pazarlás
- gomb autó: Közlekedés
- gomb hatékonyság: Hatékonyság
- gomb CO₂: CO₂ felezése
- legalább: legalább # nap
- kiinduló 8: 2026: #
- tévhit 8: szelektív gyűjtés = nincs lábnyom?
- évi 6 nap: évi # későbbre tolással kb. # év alatt megszűnne a túllépés
<!-- a GFN szerint évi 6 nappal „2050 előtt” – ez a 2019–2020-as kiindulásra igaz; a lecke a 2026-os napból számolja: (365 − 211) ÷ 6 ≈ 26 év -->
- nem összeadható: a hatások részben átfednek, nem adhatók össze
- forrás 8: Forrás: Global Footprint Network, #MoveTheDate-számítások (becslés), 2026

### Adatok
<!-- forrás (az alábbiakra): Global Footprint Network, overshoot.footprintnetwork.org/solutions/ – food: „If we reduced global meat consumption by 50% and replaced these calories through a vegetarian diet, we would move Overshoot Day 17 days”, „If we cut food waste in half worldwide, we would move Overshoot Day 13 days”; cities: ha az autózás lábnyoma 50 %-kal csökken, és az autós kilométerek harmadát tömegközlekedés váltja: 13 nap; energy: „Existing off-the-shelf, commercial energy-efficiency technologies … could move Overshoot Day at least 21 days”; „If we move the date 6 days each year, humanity can be out of overshoot before 2050”; lekérdezve: 2026-11-24. Ezek a GFN becslései, egymástól független forgatókönyvek. -->
- hús felezése: 17 nap
- pazarlás felezése: 13 nap
- autózás felezése: 13 nap
- hatékonyság: 21 nap
- évi elmozdulás: 6 nap

## 9. Összefoglalás
A **fenntarthatóság** itt azt jelenti: ne használjunk többet, mint amennyit a Föld egy év alatt újratermel. Ma kb. {Föld-szám 2026}nyi kellene. A túllépés **globális probléma**, de a lábnyom országonként, jövedelem szerint nagyon eltér. ==A lábnyom becslés, nem mérés==: az irányt jól mutatja, a pontos napot nem.

### Feliratok
- cím 9: Összefoglalás
- ö 1: A biokapacitás: amennyit a Föld egy év alatt újratermel – kb. # jut egy emberre.
- ö 2: Az ökológiai lábnyom: amennyi termékeny terület a fogyasztásunkhoz és a CO₂ elnyeléséhez kellene.
- ö 3: Ma kb. # Földnyit használunk – a túllépés napja nyár végére esik.
- ö 4: A lábnyom kb. #-a CO₂: a legnagyobb tétel az energia.
- ö 5: Országonként kb. # és # Föld között: a jövedelemmel nő.
- ö 6: Becslés, évente újraszámolják – az édesvizet a vízlábnyom méri.
- forrás 9: Források: NEFBA 2026 (Footprint Data Foundation) · Global Footprint Network · Világbank WDI
