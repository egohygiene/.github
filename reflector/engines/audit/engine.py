from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any



def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))



def _load_discovery_module(root_dir: Path):
    pass_path = root_dir / "reflector" / "passes" / "00_discovery" / "discovery.py"
    spec = spec_from_file_location("reflector_discovery_pass", pass_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load discovery pass")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module



def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")



def _organization_markdown(payload: dict[str, Any]) -> str:
    metadata = payload["metadata"]
    lines = [
        "# Organization Audit",
        "",
        f"- Organization: {payload['organization']['name']}",
        f"- Policy: {payload['policy']['name']}",
        f"- UTC Timestamp: {metadata['timestamp_utc']}",
        f"- Local Timestamp: {metadata['timestamp_local']}",
        "",
        "## Repositories",
    ]

    for repo in payload["repositories"]:
        lines.append(f"- {repo['name']}: docs={repo.get('documentation_quality', 'unknown')}, tech={', '.join(repo.get('detected_technologies', [])) or 'none'}")

    return "\n".join(lines) + "\n"



def run(spec_path: Path) -> Path:
    root_dir = Path.cwd()
    spec = _load_json(spec_path)
    policy_name = spec["enabled_policies"][0]
    policy_path = root_dir / "reflector" / "policies" / f"{policy_name}.policy.json"
    policy = _load_json(policy_path)

    now_utc = datetime.now(timezone.utc)
    now_local = datetime.now().astimezone()
    timestamp_folder = now_utc.strftime("%Y-%m-%dT%H%M%SZ")

    output_root = root_dir / spec["audit"]["output_root"] / timestamp_folder
    repositories_dir = output_root / "repositories"
    repositories_dir.mkdir(parents=True, exist_ok=True)

    discovery = _load_discovery_module(root_dir)

    repository_audits: list[dict[str, Any]] = []
    for repository in spec.get("repositories", []):
        audit = discovery.run(repository, root_dir)
        repository_audits.append(audit)

        safe_name = audit.get("safe_name", audit["name"]) or "repository"
        _write(repositories_dir / f"{safe_name}.audit.md", discovery.markdown_report(audit))
        _write(repositories_dir / f"{safe_name}.audit.json", discovery.json_report(audit))

    organization_payload = {
        "metadata": {
            "engine": spec["audit"]["engine"],
            "version": spec["audit"]["version"],
            "timestamp_utc": now_utc.isoformat(),
            "timestamp_local": now_local.isoformat(),
            "output_directory": str(output_root.relative_to(root_dir)),
            "passes": spec["audit"].get("passes", []),
            "read_only": True,
        },
        "organization": spec["organization"],
        "policy": policy,
        "repositories": repository_audits,
    }

    _write(output_root / "organization.audit.json", json.dumps(organization_payload, indent=2, sort_keys=True) + "\n")
    _write(output_root / "organization.audit.md", _organization_markdown(organization_payload))

    return output_root



def main() -> int:
    parser = argparse.ArgumentParser(description="Run Reflector organization audit")
    parser.add_argument(
        "--spec",
        default="reflector/specs/organization.spec",
        help="Path to organization specification",
    )
    args = parser.parse_args()

    output_path = run(Path(args.spec))
    print(f"audit generated: {output_path}")
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
