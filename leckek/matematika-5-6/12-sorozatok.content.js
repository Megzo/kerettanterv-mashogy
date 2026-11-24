/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 12-sorozatok.md
   Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/12-sorozatok.md */
window.LESSON_CONTENT = {
 "source": "12-sorozatok.md",
 "title": "Hány gyufa kell a 100. házhoz? – sorozatok és szabályok",
 "titleLine": 1,
 "meta": {
  "subject": "Matematika",
  "grade": "5–6.",
  "topic": "12. Sorozatok (+ 11. A függvény fogalmának előkészítése)"
 },
 "steps": [
  {
   "title": "Mi jön ezután?",
   "html": "<p data-src=\"35\">Gyufából házsort rakunk. Egy ház <b>6</b> szál, két ház <b>11</b>, három ház <b>16</b>. Hány szál kell négy házhoz? <span class=\"key\">Tippelj előbb!</span> Aztán nézd, ahogy felépül, és számold a szálakat!</p><p class=\"note\" data-src=\"37\">Kérdezd meg: ki hogyan számolt?</p>",
   "line": 34,
   "words": 33
  },
  {
   "title": "Mennyivel nő? – egyforma lépcsők",
   "html": "<p data-src=\"48\">Írjuk táblázatba! Minden új ház <b>5</b> szállal több: alul és fölül egy-egy szál, egy fal és két tetőszál. A bal szélső fal csak egyszer kell. Oszlopba rakva <span class=\"key\">egyforma lépcsők</span> jönnek. Ha egy sorozat mindig ugyanannyival nő, a neve <b>számtani sorozat</b>.</p>",
   "line": 47,
   "words": 40
  },
  {
   "title": "A 100. ház – szabály és csapda",
   "html": "<p data-src=\"58\">Nem kell megépíteni! A bal szélső fal 1 szál, utána minden ház 5. Tehát <em>n</em> házhoz <span class=\"mx\">5 · <i>n</i> + 1</span> szál kell, 100 házhoz 501. <span class=\"key\">Csapda:</span> 25 ház 126 szál, de 100 ház nem <span class=\"mx\">4 · 126 = 504</span>! Miért? Nyomd meg a gombot!</p>",
   "line": 57,
   "words": 37
  },
  {
   "title": "Pontok egy egyenesen – mégsem arányos",
   "html": "<p data-src=\"72\">Tegyük a számpárokat a koordináta-rendszerbe! A pontok <span class=\"key\">egy egyenesre esnek</span>, és lépcsőt rajzolnak: jobbra 1, fel 5. Mégsem egyenes arányosság! Az egyenes nem az origón megy át: 0 háznál 1-et mutat. Ez a bal szélső fal.</p><p class=\"note\" data-src=\"74\">Nyomd meg: hol lenne az arányos?</p>",
   "line": 71,
   "words": 42
  },
  {
   "title": "Egy kezdet, két szabály",
   "html": "<p data-src=\"86\">1; 2; 4 – mi jön ezután? <span class=\"key\">Tippelj előbb!</span> Aztán nézd meg, hogyan folytatja a gép két különböző szabállyal. <b>Melyik a jó?</b> Néhány tagból nem mindig dől el, hogyan megy tovább egy sorozat. Ezért a feladatnak a <b>szabályt</b> is meg kell adnia.</p>",
   "line": 85,
   "words": 39
  },
  {
   "title": "Háromszögszámok",
   "html": "<p data-src=\"105\">Pöttyökből háromszögeket rakunk: 1; 3; 6; 10; 15 pötty. Minden új sor eggyel hosszabb az előzőnél, ezért a növekmény 2, 3, 4, 5. <span class=\"key\">A lépcsők egyre magasabbak</span>, ez nem számtani sorozat. Ezek a <b>háromszögszámok</b>.</p><p class=\"note\" data-src=\"107\">Húzd a csúszkát! Mennyi a 10. háromszögszám?</p>",
   "line": 104,
   "words": 41
  },
  {
   "title": "Négyzetszámok",
   "html": "<p data-src=\"121\">Négyzetbe is rakhatunk pöttyöket: 1; 4; 9; 16; 25. Minden új szegély egy <b>L</b> alak: 3, 5, 7, 9 pötty – a páratlan számok! <span class=\"key\">Az első <em>n</em> páratlan szám összege <span class=\"mx\"><i>n</i> · <i>n</i></span>.</span> Vágd ketté a négyzetet: két szomszédos háromszögszám lesz belőle!</p>",
   "line": 120,
   "words": 39
  },
  {
   "title": "Gauss trükkje: 1 + 2 + … + 100",
   "html": "<p data-src=\"135\">A hagyomány szerint a kisiskolás Gauss pillanatok alatt összeadta a számokat 1-től 100-ig. A trükk: a lépcső mellé tegyünk egy fordított lépcsőt! Együtt téglalapot adnak: <span class=\"mx\">100 · 101</span>. <span class=\"key\">A lépcső ennek a fele: 5050.</span> Ez a 100. háromszögszám.</p><p class=\"note\" data-src=\"137\">Párokban: <span class=\"mx\">1 + 100 = 2 + 99 = … = 101</span>.</p>",
   "line": 134,
   "words": 38
  },
  {
   "title": "Összefoglalás",
   "html": "<ul><li data-src=\"157\">A <b>sorozat</b> tagjai egy <b>szabály</b> szerint követik egymást.</li><li data-src=\"158\">Ha mindig ugyanannyival nő: egyforma lépcsők, a pontok egy egyenesen.</li><li data-src=\"159\">A tagot a sorszámból is kiszámolhatod: <span class=\"mx\">5 · <i>n</i> + 1</span>.</li><li data-src=\"160\"><span class=\"key\">Néhány tagból többféle szabály is kijöhet.</span></li><li data-src=\"161\">Háromszög- és négyzetszámok: egyre nagyobb lépcsők.</li></ul>",
   "line": 156,
   "words": 37
  }
 ],
 "labels": {
  "tippelj": "Tippelj előbb!",
  "a tipped": "a te tipped: #",
  "házak": "házak",
  "szálak": "szálak",
  "ház sor": "# ház",
  "szál": "# szál",
  "kérdés 1": "Hány szál kell # házhoz?",
  "tipp gomb": "# szál",
  "magyarázat jó": "Ügyes! Minden új ház +5 szál.",
  "magyarázat kevés": "Kimaradt a bal szélső fal.",
  "magyarázat sok": "A közös falakat kétszer számoltad!",
  "végeredmény": "# ház: # szál",
  "plusz öt": "+5",
  "jelmagyarázat fal": "bal szélső fal: 1 szál",
  "jelmagyarázat ház": "minden új ház: 5 szál",
  "lépcső felirat": "mindig +5: egyforma lépcsők",
  "csúszka 2": "házak száma",
  "szabály": "`n` ház → `5 · n + 1` szál",
  "megszámolva": "megszámolva: # szál",
  "csúszka 3": "házak száma",
  "gomb csapda": "×4 csapda",
  "gomb sor": "Vissza a házsorhoz",
  "negyed sor": "# ház: # szál",
  "dupla fal": "dupla fal",
  "csapda kérdés": "Négy 25-ös sor: 4 · 126 = 504?",
  "csapda válasz": "Összetolva 3 fal kétszer szerepel!",
  "lépcső jobbra": "1 ház",
  "lépcső fel": "+5 szál",
  "első fal": "0 ház → 1 szál: a bal szélső fal",
  "arányos": "`5 · n`: ez lenne arányos",
  "egyenes 4": "`5 · n + 1`",
  "gomb arányos": "Arányos lenne?",
  "csúszka 4": "házak száma",
  "kérdés 5": "Mi jön ezután?",
  "tipp más": "Más szám is lehet",
  "szabály duplázás": "mindig duplázunk",
  "szabály növekmény": "egyre többel nő",
  "két szabály": "Mindkét szabály illik a kezdethez!",
  "a tipped jó": "A tipped jó – de nem az egyetlen!",
  "háromszög cím": "háromszögszámok",
  "növekmény": "növekmény:",
  "csúszka 6": "sorok száma",
  "sor hossza": "#",
  "n-edik háromszögszám": "a #. háromszögszám",
  "négyzet cím": "négyzetszámok",
  "csúszka 7": "oldal hossza",
  "gomb ketté": "Vágd ketté!",
  "gomb egész": "Rakd össze!",
  "gauss kérdés": "1 + 2 + … + # = ?",
  "gauss oszlop": "minden oszlop: # magas",
  "gauss téglalap": "téglalap: # · # = #",
  "gauss fele": "a lépcső a fele: # : 2 = #",
  "csúszka 8": "meddig adjuk össze?",
  "gomb forgasd": "Forgasd rá!",
  "gauss legenda": "hagyomány",
  "össz 1": "szabály: `5 · n + 1`",
  "össz 2": "két szabály, két folytatás",
  "össz 3": "pöttyminták",
  "össz 4": "Gauss: lépcső + lépcső = téglalap"
 },
 "data": {
  "gyufaszálak": {
   "t": "series",
   "x": [
    1.0,
    2.0,
    3.0,
    4.0,
    25.0,
    100.0
   ],
   "y": [
    6.0,
    11.0,
    16.0,
    21.0,
    126.0,
    501.0
   ],
   "ux": "",
   "uy": "",
   "dx": 0,
   "dy": 0,
   "s": "1: 6 · 2: 11 · 3: 16 · 4: 21 · 25: 126 · 100: 501"
  },
  "négyszeres tipp": {
   "v": 504.0,
   "u": "",
   "d": 0
  },
  "kezdet": {
   "t": "list",
   "v": [
    1.0,
    2.0,
    4.0
   ],
   "u": "",
   "d": 0,
   "s": "1; 2; 4"
  },
  "duplázva": {
   "t": "list",
   "v": [
    8.0,
    16.0,
    32.0
   ],
   "u": "",
   "d": 0,
   "s": "8; 16; 32"
  },
  "egyre többel": {
   "t": "list",
   "v": [
    7.0,
    11.0,
    16.0
   ],
   "u": "",
   "d": 0,
   "s": "7; 11; 16"
  },
  "háromszögszámok": {
   "t": "series",
   "x": [
    1.0,
    2.0,
    3.0,
    4.0,
    5.0
   ],
   "y": [
    1.0,
    3.0,
    6.0,
    10.0,
    15.0
   ],
   "ux": "",
   "uy": "",
   "dx": 0,
   "dy": 0,
   "s": "1: 1 · 2: 3 · 3: 6 · 4: 10 · 5: 15"
  },
  "négyzetszámok": {
   "t": "series",
   "x": [
    1.0,
    2.0,
    3.0,
    4.0,
    5.0
   ],
   "y": [
    1.0,
    4.0,
    9.0,
    16.0,
    25.0
   ],
   "ux": "",
   "uy": "",
   "dx": 0,
   "dy": 0,
   "s": "1: 1 · 2: 4 · 3: 9 · 4: 16 · 5: 25"
  },
  "Gauss-összegek": {
   "t": "series",
   "x": [
    10.0,
    100.0
   ],
   "y": [
    55.0,
    5050.0
   ],
   "ux": "",
   "uy": "",
   "dx": 0,
   "dy": 0,
   "s": "10: 55 · 100: 5050"
  }
 },
 "src": {
  "gyufaszálak": 26,
  "négyszeres tipp": 31,
  "kezdet": 97,
  "duplázva": 98,
  "egyre többel": 99,
  "háromszögszámok": 117,
  "négyzetszámok": 130,
  "Gauss-összegek": 149,
  "tippelj": 18,
  "a tipped": 19,
  "házak": 20,
  "szálak": 21,
  "ház sor": 22,
  "szál": 23,
  "kérdés 1": 40,
  "tipp gomb": 41,
  "magyarázat jó": 42,
  "magyarázat kevés": 43,
  "magyarázat sok": 44,
  "végeredmény": 45,
  "plusz öt": 51,
  "jelmagyarázat fal": 52,
  "jelmagyarázat ház": 53,
  "lépcső felirat": 54,
  "csúszka 2": 55,
  "szabály": 61,
  "megszámolva": 62,
  "csúszka 3": 63,
  "gomb csapda": 64,
  "gomb sor": 65,
  "negyed sor": 66,
  "dupla fal": 67,
  "csapda kérdés": 68,
  "csapda válasz": 69,
  "lépcső jobbra": 77,
  "lépcső fel": 78,
  "első fal": 79,
  "arányos": 80,
  "egyenes 4": 81,
  "gomb arányos": 82,
  "csúszka 4": 83,
  "kérdés 5": 89,
  "tipp más": 90,
  "szabály duplázás": 91,
  "szabály növekmény": 92,
  "két szabály": 93,
  "a tipped jó": 94,
  "háromszög cím": 110,
  "növekmény": 111,
  "csúszka 6": 112,
  "sor hossza": 113,
  "n-edik háromszögszám": 114,
  "négyzet cím": 124,
  "csúszka 7": 125,
  "gomb ketté": 126,
  "gomb egész": 127,
  "gauss kérdés": 140,
  "gauss oszlop": 141,
  "gauss téglalap": 142,
  "gauss fele": 143,
  "csúszka 8": 144,
  "gomb forgasd": 145,
  "gauss legenda": 146,
  "össz 1": 164,
  "össz 2": 165,
  "össz 3": 166,
  "össz 4": 167
 }
};
