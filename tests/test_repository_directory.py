"""Offline public navigation boundaries; no probe is a publication claim."""
import copy
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("directory", ROOT / "scripts/project_repository_directory.py")
DIRECTORY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DIRECTORY)


class RepositoryDirectory(unittest.TestCase):
    def setUp(self):
        self.value = DIRECTORY.build()

    def row(self, name):
        return next(row for row in self.value["entries"] if row["repository"] == f"egohygiene/{name}")

    def test_committed_projection_is_exact_and_retains_original_clocks(self):
        raw = (ROOT / DIRECTORY.OUTPUT_PATH).read_bytes()
        self.assertEqual(raw, DIRECTORY.encoded(self.value))
        self.assertEqual(raw, DIRECTORY.encoded(DIRECTORY.build()))
        self.assertEqual(self.value["catalog"]["observed_at"], "2026-11-09T14:06:57Z")
        self.assertEqual(self.value["source_inventory"]["observed_at"], "2026-11-10T23:49:35Z")
        self.assertFalse(self.value["scope"]["model_evidence"])
        self.assertFalse(self.value["scope"]["current_availability_checked"])

    def test_source_declaration_never_becomes_publication(self):
        dashboard = self.row("hygiene")["dashboard"]
        self.assertEqual(dashboard["url"], "https://hygiene.egohygiene.io/intelligence/")
        self.assertEqual(dashboard["link_state"], "source-declared")
        self.assertEqual(dashboard["publication"]["state"], "unknown")
        self.assertIsNone(dashboard["publication"]["observed_at"])
        self.assertIsNone(self.row("optiflow")["dashboard"]["url"])
        self.assertIsNone(self.row("antidote")["dashboard"]["url"])

    def test_recorded_receipts_are_distinct_from_historical_source(self):
        row = self.row(".github")
        self.assertEqual(row["source_observation"]["state"], "not-declared-in-inspected-source")
        publication = row["dashboard"]["publication"]
        self.assertEqual(publication["run_url"],
                         "https://github.com/egohygiene/.github/actions/runs/43372599165")
        self.assertEqual(publication["observed_at"], "2026-11-13T05:32:30Z")
        publication = self.row("empathy")["dashboard"]["publication"]
        self.assertEqual(publication["source_revision"], "41d4c8bdba88cd5cc17318647d542eea57a70364")
        self.assertEqual(publication["observed_at"], "2026-11-14T06:35:35.745Z")
        self.assertEqual(sum(row["dashboard"]["publication"]["state"] == "recorded"
                             for row in self.value["entries"]), 2)

    def test_duplicate_ids_names_dangling_rows_and_extra_model_fields_fail(self):
        mutations = [lambda value: value["entries"].append(copy.deepcopy(value["entries"][0])),
            lambda value: value["entries"][1].update(repository_id=value["entries"][0]["repository_id"]),
            lambda value: value["entries"][1].update(repository="foreign/private"),
            lambda value: value.update(core={"state": "available"}),
            lambda value: value["scope"].update(model_evidence=True)]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                value = copy.deepcopy(self.value)
                mutate(value)
                with self.assertRaises(ValueError):
                    DIRECTORY.validate(value)

    def test_unknown_destination_or_publication_cannot_gain_invented_details(self):
        dashboard = self.row("aether")["dashboard"]
        for field, value in [("url", "https://aether.egohygiene.io/intelligence/"),
                             ("publication", {"state": "recorded"})]:
            original = copy.deepcopy(dashboard[field])
            dashboard[field] = value
            with self.assertRaises(ValueError):
                DIRECTORY.validate(self.value)
            dashboard[field] = original
        publication = self.row("empathy")["dashboard"]["publication"]
        for field, value in [("evidence", None), ("run_attempt", True),
                             ("run_url", "https://github.com/egohygiene/hygiene/actions/runs/1")]:
            original = publication[field]
            publication[field] = value
            with self.assertRaises(ValueError):
                DIRECTORY.validate(self.value)
            publication[field] = original

    def test_unsafe_links_fail_before_rendering(self):
        invalid = ["javascript:alert(1)", "http://egohygiene.io/intelligence/",
            "//egohygiene.io/intelligence/", "https://egohygiene.io.evil.example/",
            "https://evil.example/intelligence/", "https://egohygiene.io@evil.example/",
            "https://egohygiene.io:443/", "https://.egohygiene.io/",
            "https://-x.egohygiene.io/", "https://egohygiene.io/%2e%2e/",
            "https://egohygiene.io/../", "https://egohygiene.io/\n",
            "https://egohygiene.io/?next=evil", "https://egohygiene.io/#secret",
            "https://egohygiene.io/\\evil"]
        for url in invalid:
            with self.subTest(url=url), self.assertRaises(ValueError):
                DIRECTORY.safe_url(url)

    def test_source_digest_and_duplicate_json_fail_closed(self):
        with self.assertRaises(ValueError):
            DIRECTORY.read(DIRECTORY.INVENTORY_PATH, "0" * 64)
        with self.assertRaises(ValueError):
            DIRECTORY.document(b'{"repository":"public","repository":"private"}')
        with self.assertRaises(ValueError):
            DIRECTORY.document(b'{"score":NaN}')

    def test_plausible_unadmitted_links_and_source_rewrites_fail(self):
        row = self.row("aether")
        row["dashboard"].update(link_state="source-declared",
                                url="https://aether.egohygiene.io/intelligence/")
        with self.assertRaises(ValueError):
            DIRECTORY.validate(self.value)
        row["source_observation"]["state"] = "pages-composition-source-declared"
        with self.assertRaises(ValueError):
            DIRECTORY.validate(self.value)
        self.value = DIRECTORY.build()
        self.row("hygiene")["dashboard"]["url"] = "https://identity.egohygiene.io/intelligence/"
        with self.assertRaises(ValueError):
            DIRECTORY.validate(self.value)
        for key, field, replacement in [("catalog", "sha256", "0" * 64),
                                         ("source_inventory", "revision", "0" * 40)]:
            self.value = DIRECTORY.build()
            self.value[key][field] = replacement
            with self.subTest(source=key), self.assertRaises(ValueError):
                DIRECTORY.validate(self.value)

    def test_plausible_receipt_replacements_and_third_publication_fail(self):
        publication = self.row("empathy")["dashboard"]["publication"]
        for field, replacement in [("sha256", "0" * 64), ("revision", "0" * 40),
                                    ("path", DIRECTORY.EVIDENCE["organization"][0])]:
            original = publication["evidence"][field]
            publication["evidence"][field] = replacement
            with self.subTest(field=field), self.assertRaises(ValueError):
                DIRECTORY.validate(self.value)
            publication["evidence"][field] = original
        publication["run_url"] = "https://github.com/egohygiene/empathy/actions/runs/1"
        with self.assertRaises(ValueError):
            DIRECTORY.validate(self.value)
        dashboard = copy.deepcopy(self.row(".github")["dashboard"])
        dashboard["url"] = "https://aether.egohygiene.io/intelligence/"
        dashboard["publication"]["run_url"] = "https://github.com/egohygiene/aether/actions/runs/43372599165"
        self.row("aether")["dashboard"] = dashboard
        with self.assertRaises(ValueError):
            DIRECTORY.validate(self.value)

    def test_failed_or_changed_publication_record_is_rejected(self):
        read = DIRECTORY.read
        for mutate in (
            lambda packet: packet["theme_refresh"]["actual_publication"].update(conclusion="failure"),
            lambda packet: packet["theme_refresh"]["actual_publication"]["hosted_receipt"].update(run_id="1"),
            lambda packet: packet["theme_refresh"]["actual_publication"]["hosted_receipt"].update(
                consumer_revision="0" * 40),
        ):
            def altered(path, sha):
                packet = read(path, sha)
                if path == DIRECTORY.EVIDENCE["organization"][0]:
                    mutate(packet)
                return packet
            with self.subTest(mutation=mutate), patch.object(DIRECTORY, "read", side_effect=altered):
                with self.assertRaises(ValueError):
                    DIRECTORY.build()


if __name__ == "__main__":
    unittest.main()
