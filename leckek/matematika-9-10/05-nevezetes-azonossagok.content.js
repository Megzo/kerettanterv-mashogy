/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 05-nevezetes-azonossagok.md
   Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/05-nevezetes-azonossagok.md */
window.LESSON_CONTENT = {
 "source": "05-nevezetes-azonossagok.md",
 "title": "Miért nem a² + b²? – nevezetes azonosságok négyzetekkel",
 "titleLine": 1,
 "meta": {
  "subject": "Matematika",
  "grade": "9–10.",
  "topic": "6. Betűs kifejezések alkalmazása egyenletmegoldás, függvényábrázolás során"
 },
 "steps": [
  {
   "title": "Mekkora a (3 + 5)²?",
   "html": "<p data-src=\"24\">Tippelj! Sokan rávágják: <span class=\"mx\">(3 + 5)<sup>2</sup> = 3<sup>2</sup> + 5<sup>2</sup> = 34</span>. Pedig <span class=\"mx\">3 + 5 = 8</span>, és <span class=\"mx\">8<sup>2</sup> = 64</span>. Rajzoljuk le! A 8 oldalú négyzetben elfér egy <span class=\"mx\">3<sup>2</sup></span>-es és egy <span class=\"mx\">5<sup>2</sup></span>-es négyzet, de <span class=\"key\">kimarad két <span class=\"mx\">3 · 5</span>-ös téglalap: ez a hiányzó 30.</span> Tehát <span class=\"mx\">(<i>a</i> + <i>b</i>)<sup>2</sup> ≠ <i>a</i><sup>2</sup> + <i>b</i><sup>2</sup></span>.</p><p class=\"note\" data-src=\"26\">Kérdezd meg az osztályt, ki tippelt 34-et!</p>",
   "line": 23,
   "words": 39
  },
  {
   "title": "Négy darab: a², 2ab, b²",
   "html": "<p data-src=\"41\">Az <span class=\"mx\"><i>a</i> + <i>b</i></span> oldalú négyzet négy darabra esik: egy <span class=\"mx\"><i>a</i><sup>2</sup></span>-es és egy <span class=\"mx\"><i>b</i><sup>2</sup></span>-es négyzetre, meg <b>két</b> <span class=\"mx\"><i>a</i> · <i>b</i></span>-s téglalapra. <span class=\"key\"><span class=\"mx\">(<i>a</i> + <i>b</i>)<sup>2</sup> = <i>a</i><sup>2</sup> + 2<i>ab</i> + <i>b</i><sup>2</sup></span>.</span> Húzd a csúszkákat: a darabok és a számok együtt változnak. A <span class=\"mx\">2<i>ab</i></span> a két téglalap – éppen ez hiányzott a tévhitből.</p><p class=\"note\" data-src=\"43\">Ez a rajz csak pozitív <em>a</em>-ra és <em>b</em>-re bizonyít: oldalhossz nem lehet negatív.</p>",
   "line": 40,
   "words": 51
  },
  {
   "title": "Minden számra: szorzás tagonként",
   "html": "<p data-src=\"56\">Negatív számhoz nincs ilyen négyzet. A szorzás viszont <b>tagonként</b> mindig elvégezhető (disztributivitás): minden tagot minden taggal szorzunk. A táblázat négy cellája ugyanaz a négy darab. <span class=\"key\">Így <span class=\"mx\">(<i>a</i> + <i>b</i>)<sup>2</sup> = <i>a</i><sup>2</sup> + 2<i>ab</i> + <i>b</i><sup>2</sup></span> minden valós <em>a</em>, <em>b</em> számra igaz.</span> Próbáld ki negatív számmal is!</p>",
   "line": 55,
   "words": 38
  },
  {
   "title": "(a − b)²: levágunk",
   "html": "<p data-src=\"70\">Az <em>a</em> oldalú négyzetből vágj le egy <em>b</em> széles csíkot jobbról, majd egyet felülről: mindkettő <span class=\"mx\"><i>a</i> · <i>b</i></span>. De a jobb felső <span class=\"mx\"><i>b</i><sup>2</sup></span>-es sarkot <span class=\"key\">kétszer vontuk le, ezért egyszer vissza kell adni</span>: <span class=\"mx\">(<i>a</i> − <i>b</i>)<sup>2</sup> = <i>a</i><sup>2</sup> − 2<i>ab</i> + <i>b</i><sup>2</sup></span>. Tehát <span class=\"mx\">(<i>a</i> − <i>b</i>)<sup>2</sup> ≠ <i>a</i><sup>2</sup> − <i>b</i><sup>2</sup></span>!</p><p class=\"note\" data-src=\"72\">Ha <em>b</em> nagyobb, a rajz tükröződik, de a képlet ugyanaz: <span class=\"mx\">(<i>a</i> − <i>b</i>)<sup>2</sup> = (<i>b</i> − <i>a</i>)<sup>2</sup></span>.</p>",
   "line": 69,
   "words": 44
  },
  {
   "title": "a² − b²: átdarabolás téglalappá",
   "html": "<p data-src=\"90\">Vágd ki az <span class=\"mx\"><i>a</i><sup>2</sup></span>-es négyzet sarkából a <span class=\"mx\"><i>b</i><sup>2</sup></span>-es négyzetet! A maradék L alak felső csíkját fordítsd át a jobb oldalra: <span class=\"key\">egy <span class=\"mx\"><i>a</i> + <i>b</i></span> hosszú, <span class=\"mx\"><i>a</i> − <i>b</i></span> magas téglalap lesz.</span> Tehát <span class=\"mx\"><i>a</i><sup>2</sup> − <i>b</i><sup>2</sup> = (<i>a</i> + <i>b</i>)(<i>a</i> − <i>b</i>)</span>. Jobbról balra olvasva: <b>szorzattá alakítás</b>, <span class=\"mx\"><i>x</i><sup>2</sup> − 9 = (<i>x</i> + 3)(<i>x</i> − 3)</span>.</p>",
   "line": 89,
   "words": 35
  },
  {
   "title": "Fejszámolás azonosságokkal",
   "html": "<p data-src=\"106\"><span class=\"key\">Keress egy kerek számot a közelben!</span> <span class=\"mx\">47<sup>2</sup> = (50 − 3)<sup>2</sup> = 2500 − 300 + 9 = 2209</span>. Ha két szám egy kerek szám körül egyformán messze áll: <span class=\"mx\">49 · 51 = 50<sup>2</sup> − 1<sup>2</sup> = 2499</span>, és <span class=\"mx\">99 · 101 = 9999</span>. Válassz egy példát, vagy húzd a csúszkát!</p><p class=\"note\" data-src=\"108\">Versenyezzen valaki számológéppel!</p>",
   "line": 105,
   "words": 30
  },
  {
   "title": "Gondolj egy számra!",
   "html": "<p data-src=\"126\">Gondolj egy pozitív egészre! Szorozd meg a nála 2-vel nagyobbal, adj hozzá 1-et, vonj belőle négyzetgyököt, és vond ki a gondolt számot. <span class=\"key\">Mindig 1 jön ki.</span> Miért? A csempék megmutatják: <span class=\"mx\"><i>x</i>(<i>x</i> + 2) + 1 = <i>x</i><sup>2</sup> + 2<i>x</i> + 1 = (<i>x</i> + 1)<sup>2</sup></span>, és ennek gyöke <span class=\"mx\"><i>x</i> + 1</span>.</p><p class=\"note\" data-src=\"128\">Egy diák gondoljon számot, a többiek számoljanak vele!</p>",
   "line": 125,
   "words": 43
  },
  {
   "title": "Két páratlan szám négyzete",
   "html": "<p data-src=\"144\">Két szomszédos páratlan szám: <span class=\"mx\">2<i>k</i> − 1</span> és <span class=\"mx\">2<i>k</i> + 1</span>. A négyzetük különbsége a rajzon egy 1 széles keret. <span class=\"key\">A keret mindig 8 egyforma, <em>k</em> hosszú darabra vágható</span>, tehát a különbség osztható 8-cal. Algebrával: <span class=\"mx\">(2<i>k</i> + 1)<sup>2</sup> − (2<i>k</i> − 1)<sup>2</sup> = 4<i>k</i> · 2 = 8<i>k</i></span>. Például <span class=\"mx\">9<sup>2</sup> − 7<sup>2</sup> = 32</span>.</p>",
   "line": 143,
   "words": 34
  },
  {
   "title": "Összefoglaló",
   "html": "<p data-src=\"157\">Három <b>nevezetes azonosság</b>, mindhárom minden valós számra igaz. <span class=\"key\">A négyzetre emelés nem megy tagonként: a <span class=\"mx\">2<i>ab</i></span> mindig ott van.</span> Mire jók?</p><ul><li data-src=\"159\">fejszámolás: <span class=\"mx\">47<sup>2</sup></span>, <span class=\"mx\">49 · 51</span></li><li data-src=\"160\">szorzattá alakítás: <span class=\"mx\"><i>x</i><sup>2</sup> − 9 = (<i>x</i> + 3)(<i>x</i> − 3)</span></li><li data-src=\"161\">oszthatóság: <span class=\"mx\">(2<i>k</i> + 1)<sup>2</sup> − (2<i>k</i> − 1)<sup>2</sup> = 8<i>k</i></span></li></ul><p class=\"note\" data-src=\"163\">A másodfokú egyenleteknél a teljes négyzetté kiegészítés is ezekre épül.</p>",
   "line": 156,
   "words": 39
  }
 ],
 "labels": {
  "bizonyítás": "bizonyítás",
  "vázlat": "vázlat",
  "pozitív bélyeg": "területtel: csak pozitív a, b",
  "tippelj": "Tippelj!",
  "sokan így": "Sokan így számolnak:",
  "valójában": "Valójában:",
  "a hiány": "A különbség:",
  "két téglalap": "a két téglalap",
  "hiányzik": "kimaradt!",
  "a csúszka": "a (az egyik oldal)",
  "b csúszka": "b (a másik oldal)",
  "tévhit 2": "a tévhitből hiányzik:",
  "együtt": "összesen:",
  "a csúszka 3": "a (negatív is lehet)",
  "b csúszka 3": "b (negatív is lehet)",
  "példa cím 3": "Próba számokkal:",
  "tévhit 3": "a tévhit:",
  "tagonként": "minden tagot minden taggal",
  "a csúszka 4": "a",
  "b csúszka 4": "b (amennyit levágunk)",
  "jobb csík": "jobb oldali csík",
  "felső csík": "felső csík (sarokkal)",
  "kétszer": "kétszer levonva!",
  "visszaadjuk": "visszaadjuk",
  "tükör": "b nagyobb: tükrözött ábra",
  "tévhit 4": "tévhit:",
  "marad": "ez marad:",
  "a csúszka 5": "a",
  "b csúszka 5": "b (a kivágott négyzet oldala)",
  "kivágjuk": "kivágjuk",
  "átfordítjuk": "átfordítjuk",
  "szorzattá": "jobbról balra: szorzattá alakítás",
  "példa 5": "Számokkal:",
  "saját szám": "a te számod (négyzetre emeljük)",
  "kerek": "kerek szám a közelben:",
  "négyzet bal": "Négyzetre emelés",
  "szorzat bal": "Szorzat, kerek szám körül",
  "gondolt csúszka": "a gondolt szám",
  "újra 7": "Még egyszer!",
  "utasítás 1": "Gondolj egy számra!",
  "utasítás 2": "Szorozd a nála 2-vel nagyobbal!",
  "utasítás 3": "Adj hozzá 1-et!",
  "utasítás 4": "Vonj négyzetgyököt!",
  "utasítás 5": "Vond ki a gondolt számot!",
  "négyzet lett": "négyzet lett!",
  "k csúszka": "k (a nagyobb szám: 2k + 1)",
  "keret": "a keret",
  "nyolc sor": "8 sor, mindegyikben k cella",
  "algebrával": "Algebrával, minden k-ra:",
  "össz 1": "összeg négyzete",
  "össz 2": "különbség négyzete",
  "össz 3": "két négyzet különbsége",
  "össz 4": "Vigyázz!"
 },
 "data": {
  "első a": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "első b": {
   "v": 5.0,
   "u": "",
   "d": 0
  },
  "kezdő a": {
   "v": 5.0,
   "u": "",
   "d": 0
  },
  "kezdő b": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "példa a": {
   "v": 7.0,
   "u": "",
   "d": 0
  },
  "példa b": {
   "v": -3.0,
   "u": "",
   "d": 0
  },
  "levágás a": {
   "v": 6.0,
   "u": "",
   "d": 0
  },
  "levágás b": {
   "v": 2.0,
   "u": "",
   "d": 0
  },
  "különbség a": {
   "v": 7.0,
   "u": "",
   "d": 0
  },
  "különbség b": {
   "v": 3.0,
   "u": "",
   "d": 0
  },
  "szorzattá példa": {
   "v": 9.0,
   "u": "",
   "d": 0
  },
  "négyzet 1": {
   "v": 47.0,
   "u": "",
   "d": 0
  },
  "négyzet 2": {
   "v": 103.0,
   "u": "",
   "d": 0
  },
  "szorzat 1": {
   "t": "list",
   "v": [
    49.0,
    51.0
   ],
   "u": "",
   "d": 0,
   "s": "49; 51"
  },
  "szorzat 2": {
   "t": "list",
   "v": [
    99.0,
    101.0
   ],
   "u": "",
   "d": 0,
   "s": "99; 101"
  },
  "négyzet 1 értéke": {
   "v": 2209.0,
   "u": "",
   "d": 0
  },
  "szorzat 1 értéke": {
   "v": 2499.0,
   "u": "",
   "d": 0
  },
  "szorzat 2 értéke": {
   "v": 9999.0,
   "u": "",
   "d": 0
  },
  "gondolt szám": {
   "v": 7.0,
   "u": "",
   "d": 0
  },
  "páratlan példa": {
   "v": 9.0,
   "u": "",
   "d": 0
  },
  "páratlan különbség": {
   "v": 32.0,
   "u": "",
   "d": 0
  }
 },
 "src": {
  "első a": 37,
  "első b": 38,
  "kezdő a": 52,
  "kezdő b": 53,
  "példa a": 66,
  "példa b": 67,
  "levágás a": 86,
  "levágás b": 87,
  "különbség a": 101,
  "különbség b": 102,
  "szorzattá példa": 103,
  "négyzet 1": 117,
  "négyzet 2": 118,
  "szorzat 1": 119,
  "szorzat 2": 120,
  "négyzet 1 értéke": 121,
  "szorzat 1 értéke": 122,
  "szorzat 2 értéke": 123,
  "gondolt szám": 141,
  "páratlan példa": 153,
  "páratlan különbség": 154,
  "bizonyítás": 19,
  "vázlat": 20,
  "pozitív bélyeg": 21,
  "tippelj": 29,
  "sokan így": 30,
  "valójában": 31,
  "a hiány": 32,
  "két téglalap": 33,
  "hiányzik": 34,
  "a csúszka": 46,
  "b csúszka": 47,
  "tévhit 2": 48,
  "együtt": 49,
  "a csúszka 3": 59,
  "b csúszka 3": 60,
  "példa cím 3": 61,
  "tévhit 3": 62,
  "tagonként": 63,
  "a csúszka 4": 75,
  "b csúszka 4": 76,
  "jobb csík": 77,
  "felső csík": 78,
  "kétszer": 79,
  "visszaadjuk": 80,
  "tükör": 81,
  "tévhit 4": 82,
  "marad": 83,
  "a csúszka 5": 93,
  "b csúszka 5": 94,
  "kivágjuk": 95,
  "átfordítjuk": 96,
  "szorzattá": 97,
  "példa 5": 98,
  "saját szám": 111,
  "kerek": 112,
  "négyzet bal": 113,
  "szorzat bal": 114,
  "gondolt csúszka": 131,
  "újra 7": 132,
  "utasítás 1": 133,
  "utasítás 2": 134,
  "utasítás 3": 135,
  "utasítás 4": 136,
  "utasítás 5": 137,
  "négyzet lett": 138,
  "k csúszka": 147,
  "keret": 148,
  "nyolc sor": 149,
  "algebrával": 150,
  "össz 1": 166,
  "össz 2": 167,
  "össz 3": 168,
  "össz 4": 169
 }
};
