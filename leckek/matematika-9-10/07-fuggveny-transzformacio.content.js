/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 07-fuggveny-transzformacio.md
   Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/07-fuggveny-transzformacio.md */
window.LESSON_CONTENT = {
 "source": "07-fuggveny-transzformacio.md",
 "title": "Merre mozdul a parabola? – függvények és transzformációik",
 "titleLine": 1,
 "meta": {
  "subject": "Matematika",
  "grade": "9–10.",
  "topic": "10. A függvény fogalma, függvénytulajdonságok (+ 7. Arányosság)"
 },
 "steps": [
  {
   "title": "A függvénygép",
   "html": "<p data-src=\"31\">A függvény egy gép: beteszel egy <em>x</em>-et, kijön egy szám, az <span class=\"mx\"><i>f</i>(<i>x</i>)</span>. Az <span class=\"mx\">(<i>x</i>; <i>f</i>(<i>x</i>))</span> párok pontként esnek a koordináta-rendszerbe, és sok pontból összeáll a <b>grafikon</b>. <span class=\"key\">Minden x-hez pontosan egy y tartozik.</span> A kör ezért nem függvénygrafikon: egy <em>x</em>-hez két <em>y</em>-t ad.</p><p class=\"note\" data-src=\"33\">Húzd a csúszkát: hány pontban metszi a függőleges egyenes a görbét?</p>",
   "line": 30,
   "words": 52
  },
  {
   "title": "Mit árul el a grafikon?",
   "html": "<p data-src=\"49\"><b>Értelmezési tartomány</b> (<span class=\"mx\"><i>D</i><sub><i>f</i></sub></span>): mely <em>x</em>-ekre van értelmezve. <b>Értékkészlet</b> (<span class=\"mx\"><i>R</i><sub><i>f</i></sub></span>): mely <em>y</em>-okat veszi fel – <span class=\"key\">nem az egész y tengely!</span> <b>Zérushely</b>: ahol <span class=\"mx\"><i>f</i>(<i>x</i>) = 0</span>, itt −1 és 3. <b>Minimum</b>: a legkisebb érték, −4. Hol csökken, hol nő?</p><p class=\"note\" data-src=\"51\">Húzd a pontot a görbén!</p>",
   "line": 48,
   "words": 39
  },
  {
   "title": "Az alapfüggvények",
   "html": "<p data-src=\"76\">Ezekből az <b>elemi függvényekből</b> építkezünk. Nézd meg, hol vannak értelmezve! A <span class=\"mx\"><span class=\"rt\">√<span class=\"rad\"><i>x</i></span></span></span> csak <span class=\"mx\"><i>x</i> ≥ 0</span>-ra, az <span class=\"mx\">1/<i>x</i></span> az <span class=\"mx\"><i>x</i> = 0</span>-ban nincs értelmezve: a két ága <span class=\"key\">sosem ér össze</span>. Az <span class=\"mx\"><i>y</i> = 12/<i>x</i></span> <b>fordított arányosság</b>: a téglalapok területe mind <span class=\"mx\"><i>x</i> · <i>y</i> = 12</span>.</p>",
   "line": 75,
   "words": 35
  },
  {
   "title": "<span class=\"mx\"><i>f</i>(<i>x</i>) + <i>v</i></span>: fel és le",
   "html": "<p data-src=\"95\">Adj minden függvényértékhez 3-at: <span class=\"mx\"><i>g</i>(<i>x</i>) = <i>f</i>(<i>x</i>) + 3</span>. Minden pont pontosan 3 egységgel <b>feljebb</b> kerül, a görbe alakja nem változik. <span class=\"key\">Pozitív v fel, negatív v le tolja.</span> Húzd a csúcsot, vagy próbáld ki más alapfüggvénnyel!</p>",
   "line": 94,
   "words": 32
  },
  {
   "title": "<span class=\"mx\"><i>f</i>(<i>x</i> + <i>u</i>)</span>: miért balra?",
   "html": "<p data-src=\"105\">A „+ 3” miatt sokan jobbra tolnák. Ha <span class=\"mx\"><i>f</i>(<i>x</i><sub>0</sub>) = <i>y</i><sub>0</sub></span>, akkor <span class=\"mx\"><i>g</i>(<i>x</i><sub>0</sub> − 3) = <i>f</i>(<i>x</i><sub>0</sub> − 3 + 3) = <i>y</i><sub>0</sub></span>. <span class=\"key\">Az f minden pontja 3-mal balra kerül:</span> a g ugyanazt az értéket 3-mal kisebb <em>x</em>-nél veszi fel. ∎</p>",
   "line": 104,
   "words": 27
  },
  {
   "title": "<span class=\"mx\"><i>a</i> · <i>f</i>(<i>x</i>)</span>: nyújtás és tükrözés",
   "html": "<p data-src=\"116\">A <span class=\"mx\">2 · <i>f</i>(<i>x</i>)</span> minden <em>y</em>-értéket a kétszeresére növel, az <em>x</em> marad. A parabola ezért <b>keskenyebbnek</b> látszik – nem lett „kétszer szélesebb”, csak magasabb. Az <em>x</em> tengely pontjai helyben maradnak. <span class=\"key\">Negatív szorzó az x tengelyre tükröz.</span></p>",
   "line": 115,
   "words": 33
  },
  {
   "title": "<span class=\"mx\">|<i>f</i>(<i>x</i>)|</span>: felhajtás",
   "html": "<p data-src=\"127\">Az abszolútérték a negatív értékeket ellentettjükre váltja: a grafikon tengely alatti része <span class=\"key\">felhajlik, az x tengelyre tükrözve.</span> Az <span class=\"mx\">|<i>x</i><sup>2</sup> − 4|</span> zérushelyei maradnak <span class=\"mx\">±2</span>, és az <span class=\"mx\"><i>x</i> = 0</span>-ban <b>helyi maximuma</b> lett: 4. Vigyázz: az <span class=\"mx\"><i>f</i>(|<i>x</i>|)</span> egészen mást jelent!</p>",
   "line": 126,
   "words": 35
  },
  {
   "title": "<span class=\"mx\"><i>f</i>(<i>x</i>) = <i>c</i></span> és a megfordítás",
   "html": "<p data-src=\"140\">Melyik <em>x</em>-hez tartozik az 5? Az <span class=\"mx\"><i>x</i><sup>2</sup> = 5</span> egyenletnek két megoldása van: <span class=\"mx\"><i>x</i> = ±<span class=\"rt\">√<span class=\"rad\">5</span></span> ≈ ±</span>2,24. Két <em>x</em> ugyanahhoz az <em>y</em>-hoz: így az <span class=\"mx\"><i>x</i><sup>2</sup></span> <span class=\"key\">nem fordítható meg</span>. Az <span class=\"mx\"><i>x</i> ≥ 0</span> rész már <b>kölcsönösen egyértelmű</b>: tükrözzük az <span class=\"mx\"><i>y</i> = <i>x</i></span> egyenesre – ez a <span class=\"mx\"><span class=\"rt\">√<span class=\"rad\"><i>x</i></span></span></span>.</p>",
   "line": 139,
   "words": 36
  },
  {
   "title": "Találd el! – összefoglalás",
   "html": "<p data-src=\"161\">Válaszd ki az alapfüggvényt, és állítsd be a csúszkákat úgy, hogy a görbéd <span class=\"key\">fedje a célgörbét</span>! A szabályok a vásznon.</p>",
   "line": 160,
   "words": 20
  }
 ],
 "labels": {
  "alap x": "x",
  "alap x2": "x²",
  "alap gyök": "√x",
  "alap 1/x": "1/x",
  "alap abs": "|x|",
  "a csúszka": "a (nyújtás, tükrözés)",
  "u csúszka": "u (vízszintes eltolás)",
  "v csúszka": "v (függőleges eltolás)",
  "abs gomb": "|·| felhajtás",
  "eredeti": "eredeti",
  "új görbe": "új",
  "gép": "FÜGGVÉNYGÉP",
  "bemenet": "be: x",
  "kimenet": "ki: f(x)",
  "kör cím": "kör – nem függvény",
  "két y": "egy x-hez két y",
  "egy y": "egy x-hez egy y",
  "gép csúszka": "x (bemenet)",
  "ÉT felirat": "értelmezési tartomány",
  "ÉK felirat": "értékkészlet",
  "nem az egész": "nem az egész y tengely!",
  "zérushely felirat": "zérushely",
  "minimum felirat": "minimum",
  "csökken": "csökken",
  "nő": "nő",
  "pont csúszka": "x (a pont helye)",
  "lineáris": "lineáris",
  "másodfokú": "másodfokú",
  "abszolút": "abszolútérték",
  "négyzetgyök": "négyzetgyök",
  "reciprok": "fordított arányosság",
  "ÉT mind": "minden x",
  "ÉT gyök": "`x >= 0`",
  "ÉT reciprok": "`x != 0`",
  "téglalap cím": "mind ugyanakkora területű",
  "szélesség csúszka": "x (a téglalap szélessége)",
  "fel": "minden pont # egységgel feljebb",
  "le": "minden pont # egységgel lejjebb",
  "tipp": "tipp: jobbra?",
  "nem jobbra": "nem jobbra – balra!",
  "bizonyítás": "bizonyítás",
  "keskenyebb": "keskenyebb? Nem: magasabb!",
  "tükrözés felirat": "tükrözés az x tengelyre",
  "felhajtott rész": "a tengely alatti rész felhajlik",
  "helyi max": "helyi maximum",
  "f abs x gomb": "f(|x|) mutatása",
  "nem ugyanaz": "f(|x|) ≠ |f(x)|",
  "megoldás db": "# megoldás",
  "nincs megoldás": "nincs megoldás",
  "nem fordítható": "két x → nem fordítható meg",
  "fordítható": "egy x → megfordítható",
  "csak pozitív": "csak az x ≥ 0 rész",
  "tükör": "y = x",
  "megfordítva": "megfordítva:",
  "parabola példa": "x² (x ≥ 0) ↔ √x",
  "egyenes példa gomb": "2x + 1 ↔ (x − 1)/2",
  "újra tükröz": "Tükrözés újra",
  "c csúszka": "c (vízszintes egyenes)",
  "célgörbe": "célgörbe",
  "talált": "Talált!",
  "még nem": "még nem fedi",
  "új cél": "Új célgörbe",
  "szabályok": "A négy lépés",
  "össz v": "függőleges eltolás (v > 0: fel)",
  "össz u": "vízszintes eltolás (u > 0: balra!)",
  "össz a": "nyújtás, a < 0: tükrözés",
  "össz abs": "a negatív rész felhajlik"
 },
 "data": {
  "gép szabálya": {
   "t": "expr",
   "tok": [
    "x",
    "^",
    "2"
   ],
   "tree": [
    "^",
    "x",
    2
   ],
   "s": "x^2"
  },
  "gép bemenetei": {
   "t": "list",
   "v": [
    -3.0,
    -2.0,
    -1.0,
    0.0,
    1.0,
    2.0,
    3.0
   ],
   "u": "",
   "d": 0,
   "s": "−3; −2; −1; 0; 1; 2; 3"
  },
  "vizsgált függvény": {
   "t": "expr",
   "tok": [
    "x",
    "^",
    "2",
    "−",
    "2",
    "x",
    "−",
    "3"
   ],
   "tree": [
    "−",
    [
     "−",
     [
      "^",
      "x",
      2
     ],
     [
      "imp",
      2,
      "x"
     ]
    ],
    3
   ],
   "s": "x^2 − 2x − 3"
  },
  "ÉT eleje": {
   "v": -2.0,
   "u": "",
   "d": 0
  },
  "ÉT vége": {
   "v": 4.0,
   "u": "",
   "d": 0
  },
  "zérushely 1": {
   "v": -1.0,
   "u": "",
   "d": 0
  },
  "zérushely 2": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "minimum helye": {
   "v": 1.0,
   "u": "",
   "d": 0
  },
  "minimum értéke": {
   "v": -4.0,
   "u": "",
   "d": 0
  },
  "ÉK felső határa": {
   "v": 5.0,
   "u": "",
   "d": 0
  },
  "téglalap területe": {
   "v": 12.0,
   "u": "",
   "d": 0
  },
  "téglalap szélessége": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "függőleges eltolás": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "vízszintes eltolás": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "nyújtás": {
   "v": 2.0,
   "u": "",
   "d": 0
  },
  "tükrözés": {
   "v": -1.0,
   "u": "",
   "d": 0
  },
  "süllyesztés": {
   "v": -4.0,
   "u": "",
   "d": 0
  },
  "helyi maximum": {
   "v": 4.0,
   "u": "",
   "d": 0
  },
  "c érték": {
   "v": 5.0,
   "u": "",
   "d": 0
  },
  "megoldás közelítőleg": {
   "v": 2.24,
   "u": "",
   "d": 2
  },
  "egyenes példa": {
   "t": "expr",
   "tok": [
    "2",
    "x",
    "+",
    "1"
   ],
   "tree": [
    "+",
    [
     "imp",
     2,
     "x"
    ],
    1
   ],
   "s": "2x + 1"
  },
  "célgörbe magja": {
   "v": 7.0,
   "u": "",
   "d": 0
  }
 },
 "src": {
  "gép szabálya": 45,
  "gép bemenetei": 46,
  "vizsgált függvény": 64,
  "ÉT eleje": 65,
  "ÉT vége": 66,
  "zérushely 1": 67,
  "zérushely 2": 68,
  "minimum helye": 69,
  "minimum értéke": 70,
  "ÉK felső határa": 71,
  "téglalap területe": 91,
  "téglalap szélessége": 92,
  "függőleges eltolás": 102,
  "vízszintes eltolás": 113,
  "nyújtás": 123,
  "tükrözés": 124,
  "süllyesztés": 136,
  "helyi maximum": 137,
  "c érték": 156,
  "megoldás közelítőleg": 157,
  "egyenes példa": 158,
  "célgörbe magja": 175,
  "alap x": 18,
  "alap x2": 19,
  "alap gyök": 20,
  "alap 1/x": 21,
  "alap abs": 22,
  "a csúszka": 23,
  "u csúszka": 24,
  "v csúszka": 25,
  "abs gomb": 26,
  "eredeti": 27,
  "új görbe": 28,
  "gép": 36,
  "bemenet": 37,
  "kimenet": 38,
  "kör cím": 39,
  "két y": 40,
  "egy y": 41,
  "gép csúszka": 42,
  "ÉT felirat": 54,
  "ÉK felirat": 55,
  "nem az egész": 56,
  "zérushely felirat": 57,
  "minimum felirat": 58,
  "csökken": 59,
  "nő": 60,
  "pont csúszka": 61,
  "lineáris": 79,
  "másodfokú": 80,
  "abszolút": 81,
  "négyzetgyök": 82,
  "reciprok": 83,
  "ÉT mind": 84,
  "ÉT gyök": 85,
  "ÉT reciprok": 86,
  "téglalap cím": 87,
  "szélesség csúszka": 88,
  "fel": 98,
  "le": 99,
  "tipp": 108,
  "nem jobbra": 109,
  "bizonyítás": 110,
  "keskenyebb": 119,
  "tükrözés felirat": 120,
  "felhajtott rész": 130,
  "helyi max": 131,
  "f abs x gomb": 132,
  "nem ugyanaz": 133,
  "megoldás db": 143,
  "nincs megoldás": 144,
  "nem fordítható": 145,
  "fordítható": 146,
  "csak pozitív": 147,
  "tükör": 148,
  "megfordítva": 149,
  "parabola példa": 150,
  "egyenes példa gomb": 151,
  "újra tükröz": 152,
  "c csúszka": 153,
  "célgörbe": 164,
  "talált": 165,
  "még nem": 166,
  "új cél": 167,
  "szabályok": 168,
  "össz v": 169,
  "össz u": 170,
  "össz a": 171,
  "össz abs": 172
 }
};
