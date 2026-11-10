#!/usr/bin/env python3
"""Regression tests for non-destructive classification of project sources."""
import importlib.util
import unittest
from pathlib import Path

path = Path(__file__).with_name("watch_project_sources.py")
spec = importlib.util.spec_from_file_location("watch_project_sources", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ClassificationTest(unittest.TestCase):
    def test_known_project_url(self):
        row = {"url": "https://lindbacks.se/alla-projekt/kallkallan", "title": "Kallkällan 46 lägenheter i Luleå", "source": "Lindbäcks"}
        self.assertEqual(module.candidate_class(row, {row["url"]}, []), "Känd projektkälla")

    def test_no_automatic_known_on_nonmatching_title(self):
        row = {"url": "https://lulebo.se/artikel/28-nya-lagenheter-i-gammelstad", "title": "28 nya lägenheter i Gammelstad", "source": "Lulebo"}
        self.assertEqual(module.candidate_class(row, set(), ["kallkällan"]), "Möjligt nytt projekt – granska")

    def test_other_city_rejected(self):
        row = {"url": "https://lindbacks.se/alla-projekt/kv-nacken", "title": "90 bostäder i Piteå", "source": "Lindbäcks"}
        self.assertIn("Utanför", module.candidate_class(row, set(), []))

    def test_local_lindbacks_accepted(self):
        row = {"url": "https://lindbacks.se/alla-projekt/skogsglantan", "title": "52 bostäder i Luleå", "source": "Lindbäcks"}
        self.assertEqual(module.candidate_class(row, set(), []), "Möjligt nytt projekt – granska")

    def test_irrelevant_lulebo_link(self):
        row = {"url": "https://lulebo.se/artikel/ny-lagenhetshyra", "title": "Ny lägenhetshyra", "source": "Lulebo"}
        self.assertIn("Övrig länk", module.candidate_class(row, set(), []))

    def test_rent_increase_not_project(self):
        row = {"url": "https://lulebo.se/artikel/ny-lagenhetshyra-fran-1-juli-2027", "title": "Ny lägenhetshyra från 1 juli", "source": "Lulebo"}
        self.assertIn("Övrig länk", module.candidate_class(row, set(), []))

    def test_new_housing_project_still_candidate(self):
        row = {"url": "https://lulebo.se/artikel/28-nya-lagenheter-i-gammelstad", "title": "28 nya hyresrätter i Gammelstad", "source": "Lulebo"}
        self.assertEqual(module.candidate_class(row, set(), []), "Möjligt nytt projekt – granska")

    def test_new_rental_housing_with_hyphenated_url(self):
        row = {"url": "https://lulebo.se/artikel/28-nya-hyresratter-i-gammelstad", "title": "28 nya hyresrätter i Gammelstad", "source": "Lulebo"}
        self.assertEqual(module.candidate_class(row, set(), []), "Möjligt nytt projekt – granska")

    def test_rent_negotiation_not_new_project(self):
        row = {"url": "https://lulebo.se/artikel/hyresforhandlingar", "title": "Ny hyresförhandling för 2027", "source": "Lulebo"}
        self.assertIn("Övrig länk", module.candidate_class(row, set(), []))

    def test_planning_permission_not_build_project(self):
        row = {"url": "http://lulea.se/detaljplan-fageln", "title": "Detaljplan Fågeln", "source": "Luleå kommun – mark och exploatering"}
        self.assertEqual(module.candidate_class(row, set(), []), "Planeringsunderlag – ej verifierat byggprojekt")

    def test_municipal_project_overview_as_context(self):
        row = {"url": "https://lulea.se/samhalle--utveckling/aktuella-projekt.html", "title": "Aktuella projekt", "source": "Luleå kommun – Kronandalen"}
        self.assertEqual(module.candidate_class(row, set(), []), "Planeringsunderlag – ej verifierat byggprojekt")

    def test_bonava_category_page_not_project(self):
        row = {"url": "https://bonava.se/bostad/lulea/lagenhet", "title": "Lägenheter", "source": "Bonava"}
        self.assertEqual(module.candidate_class(row, set(), []), "Översiktssida – sök projektspecifika länkar")

    def test_bonava_project_detail_still_candidate(self):
        row = {"url": "https://bonava.se/bostad/lulea/kronandalen/kasan", "title": "Kåsan", "source": "Bonava"}
        self.assertEqual(module.candidate_class(row, set(), []), "Möjligt nytt projekt – granska")

    def test_lulebo_project_list_is_overview(self):
        row = {"url": "https://lulebo.se/artikel/projekt-i-vara-omraden", "title": "Projekt i våra områden", "source": "Lulebo"}
        self.assertEqual(module.candidate_class(row, set(), []), "Översiktssida – sök projektspecifika länkar")

    def test_manual_review_project_category(self):
        decision = {"project_id": "lulebo-hertson-ekorr-radjur", "status": "Granskat – befintligt projekt", "comment": "Samma projekt"}
        self.assertEqual(module.review_category(decision), "Granskat – kopplat ProjektID")

    def test_manual_review_historical_not_new(self):
        decision = {"project_id": "", "status": "Historiskt projekt", "comment": "Äldre inflyttning"}
        self.assertEqual(module.review_category(decision), "Granskat – historiskt projekt")

    def test_manual_review_invalid_without_id(self):
        with self.assertRaises(ValueError):
            module.review_category({"project_id": "", "status": "Granskat – befintligt projekt"})

    def test_reviewed_urls_are_normalized(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            csv_file = Path(directory) / "decisions.csv"
            csv_file.write_text("URL,ProjektID,Granskningsstatus,Kommentar\\nhttps://www.lulebo.se/artikel/assistentvagen/, ,Historiskt projekt,Äldre\\n", encoding="utf-8")
            decisions = module.load_link_decisions(csv_file)
            self.assertIn("https://lulebo.se/artikel/assistentvagen", decisions)

    def test_normalize_query_and_www(self):
        self.assertEqual(module.normalize("https://www.lulebo.se/artikel/nybygge/?utm_source=test"), "https://lulebo.se/artikel/nybygge")

if __name__ == "__main__":
    unittest.main()
