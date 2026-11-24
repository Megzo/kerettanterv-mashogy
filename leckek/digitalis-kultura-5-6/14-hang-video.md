# Hogyan lesz a hangból szám? – mintavétel és képkocka
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 6. Multimédiás elemek készítése

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/14-hang-video.md

  A „Tippelj!” lépésekben (3. és 6.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A feliratokban a # jel helyére a lecke számot ír (a számokat a lecke az Adatokból számolja).
  A hang csak a „Meghallgatom” gombra szól, mérsékelt hangerővel; a lecke hang nélkül is teljes.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- kitalált bélyeg: kitalált dallam
- sematikus bélyeg: sematikus rajz
- modell bélyeg: modell
- jel tengely: a jel
- idő tengely: idő (ms)
- szól felirat: szól: #
- eredeti hang felirat: az eredeti dallam
- meghallgatom gomb: Meghallgatom

### Adatok
- dallam hangjai: 262; 330; 392; 330; 349; 294; 392; 523 Hz
<!-- forrás: kitalált dallam (a lecke saját szerzeménye) – C-dúr hangok A = 440 Hz-es temperált hangolásban, egészre
     kerekítve: c′ 261,6 · e′ 329,6 · g′ 392,0 · f′ 349,2 · d′ 293,7 · c″ 523,3 Hz. A hangszín: alaphang + 2. és 3. felhang
     (1 : 0,5 : 0,3) – a legmagasabb összetevő 3 · 523 = 1569 Hz, ezért a kis mintavételi értékek (2–8 kHz) ennél a dallamnál
     már hallhatóan rontanak -->
- egy hang hossza: 0,4 s
<!-- forrás: a lecke beállítása (8 hang · 0,4 s = 3,2 s-os dallam) -->
- CD bitmélysége: 16 bit
<!-- forrás: IEC 60908:1999 (Audio recording – Compact disc digital audio system, „Red Book”): 16 bites lineáris kódolás,
     2^16 = 65 536 szint (a lecke számolja) -->

## 1. A hang: rezgő levegő
A hang a levegő **rezgése**. A **mikrofon** ezt elektromos jellé alakítja: hullámzó görbévé. ==A görbe magassága a hangerő, a sűrűsége a hangmagasság.== Válassz hangot a csúszkával, és hallgasd meg a dallamot!

> megjegyzés: A hang fizikájáról fizikaórán többet tanulsz.

### Feliratok
- furulya felirat: furulya
- levegő felirat: a levegő rezeg
- mikrofon felirat: mikrofon
- elektromos jel felirat: elektromos jel
- dallam felirat: a dallam: # hang
- magas felirat: magas
- mély felirat: mély
- nagyító felirat: #. hang: az első # ezredmásodperc, felnagyítva
- hangerő felirat: magasság = hangerő
- hangmagasság felirat: sűrűség = hangmagasság
- rezgés felirat: # rezgés másodpercenként
- egy rezgés felirat: 1 rezgés
- hang csúszka: Melyik hang?
- hang sorszám felirat: #. hang

## 2. Mintavétel: pöttyök a görbén
A gép görbét nem tud tárolni, csak számokat. Ezért másodpercenként sokszor megméri a jelet: ez a **mintavétel**. Minden pötty egy szám. ==Kevés minta: a visszarajzolt görbe torz.== Állítsd a csúszkát, és hallgasd meg!

> megjegyzés: 1 kHz (kilohertz) = 1000 minta másodpercenként.

### Feliratok
- mért jel felirat: a mikrofon jele és a minták
- visszarajzolt felirat: amit a gép a számokból visszarajzol
- mintavétel felirat: # minta másodpercenként
- ablak felirat: # ezredmásodperc alatt: # minta
- szalag felirat: az első # mért szám (# biten: 0 és # között)
- többi felirat: … és még # szám
- hangosabb tévhit felirat: Több minta → hangosabb hang.
- hangosabb válasz felirat: Nem hangosabb, csak hűbb – és nagyobb a fájl.
- mintavétel csúszka: Mintavétel

### Adatok
- mintavételi lépcsők: 2; 4; 8; 22,05; 44,1 kHz
<!-- forrás: a lecke beállítása (a terv 14-es briefje); a 22,05 kHz a CD-érték fele (régebbi, kisebb hangfájlok),
     a 44,1 kHz a CD-é (IEC 60908); a 2–8 kHz-es értékek a kitalált dallamhoz méretezve -->

## 3. Hány minta kell a CD-hez?
A zenei **CD** nagyon hű hangot tárol. ==Hány mintát vesz másodpercenként? Tippelj!==

Ennyit: {CD mintavételi gyakorisága}. A legmagasabb hang, amit hallunk, {legmagasabb hallható hang}: ennyiszer rezeg másodpercenként. ==Minden rezgésre kettőnél több minta kell==, különben a magas hang elvész.

> megjegyzés: Ez a mintavételi tétel (Nyquist–Shannon).

### Feliratok
- cd kérdés felirat: Hány mintát vesz a CD másodpercenként?
- 44 tipp: 44
- 4410 tipp: 4410
- 44100 tipp: 44 100
- egy másodperc felirat: 1 másodperc
- egy ezredmásodperc felirat: 1 ezredmásodperc: # minta
- másodpercenként felirat: # minta minden másodpercben
- legmagasabb felirat: a legmagasabb hallható hang: kb. # rezgés/s
- kétszer felirat: legalább 2 · # = # minta/s kell
- cd elég felirat: a CD: # minta/s – elég!
- jó mintavétel felirat: # minta/s: a rezgés megmarad
- rossz mintavétel felirat: # minta/s: minden pötty egyforma – a hang elvész
- cd felirat: CD

### Adatok
- CD mintavételi gyakorisága: 44100 minta/s
<!-- forrás: IEC 60908:1999 („Red Book”): 44,1 kHz mintavételi frekvencia, 16 bit, 2 csatorna -->
- legmagasabb hallható hang: kb. 20000 Hz
<!-- forrás: becslés – az emberi hallás felső határa fiatalon kb. 20 kHz, a korral csökken (ISO 7029:2017 a korfüggésről);
     ugyanez a szám a fizika-7-8/12-hullam-hang leckében. Mintavételi tétel: C. E. Shannon, „Communication in the
     Presence of Noise”, Proc. IRE 37 (1949); H. Nyquist (1928) – a mintavételi frekvenciának a legmagasabb
     összetevő kétszeresénél nagyobbnak kell lennie: 2 · 20 000 = 40 000 < 44 100 (a lecke számolja) -->

## 4. Hány szint? – bitmélység
Minden mérést a gép a legközelebbi **szintre** kerekít. A **bitmélység** mondja meg, hány szint van: minden újabb bit megduplázza a számukat. ==Kevés szint: recsegő hang.== Próbáld ki! A CD minden mintája {CD bitmélysége}.

> megjegyzés: Mint a pixelnél: n bit 2^n féle szám.

### Feliratok
- szintek felirat: # bit → # szint
- kerekítés felirat: a minták a legközelebbi szintre kerekítve
- minta bitjei felirat: a kiemelt minta: # (# biten)
- szintlánc felirat: minden bit duplázza a szintek számát:
- szintlánc elem: # bit: #
- sűrű szint felirat: # szint – a vonalak már össze is érnek
- bitmélység csúszka: Bitmélység

### Adatok
- bitmélységek: 2; 4; 8; 16 bit
<!-- forrás: a lecke beállítása (a terv 14-es briefje); 2^2 = 4, 2^4 = 16, 2^8 = 256, 2^16 = 65 536 szint (a lecke számolja) -->

## 5. Mekkora lesz a fájl?
Egy másodperc hang mérete: minta/s × bitmélység × **csatornák** száma. A sztereó hang két csatornás: bal és jobb. ==Állítsd a csúszkákat, figyeld a fájlméretet!== 8 bit = 1 bájt.

### Feliratok
- minta tényező felirat: minta/s
- bit tényező felirat: bit
- csatorna tényező felirat: csatorna
- idő tényező felirat: másodperc
- bitráta felirat: = # bit minden másodpercben (# kbit/s)
- bájt felirat: összesen # bit : 8 = # bájt ≈ #
- cd sáv felirat: CD-minőség (# perc): #
- saját sáv felirat: a te beállításod (# perc): #
- tömörített sáv felirat: tömörített zene, # kbit/s (# perc): #
- hang tévhit felirat: A gép a hangot hangként tárolja.
- hang válasz felirat: Csak számokat tárol – CD-minőségben # darabot másodpercenként.
- mintavétel 5 csúszka: Mintavétel
- bitmélység 5 csúszka: Bitmélység
- csatorna csúszka: Csatornák
- hossz csúszka: Hossz (perc)

### Adatok
- CD csatornái: 2
<!-- forrás: IEC 60908:1999 – két csatorna (sztereó); 44 100 · 16 · 2 = 1 411 200 bit/s = 1411,2 kbit/s, egy perc
     1 411 200 · 60 : 8 = 10 584 000 bájt ≈ 10,6 MB (a lecke számolja, L.checks) -->
- tömörített zene: 128 kbit/s
<!-- forrás: becslés – gyakori bitráta a veszteséges zenei tömörítésnél (MPEG-1 Audio Layer III, ISO/IEC 11172-3:1993;
     a szabvány 32–320 kbit/s-ot enged); egy perc 128 000 · 60 : 8 = 960 000 bájt = 960 kB ≈ 0,96 MB (a lecke számolja) -->

## 6. Mozgókép = sok állókép
A videó gyorsan egymás után mutatott állóképek, **képkockák** sora. ==Hány kocka kell másodpercenként, hogy a labda folyamatosan mozogjon? Tippelj!==

**Kb. 12** fölött a szemünk már mozgásnak látja. A mozifilm {film képkockái} sebességgel megy: ennyi kép villan fel másodpercenként. ==Húzd a csúszkát!==

### Feliratok
- kocka kérdés felirat: Hány kocka kell másodpercenként a folyamatos mozgáshoz?
- 3 tipp: 3
- 12 tipp: kb. 12
- 100 tipp: 100
- filmszalag felirat: # képkocka – egy pattanás, # kocka/s mellett
- kockaméret felirat: minden kocka egy pixelkép: # × # pixel
- lejátszó felirat: # kocka másodpercenként
- egy másodperc 6 felirat: 1 másodperc: # kép
- akadozik felirat: akadozik – külön képeket látsz
- folyamatos felirat: folyamatos mozgásnak látszik
- film felirat: mozifilm: # kocka/s
- folyamatos tévhit felirat: A videó egy folyamatos kép.
- folyamatos válasz felirat: A videó állóképek gyors sora.
- kocka csúszka: Képkocka/másodperc

### Adatok
- folyamatos mozgás határa: kb. 12 kocka/s
<!-- forrás: becslés, forrásonként eltér (10–12 kép/s fölött már mozgásnak, alatta külön képeknek látjuk): P. Read,
     M.-P. Meyer: Restoration of Motion Picture Film (Butterworth-Heinemann, 2000), 24–26. o. A villogás észlelése más
     kérdés (ezért vetít a mozigép egy kockát kétszer-háromszor) – a lecke csak a „mozgásnak látszik” küszöbről beszél -->
- film képkockái: 24 kocka/s
<!-- forrás: a hangosfilm szabványos sebessége az 1920-as évek vége óta 24 kép/s (SMPTE ST 428 / ITU-R BT.709 is
     támogatja); a hazai (PAL) tévé 25 kép/s – ezt a lecke nem használja -->

## 7. Videó: miért tömörítünk?
A videó képkockák és hang együtt. Tömörítetlenül óriási: nézd a számokat! A **tömörítés** kicsinyíti. Az egymás utáni kockák szinte egyformák: ==elég a változást tárolni==. Közben apró, alig látható részletek el is vesznek.

> megjegyzés: A tömörítésről 7–8. osztályban többet tanulsz.

### Feliratok
- egy kocka felirat: 1 kocka: # × # pixel · # bájt = #
- másodperc felirat: × # kocka/s = # minden másodpercben
- perc felirat: × 60 s ≈ # egy percre
- videó hang felirat: + a hang (CD-minőség): # – ehhez képest apróság
- tömörítetlen sáv felirat: tömörítetlenül: #
- tömörített videó sáv felirat: tömörítve (kb. # Mbit/s): kb. #
- kisebb felirat: kb. #-szor kisebb
- kocka a felirat: #. kocka
- kocka b felirat: #. kocka
- változás cím felirat: ami változott
- változás felirat: csak # pixel változott a #-ból
- tömörítés tévhit felirat: A tömörített fájl ugyanaz, csak kisebb.
- tömörítés válasz felirat: Apró részleteket is elhagy – alig vesszük észre.
- következő gomb: Következő kockapár

### Adatok
- Full HD szélessége: 1920 pixel
<!-- forrás: ITU-R BT.709-6 (2015), HDTV-képformátum: 1920 × 1080 aktív képpont (ugyanez a 13-pixel leckében) -->
- Full HD magassága: 1080 pixel
<!-- forrás: ITU-R BT.709-6 (2015) -->
- egy pixel mérete: 3 bájt
<!-- forrás: 3 színcsatorna (R, G, B) · 8 bit = 24 bit = 3 bájt (a 13-pixel lecke) → 1920 · 1080 · 3 = 6 220 800 bájt ≈ 6,2 MB
     kockánként; · 24 = 149 299 200 bájt/s ≈ 149,3 MB/s; · 60 = 8 957 952 000 bájt ≈ 9,0 GB percenként (a lecke számolja) -->
- tömörített videó: kb. 8 Mbit/s
<!-- forrás: becslés – egy nagy videómegosztó ajánlott feltöltési bitrátája 1080p-hez (24–30 kép/s, SDR): 8 Mbit/s
     (support.google.com/youtube/answer/1722171, 2026-11-24); a streamelt Full HD jellemzően 3–8 Mbit/s. Egy perc:
     8 000 000 · 60 : 8 = 60 000 000 bájt = 60 MB; az arány 149 299 200 · 8 : 8 000 000 ≈ 149 → „kb. 150-szer” -->

## 8. Összefoglalás
A **digitalizálás** a folytonos jelet számsorrá alakítja. A hangot másodpercenként sokszor megmérjük (**mintavétel**), és szintekre kerekítjük (**bitmélység**). A videó **képkockák** sora. Sok szám → nagy fájl: ezért **tömörítünk**.

> megjegyzés: Feladat: rögzíts telefonnal 10 másodperc hangot és videót, és hasonlítsd össze a fájlok méretét!

### Feliratok
- összefoglaló cím felirat: A digitalizálás: jelből számsor
- összegzés rezgés felirat: hang = a levegő rezgése → a mikrofon jele
- összegzés mintavétel felirat: mintavétel: másodpercenként sokszor megmérjük
- összegzés bitmélység felirat: bitmélység: hány szintre kerekítünk (16 bit: # szint)
- összegzés cd felirat: CD: # minta/s · # bit · # csatorna = # kbit/s
- összegzés kocka felirat: videó = képkockák sora (film: # kocka/s)
- összegzés tömörítés felirat: tömörítés: kisebb fájl – de részlet veszhet el

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a dallam (8 hang, C-dúr), a hangszín (alaphang + két felhang), a pattogó labda képkockái és a
    furulyás–mikrofonos rajz a lecke saját, kódból készült anyagai. Felvett hang, zene, fotó nincs a leckében; a hang
    Web Audióval, a böngészőben készül (szerződés 19., „Szerzői jog”).
  - Mintavétel a leckében: a „visszarajzolt” görbe és a lejátszott hang „mintavétel és tartás” (minden minta a
    következőig kitart) – ezért kevés mintánál lépcsős a görbe, és zúgó, torz a hang. A valódi eszközök a mintavétel
    előtt kiszűrik a túl magas hangokat, és visszajátszáskor simítanak – az eredmény kevésbé recsegő, inkább tompa
    lesz. A 2–8 kHz-es lépcső a kitalált dallamhoz méretezett szemléltetés, nem valódi fájlformátum (a telefonhang
    régen 8 kHz-es volt).
  - Mintavételi tétel (Nyquist–Shannon): a mintavételi frekvencia legyen nagyobb, mint a legmagasabb összetevő
    kétszerese. A 3. lépés jobb oldali rajza a szélső esetet mutatja: rezgésenként pontosan egy minta – minden pötty
    ugyanabba a fázisba esik, a rezgés eltűnik. A hallás felső határa (kb. 20 kHz) egyénenként és korral változik.
  - Bitmélység: a lecke a mintákat 0 és 2^n − 1 közötti szintszámként mutatja (a csend a középen van). A CD valójában
    előjeles számokat tárol (−32 768 … 32 767) – ugyanannyi szint, csak máshonnan számozva. A 8 bites kerekítés
    zaja halkan is hallható, a 16 bitesé gyakorlatilag nem.
  - Fájlméret: tömörítetlen hang = minta/s · bit · csatorna · idő : 8 bájt; 1 kB = 1000 bájt (SI; a 17-szamitogep
    lecke szerint). A 128 kbit/s-os tömörített zene becsült, tipikus érték; a veszteséges tömörítés a hallás
    tulajdonságait használja ki (a halk, elfedett hangokat elhagyja) – ennek részletei a 7–8. évfolyam anyaga.
  - Képkocka: a 10–12 kép/s-os „mozgásküszöb” becslés, forrásonként eltér; a villogás észlelése (mozigép: kockánként
    2–3 felvillanás) és a nagyon gyors mozgás simasága (60–120 kép/s) más kérdés – a lecke nem tárgyalja. A labda
    képkockái 32 × 24 pixeles, kódból rajzolt képek; a lejátszó a folytonos mozgásból vesz „mintát” a beállított
    kocka/s szerint (a hang mintavételének párja).
  - Videó: a tömörítetlen méret 24 kocka/s-mal számolva (mozifilm); 25 kocka/s-mal (hazai tévé) 155,5 MB/s. A
    tömörített videó 8 Mbit/s-os értéke becslés (egy nagy videómegosztó ajánlása Full HD feltöltéshez); a valódi
    videótömörítés a kockák közti változást (mozgásbecslés) és a kockán belüli, alig látható részletek elhagyását
    is használja. A „csak a változott pixelek” rajz egyszerűsített modell.
  - Átfedés: a hang fizikája (rezgésszám, hangerő) a fizika-7-8/12-hullam-hang leckében; a pixel és az RGB a
    13-pixel leckében; a bit, bájt, kB, MB a 17-szamitogep leckében. Az órán használt hang- és videóprogramban a
    mintavételt és a bitmélységet a mentés/exportálás beállításainál találod.
-->
