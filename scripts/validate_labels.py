#!/usr/bin/env python3
"""Validate the organization label catalog and repository assignments."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / ".github/labels/catalog.v1.json"
REPOSITORIES_PATH = ROOT / ".github/labels/repositories.v1.json"
HEX_COLOR = re.compile(r"^[0-9a-f]{6}$")
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
REPOSITORY = re.compile(r"^egohygiene/[A-Za-z0-9._-]+$")

EXPECTED_OVERLAY_LABELS = {
    "☁️ aether",
    "♻️ refactor",
    "⚙️ infra",
    "⚡ dx",
    "✍️ writing",
    "🌍 domain",
    "🌐 website",
    "🌱 mindgarden",
    "🎥 video",
    "🎨 design",
    "🎬 dreamscape",
    "🎯 practice",
    "🎵 music",
    "🏗️ architecture",
    "🏛️ philosophy",
    "🐛 bug",
    "💰 funding",
    "📄 documentation",
    "📋 backlog",
    "📐 schema",
    "📖 magazine",
    "📚 article",
    "📝 publishing",
    "📣 marketing",
    "📦 package",
    "📱 flutter",
    "🔄 lifecycle",
    "🔌 plugin",
    "🔬 research",
    "🗺️ journey",
}
REQUIRED_CATEGORIES = {"priority", "type", "area", "coordination", "status"}
APPROVED_OVERLAY_DIGEST = (
    "b66b6e4ff8e0e1ffa36536633a3d82981bbfd78a61a80a9c4ba5a980e06c7038"
)


class ValidationError(ValueError):
    """Raised when a governed label document violates its contract."""


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON object while rejecting duplicate keys."""

    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValidationError(f"{path}: duplicate key {key!r}")
            result[key] = value
        return result

    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"{path}: {error}") from error
    if not isinstance(value, dict):
        raise ValidationError(f"{path}: root must be an object")
    return value


def require_keys(value: dict[str, Any], required: set[str], context: str) -> None:
    """Require an exact object shape."""

    actual = set(value)
    if actual != required:
        raise ValidationError(
            f"{context}: expected keys {sorted(required)}, got {sorted(actual)}"
        )


def validate_label(label: Any, context: str, *, universal: bool = False) -> str:
    """Validate one label and return its name."""

    if not isinstance(label, dict):
        raise ValidationError(f"{context}: label must be an object")
    keys = {"name", "description", "color", "category"} if universal else {
        "name",
        "description",
        "color",
    }
    require_keys(label, keys, context)
    name = label["name"]
    description = label["description"]
    color = label["color"]
    if not isinstance(name, str) or not 1 <= len(name) <= 50:
        raise ValidationError(f"{context}: name must contain 1 to 50 characters")
    if not isinstance(description, str) or not 1 <= len(description) <= 100:
        raise ValidationError(f"{context}: description must contain 1 to 100 characters")
    if not isinstance(color, str) or HEX_COLOR.fullmatch(color) is None:
        raise ValidationError(f"{context}: color must be six lowercase hexadecimal digits")
    if universal and label["category"] not in REQUIRED_CATEGORIES:
        raise ValidationError(f"{context}: unknown universal category {label['category']!r}")
    return name


def validate_catalog(catalog: dict[str, Any]) -> tuple[set[str], set[str]]:
    """Validate the canonical catalog and return label and overlay identifiers."""

    require_keys(
        catalog,
        {
            "$schema",
            "schema_version",
            "catalog_version",
            "owner",
            "defaults",
            "universal",
            "overlays",
            "deprecations",
        },
        "catalog",
    )
    if catalog["schema_version"] != 1:
        raise ValidationError("catalog: schema_version must be 1")
    if catalog["$schema"] != "./schema/catalog.v1.schema.json":
        raise ValidationError("catalog: $schema must reference the checked-in v1 schema")
    if not isinstance(catalog["catalog_version"], str) or SEMVER.fullmatch(
        catalog["catalog_version"]
    ) is None:
        raise ValidationError("catalog: catalog_version must be semantic versioning")
    if catalog["owner"] != "egohygiene/.github":
        raise ValidationError("catalog: owner must be egohygiene/.github")
    if catalog["defaults"] != {"required": True, "removal_policy": "retain"}:
        raise ValidationError("catalog: defaults must require universal labels and retain removals")

    universal = catalog["universal"]
    overlays = catalog["overlays"]
    if not isinstance(universal, list) or not universal:
        raise ValidationError("catalog: universal must be a non-empty array")
    if not isinstance(overlays, list) or not overlays:
        raise ValidationError("catalog: overlays must be a non-empty array")

    names: set[str] = set()
    categories: set[str] = set()
    for index, label in enumerate(universal):
        name = validate_label(label, f"catalog.universal[{index}]", universal=True)
        if name in names:
            raise ValidationError(f"catalog: duplicate label name {name!r}")
        names.add(name)
        categories.add(label["category"])
    if categories != REQUIRED_CATEGORIES:
        raise ValidationError(
            f"catalog: universal categories must be {sorted(REQUIRED_CATEGORIES)}"
        )

    overlay_ids: set[str] = set()
    overlay_names: set[str] = set()
    for overlay_index, overlay in enumerate(overlays):
        context = f"catalog.overlays[{overlay_index}]"
        if not isinstance(overlay, dict):
            raise ValidationError(f"{context}: overlay must be an object")
        require_keys(overlay, {"id", "description", "labels"}, context)
        overlay_id = overlay["id"]
        if not isinstance(overlay_id, str) or re.fullmatch(r"[a-z][a-z0-9-]*", overlay_id) is None:
            raise ValidationError(f"{context}: invalid overlay id")
        if overlay_id in overlay_ids:
            raise ValidationError(f"catalog: duplicate overlay id {overlay_id!r}")
        overlay_ids.add(overlay_id)
        if not isinstance(overlay["description"], str) or not overlay["description"]:
            raise ValidationError(f"{context}: description must be non-empty")
        if not isinstance(overlay["labels"], list) or not overlay["labels"]:
            raise ValidationError(f"{context}: labels must be a non-empty array")
        for label_index, label in enumerate(overlay["labels"]):
            name = validate_label(label, f"{context}.labels[{label_index}]")
            if name in names:
                raise ValidationError(f"catalog: duplicate label name {name!r}")
            names.add(name)
            overlay_names.add(name)

    if overlay_names != EXPECTED_OVERLAY_LABELS:
        missing = sorted(EXPECTED_OVERLAY_LABELS - overlay_names)
        unexpected = sorted(overlay_names - EXPECTED_OVERLAY_LABELS)
        raise ValidationError(
            f"catalog: approved overlay catalog mismatch; missing={missing}, unexpected={unexpected}"
        )
    approved_rows = sorted(
        (label["name"], label["description"], label["color"])
        for overlay in overlays
        for label in overlay["labels"]
    )
    approved_digest = hashlib.sha256(
        json.dumps(
            approved_rows, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()
    if approved_digest != APPROVED_OVERLAY_DIGEST:
        raise ValidationError(
            "catalog: approved overlay names, descriptions, or colors changed"
        )
    deprecations = catalog["deprecations"]
    if not isinstance(deprecations, list):
        raise ValidationError("catalog: deprecations must be an array")
    deprecated_names: set[str] = set()
    for index, deprecation in enumerate(deprecations):
        context = f"catalog.deprecations[{index}]"
        if not isinstance(deprecation, dict):
            raise ValidationError(f"{context}: deprecation must be an object")
        require_keys(deprecation, {"name", "replacement", "remove_after"}, context)
        name = deprecation["name"]
        replacement = deprecation["replacement"]
        if not isinstance(name, str):
            raise ValidationError(f"{context}: name must be a string")
        if replacement is not None and not isinstance(replacement, str):
            raise ValidationError(f"{context}: replacement must be a string or null")
        if name not in names:
            raise ValidationError(f"{context}: deprecated label must remain in the catalog")
        if name in deprecated_names:
            raise ValidationError(f"{context}: label is deprecated more than once")
        deprecated_names.add(name)
        if replacement is not None and replacement not in names:
            raise ValidationError(f"{context}: replacement must name a catalog label")
        if replacement == name:
            raise ValidationError(f"{context}: replacement must differ from the deprecated label")
        try:
            date.fromisoformat(deprecation["remove_after"])
        except (TypeError, ValueError) as error:
            raise ValidationError(f"{context}: remove_after must be an ISO date") from error
    return names, overlay_ids


def validate_repositories(
    assignments: dict[str, Any], catalog: dict[str, Any], names: set[str], overlay_ids: set[str]
) -> None:
    """Validate repository assignments against the exact catalog version."""

    require_keys(
        assignments,
        {"$schema", "schema_version", "catalog_version", "repositories"},
        "repositories",
    )
    if assignments["schema_version"] != 1:
        raise ValidationError("repositories: schema_version must be 1")
    if assignments["$schema"] != "./schema/repositories.v1.schema.json":
        raise ValidationError("repositories: $schema must reference the checked-in v1 schema")
    if assignments["catalog_version"] != catalog["catalog_version"]:
        raise ValidationError("repositories: catalog_version must match the catalog")
    repositories = assignments["repositories"]
    if not isinstance(repositories, list) or not repositories:
        raise ValidationError("repositories: repositories must be a non-empty array")

    seen: set[str] = set()
    for index, assignment in enumerate(repositories):
        context = f"repositories.repositories[{index}]"
        if not isinstance(assignment, dict):
            raise ValidationError(f"{context}: assignment must be an object")
        require_keys(
            assignment,
            {"repository", "include_universal", "overlays", "additional_labels"},
            context,
        )
        repository = assignment["repository"]
        if not isinstance(repository, str) or REPOSITORY.fullmatch(repository) is None:
            raise ValidationError(f"{context}: invalid repository name")
        if repository in seen:
            raise ValidationError(f"repositories: duplicate repository {repository!r}")
        seen.add(repository)
        if assignment["include_universal"] is not True:
            raise ValidationError(f"{context}: universal taxonomy cannot be disabled")
        overlays = assignment["overlays"]
        if not isinstance(overlays, list) or any(not isinstance(item, str) for item in overlays):
            raise ValidationError(f"{context}: overlays must be an array of strings")
        if len(overlays) != len(set(overlays)):
            raise ValidationError(f"{context}: overlays must be unique")
        unknown = set(overlays) - overlay_ids
        if unknown:
            raise ValidationError(f"{context}: unknown overlays {sorted(unknown)}")
        additional = assignment["additional_labels"]
        if not isinstance(additional, list):
            raise ValidationError(f"{context}: additional_labels must be an array")
        local_names: set[str] = set()
        for label_index, label in enumerate(additional):
            name = validate_label(label, f"{context}.additional_labels[{label_index}]")
            if name in names or name in local_names:
                raise ValidationError(f"{context}: additional label collides with {name!r}")
            local_names.add(name)


def validate() -> None:
    """Validate all governed label documents."""

    catalog = load_json(CATALOG_PATH)
    assignments = load_json(REPOSITORIES_PATH)
    names, overlay_ids = validate_catalog(catalog)
    validate_repositories(assignments, catalog, names, overlay_ids)


def main() -> int:
    """Run validation and report one actionable diagnostic."""

    try:
        validate()
    except ValidationError as error:
        print(f"label contract invalid: {error}", file=sys.stderr)
        return 1
    print("label contract valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
