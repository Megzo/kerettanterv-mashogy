#!/usr/bin/env python3
"""A NAT 2020-hoz tartozó kerettantervek letöltése az Oktatási Hivatal oldaláról.

Forrás: https://www.oktatas.hu/kozneveles/kerettantervek/2020_nat
Kimenet: sources/oktatas.hu_2020_nat/<sáv>/ + manifest.json (URL, cím, dátum, sha256).

Futtatás (a projekt gyökeréből):  python3 -I tools/download_kerettanterv.py
"""
import datetime
import hashlib
import html
import json
import pathlib
import re
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "sources" / "oktatas.hu_2020_nat"
BASE = "https://www.oktatas.hu"
INDEX = BASE + "/kozneveles/kerettantervek/2020_nat"

# oldal-slug -> helyi mappanév
PAGES = {
    "kerettanterv_alt_isk_1_4_evf": "altisk_1-4",
    "kerettanterv_alt_isk_5_8": "altisk_5-8",
    "kerettanterv_gimn_9_12_evf": "gimn_9-12",
    "kerettanterv_gimn_7_12_evf": "gimn6_7-12",
}
UA = {"User-Agent": "Mozilla/5.0 (kerettanterv-downloader)"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()


def main():
    today = datetime.date.today().isoformat()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "_pages").mkdir(exist_ok=True)
    (OUT / "_pages" / "2020_nat.html").write_bytes(get(INDEX))
    (OUT / "_pages" / "bevezeto.html").write_bytes(get(INDEX + "/bevezeto"))
    manifest = {"source_index": INDEX, "downloaded": today, "files": []}
    for slug, folder in PAGES.items():
        page_url = f"{INDEX}/{slug}"
        raw = get(page_url)
        (OUT / "_pages" / f"{slug}.html").write_bytes(raw)
        page = raw.decode("utf-8", errors="replace")
        d = OUT / folder
        d.mkdir(exist_ok=True)
        seen = set()
        for m in re.finditer(r'<a [^>]*href="([^"]+\.(?:docx?|pdf))"[^>]*>(.*?)</a>', page, re.S | re.I):
            href = m.group(1)
            if href in seen:
                continue
            seen.add(href)
            title = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
            url = urllib.parse.urljoin(BASE, href)
            name = pathlib.PurePosixPath(urllib.parse.urlparse(url).path).name
            data = get(url)
            (d / name).write_bytes(data)
            manifest["files"].append({
                "band": folder, "title": title, "url": url, "page": page_url,
                "file": f"{folder}/{name}", "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            })
            print(f"{folder:12} {len(data):>9}  {name}  ({title})")
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n{len(manifest['files'])} fájl -> {OUT}")


if __name__ == "__main__":
    main()
