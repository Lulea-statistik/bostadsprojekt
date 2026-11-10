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


def candidate_class(item, known, names):
    """Conservative triage: never equate a link with an actual project."""
    title = item["title"].lower()
    url = item["url"].lower()
    source = item["source"].lower()
    path = urlsplit(url).path.lower()
    if item["url"] in known:
        return "Känd projektkälla"
    if ("lindbäcks" in source or "lindb" in source):
        if not re.search(r"\bluleå\b|\blulea\b", title + " " + path):
            return "Utanför Luleå / osäker geografi"
    if "bonava" in source and "/lulea/" not in path:
        return "Utanför Luleå / osäker geografi"
    if "lulebo" in source:
        if not re.search(r"nyproduktion|nya.lägenhet|ny.lägenhet|bygger|nybygg|kallkallan|hertson|ekorr|radjur|edefors|projekt", title + " " + path, re.I):
            return "Övrig länk – ej projektindikation"
    if "galären" in source and not re.search(r"/projekt/|/galaren-projekt/|nyproduktion|bygger|bostadsprojekt", title + " " + path, re.I):
        return "Övrig länk – ej projektindikation"
    if "aktuella projekt" in source and not re.search(r"bostad|boende|kronanvägen|kronandalen|hertsöheden|bävern|pontonen", title + " " + path, re.I):
        return "Övrig länk – ej projektindikation"
    if "mark och exploatering" in source and not re.search(r"detaljplan|bostad|markanvis", title + " " + path, re.I):
        return "Övrig länk – ej projektindikation"
    # Only exact, distinctive names: fuzzy generic matching can merge unrelated projects.
    for name in names:
        if len(name) >= 9 and name in title and name not in ("kronandalen", "luleå", "projekt"):
            return "Möjligen redan känt projekt – verifiera"
    return "Möjligt nytt projekt – granska"

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
    seen = set(previous.get("urls", []))
    reviewed = set(previous.get("reviewed", []))
    today = date.today().isoformat()
    # Retain candidate URLs across runs: source link disappearance is never a project cancellation.
    # Migrate first-run queue; older state has only a list of URLs.
    persistent = previous.get("candidates", {})
    if not persistent and (DATA / "source_review_queue.csv").exists():
        with (DATA / "source_review_queue.csv").open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                url = row.get("URL", "")
                if url and url not in reviewed:
                    persistent[url] = {
                        "source": row.get("Källa", ""), "title": row.get("Länkrubrik", ""),
                        "first_seen": "2026-11-10", "last_seen": "2026-11-10",
                        "source_status": "Historisk länk – inte kontrollerad denna vecka"
                    }
    names = []
    with (DATA / "project_registry.csv").open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            name = row.get("CanonicalProjekt", "").lower()
            names.extend([name, row.get("ProjektID", "").replace("-", " ").lower()])
    for url, item in collected.items():
        old = persistent.get(url, {})
        persistent[url] = {
            "source": item["source"], "title": item["title"],
            "first_seen": old.get("first_seen", today),
            "last_seen": today,
            "source_status": "Länk synlig vid senaste körningen"
        }
    # No deletions or completion inference, even when sources are unreachable.
    fresh = [url for url in collected if url not in seen and url not in known and url not in reviewed]
    categories = {}
    rows = []
    for url, item in sorted(persistent.items()):
        if url in reviewed:
            continue
        label = candidate_class({"url": url, "title": item["title"], "source": item["source"]}, known, names)
        categories[label] = categories.get(label, 0) + 1
        rows.append((label, item, url))
    order = {
        "Möjligt nytt projekt – granska": 0,
        "Möjligen redan känt projekt – verifiera": 1,
        "Känd projektkälla": 2,
        "Utanför Luleå / osäker geografi": 3,
        "Övrig länk – ej projektindikation": 4
    }
    rows.sort(key=lambda x: (order.get(x[0], 5), x[1]["source"], x[2]))
    previous_file.write_text(
        json.dumps({"urls": sorted(seen | set(collected)), "reviewed": sorted(reviewed),
                    "candidates": persistent}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    with (DATA / "source_review_queue.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Källa", "Länkrubrik", "URL", "Kategori", "Först upptäckt", "Senast sedd", "Källstatus"])
        for label, item, url in rows:
            writer.writerow([item["source"], item["title"], url, label,
                             item["first_seen"], item["last_seen"], item["source_status"]])
    report = ROOT / "reports/source_watch_latest.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Bevakning av bostadsprojekt", "", "Kontrollerad: " + today, "",
             "Källor som kunde läsas: " + str(len(successful)) + "/" + str(len(sources)),
             "Nya länkar sedan föregående kontroll: " + str(len(fresh)),
             "Bevarade kandidatlänkar i kön: " + str(len(rows)), "",
             "## Kategorier", ""]
    for name, count in sorted(categories.items(), key=lambda pair: order.get(pair[0], 5)):
        lines.append("- " + name + ": **" + str(count) + "**")
    lines += ["", "## Nya länkträffar", ""]
    for url in fresh[:100]:
        item = collected[url]
        lines.append("- " + item["source"] + ": [" + item["title"].replace("[", "(").replace("]", ")") + "](" + url + ")")
    if not fresh:
        lines.append("Inga nya länkar.")
    lines += ["", "## Källstatus", ""]
    for name, count in successful:
        lines.append("- OK: " + name + " (" + str(count) + " matchande länkar)")
    for name, error in failed:
        lines.append("- FEL: " + name + " (" + error + ")")
    lines += ["", "## Bevaranderegel", "",
              "**Ett projekt får aldrig raderas, stängas eller omklassas enbart därför att dess källa försvinner.**",
              "Även en försvunnen URL ligger kvar i kön med tidigare källstatus och senaste fynddatum. ",
              "Projekt-ID, statusklass, bostadsvolym och snapshots förblir oförändrade av denna kontroll.",
              "Om en källa flyttar till en annan URL ska samma projekt-ID användas och den nya URL:en läggas till som ytterligare källbelägg efter granskning.",
              "Geografisk filtrering och matchning är heuristisk: kontrollera kommun, fastighetsbeteckning, byggherre och etapper manuellt.",
              "Tidigare registrerade URL:er räknas inte automatiskt som fullständiga eller aktuella projektbelägg.",
              "Sätt granskade URL:er i arrayen reviewed i data/source_discovery_state.json för att dölja dem i kön.",
              ""]
    report.write_text("\n".join(lines), encoding="utf-8")
    print("Sources OK", len(successful), "failed", len(failed),
          "new", len(fresh), "retained", len(rows), "categories", categories)

if __name__ == "__main__":
    main()
