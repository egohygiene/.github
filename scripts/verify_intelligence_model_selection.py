#!/usr/bin/env python3
# Copyright 2026 Ego Hygiene
# SPDX-License-Identifier: MIT
"""Bind a separate public selection receipt to a Relay-verified review export.

This is a transport/presentation binding. It does not replay normalization,
execute producer JavaScript, authorize publication or authenticate human claims.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import stat
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_SHA256 = "c4e41df201500c5a00aa7b0e5e30cc4d8054f33eb39c842718266c70530175a9"
TARGET = {"origin": "https://egohygiene.github.io", "base_path": "/.github/"}
SHA = re.compile(r"[a-f0-9]{64}")
REVISION = re.compile(r"[a-f0-9]{40}")
MODULES = ("core", "audits", "sanity")
MAXIMUM = 262144


def require(value):
    if not value:
        raise ValueError("Model selection receipt binding denied")


def digest(content):
    return hashlib.sha256(content).hexdigest()


def local(value):
    path = Path(value).absolute()
    require(not any(item.is_symlink() for item in (path, *path.parents)))
    return path


def read(path):
    path = local(path)
    require(path.is_file() and 0 < path.stat().st_size <= MAXIMUM)
    content = path.read_bytes()
    require(0 < len(content) <= MAXIMUM)
    return content


def document(content):
    def unique(items):
        result = {}
        for key, value in items:
            require(key not in result)
            result[key] = value
        return result
    value = json.loads(content.decode("utf-8", errors="strict"), object_pairs_hook=unique,
                       parse_constant=lambda _: require(False))
    json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8", errors="strict")
    return value


def closed(value, keys):
    require(type(value) is dict and set(value) == set(keys))
    return value


def instant(value, provider=False):
    require(type(value) is str and re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z" if provider
            else r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value))
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(result.tzinfo == timezone.utc)
    return result


def public_names():
    raw = read(ROOT / "docs/intelligence/repositories.source.json")
    require(digest(raw) == INVENTORY_SHA256)
    inventory = document(raw)
    require(inventory["visibility"] == "public")
    return {row["repo"] for row in inventory["repositories"]
            if type(row) is dict and row.get("visibility") == "public"}


def verify(args):
    for value in (args.archive_sha256, args.receipt_sha256, args.manifest_sha256):
        require(SHA.fullmatch(value))
    require(REVISION.fullmatch(args.producer_commit))
    archive = read(args.archive)
    require(digest(archive) == args.archive_sha256)
    with zipfile.ZipFile(io.BytesIO(archive)) as source:
        entries = source.infolist()
        require(len(entries) == 1)
        entry = entries[0]
        mode = entry.external_attr >> 16
        require(entry.filename == "model-selection-receipt.json" and not entry.is_dir()
                and not entry.flag_bits & 1 and (not stat.S_IFMT(mode) or stat.S_ISREG(mode))
                and entry.compress_type in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}
                and 0 < entry.file_size <= 65536 and entry.compress_size > 0
                and entry.file_size <= max(65536, entry.compress_size * 256))
        with source.open(entry) as stream:
            raw = stream.read(65537)
        require(len(raw) == entry.file_size and digest(raw) == args.receipt_sha256)
    value = document(raw)
    # Reject a nonpublic receipt before inspecting source identities or counts.
    require(type(value) is dict and value.get("visibility") == "public")
    closed(value, {"schema", "contract_version", "visibility", "publication", "producer", "target",
                   "evaluated_at", "export_manifest_sha256", "modules"})
    require(value["schema"] == "egohygiene.website.organization-intelligence-model-selection-receipt/v1"
            and value["contract_version"] == "1.0.0-alpha.1" and value["publication"] == "review-only"
            and value["target"] == TARGET)
    expected_producer = {"repository": "egohygiene/egohygiene.io", "revision": args.producer_commit}
    require(value["producer"] == expected_producer and value["export_manifest_sha256"] == args.manifest_sha256)
    manifest_raw = read(args.export_manifest)
    require(digest(manifest_raw) == args.manifest_sha256)
    manifest = document(manifest_raw)
    require(manifest["producer"] == expected_producer and manifest["target"] == TARGET
            and manifest["as_of"] == value["evaluated_at"])
    evaluated = instant(value["evaluated_at"])
    for path in (args.export_artifact_metadata, args.selection_artifact_metadata):
        require(evaluated <= instant(document(read(path))["created_at"], provider=True))
    allowed = public_names()
    closed(value["modules"], MODULES)
    for module in MODULES:
        record = closed(value["modules"][module], {"state", "code", "source_as_of", "source", "presentation_sha256", "presentation_state"})
        require(record["state"] in {"available", "partial", "unavailable", "stale", "incompatible"})
        require(record["presentation_state"] in {"available", "partial", "stale", "unavailable", "incompatible", "error"})
        admitted = record["state"] in {"available", "partial"}
        model = manifest["models"][module]
        require((model["state"] == "available") == admitted
                and record["presentation_sha256"] == model["presentation_sha256"])
        if admitted:
            provenance = record["source"]
            require(type(provenance) is dict and provenance.get("repository") in allowed)
            closed(provenance, {"repository", "revision", "workflow_path", "run_id", "run_attempt"})
            require(REVISION.fullmatch(provenance["revision"])
                    and re.fullmatch(r"\.github/workflows/[A-Za-z0-9][A-Za-z0-9._-]*\.ya?ml", provenance["workflow_path"])
                    and type(provenance["run_id"]) is int and 1 <= provenance["run_id"] <= 9007199254740991
                    and type(provenance["run_attempt"]) is int and 1 <= provenance["run_attempt"] <= 1000000
                    and SHA.fullmatch(record["presentation_sha256"])
                    and instant(record["source_as_of"]) <= evaluated
                    and record["code"] == ("NONE" if record["state"] == "available" else "PARTIAL"))
        else:
            codes = {"unavailable": {"NOT_CONFIGURED", "INPUT_UNAVAILABLE"}, "stale": {"INPUT_STALE"},
                     "incompatible": {"INPUT_INCOMPATIBLE", "OWNER_INPUT_DENIED"}}
            require(record["code"] in codes[record["state"]] and record["source_as_of"] is None
                    and record["source"] is None and record["presentation_sha256"] is None)
    output = local(args.output)
    require(output.parent.is_dir() and not output.exists())
    with output.open("xb") as destination:
        destination.write(raw)
    output.chmod(0o600)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("archive", "archive-sha256", "receipt-sha256", "manifest-sha256", "producer-commit", "export-manifest",
                 "export-artifact-metadata", "selection-artifact-metadata", "output"):
        parser.add_argument("--" + name, required=True)
    try:
        verify(parser.parse_args())
    except Exception:
        print("Public model selection receipt denied; deployment remains disabled", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
