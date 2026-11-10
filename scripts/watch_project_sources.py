#!/usr/bin/env python3
"""Weekly, read-only project lead discovery. Never changes historical project data."""
import csv
import json
import re
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
GOOD = re.compile(r"bostad|hyresrätt|bostadsrätt|lägenhet|studentbo|nyproduktion|byggprojekt|byggstart|markanvis|detaljplan|exploater|kvarter|förtätn|projekt|brf|kronan|porsön", re.I)
BAD = re.compile(r"cookie|integritet|kontakt|karriär|ledig tjänst|facebook|instagram|linkedin|logga in|nyhetsbrev|personuppgift", re.I)

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.active = None
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.active = {"url": dict(attrs).get("href", ""), "title": ""}
    def handle_data(self, data):
        if self.active is not None:
            self.active["title"] += data
    def handle_endtag(self, tag):
        if tag == "a" and self.active is not None:
            self.links.append(self.active)
            self.active = None

def normalize(url):
    p = urlsplit(url)
    return urlunsplit((p.scheme.lower(), p.netloc.lower().removeprefix("www."), p.path.rstrip("/") or "/", "", ""))

def main():
    sources = list(csv.DictReader((DATA / "source_watchlist.csv").open(encoding="utf-8-sig", newline="")))
    previous_file = DATA / "source_discovery_state.json"
    previous = json.loads(previous_file.read_text(encoding="utf-8")) if previous_file.exists() else {"urls": [], "reviewed": []}
    known = set()
    with (DATA / "history.csv").open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("Direkt URL", "").startswith("http"):
                known.add(normalize(row["Direkt URL"]))
    collected = {}
    successful, failed = [], []
    for source in sources:
        name, base = source["Källa"], source["URL"].strip()
        try:
            req = urllib.request.Request(base, headers={"User-Agent": "LuleaHousingProjectWatch/1.0 (public link discovery only)", "Accept": "text/html"})
            with urllib.request.urlopen(req, timeout=18) as response:
                if "html" not in response.headers.get("Content-Type", "").lower():
                    raise ValueError("not HTML")
                raw = response.read(1200001)
                if len(raw) > 1200000:
                    raise ValueError("page too large")
                html = raw.decode(response.headers.get_content_charset() or "utf-8", errors="replace")
            parser = LinkParser()
            parser.feed(html)
            local = {}
            for item in parser.links:
                title = " ".join(item["title"].split())[:140]
                href = item["url"]
                if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
                    continue
                url = urljoin(base, href)
                a, b = (urlsplit(url).hostname or "").removeprefix("www."), (urlsplit(base).hostname or "").removeprefix("www.")
                if a != b or urlsplit(url).scheme not in ("http", "https"):
                    continue
                url = normalize(url)
                if url == normalize(base) or re.search(r"\.(pdf|jpg|png|svg|css|js|xml|zip|docx?)$", urlsplit(url).path, re.I):
                    continue
                if BAD.search(title) or not GOOD.search(title + " " + urlsplit(url).path):
                    continue
                local.setdefault(url, title or urlsplit(url).path.rsplit("/", 1)[-1])
            for url, title in sorted(local.items())[:50]:
                collected.setdefault(url, {"source": name, "title": title, "url": url})
            successful.append((name, len(local)))
        except Exception as exc:
            failed.append((name, str(exc)[:160]))
    if not successful:
        raise SystemExit("No sources could be reached; no state changed")
    seen = set(previous["urls"])
    reviewed = set(previous.get("reviewed", []))
    new = [item for url, item in sorted(collected.items()) if url not in seen and url not in known and url not in reviewed]
    pending = [item for url, item in sorted(collected.items()) if url not in known and url not in reviewed]
    previous_file.write_text(json.dumps({"urls": sorted(seen | set(collected)), "reviewed": sorted(reviewed)}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (DATA / "source_review_queue.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Källa", "Länkrubrik", "URL", "Status"])
        for item in pending:
            writer.writerow([item["source"], item["title"], item["url"], "Kräver manuell kontroll"])
    report = ROOT / "reports/source_watch_latest.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Bevakning av nya bostadsprojekt", "", "Kontrollerad: " + date.today().isoformat(), "",
             "Källor som kunde läsas: " + str(len(successful)) + "/" + str(len(sources)),
             "Nya länkträffar: " + str(len(new)), "Länkträffar att granska: " + str(len(pending)), "",
             "En länk är en kandidat, inte ett verifierat bostadsprojekt. Ingen automatisk ändring sker i projekthistorik eller räknegrupper.", "",
             "## Nya kandidater", ""]
    for x in new[:100]:
        lines.append("- " + x["source"] + ": [" + x["title"].replace("[", "(").replace("]", ")") + "](" + x["url"] + ")")
    if not new:
        lines.append("Inga nya länkar.")
    lines += ["", "## Källstatus", ""]
    for name, count in successful:
        lines.append("- OK: " + name + " (" + str(count) + " matchande länkar)")
    for name, error in failed:
        lines.append("- FEL: " + name + " (" + error + ")")
    lines += ["", "Kontrollera varje kandidats bostadsändamål och jämför med befintligt ProjektID, adress och byggherre innan ny post skapas.",
              "Granskade länkar kan läggas till i fältet reviewed i data/source_discovery_state.json.",
              "JavaScript-renderade projektlistor kan missas; en lyckad HTTP-hämtning är inte garanti för fullständighet.", ""]
    report.write_text("\n".join(lines), encoding="utf-8")
    print("Sources OK", len(successful), "failed", len(failed), "new", len(new), "pending", len(pending))

if __name__ == "__main__":
    main()
