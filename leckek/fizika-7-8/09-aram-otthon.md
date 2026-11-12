# Miért old le a biztosíték? – Joule-hő, teljesítmény, fogyasztás
tantárgy: Fizika · évfolyam: 7–8. · témakör: 6. Elektromosság a háztartásban (+ 2. Az energia)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/09-aram-otthon.md

  Előzmény: 08-aramkor (töltés, áram, feszültség, Ohm-törvény). A rajzok (vezeték, elektron-pöttyök,
  mérők, kártyák) annak a leckének a vizuális nyelvét követik.

  Modell és egyszerűsítések:
  - A konnektorban VÁLTAKOZÓ áram van: a pöttyök (elektronok) oda-vissza lengenek, a kitérés arányos
    az áramerősséggel (lassítva; valójában 50 lengés másodpercenként). A 230 V és az áramerősségek
    effektív értékek; a készülékeket ohmos fogyasztónak vesszük: I = P / U.
  - Az áramerősségeket 0,01 A-re kerekítve adjuk össze; a kismegszakító ugyanebből az összegből dönt,
    és PONTOSAN a névleges érték fölött old le. A valódi (hőkioldós) kismegszakító kis túllépésnél csak
    percek múlva old le, nagy túlterhelésnél gyorsabban – a leckében egységesen kb. 1 s után.
  - 1. lépés: hőveszteség nélkül számolunk (Q = c · m · ΔT); 1 kg víz 20 → 100 °C: 336 000 J,
    2000 W-tal kb. 2,8 perc ≈ 3 perc. A vezeték színe/izzása csak jelzi a melegedést.
  - 6. lépés: rövidzárban I = U / R_hurok (a hurok: a falban futó vezeték + a hálózat ellenállása,
    tipikusan néhány tized ohm). A vezeték melegedése hőveszteség nélkül, 1,5 mm²-es rézre:
    ΔT/t = I²·ρ / (A²·c·sűrűség) ≈ 22 °C/s 100 A-nél (ez I²-tel nő: 460 A-nél ≈ 470 °C/s).
    A PVC-szigetelés rövidzárlati határhőmérséklete kb. 160 °C. A „B” jelű kismegszakító ekkora
    áramnál elektromágnesesen, néhány ezredmásodperc alatt old le.
  - 7. lépés: FI-relé (áram-védőkapcsoló) 30 mA-es; szabvány szerint névleges hibaáramnál ≤ 0,3 s,
    5-szörösénél (150 mA) ≤ 40 ms alatt kapcsol le. A FI-relé NEM korlátozza az áramot, csak gyorsan
    lekapcsol: rövid áramütést ilyenkor is érezhet az ember.
  - 7–8. lépés: a test ellenállása kb. 1000 Ω – legrosszabb esetre (nedves bőr, nagy érintkezési
    felület) számolva. Száraz bőrön, kis feszültségnél nagyobb, de 230 V-on a bőr ellenállása
    lecsökken. Az áramerősség-határok 50 Hz-es váltakozó áramra vonatkoznak (MSZ EN / IEC 60479
    alapján, kerekítve): ≈ 1 mA érezhető, ≈ 10 mA felett nem lehet elengedni, 50–100 mA
    szívkamra-fibrillációt okozhat. Az 50 V-os érintésvédelmi határ ugyanebből jön: 50 V / 1000 Ω = 50 mA.

  FRISSÍTENDŐ ÉRTÉKEK (évről évre változnak, kérjük, a tanár ellenőrizze):
  - áram ára: a lakossági (rezsicsökkentett) ár kerekítve, az átlagfogyasztásig (kb. 2523 kWh/év).
  - készenléti teljesítmény: régebbi készülékekre jellemző érték; az újakra uniós előírás szerint ≤ 0,5 W.
-->

## Közös

### Feliratok
- konnektor: konnektor
- vízforraló: vízforraló
- hajszárító: hajszárító
- mikró: mikró
- tévé: tévé
- lámpa: LED-lámpa
- áramerősség: áramerősség
- feszültség: feszültség
- teljesítmény: teljesítmény
- ellenállás: ellenállás
- lassítva: lassítva: valójában 50 lengés másodpercenként
- kismegszakító: kismegszakító
- FI-relé: FI-relé
- leoldott: LEOLDOTT
- bekapcsolva: bekapcsolva
- áramár: áramár

### Adatok
- hálózati feszültség: 230 V
- vízforraló teljesítménye: 2000 W
- hajszárító teljesítménye: 1800 W
- mikró teljesítménye: 1200 W
- tévé teljesítménye: 100 W
- LED-lámpa teljesítménye: 9 W
- kismegszakító névleges árama: 16 A
- áram ára: 36 Ft/kWh
- az emberi test ellenállása: 1000 Ω
- vezetékhurok ellenállása: 0,5 Ω

## 1. A fűtőszál melegszik
Az áram nem fogy el, de **energiát** ad át (08. lecke). Hol?

A vezetékben és a fűtőszálban ugyanakkora az áram. A vékony fűtőszálban az elektronok újra meg újra meglökik az atomtörzseket, azok erősebben rezegnek: ==ahol nagy az ellenállás, ott keletkezik a hő==. Ez a **Joule-hő**.

> megjegyzés: Ezen működik a vasaló, a hajszárító és a vízmelegítő is.

### Feliratok
- be-ki gomb: Bekapcsol / kikapcsol
- tápvezeték: tápvezeték
- fűtőszál: fűtőszál
- vezeték: vezeték
- áram mindkettőben: áram mindkettőben
- hő 1 s alatt: hő 1 s alatt
- nagyítás: nagyítás: a fűtőszál belseje
- meglökik: elektronok lökik az atomtörzseket
- melegítés ideje: melegítés ideje:
- felgyorsítva: felgyorsítva 40×
- forr: forr!

### Adatok
- tápvezeték ellenállása: 0,07 Ω
- víz tömege: 1,0 kg
- víz fajhője: 4200 J/(kg·°C)
- kezdeti vízhőmérséklet: 20 °C

## 2. Teljesítmény: P = U · I
Minden konnektorban **{hálózati feszültség}** van. Mégis: a vízforraló több mint kétszázszor akkora áramot vesz fel, mint a LED-lámpa.

A **teljesítmény**: mennyi energiát alakít át a készülék másodpercenként. Mértékegysége a watt (1 W = 1 J/s).

> megjegyzés: Tévhit: „csak a feszültség számít”. A feszültség ugyanaz – ==az áram dönti el== a teljesítményt.

### Feliratok
- fogyasztásmérő: fogyasztásmérő
- áram 230 V-on: Mekkora áramot vesz fel 230 V-on?

## 3. kWh és forint
**Energia = teljesítmény × idő.** Otthon kilowattórában (kWh) mérjük, ezt fizetjük ki.

Tévhit: a nagyobb teljesítményű készülék mindig többet fogyaszt. ==Az idő is számít!== A tévé 1 óra alatt ugyanannyi energiát használ, mint a vízforraló 3 perc alatt.

képlet: E = P · t

> megjegyzés: Húzd a tévé idejét! Hány perc tévézés ér fel két forralással?

### Feliratok
- tengely P: teljesítmény (W)
- tengely t: idő (perc)
- húzd: húzd!
- ugyanannyi energia: ugyanannyi energia!
- egy cella: egy cella = 0,01 kWh
- kWh jelentése: 1 kWh = 1000 W · 1 óra
- tévé csúszka: A tévézés ideje

### Adatok
- vízforralás ideje: 3 perc
- tévézés ideje: 60 perc

## 4. Izzó, LED, készenlét
A hagyományos izzó Joule-hővel világít: a szála izzásig forrósodik. Az energia nagy része **hő** lesz, nem fény. A LED ugyanannyi fényt {LED-lámpa teljesítménye} teljesítménnyel ad.

Tévhit: készenlétben a tévé nem fogyaszt. ==A piros lámpa egész évben, éjjel-nappal fogyaszt!==

> megjegyzés: Állítsd be, hány órát világít naponta a lámpa! Melyik éri meg?

### Feliratok
- izzó: hagyományos izzó
- ugyanannyi fény: ugyanannyi fény
- főleg hő: főleg hő
- kevés hő: kevés hő
- készenlét: tévé készenlétben
- éjjel-nappal: éjjel-nappal, egész évben
- egy év alatt: Egy év alatt
- napi csúszka: Napi világítás
- naponta: óra/nap · 365 nap

### Adatok
- izzólámpa teljesítménye: 60 W
- napi világítás: 3 óra
- készenléti teljesítmény: 1,0 W

## 5. Túlterhelés
A konnektorok **párhuzamosan** vannak kötve: mindegyik 230 V-ot kap. A közös vezetékben ==az áramok összeadódnak==.

Nagyobb áram → melegebb vezeték. Ha az áram {kismegszakító névleges árama} fölé nő, a **kismegszakító** lekapcsol, mielőtt a vezeték túlmelegedne.

> megjegyzés: A valódi kismegszakító kis túllépésnél csak percek múlva old le.

### Feliratok
- konyha: konyha
- fürdő: fürdő
- nappali: nappali
- közös vezetékben: a közös vezetékben
- visszakapcsol gomb: Visszakapcsolás
- túlterhelés: Túlterhelés

## 6. Rövidzár
Ha megsérül a szigetelés, a két ér összeérhet. Az áram ekkor **megkerüli** a lámpát: szinte nincs ellenállás, ezért I = U / R ==óriási==.

A kismegszakító ezt {kioldási idő rövidzárnál} alatt lekapcsolja. Nélküle a vezeték pillanatok alatt felforrósodna, és meggyulladhatna a szigetelés.

> megjegyzés: Az időtengely lassított: minden osztás tízszer annyi idő.

### Feliratok
- rövidzár gomb: Rövidzár!
- javítás gomb: Javítás és visszakapcsolás
- nélküle gomb: Kismegszakító nélkül?
- sérült szigetelés: sérült szigetelés
- rövidzár: Rövidzár!
- vezeték hőmérséklete: a vezeték hőmérséklete
- zárlat óta: a zárlat óta eltelt idő (lassítva)
- alig melegedett: Leoldott – a vezeték alig melegedett
- tűzveszély: Ég a szigetelés – tűzveszély!
- kismegszakító nélkül: kismegszakító nélkül
- állólámpa: állólámpa

### Adatok
- kioldási idő rövidzárnál: 10 ms
- a vezeték melegedése 100 A-nél: 22 °C/s
- a szigetelés tűréshatára: 160 °C

## 7. Földelés és FI-relé
Hibás mosógép: a fázis hozzáér a fémházhoz. Ha megérinted, rajtad át folyik áram a földbe.

Tévhit: a biztosíték az embert védi. Ez az áram ==a kismegszakítónak túl kicsi==. Véd a **földelés**: a hibaáram a védővezetéken folyik el, leold a kismegszakító. És a **FI-relé**: lekapcsol, ha {FI-relé érzékenysége}-nél több nem jön vissza.

> megjegyzés: Próbáld ki a négy esetet!

### Feliratok
- földelés gomb: Földelés be / ki
- FI gomb: FI-relé be / ki
- mosógép: mosógép (fémház)
- zárlat a házra: zárlat a házra!
- a ház: a ház
- védővezeték: védővezeték
- nincs bekötve: nincs bekötve
- fázis: fázis
- nulla: nulla
- kimenő áram: kimenő áram (fázis)
- visszajövő áram: visszajövő áram (nulla)
- különbség: különbség
- nincs FI: nincs FI-relé
- földelő: földelés
- működik: A gép rendben működik.
- életveszély: ÉLETVESZÉLY: áram a testen át!
- nem old le: A kismegszakító nem old le
- FI leold: A FI-relé lekapcsolt
- biztonságos: Leoldott – a ház nem veszélyes
- a föld visszavezeti: a föld visszavezeti az áramot

### Adatok
- mosógép teljesítménye: 2000 W
- FI-relé érzékenysége: 30 mA
- FI-relé kioldási ideje: 40 ms

## 8. Áramütés
Nem a feszültség „üt”, hanem a testen átfolyó **áram**. Ezt a feszültség hajtja át: I = U / R. Minél tovább tart, annál veszélyesebb.

{érezhető áram} érezhető, {elengedési határ} felett nem tudod elengedni, {fibrillációs áram} felett leállhat a szív. ==A 230 V életveszélyes!==

> megjegyzés: Soha ne kísérletezz konnektorral, sérült kábellel! A laposelem (4,5 V) csak kis áramot hajt át rajtad.

### Feliratok
- feszültség csúszka: Érintési feszültség
- konnektor gomb: Konnektor: 230 V
- nem érzed: nem érzed
- érezhető: érezhető, bizsergés
- nem tudod elengedni: görcs: nem tudod elengedni
- fibrilláció: szívkamra-fibrilláció
- FI-relé határa: a FI-relé leold
- legrosszabb eset: test: nedves bőr, legrosszabb eset
- a testen át: a testen át

### Adatok
- érezhető áram: 1 mA
- elengedési határ: 10 mA
- fibrillációs áram: 50 mA

## 9. Összefoglalás
- **Joule-hő**: az áram melegíti a vezetőt, leginkább ott, ahol nagy az ellenállás.
- Teljesítmény: **P = U · I**. Energia: **E = P · t** – ebből lesz a számla.
- A kismegszakító ==a vezetéket védi== túlterhelés és rövidzár ellen.
- Az embert a **földelés** és a **FI-relé** védi.

> megjegyzés: Mennyibe kerül egy évig naponta háromszor forralni a {vízforraló teljesítménye}-os vízforralóval?

### Feliratok
- összegzés Joule: Joule-hő
- összegzés Joule 2: ott keletkezik, ahol nagy az ellenállás
- összegzés P: teljesítmény (W) = feszültség × áram
- összegzés E: energia (kWh) = teljesítmény × idő
- összegzés védelem 1: kismegszakító: a vezetéket védi
- összegzés védelem 2: földelés + FI-relé: az embert védi
- tanulság: Az áram hőt termel és pénzbe kerül – a 230 V pedig életveszélyes.
