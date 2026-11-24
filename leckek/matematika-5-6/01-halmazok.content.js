/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 01-halmazok.md
   Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/01-halmazok.md */
window.LESSON_CONTENT = {
 "source": "01-halmazok.md",
 "title": "Hová kerül a 15? – halmazok, „és”, „vagy”",
 "titleLine": 1,
 "meta": {
  "subject": "Matematika",
  "grade": "5–6.",
  "topic": "1. Halmazok"
 },
 "steps": [
  {
   "title": "Válogassunk!",
   "html": "<p data-src=\"49\">Itt van húsz számkártya, 1-től 20-ig: ez az <b>alaphalmaz</b>. A páros számokat egy körbe tesszük. Ők alkotják a páros számok <b>halmazát</b>. A 4 <b>eleme</b> a halmaznak, a 7 nem eleme. <span class=\"key\">Minden számról eldönthető: benne van, vagy nincs.</span></p><p class=\"note\" data-src=\"51\">Válassz más tulajdonságot is a gombokkal!</p>",
   "line": 48,
   "words": 43
  },
  {
   "title": "Két szempont egyszerre",
   "html": "<p data-src=\"57\">Most két kör van: <b>A</b> a páros számok, <b>B</b> a 3-mal osztható számok halmaza. A két kör egymásba lóg. <span class=\"key\">Tippelj előbb!</span> Hová kerül a 15? Gondold végig: páros? Osztható 3-mal?</p><p class=\"note\" data-src=\"59\">Kattints egy kártyára: megmutatja, melyik feltétel igaz rá.</p>",
   "line": 56,
   "words": 38
  },
  {
   "title": "„És”: a közös rész",
   "html": "<p data-src=\"74\">A két kör <b>közös részébe</b> azok a számok kerülnek, amelyek párosak <b>és</b> 3-mal oszthatók. <span class=\"key\">Az „és” azt jelenti: mindkét feltétel igaz.</span> Ezek: {6; 12; 18}. A 15 csak az egyik feltételnek felel meg, ezért nincs itt.</p>",
   "line": 73,
   "words": 34
  },
  {
   "title": "„Vagy”: az egyesítés",
   "html": "<p data-src=\"80\">Az <b>egyesítésbe</b> azok kerülnek, amelyek párosak <b>vagy</b> 3-mal oszthatók. Tévhit: a „vagy” kizárja, hogy mindkettő igaz legyen. <span class=\"key\">A matekban a „vagy” megengedő: mindkettő is jó!</span> Így a 6, a 12 és a 18 is benne van.</p><p class=\"note\" data-src=\"82\">Hasonlítsd össze: „vagy…, vagy…”!</p>",
   "line": 79,
   "words": 40
  },
  {
   "title": "Hányan vannak?",
   "html": "<p data-src=\"92\"><span class=\"key\">Tippelj előbb!</span> Hány szám van az egyesítésben? Csábító összeadni: 10 + 6. De így a közös rész számait <b>kétszer</b> számolnánk! Az egyesítés elemszáma: a két elemszám összege, <b>mínusz</b> a közös rész elemszáma.</p>",
   "line": 91,
   "words": 31
  },
  {
   "title": "„Nem”: a kiegészítő halmaz",
   "html": "<p data-src=\"101\">Melyik szám <b>nem</b> páros? Az alaphalmaz többi eleme: ez az A <b>kiegészítő halmaza</b>. Tévhit: ami egyik körben sincs, az „nem tartozik sehova”. <span class=\"key\">Pedig ezek is az alaphalmaz elemei!</span></p><p class=\"note\" data-src=\"103\">Nézd meg a „se nem…, se nem…” gombot is!</p>",
   "line": 100,
   "words": 37
  },
  {
   "title": "Részhalmaz",
   "html": "<p data-src=\"113\">A 4-gyel osztható számok mind párosak. Így a B minden eleme benne van A-ban: B <b>részhalmaza</b> A-nak. A kör belecsúszik a másikba. <span class=\"key\">Egyetlen ellenpélda elég, és már nem részhalmaz.</span> Minden halmaz önmagának is részhalmaza.</p><p class=\"note\" data-src=\"115\">Próbáld ki a gombokat!</p>",
   "line": 112,
   "words": 38
  },
  {
   "title": "Halmaz a számegyenesen",
   "html": "<p data-src=\"126\">„<b>Legalább</b> 3”: ez is jó, és minden nagyobb. „<b>Legfeljebb</b> 8”: ez is jó, és minden kisebb. <span class=\"key\">Az „és” itt is a közös rész.</span> A teli karika: a szám benne van. Az üres karika: már nincs benne.</p><p class=\"note\" data-src=\"128\">A vastag vonal a köztes törteket is jelöli.</p>",
   "line": 125,
   "words": 44
  },
  {
   "title": "Összefoglalás",
   "html": "<ul><li data-src=\"152\"><b>Közös rész</b> („és”): mindkettő igaz.</li><li data-src=\"153\"><b>Egyesítés</b> („vagy”): legalább az egyik igaz.</li><li data-src=\"154\"><b>Kiegészítő halmaz</b> („nem”): a többi elem.</li><li data-src=\"155\"><b>Részhalmaz:</b> minden eleme a másikban is benne van.</li><li data-src=\"156\"><span class=\"key\">Válassz két tulajdonságot!</span></li></ul>",
   "line": 151,
   "words": 28
  }
 ],
 "labels": {
  "alaphalmaz felirat": "alaphalmaz: az egész számok 1-től 20-ig",
  "páros": "páros",
  "páratlan": "páratlan",
  "3-mal osztható": "3-mal osztható",
  "10-nél nagyobb": "10-nél nagyobb",
  "prím": "prím",
  "5-re végződik": "5-re végződik",
  "4-gyel osztható": "4-gyel osztható",
  "igen": "igen",
  "nem": "nem",
  "tippelj": "Tippelj előbb!",
  "a tipped": "a te tipped",
  "és sablon": "# és #",
  "vagy sablon": "# vagy #",
  "nem sablon": "nem #",
  "pontosan sablon": "vagy #, vagy #",
  "egyik sem sablon": "se nem #, se nem #",
  "elemszám": "# elem",
  "üres halmaz": "üres halmaz",
  "válogatás cím": "Melyik szám kerül a körbe?",
  "hová cím": "Hová kerül a #?",
  "tipp csak A": "csak az A-ba",
  "tipp közös": "a közös részbe",
  "tipp csak B": "csak a B-be",
  "tipp egyik sem": "egyik körbe sem",
  "és cím": "Melyik szám páros és 3-mal osztható is?",
  "vagy cím": "Melyik szám páros vagy 3-mal osztható?",
  "vagy gomb": "vagy",
  "vagyvagy gomb": "vagy…, vagy…",
  "mindkettő jó": "mindkettő is jó!",
  "kimarad": "kimarad: mindkettő igaz",
  "hány cím": "Hány szám van az egyesítésben?",
  "tipp szám": "# szám",
  "kétszer": "kétszer számoltuk!",
  "egyesítésben": "az egyesítésben # szám van",
  "nem cím": "Ami kimaradt, az is a téglalapban van!",
  "nem A gomb": "nem A",
  "nem B gomb": "nem B",
  "egyik sem gomb": "se nem A, se nem B",
  "alaphalmaz elemei": "ezek is az alaphalmaz elemei!",
  "rész cím": "Benne van-e B minden eleme A-ban?",
  "üres rész": "ez a rész üres!",
  "részhalmaz igen": "B részhalmaza A-nak",
  "részhalmaz nem": "B nem részhalmaza A-nak",
  "ellenpélda": "ellenpélda: #",
  "önmaga": "B = A: önmagának is részhalmaza",
  "legalább sablon": "legalább #",
  "legfeljebb sablon": "legfeljebb #",
  "kisebb sablon": "kisebb, mint #",
  "és szó": "és",
  "vagy szó": "vagy",
  "legalább csúszka": "legalább …",
  "legfeljebb csúszka": "legfeljebb / kisebb, mint …",
  "kisebb gomb": "legfeljebb ↔ kisebb, mint",
  "és vagy gomb": "és ↔ vagy",
  "egész számok": "# egész szám",
  "minden szám": "minden szám benne van!",
  "A csúszka": "A halmaz",
  "B csúszka": "B halmaz",
  "és gomb": "és",
  "vagy gomb 9": "vagy",
  "nem A gomb 9": "nem A",
  "pontosan gomb": "pontosan az egyik",
  "játék cím": "Válassz két tulajdonságot!",
  "A része B": "A részhalmaza B-nek",
  "nincs közös": "nincs közös elemük"
 },
 "data": {
  "alaphalmaz": {
   "t": "range",
   "lo": 1.0,
   "hi": 20.0,
   "v": 10.5,
   "u": "",
   "d": 0,
   "s": "1–20"
  },
  "páros számok száma": {
   "v": 10.0,
   "u": "",
   "d": 0
  },
  "3-mal oszthatók száma": {
   "v": 6.0,
   "u": "",
   "d": 0
  },
  "közös rész elemei": {
   "t": "list",
   "v": [
    6.0,
    12.0,
    18.0
   ],
   "u": "",
   "d": 0,
   "s": "6; 12; 18"
  },
  "egyesítés elemszáma": {
   "v": 13.0,
   "u": "",
   "d": 0
  },
  "egyik sem elemei": {
   "t": "list",
   "v": [
    1.0,
    5.0,
    7.0,
    11.0,
    13.0,
    17.0,
    19.0
   ],
   "u": "",
   "d": 0,
   "s": "1; 5; 7; 11; 13; 17; 19"
  },
  "vizsgált szám": {
   "v": 15.0,
   "u": "",
   "d": 0
  },
  "legalább érték": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "legfeljebb érték": {
   "v": 8.0,
   "u": "",
   "d": 0
  },
  "egész számok száma": {
   "v": 6.0,
   "u": "",
   "d": 0
  }
 },
 "src": {
  "alaphalmaz": 38,
  "páros számok száma": 39,
  "3-mal oszthatók száma": 40,
  "közös rész elemei": 41,
  "egyesítés elemszáma": 42,
  "egyik sem elemei": 43,
  "vizsgált szám": 69,
  "legalább érték": 144,
  "legfeljebb érték": 145,
  "egész számok száma": 146,
  "alaphalmaz felirat": 17,
  "páros": 18,
  "páratlan": 19,
  "3-mal osztható": 20,
  "10-nél nagyobb": 21,
  "prím": 22,
  "5-re végződik": 23,
  "4-gyel osztható": 24,
  "igen": 25,
  "nem": 26,
  "tippelj": 27,
  "a tipped": 28,
  "és sablon": 29,
  "vagy sablon": 30,
  "nem sablon": 31,
  "pontosan sablon": 32,
  "egyik sem sablon": 33,
  "elemszám": 34,
  "üres halmaz": 35,
  "válogatás cím": 54,
  "hová cím": 62,
  "tipp csak A": 63,
  "tipp közös": 64,
  "tipp csak B": 65,
  "tipp egyik sem": 66,
  "és cím": 77,
  "vagy cím": 85,
  "vagy gomb": 86,
  "vagyvagy gomb": 87,
  "mindkettő jó": 88,
  "kimarad": 89,
  "hány cím": 95,
  "tipp szám": 96,
  "kétszer": 97,
  "egyesítésben": 98,
  "nem cím": 106,
  "nem A gomb": 107,
  "nem B gomb": 108,
  "egyik sem gomb": 109,
  "alaphalmaz elemei": 110,
  "rész cím": 118,
  "üres rész": 119,
  "részhalmaz igen": 120,
  "részhalmaz nem": 121,
  "ellenpélda": 122,
  "önmaga": 123,
  "legalább sablon": 131,
  "legfeljebb sablon": 132,
  "kisebb sablon": 133,
  "és szó": 134,
  "vagy szó": 135,
  "legalább csúszka": 136,
  "legfeljebb csúszka": 137,
  "kisebb gomb": 138,
  "és vagy gomb": 139,
  "egész számok": 140,
  "minden szám": 141,
  "A csúszka": 159,
  "B csúszka": 160,
  "és gomb": 161,
  "vagy gomb 9": 162,
  "nem A gomb 9": 163,
  "pontosan gomb": 164,
  "játék cím": 165,
  "A része B": 166,
  "nincs közös": 167
 }
};
