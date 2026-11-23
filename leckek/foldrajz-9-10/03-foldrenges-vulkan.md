# Miért éppen ott? – földrengés, vulkán és cunami a lemezszegélyen
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 2. A kőzetburok

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/03-foldrenges-vulkan.md
  A számok az animációt is vezérlik (pl. a katalógus évei, a hullámsebességek, a magnitúdó-kitevő).
-->

## Közös

### Feliratok
- modell: modell
- vázlatos: vázlatos
- illusztráció: illusztráció
- becslés: becslés
- torzítás: függőleges torzítás #×
- méretarányos: méretarányos
- lépték: # km
- mélység km: mélység (km)
- sekély: sekély fészek (< 70 km)
- közepes: közepes (70–300 km)
- mély: mély fészek (> 300 km)
- lemezhatár: lemezhatár
- holocén vulkán: vulkán (az utolsó 11 700 évben működött)
- forrás rengés: Forrás: USGS ComCat · lemezhatárok: P. Bird (2003), PB2002 · Made with Natural Earth
- forrás vulkán: Forrás: NOAA NCEI vulkánadatbázis · lemezhatárok: P. Bird (2003), PB2002
- forrás szelvény: Domborzat: NOAA ETOPO 2022 · rengések: USGS ComCat (é. sz. 35–41,5° sáv)
- Japán-árok: Japán-árok
- Honsú: Honsú
- Japán-tenger: Japán-tenger
- Csendes-óceán: Csendes-óceán
- Csendes-óceáni-lemez: Csendes-óceáni-lemez
- felső lemez: a fölötte lévő lemez
- óceáni kéreg: óceáni kéreg (bazalt)
- kontinentális kéreg: kontinentális kéreg (gránitos)
- kőzetlemez: kőzetlemez (litoszféra)
- köpeny: köpeny (szilárd, lassan folyik)
- víz: tenger

### Adatok
<!-- forrás (az alábbiakra): USGS ComCat FDSN, shared/foldrajz/rengesek.js (lekérdezve: 2026-11-23, közkincs); a mélységi osztályok a szokásos USGS-beosztás szerint -->
- rengéskatalógus: USGS ComCat
- katalógus kezdete: 1975
- katalógus vége: 2024
- küszöb-magnitúdó: 6,0
- rengések száma: 6992
- sekély határa: 70 km
- mély határa: 300 km
- lemezhatár-adat: PB2002 (Bird 2003)
<!-- forrás: P. Bird (2003), An updated digital model of plate boundaries, G³ 4(3), 1027, doi:10.1029/2001GC000252; GeoJSON: H. Ahlenius (Nordpil), github.com/fraxen/tectonicplates – ODC-BY 1.0, a megjelölés kötelező (a vásznon a forrássorban) -->
- vulkánadatbázis: NOAA NCEI
<!-- forrás: NOAA NCEI / WDS Global Volcano Locations Database, doi:10.7289/V5TB14V7, shared/foldrajz/vulkanok.js (lekérdezve: 2026-11-23, közkincs) -->
- domborzati szelvény: NOAA ETOPO 2022
<!-- forrás: NOAA NCEI ETOPO 2022 15″, shared/foldrajz/szelveny-japan.js, é. sz. 38,3°, k. h. 128–150° (lekérdezve: 2026-11-23, közkincs) -->

## 1. Hol rengett 50 év alatt?
A gömbön az {katalógus kezdete} és {katalógus vége} közötti {rengések száma} **földrengés** látszik, mind legalább 6-os erősségű. Szétszórva? Nem: keskeny sávokba rendeződnek – a **kőzetlemezek** szegélyére.

A legnagyobb rengések {tűzgyűrű aránya}-a a Csendes-óceán peremén, a ==tűzgyűrűn== pattant ki.

> megjegyzés: Kapcsold be a lemezhatárokat, és húzd a gömböt! A pont színe a rengés fészkének mélységét jelzi.

### Feliratok
- tűzgyűrű: Csendes-óceáni tűzgyűrű
- Atlanti-hátság: Közép-atlanti-hátság
- Himalája: Himalája
- Andok: Andok
- évszám: #
- darabszám: # rengés, M ≥ #
- fészekmélység: a fészek mélysége
- gomb lemezhatár be: Lemezhatárok mutatása
- gomb lemezhatár ki: Lemezhatárok elrejtése
- húzd: húzd a gömböt

### Adatok
- tűzgyűrű aránya: kb. 81 %
<!-- forrás: USGS, Where do earthquakes occur? (usgs.gov/faqs/where-do-earthquakes-occur), lekérdezve: 2026-11-23 – „about 81 percent of our planet's largest earthquakes”; nem a lecke adatából számolva -->

## 2. Egyre mélyebben: a lebukó lemez
Vágjuk ketté a Földet Japánnál! A **mélytengeri árok** mentén a Csendes-óceáni-lemez a másik lemez alá bukik: ez az **alábukás**.

A rengések egy ferde sávban egyre mélyebbről jönnek – ez a ==lebukó lemez==, 600 km mélyig. Méretarányosan az árok csak egy karcolás.

> megjegyzés: Nagyíts a felső 60 km-re: ott, a két lemez határán pattant ki a Tóhoku-rengés.

### Feliratok
- szelvény: szelvény: é. sz. 38,3°
- Wadati–Benioff-öv: a rengések sávja (Wadati–Benioff-öv)
- illesztett: a lemez felszíne (a rengésekre illesztve)
- Tóhoku: Tóhoku, 2011
- gomb nagyítás: Nagyítás: a felső 60 km
- gomb egész: Vissza: a teljes szelvény

### Adatok
- Tóhoku-rengés: 2011. március 11.
<!-- forrás: USGS, M 9.1 – 2011 Great Tohoku Earthquake (earthquake.usgs.gov/earthquakes/eventpage/official20110311054624120_30), lekérdezve: 2026-11-23 -->
- Tóhoku helye: 38,30° É, 142,37° K
<!-- forrás: USGS (38,297° É, 142,373° K), lekérdezve: 2026-11-23 -->
- Tóhoku mélysége: 29 km
<!-- forrás: USGS ComCat, lekérdezve: 2026-11-23 -->

## 3. Miért pattan? A feszültség és a kioldás
A lemez évente {lemezsebesség} sebességgel mozog, de a határon a kőzetek összeakadnak, és rugóként feszülnek – évszázadokig.

Ha a feszültség legyőzi a súrlódást, a törés ==egy pillanat alatt== elcsúszik: ez a rengés. Aztán elölről.

> megjegyzés: Erősebb tapadás: ritkább, de nagyobb rengés.

### Feliratok
- húzó lemez: a mozgó lemez
- rugó: rugalmas kőzet
- tömb: összeakadt törés
- álló lemez: a másik lemez
- feszültség: feszültség
- idő év: idő (év)
- rengés: RENGÉS!
- rengésjel: szeizmográf
- ciklus: rengés kb. # évente
- csúszás: egyszerre kb. # m csúszás
- összesen: összesen: # m / # év
- csúszka tapadás: A törés tapadása
- csúszka év: # évente pattan

### Adatok
- lemezsebesség: kb. 8 cm/év
<!-- forrás: GSI (Geospatial Information Authority of Japan), Interplate coupling estimated from continuous GPS observation (gsi.go.jp/cais/tectonics_plate_coupling-e.html), lekérdezve: 2026-11-23 – „over 80 mm/yr”, a Japán-árok közeledési sebessége é. sz. 38° körül -->
- legrövidebb ciklus: 100 év (modell)
<!-- forrás: modellparaméter; a 600 év × 8 cm/év = 48 m nagyságrendileg a Tóhoku-rengés legnagyobb csúszása (kb. 50 m) -->
- leghosszabb ciklus: 600 év (modell)
<!-- forrás: modellparaméter -->
- kezdő ciklus: 250 év (modell)
<!-- forrás: modellparaméter -->

## 4. Tévhit: a 8-as kétszer akkora, mint a 4-es?
A **magnitúdó** a rengés méretét méri, de nem egyenletes skálán. Egy egységnyi növekedés ==tízszer akkora kitérést== jelent a szeizmográfon, és kb. {energia-szorzó}-szoros energiát.

A 8-as rengés tehát nem kétszer, hanem egymilliószor annyi energiát szabadít fel, mint a 4-es.

> megjegyzés: Húzd a csúszkát! A kockák térfogata az energiával arányos.

### Feliratok
- csúszka M: Magnitúdó (M)
- tévhit: Tévhit: M 8 = 2 × M 4
- valójában: Valójában: # × annyi energia
- kocka M: M #
- kocka arány 1: a választott rengés
- kocka arány 2: 1/# annyi energia
- létra cím: minden lépés kb. ×# energia
- skála: log. skála
- Dunaharaszti: Dunaharaszti, #
- Törökország: Törökország, #
- Tóhoku-létra: Tóhoku, #
- Szumátra: Szumátra, #
- Valdivia: Valdivia (Chile), #
- választott: választott: M #
- ezer: ezer
- millió: millió
- milliárd: milliárd
- energia-sor: # × a 4-es rengés energiája

### Adatok
- energia-kitevő: 1,5
<!-- forrás: Gutenberg–Richter energia–magnitúdó összefüggés, lg E = 1,5 M + 4,8 (E joule-ban) – közismert; USGS: The Science of Earthquakes -->
- energia-szorzó: 32
<!-- forrás: 10^1,5 ≈ 31,6 – a lecke ellenőrzi, hogy egyezik-e az energia-kitevővel -->
- Dunaharaszti magnitúdója: 5,6
<!-- forrás: Kövesligethy Radó Szeizmológiai Obszervatórium (M 5,6); az USGS ISC-GEM katalógusa Mw 5,8-at ad – ellenőrizendő, melyiket tanítsuk -->
- Dunaharaszti-rengés: 1956. január 12.
<!-- forrás: Kövesligethy Radó Szeizmológiai Obszervatórium; en.wikipedia.org/wiki/1956_Budapest_earthquake, lekérdezve: 2026-11-23 -->
- Törökország magnitúdója: 7,8
<!-- forrás: USGS, M 7.8 – Pazarcık earthquake, Kahramanmaraş, 2023-02-06, lekérdezve: 2026-11-23 -->
- törökországi rengés: 2023. február 6.
<!-- forrás: USGS, lekérdezve: 2026-11-23 -->
- Tóhoku magnitúdója: 9,1
<!-- forrás: USGS (Mw 9,1; a Japán Meteorológiai Ügynökség Mw 9,0-t ad) -->
- Szumátra magnitúdója: 9,1
<!-- forrás: USGS (Mw 9,1; más becslések 9,1–9,3) -->
- szumátrai rengés: 2004. december 26.
<!-- forrás: USGS, lekérdezve: 2026-11-23 -->
- Valdivia magnitúdója: 9,5
<!-- forrás: USGS, a legnagyobb műszeresen mért rengés (Mw 9,5) -->
- valdiviai rengés: 1960. május 22.
<!-- forrás: USGS, lekérdezve: 2026-11-23 -->
- kezdő magnitúdó: 7,0
<!-- forrás: a csúszka kezdőértéke (nem tényadat) -->

## 5. Honnan tudjuk? Három szeizmográf
A rengésből két hullám indul: a gyorsabb **P-hullám** ({P-hullám sebessége}) és a lassabb **S-hullám** ({S-hullám sebessége}). Minél messzebb van az állomás, annál később ér oda az S a P után.

Az S–P időből jön a távolság, ==három állomás köréből a hely==.

> megjegyzés: Minden másodpercnyi S–P idő kb. 8 km. Az USGS-katalógust világszerte sok ezer állomás adata adja.

### Feliratok
- állomás: #. állomás
- P-hullám: P-hullám
- S-hullám: S-hullám
- S–P: S–P = # s
- távolság: → # km
- epicentrum: itt pattant ki (epicentrum)
- idő s: idő a rengés óta (s)
- gomb új rengés: Új rengés
- térkép: felülnézet

### Adatok
- P-hullám sebessége: kb. 6 km/s
<!-- forrás: közismert átlagérték a földkéregben (5,5–7 km/s); a modell állandó sebességgel számol -->
- S-hullám sebessége: kb. 3,5 km/s
<!-- forrás: közismert átlagérték a földkéregben (3–4 km/s) -->

## 6. Vulkánok: miért éppen ott?
A **vulkánok** is a lemezszegélyeken sorakoznak. Az alábukó lemezből {olvadás mélysége} mélyen víz szabadul fel.

A víz csökkenti a köpeny olvadáspontját, a kőzet ==részben megolvad==: így lesz **magma**. A könnyebb magma felszáll, az árok mögött vulkánsor épül.

> megjegyzés: Izlandon a széttartó lemezek alatt csökken a nyomás, Hawaii alatt forró köpenyanyag áramlik fel – ott is olvad a kőzet.

### Feliratok
- víz szabadul: víz szabadul fel
- olvadás: a köpeny részben megolvad
- magma felszáll: magma
- vulkáni ív: vulkánsor
- olvadás mélysége felirat: kb. # km
- Japán: Japán – alábukás
- Izland: Izland – szétnyíló hátság
- Hawaii: Hawaii – forró pont
- gomb Japán: Japán
- gomb Izland: Izland
- gomb Hawaii: Hawaii

### Adatok
- olvadás mélysége: kb. 100 km
<!-- forrás: a vulkánsor alatt a lebukó lemez felszíne átlagosan kb. 100 km mélyen van (England, Engdahl & Thompson 2004, GJI 156); a lecke illesztett lemezfelszíne itt kb. 110 km -->
- Japán helye: 38,3° É, 141° K
<!-- forrás: közismert (térképi hely) -->
- Izland helye: 64,8° É, 18° Ny
<!-- forrás: közismert (térképi hely) -->
- Hawaii helye: 19,5° É, 155,5° Ny
<!-- forrás: közismert (térképi hely) -->

## 7. Kétféle kitörés: híg és robbanásos
A magma összetétele dönt. A SiO₂-ban szegény **bazaltos magma** forró és híg: a gáz könnyen kiszökik, a **láva** szétfolyik, lapos pajzsvulkán épül.

A SiO₂-ban gazdag magma sűrűn folyik, a gáz bennreked, és ==robbanás== tépi szét – meredek rétegvulkán lesz.

> megjegyzés: Tévhit: minden vulkán robbanásos. Mount St. Helens ({St. Helens kitörése}) {St. Helens magasságvesztése}-rel lett alacsonyabb.

### Feliratok
- csúszka SiO2: A magma SiO₂-tartalma
- bazaltos: bazaltos magma
- andezites: andezites magma
- riolitos: riolitos magma
- híg: híg, a gáz kiszökik
- sűrű: sűrűn folyik, a gáz bennreked
- pajzsvulkán: pajzsvulkán
- rétegvulkán: rétegvulkán
- láva: láva
- hamufelhő: hamu- és gázfelhő
- magmakamra: magmakamra
- kürtő: kürtő
- gázbuborék: gázbuborék
- SiO2 érték: SiO₂: kb. # %
- hőmérséklet: # °C
- példák híg: pl. Hawaii, Izland, Etna
- példák sűrű: pl. Mount St. Helens, Vezúv, Popocatépetl
- sáv híg: híg
- sáv sűrű: sűrű

### Adatok
- bazalt felső határa: 52 %
<!-- forrás: a vulkáni kőzetek TAS-osztályozása (Le Bas et al. 1986): bazalt 45–52 % SiO₂ -->
- andezit felső határa: 63 %
<!-- forrás: TAS-osztályozás: andezit 57–63 % (bazaltos andezit 52–57 %); a lecke az 52–63 %-ot „andezites”-nek mutatja -->
- bazaltos hőmérséklet: 1100–1200 °C
<!-- forrás: tankönyvi érték (kb.); USGS Volcano Hazards Program: a bazaltos láva kb. 1100–1200 °C – ellenőrizendő -->
- sűrű magma hőmérséklete: 800–1000 °C
<!-- forrás: tankönyvi érték az andezites–riolitos magmára (kb.); a riolitos ennél hidegebb is lehet (kb. 700–850 °C) – ellenőrizendő -->
- St. Helens kitörése: 1980. május 18.
<!-- forrás: USGS Fact Sheet 036-00, pubs.usgs.gov/fs/2000/fs036-00, lekérdezve: 2026-11-23 -->
- St. Helens magasságvesztése: kb. 400 m
<!-- forrás: USGS FS 036-00: 9677 ft → 8363 ft, 1314 ft ≈ 400 m; 57 halálos áldozat -->
- kezdő SiO2: 50 %
<!-- forrás: a csúszka kezdőértéke (nem tényadat) -->

## 8. Cunami: gyors a mélyben, magas a parton
A tenger alatti rengés megemeli a teljes vízoszlopot. A **cunami** sebessége a mélységtől függ: c = √(g·h). A mély óceánon repülőgép-sebességű, de alig 1 m magas.

A sekély parton lelassul, a víz feltorlódik, és ==magasra csap fel==.

> megjegyzés: 2011-ben a víz Japánban {Tóhoku felfutás} magasra futott fel. Erős rengés a parton: azonnal menj magaslatra!

### Feliratok
- csúszka mélység: Vízmélység
- képlet: c = √(g·h)
- sebesség: c ≈ # m/s ≈ # km/h
- hullámmagasság: magasság ≈ # m
- repülő: mint egy repülőgép
- autó: mint egy autó
- futó: még mindig gyorsabb egy futónál
- vízoszlop: a teljes vízoszlop mozog
- hullám nem méretarányos: a hullám magassága nagyítva
- part: part (Ósika-félsziget)
- eltelt: # perccel a rengés után
- itt: itt # m mély

### Adatok
- nehézségi gyorsulás: 9,81 m/s²
<!-- forrás: közismert -->
- kiinduló mélység: 4000 m
<!-- forrás: modellparaméter (a mély óceán jellemző mélysége) -->
- kiinduló hullámmagasság: 1 m (modell)
<!-- forrás: modellparaméter; a magasság a Green-törvény szerint nő (H ~ h^−1/4) – a felfutást és a törést a modell nem számolja -->
- legkisebb mélység: 10 m
<!-- forrás: modellparaméter (a csúszka alsó határa) -->
- Tóhoku felfutás: kb. 40 m
<!-- forrás: NOAA NCEI, On this day: 2011 Japan earthquake and tsunami (ncei.noaa.gov/news/day-2011-japan-earthquake-and-tsunami), lekérdezve: 2026-11-23 – „almost 40 meters”, Ivate prefektúra -->

## 9. Összefoglalás: veszély és kockázat
A rengést és a kitörést nem tudjuk megakadályozni, és ==napra pontosan nem jósolható==. A kockázat viszont csökkenthető: veszélytérképpel, rengésálló épülettel, korai riasztással és gyakorlással.

Magyarországon is van rengés: {Dunaharaszti-rengés}, M {Dunaharaszti magnitúdója}.

> megjegyzés: Beszéljétek meg: mit érezhetnek és mit tehetnek az emberek rengéskor, kitöréskor, cunaminál?

### Feliratok
- ö cím 1: Hol?
- ö szöveg 1: a lemezszegélyeken – tűzgyűrű
- ö cím 2: Miért?
- ö szöveg 2: összeakadt lemezek, hirtelen csúszás
- ö cím 3: Mekkora?
- ö szöveg 3: +1 magnitúdó ≈ 32× energia
- ö cím 4: Vulkán
- ö szöveg 4: víz → olvadás; híg vagy robbanásos
- ö cím 5: Cunami
- ö szöveg 5: c = √(g·h): a parton lassul, magasodik
- ö cím 6: Honnan tudjuk?
- ö szöveg 6: szeizmográfok: S–P idő → távolság
- teendő cím: Ha földrengés van:
- teendő 1: Le a földre!
- teendő 2: Bújj asztal alá!
- teendő 3: Kapaszkodj!
- teendő 4: Parton: azonnal magaslatra!
- tévhit jóslás: Napra pontos jóslás nincs – csak veszélytérkép és másodpercekkel előbbi riasztás.
- Magyarország cím: Magyarországon is:
- Magyarország sor: Dunaharaszti, # · M #
- Csomád sor: a Kárpát-medence legutolsó kitörése: Csomád, #

### Adatok
- Csomád utolsó kitörése: kb. 32 ezer éve
<!-- forrás: Harangi Sz. és mtsai, cirkon-kormeghatározás (Origo, 2023. dec.; Bull. Volcanol. 2015) – „1–2 ezer éves hibahatárral 32 ezer éve”; a terv „100–200 ezer éve” értéke elavult -->

<!-- Vitatott / bizonytalan pontok a tanári review-hoz:
  - Dunaharaszti 1956: a magyar obszervatórium M 5,6-ot, az USGS ISC-GEM Mw 5,8-at ad. A lecke a magyar értéket mutatja.
  - Tóhoku magnitúdója: USGS Mw 9,1, JMA Mw 9,0. Áldozatok (a lecke nem írja ki): 15 901 halott és 2519 eltűnt
    (Japán Rendőrség, 2026. március, nippon.com), kb. 18 400 fő.
  - A „81 %” az USGS általános megállapítása a legnagyobb rengésekről, nem a vásznon látható M ≥ 6-os katalógusból számolt arány.
  - A 2. lépés szelvényére az é. sz. 35–41,5° sávban lévő rengéseket vetítettük, a Japán-árok irányával (kb. É 16° K)
    párhuzamosan eltolva; a lemezfelszín ezekre illesztett harmadfokú görbe. A fölötte lévő lemez a PB2002 szerint az
    Ohotszki-lemez (a tanterv 9 nagy lemeze közül az Észak-amerikai-lemez része) – ezért a felirat semleges.
  - A kéreg vastagsága (kb. 30 km), a lemez vastagsága (kb. 90 km) a szelvényen vázlatos.
  - Magmahőmérsékletek: forrásonként eltérnek; a riolitos magma 700–850 °C is lehet.
  - A Green-törvény (H ~ h^−1/4) csak a parttól távol érvényes; a felfutást (Tóhoku: kb. 40 m) a modell nem számolja.
  - A rugós modell ciklusideje (100–600 év) didaktikus: a valódi rengések nem szabályos időközönként jönnek.
-->
