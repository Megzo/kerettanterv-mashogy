/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 06-egyenletrendszer.md
   Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/06-egyenletrendszer.md */
window.LESSON_CONTENT = {
 "source": "06-egyenletrendszer.md",
 "title": "Hány tyúk és hány nyúl? – egyenletek, egyenlőtlenségek, egyenletrendszerek",
 "titleLine": 1,
 "meta": {
  "subject": "Matematika",
  "grade": "9–10.",
  "topic": "8. Elsőfokú egyenletek, egyenlőtlenségek, egyenletrendszerek"
 },
 "steps": [
  {
   "title": "A mérleg: mindkét oldalon ugyanazt",
   "html": "<p data-src=\"33\">A mérleg egyensúlyban van: <span class=\"mx\">3<i>x</i> + 5 = <i>x</i> + 13</span>. Vegyünk le <b>mindkét</b> tányérról egy dobozt, aztán öt golyót, végül osszuk két egyenlő részre. <span class=\"key\">Ha mindkét oldallal ugyanazt tesszük, az egyensúly megmarad</span>: <span class=\"mx\"><i>x</i> = 4</span>.</p><p class=\"note\" data-src=\"35\">Vegyél le csak az egyik oldalról: billen!</p>",
   "line": 32,
   "words": 35
  },
  {
   "title": "Egyenlőtlenség: mikor fordul a jel?",
   "html": "<p data-src=\"59\"><span class=\"mx\">2 &lt; 3</span>. Szorozzuk mindkét oldalt mínusz eggyel! Ez a számegyenest a nullára tükrözi, ezért a két pont helyet cserél: <span class=\"mx\">−2 &gt; −3</span>. <span class=\"key\">Negatív számmal szorozva vagy osztva a reláció megfordul.</span> Így <span class=\"mx\">−2<i>x</i> &lt; 6</span>-ból nem <span class=\"mx\"><i>x</i> &lt; −3</span>, hanem <span class=\"mx\"><i>x</i> &gt; −3</span> lesz.</p><p class=\"note\" data-src=\"61\">Húzd a szorzót! Pozitív számnál a jel marad, negatívnál fordul.</p>",
   "line": 58,
   "words": 44
  },
  {
   "title": "Két taxi: melyik éri meg?",
   "html": "<p data-src=\"83\">Az A taxi 700 Ft-tal indul, és 400 Ft/km; a B 1000 Ft-tal, de csak 350 Ft/km. Mindkét ár egy egyenes. <span class=\"key\">Ahol metszik egymást, ott egyenlő az ár</span>: 6 km-nél 3100 Ft. A leolvasott értéket <b>behelyettesítéssel ellenőrizzük</b> – így a grafikus megoldás is pontos. Hosszabb úton a B olcsóbb.</p><p class=\"note\" data-src=\"85\">Húzd a csúszkát: melyik taxi olcsóbb 3 km-en? És 9 km-en?</p>",
   "line": 82,
   "words": 53
  },
  {
   "title": "Tyúkok és nyulak: két egyenlet",
   "html": "<p data-src=\"109\">Egy udvaron tyúkok és nyulak vannak: összesen 35 fej és 94 láb. Hány tyúk és hány nyúl? Legyen <em>x</em> a tyúkok, <em>y</em> a nyulak száma. <span class=\"key\">Két feltétel, két egyenlet</span>: <span class=\"mx\"><i>x</i> + <i>y</i> = 35</span> (fejek) és <span class=\"mx\">2<i>x</i> + 4<i>y</i> = 94</span> (lábak). Próbálgass: minden nyúl két lábbal többet ad!</p><p class=\"note\" data-src=\"111\">Ősi feladat: egy kínai számtankönyvben már szerepel, legalább 1500 éve.</p>",
   "line": 108,
   "words": 51
  },
  {
   "title": "Egy egyenlet = egy egyenes",
   "html": "<p data-src=\"136\">Az <span class=\"mx\"><i>x</i> + <i>y</i> = 35</span> egyenletnek sok megoldása van: <span class=\"mx\">(0; 35)</span>, <span class=\"mx\">(1; 34)</span>, … <span class=\"mx\">(35; 0)</span>. Ábrázolva <span class=\"key\">a megoldások egy egyenesen vannak</span>, és az egyenes minden pontja megoldás. Az udvarhoz csak a nemnegatív egész pontok illenek. A fejek száma mindenhol 35, a lábaké nem!</p><p class=\"note\" data-src=\"138\">Húzd a pontot az egyenesen, és figyeld a lábak számát.</p>",
   "line": 135,
   "words": 47
  },
  {
   "title": "A metszéspont a megoldás",
   "html": "<p data-src=\"147\">A lábak egyenlete is egy egyenes. <span class=\"key\">A két egyenes metszéspontja mindkét egyenletet kielégíti</span>: <span class=\"mx\"><i>M</i>(23; 12)</span>. Számolva: a fejek egyenletét 2-vel szorozzuk, <span class=\"mx\">2<i>x</i> + 2<i>y</i> = 70</span>, és ezt a lábakéból kivonjuk: <span class=\"mx\">2<i>y</i> = 24</span>, tehát <span class=\"mx\"><i>y</i> = 12</span>, <span class=\"mx\"><i>x</i> = 23</span>. Ez az <b>egyenlő együtthatók</b> módszere.</p><p class=\"note\" data-src=\"149\">Behelyettesítéssel is megy: <span class=\"mx\"><i>y</i> = 35 − <i>x</i></span> a második egyenletbe.</p>",
   "line": 146,
   "words": 42
  },
  {
   "title": "Fél nyúl? Ellenőrzés",
   "html": "<p data-src=\"163\">95 lábnál a metszéspont <span class=\"mx\">(22,5; 12,5)</span> – fél nyúl nincs! 150 lábnál <span class=\"mx\"><i>x</i> = −5</span>: negatív tyúk sincs. <span class=\"key\">Az egyenletrendszernek van megoldása, a feladatnak mégsincs.</span> Ezért a kapott számokat mindig visszahelyettesítjük a szövegbe, és megnézzük: egész-e, nemnegatív-e?</p><p class=\"note\" data-src=\"165\">Húzd a lábak számát! Melyik lábszámnál jó a megoldás?</p>",
   "line": 162,
   "words": 42
  },
  {
   "title": "Párhuzamos és egybeeső egyenesek",
   "html": "<p data-src=\"183\">Ha minden állat kétlábú: <span class=\"mx\">2<i>x</i> + 2<i>y</i> = 94</span>, azaz <span class=\"mx\"><i>x</i> + <i>y</i> = 47</span>. Ez párhuzamos a fejekével: <span class=\"key\">nincs metszéspont, nincs megoldás</span>. 70 lábnál a két egyenes egybeesik: végtelen sok megoldás, a második adat nem mond újat.</p><p class=\"note\" data-src=\"185\">Kapcsold vissza a nyulakat!</p>",
   "line": 182,
   "words": 34
  },
  {
   "title": "Összefoglalás",
   "html": "<p data-src=\"207\"><b>Mérlegelv:</b> mindkét oldallal ugyanazt tesszük. <b>Egyenlőtlenség:</b> negatív számmal szorozva vagy osztva megfordul a jel. <b>Egyenletrendszer:</b> két egyenes – <span class=\"key\">a megoldás a metszéspont</span>; egy, egy sem vagy végtelen sok lehet. A végén <b>ellenőrizz</b> a szövegben: értelmes-e a válasz?</p>",
   "line": 206,
   "words": 36
  }
 ],
 "labels": {
  "bizonyítás": "bizonyítás",
  "mérés": "mérés",
  "kitalált adat": "kitalált adat",
  "ellenőrzés": "Ellenőrzés:",
  "fejek": "fejek",
  "lábak": "lábak",
  "tyúk tengely": "x (tyúk)",
  "nyúl tengely": "y (nyúl)",
  "doboz jelentése": "= ismeretlen súly",
  "golyó jelentése": "= 1 egység",
  "lépések cím": "Mérlegelv, lépésenként",
  "csak bal": "csak bal oldalon!",
  "billen": "Billen! Ez már nem egyenlőség.",
  "egy doboz": "1 doboz ugyanannyi, mint 4 golyó",
  "billen tipp": "A mérleg billen – kezdd újra!",
  "kész tipp": "Kész: egy dobozt kaptunk meg.",
  "osztás tipp": "Osztani akkor lehet, ha az egyik oldalon csak doboz van.",
  "üres tipp": "Ebből már nincs mindkét oldalon.",
  "doboz gomb": "−1 doboz mindkét oldalról",
  "golyó gomb": "−1 golyó mindkét oldalról",
  "oszt gomb": "Oszd egyenlő részekre",
  "csak bal gomb": "−1 golyó csak balról",
  "újra gomb": "Újra, magad!",
  "fordul": "a jel megfordul!",
  "marad": "a jel marad",
  "nulla": "mindkettő 0",
  "biz cím": "Miért fordul meg?",
  "biz magyarázat": "mindkét oldalból ugyanazt vontuk ki: ez is mérlegelv",
  "tévhit 2": "Gyakori hiba:",
  "rossz": "rossz",
  "jó": "jó",
  "megoldáshalmaz": "megoldáshalmaz",
  "rossz irány": "a rossz irány",
  "szorzó csúszka": "szorzó (k)",
  "A taxi": "A taxi",
  "B taxi": "B taxi",
  "A olcsóbb": "A olcsóbb",
  "B olcsóbb": "B olcsóbb",
  "egyforma": "egyforma",
  "számolás cím": "Számolással: mikor egyenlő?",
  "útnál": "útnál",
  "út tengely": "út (km)",
  "ár tengely": "ár (Ft)",
  "út csúszka": "út (km)",
  "feladat": "35 fej, 94 láb. Hány tyúk, hány nyúl?",
  "forrás 4": "Kínai feladat, Sunzi suanjing (kb. 3–5. század)",
  "jelölés cím": "Jelöljük:",
  "tyúk": "a tyúkok száma",
  "nyúl": "a nyulak száma",
  "próbálgatás": "Próbálgatás:",
  "fej": "fej",
  "láb": "láb",
  "pont annyi": "pont 94 láb!",
  "hiányzik láb": "még # láb hiányzik",
  "sok láb": "# lábbal több",
  "nyúl ad": "Ha egy tyúk helyére nyúl kerül, a fejek száma marad, a lábaké 2-vel nő.",
  "nyúl csúszka": "nyulak száma (y)",
  "megoldások cím": "A pont koordinátái:",
  "lábak most": "és a lábak száma:",
  "egyenes": "Minden ilyen pont egy egyenesen van.",
  "tyúk csúszka": "tyúkok száma (x)",
  "módszer cím": "Egyenlő együtthatók módszere",
  "kivonva": "kivonva",
  "mindkettő igaz": "mindkét egyenlet igaz",
  "csak az egyik": "csak a fejek stimmelnek",
  "húzd a pontot": "Húzd a pontot a metszéspontba!",
  "tyúk csúszka 6": "tyúkok száma (x)",
  "értelmes": "itt értelmes",
  "egész": "egész szám?",
  "nemnegatív": "nemnegatív?",
  "jó megoldás": "jó megoldás",
  "fél nyúl": "fél állat – nincs ilyen udvar",
  "negatív tyúk": "negatív tyúk – nincs ilyen udvar",
  "negatív nyúl": "negatív nyúl – nincs ilyen udvar",
  "van megoldás": "Az egyenletrendszernek van megoldása, a feladatnak nincs.",
  "láb csúszka": "lábak száma",
  "kétlábú cím": "Minden állat kétlábú",
  "négylábú cím": "Tyúkok és nyulak",
  "ugyanaz": "ugyanaz az egyenlet!",
  "ellentmondás": "ellentmondás",
  "egy megoldás": "egy megoldás",
  "nincs megoldás": "nincs megoldás",
  "végtelen sok": "végtelen sok megoldás",
  "egyértelmű": "Két metsző egyenes: pontosan egy közös pont.",
  "ellentmondó": "Ellentmondó adatok: a két feltétel nem teljesülhet egyszerre.",
  "hiányos": "Hiányos adat: a második egyenlet nem mond újat.",
  "három eset": "Két egyenes – három eset",
  "metsző": "metsző",
  "párhuzamos": "párhuzamos",
  "egybeeső": "egybeeső",
  "kétlábú gomb": "Minden állat kétlábú",
  "négylábú gomb": "Nyulak vissza",
  "láb csúszka 8": "lábak száma",
  "össz 1 cím": "Mérlegelv",
  "össz 1": "mindkét oldallal ugyanazt",
  "össz 2 cím": "Egyenlőtlenség",
  "össz 2": "Negatív számmal szorozva vagy osztva a reláció megfordul.",
  "össz 3 cím": "Egyenletrendszer",
  "össz 3": "A megoldás a két egyenes metszéspontja: egy, egy sem vagy végtelen sok.",
  "össz 4 cím": "Ellenőrizz!",
  "össz 4": "Fél nyúl nincs: helyettesíts vissza a szövegbe!"
 },
 "data": {
  "fejek száma": {
   "v": 35.0,
   "u": "",
   "d": 0
  },
  "lábak száma": {
   "v": 94.0,
   "u": "",
   "d": 0
  },
  "mérleg egyenlet": {
   "t": "expr",
   "tok": [
    "3",
    "x",
    "+",
    "5",
    "=",
    "x",
    "+",
    "13"
   ],
   "tree": [
    "=",
    [
     "+",
     [
      "imp",
      3,
      "x"
     ],
     5
    ],
    [
     "+",
     "x",
     13
    ]
   ],
   "s": "3x + 5 = x + 13"
  },
  "mérleg megoldás": {
   "v": 4.0,
   "u": "",
   "d": 0
  },
  "pontpár": {
   "t": "list",
   "v": [
    2.0,
    3.0
   ],
   "u": "",
   "d": 0,
   "s": "2; 3"
  },
  "hibás egyenlőtlenség": {
   "t": "expr",
   "tok": [
    "−",
    "2",
    "x",
    "<",
    "6"
   ],
   "tree": [
    "<",
    [
     "imp",
     [
      "neg",
      2
     ],
     "x"
    ],
    6
   ],
   "s": "−2x < 6"
  },
  "egyenlőtlenség határa": {
   "v": -3.0,
   "u": "",
   "d": 0
  },
  "próbapontok": {
   "t": "list",
   "v": [
    0.0,
    -4.0
   ],
   "u": "",
   "d": 0,
   "s": "0; −4"
  },
  "A alapdíj": {
   "v": 700.0,
   "u": "Ft",
   "d": 0
  },
  "A km-díj": {
   "v": 400.0,
   "u": "Ft/km",
   "d": 0
  },
  "B alapdíj": {
   "v": 1000.0,
   "u": "Ft",
   "d": 0
  },
  "B km-díj": {
   "v": 350.0,
   "u": "Ft/km",
   "d": 0
  },
  "kiegyenlítés távolsága": {
   "v": 6.0,
   "u": "km",
   "d": 0
  },
  "kiegyenlítés ára": {
   "v": 3100.0,
   "u": "Ft",
   "d": 0
  },
  "nyulak": {
   "v": 12.0,
   "u": "",
   "d": 0
  },
  "tyúkok": {
   "v": 23.0,
   "u": "",
   "d": 0
  },
  "fél nyúl lábszám": {
   "v": 95.0,
   "u": "",
   "d": 0
  },
  "negatív tyúk lábszám": {
   "v": 150.0,
   "u": "",
   "d": 0
  }
 },
 "src": {
  "fejek száma": 29,
  "lábak száma": 30,
  "mérleg egyenlet": 55,
  "mérleg megoldás": 56,
  "pontpár": 77,
  "hibás egyenlőtlenség": 78,
  "egyenlőtlenség határa": 79,
  "próbapontok": 80,
  "A alapdíj": 101,
  "A km-díj": 102,
  "B alapdíj": 103,
  "B km-díj": 104,
  "kiegyenlítés távolsága": 105,
  "kiegyenlítés ára": 106,
  "nyulak": 129,
  "tyúkok": 160,
  "fél nyúl lábszám": 179,
  "negatív tyúk lábszám": 180,
  "bizonyítás": 19,
  "mérés": 20,
  "kitalált adat": 21,
  "ellenőrzés": 22,
  "fejek": 23,
  "lábak": 24,
  "tyúk tengely": 25,
  "nyúl tengely": 26,
  "doboz jelentése": 38,
  "golyó jelentése": 39,
  "lépések cím": 40,
  "csak bal": 41,
  "billen": 42,
  "egy doboz": 43,
  "billen tipp": 44,
  "kész tipp": 45,
  "osztás tipp": 46,
  "üres tipp": 47,
  "doboz gomb": 48,
  "golyó gomb": 49,
  "oszt gomb": 50,
  "csak bal gomb": 51,
  "újra gomb": 52,
  "fordul": 64,
  "marad": 65,
  "nulla": 66,
  "biz cím": 67,
  "biz magyarázat": 68,
  "tévhit 2": 69,
  "rossz": 70,
  "jó": 71,
  "megoldáshalmaz": 72,
  "rossz irány": 73,
  "szorzó csúszka": 74,
  "A taxi": 88,
  "B taxi": 89,
  "A olcsóbb": 90,
  "B olcsóbb": 91,
  "egyforma": 92,
  "számolás cím": 93,
  "útnál": 94,
  "út tengely": 95,
  "ár tengely": 96,
  "út csúszka": 97,
  "feladat": 114,
  "forrás 4": 115,
  "jelölés cím": 116,
  "tyúk": 117,
  "nyúl": 118,
  "próbálgatás": 119,
  "fej": 120,
  "láb": 121,
  "pont annyi": 122,
  "hiányzik láb": 123,
  "sok láb": 124,
  "nyúl ad": 125,
  "nyúl csúszka": 126,
  "megoldások cím": 141,
  "lábak most": 142,
  "egyenes": 143,
  "tyúk csúszka": 144,
  "módszer cím": 152,
  "kivonva": 153,
  "mindkettő igaz": 154,
  "csak az egyik": 155,
  "húzd a pontot": 156,
  "tyúk csúszka 6": 157,
  "értelmes": 168,
  "egész": 169,
  "nemnegatív": 170,
  "jó megoldás": 171,
  "fél nyúl": 172,
  "negatív tyúk": 173,
  "negatív nyúl": 174,
  "van megoldás": 175,
  "láb csúszka": 176,
  "kétlábú cím": 188,
  "négylábú cím": 189,
  "ugyanaz": 190,
  "ellentmondás": 191,
  "egy megoldás": 192,
  "nincs megoldás": 193,
  "végtelen sok": 194,
  "egyértelmű": 195,
  "ellentmondó": 196,
  "hiányos": 197,
  "három eset": 198,
  "metsző": 199,
  "párhuzamos": 200,
  "egybeeső": 201,
  "kétlábú gomb": 202,
  "négylábú gomb": 203,
  "láb csúszka 8": 204,
  "össz 1 cím": 210,
  "össz 1": 211,
  "össz 2 cím": 212,
  "össz 2": 213,
  "össz 3 cím": 214,
  "össz 3": 215,
  "össz 4 cím": 216,
  "össz 4": 217
 }
};
