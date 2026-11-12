/* GENERÁLT FÁJL — ne szerkeszd kézzel. Forrás: 09-aram-otthon.md
   Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/09-aram-otthon.md */
window.LESSON_CONTENT = {
 "source": "09-aram-otthon.md",
 "title": "Miért old le a biztosíték? – Joule-hő, teljesítmény, fogyasztás",
 "titleLine": 1,
 "meta": {
  "subject": "Fizika",
  "grade": "7–8.",
  "topic": "6. Elektromosság a háztartásban (+ 2. Az energia)"
 },
 "steps": [
  {
   "title": "A fűtőszál melegszik",
   "html": "<p data-src=\"73\">Az áram nem fogy el, de <b>energiát</b> ad át (08. lecke). Hol?</p><p data-src=\"75\">A vezetékben és a fűtőszálban ugyanakkora az áram. A vékony fűtőszálban az elektronok újra meg újra meglökik az atomtörzseket, azok erősebben rezegnek: <span class=\"key\">ahol nagy az ellenállás, ott keletkezik a hő</span>. Ez a <b>Joule-hő</b>.</p><p class=\"note\" data-src=\"77\">Ezen működik a vasaló, a hajszárító és a vízmelegítő is.</p>",
   "line": 72,
   "words": 55
  },
  {
   "title": "Teljesítmény: P = U · I",
   "html": "<p data-src=\"99\">Minden konnektorban <b>230 V</b> van. Mégis: a vízforraló több mint kétszázszor akkora áramot vesz fel, mint a LED-lámpa.</p><p data-src=\"101\">A <b>teljesítmény</b>: mennyi energiát alakít át a készülék másodpercenként. Mértékegysége a watt (1 W = 1 J/s).</p><p class=\"note\" data-src=\"103\">Tévhit: „csak a feszültség számít”. A feszültség ugyanaz – <span class=\"key\">az áram dönti el</span> a teljesítményt.</p>",
   "line": 98,
   "words": 48
  },
  {
   "title": "kWh és forint",
   "html": "<p data-src=\"110\"><b>Energia = teljesítmény × idő.</b> Otthon kilowattórában (kWh) mérjük, ezt fizetjük ki.</p><p data-src=\"112\">Tévhit: a nagyobb teljesítményű készülék mindig többet fogyaszt. <span class=\"key\">Az idő is számít!</span> A tévé 1 óra alatt ugyanannyi energiát használ, mint a vízforraló 3 perc alatt.</p><p class=\"big-fx\" data-src=\"114\">E = P · t</p><p class=\"note\" data-src=\"116\">Húzd a tévé idejét! Hány perc tévézés ér fel két forralással?</p>",
   "line": 109,
   "words": 51
  },
  {
   "title": "Izzó, LED, készenlét",
   "html": "<p data-src=\"132\">A hagyományos izzó Joule-hővel világít: a szála izzásig forrósodik. Az energia nagy része <b>hő</b> lesz, nem fény. A LED ugyanannyi fényt 9 W teljesítménnyel ad.</p><p data-src=\"134\">Tévhit: készenlétben a tévé nem fogyaszt. <span class=\"key\">A piros lámpa egész évben, éjjel-nappal fogyaszt!</span></p><p class=\"note\" data-src=\"136\">Állítsd be, hány órát világít naponta a lámpa! Melyik éri meg?</p>",
   "line": 131,
   "words": 48
  },
  {
   "title": "Túlterhelés",
   "html": "<p data-src=\"155\">A konnektorok <b>párhuzamosan</b> vannak kötve: mindegyik 230 V-ot kap. A közös vezetékben <span class=\"key\">az áramok összeadódnak</span>.</p><p data-src=\"157\">Nagyobb áram → melegebb vezeték. Ha az áram 16 A fölé nő, a <b>kismegszakító</b> lekapcsol, mielőtt a vezeték túlmelegedne.</p><p class=\"note\" data-src=\"159\">A valódi kismegszakító kis túllépésnél csak percek múlva old le.</p>",
   "line": 154,
   "words": 42
  },
  {
   "title": "Rövidzár",
   "html": "<p data-src=\"170\">Ha megsérül a szigetelés, a két ér összeérhet. Az áram ekkor <b>megkerüli</b> a lámpát: szinte nincs ellenállás, ezért I = U / R <span class=\"key\">óriási</span>.</p><p data-src=\"172\">A kismegszakító ezt 10 ms alatt lekapcsolja. Nélküle a vezeték pillanatok alatt felforrósodna, és meggyulladhatna a szigetelés.</p><p class=\"note\" data-src=\"174\">Az időtengely lassított: minden osztás tízszer annyi idő.</p>",
   "line": 169,
   "words": 46
  },
  {
   "title": "Földelés és FI-relé",
   "html": "<p data-src=\"195\">Hibás mosógép: a fázis hozzáér a fémházhoz. Ha megérinted, rajtad át folyik áram a földbe.</p><p data-src=\"197\">Tévhit: a biztosíték az embert védi. Ez az áram <span class=\"key\">a kismegszakítónak túl kicsi</span>. Véd a <b>földelés</b>: a hibaáram a védővezetéken folyik el, leold a kismegszakító. És a <b>FI-relé</b>: lekapcsol, ha 30 mA-nél több nem jön vissza.</p><p class=\"note\" data-src=\"199\">Próbáld ki a négy esetet!</p>",
   "line": 194,
   "words": 55
  },
  {
   "title": "Áramütés",
   "html": "<p data-src=\"229\">Nem a feszültség „üt”, hanem a testen átfolyó <b>áram</b>. Ezt a feszültség hajtja át: I = U / R. Minél tovább tart, annál veszélyesebb.</p><p data-src=\"231\">1 mA érezhető, 10 mA felett nem tudod elengedni, 50 mA felett leállhat a szív. <span class=\"key\">A 230 V életveszélyes!</span></p><p class=\"note\" data-src=\"233\">Soha ne kísérletezz konnektorral, sérült kábellel! A laposelem (4,5 V) csak kis áramot hajt át rajtad.</p>",
   "line": 228,
   "words": 55
  },
  {
   "title": "Összefoglalás",
   "html": "<ul><li data-src=\"252\"><b>Joule-hő</b>: az áram melegíti a vezetőt, leginkább ott, ahol nagy az ellenállás.</li><li data-src=\"253\">Teljesítmény: <b>P = U · I</b>. Energia: <b>E = P · t</b> – ebből lesz a számla.</li><li data-src=\"254\">A kismegszakító <span class=\"key\">a vezetéket védi</span> túlterhelés és rövidzár ellen.</li><li data-src=\"255\">Az embert a <b>földelés</b> és a <b>FI-relé</b> védi.</li></ul><p class=\"note\" data-src=\"257\">Mennyibe kerül egy évig naponta háromszor forralni a 2000 W-os vízforralóval?</p>",
   "line": 251,
   "words": 51
  }
 ],
 "labels": {
  "konnektor": "konnektor",
  "vízforraló": "vízforraló",
  "hajszárító": "hajszárító",
  "mikró": "mikró",
  "tévé": "tévé",
  "lámpa": "LED-lámpa",
  "áramerősség": "áramerősség",
  "feszültség": "feszültség",
  "teljesítmény": "teljesítmény",
  "ellenállás": "ellenállás",
  "lassítva": "lassítva: valójában 50 lengés másodpercenként",
  "kismegszakító": "kismegszakító",
  "FI-relé": "FI-relé",
  "leoldott": "LEOLDOTT",
  "bekapcsolva": "bekapcsolva",
  "áramár": "áramár",
  "be-ki gomb": "Bekapcsol / kikapcsol",
  "tápvezeték": "tápvezeték",
  "fűtőszál": "fűtőszál",
  "vezeték": "vezeték",
  "áram mindkettőben": "áram mindkettőben",
  "hő 1 s alatt": "hő 1 s alatt",
  "nagyítás": "nagyítás: a fűtőszál belseje",
  "meglökik": "elektronok lökik az atomtörzseket",
  "melegítés ideje": "melegítés ideje:",
  "felgyorsítva": "felgyorsítva 40×",
  "forr": "forr!",
  "fogyasztásmérő": "fogyasztásmérő",
  "áram 230 V-on": "Mekkora áramot vesz fel 230 V-on?",
  "tengely P": "teljesítmény (W)",
  "tengely t": "idő (perc)",
  "húzd": "húzd!",
  "ugyanannyi energia": "ugyanannyi energia!",
  "egy cella": "egy cella = 0,01 kWh",
  "kWh jelentése": "1 kWh = 1000 W · 1 óra",
  "tévé csúszka": "A tévézés ideje",
  "izzó": "hagyományos izzó",
  "ugyanannyi fény": "ugyanannyi fény",
  "főleg hő": "főleg hő",
  "kevés hő": "kevés hő",
  "készenlét": "tévé készenlétben",
  "éjjel-nappal": "éjjel-nappal, egész évben",
  "egy év alatt": "Egy év alatt",
  "napi csúszka": "Napi világítás",
  "naponta": "óra/nap · 365 nap",
  "konyha": "konyha",
  "fürdő": "fürdő",
  "nappali": "nappali",
  "közös vezetékben": "a közös vezetékben",
  "visszakapcsol gomb": "Visszakapcsolás",
  "túlterhelés": "Túlterhelés",
  "rövidzár gomb": "Rövidzár!",
  "javítás gomb": "Javítás és visszakapcsolás",
  "nélküle gomb": "Kismegszakító nélkül?",
  "sérült szigetelés": "sérült szigetelés",
  "rövidzár": "Rövidzár!",
  "vezeték hőmérséklete": "a vezeték hőmérséklete",
  "zárlat óta": "a zárlat óta eltelt idő (lassítva)",
  "alig melegedett": "Leoldott – a vezeték alig melegedett",
  "tűzveszély": "Ég a szigetelés – tűzveszély!",
  "kismegszakító nélkül": "kismegszakító nélkül",
  "állólámpa": "állólámpa",
  "földelés gomb": "Földelés be / ki",
  "FI gomb": "FI-relé be / ki",
  "mosógép": "mosógép (fémház)",
  "zárlat a házra": "zárlat a házra!",
  "a ház": "a ház",
  "védővezeték": "védővezeték",
  "nincs bekötve": "nincs bekötve",
  "fázis": "fázis",
  "nulla": "nulla",
  "kimenő áram": "kimenő áram (fázis)",
  "visszajövő áram": "visszajövő áram (nulla)",
  "különbség": "különbség",
  "nincs FI": "nincs FI-relé",
  "földelő": "földelés",
  "működik": "A gép rendben működik.",
  "életveszély": "ÉLETVESZÉLY: áram a testen át!",
  "nem old le": "A kismegszakító nem old le",
  "FI leold": "A FI-relé lekapcsolt",
  "biztonságos": "Leoldott – a ház nem veszélyes",
  "a föld visszavezeti": "a föld visszavezeti az áramot",
  "feszültség csúszka": "Érintési feszültség",
  "konnektor gomb": "Konnektor: 230 V",
  "nem érzed": "nem érzed",
  "érezhető": "érezhető, bizsergés",
  "nem tudod elengedni": "görcs: nem tudod elengedni",
  "fibrilláció": "szívkamra-fibrilláció",
  "FI-relé határa": "a FI-relé leold",
  "legrosszabb eset": "test: nedves bőr, legrosszabb eset",
  "a testen át": "a testen át",
  "összegzés Joule": "Joule-hő",
  "összegzés Joule 2": "ott keletkezik, ahol nagy az ellenállás",
  "összegzés P": "teljesítmény (W) = feszültség × áram",
  "összegzés E": "energia (kWh) = teljesítmény × idő",
  "összegzés védelem 1": "kismegszakító: a vezetéket védi",
  "összegzés védelem 2": "földelés + FI-relé: az embert védi",
  "tanulság": "Az áram hőt termel és pénzbe kerül – a 230 V pedig életveszélyes."
 },
 "data": {
  "hálózati feszültség": {
   "v": 230.0,
   "u": "V",
   "d": 0
  },
  "vízforraló teljesítménye": {
   "v": 2000.0,
   "u": "W",
   "d": 0
  },
  "hajszárító teljesítménye": {
   "v": 1800.0,
   "u": "W",
   "d": 0
  },
  "mikró teljesítménye": {
   "v": 1200.0,
   "u": "W",
   "d": 0
  },
  "tévé teljesítménye": {
   "v": 100.0,
   "u": "W",
   "d": 0
  },
  "LED-lámpa teljesítménye": {
   "v": 9.0,
   "u": "W",
   "d": 0
  },
  "kismegszakító névleges árama": {
   "v": 16.0,
   "u": "A",
   "d": 0
  },
  "áram ára": {
   "v": 36.0,
   "u": "Ft/kWh",
   "d": 0
  },
  "az emberi test ellenállása": {
   "v": 1000.0,
   "u": "Ω",
   "d": 0
  },
  "vezetékhurok ellenállása": {
   "v": 0.5,
   "u": "Ω",
   "d": 1
  },
  "tápvezeték ellenállása": {
   "v": 0.07,
   "u": "Ω",
   "d": 2
  },
  "víz tömege": {
   "v": 1.0,
   "u": "kg",
   "d": 1
  },
  "víz fajhője": {
   "v": 4200.0,
   "u": "J/(kg·°C)",
   "d": 0
  },
  "kezdeti vízhőmérséklet": {
   "v": 20.0,
   "u": "°C",
   "d": 0
  },
  "vízforralás ideje": {
   "v": 3.0,
   "u": "perc",
   "d": 0
  },
  "tévézés ideje": {
   "v": 60.0,
   "u": "perc",
   "d": 0
  },
  "izzólámpa teljesítménye": {
   "v": 60.0,
   "u": "W",
   "d": 0
  },
  "napi világítás": {
   "v": 3.0,
   "u": "óra",
   "d": 0
  },
  "készenléti teljesítmény": {
   "v": 1.0,
   "u": "W",
   "d": 1
  },
  "kioldási idő rövidzárnál": {
   "v": 10.0,
   "u": "ms",
   "d": 0
  },
  "a vezeték melegedése 100 A-nél": {
   "v": 22.0,
   "u": "°C/s",
   "d": 0
  },
  "a szigetelés tűréshatára": {
   "v": 160.0,
   "u": "°C",
   "d": 0
  },
  "mosógép teljesítménye": {
   "v": 2000.0,
   "u": "W",
   "d": 0
  },
  "FI-relé érzékenysége": {
   "v": 30.0,
   "u": "mA",
   "d": 0
  },
  "FI-relé kioldási ideje": {
   "v": 40.0,
   "u": "ms",
   "d": 0
  },
  "érezhető áram": {
   "v": 1.0,
   "u": "mA",
   "d": 0
  },
  "elengedési határ": {
   "v": 10.0,
   "u": "mA",
   "d": 0
  },
  "fibrillációs áram": {
   "v": 50.0,
   "u": "mA",
   "d": 0
  }
 },
 "src": {
  "hálózati feszültség": 61,
  "vízforraló teljesítménye": 62,
  "hajszárító teljesítménye": 63,
  "mikró teljesítménye": 64,
  "tévé teljesítménye": 65,
  "LED-lámpa teljesítménye": 66,
  "kismegszakító névleges árama": 67,
  "áram ára": 68,
  "az emberi test ellenállása": 69,
  "vezetékhurok ellenállása": 70,
  "tápvezeték ellenállása": 93,
  "víz tömege": 94,
  "víz fajhője": 95,
  "kezdeti vízhőmérséklet": 96,
  "vízforralás ideje": 128,
  "tévézés ideje": 129,
  "izzólámpa teljesítménye": 150,
  "napi világítás": 151,
  "készenléti teljesítmény": 152,
  "kioldási idő rövidzárnál": 190,
  "a vezeték melegedése 100 A-nél": 191,
  "a szigetelés tűréshatára": 192,
  "mosógép teljesítménye": 224,
  "FI-relé érzékenysége": 225,
  "FI-relé kioldási ideje": 226,
  "érezhető áram": 247,
  "elengedési határ": 248,
  "fibrillációs áram": 249,
  "konnektor": 43,
  "vízforraló": 44,
  "hajszárító": 45,
  "mikró": 46,
  "tévé": 47,
  "lámpa": 48,
  "áramerősség": 49,
  "feszültség": 50,
  "teljesítmény": 51,
  "ellenállás": 52,
  "lassítva": 53,
  "kismegszakító": 54,
  "FI-relé": 55,
  "leoldott": 56,
  "bekapcsolva": 57,
  "áramár": 58,
  "be-ki gomb": 80,
  "tápvezeték": 81,
  "fűtőszál": 82,
  "vezeték": 83,
  "áram mindkettőben": 84,
  "hő 1 s alatt": 85,
  "nagyítás": 86,
  "meglökik": 87,
  "melegítés ideje": 88,
  "felgyorsítva": 89,
  "forr": 90,
  "fogyasztásmérő": 106,
  "áram 230 V-on": 107,
  "tengely P": 119,
  "tengely t": 120,
  "húzd": 121,
  "ugyanannyi energia": 122,
  "egy cella": 123,
  "kWh jelentése": 124,
  "tévé csúszka": 125,
  "izzó": 139,
  "ugyanannyi fény": 140,
  "főleg hő": 141,
  "kevés hő": 142,
  "készenlét": 143,
  "éjjel-nappal": 144,
  "egy év alatt": 145,
  "napi csúszka": 146,
  "naponta": 147,
  "konyha": 162,
  "fürdő": 163,
  "nappali": 164,
  "közös vezetékben": 165,
  "visszakapcsol gomb": 166,
  "túlterhelés": 167,
  "rövidzár gomb": 177,
  "javítás gomb": 178,
  "nélküle gomb": 179,
  "sérült szigetelés": 180,
  "rövidzár": 181,
  "vezeték hőmérséklete": 182,
  "zárlat óta": 183,
  "alig melegedett": 184,
  "tűzveszély": 185,
  "kismegszakító nélkül": 186,
  "állólámpa": 187,
  "földelés gomb": 202,
  "FI gomb": 203,
  "mosógép": 204,
  "zárlat a házra": 205,
  "a ház": 206,
  "védővezeték": 207,
  "nincs bekötve": 208,
  "fázis": 209,
  "nulla": 210,
  "kimenő áram": 211,
  "visszajövő áram": 212,
  "különbség": 213,
  "nincs FI": 214,
  "földelő": 215,
  "működik": 216,
  "életveszély": 217,
  "nem old le": 218,
  "FI leold": 219,
  "biztonságos": 220,
  "a föld visszavezeti": 221,
  "feszültség csúszka": 236,
  "konnektor gomb": 237,
  "nem érzed": 238,
  "érezhető": 239,
  "nem tudod elengedni": 240,
  "fibrilláció": 241,
  "FI-relé határa": 242,
  "legrosszabb eset": 243,
  "a testen át": 244,
  "összegzés Joule": 260,
  "összegzés Joule 2": 261,
  "összegzés P": 262,
  "összegzés E": 263,
  "összegzés védelem 1": 264,
  "összegzés védelem 2": 265,
  "tanulság": 266
 }
};
