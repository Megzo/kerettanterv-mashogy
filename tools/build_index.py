#!/usr/bin/env python3
"""Nyitóoldal (index.html a repó gyökerében) generálása.

Források:
  kerettanterv/temakorok.json        – a kerettanterv témakörei (tantárgy, sáv, óraszám)
  leckek/<mappa>/NN-slug.md          – kész leckék (1. sor: cím, 2. sor: tantárgy/évfolyam/témakör)
  pilot/<mappa>/terv.md              – tervezett leckék („## 2. A leckék” táblázat)

Ami a tervben szerepel, de még nincs .html-je, az „hamarosan” (szürke).
A kimenet egyetlen, önálló HTML-fájl (az adatok beágyazva), így file://-ról és
GitHub Pages-ről is működik.

    python3 tools/build_index.py
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/Megzo/kerettanterv-mashogy/blob/main/"

# A „fő tárgyak” 5–12. évfolyamra, megjelenítési sorrendben.
SUBJECTS = [
    ("Matematika", "matematika"),
    ("Magyar nyelv és irodalom", "magyar"),
    ("Történelem", "tortenelem"),
    ("Természettudomány", "termtud"),
    ("Fizika", "fizika"),
    ("Kémia", "kemia"),
    ("Biológia", "biologia"),
    ("Földrajz", "foldrajz"),
    ("Digitális kultúra", "digkult"),
]
# Évfolyam-oszlopok: (felirat, iskolatípus, a kerettanterv sávjai, amelyek ide tartoznak)
GRADES = [
    ("5–6", "általános iskola", {"5–6"}),
    ("7–8", "általános iskola", {"7–8"}),
    ("9–10", "gimnázium (4 évfolyamos)", {"9–10"}),
    ("11–12", "gimnázium (4 évfolyamos)", {"11–12", "11", "12"}),
]


def topics():
    rows = json.loads((ROOT / "kerettanterv/temakorok.json").read_text(encoding="utf-8"))
    out = {}
    for name, key in SUBJECTS:
        for g, school, bands in GRADES:
            ts = [r for r in rows if r["tantargy"] == name and r["iskolatipus"] == school
                  and r["sav"] in bands]
            if not ts:
                continue
            out[f"{key}/{g}"] = {
                "fajl": ts[0]["fajl"],
                "temakorok": [{
                    "n": r["sorszam"], "cim": r["temakor"], "ora": r["javasolt_oraszam"],
                    "modul": r["modul"], "sav": r["sav"], "leckek": [],
                } for r in ts],
            }
    return out


HEAD_RE = re.compile(r"tantárgy:\s*(.+?)\s*·\s*évfolyam:\s*([\d–-]+)\.?\s*·\s*témakör:\s*(\d+)")


def lessons():
    """Kész leckék a .md fejlécéből + tervezettek a terv.md-ből."""
    found = {}
    for md in sorted((ROOT / "leckek").glob("*/[0-9][0-9]-*.md")):
        lines = md.read_text(encoding="utf-8").splitlines()
        m = HEAD_RE.search(lines[1] if len(lines) > 1 else "")
        if not m:
            raise SystemExit(f"{md}: a 2. sor nem „tantárgy: … · évfolyam: … · témakör: N. …”")
        page = md.with_suffix(".html")
        found[(md.parent.name, md.stem)] = {
            "tantargy": m.group(1), "evfolyam": m.group(2).replace("-", "–"),
            "temakor": int(m.group(3)), "cim": lines[0].lstrip("# ").strip(),
            "lepes": sum(1 for l in lines if re.match(r"## \d+\.", l)),
            "url": page.relative_to(ROOT).as_posix() if page.exists() else None,
            "md": REPO + md.relative_to(ROOT).as_posix(),
        }
    planned = []
    for terv in sorted((ROOT / "pilot").glob("*/terv.md")):
        folder = terv.parent.name
        text = terv.read_text(encoding="utf-8")
        sect = text.split("## 2. A leckék", 1)[-1].split("\n## ", 1)[0]
        known = [v for (f, _), v in found.items() if f == folder]
        if not known:
            continue
        for row in re.finditer(r"^\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*(\d+)", sect, re.M):
            slug, cim, tk = row.groups()
            if (folder, slug) in found:
                continue
            planned.append({
                "tantargy": known[0]["tantargy"], "evfolyam": known[0]["evfolyam"],
                "temakor": int(tk), "cim": cim, "lepes": 0, "url": None, "md": None,
                "slug": slug,
            })
    out = []
    for (folder, slug), v in found.items():
        v["slug"] = slug
        out.append(v)
    return sorted(out + planned, key=lambda v: v["slug"])


def build():
    data = topics()
    key_of = {n: k for n, k in SUBJECTS}
    for les in lessons():
        cell = data.get(f"{key_of.get(les['tantargy'])}/{les['evfolyam']}")
        if not cell:
            raise SystemExit(f"{les['slug']}: nincs ilyen tantárgy/évfolyam: {les['tantargy']} {les['evfolyam']}")
        tk = next((t for t in cell["temakorok"] if t["n"] == les["temakor"] and not t["modul"]), None)
        if not tk:
            raise SystemExit(f"{les['slug']}: nincs {les['temakor']}. témakör")
        tk["leckek"].append({k: les[k] for k in ("cim", "url", "md", "lepes")})
    for cell in data.values():
        cell["fajl"] = REPO + "kerettanterv/" + cell["fajl"]
    meta = {"subjects": SUBJECTS, "grades": [g for g, _, _ in GRADES],
            "schools": {g: s for g, s, _ in GRADES}}
    payload = json.dumps({"meta": meta, "cells": data}, ensure_ascii=False, separators=(",", ":"))
    tpl = (ROOT / "tools/index_template.html").read_text(encoding="utf-8")
    out = tpl.replace("/*__DATA__*/null", payload.replace("</", "<\\/"))
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    ready = sum(1 for c in data.values() for t in c["temakorok"] for l in t["leckek"] if l["url"])
    soon = sum(1 for c in data.values() for t in c["temakorok"] for l in t["leckek"] if not l["url"])
    print(f"✓ index.html · {len(data)} tantárgy–évfolyam · {ready} kész lecke · {soon} hamarosan")


if __name__ == "__main__":
    build()
