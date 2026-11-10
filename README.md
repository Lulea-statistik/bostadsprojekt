# Bostadsprojekt i Luleå kommun

Sammanställning av kommande, planerade, säljstartade och pågående nya bostadsprojekt i Luleå kommun.

**Senaste registerkomplettering:** 2026-11-10 (tidigare befintliga projekt: senaste källkontroll 2026-10-16).  
**Källprincip:** privata byggherre- och fastighetsägarkällor används i första hand för projektspecifika fakta. Luleå kommuns planer, markanvisningar och aktuella projekt används nu också som **primär källa för kommunala beslut och planeringsstatus** samt för att upptäcka tidiga projekt. Kommunala uppgifter om faktiskt påbörjad byggnation kan styrka status för det särskilda projektet, men en plan eller markanvisning får aldrig räknas som säkert byggstartad bostadsvolym. Kommunala bolags egna projektuppgifter får användas som projektägarkälla med tydlig avsändare.

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

**Bevakningsfall i ursprunglig genomgång: 6.** Från 2026-11-10 har registret kompletterats med nya projekt från kommunala uppgifter; totalsiffran ovan avser den äldre genomgången från oktober.

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

Fastighetsbyrån, Bjurfors Nyproduktion, HusmanHagberg, Svensk Fastighetsförmedling Nyproduktion, Länsförsäkringar Fastighetsförmedling, MOHV, Riksbyggen, Peab Bostad, HSB, Skanska, NCC, Nåiden, Bonava, Lindbäcks, Galären, Booli, Hemnet, Diös, Cederfors Bostad, Nya Projekt, **Byggfakta**, **RAWI**, **Stålstaden**, **Hemsö**, **SBS/Studentbostäder i Norden**, **STUSAB Luleå Fastigheter** och **Rikshem**.


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


### Utökad kärnlista för lokal projektbevakning

Följande privata aktörer bevakas särskilt eftersom de har tydlig lokal närvaro, projektutveckling eller större bostadsbestånd i Luleå:

- **RAWI** – hög prioritet; lokal privat fastighetsaktör med uppgift om större nybyggnadsprojekt i Luleå.
- **Stålstaden** – hög prioritet; lokal fastighetsaktör och relevant för bostadsdominerad blandstad, bland annat Mjölkuddens centrum.
- **Hemsö** – medel–hög prioritet; relevant som projektpartner i blandstads-/centrumprojekt.
- **SBS / Studentbostäder i Norden** – medel–hög prioritet; stor privat studentbostadsaktör i Luleå.
- **STUSAB Luleå Fastigheter** – medel prioritet; används främst som bolags-/ägarkontroll inom SBS-sfären.
- **Rikshem** – medel prioritet; stor privat bostadsägare med egen nyproduktionsbevakning.

För att undvika dubbelräkning behandlas **SBS/Studentbostäder i Norden och STUSAB** som närstående källor. Ett projekt som förekommer hos båda ska fortfarande bara få ett ProjektID och en Räknegrupp.

## Komplettering 10 november 2026 – kommunala projekt och tidiga bevakningsfall

Följande nya projekt-ID har lagts till i `data/project_registry.csv` och `data/history.csv`. Nya rader är en **avgränsad komplettering**, inte en ny samlad källkontroll av samtliga befintliga projekt. Det tidigare projekturvalet behåller sina faktiska kontrolltider. Inga tidigare snapshots har skrivits om.

| Projekt-ID | Projekt | Status och avgränsning |
|---|---|---|
| `skidan` | Skidan, Kronandalen | **Aktiv/verifierad:** BD Bygg påbörjade byggnation våren 2026; 95 lägenheter enligt kommunens projektsida. Separat från Kronanvägen och Lulebos Västra entrén. |
| `vastra-entren-lulebo` | Lulebo, Västra entrén | **Bevakning:** markanvisning och detaljplanearbete; fyra punkthus, antal bostäder inte fastställt. |
| `bavern-1` | Bävern 1 | **Bevakning:** blandstad med bostäder som möjlig användning; ingen säker bostadsvolym. |
| `pontonen-2` | Pontonen 2 | **Bevakning:** bostäder i blandprojekt med hotell och kontor; förberedande markarbeten är inte verifierad bostadsbyggstart. |
| `porson-1-427` | Porsön 1:427 | **Bevakning:** planärende för studentbostäder. |
| `orren-6` | Orren 6 | **Bevakning:** Lulebos planansökan för omvandling från kontor till bostäder. |
| `torsken-9` | Torsken 9 | **Bevakning:** alternativ hotell eller bostäder; osäker bostadsandel. |

**Inte tillagt:** Björsbyn 1:12 (Dalbo) eftersom markanvisningens ändamål som bostadsprojekt ännu inte verifierats. Registrera inte rena markanvisningsobjekt som bostadsprojekt utan belägg.

### Löpande bevakning och källa

Se `data/source_watchlist.csv`. Dokumentet skiljer mellan officiell projektsida, kommunens plan-/markanvisningsinformation och privat byggherres projektsidor. Vid återkommande kontroll ska varje ny informationshändelse jämföras med befintliga `ProjektID`, `Räknegrupp`, fastighetsbeteckning och byggherre. En detaljplan och en byggherres projektsida får aldrig skapa två projekt-ID för samma tillkommande bostäder.

**Automatisk insamling:** källregistret är ett underlag för kommande bevakningsflöden; att en källa finns på listan betyder inte att den redan hämtas automatiskt. Källan måste kunna läsas lagenligt och tekniskt. Ingen uppskattad bostadsvolym får räknas som verifierad.

## Automatisk veckobevakning av nya projektkällor

Arbetsflödet **Weekly housing project source watch** (`.github/workflows/watch-project-sources.yml`) körs tisdagar kl. 06.15 UTC och kan även startas manuellt med `workflow_dispatch`.

Flödet läser de 10 offentliga listningssidorna i `data/source_watchlist.csv` med låg volym (en HTML-hämtning per källa). Det sammanställer länkar som kan handla om projekt och planering. Resultatet finns i:

- `reports/source_watch_latest.md` – senaste källkontroll, nya länkar och hämtfel.
- `data/source_review_queue.csv` – kandidatlänkar som måste granskas och jämföras med befintliga projekt.
- `data/source_discovery_state.json` – tidigare upptäckta och manuellt granskade URL:er.

**Källavgränsning:** det är länkar från respektive startsida/listningssida som bevakas; sidor bakom JavaScript-rendering, paginering, inloggning eller djupa undermenyer kan missas. En lyckad hämtning bevisar inte att källan är fullständigt indexerad.

**Kvalitet och säkerhet:** flödet skriver inte i `data/history.csv`, `data/project_registry.csv` eller `snapshots/`. En länkträff räknas inte som ett bostadsprojekt, och ingen osäker bostadsvolym adderas till summeringarna. Granskare kontrollerar bostadsändamål, befintliga `ProjektID`, fastighet, projektetapper, byggstart och tidsplan innan projektpost godkänns. Länkar som granskats utan att registreras läggs i arrayen `reviewed` i `data/source_discovery_state.json`.

För att automatiska commits till rapport och kö ska fungera behöver GitHub Actions ha rätt att skriva till repositoriet och eventuell branch protection tillåta den typen av uppdatering. Om det inte fungerar kan rapporten fortfarande laddas ned som workflow-artifact från körningen. Första körningen etablerar en baslinje och kan därför ge många länkträffar som inte är nya bostadsprojekt.

### Beständig projektbevakning och källbortfall (november 2026)

Den veckovisa källbevakningen **tar aldrig bort ett projekt för att en länk saknas**. Projektets stabila identitet är ProjektID, inte URL. Ett projekt kan förekomma på flera byggaktörers, mäklares och kommunens webbplatser. Frånvaro på en webbplats kan bero på publiceringsändring, flyttad URL, avpublicering eller tillfälligt hämtfel och betyder **inte** att byggprojektet avslutats.

Upptäckta källänkar lagras beständigt i data/source_discovery_state.json med first_seen och last_seen. Om en länk inte återfinns i ett senare söktillfälle står tidigare senaste fynddatum kvar, och länken ligger kvar i granskningskön. En sådan länkträff är inte ett påstående om att den gamla sidan fortfarande är aktuell.

data/source_review_queue.csv innehåller automatiskt kategorierna:
- Möjligt nytt projekt – granska
- Möjligen redan känt projekt – verifiera
- Känd projektkälla
- Utanför Luleå / osäker geografi
- Övrig länk – ej projektindikation

Kategorierna baseras på regelbaserad indikativ filtrering och **är inte automatiskt kvalitetsgodkända projekt**. Framför allt måste osäker geografi och matchning på namn kontrolleras manuellt. Lägg först efter verifiering in en ny URL som kompletterande källa till ett existerande ProjektID. Projektstatus, bostadsantal, historikrader och snapshots ändras aldrig av källbevakningen.

Första körningen från 10 november 2026 gav 148 råa länkträffar. Den nya modellen behåller dessa i den beständiga länkhistoriken men delar upp dem efter relevans för att minska manuell granskning.

Tester för kategorisering körs före källhämtning i GitHub Actions (scripts/test_watch_project_sources.py).

### Avgränsning av aktiv bevakning från 10 november 2026

- **Lulebo och Bonava:** prioriterade för projektspecifik bevakning av kommande, pågående och marknadsförda bostadsprojekt. Kontrollera om länkar gäller samma byggprojekt, etapp eller färdigställda bostäder.
- **Kommunala detaljplaner, markanvisningar och projekt-/översiktssidor:** behandlas enbart som *planeringsunderlag*. En detaljplan möjliggör bebyggelse men innebär varken att byggstart är beslutad eller att ett bostadsprojekt genomförs.
- **Samlings- och söksidor** hos Lulebo och Bonava ger uppslag till direktlänkar men är inte enskilda projekt.
- Övriga privata byggherrekällor behålls i källregistret. Ingen gammal länk eller projektpost tas bort; denna prioritering påverkar enbart granskningskön.
- Projektvolym, byggstart och framtida bostadstillskott räknas aldrig från enbart planeringsunderlag. Även projekt som inte längre finns på en källa kan fortsätta att följas med samma ProjektID och andra källor.

Rapporten `reports/source_watch_latest.md` innehåller nu ett eget avsnitt för direkta Lulebo-/Bonava-träffar och skiljer dem från kommunala planeringsunderlag. Källan måste fortfarande granskas innan ett projekt läggs till eller ändras.

### Källgranskning av Lulebos projektsidor (10 november 2026)

Projektuppgifter från de sju kandidatlänkarna och en Kallkällan-träff har jämförts med projektregistret och dokumenterats i `data/lulebo_source_audit_2026-11-10.csv`. Granskningen skiljer mellan *historiska uppgifter*, *pågående nyproduktion*, *villkorade nya bostäder inom ROT* och *möjlig dubbelräkning*. Datum som redan passerat i en äldre webbsida är inte i sig bevis för faktiskt färdigställande.

- **Hertsön / Ekorr- och Rådjursstigarna:** två Lulebo-länkar beskriver ett enda projekt om 28 lägenheter, med ett ProjektID och en enda räknegrupp. Lulebo anger byggstart hösten 2025 och planerad inflyttning mars 2027.
- **Edeforsgatan:** preliminärt 40–50 nytillkommande källarlägenheter under flerårig ROT; för första etappen anges fem preliminära lägenheter. Cirka 270 befintliga ROT-bostäder får **inte** adderas som nya. RäknaIProjektTotal = Nej tills bostadstillskottet är klarlagt.
- **Gammelstad, Assistentvägen, Björkskatan och Malmudden:** historiska projektsidor med inflyttningsuppgifter 2021–2024. De skapar inte nya kommande byggprojekt i registret. För Gäddviksvägen ersattes 24 lägenheter med 28, vilket innebär ett netto om fyra om projektet genomförts som beskrivet.
- **Kallkällan:** Lulebos 152 lägenheter och Lindbäcks 46 lägenheter följs med skilda identiteter. De får **inte** adderas tillsammans utan att byggnads-/fastighetsmässig överlappning har uteslutits. Båda ligger därför utanför säker räkning tills kompletterande granskning genomförts.

Den automatiska länkkön kan fortfarande visa redan granskade projektlänkar som kandidater; den manuella sakgranskningen finns i separat revisionsfil. Regler för projektstatus, sista fynddatum och bevarande av försvunna källor fortsätter gälla.

### Beständiga länkningsbeslut för granskade källor

`data/source_link_decisions.csv` är det manuella beslutsregistret, med en rad per exakt granskad URL (normaliserad från www, avslutande snedstreck och spårningsparametrar). Kolumner:

- `URL`: granskad källa.
- `ProjektID`: redan befintligt ID i `data/project_registry.csv`; obligatoriskt för **Granskat – befintligt projekt**.
- `Granskningsstatus`: **Granskat – befintligt projekt** eller **Historiskt projekt**.
- `Kommentar`: granskningsmotivering och eventuella begränsningar.

Källbevakningen använder besluten **före** den automatiska heuristiken, validerar ProjektID mot projektregistret och visar känd projekttillhörighet i `data/source_review_queue.csv`. Redan granskade länkar finns kvar som spårbar historik, men sorteras under **Granskat – kopplat ProjektID** eller **Granskat – historiskt projekt** i stället för *Möjligt nytt projekt*. De räknas inte som nya länkträffar.

**Ny URL till samma projekt:** en ny webbadress får ingen automatisk identitet enbart genom namnlikhet. Om projekt-ID inte är verifierat för den nya URL:en flaggas den fortsatt för manuell granskning. Lägg sedan till exakt den nya URL:en med det befintliga ProjektID:t i beslutsregistret, utan att skapa en ny projektpost. Att en tidigare URL saknas ändrar aldrig projektstatus eller historik.

Första manuella registreringen (10 november 2026) omfattar nio länkar: två till samma Hertsön-projekt, Edeforsgatan, Lulebos punkthus på Kallkällan, Lindbäcks separata Kallkällan-fall och fyra historiska projektlänkar. Äldre daterade inflyttningsplaner har inte ensamma använts som bevis för faktisk färdigställandestatus.
