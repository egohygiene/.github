#!/usr/bin/env python3
"""Project the canonical label catalog for one configured repository."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_labels import (
    CATALOG_PATH,
    REPOSITORIES_PATH,
    ValidationError,
    load_json,
    validate_catalog,
    validate_repositories,
)


def project(repository: str) -> dict[str, Any]:
    """Return a deterministic, provider-neutral label projection."""

    catalog = load_json(CATALOG_PATH)
    assignments = load_json(REPOSITORIES_PATH)
    names, overlay_ids = validate_catalog(catalog)
    validate_repositories(assignments, catalog, names, overlay_ids)

    assignment = next(
        (item for item in assignments["repositories"] if item["repository"] == repository),
        None,
    )
    if assignment is None:
        raise ValidationError(f"repository {repository!r} has no governed assignment")

    selected_overlays = set(assignment["overlays"])
    labels = [
        {key: label[key] for key in ("name", "description", "color")}
        for label in catalog["universal"]
    ]
    for overlay in catalog["overlays"]:
        if overlay["id"] in selected_overlays:
            labels.extend(overlay["labels"])
    labels.extend(assignment["additional_labels"])
    labels.sort(key=lambda label: label["name"])
    return {
        "schema_version": 1,
        "catalog_version": catalog["catalog_version"],
        "repository": repository,
        "removal_policy": catalog["defaults"]["removal_policy"],
        "labels": labels,
    }


def main() -> int:
    """Parse arguments and write the JSON projection to stdout or a file."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True, help="Repository in owner/name form")
    parser.add_argument("--output", type=Path, help="Write to this path instead of stdout")
    arguments = parser.parse_args()
    try:
        payload = json.dumps(project(arguments.repository), ensure_ascii=False, indent=2) + "\n"
    except ValidationError as error:
        print(f"cannot project labels: {error}", file=sys.stderr)
        return 1
    if arguments.output is None:
        sys.stdout.write(payload)
    else:
        arguments.output.write_text(payload, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
