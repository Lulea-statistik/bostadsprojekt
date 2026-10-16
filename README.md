# Bostadsprojekt i Luleå kommun

Sammanställning av kommande, planerade, säljstartade och pågående nya bostadsprojekt i Luleå kommun.

**Senaste kontroll:** 2026-10-16  
**Källprincip:** endast privata/icke-kommunala källor. Luleå kommun och kommunala bolag används inte som verifieringskälla.

## Aktiva och verifierat planerade projekt

| Projekt | Område | Antal bostäder | Upplåtelseform | Byggherre/fastighetsägare | Status | Planerad byggstart | Planerad inflyttning | Senast ändrad |
|---|---|---:|---|---|---|---|---|---|
| Bonum Brf Årstiden | Björkskatan | 48 | Bostadsrätt, 55+ | Riksbyggen | Försäljning pågår | Ej verifierad | Prel. 2029 | 2026-10-16 |
| Termosen | Kronandalen | 32 | Bostadsrätt | Bonava | Försäljning pågår | Ej verifierad | Våren 2027, äldre prognos | 2026-10-16 |
| Kvarteret Skogsgläntan | Notviken | 52 | 48 bostadsrätter + 4 äganderätter | Lindbäcks + Cederfors | Etappvis försäljning pågår | 2026 enligt tidigare plan | 2027 för Brf Granen | 2026-10-16 |
| Kronanvägen | Kronan | ca 140 | Hyresrätt | Nornan Fastighetsutveckling + Lindbäcks | Planerat | 2026 enligt projektkatalog | Ej verifierad | 2026-10-16 |
| Brf Västra Stranden | Centrum/Västra Stranden | 74 | Bostadsrätt | Diös | Försäljning pågår | Ej verifierad | Ej verifierad | 2026-10-16 |
| Kv Fjärilen | Varvet | ca 38 | Ej verifierad | Galären | Planerat, detaljplaneskede | Tidigast våren 2027, villkorat | Ej verifierad | 2026-10-16 |
| Kåsan i Kronandalen | Kronandalen | 43 | Bostadsrätt | Bonava | Planerat, intresseanmälan | Ej verifierad | Ej verifierad | 2026-10-16 |
| Ryggsäcken i Kronandalen | Kronandalen | 38 | Bostadsrätt | Bonava | Planerat, intresseanmälan | Ej verifierad | Ej verifierad | 2026-10-16 |

**Aktiva/verifierade projekt: 8.** Publicerade projektuppgifter motsvarar cirka **465 bostäder**. Det är inte samma sak som byggstartade eller färdigställda bostäder.

## Bevakningsfall

| Projekt | Område | Antal bostäder | Status | Orsak till bevakning | Senast kontrollerad |
|---|---|---:|---|---|---|
| Brf Bergtallen | Dalbo | 25 | Försäljning pausad | Ingen verifierad återstart | 2026-10-16 |
| Kallkällan | Luleå | 46 | Osäker, möjligen färdigställt | Publicerad färdigställandetid har passerat | 2026-10-16 |
| Kv Gäddan | Centrum | drygt 78 | Kommande enligt äldre information | Färsk genomförandetidplan saknas | 2026-10-16 |
| Munkeberg Strand | Munkeberg | Ej verifierat | Tidigt skede | Aktualitet och tidplan osäkra | 2026-10-16 |
| Centralt bostadshus vid Varvsleden / Gersen | Centrum | 24 | Troligen inaktuell | Äldre planerad byggstart 2019 | 2026-10-16 |
| Hertsöheden – Bonava/Ekeblad | Hertsöheden | Ej fastställt per aktör | Tidigt planeringsskede | Områdesvolym kan inte tillskrivas respektive byggherre | 2026-10-16 |

**Bevakningsfall: 6.**

## Förändringar vid senaste kontrollen

- Skogsgläntan: ny annonseringsaktivitet och informationsträff för Brf Granen 21 oktober 2026.
- Kronanvägen: ägarförhållanden och upplåtelseform preciserade; byggstart fortfarande inte verifierad.
- Västra Stranden: adressuppgift kompletterad.
- Kåsan och Ryggsäcken: Regementsvägen verifierad som gatuadress.
- Hertsöheden: tillagt som bevakningsfall; bygger på äldre privat information, inte en nyannonsering 2026-10-16.

## Metod

Varje körning söker efter kommande, planerade, säljstartade eller pågående nya bostadsprojekt inom Luleå kommun. Projektens detaljsidor öppnas när de finns. Primär privat källa, exempelvis byggherre eller fastighetsägare, prioriteras. Mäklar-, portal- och branschkällor används som kompletterande kontroll.

Uppgifter om antal bostäder, byggstart, säljstart eller inflyttning gissas inte. Gamla, motsägelsefulla eller osäkra uppgifter markeras och kan flyttas till bevakningslistan.

Historiken sparas i `data/history.csv`. Varje körning sparas även som en daterad snapshot i `snapshots/`.

## Bevakade källor

Fastighetsbyrån, Bjurfors Nyproduktion, HusmanHagberg, Svensk Fastighetsförmedling Nyproduktion, Länsförsäkringar Fastighetsförmedling, MOHV, Riksbyggen, Peab Bostad, HSB, Skanska, NCC, Nåiden, Bonava, Lindbäcks, Galären, Booli, Hemnet, Diös, Cederfors Bostad, Nya Projekt och **Byggfakta**.


## Webbplats

Den filtrerbara tabellen publiceras via GitHub Pages från root på `main`:

https://lulea-statistik.github.io/bostadsprojekt/

Webbsidan läser den senaste snapshoten ur `data/history.csv` och kan filtreras på projekttext, statusklass, område och byggherre.

## Kvalitetskontroll mot dubbelräkning

Varje projekt har ett stabilt `ProjektID` i `data/project_registry.csv`. Registret innehåller även en `Räknegrupp` som används när flera namn eller deletapper hör till samma övergripande projekt.

Exempel: **Kvarteret Skogsgläntan** räknas som ett projekt med 52 bostäder. Brf Granen, Brf Tallen och äganderättsradhusen får därför inte samtidigt läggas in som separata aktiva projekt ovanpå moderprojektet.

GitHub Actions kör `scripts/validate_data.py` vid ändringar i data eller snapshots och stoppar valideringen om:

- samma `ProjektID` förekommer mer än en gång i samma snapshot,
- två aktiva rader har samma `Räknegrupp`,
- ett okänt `ProjektID` används,
- samma kombination av `Snapshot + ProjektID` förekommer flera gånger i historiken.


## Källdatum och kontrolltid

Från och med 2026-10-16 sparas även:

- `Källsida datum` – datum som faktiskt anges av källan,
- `Datumtyp` – om datumet är `Uppdaterad`, `Publicerad` eller om datum saknas,
- `Senast kontrollerad` – datum då vi senast kontrollerade projektsidan.

Om en projektsida inte själv redovisar ett säkert publicerings- eller uppdateringsdatum anges **Ej publicerat**. Crawldatum, sökmotorns indexdatum eller ett datum som bara förekommer i brödtext används inte som ersättning för sidans uppdateringsdatum.


## Följ projekt

GitHub Pages innehåller även sidan **Följ projekt**:

https://lulea-statistik.github.io/bostadsprojekt/folj-projekt.html

Där kan ett projekt väljas i en lista. Ett Gantt-liknande historikdiagram visar hur statusklass, projektstatus, bostadsantal, byggherre, upplåtelseform, planerad byggstart, säljstart och inflyttning förändras mellan snapshots. Under diagrammet visas även den fullständiga snapshot-historiken för valt projekt.


### Byggfakta som kompletterande källa

Byggfakta används som **sekundär aggregator**, inte som primär projektkälla. Uppgifter därifrån kan användas för att:

- upptäcka projekt som ännu inte fångats av övriga källor,
- komplettera byggstart, byggslut, projektstadium och involverade aktörer,
- identifiera förändrade tidsplaner eller projektstatus,
- kontrollera avvikelser mot byggherres eller fastighetsägares egen projektsida.

Om Byggfakta och en aktuell primär privat källa motsäger varandra prioriteras normalt primärkällan, och avvikelsen dokumenteras. Uppgifter bakom inloggning eller abonnemang används bara när de faktiskt är åtkomliga i den aktuella körningen.
