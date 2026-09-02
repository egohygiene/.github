from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from project_labels import project  # noqa: E402
from validate_labels import (  # noqa: E402
    CATALOG_PATH,
    REPOSITORIES_PATH,
    ValidationError,
    load_json,
    validate,
    validate_catalog,
    validate_repositories,
)


class LabelContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = load_json(CATALOG_PATH)
        self.repositories = load_json(REPOSITORIES_PATH)

    def test_checked_in_contract_is_valid(self) -> None:
        validate()

    def test_projection_matches_golden_consumer(self) -> None:
        expected = json.loads(
            (ROOT / "fixtures/labels/dot-github.expected.json").read_text(encoding="utf-8")
        )
        self.assertEqual(project("egohygiene/.github"), expected)

    def test_unknown_overlay_fails_closed(self) -> None:
        assignments = copy.deepcopy(self.repositories)
        assignments["repositories"][0]["overlays"].append("unknown")
        names, overlay_ids = validate_catalog(self.catalog)
        with self.assertRaisesRegex(ValidationError, "unknown overlays"):
            validate_repositories(assignments, self.catalog, names, overlay_ids)

    def test_repository_label_cannot_redefine_canonical_label(self) -> None:
        assignments = copy.deepcopy(self.repositories)
        assignments["repositories"][0]["additional_labels"].append(
            {"name": "ready", "description": "Different meaning", "color": "ffffff"}
        )
        names, overlay_ids = validate_catalog(self.catalog)
        with self.assertRaisesRegex(ValidationError, "collides"):
            validate_repositories(assignments, self.catalog, names, overlay_ids)

    def test_universal_taxonomy_cannot_be_disabled(self) -> None:
        assignments = copy.deepcopy(self.repositories)
        assignments["repositories"][0]["include_universal"] = False
        names, overlay_ids = validate_catalog(self.catalog)
        with self.assertRaisesRegex(ValidationError, "cannot be disabled"):
            validate_repositories(assignments, self.catalog, names, overlay_ids)

    def test_unapproved_catalog_change_fails(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["overlays"][0]["labels"].pop()
        with self.assertRaisesRegex(ValidationError, "approved overlay catalog mismatch"):
            validate_catalog(catalog)

    def test_approved_description_and_color_are_exact(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["overlays"][0]["labels"][0]["color"] = "ffffff"
        with self.assertRaisesRegex(ValidationError, "descriptions, or colors changed"):
            validate_catalog(catalog)

    def test_deprecation_must_reference_catalog_labels(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["deprecations"].append(
            {
                "name": "not-a-label",
                "replacement": "ready",
                "remove_after": "2027-01-01",
            }
        )
        with self.assertRaisesRegex(ValidationError, "must remain in the catalog"):
            validate_catalog(catalog)

    def test_missing_repository_assignment_fails_projection(self) -> None:
        with self.assertRaisesRegex(ValidationError, "no governed assignment"):
            project("egohygiene/not-configured")


if __name__ == "__main__":
    unittest.main()
