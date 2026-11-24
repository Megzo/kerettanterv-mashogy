# Hol készül a pólód? – globalizáció, munkamegosztás, ellátási lánc
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 7. A nemzetgazdaságtól a globális világgazdaságig

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/12-globalizacio.md
  A „póló útja” illusztráció: egy elképzelt, de jellemző ellátási lánc (nem egy valódi márka
  beszállítói hálózata). A hajóutak vázlatosak (néhány töréspont, közöttük főkörív). Az
  országok jövedelme a shared/foldrajz/fejlettseg-wdi.js adatfájlból jön (Világbank WDI),
  a térkép a shared/foldrajz/orszagok.js-ből (Natural Earth). A lecke ellenőrzi, hogy az
  alábbi, a panelen kimondott számok egyeznek-e a kiszámolt értékekkel (QA: L.checks).
-->

## Közös

### Feliratok
- modell: modell
- becslés: becslés
- vázlatos: vázlatos
- illusztráció: illusztráció
- km: # km
- ezer km: # ezer km

### Adatok
<!-- forrás (az alábbiakra): World Bank, World Development Indicators (data.worldbank.org, API v2, frissítve: 2026-11-11), shared/foldrajz/fejlettseg-wdi.js, lekérdezve: 2026-11-23, CC BY 4.0. Térkép: Natural Earth 1:110m (közkincs, „Made with Natural Earth”), shared/foldrajz/orszagok.js. -->
- WDI adatkészlet: Világbank WDI, 2026
- országhatárok: Natural Earth

## 1. Honnan jön a pólód?
Nézd meg a pólód **címkéjét**: „Készült: Bangladesben”. **Tévhit:** a termék abban az országban készül, amelyik a címkén áll. A címke csak az ==utolsó lényeges feldolgozás== helyét mutatja. Ez a póló {a póló útja} utat tett meg – többet, mint a Föld kerülete. Ez a **globalizáció**: a világ gazdaságai összefonódnak.

### Feliratok
- cím 1: Egy pamutpóló útja a boltig
- csúszka út: Az út
- gomb lejátszás: Lejátszás
- címke fej: CÍMKE
- címke szöveg: Készült: Bangladesben
- címke anyag: 100 % pamut
- állomás 1: gyapot
- állomás 2: fonás, kötés, festés
- állomás 3: varrás
- állomás 4: kikötő
- állomás 5: bolt
- ország 1: Egyesült Államok
- ország 2: Kína
- ország 3: Banglades
- ország 4: Hollandia
- ország 5: Magyarország
- mód hajó: hajó
- mód szárazföld: vonat, kamion
- megtett út: eddig megtett út
- Föld kerülete felirat: a Föld kerülete: #
- forrás 1: Útvonal: saját vázlat (illusztráció) · Natural Earth

### Adatok
- a póló útja: kb. 44 ezer km (modell)
<!-- forrás: a lecke számolja a vázlatos útvonalból (5 szakasz, főkörívek a töréspontok között, 1,2°-os sűrítéssel): 43 828 km; a QA ellenőrzi (±3 %) -->
- Föld kerülete: 40 075 km
<!-- forrás: közismert (az Egyenlítő hossza, WGS 84) -->

## 2. Hol épüljön a gyár?
A gyár oda települ, ahol az összes költség a legkisebb. **Telepítő tényezők:** nyersanyag, munkaerő, piac, közlekedés. Régen drága volt a szén szállítása: a gyár a bányához települt. Ma olcsó a szállítás: ==a bér dönt==. **Tévhit:** mindig az olcsó munkaerő nyer – a **robotizált** gyár a piachoz költözik.

> megjegyzés: Modell: három helyszín, egyenes utak. Húzd a gyárat!

### Feliratok
- cím 2: Hol a legkisebb az összes költség?
- gomb régen: 1900 körül
- gomb ma: 2000 körül
- gomb robot: Robotizált gyár
- súly nyersanyag: Nyersanyag, energia szállítása
- súly piac: Szállítás a piacra
- súly bér: Bérköltség
- hely nyersanyag: nyersanyag, energia
- hely piac: piac (nagyváros)
- hely munkaerő: olcsó munkaerő
- legjobb hely: legkisebb költség
- húzd: húzd a gyárat!
- a gyárad: a te gyárad
- költség nyersanyag: nyersanyag
- költség piac: piacra
- költség bér: bér
- összes: összesen
- olcsóbb: olcsóbb
- drágább: drágább
- többlet: +# %-kal drágább
- súlyok fej: a költségek súlya (modell)
- tévhit 2: a bér sem dönt mindig!

### Adatok
- súlyok 1900 körül: 8; 3; 2 (modell)
<!-- forrás: saját modell (Weber-féle telephelyelmélet, 1909, munkaerő-tényezővel); a három szám: a nyersanyag és az energia szállítása, a termék szállítása, a bér súlya -->
- súlyok 2000 körül: 1; 1; 8 (modell)
<!-- forrás: saját modell (lásd fent) -->
- súlyok robotizált gyár: 1; 2; 0,5 (modell)
<!-- forrás: saját modell (lásd fent) -->
- bérszint a munkaerő-régióban: 20 % (modell)
<!-- forrás: saját modell: a bér az olcsó munkaerő helyén a máshol szokásos 20 %-a (Banglades–Magyarország jövedelemaránya kb. 1 : 8, lásd 3. lépés) -->

## 3. Munkamegosztás: ki mit csinál?
A póló minden lépése oda került, ahol a legolcsóbb vagy a legjobb: ez a **nemzetközi munkamegosztás**. A munkaigényes varrás alacsony bérű országba kerül: Bangladesben az egy főre jutó jövedelem {Banglades GNI-je}, nálunk {Magyarország GNI-je}. ==A tervezés és a márka== a magas jövedelmű országokban marad.

> megjegyzés: Kattints egy országra!

### Feliratok
- cím 3: Ki mit csinál a pólón?
- szerep 1: gyapot
- szerep 2: fonal, kelme
- szerep 3: varrás
- szerep 4: tervezés, márka
- szerep 5: vásárló
- leg jövedelem: Világbank-jövedelmi csoport (# júliusi besorolás)
- inc LIC: alacsony
- inc LMC: alsó-közepes
- inc UMC: felső-közepes
- inc HIC: magas
- nincs adat: nincs adat
- kártya jövedelem: jövedelmi csoport
- kártya GNI: GNI/fő (Atlas-módszer)
- érték dollár: # $
- érték nincs: nincs adat
- forrás 3: Forrás: Világbank, WDI (GNI/fő, #) és jövedelmi csoportok · Natural Earth · Equal Earth-vetület

### Adatok
<!-- forrás (az alábbiakra): Világbank WDI, NY.GNP.PCAP.CD (GNI/fő, Atlas-módszer, folyó USD), 2025, shared/foldrajz/fejlettseg-wdi.js, lekérdezve: 2026-11-23, CC BY 4.0; a lecke ellenőrzi az adatfájllal -->
- Banglades GNI-je: 2840 dollár (2025, frissítendő)
- Magyarország GNI-je: 23 850 dollár (2025, frissítendő)
- jövedelmi adat éve: 2025
- jövedelmi besorolás éve: 2026
<!-- forrás: Világbank-jövedelmi csoportok, FY2027 (2026. július; a 2025-ös GNI/fő alapján) – az adatfájl letöltéskori besorolása -->

## 4. A doboz, amely összezsugorította a világot
1956 áprilisában egy hajó {konténerek 1956-ban} acél **konténerrel** indult útnak. A rakodás tonnánként {hagyományos rakodás} helyett {konténeres rakodás} lett. Ma a legnagyobb hajók kb. 24 ezer konténert visznek. Egy konténerben {pólók egy konténerben} póló fér el: ==a tengeri út pólónként csak néhány cent==.

> megjegyzés: Állítsd a fuvardíjat! 2021-ben a díj többszörösére nőtt.

### Feliratok
- cím 4: A konténer: olcsó szállítás
- rakodás fej: rakodás költsége tonnánként (#)
- hagyományos: zsákok, ládák, kézzel
- konténeres: konténer, darurral
- olcsóbb 97: # %-kal olcsóbb
- hajók fej: a legnagyobb konténerhajó befogadóképessége
- hajók y: húszlábas konténer (TEU)
- csúszka fuvardíj: Fuvardíj (40 lábas konténer)
- fuvar fej: Sanghaj → Rotterdam, egy 40 lábas konténer
- fuvardíj: fuvardíj: # $
- pólónként: # cent / póló
- pólók: kb. # póló
- jel 2021: 2021. szept.
- jel 2026: 2026. szept.
- forrás 4: Forrás: Levinson, The Box (2006) · Notteboom–Pallis–Rodrigue, Port Economics (2022) · Drewry WCI

### Adatok
- első konténerhajó: 1956. április 26.
<!-- forrás: Levinson, M.: The Box (Princeton University Press, 2006); transportgeography.org „Ideal-X, first containership, 1956”, lekérdezve: 2026-11-24 (Newark → Houston) -->
- konténerek 1956-ban: 58 darab
<!-- forrás: Levinson 2006 (58 db 35 lábas konténer), lekérdezve: 2026-11-24 -->
- hagyományos rakodás: 5,83 dollár/t
<!-- forrás: Levinson 2006 (McLean 1956-os számítása: hagyományos rakodás 5,83 $/t), lekérdezve: 2026-11-24 -->
- konténeres rakodás: 0,158 dollár/t
<!-- forrás: Levinson 2006 (az Ideal-X rakodása 15,8 cent/t), lekérdezve: 2026-11-24 -->
- legnagyobb konténerhajó: 1972: 2400 · 1981: 3430 · 1988: 4500 · 1996: 6000 · 1997: 8000 · 2006: 12 500 · 2013: 18 000 · 2019: 24 000 TEU
<!-- forrás: Notteboom, Pallis, Rodrigue: Port Economics, Management and Policy (Routledge, 2022), „The Largest Available Containership, 1970–2024 (in TEUs)”, porteconomicsmanagement.org, lekérdezve: 2026-11-24 (a 2019-es érték a „Megamax” osztály kerekítve; a ma legnagyobb hajók kb. 24 000–24 300 TEU-sok) -->
- pólók egy konténerben: kb. 50 ezer darab (becslés)
<!-- forrás: saját becslés: 40 lábas konténer belső térfogata kb. 67 m³, egy hajtogatott, csomagolt póló kb. 1,2–1,4 dm³ → kb. 45–55 ezer db; a forgalmazói becslések 40–60 ezer között szórnak -->
- fuvardíj 2021: 14 287 dollár (2021)
<!-- forrás: Drewry World Container Index, Sanghaj–Rotterdam, 40 láb, 2021. szeptember eleje (hellenicshippingnews.com „Drewry: World Container Index…”), lekérdezve: 2026-11-24 -->
- fuvardíj 2026: 3997 dollár (2026, frissítendő)
<!-- forrás: Drewry World Container Index, Sanghaj–Rotterdam, 40 láb, 2026. szeptember 10. (drewry.co.uk/WCI), lekérdezve: 2026-11-24 -->

## 5. Tengeri utak – és ha elakad egy hajó
A világkereskedelem árujának {tengeri szállítás aránya} hajón utazik (tömegben). Ázsia és Európa között a rövidebb út a **Szuezi-csatornán** át vezet. 2021 márciusában egy {hajó hossza} hosszú hajó keresztben elakadt, és hat napra elzárta. ==Az ellátási lánc ott sérül, ahol szűk==: hajók százai vártak, mások Afrikát kerülték meg.

> megjegyzés: Zárd le a csatornát!

### Feliratok
- cím 5: Ahol a világ árui utaznak
- gomb nyitva: Csatorna nyitva
- gomb zárva: Elakad egy hajó
- tengeri arány: a világkereskedelem #-a hajón utazik (tömegben)
- szuezi arány: kb. #-a a Szuezi-csatornán át
- nap: #. nap
- várakozik: kb. # hajó vár
- valóság: a valóságban: több mint # hajó
- elzárva: 2021. március 23–29.
- kerülő: kerülőút Afrika körül: + # km
- kerülő nap: kb. + # nap (# km/h-val)
- inset fej: Szuezi-csatorna
- Port Szaid: Port Szaid
- Szuez: Szuez
- Földközi-tenger: Földközi-tenger
- Vörös-tenger: Vörös-tenger
- hajó keresztben: # m-es hajó
- egy jel: 1 jel = 5 hajó
- Szuezi-csatorna: Szuezi-csatorna
- Jóreménység-foka: Jóreménység-foka
- Malaka-szoros: Malaka-szoros
- forrás 5: Forrás: UNCTAD · Szuezi-csatorna Hatóság (2020) · útvonalak: saját vázlat

### Adatok
- tengeri szállítás aránya: kb. 80 %
<!-- forrás: UNCTAD, Review of Maritime Transport (a világkereskedelem árumennyiségének több mint 80 %-a tengeren), lekérdezve: 2026-11-24 -->
- Szuezi-csatorna aránya: kb. 12 %
<!-- forrás: a világkereskedelem kb. 12 %-a halad át (2021-es becslés; en.wikipedia.org „2021 Suez Canal obstruction”, több hírforrás alapján), lekérdezve: 2026-11-24 -->
- hajó hossza: 400 m
<!-- forrás: a hajó hossza 400 m, befogadóképessége kb. 20 000 TEU (en.wikipedia.org „2021 Suez Canal obstruction”), lekérdezve: 2026-11-24 -->
- elzáródás kezdete: 2021. március 23.
<!-- forrás: elakadt 2021. 03. 23. 7:40 (helyi idő), a forgalom 2021. 03. 29. 19:00-kor indult újra (kb. 6 nap 11 óra) – en.wikipedia.org „2021 Suez Canal obstruction”, lekérdezve: 2026-11-24 -->
- elzáródás vége: 2021. március 29.
<!-- forrás: lásd fent -->
- napi áthaladás: kb. 51 hajó (2020)
<!-- forrás: Szuezi-csatorna Hatóság: 2020-ban 18 829 hajó (maritime-executive.com, 2021. jan.) → 18 829 / 366 = 51,4 hajó/nap, lekérdezve: 2026-11-24 -->
- várakozó hajók: 400 hajó
<!-- forrás: 2021. 03. 29. estéjén több mint 400 hajó várt (kb. 200 a Vörös-tengeren, kevesebb mint 200 a Földközi-tengeren, kb. 50 a Keserű-tavakon); a torlódás 2021. 04. 03-ra oldódott fel (en.wikipedia.org „2021 Suez Canal obstruction”), lekérdezve: 2026-11-24 -->
- hajó sebessége: 30 km/h (modell)
<!-- forrás: saját feltevés: kb. 16 csomó, a konténerhajók szokásos utazósebessége 14–20 csomó (26–37 km/h) -->
- kerülő többlet: kb. 6800 km (modell)
<!-- forrás: a lecke számolja a vázlatos útvonalakból (Szingapúr–Rotterdam: Szuezen át kb. 15 500 km, Afrika körül kb. 22 200 km, a különbség a lecke sűrítésével kb. 6800 km); a tengerészeti távolságtáblák kb. 8300 és 11 700 tengeri mérföldet adnak (15 400 és 21 700 km) -->

## 6. Hol keletkezik az érték?
A **mosolygörbe** szerint a legtöbb érték a lánc két végén keletkezik: a kutatásnál, a tervezésnél, a márkánál és az eladásnál. A gyártás a görbe alján van. Egy {póló ára} árú pólóból a varrónők bérére ==kevesebb mint 1 %== jut. A vámstatisztika viszont a teljes árat a címke országához írja.

### Feliratok
- cím 6: Hol keletkezik az érték?
- görbe y: hozzáadott érték
- görbe x: az értéklánc lépései
- lánc 1: kutatás, fejlesztés
- lánc 2: tervezés
- lánc 3: alapanyag
- lánc 4: gyártás
- lánc 5: szállítás
- lánc 6: márka, reklám
- lánc 7: eladás
- ár fej: egy # árú póló ára
- rész 1: bolt (kiskereskedő)
- rész 2: márkatulajdonos
- rész 3: anyagköltség
- rész 4: szállítás, vám
- rész 5: a gyár nyeresége
- rész 6: közvetítő
- rész 7: a varrónők bére
- rész érték: # %
- euró: # €
- honnan típus: statisztika
- honnan cím: Honnan tudjuk?
- honnan 1: vám
- honnan 1 v: a teljes ár a címke országáé
- honnan 2: OECD
- honnan 2 v: TiVA: hozzáadott érték országonként
- honnan 3: korlát
- honnan 3 v: becslés, cégadatok nélkül
- forrás 6: Forrás: Clean Clothes Campaign becslése · mosolygörbe: Stan Shih (1992), modell

### Adatok
- póló ára: 29 euró
<!-- forrás (ez és az alábbi megoszlás): Clean Clothes Campaign becslése egy Bangladesben varrt, Európában 29 euróért eladott pólóra (cleanclothes.org; összefoglalva: voronoiapp.com „Workers Receive Less Than 1% of the Price of a T-Shirt”, statista.com 34514), lekérdezve: 2026-11-24. A részek kerekítve; a forrás a varrónők részét „1 % alatt”-nak adja, a 0,6 % a kampányanyagok gyakori értéke – ellenőrizendő -->
- árrészek: 59; 12; 12; 8; 4; 4; 0,6 % (becslés)
<!-- forrás: lásd fent (bolt, márka, anyag, szállítás és vám, gyári nyereség, közvetítő, bér) -->

## 7. Működőtőke és pénztőke
A **transznacionális vállalat** központja egy országban van, gyárai sok másikban. Ha gyárat épít, vagy egy cégben legalább {működőtőke határa} részesedést vesz, az **működőtőke**: évtizedekre marad. A **pénztőke** (részvény, kötvény) napok alatt kivonható. **Tévhit:** a kettő ugyanaz. Válságban ==a pénztőke elmenekül, a gyár marad==.

> megjegyzés: Nyomd meg a „Válság” gombot!

### Feliratok
- cím 7: Mi marad egy válságban?
- központ: központ (anyavállalat)
- ország A: A ország
- ország B: B ország
- ország C: C ország
- leány: gyár (leányvállalat)
- bolt: értékesítés
- működőtőke: működőtőke
- pénztőke: pénztőke
- gomb válság: Válság!
- gomb újra: Újra
- grafikon fej: a külföldi tőke a B országban
- grafikon x: napok
- grafikon y: tőke (induló = 100)
- válság jel: válság
- marad: a gyár marad
- elmegy: a pénz elmenekül
- forrás 7: Modell · a működőtőke határa: OECD Benchmark Definition of FDI, 4. kiadás (2008)

### Adatok
- működőtőke határa: 10 %
<!-- forrás: OECD Benchmark Definition of Foreign Direct Investment, 4. kiadás (2008) és IMF BPM6: közvetlen befektetés, ha a befektető a szavazati jogok legalább 10 %-ával rendelkezik -->
- pénztőke kivonása: 60 % (modell)
<!-- forrás: saját modell: válságban a pénztőke 60 %-a napok alatt távozik (szemléltetés, nem egy valódi válság adata) -->

## 8. Kinek jó, kinek nem?
A világkereskedelem a világ GDP-jének {kereskedelem 1970}-a volt 1970-ben, {kereskedelem 2024}-a 2024-ben. A **globalizációnak** nyertesei és vesztesei is vannak. Olcsóbb áru és új munkahelyek – de bezáró gyárak, sérülékeny láncok, és a szállítás is szennyez.

> megjegyzés: Válassz szereplőt! Vitassátok meg: mi a mérleg?

### Feliratok
- cím 8: Kinek jó a globalizáció?
- grafikon 8 fej: export + import a világ GDP-jének %-ában
- válság 2009: 2009
- válság 2020: 2020
- szereplő 1: Vásárló
- szereplő 2: Varrónő Bangladesben
- szereplő 3: Textilmunkás Európában
- szereplő 4: Banglades gazdasága
- szereplő 5: Környezet
- előny 1: olcsóbb ruha, nagyobb választék
- hátrány 1: ha a lánc elakad, késik az áru, nő az ár (2021)
- előny 2: fizetett munka, sokaknak az első saját jövedelem
- hátrány 2: alacsony bér; 2013-ban egy gyárépület összeomlásakor # ember halt meg
- előny 3: új munka a tervezésben, a logisztikában, az eladásban
- hátrány 3: sok hazai textilgyár bezárt, a munka elköltözött
- előny 4: a ruházat adja az export #-át
- hátrány 4: egy ágazattól függ: ha a rendelés elmarad, sokan munka nélkül maradnak
- előny 5: a hajó tonnakilométerenként takarékos szállító
- hátrány 5: a hajózás adja az üvegházgázok #-át (2018), és több ruhát dobunk ki
- előny: előny
- hátrány: hátrány
- forrás 8: Forrás: Világbank, WDI (NE.TRD.GNFS.ZS) · ILO · IMO, 4. üvegházgáz-tanulmány (2020)

### Adatok
- világkereskedelem: 1970: 25,75 · 1971: 25,79 · 1972: 25,98 · 1973: 29,00 · 1974: 33,74 · 1975: 31,94 · 1976: 32,73 · 1977: 33,09 · 1978: 33,49 · 1979: 35,66 · 1980: 38,63 · 1981: 39,07 · 1982: 37,06 · 1983: 36,22 · 1984: 37,51 · 1985: 37,06 · 1986: 34,59 · 1987: 35,86 · 1988: 37,66 · 1989: 38,05 · 1990: 38,10 · 1991: 37,76 · 1992: 40,65 · 1993: 40,17 · 1994: 41,02 · 1995: 42,74 · 1996: 42,82 · 1997: 44,63 · 1998: 45,29 · 1999: 45,76 · 2000: 50,12 · 2001: 49,01 · 2002: 49,00 · 2003: 50,66 · 2004: 54,19 · 2005: 56,22 · 2006: 58,36 · 2007: 58,74 · 2008: 60,32 · 2009: 51,89 · 2010: 56,19 · 2011: 59,31 · 2012: 59,30 · 2013: 58,63 · 2014: 58,03 · 2015: 55,62 · 2016: 53,79 · 2017: 55,46 · 2018: 56,99 · 2019: 55,80 · 2020: 51,87 · 2021: 56,50 · 2022: 62,15 · 2023: 58,07 · 2024: 56,72 %
<!-- forrás: Világbank WDI, Trade (% of GDP), NE.TRD.GNFS.ZS, Világ (WLD), api.worldbank.org (frissítve: 2026-11-11), lekérdezve: 2026-11-24, CC BY 4.0. A 2025-ös érték (68,49) a lekérdezéskor kiugró, előzetes adat – kihagyva -->
- kereskedelem 1970: 26 % (1970)
<!-- forrás: a fenti sor 1970-es értéke kerekítve (a lecke ellenőrzi) -->
- kereskedelem 2024: 57 % (2024, frissítendő)
<!-- forrás: a fenti sor 2024-es értéke kerekítve (a lecke ellenőrzi) -->
- gyárépület áldozatai: 1134 fő
<!-- forrás: ILO, „The Rana Plaza Accident and its aftermath” (ilo.org): 2013. április 24., Dakka környéke, 1134 halott -->
- ruházat az exportban: kb. 80 % (2024, frissítendő)
<!-- forrás: Banglades exportbevételének 81–84 %-a ruházat (Export Promotion Bureau, 2023/24-es pénzügyi év; a kereskedelmi miniszter nyilatkozata: kb. 84 % – unb.com.bd), lekérdezve: 2026-11-24 -->
- hajózás kibocsátása: 2,9 % (2018)
<!-- forrás: IMO Fourth Greenhouse Gas Study 2020: a nemzetközi és belföldi hajózás a világ antropogén üvegházgáz-kibocsátásának 2,89 %-a (2018) -->

## 9. Összefoglalás
A **globalizáció** a termelés, a kereskedelem és a tőke világméretű összefonódása. Olcsó szállítás és gyors információ nélkül nem működne. ==Előnyei és hátrányai is vannak==, és ezek nem egyformán oszlanak el az országok és az emberek között.

### Feliratok
- cím 9: A globalizáció – röviden
- ö 1: A termék sok országban készül; a címke csak az utolsó lépést mutatja.
- ö 2: Telepítő tényezők: régen a nyersanyag, ma a bér, a piac, a tudás.
- ö 3: Nemzetközi munkamegosztás: mindenki azt csinálja, amiben olcsó vagy jó.
- ö 4: A konténer olcsóvá tette a szállítást – a lánc a szűk pontokon sérül.
- ö 5: Az érték a kutatásnál, a márkánál, az eladásnál keletkezik.
- ö 6: A működőtőke évtizedekre jön, a pénztőke napok alatt távozhat.
- forrás 9: Forrás: Világbank, WDI · UNCTAD · útvonalak: saját vázlat · Natural Earth

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - A „póló útja” illusztráció: jellemző, de elképzelt lánc (texasi gyapot, kínai fonás és kötés,
    bangladesi varrás, rotterdami kikötő, hazai bolt). A valóságban Banglades gyapotot Indiából,
    Afrikából, Brazíliából is vesz, és a fonás egy része is ott történik. A hajóutak vázlatosak.
  - A címke („Made in …”) a vámjogi származási szabály szerint az utolsó lényeges feldolgozás helyét
    mutatja – ruházatnál ez jellemzően a szabás-varrás. A szabály országonként, egyezményenként eltér.
  - A 2. lépés telephelymodellje didaktikus (Weber-féle súlyozott távolság + bértényező): a súlyok
    kitaláltak, a „1900 körül / 2000 körül / robotizált” korszakok csak a tendenciát mutatják.
  - A 3. lépésben a GNI/fő (Atlas-módszer) a bérszint közelítése, nem maga a bér; a jövedelmi
    csoportok évente változnak (a Világbank júliusi besorolása).
  - A póló árának megoszlása (Clean Clothes Campaign) érdekvédelmi szervezet becslése, egyetlen
    „tipikus” pólóra; más becslések (pl. a gyári exportár 12 %-a a bér) más alapra vonatkoznak.
  - A mosolygörbe (Stan Shih, 1992) szemléltető modell; a görbe alakja ágazatonként eltér.
  - A Szuez-modell (várakozó hajók = napi áthaladás × napok) kb. 330 hajót ad; a valóságban több mint
    400 várt, mert a konvojrend miatt az elzáródás előtt is gyűltek hajók, és a torlódás csak
    április 3-ra oldódott fel. Hogy a világkereskedelem kb. 12 %-a halad át, az gyakran idézett
    kerekítés (forrásonként 10–15 %).
  - A 7. lépés tőkemodellje szemléltetés (a pénztőke 60 %-a távozik napok alatt); valódi válságok
    (pl. 1997–98, Kelet-Ázsia) adatai ennél változatosabbak.
  - A 8. lépés szereplőkártyái válogatott előnyök és hátrányok – a tanár bővítheti; gazdaságpolitikai
    értékelést szándékosan nem tartalmaznak. A 2013-as épületomlás (Rana Plaza, ILO: 1134 halott) után
    nemzetközi épület- és tűzbiztonsági megállapodás született (2013, Accord).
  - A hajózás „takarékos tonnakilométerenként” állítás általános összevetés (közúti, légi szállításhoz).
  - A Föld kerülete az Egyenlítő hossza (40 075 km); a póló útja kb. 9 %-kal hosszabb.
-->
