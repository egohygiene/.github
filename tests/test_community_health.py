"""Owned default-file and form contracts; hosted inheritance is separate."""
import hashlib
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class CommunityHealthTests(unittest.TestCase):
    def test_adopted_default_paths_and_explicit_deferrals(self):
        for name in ("CONTRIBUTING.md", "SUPPORT.md", "SECURITY.md", ".github/FUNDING.yml", ".github/PULL_REQUEST_TEMPLATE.md"):
            self.assertTrue((ROOT / name).is_file(), name)
        decisions = (ROOT / "docs/community-health.md").read_text()
        for name in ("Code of conduct", "Accessibility policy", "Private vulnerability form", "Discussion category forms"):
            self.assertRegex(decisions, re.escape(name) + r"[^\n]+Defer")
        self.assertFalse((ROOT / "CODE_OF_CONDUCT.md").exists())
        self.assertNotIn("GOVERNANCE.md | Adopt", decisions)

    def test_funding_move_preserves_exact_original_bytes(self):
        content = (ROOT / ".github/FUNDING.yml").read_bytes()
        self.assertEqual(hashlib.sha256(content).hexdigest(), "8df3d664dfab0b0e7a6bdbfc7772c8db94df77cc286bd9bebb89f69b1e067205")
        self.assertFalse((ROOT / "FUNDING.yml").exists())

    def test_every_type_form_uses_canonical_title_label_and_required_fields(self):
        title = json.loads((ROOT / ".github/issues/title-contract.v1.json").read_text())
        authoring = json.loads((ROOT / ".github/issues/authoring.v1.json").read_text())
        forms = [json.loads(p.read_text()) for p in (ROOT / ".github/ISSUE_TEMPLATE").glob("organization-*.yml")]
        by_label = {row["label"]: row for row in title["types"]}
        ordinary = [form for form in forms if form["name"] != "Organization checkpoint"]
        self.assertEqual({form["labels"][0] for form in ordinary}, set(by_label))
        for form in forms:
            self.assertEqual(len(form["labels"]), 1)
            row = by_label[form["labels"][0]]
            self.assertTrue(form["title"].startswith(f'{row["emoji"]} [{row["type"]}] '))
            fields = {field["id"]: field for field in form["body"] if "id" in field}
            required = authoring["required_fields"] + (authoring["checkpoint_required_fields"] if form["name"] == "Organization checkpoint" else [])
            for name in required:
                self.assertTrue(fields[name]["validations"]["required"], name)

    def test_api_examples_follow_the_same_contract(self):
        examples = json.loads((ROOT / "fixtures/issue-authoring/examples.v1.json").read_text())["examples"]
        contract = json.loads((ROOT / ".github/issues/authoring.v1.json").read_text())
        mapping = json.loads((ROOT / ".github/issues/title-contract.v1.json").read_text())["types"]
        for example in examples:
            row = next(row for row in mapping if row["label"] == example["labels"][0])
            self.assertTrue(example["title"].startswith(f'{row["emoji"]} [{row["type"]}] '))
            required = contract["required_fields"] + (contract["checkpoint_required_fields"] if example["kind"] == "checkpoint" else [])
            self.assertTrue(all(example["fields"][name] for name in required))

    def test_new_markdown_local_links_resolve(self):
        names = ["CONTRIBUTING.md", "SUPPORT.md", "SECURITY.md", "docs/community-health.md", "docs/issue-authoring.md", ".github/PULL_REQUEST_TEMPLATE.md"]
        for name in names:
            document = ROOT / name
            for raw in re.findall(r"\[[^]]*\]\(([^)]+)\)", document.read_text()):
                destination = raw.split("#", 1)[0]
                if not destination or destination.startswith(("https:", "http:", "mailto:")):
                    continue
                self.assertTrue((document.parent / unquote(destination)).is_file(), (name, destination))
