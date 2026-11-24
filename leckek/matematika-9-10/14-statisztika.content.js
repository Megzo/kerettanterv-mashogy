/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 14-statisztika.md
   Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/14-statisztika.md */
window.LESSON_CONTENT = {
 "source": "14-statisztika.md",
 "title": "Kinek hazudik az átlag? – középértékek, szóródás, diagramtrükkök",
 "titleLine": 1,
 "meta": {
  "subject": "Matematika",
  "grade": "9–10.",
  "topic": "16. Leíró statisztika"
 },
 "steps": [
  {
   "title": "Az átlag: az egyensúly pontja",
   "html": "<p data-src=\"29\">Egy kis cég kilenc dolgozójának bére egy deszkán: minden bér egy egyforma súly. Hol kell alátámasztani, hogy ne billenjen? <span class=\"key\">Pontosan az átlagnál.</span> Ott a bal oldali eltérések összege egyenlő a jobb oldaliakéval: 227,8 ezer Ft mindkét oldalon. Húzz el egy súlyt: a deszka megbillen, az alátámasztás utánacsúszik.</p><p class=\"note\" data-src=\"31\">Bizonyítsd: az átlagtól való eltérések összege mindig 0.</p>",
   "line": 28,
   "words": 55
  },
  {
   "title": "Megérkezik a tulajdonos",
   "html": "<p data-src=\"52\"><span class=\"key\">Tippelj előbb!</span> Belép a tulajdonos is, havi 6000 ezer forinttal. Az átlag 1037 ezer Ft lesz – több, mint amennyit a kilenc dolgozó bármelyike keres. A medián csak 490 ezer Ft. <span class=\"key\">Egy kiugró adat az átlagot elrántja, a mediánt alig mozdítja.</span> Húzd a csúszkát!</p><p class=\"note\" data-src=\"54\">Melyik számot írná egy álláshirdetés? Melyiket a szakszervezet?</p>",
   "line": 51,
   "words": 51
  },
  {
   "title": "Valódi adat: átlagkereset és mediánkereset",
   "html": "<p data-src=\"75\">A KSH szerint (2024. október) a teljes munkaidőben dolgozók bruttó <b>átlagkeresete</b> 637 200 Ft, <b>mediánkeresete</b> csak 529 000 Ft volt. Az eloszlás <b>jobbra elnyúló</b>: kevés nagyon magas kereset húzza fel az átlagot. <span class=\"key\">Mivel a medián kisebb az átlagnál, a dolgozók legalább fele az átlag alatt keres.</span></p><p class=\"note\" data-src=\"77\">A görbe csak az eloszlás alakját mutatja (modell), a két jelölt érték valódi.</p>",
   "line": 74,
   "words": 54
  },
  {
   "title": "Melyik jegy jár? – mikor melyik középérték",
   "html": "<p data-src=\"102\">Jegyeid: 2; 3; 5; 5; 5. Az átlag 4, a medián és a módusz 5. <span class=\"key\">Ugyanaz az adatsor, három „igazság”</span> – érvelj az ötösért! Húzd a jegyeket: mikor ad a három mutató különböző jegyet? Ökölszabály: torz, kiugró adatoknál a <b>medián</b>, ha az összeg számít, az <b>átlag</b>, kategóriáknál a <b>módusz</b> a beszédes.</p>",
   "line": 101,
   "words": 46
  },
  {
   "title": "Ugyanaz az átlag, mégis más: a szóródás",
   "html": "<p data-src=\"123\">Két kosaras hat meccse: átlag, medián, módusz egyaránt 16 pont. Mégis más a kettő! A <b>terjedelem</b>: legnagyobb adat − legkisebb adat. A <b>szórás</b> az átlagtól való <span class=\"mx\"><i>d</i></span> eltérések tipikus mérete: <span class=\"key\">az eltérésnégyzetek átlagának négyzetgyöke</span> (piros négyzet).</p><p class=\"big-fx\" data-src=\"125\"><span class=\"mx\"><i>σ</i> = <span class=\"rt\">√<span class=\"rad\"><span class=\"rp\">(</span><span class=\"frac\"><span class=\"fn\"><i>d</i><sub>1</sub><sup>2</sup> + … + <i>d</i><sub><i>n</i></sub><sup>2</sup></span><span class=\"fs\">/</span><span class=\"fd\"><i>n</i></span></span><span class=\"rp\">)</span></span></span></span></p>",
   "line": 122,
   "words": 38
  },
  {
   "title": "Kvartilisek és dobozábra",
   "html": "<p data-src=\"152\">Rendezd sorba a tizenegy adatot! A medián kettévágja a sort, a két fél mediánja az <b>alsó</b> és a <b>felső kvartilis</b> (<span class=\"mx\"><i>Q</i><sub>1</sub></span>, <span class=\"mx\"><i>Q</i><sub>3</sub></span>). A <b>dobozábra</b> öt számot mutat: legkisebb, <span class=\"mx\"><i>Q</i><sub>1</sub></span>, medián, <span class=\"mx\"><i>Q</i><sub>3</sub></span>, legnagyobb. <span class=\"key\">A dobozban van az adatok középső fele.</span> Húzd a pöttyöket: melyik szám mozdul?</p>",
   "line": 151,
   "words": 45
  },
  {
   "title": "A levágott tengely",
   "html": "<p data-src=\"179\">Két jelölt: 52 % és 48 %. Húzd a csúszkát: honnan induljon a függőleges tengely? Ha 45 %-nál kezdődik, az egyik oszlop 2,33-szer olyan magas, mint a másik – pedig a valódi arány csak kb. 1,08. <span class=\"key\">Oszlopdiagramon a tengely 0-tól induljon, különben az oszlopok magassága hazudik.</span></p><p class=\"note\" data-src=\"181\">Keress a hírekben levágott tengelyű diagramot, és rajzold újra 0-tól!</p>",
   "line": 178,
   "words": 53
  },
  {
   "title": "Együtt mozog – de oka-e?",
   "html": "<p data-src=\"202\">Húsz nyári nap: amikor több fagyi fogyott, többen égtek le. <span class=\"key\">Okozza a fagyi a leégést?</span> Nem: mindkettőt egy <b>harmadik tényező</b>, a napos meleg növeli. Hasonló hőmérsékletű napokon az összefüggés eltűnik. <span class=\"key\">Az együttmozgás (korreláció) nem bizonyít ok-okozatot.</span></p><p class=\"note\" data-src=\"204\">Cipőméret és helyesírás alsósoknál – mi a harmadik tényező?</p>",
   "line": 201,
   "words": 44
  },
  {
   "title": "Összefoglalás",
   "html": "<ul><li data-src=\"231\"><b>Átlag:</b> egyensúlyi pont; a kiugró adat elrántja. <b>Medián:</b> középső adat; kiugró adatnál beszédesebb. <b>Módusz:</b> a leggyakoribb.</li><li data-src=\"232\"><b>Szóródás:</b> terjedelem, szórás, kvartilisek – dobozábra.</li><li data-src=\"233\"><span class=\"key\">Diagramon a tengely 0-tól induljon.</span></li><li data-src=\"234\"><span class=\"key\">Az együttmozgás nem ok-okozat.</span></li></ul>",
   "line": 230,
   "words": 30
  }
 ],
 "labels": {
  "kitalált adat": "kitalált adat",
  "valós adat": "valós adat",
  "modell bélyeg": "modell – csak az alak szemléltetés",
  "kitekintés": "kitekintés – 11–12. évfolyam",
  "átlag": "átlag",
  "medián": "medián",
  "módusz": "módusz",
  "ezer Ft": "ezer Ft",
  "bérek cím": "Havi bér egy kilencfős cégnél",
  "bal oldal": "bal oldali eltérések: #",
  "jobb oldal": "jobb oldali eltérések: #",
  "egyensúly": "egyensúlyban",
  "billen": "billen…",
  "bér tengely": "bér (ezer Ft)",
  "alaphelyzet 1": "Eredeti bérek",
  "kérdés 2": "Mennyi lesz most az átlag?",
  "tippelj": "Tippelj előbb!",
  "tipp 2a": "kb. 500",
  "tipp 2b": "kb. 700",
  "tipp 2c": "1000 fölött",
  "a tipped": "a te tipped",
  "tulajdonos csúszka": "a tulajdonos bére (ezer Ft)",
  "tulajdonos": "tulajdonos",
  "dolgozók az átlag alatt": "az átlag alatt: # dolgozó a #-ből",
  "ksh cím": "Bruttó havi kereset Magyarországon",
  "dolgozók fele": "a dolgozók fele",
  "forrás ksh": "Forrás: KSH, Keresetek gyorstájékoztató, #",
  "kereset tengely": "bruttó kereset (ezer Ft)",
  "gyakoriság tengely": "dolgozók aránya",
  "különbség": "az átlag # %-kal több a mediánnál",
  "jegyek cím": "Év végi jegyek matekból",
  "jegy tengely": "érdemjegy",
  "jegy szerint": "→ jegy: #",
  "alaphelyzet 4": "Eredeti jegyek",
  "mikor medián": "bérek, lakásárak: kiugró adatok",
  "mikor átlag": "összeg számít: költség, termés",
  "mikor módusz": "kategória: cipőméret, kedvenc szín",
  "ökölszabály": "ökölszabály",
  "játékos A": "Andi",
  "játékos B": "Bori",
  "játékos gomb": "Andi ↔ Bori",
  "pont tengely": "pont meccsenként",
  "terjedelem": "terjedelem: #",
  "szórás": "szórás: σ #",
  "átlagos négyzet": "az eltérésnégyzetek átlaga",
  "alaphelyzet 5": "Eredeti pontok",
  "képernyő cím": "Napi képernyőidő (perc), 11 diák",
  "perc tengely": "perc",
  "alsó fél": "alsó fél",
  "felső fél": "felső fél",
  "legkisebb": "legkisebb",
  "legnagyobb": "legnagyobb",
  "Q1 felirat": "alsó kvartilis",
  "Q3 felirat": "felső kvartilis",
  "középső fele": "az adatok középső fele",
  "alaphelyzet 6": "Eredeti adatok",
  "szavazás cím": "Ki nyeri a szavazást?",
  "jelölt A": "A jelölt",
  "jelölt B": "B jelölt",
  "tengely csúszka": "a tengely kezdete (%)",
  "látszik": "látszólag ennyiszer magasabb:",
  "valójában": "valójában ennyiszer több:",
  "levágva": "levágott tengely!",
  "becsületes": "a tengely 0-tól indul",
  "fagyi cím": "Fagylalt és leégés – 20 nyári nap",
  "fagyi tengely": "eladott gombóc",
  "leégés tengely": "leégés miatt orvosnál",
  "háttér gomb": "Mi van a háttérben?",
  "sáv csúszka": "csak ezek a napok",
  "mind": "minden nap",
  "hőség": "meleg, napos idő",
  "fagyi ok": "több fagyi",
  "leégés ok": "több leégés",
  "okoz": "okozza?",
  "hőmérséklet jelmagyarázat": "hűvösebb → melegebb nap",
  "nincs összefüggés": "itt nincs összefüggés",
  "össz középérték": "középérték: hol a közép?",
  "össz szóródás": "szóródás: mennyire szórt?",
  "össz tengely": "tengely 0-tól",
  "össz korreláció": "korreláció ≠ ok-okozat"
 },
 "data": {
  "bérek": {
   "t": "list",
   "v": [
    400.0,
    420.0,
    450.0,
    450.0,
    480.0,
    500.0,
    520.0,
    550.0,
    600.0
   ],
   "u": "",
   "d": 0,
   "s": "400; 420; 450; 450; 480; 500; 520; 550; 600"
  },
  "bérek átlaga": {
   "v": 485.6,
   "u": "",
   "d": 1
  },
  "bérek mediánja": {
   "v": 480.0,
   "u": "",
   "d": 0
  },
  "eltérések összege": {
   "v": 227.8,
   "u": "",
   "d": 1
  },
  "tulajdonos bére": {
   "v": 6000.0,
   "u": "",
   "d": 0
  },
  "új átlag": {
   "v": 1037.0,
   "u": "",
   "d": 0
  },
  "új medián": {
   "v": 490.0,
   "u": "",
   "d": 0
  },
  "ksh hónap": {
   "t": "date",
   "v": 2024,
   "ymd": [
    2024,
    10,
    null
   ],
   "a": 2024.791,
   "s": "2024. október"
  },
  "ksh átlag": {
   "v": 637200.0,
   "u": "Ft",
   "d": 0,
   "yr": 2024,
   "upd": true,
   "s": "637 200 Ft"
  },
  "ksh medián": {
   "v": 529000.0,
   "u": "Ft",
   "d": 0,
   "yr": 2024,
   "upd": true,
   "s": "529 000 Ft"
  },
  "jegyek": {
   "t": "list",
   "v": [
    2.0,
    3.0,
    5.0,
    5.0,
    5.0
   ],
   "u": "",
   "d": 0,
   "s": "2; 3; 5; 5; 5"
  },
  "jegyek átlaga": {
   "v": 4.0,
   "u": "",
   "d": 0
  },
  "jegyek mediánja": {
   "v": 5.0,
   "u": "",
   "d": 0
  },
  "Andi pontjai": {
   "t": "list",
   "v": [
    14.0,
    15.0,
    16.0,
    16.0,
    17.0,
    18.0
   ],
   "u": "",
   "d": 0,
   "s": "14; 15; 16; 16; 17; 18"
  },
  "Bori pontjai": {
   "t": "list",
   "v": [
    9.0,
    11.0,
    16.0,
    16.0,
    21.0,
    23.0
   ],
   "u": "",
   "d": 0,
   "s": "9; 11; 16; 16; 21; 23"
  },
  "pontátlag": {
   "v": 16.0,
   "u": "",
   "d": 0
  },
  "Andi terjedelme": {
   "v": 4.0,
   "u": "",
   "d": 0
  },
  "Bori terjedelme": {
   "v": 14.0,
   "u": "",
   "d": 0
  },
  "Andi szórása": {
   "v": 1.29,
   "u": "",
   "d": 2
  },
  "Bori szórása": {
   "v": 4.97,
   "u": "",
   "d": 2
  },
  "képernyőidő": {
   "t": "list",
   "v": [
    40.0,
    50.0,
    70.0,
    90.0,
    100.0,
    110.0,
    120.0,
    140.0,
    160.0,
    190.0,
    240.0
   ],
   "u": "",
   "d": 0,
   "s": "40; 50; 70; 90; 100; 110; 120; 140; 160; 190; 240"
  },
  "alsó kvartilis": {
   "v": 70.0,
   "u": "",
   "d": 0
  },
  "képernyő medián": {
   "v": 110.0,
   "u": "",
   "d": 0
  },
  "felső kvartilis": {
   "v": 160.0,
   "u": "",
   "d": 0
  },
  "szavazat A": {
   "v": 52.0,
   "u": "%",
   "d": 0
  },
  "szavazat B": {
   "v": 48.0,
   "u": "%",
   "d": 0
  },
  "tengely kezdete": {
   "v": 45.0,
   "u": "%",
   "d": 0
  },
  "látszólagos arány": {
   "v": 2.33,
   "u": "",
   "d": 2
  },
  "napi hőmérséklet": {
   "t": "list",
   "v": [
    19.0,
    19.0,
    20.0,
    20.0,
    21.0,
    23.0,
    24.0,
    23.0,
    25.0,
    24.0,
    27.0,
    27.0,
    28.0,
    28.0,
    29.0,
    33.0,
    32.0,
    32.0,
    31.0,
    31.0
   ],
   "u": "°C",
   "d": 0,
   "s": "19; 19; 20; 20; 21; 23; 24; 23; 25; 24; 27; 27; 28; 28; 29; 33; 32; 32; 31; 31 °C"
  },
  "fagyi eladás": {
   "t": "list",
   "v": [
    51.0,
    38.0,
    68.0,
    80.0,
    63.0,
    116.0,
    123.0,
    93.0,
    106.0,
    87.0,
    148.0,
    129.0,
    170.0,
    159.0,
    144.0,
    184.0,
    197.0,
    178.0,
    202.0,
    214.0
   ],
   "u": "",
   "d": 0,
   "s": "51; 38; 68; 80; 63; 116; 123; 93; 106; 87; 148; 129; 170; 159; 144; 184; 197; 178; 202; 214"
  },
  "leégés": {
   "t": "list",
   "v": [
    4.0,
    2.0,
    1.0,
    3.0,
    5.0,
    4.0,
    8.0,
    7.0,
    5.0,
    6.0,
    6.0,
    9.0,
    10.0,
    8.0,
    12.0,
    15.0,
    10.0,
    10.0,
    13.0,
    12.0
   ],
   "u": "",
   "d": 0,
   "s": "4; 2; 1; 3; 5; 4; 8; 7; 5; 6; 6; 9; 10; 8; 12; 15; 10; 10; 13; 12"
  }
 },
 "src": {
  "bérek": 43,
  "bérek átlaga": 44,
  "bérek mediánja": 45,
  "eltérések összege": 46,
  "tulajdonos bére": 68,
  "új átlag": 69,
  "új medián": 70,
  "ksh hónap": 88,
  "ksh átlag": 89,
  "ksh medián": 90,
  "jegyek": 115,
  "jegyek átlaga": 116,
  "jegyek mediánja": 117,
  "Andi pontjai": 138,
  "Bori pontjai": 139,
  "pontátlag": 140,
  "Andi terjedelme": 141,
  "Bori terjedelme": 142,
  "Andi szórása": 143,
  "Bori szórása": 144,
  "képernyőidő": 167,
  "alsó kvartilis": 168,
  "képernyő medián": 169,
  "felső kvartilis": 170,
  "szavazat A": 194,
  "szavazat B": 195,
  "tengely kezdete": 196,
  "látszólagos arány": 197,
  "napi hőmérséklet": 221,
  "fagyi eladás": 222,
  "leégés": 223,
  "kitalált adat": 19,
  "valós adat": 20,
  "modell bélyeg": 21,
  "kitekintés": 22,
  "átlag": 23,
  "medián": 24,
  "módusz": 25,
  "ezer Ft": 26,
  "bérek cím": 34,
  "bal oldal": 35,
  "jobb oldal": 36,
  "egyensúly": 37,
  "billen": 38,
  "bér tengely": 39,
  "alaphelyzet 1": 40,
  "kérdés 2": 57,
  "tippelj": 58,
  "tipp 2a": 59,
  "tipp 2b": 60,
  "tipp 2c": 61,
  "a tipped": 62,
  "tulajdonos csúszka": 63,
  "tulajdonos": 64,
  "dolgozók az átlag alatt": 65,
  "ksh cím": 80,
  "dolgozók fele": 81,
  "forrás ksh": 82,
  "kereset tengely": 83,
  "gyakoriság tengely": 84,
  "különbség": 85,
  "jegyek cím": 105,
  "jegy tengely": 106,
  "jegy szerint": 107,
  "alaphelyzet 4": 108,
  "mikor medián": 109,
  "mikor átlag": 110,
  "mikor módusz": 111,
  "ökölszabály": 112,
  "játékos A": 128,
  "játékos B": 129,
  "játékos gomb": 130,
  "pont tengely": 131,
  "terjedelem": 132,
  "szórás": 133,
  "átlagos négyzet": 134,
  "alaphelyzet 5": 135,
  "képernyő cím": 155,
  "perc tengely": 156,
  "alsó fél": 157,
  "felső fél": 158,
  "legkisebb": 159,
  "legnagyobb": 160,
  "Q1 felirat": 161,
  "Q3 felirat": 162,
  "középső fele": 163,
  "alaphelyzet 6": 164,
  "szavazás cím": 184,
  "jelölt A": 185,
  "jelölt B": 186,
  "tengely csúszka": 187,
  "látszik": 188,
  "valójában": 189,
  "levágva": 190,
  "becsületes": 191,
  "fagyi cím": 207,
  "fagyi tengely": 208,
  "leégés tengely": 209,
  "háttér gomb": 210,
  "sáv csúszka": 211,
  "mind": 212,
  "hőség": 213,
  "fagyi ok": 214,
  "leégés ok": 215,
  "okoz": 216,
  "hőmérséklet jelmagyarázat": 217,
  "nincs összefüggés": 218,
  "össz középérték": 237,
  "össz szóródás": 238,
  "össz tengely": 239,
  "össz korreláció": 240
 }
};
