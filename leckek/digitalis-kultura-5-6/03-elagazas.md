# Melyik ládába kerül az alma? – feltétel és elágazás
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 1. Algoritmizálás és blokkprogramozás

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/03-elagazas.md

  A blokkok felirata a „… blokk” kulcsokból jön; a # a paraméter helye (szám, láda, feltétel).
  Az almák színe a „… színei” sorokban pontosvesszővel elválasztva áll; minden szín pontosan
  az egyik „… szín” felirat legyen (piros, zöld, sárga, zöld-piros) – különben a lecke hibát jelez.
  A „Tippelj!” lépésekben (5., 6.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  Hogy melyik alma melyik ládába kerül, azt mindig a program számolja ki az Adatokból – a ládák
  tartalma, a darabszámok és az IGAZ / HAMIS jelek nincsenek kézzel beírva.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- modell bélyeg: modell
- kitalált bélyeg: kitalált almák
- program felirat: A PROGRAM
- gép felirat: A VÁLOGATÓGÉP FELÜLRŐL
- fa felirat: DÖNTÉSI FA
- ha-különben blokk: ha # akkor
- ha-különben közép: különben
- ha-különben vége: elágazás vége
- ha blokk: ha # akkor
- ha vége: elágazás vége
- > blokk: # > # cm
- ≥ blokk: # ≥ # cm
- = blokk: # = #
- és blokk: # és #
- vagy blokk: # vagy #
- tereld blokk: tereld a(z) # ládába
- méret opció: méret
- szín opció: szín
- A opció: A
- B opció: B
- C opció: C
- piros szín: piros
- zöld szín: zöld
- sárga szín: sárga
- zöld-piros szín: zöld-piros
- igaz felirat: IGAZ
- hamis felirat: HAMIS
- start felirat: start
- stop felirat: vége
- futtatás gomb: Futtatás
- egy lépés gomb: Egy lépés
- alaphelyzet gomb: Alaphelyzet
- sebesség csúszka: Sebesség
- lassú felirat: lassú
- normál felirat: normál
- gyors felirat: gyors
- azonnal felirat: azonnal
- kapu felirat: mérőkapu
- láda felirat: # láda
- darab felirat: # db
- szalag vége felirat: szalag vége
- mérés felirat: # · #
- összevetés felirat: # # #?
- méret csúszka: Az alma mérete
- szín gomb: Másik szín
- almasor színei: piros; zöld; piros; sárga; zöld; piros

### Adatok
- almasor méretei: 6,5; 8,2; 7; 7,5; 5,5; 9 cm
<!-- forrás: kitalált példa – a valódi étkezési almák átmérője jellemzően kb. 6–9 cm; a 7 cm a lecke saját küszöbe, nem szabvány -->
- küszöb: 7 cm
<!-- forrás: kitalált példa (a lecke válogatási szabálya; a valódi almaválogatók is átmérő vagy tömeg szerint osztályoznak, de a határokat a megrendelő szabja meg) -->

## 1. Döntések körülöttünk
Reggel: **ha** esik az eső, viszed az esernyőt, **különben** otthon hagyod. A válogatógép is így dönt – minden almánál. ==A gép nem „látja”, melyik alma való hová: a program szerint dönt.== Kapcsold át az időjárást!

> megjegyzés: Kérdezd meg: milyen „ha… akkor…” döntést hoztál ma?

### Feliratok
- esik? blokk: esik az eső
- esernyő lépés: vidd az esernyőt
- otthon lépés: hagyd otthon az esernyőt
- reggel felirat: REGGEL, INDULÁS ELŐTT
- eső gomb: Időjárás: eső / napsütés
- esik felirat: esik
- nem esik felirat: süt a nap
- kérdés felirat: Mi alapján választ ládát a gép?

## 2. Feltétel: IGAZ vagy HAMIS
A mérőkapu egy kérdést tesz fel: nagyobb az alma 7 cm-nél? Ez a **feltétel**: a válasza mindig ==IGAZ vagy HAMIS==. A „Hány cm az alma?” nem feltétel – arra egy szám a válasz. Állítsd a küszöböt!

### Feliratok
- feltétel kérdés felirat: Nagyobb az alma, mint # cm?
- küszöb csúszka: Küszöb
- napló felirat: MÉRÉSI NAPLÓ
- alma oszlop: alma
- méret oszlop: méret
- válasz oszlop: válasz
- sorszám felirat: #.
- melyik felirat: MELYIK FELTÉTEL?
- mondat 1 felirat: Nagyobb az alma 7 cm-nél?
- mondat 2 felirat: Hány cm az alma?
- mondat 3 felirat: Piros az alma?
- mondat 4 felirat: Tedd a ládába!
- feltétel címke: feltétel: IGAZ vagy HAMIS
- szám címke: nem feltétel: a válasz szám
- utasítás címke: nem feltétel: utasítás

## 3. Ha … akkor … különben
Az **elágazás** a feltételtől függően választ: ha IGAZ, az „akkor” ág fut, ha HAMIS, a „különben” ág. ==Egy almánál mindig csak az egyik ág fut.== Vedd ki a „különben” ágat – hová kerülnek a kis almák?

> megjegyzés: A számokra és a ládabetűkre kattintva a program átírható.

### Feliratok
- folyamatábra felirat: UGYANEZ FOLYAMATÁBRÁN
- különben gomb: „Különben” ág: ki / be
- akkor ág felirat: az „akkor” ág: #
- különben ág felirat: a „különben” ág: #
- mindkettő felirat: mindkét ág egyszerre: #

## 4. Elágazás az elágazásban
A „különben” ágba újabb elágazás tehető, így a gép három láda közül választ. Ez a **többirányú elágazás**. Rajzolva egy **döntési fa**: az alma kérdésről kérdésre halad lefelé. ==Állíts be saját almát, és kövesd az útját!==

### Feliratok
- saját alma felirat: SAJÁT ALMA
- út felirat: # → # láda

### Adatok
- saját alma mérete: 6,5 cm
<!-- forrás: kitalált példa (a csúszka kezdőértéke) -->

## 5. Tippelj: hová kerül?
Jön egy nagy, {nagy piros alma mérete}-es piros alma. Mindkét kérdésre IGAZ a válasz. ==Hová kerül? Tippelj!==

**Az A ládába.** A gép fentről lefelé kérdez, és az **első** IGAZ válasznál dönt. A második kérdést fel sem teszi. Cseréld fel a két kérdést – most hová kerül?

### Feliratok
- nagy kérdés felirat: Hová kerül a nagy piros alma?
- a tipp: az A ládába
- b tipp: a B ládába
- mindkettő tipp: mindkét ládába
- csere gomb: Cseréld fel a két kérdést!
- nem kérdezett felirat: ezt fel sem tette
- sorrend felirat: a sorrend számít: # helyett #

### Adatok
- nagy piros alma mérete: 8,2 cm
<!-- forrás: kitalált példa -->

## 6. Határeset: pontosan 7 cm
Most egy pontosan {határeset alma mérete}-es sárga alma jön. ==Hová kerül? Tippelj!==

**Nem az A-ba.** A „7 > 7” HAMIS: semmi sem nagyobb önmagánál. Ha a 7 cm-es is nagynak számít, a **≥** jel kell: nagyobb vagy egyenlő. A **határesetet** mindig próbáld ki külön!

### Feliratok
- határ kérdés felirat: Hová kerül a pontosan 7 cm-es alma?
- határ a tipp: az A ládába
- határ bc tipp: a B-be vagy a C-be
- elakad tipp: a gép elakad
- reláció gomb: Jel: > vagy ≥
- számegyenes felirat: AZ A LÁDÁBA KERÜL:
- nagyobb jel felirat: nagyobb
- nagyobb egyenlő felirat: nagyobb vagy egyenlő

### Adatok
- határeset alma mérete: 7 cm
<!-- forrás: kitalált példa (pontosan a küszöbön) -->

## 7. „És” vagy „vagy”?
Két feltétel összeköthető. Az **és** csak akkor IGAZ, ha mindkét feltétel IGAZ. A **vagy** akkor IGAZ, ha legalább az egyik. ==Kapcsolj át, és figyeld: hány alma kerül az A ládába?==

### Feliratok
- és vagy gomb: Összekötés: és / vagy
- táblázat felirat: A KÉT FELTÉTEL ÉS AZ EREDMÉNY
- eredmény oszlop: eredmény

## 8. Teszteljük szélsőséges almákkal!
Próbáljuk ki furcsa bemenettel is: 1 cm, 20 cm, kétszínű alma! A program mindegyikre választ ad – de azt, amit szeretnénk? ==A 20 cm-es „alma” is az A ládába kerül.== Készíts saját tesztalmát!

<!-- A „Mit vártál az 1 cm-es piros almánál?” kérdést a tanár szóban teheti fel; a vásznon: „a program csak méretet és színt mér”. -->

### Feliratok
- tesztalmák színei: piros; piros; zöld; zöld-piros
- teszt felirat: TESZTNAPLÓ
- láda oszlop: láda
- saját sor felirat: saját
- saját méret csúszka: Saját tesztalma mérete
- saját szín gomb: Tesztalma: másik szín
- csak mér felirat: a program csak méretet és színt mér

### Adatok
- tesztalmák méretei: 1; 20; 7; 6,5 cm
<!-- forrás: kitalált példa – szándékosan szélsőséges értékek (1 cm: cseresznyényi; 20 cm: dinnyényi; 7 cm: pontosan a küszöb; 6,5 cm kétszínű) -->
- saját tesztalma mérete: 12 cm
<!-- forrás: kitalált példa (a csúszka kezdőértéke) -->

## 9. Összefoglalás
A **feltétel** kérdés, a válasza IGAZ vagy HAMIS. Az **elágazás** ettől függően választ ágat – mindig csak egyet. Több elágazás egymásba tehető: a gép az első IGAZ válasznál dönt. A **határesetet** és a szélsőséges bemenetet mindig teszteld!

### Feliratok
- feltétel kártya: feltétel: kérdés, a válasz IGAZ vagy HAMIS
- elágazás kártya: ha … akkor … különben: mindig csak egy ág fut
- többirányú kártya: elágazás az elágazásban: az első IGAZ dönt
- határ kártya: határeset: > vagy ≥? – próbáld ki!
- és vagy kártya: és: mindkettő IGAZ · vagy: legalább az egyik
- teszt kártya: tesztelj szélsőséges bemenettel is!

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a válogatógép, az almák (méret, szín), a 7 cm-es küszöb, a ládák szabálya (A: nagy;
    B: piros; C: többi) és minden program a lecke saját példája.
  - Modell-egyszerűsítések: a mérőkapu pontosan méri az átmérőt és egyetlen színt ad (a kétszínű alma
    színe „zöld-piros”, és ez nem azonos a „piros”-sal). A valódi almaválogató gépek kamerával, optikai
    szenzorral vagy mérleggel mérnek, és sok osztályba válogatnak; a sebesség, a szalag és a terelőlapok
    itt jelzésszerűek („modell” bélyeg). A gép nem „lát” és nem „tudja”, melyik alma jó: a program
    szerint dönt.
  - A blokknyelv a lecke saját nyelve (papír blokk, bal oldali kategóriasáv, „elágazás vége” záró sáv).
    Az órán használt blokkprogramozó környezetben a blokkok színe, alakja és felirata eltér (pl. „ha …
    akkor … különben” egyetlen blokk két nyílással); a szerkezet ugyanaz. A többirányú elágazás itt
    egymásba ágyazott „ha … különben” – sok környezetben is így készül.
  - A „≥” jel: nagyobb vagy egyenlő (a matematikaórán is előkerül). Az „és”, „vagy” halmazos oldala a
    matematika 5–6. (01-halmazok) leckében van; az igazságtábla 9–10. évfolyamon jön.
  - A folyamatábra és a döntési fa ugyanannak a programnak két rajza: a döntési fán az IGAZ ág balra,
    a HAMIS jobbra indul, a folyamatábrán az IGAZ lefelé, a HAMIS jobbra.
  - A panelszövegben a „7 cm”, „1 cm”, „20 cm” kézzel írt szám (a vászon az Adatokból számol): ha a
    küszöböt vagy a tesztalmákat átírod, ezeket is írd át.
-->
