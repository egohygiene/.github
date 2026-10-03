from __future__ import annotations

import json
import unittest
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / ".github/issues/title-contract.v1.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class IssueTitleContractTests(unittest.TestCase):
    """Check owned contract data; provider validation is implemented in Egolint."""

    @classmethod
    def setUpClass(cls):
        cls.contract = load(CONTRACT_PATH)
        cls.catalog = load(CONTRACT_PATH.parent / cls.contract["label_catalog"]["path"])
        cls.examples = load(CONTRACT_PATH.parent / cls.contract["conformance_examples"])
        cls.by_label = {row["label"]: row for row in cls.contract["types"]}

    def test_mapping_covers_exactly_the_universal_types(self):
        expected = {
            row["name"] for row in self.catalog["universal"] if row["category"] == "type"
        }
        self.assertEqual(set(self.by_label), expected)
        self.assertEqual(len(self.by_label), len(self.contract["types"]))
        self.assertEqual(len({row["type"] for row in self.by_label.values()}), len(expected))
        self.assertEqual(self.contract["label_catalog"]["version"], self.catalog["catalog_version"])
        for label, row in self.by_label.items():
            with self.subTest(label=label):
                self.assertEqual(label, "type:" + row["type"])
                self.assertTrue(row["emoji"])
                self.assertEqual(row["emoji"], row["emoji"].strip())

    def test_referenced_contract_files_exist(self):
        for key in ["$schema", "semantics", "conformance_examples"]:
            with self.subTest(reference=key):
                self.assertTrue((CONTRACT_PATH.parent / self.contract[key]).is_file())
        self.assertEqual(
            self.contract["$schema"], "./schema/title-contract.v1.schema.json"
        )

    def test_example_identity_and_required_outcomes(self):
        self.assertEqual(self.examples["contract_id"], self.contract["contract_id"])
        self.assertEqual(self.examples["contract_version"], self.contract["contract_version"])
        cases = self.examples["cases"]
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertEqual(
            {case["expected"]["status"] for case in cases},
            {"conformant", "nonconformant", "needs-classification", "conflict", "unsupported-type"},
        )
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertIsInstance(case["input"]["title"], str)
                self.assertTrue(all(isinstance(label, str) for label in case["input"]["labels"]))

    def test_conformant_examples_agree_with_the_mapping(self):
        covered = set()
        for case in self.examples["cases"]:
            if case["expected"]["status"] != "conformant":
                continue
            with self.subTest(case=case["id"]):
                primary = [
                    self.by_label[label] for label in set(case["input"]["labels"])
                    if label in self.by_label
                ]
                self.assertEqual(len(primary), 1)
                row = primary[0]
                covered.add(row["type"])
                self.assertEqual(case["expected"]["type"], row["type"])
                prefix = self.contract["format"].format(**row, subject="")
                title = case["input"]["title"]
                self.assertTrue(title.startswith(prefix))
                subject = title[len(prefix):]
                self.assertTrue(subject)
                self.assertEqual(subject, subject.strip())
                self.assertEqual(subject.splitlines(), [subject])
                # Re-rendering a valid example preserves its exact title.
                self.assertEqual(self.contract["format"].format(**row, subject=subject), title)
        self.assertEqual(covered, {row["type"] for row in self.by_label.values()})

    def test_reviewed_migration_examples_preserve_labels_and_identifiers(self):
        for case in self.examples["migrations"]:
            with self.subTest(case=case["id"]):
                self.assertEqual(case["before"]["labels"], case["after"]["labels"])
                primary = [label for label in case["after"]["labels"] if label in self.by_label]
                self.assertEqual(len(primary), 1)
                row = self.by_label[primary[0]]
                self.assertEqual(
                    self.contract["format"].format(**row, subject=case["reviewed_subject"]),
                    case["after"]["title"],
                )
                self.assertIn(case["reviewed_subject"], case["before"]["title"])
        no_op = next(case for case in self.examples["migrations"] if case["id"] == "already-conformant-no-op")
        self.assertEqual(no_op["before"], no_op["after"])

    @unittest.skipIf(Draft202012Validator is None, "JSON Schema engine unavailable; full schema execution deferred")
    def test_full_contract_json_schema(self):
        schema = load(CONTRACT_PATH.parent / self.contract["$schema"])
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(self.contract)


if __name__ == "__main__":
    unittest.main()
