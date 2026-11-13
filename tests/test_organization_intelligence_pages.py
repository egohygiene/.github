"""Focused publisher boundaries; synthetic local data and mocked HTTPS only."""
import argparse
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("organization_pages", ROOT / "scripts/organization_intelligence_pages.py")
PAGES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PAGES)


class PagesBoundaries(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="organization-pages-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.site = self.root / "site"
        self.site.mkdir()
        self.body = b"<!doctype html><title>Synthetic publisher boundary</title>"
        self.value = {"schema": "egohygiene.github.organization-intelligence-pages/v1", "target": PAGES.TARGET,
            "consumer_revision": "a" * 40, "review": {}, "owners": {}, "declaration_sha256": "b" * 64,
            "files": [{"path": ".nojekyll", "sha256": PAGES.digest(b""), "size_bytes": 0},
                {"path": "index.html", "sha256": PAGES.digest(self.body), "size_bytes": len(self.body)}],
            "routes": [{"path": "/", "canonical_path": "/", "file": "index.html", "id": "home"}],
            "export_as_of": "2026-11-13T00:04:12Z", "acquisition": "github-read-only"}
        (self.site / "index.html").write_bytes(self.body)
        (self.site / ".nojekyll").write_bytes(b"")
        self.save()

    def save(self):
        self.raw = PAGES.encoded(self.value)
        (self.site / PAGES.PUBLICATION).write_bytes(self.raw)
        self.args = argparse.Namespace(site=str(self.site), publication_sha256=PAGES.digest(self.raw),
            consumer_revision="a" * 40, output=str(self.root / "recovery"))

    def test_clean_exact_handoff_binds_publication_and_consumer(self):
        self.assertEqual(PAGES.checked_site(self.args), self.value)
        self.args.consumer_revision = "c" * 40
        with self.assertRaises(ValueError):
            PAGES.checked_site(self.args)
        self.args.consumer_revision = "a" * 40
        self.args.publication_sha256 = "d" * 64
        with self.assertRaises(ValueError):
            PAGES.checked_site(self.args)

    def test_changed_missing_extra_and_symlink_files_fail(self):
        for state in ("changed", "missing", "extra", "symlink"):
            with self.subTest(state=state):
                path = self.site / "index.html"
                if state == "changed":
                    path.write_bytes(b"different")
                elif state == "missing":
                    path.unlink()
                elif state == "extra":
                    (self.site / "extra.txt").write_text("unexpected")
                else:
                    path.unlink()
                    path.symlink_to(self.site / ".nojekyll")
                with self.assertRaises((ValueError, OSError)):
                    PAGES.checked_site(self.args)
                if path.exists() or path.is_symlink():
                    path.unlink()
                path.write_bytes(self.body)
                (self.site / "extra.txt").unlink(missing_ok=True)

    def test_local_replay_and_domain_control_files_cannot_deploy(self):
        self.value["acquisition"] = "local-unverified"
        self.save()
        with self.assertRaises(ValueError):
            PAGES.checked_site(self.args)
        self.value["acquisition"] = "github-read-only"
        self.value["files"].append({"path": "CNAME", "sha256": PAGES.digest(b"example.invalid"), "size_bytes": 15})
        (self.site / "CNAME").write_bytes(b"example.invalid")
        self.save()
        with self.assertRaises(ValueError):
            PAGES.checked_site(self.args)

    def test_first_deployment_requires_both_manifest_and_root_missing(self):
        with patch.object(PAGES, "remote", side_effect=[None, b"existing unmanifested site"]):
            with self.assertRaises(ValueError):
                PAGES.capture_recovery(self.args)
        self.assertFalse(Path(self.args.output).exists())
        with patch.object(PAGES, "remote", side_effect=[None, None]):
            PAGES.capture_recovery(self.args)
        self.assertEqual(json.loads((Path(self.args.output) / "recovery.json").read_bytes()),
                         {"state": "first-deployment", "prior_publication_sha256": None})

    def test_replacement_recovery_requires_every_exact_prior_byte(self):
        def remote(path, **unused):
            return self.raw if path == PAGES.PUBLICATION else self.body
        with patch.object(PAGES, "remote", side_effect=remote):
            PAGES.capture_recovery(self.args)
        prior = Path(self.args.output) / "site"
        self.assertEqual(PAGES.check(prior, deployable=True), self.value)
        self.assertEqual((prior / "index.html").read_bytes(), self.body)

    def test_live_drift_writes_no_success_receipt(self):
        recovery = self.root / "prior"
        recovery.mkdir()
        (recovery / "recovery.json").write_bytes(PAGES.encoded({"state": "first-deployment", "prior_publication_sha256": None}))
        self.args.recovery = str(recovery)
        self.args.output = str(self.root / "live.json")
        with patch.object(PAGES, "remote", side_effect=[self.raw, b"drift"]):
            with self.assertRaises(ValueError):
                PAGES.verify_live(self.args)
        self.assertFalse(Path(self.args.output).exists())
        with patch.object(PAGES, "remote", side_effect=[self.raw, self.body]):
            PAGES.verify_live(self.args)
        receipt = json.loads(Path(self.args.output).read_bytes())
        self.assertEqual(receipt["consumer_revision"], "a" * 40)
        self.assertEqual(receipt["publication_sha256"], PAGES.digest(self.raw))
        self.assertEqual(receipt["recovery"]["state"], "first-deployment")

    def test_https_redirects_and_missing_non404_files_fail(self):
        class Response:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *unused): return False
            def geturl(self): return "https://example.invalid/elsewhere"
            def read(self, maximum): return b"redirected"
        with patch.object(PAGES, "urlopen", return_value=Response()):
            with self.assertRaises(ValueError):
                PAGES.remote("index.html")
        base = PAGES.TARGET["origin"] + PAGES.TARGET["base_path"]
        with patch.object(PAGES, "urlopen", side_effect=HTTPError(base + "asset.js", 404, "missing", {}, io.BytesIO(b"not found"))):
            with self.assertRaises(ValueError):
                PAGES.remote("asset.js")
        with patch.object(PAGES, "urlopen", side_effect=HTTPError(base + "404.html", 404, "custom", {}, io.BytesIO(b"custom 404"))):
            self.assertEqual(PAGES.remote("404.html"), b"custom 404")

    def test_duplicate_json_keys_and_unsafe_routes_fail(self):
        with self.assertRaises(ValueError):
            PAGES.document(b'{"target":1,"target":2}')
        self.value["routes"][0]["path"] = "/../outside/"
        self.save()
        with self.assertRaises(ValueError):
            PAGES.checked_site(self.args)


if __name__ == "__main__":
    unittest.main()
