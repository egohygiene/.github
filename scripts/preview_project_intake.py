#!/usr/bin/env python3
"""Preview missing public issue membership in Ego Hygiene Project 1; never write."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import tempfile
from urllib.parse import urlencode

OWNER = "egohygiene"
PROJECT = 1
MAX_RESPONSE = 16 * 1024 * 1024
QUERY = """query($owner:String!, $number:Int!, $cursor:String) {
  organization(login:$owner) { projectV2(number:$number) {
    id number title closed url
    items(first:100, after:$cursor) {
      nodes { id isArchived content {
        __typename ... on Issue { id number url state repository { nameWithOwner visibility } }
      } }
      pageInfo { hasNextPage endCursor }
    }
  } }
}"""


class IntakeError(ValueError):
    """A bounded failure that cannot be treated as a membership decision."""


def require(condition, code):
    if not condition:
        raise IntakeError(code)


def document(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "DUPLICATE_PROVIDER_FIELD")
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_constant=lambda _: require(False, "NONFINITE_PROVIDER_VALUE"))


class GitHub:
    """Fixed-host read-only GitHub transport; GraphQL uses only a query operation."""
    def request(self, endpoint, payload=None):
        command = ["gh", "api", "--hostname", "github.com", "--method", "GET", endpoint]
        if payload is not None:
            require(endpoint == "graphql" and payload["query"] == QUERY, "QUERY_NOT_ALLOWED")
            command = ["gh", "api", "--hostname", "github.com", "--method", "POST", "graphql", "--input", "-"]
        environment = os.environ.copy()
        environment.update(GH_HOST="github.com", GH_PROMPT_DISABLED="1", GH_PAGER="cat")
        try:
            # Spool provider bytes rather than accumulating unbounded captured stdout.
            with tempfile.TemporaryFile() as output:
                def limit_output():
                    resource.setrlimit(resource.RLIMIT_FSIZE, (MAX_RESPONSE, MAX_RESPONSE))
                result = subprocess.run(command, input=None if payload is None else json.dumps(payload).encode(),
                    stdout=output, stderr=subprocess.DEVNULL, env=environment, timeout=60, check=False,
                    preexec_fn=limit_output)
                require(result.returncode == 0, "PROVIDER_ACCESS_RATE_OR_TRANSPORT_FAILURE")
                require(0 < output.tell() <= MAX_RESPONSE, "PROVIDER_RESPONSE_SIZE")
                output.seek(0)
                return document(output.read(MAX_RESPONSE + 1))
        except (OSError, subprocess.TimeoutExpired, UnicodeError, json.JSONDecodeError) as error:
            raise IntakeError("PROVIDER_RESPONSE_UNAVAILABLE") from error


def pages(client, endpoint, maximum):
    """Walk every REST page until an explicit short page, rejecting truncation."""
    for page in range(1, maximum + 1):
        separator = "&" if "?" in endpoint else "?"
        batch = client.request(endpoint + separator + urlencode({"per_page": 100, "page": page}))
        require(type(batch) is list and len(batch) <= 100, "REST_PAGE_INVALID")
        yield from batch
        if len(batch) < 100:
            return
    raise IntakeError("REST_PAGINATION_LIMIT")


def project_membership(client, maximum):
    cursor = None
    cursors = set()
    membership = {}
    project = None
    for _ in range(maximum):
        response = client.request("graphql", {"query": QUERY,
            "variables": {"owner": OWNER, "number": PROJECT, "cursor": cursor}})
        require(type(response) is dict and not response.get("errors"), "PROJECT_QUERY_FAILURE")
        try:
            current = response["data"]["organization"]["projectV2"]
            require(type(current) is dict and type(current["number"]) is int and current["number"] == PROJECT and current["closed"] is False,
                    "PROJECT_NOT_AVAILABLE")
            identity = {key: current[key] for key in ("id", "number", "title", "url")}
            require(type(identity["id"]) is str and bool(identity["id"])
                    and identity["url"] == "https://github.com/orgs/egohygiene/projects/1", "PROJECT_IDENTITY_INVALID")
            require(project is None or project == identity, "PROJECT_CHANGED_DURING_READ")
            project = identity
            connection = current["items"]
            require(type(connection["nodes"]) is list and len(connection["nodes"]) <= 100, "PROJECT_PAGE_INVALID")
            for item in connection["nodes"]:
                require(type(item) is dict and type(item["id"]) is str, "PROJECT_ITEM_INVALID")
                content = item.get("content")
                # Draft, redacted, inaccessible and private content supplies no public identity/count.
                if (type(content) is not dict or content.get("__typename") != "Issue"
                        or type(content.get("repository")) is not dict
                        or content["repository"].get("visibility") != "PUBLIC"):
                    continue
                full_name = content["repository"].get("nameWithOwner")
                if not valid_repository(full_name):
                    continue
                url = issue_url(full_name, content.get("number"))
                require(content.get("url") == url and type(content.get("id")) is str and bool(content["id"]), "PROJECT_ISSUE_IDENTITY_INVALID")
                record = membership.setdefault(url, {"node_id": content["id"], "items": set()})
                require(record["node_id"] == content["id"], "PROJECT_ISSUE_IDENTITY_CHANGED")
                require(item["id"] not in record["items"], "PROJECT_REPEATED_PAGE_ITEM")
                record["items"].add(item["id"])
            info = connection["pageInfo"]
            require(type(info["hasNextPage"]) is bool, "PROJECT_PAGE_INFO_INVALID")
            if not info["hasNextPage"]:
                return project, membership
            cursor = info["endCursor"]
            require(type(cursor) is str and bool(cursor) and cursor not in cursors, "PROJECT_CURSOR_INVALID")
            cursors.add(cursor)
        except (KeyError, TypeError) as error:
            raise IntakeError("PROJECT_RESPONSE_INVALID") from error
    raise IntakeError("PROJECT_PAGINATION_LIMIT")


def valid_repository(value):
    return (type(value) is str and re.fullmatch(r"egohygiene/[A-Za-z0-9_.-]+", value) is not None
            and value.split("/")[1] not in {".", ".."})


def issue_url(repository, number):
    require(valid_repository(repository) and type(number) is int and number > 0, "ISSUE_IDENTITY_INVALID")
    return f"https://github.com/{repository}/issues/{number}"


def preview(client, maximum=1000):
    """Require complete accessible-public inventory before an actionable preview."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    report = {"schema": "egohygiene.organization-project-intake-preview/v1", "mode": "read-only",
        "observed_at": now, "scope": {"owner": OWNER, "visibility": "public", "state": "open",
        "project_number": PROJECT, "maximum_pages_per_connection": maximum,
        "completeness": "accessible-public-repositories-only"}, "complete": False,
        "project": None, "repositories": [], "summary": {}, "errors": [], "writes": 0}
    try:
        require(type(maximum) is int and 1 <= maximum <= 10000, "INVALID_PAGE_BUDGET")
        project, membership = project_membership(client, maximum)
        report["project"] = project
        admitted = {}
        for repo in pages(client, "/orgs/egohygiene/repos?type=public&sort=full_name&direction=asc", maximum):
            require(type(repo) is dict, "REPOSITORY_RESPONSE_INVALID")
            if repo.get("private") is not False or repo.get("visibility") != "public":
                continue
            name = repo.get("full_name")
            require(valid_repository(name) and type(repo.get("id")) is int, "REPOSITORY_IDENTITY_INVALID")
            require(name not in admitted, "REPEATED_REPOSITORY")
            admitted[name] = repo
        for name in sorted(admitted):
            row = {"repository": name, "state": "complete", "issues": [], "errors": []}
            report["repositories"].append(row)
            seen = set()
            try:
                for issue in pages(client, f"/repos/{name}/issues?state=open&sort=created&direction=asc", maximum):
                    require(type(issue) is dict, "ISSUE_RESPONSE_INVALID")
                    if "pull_request" in issue:
                        continue
                    require(issue.get("state") == "open" and type(issue.get("node_id")) is str and bool(issue["node_id"]), "ISSUE_RESPONSE_INVALID")
                    url = issue_url(name, issue.get("number"))
                    require(issue.get("html_url") == url and url not in seen, "ISSUE_DUPLICATE_OR_INVALID_URL")
                    seen.add(url)
                    member = membership.get(url)
                    require(member is None or member["node_id"] == issue["node_id"], "ISSUE_IDENTITY_CHANGED")
                    count = 0 if member is None else len(member["items"])
                    row["issues"].append({"url": url, "node_id": issue["node_id"],
                        "membership": "missing" if count == 0 else "existing" if count == 1 else "duplicate",
                        "proposed_action": "add-with-backlog-after-reviewed-apply" if count == 0 else "leave-unchanged"})
                row["issues"].sort(key=lambda item: item["url"])
            except IntakeError as error:
                row["state"] = "incomplete"
                row["errors"].append(str(error))
        report["complete"] = all(row["state"] == "complete" for row in report["repositories"])
    except IntakeError as error:
        report["errors"].append(str(error))
    counts = {key: 0 for key in ("missing", "existing", "duplicate")}
    for row in report["repositories"]:
        for issue in row["issues"]:
            counts[issue["membership"]] += 1
    report["summary"] = {**counts, "repositories_complete": sum(row["state"] == "complete" for row in report["repositories"]),
        "repositories_incomplete": sum(row["state"] != "complete" for row in report["repositories"])}
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-pages", type=int, default=1000)
    parser.add_argument("--output", type=Path, help="New local JSON file; defaults to stdout")
    args = parser.parse_args(argv)
    try:
        result = preview(GitHub(), args.max_pages)
        content = json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2) + "\n"
        if args.output is None:
            sys.stdout.write(content)
        else:
            # Existing paths and symlinks are never overwritten.
            with args.output.open("x", encoding="utf-8") as destination:
                destination.write(content)
        return 0 if result["complete"] else 1
    except (OSError, ValueError):
        print("Project intake preview unavailable; no writes performed", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
