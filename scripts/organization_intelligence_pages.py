#!/usr/bin/env python3
"""Repository-owned Pages handoff for an unchanged, owner-verified export.

Relay owns static export validation; Hygiene owns surface declarations. This
adapter selects their exact sources, authenticates a retained review artifact,
and owns this repository's publication/recovery boundary only.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
TARGET = {"origin": "https://egohygiene.github.io", "base_path": "/.github/"}
PUBLICATION = "organization-intelligence-publication.json"
MAXIMUM = 80 * 1024 * 1024
HEX40 = re.compile(r"[a-f0-9]{40}")
HEX64 = re.compile(r"[a-f0-9]{64}")
DENIED = "Organization Intelligence Pages admission denied"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, destination):
        return None


def urlopen(request, *, timeout):
    return build_opener(NoRedirect()).open(request, timeout=timeout)


def require(value):
    if not value:
        raise ValueError(DENIED)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()


def document(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result)
            result[key] = value
        return result
    return json.loads(raw.decode("utf-8", errors="strict"), object_pairs_hook=pairs,
                      parse_constant=lambda _: require(False))


def closed(value, keys):
    require(type(value) is dict and set(value) == set(keys))
    return value


def local(value):
    path = Path(value).absolute()
    require(".." not in path.parts and ".git" not in path.parts
            and all(not part.is_symlink() for part in (path, *path.parents)))
    return path


def relative(value):
    require(type(value) is str and re.fullmatch(r"[A-Za-z0-9_.-][A-Za-z0-9._/-]{0,239}", value)
            and all(part not in {"", ".", "..", ".git"} for part in value.split("/")))
    return value


def read(path, maximum=1024 * 1024):
    path = local(path)
    require(path.is_file() and 0 < path.stat().st_size <= maximum)
    raw = path.read_bytes()
    require(0 < len(raw) <= maximum)
    return raw


def write(path, raw):
    path = local(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with path.open("xb") as target:
        target.write(raw)
    path.chmod(0o600)


def instant(value):
    require(type(value) is str and re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,7})?Z", value))
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def source_revision(source):
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, timeout=10, text=True).strip()
    require(HEX40.fullmatch(head) and not subprocess.check_output(
        ["git", "--no-optional-locks", "status", "--porcelain", "--untracked-files=all"], cwd=source, timeout=10))
    return head


def owner_source(path, selected, module_name, entry):
    path = local(path)
    require(source_revision(path) == selected["revision"])
    require(type(selected["files"]) is dict and selected["files"])
    for name, expected in selected["files"].items():
        require(HEX64.fullmatch(expected) and digest(read(path / relative(name), MAXIMUM)) == expected)
    require(entry in selected["files"])
    spec = importlib.util.spec_from_file_location(module_name, path / entry)
    module = importlib.util.module_from_spec(spec)
    # The Hygiene helper imports its separately hash-bound HTTPS primitives.
    sys.path.insert(0, str(path / "tools"))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


def selection(path, expected):
    path = local(path)
    require(ROOT in path.parents and HEX64.fullmatch(expected))
    raw = read(path, 65536)
    require(digest(raw) == expected)
    value = closed(document(raw), {"schema", "target", "review", "owners", "declaration", "assessment_at"})
    require(value["schema"] == "egohygiene.github.organization-intelligence-pages-selection/v1"
            and value["target"] == TARGET and instant(value["assessment_at"]) <= datetime.now(timezone.utc))
    review = closed(value["review"], {"run_id", "run_attempt", "consumer_revision", "artifact_id", "archive_sha256",
        "manifest_sha256", "producer_revision", "intake_receipt_sha256", "selection_receipt_sha256"})
    for key in ("run_id", "run_attempt", "artifact_id"):
        require(type(review[key]) is int and 1 <= review[key] <= 9007199254740991)
    for key in ("consumer_revision", "producer_revision"):
        require(HEX40.fullmatch(review[key]))
    for key in ("archive_sha256", "manifest_sha256", "intake_receipt_sha256", "selection_receipt_sha256"):
        require(HEX64.fullmatch(review[key]))
    owners = closed(value["owners"], {"relay", "hygiene"})
    for owner in owners.values():
        closed(owner, {"revision", "files"})
        require(HEX40.fullmatch(owner["revision"]))
    declaration = closed(value["declaration"], {"path", "sha256"})
    require(HEX64.fullmatch(declaration["sha256"]))
    relative(declaration["path"])
    return value


def acquire(work, selected):
    transport = work / "transport"
    transport.mkdir(mode=0o700)
    environment = {"PATH": os.environ.get("PATH", ""), "GH_TOKEN": os.environ.get("GH_TOKEN", ""),
        "GH_HOST": "github.com", "GH_PROMPT_DISABLED": "1", "GH_PAGER": "cat", "LANG": "C.UTF-8",
        "GH_CONFIG_DIR": str(work / "gh-config"), "XDG_STATE_HOME": str(work / "gh-state")}
    for key in ("HTTPS_PROXY", "HTTP_PROXY", "ALL_PROXY", "NO_PROXY", "https_proxy", "http_proxy",
                "all_proxy", "no_proxy", "SSL_CERT_FILE", "SSL_CERT_DIR", "REQUESTS_CA_BUNDLE",
                "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS"):
        if key in os.environ:
            environment[key] = os.environ[key]
    def capture(endpoint, name):
        path = transport / name
        def limit():
            resource.setrlimit(resource.RLIMIT_FSIZE, (MAXIMUM, MAXIMUM))
        with path.open("xb") as output:
            subprocess.run(["gh", "api", "--hostname", "github.com", "--method", "GET", endpoint],
                stdout=output, stderr=subprocess.DEVNULL, env=environment, check=True, timeout=90, preexec_fn=limit)
        return read(path, MAXIMUM)
    prefix = "/repos/egohygiene/.github"
    repository = document(capture(prefix, "repository.json"))
    require(repository.get("full_name") == "egohygiene/.github" and repository.get("private") is False
            and repository.get("visibility") == "public" and repository.get("default_branch") == "main")
    run = document(capture(prefix + f"/actions/runs/{selected['run_id']}/attempts/{selected['run_attempt']}", "run.json"))
    require(run.get("id") == selected["run_id"] and run.get("run_attempt") == selected["run_attempt"]
            and run.get("head_sha") == selected["consumer_revision"] and run.get("head_branch") == "main"
            and run.get("head_repository", {}).get("full_name") == "egohygiene/.github"
            and run.get("event") == "workflow_dispatch" and run.get("status") == "completed"
            and run.get("conclusion") == "success" and run.get("path") == ".github/workflows/organization-intelligence-review.yml")
    artifact = document(capture(prefix + f"/actions/artifacts/{selected['artifact_id']}", "artifact.json"))
    require(artifact.get("id") == selected["artifact_id"] and artifact.get("expired") is False
            and artifact.get("name") == f"organization-intelligence-review-{selected['run_id']}-{selected['run_attempt']}"
            and artifact.get("digest") == "sha256:" + selected["archive_sha256"]
            and artifact.get("workflow_run", {}).get("id") == selected["run_id"]
            and artifact.get("workflow_run", {}).get("head_sha") == selected["consumer_revision"]
            and type(artifact.get("size_in_bytes")) is int and 0 < artifact["size_in_bytes"] <= MAXIMUM)
    now = datetime.now(timezone.utc)
    require(instant(run["run_started_at"]) <= instant(artifact["created_at"]) <= instant(run["updated_at"]) <= now
            and instant(artifact["expires_at"]) > now)
    raw = capture(prefix + f"/actions/artifacts/{selected['artifact_id']}/zip", "review.zip")
    require(len(raw) == artifact["size_in_bytes"] and digest(raw) == selected["archive_sha256"])
    return transport / "review.zip"


def prepare(args):
    value = selection(args.selection, args.selection_sha256)
    revision = source_revision(ROOT)
    output = local(args.output)
    require(ROOT not in output.parents and output not in ROOT.parents and output != ROOT
            and output.parent.is_dir() and not output.exists())
    relay = owner_source(args.relay_source, value["owners"]["relay"], "pages_relay_intake",
                         "actions/repository-intelligence-static-intake/scripts/static_intake.py")
    hygiene = owner_source(args.hygiene_source, value["owners"]["hygiene"], "pages_hygiene_surfaces", "tools/organization_hosting.py")
    declaration_raw = read(ROOT / value["declaration"]["path"])
    require(digest(declaration_raw) == value["declaration"]["sha256"])
    declaration = document(declaration_raw)
    registry = hygiene.load_json(Path(args.hygiene_source) / "catalog/public-site-surface-registry.json")
    require(not hygiene.validate_registry(registry) and not hygiene.validate_declaration(
        declaration, registry, expected_registry_revision=value["owners"]["hygiene"]["revision"]))
    require(declaration["synthetic"] is False and declaration["site"]["id"] == "egohygiene/.github"
        and declaration["site"]["publication_repository"] == "egohygiene/.github"
        and declaration["site"]["origin"] == TARGET["origin"] and declaration["site"]["base_path"] == TARGET["base_path"]
        and declaration["site"]["route_profile"] == "organization" and declaration["site"]["visibility"] == "public")
    output.mkdir(mode=0o700)
    archive = local(args.review_archive) if args.review_archive else acquire(output, value["review"])
    files, directories = relay.input_archive(archive, value["review"]["archive_sha256"])
    for name, key in (("intake-receipt.json", "intake_receipt_sha256"), ("model-selection-receipt.json", "selection_receipt_sha256")):
        require(name in files and digest(files[name]) == value["review"][key])
        del files[name]
    manifest, _ = relay.validate(files, directories, manifest_sha256=value["review"]["manifest_sha256"],
        producer_commit=value["review"]["producer_revision"], target_origin=TARGET["origin"], target_base=TARGET["base_path"])
    paths = {row["path"] for row in manifest["routes"]}
    implemented = set()
    for row in declaration["surfaces"]:
        if row["publication"]["implementation_state"] == "implemented":
            require(row["canonical_route"] in paths and all(alias in paths for alias in row["aliases"]))
            require(row["publication"]["publication_state"] == "unpublished")
            require(row["renderer"]["version"] == value["review"]["producer_revision"])
            implemented.add(row["canonical_route"])
    require(paths <= implemented | {alias for row in declaration["surfaces"] for alias in row["aliases"]})
    require(source_revision(ROOT) == revision)
    # Producer bytes stay exact. Consumer-owned metadata is a separate file.
    for name, raw in files.items():
        if name.startswith("site/"):
            write(output / name, raw)
    publication = {"schema": "egohygiene.github.organization-intelligence-pages/v1", "target": TARGET,
        "consumer_revision": revision, "review": value["review"], "owners": value["owners"],
        "declaration_sha256": value["declaration"]["sha256"], "files": manifest["files"],
        "routes": manifest["routes"], "export_as_of": manifest["as_of"],
        "acquisition": "local-unverified" if args.review_archive else "github-read-only"}
    write(output / "site" / PUBLICATION, encoded(publication))
    write(output / "publication.json", encoded(publication))
    write(output / "export-manifest.json", files["export-manifest.json"])
    write(output / "declaration.json", declaration_raw)
    write(output / "selection.json", read(args.selection, 65536))
    print("Organization Intelligence site and declaration verified; no deployment performed")


def publication(site, *, deployable=False):
    site = local(site)
    value = closed(document(read(site / PUBLICATION)), {"schema", "target", "consumer_revision", "review", "owners",
        "declaration_sha256", "files", "routes", "export_as_of", "acquisition"})
    require(value["schema"] == "egohygiene.github.organization-intelligence-pages/v1" and value["target"] == TARGET
            and HEX40.fullmatch(value["consumer_revision"]) and value["acquisition"] in {"github-read-only", "local-unverified"})
    if deployable:
        require(value["acquisition"] == "github-read-only")
    names = set()
    total = 0
    require(type(value["files"]) is list and 1 <= len(value["files"]) <= 256)
    for row in value["files"]:
        closed(row, {"path", "sha256", "size_bytes"})
        name = relative(row["path"])
        require(name not in names and name not in {PUBLICATION, "CNAME"} and HEX64.fullmatch(row["sha256"])
                and type(row["size_bytes"]) is int and 0 <= row["size_bytes"] <= 16 * 1024 * 1024)
        names.add(name)
        total += row["size_bytes"]
    require(total <= 64 * 1024 * 1024)
    require(type(value["routes"]) is list and 1 <= len(value["routes"]) <= 256)
    route_files = set()
    for row in value["routes"]:
        closed(row, {"path", "canonical_path", "file", "id"})
        require(row["file"] in names and row["file"] not in route_files)
        route_files.add(row["file"])
        for key in ("path", "canonical_path"):
            route = row[key]
            require(type(route) is str and route.startswith("/") and route.endswith("/"))
            if route != "/":
                relative(route[1:-1])
    instant(value["export_as_of"])
    return value


def check(site, *, deployable=False):
    site = local(site)
    value = publication(site, deployable=deployable)
    expected = {row["path"] for row in value["files"]} | {PUBLICATION}
    actual = set()
    for path in site.rglob("*"):
        require(not path.is_symlink() and (path.is_dir() or path.is_file()))
        if path.is_file():
            actual.add(path.relative_to(site).as_posix())
    require(actual == expected)
    for row in value["files"]:
        path = local(site / row["path"])
        require(path.stat().st_size == row["size_bytes"])
        raw = path.read_bytes()
        require(len(raw) == row["size_bytes"] and digest(raw) == row["sha256"])
    return value


def checked_site(args):
    value = check(args.site, deployable=True)
    require(HEX64.fullmatch(args.publication_sha256) and HEX40.fullmatch(args.consumer_revision)
        and digest(read(local(args.site) / PUBLICATION)) == args.publication_sha256
        and value["consumer_revision"] == args.consumer_revision)
    return value


def public_file(value, name):
    # Request canonical directory URLs; Pages may redirect index.html spellings.
    return next((row["path"].lstrip("/") for row in value["routes"] if row["file"] == name), name)


def remote(path, *, missing=False):
    url = TARGET["origin"] + TARGET["base_path"] + path
    request = Request(url, headers={"User-Agent": "egohygiene-organization-intelligence-pages/1"})
    try:
        with urlopen(request, timeout=20) as response:
            require(response.geturl() == url and response.status == 200)
            raw = response.read(16 * 1024 * 1024 + 1)
    except HTTPError as error:
        require(error.geturl() == url)
        if missing and error.code == 404:
            return None
        # GitHub serves the declared custom 404 file with a 404 status.
        require(path == "404.html" and error.code == 404)
        raw = error.read(16 * 1024 * 1024 + 1)
    require(len(raw) <= 16 * 1024 * 1024)
    return raw


def capture_recovery(args):
    # Validate the prospective exact site before any remote or write operation.
    checked_site(args)
    output = local(args.output)
    require(not output.exists() and output.parent.is_dir() and output != ROOT and ROOT not in output.parents)
    raw = remote(PUBLICATION, missing=True)
    if raw is None:
        require(remote("", missing=True) is None)
        write(output / "recovery.json", encoded({"state": "first-deployment", "prior_publication_sha256": None}))
        return
    # A prior public manifest is data: validate its closed target/inventory first.
    write(output / "site" / PUBLICATION, raw)
    previous = publication(output / "site", deployable=True)
    for row in previous["files"]:
        content = b"" if row["path"] == ".nojekyll" else remote(public_file(previous, row["path"]))
        require(len(content) == row["size_bytes"] and digest(content) == row["sha256"])
        write(output / "site" / row["path"], content)
    check(output / "site", deployable=True)
    write(output / "recovery.json", encoded({"state": "retained-prior-site", "prior_publication_sha256": digest(raw)}))


def verify_live(args):
    value = checked_site(args)
    expected = read(local(args.site) / PUBLICATION)
    require(remote(PUBLICATION) == expected)
    for row in value["files"]:
        if row["path"] != ".nojekyll":
            raw = remote(public_file(value, row["path"]))
            require(len(raw) == row["size_bytes"] and digest(raw) == row["sha256"])
    receipt = {"schema": "egohygiene.github.organization-intelligence-pages-verification/v1", "target": TARGET,
        "consumer_revision": value["consumer_revision"], "publication_sha256": digest(expected),
        "review": value["review"], "verified_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "run_id": os.environ.get("GITHUB_RUN_ID"), "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "recovery": document(read(local(args.recovery) / "recovery.json")), "file_count": len(value["files"])}
    write(local(args.output), encoded(receipt))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare_parser = commands.add_parser("prepare")
    for name in ("selection", "selection-sha256", "relay-source", "hygiene-source", "output"):
        prepare_parser.add_argument("--" + name, required=True)
    prepare_parser.add_argument("--review-archive")
    inspect_parser = commands.add_parser("inspect")
    inspect_parser.add_argument("--selection", required=True)
    inspect_parser.add_argument("--selection-sha256", required=True)
    inspect_parser.add_argument("--github-output", required=True)
    check_parser = commands.add_parser("check")
    check_parser.add_argument("--site", required=True)
    check_parser.add_argument("--publication-sha256", required=True)
    check_parser.add_argument("--consumer-revision", required=True)
    for command in ("capture-recovery", "verify-live"):
        child = commands.add_parser(command)
        child.add_argument("--site", required=True)
        child.add_argument("--publication-sha256", required=True)
        child.add_argument("--consumer-revision", required=True)
        child.add_argument("--output", required=True)
        if command == "verify-live":
            child.add_argument("--recovery", required=True)
    args = parser.parse_args()
    try:
        if args.command == "inspect":
            value = selection(args.selection, args.selection_sha256)
            with local(args.github_output).open("a", encoding="utf-8") as output:
                for owner in ("relay", "hygiene"):
                    output.write(owner + "-revision=" + value["owners"][owner]["revision"] + "\n")
        elif args.command == "check":
            checked_site(args)
        else:
            {"prepare": prepare, "capture-recovery": capture_recovery, "verify-live": verify_live}[args.command](args)
    except Exception:
        print(DENIED, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
