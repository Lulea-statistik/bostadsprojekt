import csv, glob, sys
from pathlib import Path

registry_path = Path("data/project_registry.csv")
with registry_path.open(encoding="utf-8-sig", newline="") as f:
    registry = {r["ProjektID"]: r for r in csv.DictReader(f)}

errors = []
for path in sorted(glob.glob("snapshots/*.csv")):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    ids = [r.get("ProjektID","").strip() for r in rows]
    if any(not x for x in ids):
        errors.append(f"{path}: saknar ProjektID på minst en rad")
    unknown = sorted(set(ids) - set(registry))
    if unknown:
        errors.append(f"{path}: okända ProjektID: {', '.join(unknown)}")
    dup = sorted({x for x in ids if ids.count(x) > 1 and x})
    if dup:
        errors.append(f"{path}: samma ProjektID förekommer flera gånger: {', '.join(dup)}")
    groups = []
    for r in rows:
        if r.get("Statusklass") == "Aktiv/verifierad":
            meta = registry.get(r.get("ProjektID",""), {})
            if meta.get("RäknaIProjektTotal") == "Ja":
                groups.append(meta.get("Räknegrupp") or r.get("ProjektID"))
    gdup = sorted({x for x in groups if groups.count(x) > 1 and x})
    if gdup:
        errors.append(f"{path}: dubbel räknegrupp bland aktiva projekt: {', '.join(gdup)}")

history = Path("data/history.csv")
if history.exists():
    with history.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    keys=[(r.get("Snapshot",""), r.get("ProjektID","")) for r in rows]
    dup=sorted({k for k in keys if keys.count(k)>1 and all(k)})
    if dup:
        errors.append("data/history.csv: dubbletter av Snapshot + ProjektID: " + ", ".join(f"{a}/{b}" for a,b in dup))

if errors:
    print("\n".join("ERROR: "+e for e in errors))
    sys.exit(1)
print("OK: inga dubbla ProjektID eller aktiva räknegrupper hittades.")
