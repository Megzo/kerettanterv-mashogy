/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 08-masodfoku.md
   Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/08-masodfoku.md */
window.LESSON_CONTENT = {
 "source": "08-masodfoku.md",
 "title": "Hol metszi a parabola a tengelyt? – teljes négyzet, megoldóképlet, diszkrimináns",
 "titleLine": 1,
 "meta": {
  "subject": "Matematika",
  "grade": "9–10.",
  "topic": "9. Másodfokú egyenletek, egyenlőtlenségek (+ 6. Betűs kifejezések, 10. Függvények)"
 },
 "steps": [
  {
   "title": "Al-Hvárizmi négyzete",
   "html": "<p data-src=\"24\">Al-Hvárizmi bagdadi tudós könyvének feladata: <span class=\"mx\"><i>x</i><sup>2</sup> + 10<i>x</i> = 39</span>. Rajzoljuk le! Az <span class=\"mx\"><i>x</i><sup>2</sup></span> egy négyzet, a <span class=\"mx\">10<i>x</i></span> két <span class=\"mx\">5<i>x</i></span>-es csík a két oldalán. A sarokból hiányzik egy <span class=\"mx\">5 · 5</span>-ös négyzet – tegyük be! <span class=\"key\">Így egy <span class=\"mx\"><i>x</i> + 5</span> oldalú, 64 területű négyzet lesz</span>: az oldala 8, tehát <span class=\"mx\"><i>x</i> = 3</span>.</p><p class=\"note\" data-src=\"26\">Ő csak a pozitív megoldást kereste. Van másik is – a 4. lépésben kiderül.</p>",
   "line": 23,
   "words": 54
  },
  {
   "title": "Teljes négyzet a betűkkel",
   "html": "<p data-src=\"46\">Ugyanez minden <em>b</em>-re: az <span class=\"mx\"><i>x</i><sup>2</sup> + <i>bx</i></span> mellé két <span class=\"mx\"><i>b</i>/2 · <i>x</i></span>-es csík kerül, a sarokból <span class=\"mx\">(<i>b</i>/2)<sup>2</sup></span> hiányzik. Hozzáadjuk, és ugyanannyit le is vonunk: <span class=\"key\"><span class=\"mx\"><i>x</i><sup>2</sup> + <i>bx</i> = (<i>x</i> + <i>b</i>/2)<sup>2</sup> − (<i>b</i>/2)<sup>2</sup></span>.</span> Negatív <em>b</em>-re a rajz nem működik, a számolás igen.</p><p class=\"note\" data-src=\"48\">Húzd a <em>b</em> csúszkát! A példa a következő lépés függvénye.</p>",
   "line": 45,
   "words": 40
  },
  {
   "title": "A parabola csúcsa",
   "html": "<p data-src=\"58\">A teljes négyzetes alakból leolvasható a grafikon: <span class=\"mx\">(<i>x</i> − 2)<sup>2</sup> − 1</span> az <span class=\"mx\"><i>x</i><sup>2</sup></span> parabolája <b>2-vel jobbra és 1-gyel lefelé</b> tolva. Mivel <span class=\"mx\">(<i>x</i> − 2)<sup>2</sup> ≥ 0</span>, a függvény <span class=\"key\">legkisebb értéke −1, az <span class=\"mx\"><i>x</i> = 2</span> helyen</span>: ez a csúcs. A parabola az <span class=\"mx\"><i>x</i> = 2</span> egyenesre szimmetrikus.</p><p class=\"note\" data-src=\"60\">Húzd a pontot: a magassága a csúcs fölött éppen <span class=\"mx\">(<i>x</i> − 2)<sup>2</sup></span>.</p>",
   "line": 57,
   "words": 46
  },
  {
   "title": "Hol metszi a tengelyt?",
   "html": "<p data-src=\"74\">A zérushelyen <span class=\"mx\"><i>f</i>(<i>x</i>) = 0</span>, azaz <span class=\"mx\">(<i>x</i> − 2)<sup>2</sup> = 1</span>. Melyik szám négyzete 1? Az 1-é <b>és a −1-é</b> is! Tehát <span class=\"mx\"><i>x</i> − 2 = 1</span> vagy <span class=\"mx\"><i>x</i> − 2 = −1</span>, így <span class=\"key\"><span class=\"mx\"><i>x</i> = 3</span> vagy <span class=\"mx\"><i>x</i> = 1</span></span> – a csúcstól egyformán messze. Az <span class=\"mx\"><i>x</i><sup>2</sup> = 9</span>-nek is két megoldása van: 3 és −3.</p><p class=\"note\" data-src=\"76\">Al-Hvárizmi egyenlete: <span class=\"mx\"><i>x</i> + 5 = −8</span> is lehet, tehát <span class=\"mx\"><i>x</i> = −13</span>.</p>",
   "line": 73,
   "words": 43
  },
  {
   "title": "A diszkrimináns",
   "html": "<p data-src=\"88\">A parabola <b>metszi, érinti vagy elkerüli</b> a tengelyt. Melyik? Egyetlen szám dönti el, a <b>diszkrimináns</b>: <span class=\"mx\"><i>D</i> = <i>b</i><sup>2</sup> − 4<i>ac</i></span>. <span class=\"key\"><span class=\"mx\"><i>D</i> &gt; 0</span>: két megoldás, <span class=\"mx\"><i>D</i> = 0</span>: egy, <span class=\"mx\"><i>D</i> &lt; 0</span>: nincs valós megoldás.</span></p>",
   "line": 87,
   "words": 25
  },
  {
   "title": "Megoldóképlet és gyöktényezős alak",
   "html": "<p data-src=\"103\">A teljes négyzetté kiegészítés betűkkel adja a <b>megoldóképletet</b>:</p><p class=\"big-fx\" data-src=\"105\"><span class=\"mx\"><i>x</i> = <span class=\"frac\"><span class=\"fn\">−<i>b</i> ± <span class=\"rt\">√<span class=\"rad\"><span class=\"rp\">(</span><i>b</i><sup>2</sup> − 4<i>ac</i><span class=\"rp\">)</span></span></span></span><span class=\"fs\">/</span><span class=\"fd\">2<i>a</i></span></span></span></p><p data-src=\"107\">Példa: <span class=\"mx\">2<i>x</i><sup>2</sup> + 3<i>x</i> − 2 = 0</span>, <span class=\"mx\"><i>D</i> = 25</span>, <span class=\"mx\"><i>x</i> = (−3 ± 5)/4</span>, <span class=\"key\">így <span class=\"mx\"><i>x</i><sub>1</sub> = 0,5</span> és <span class=\"mx\"><i>x</i><sub>2</sub> = −2</span>.</span> A <b>gyöktényezős alak</b>, <span class=\"mx\">2(<i>x</i> − 0,5)(<i>x</i> + 2)</span>, a zérushelyeket mutatja. Negatív <em>D</em>-nél nincs valós gyök: negatív számnak nincs négyzetgyöke.</p>",
   "line": 102,
   "words": 35
  },
  {
   "title": "Ne ossz x-szel!",
   "html": "<p data-src=\"126\">Csábító: <span class=\"mx\"><i>x</i><sup>2</sup> = 3<i>x</i></span>, osszunk <em>x</em>-szel, és kész: <span class=\"mx\"><i>x</i> = 3</span>. De a grafikonok <b>két</b> pontban metszik egymást! <em>x</em>-szel osztani csak <span class=\"mx\"><i>x</i> ≠ 0</span> esetén szabad: <span class=\"key\">az <span class=\"mx\"><i>x</i> = 0</span> megoldás elveszett.</span> Helyesen: <span class=\"mx\"><i>x</i><sup>2</sup> − 3<i>x</i> = 0</span>, kiemelve <span class=\"mx\"><i>x</i>(<i>x</i> − 3) = 0</span>. Egy szorzat akkor 0, ha valamelyik tényezője 0.</p>",
   "line": 125,
   "words": 36
  },
  {
   "title": "Mikor negatív? (egyenlőtlenség)",
   "html": "<p data-src=\"140\">Sokan így oldják meg: <span class=\"mx\"><i>x</i><sup>2</sup> − <i>x</i> − 6 &lt; 0</span>, tehát <span class=\"mx\"><i>x</i> &lt; 3</span>. Próbáld ki az <span class=\"mx\"><i>x</i> = −3</span>-at: <span class=\"mx\">9 + 3 − 6 = 6</span>, ez nem negatív! A zérushelyek −2 és 3, és <span class=\"key\">a parabola csak a kettő között van a tengely alatt</span>: <span class=\"mx\">−2 &lt; <i>x</i> &lt; 3</span>, vagyis <span class=\"mx\"><i>x</i> ∈ ]−2; 3[</span>.</p><p class=\"note\" data-src=\"142\">Próbáld a többi relációt is!</p>",
   "line": 139,
   "words": 39
  },
  {
   "title": "A legnagyobb kert – összefoglalás",
   "html": "<p data-src=\"167\">20 m spárgával téglalap alakú kertet kerítünk. Ha az egyik oldal <em>x</em>, a másik <span class=\"mx\">10 − <i>x</i></span>, a terület <span class=\"mx\"><i>T</i>(<i>x</i>) = <i>x</i>(10 − <i>x</i>)</span>. Húzd a sarkot! Teljes négyzettel: <span class=\"mx\"><i>T</i>(<i>x</i>) = 25 − (<i>x</i> − 5)<sup>2</sup> ≤ 25</span>. <span class=\"key\">A legnagyobb kert az <span class=\"mx\">5 · 5</span>-ös négyzet, 25 m².</span></p>",
   "line": 166,
   "words": 31
  }
 ],
 "labels": {
  "bizonyítás": "bizonyítás",
  "mérés": "mérés",
  "csúcs felirat": "csúcs",
  "vagy": "vagy",
  "forrás 1": "al-Hvárizmi, Bagdad, kb. 820",
  "algebra szó": "a könyv címéből (al-dzsabr) lett az „algebra” szó",
  "terület 1": "területük együtt:",
  "hiányzik": "hiányzik:",
  "kész négyzet": "teljes négyzet",
  "pozitív": "al-Hvárizmi: csak pozitív",
  "újra 1 gomb": "Rakd össze újra!",
  "b csúszka": "b (az x-es tag szorzója)",
  "x bármi": "x bármilyen pozitív szám",
  "ennyi hiányzik": "ennyi hiányzik",
  "általános": "általában:",
  "példa cím": "Példa (negatív b):",
  "jobbra": "jobbra",
  "lefelé": "lefelé",
  "szimmetriatengely": "szimmetriatengely",
  "pont csúszka": "x (a pont helye)",
  "csúcs fölött": "a csúcs fölött:",
  "tévhit 4": "Csak egy megoldás?",
  "négyzet 1": "melyik szám négyzete 1?",
  "egyforma": "egyformán messze",
  "a csúszka": "a (az x² szorzója)",
  "b csúszka 5": "b (az x szorzója)",
  "c csúszka": "c (a konstans tag)",
  "mérő cím": "diszkrimináns",
  "két megoldás": "2 megoldás",
  "egy megoldás": "1 megoldás",
  "nincs megoldás": "nincs valós megoldás",
  "nem hiba": "nem hiba: a parabola nem éri el a tengelyt",
  "nem másodfokú": "a = 0: ez már nem másodfokú",
  "alaphelyzet 5": "Alaphelyzet",
  "levezetés cím": "Honnan jön? Teljes négyzet betűkkel",
  "szoroz": "szorozzuk 4a-val",
  "teljes négyzet": "teljes négyzet!",
  "ha D": "ha `D >= 0`",
  "behelyettesítés": "behelyettesítve:",
  "gyöktényezős cím": "gyöktényezős alak:",
  "nem bontható": "nincs valós gyök – nem bontható",
  "egy gyök": "egy (kétszeres) gyök",
  "rossz út": "osztunk x-szel:",
  "elveszett": "elveszett megoldás!",
  "nem oszthatsz": "ha x = 0, nem oszthatsz vele",
  "jó út": "kiemelünk:",
  "szorzat nulla": "a szorzat 0, ha egy tényezője 0",
  "k csúszka": "k (az egyenlet: x² = k · x)",
  "sokan így": "Sokan így:",
  "ellenpélda": "ellenpélda:",
  "nem negatív": "nem negatív!",
  "itt negatív": "itt negatív",
  "itt pozitív": "itt pozitív",
  "megoldás 8": "megoldás:",
  "próbapont csúszka": "próbapont x",
  "igaz": "igaz",
  "hamis": "hamis",
  "nincs megoldás 8": "nincs megoldás",
  "minden x": "minden x megoldás",
  "kisebb gomb": "< 0",
  "nagyobb gomb": "> 0",
  "legfeljebb gomb": "≤ 0",
  "legalább gomb": "≥ 0",
  "spárga": "spárga:",
  "kert": "kert",
  "oldal csúszka": "x (a kert egyik oldala, m)",
  "terület tengely": "T (m²)",
  "oldal tengely": "x (m)",
  "maximum": "maximum!",
  "össz 1 cím": "Teljes négyzet",
  "össz 2 cím": "Csúcs",
  "össz 3 cím": "Hány megoldás?",
  "össz 4 cím": "Egyenlőtlenség",
  "össz 3": "D > 0: 2 · D = 0: 1 · D < 0: 0",
  "össz 4": "a grafikonról olvasd le!"
 },
 "data": {
  "hvárizmi b": {
   "v": 10.0,
   "u": "",
   "d": 0
  },
  "hvárizmi c": {
   "v": 39.0,
   "u": "",
   "d": 0
  },
  "hvárizmi megoldás": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "példa függvény": {
   "t": "expr",
   "tok": [
    "x",
    "^",
    "2",
    "−",
    "4",
    "x",
    "+",
    "3"
   ],
   "tree": [
    "+",
    [
     "−",
     [
      "^",
      "x",
      2
     ],
     [
      "imp",
      4,
      "x"
     ]
    ],
    3
   ],
   "s": "x^2 − 4x + 3"
  },
  "példa csúcs": {
   "t": "point",
   "x": 2.0,
   "y": -1.0,
   "s": "(2; −1)"
  },
  "példa zérushelyek": {
   "t": "list",
   "v": [
    1.0,
    3.0
   ],
   "u": "",
   "d": 0,
   "s": "1; 3"
  },
  "négyzet példa": {
   "v": 9.0,
   "u": "",
   "d": 0
  },
  "példa 6a": {
   "t": "expr",
   "tok": [
    "2",
    "x",
    "^",
    "2",
    "+",
    "3",
    "x",
    "−",
    "2"
   ],
   "tree": [
    "−",
    [
     "+",
     [
      "imp",
      2,
      [
       "^",
       "x",
       2
      ]
     ],
     [
      "imp",
      3,
      "x"
     ]
    ],
    2
   ],
   "s": "2x^2 + 3x − 2"
  },
  "példa 6b": {
   "t": "expr",
   "tok": [
    "x",
    "^",
    "2",
    "−",
    "6",
    "x",
    "+",
    "9"
   ],
   "tree": [
    "+",
    [
     "−",
     [
      "^",
      "x",
      2
     ],
     [
      "imp",
      6,
      "x"
     ]
    ],
    9
   ],
   "s": "x^2 − 6x + 9"
  },
  "példa 6c": {
   "t": "expr",
   "tok": [
    "x",
    "^",
    "2",
    "+",
    "2",
    "x",
    "+",
    "5"
   ],
   "tree": [
    "+",
    [
     "+",
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
    5
   ],
   "s": "x^2 + 2x + 5"
  },
  "6a gyökei": {
   "t": "list",
   "v": [
    -2.0,
    0.5
   ],
   "u": "",
   "d": 1,
   "s": "−2; 0,5"
  },
  "osztás k": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "egyenlőtlenség": {
   "t": "expr",
   "tok": [
    "x",
    "^",
    "2",
    "−",
    "x",
    "−",
    "6"
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
     "x"
    ],
    6
   ],
   "s": "x^2 − x − 6"
  },
  "ellenpélda x": {
   "v": -3.0,
   "u": "",
   "d": 0
  },
  "egyenlőtlenség határai": {
   "t": "list",
   "v": [
    -2.0,
    3.0
   ],
   "u": "",
   "d": 0,
   "s": "−2; 3"
  },
  "spárga hossza": {
   "v": 20.0,
   "u": "m",
   "d": 0
  },
  "legnagyobb terület": {
   "v": 25.0,
   "u": "m²",
   "d": 0
  }
 },
 "src": {
  "hvárizmi b": 38,
  "hvárizmi c": 39,
  "hvárizmi megoldás": 40,
  "példa függvény": 70,
  "példa csúcs": 71,
  "példa zérushelyek": 84,
  "négyzet példa": 85,
  "példa 6a": 120,
  "példa 6b": 121,
  "példa 6c": 122,
  "6a gyökei": 123,
  "osztás k": 137,
  "egyenlőtlenség": 162,
  "ellenpélda x": 163,
  "egyenlőtlenség határai": 164,
  "spárga hossza": 184,
  "legnagyobb terület": 185,
  "bizonyítás": 18,
  "mérés": 19,
  "csúcs felirat": 20,
  "vagy": 21,
  "forrás 1": 29,
  "algebra szó": 30,
  "terület 1": 31,
  "hiányzik": 32,
  "kész négyzet": 33,
  "pozitív": 34,
  "újra 1 gomb": 35,
  "b csúszka": 51,
  "x bármi": 52,
  "ennyi hiányzik": 53,
  "általános": 54,
  "példa cím": 55,
  "jobbra": 63,
  "lefelé": 64,
  "szimmetriatengely": 65,
  "pont csúszka": 66,
  "csúcs fölött": 67,
  "tévhit 4": 79,
  "négyzet 1": 80,
  "egyforma": 81,
  "a csúszka": 91,
  "b csúszka 5": 92,
  "c csúszka": 93,
  "mérő cím": 94,
  "két megoldás": 95,
  "egy megoldás": 96,
  "nincs megoldás": 97,
  "nem hiba": 98,
  "nem másodfokú": 99,
  "alaphelyzet 5": 100,
  "levezetés cím": 110,
  "szoroz": 111,
  "teljes négyzet": 112,
  "ha D": 113,
  "behelyettesítés": 114,
  "gyöktényezős cím": 115,
  "nem bontható": 116,
  "egy gyök": 117,
  "rossz út": 129,
  "elveszett": 130,
  "nem oszthatsz": 131,
  "jó út": 132,
  "szorzat nulla": 133,
  "k csúszka": 134,
  "sokan így": 145,
  "ellenpélda": 146,
  "nem negatív": 147,
  "itt negatív": 148,
  "itt pozitív": 149,
  "megoldás 8": 150,
  "próbapont csúszka": 151,
  "igaz": 152,
  "hamis": 153,
  "nincs megoldás 8": 154,
  "minden x": 155,
  "kisebb gomb": 156,
  "nagyobb gomb": 157,
  "legfeljebb gomb": 158,
  "legalább gomb": 159,
  "spárga": 170,
  "kert": 171,
  "oldal csúszka": 172,
  "terület tengely": 173,
  "oldal tengely": 174,
  "maximum": 175,
  "össz 1 cím": 176,
  "össz 2 cím": 177,
  "össz 3 cím": 178,
  "össz 4 cím": 179,
  "össz 3": 180,
  "össz 4": 181
 }
};
