from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_MANIFEST_FILES = {
    "package.json": "node",
    "pyproject.toml": "python",
    "requirements.txt": "python",
    "setup.py": "python",
    "go.mod": "go",
    "Cargo.toml": "rust",
    "pom.xml": "java",
    "build.gradle": "java",
    "Gemfile": "ruby",
}



def _safe_name(name: str) -> str:
    return name.replace("/", "_")



def _find_files(repo_path: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo_path.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            files.append(path)
    return files



def _documentation_files(files: list[Path], repo_path: Path) -> list[str]:
    docs: list[str] = []
    for file in files:
        rel = file.relative_to(repo_path)
        name = rel.name.lower()
        if name.startswith("readme") or rel.parts[0].lower() == "docs":
            docs.append(str(rel))
    return sorted(docs)



def _project_manifests(files: list[Path], repo_path: Path) -> list[str]:
    manifests: list[str] = []
    for file in files:
        if file.name in _MANIFEST_FILES:
            manifests.append(str(file.relative_to(repo_path)))
    return sorted(manifests)



def _detected_technologies(manifests: list[str]) -> list[str]:
    technologies = {
        _MANIFEST_FILES[Path(manifest).name]
        for manifest in manifests
        if Path(manifest).name in _MANIFEST_FILES
    }
    return sorted(technologies)



def _documentation_quality(docs: list[str]) -> str:
    if any(Path(doc).name.lower().startswith("readme") for doc in docs) and len(docs) > 1:
        return "good"
    if docs:
        return "basic"
    return "limited"



def _github_metadata(repo_path: Path) -> dict[str, Any]:
    workflows = sorted(
        str(path.relative_to(repo_path))
        for path in repo_path.glob(".github/workflows/*")
        if path.is_file()
    )
    issue_templates = sorted(
        str(path.relative_to(repo_path))
        for path in repo_path.glob(".github/ISSUE_TEMPLATE/*")
        if path.is_file()
    )
    return {
        "workflows": workflows,
        "issue_templates": issue_templates,
    }



def run(repository: dict[str, Any], root_dir: Path) -> dict[str, Any]:
    repo_name = repository["name"]
    repo_path = (root_dir / repository["path"]).resolve()

    if not repo_path.exists():
        return {
            "name": repo_name,
            "path": repository["path"],
            "purpose": repository.get("purpose", ""),
            "exists": False,
            "error": "Repository path does not exist",
        }

    files = _find_files(repo_path)
    docs = _documentation_files(files, repo_path)
    manifests = _project_manifests(files, repo_path)
    technologies = _detected_technologies(manifests)
    github_metadata = _github_metadata(repo_path)

    top_level_dirs = sorted(
        path.name
        for path in repo_path.iterdir()
        if path.is_dir() and path.name != ".git"
    )

    architecture_observations = [
        "Repository appears to be organized with top-level directories: "
        + (", ".join(top_level_dirs) if top_level_dirs else "none"),
        "Discovery pass is read-only and did not modify repository content",
    ]

    strengths = []
    if docs:
        strengths.append("Documentation entry points are present")
    if technologies:
        strengths.append("Technology manifests were detected")

    questions = []
    if not docs:
        questions.append("Should this repository include a README or docs directory?")
    if not manifests:
        questions.append("Are project manifests intentionally absent for this repository type?")

    return {
        "name": repo_name,
        "safe_name": _safe_name(repo_name),
        "path": repository["path"],
        "purpose": repository.get("purpose", ""),
        "exists": True,
        "detected_technologies": technologies,
        "documentation_quality": _documentation_quality(docs),
        "documentation_files": docs,
        "project_manifests": manifests,
        "github_metadata": github_metadata,
        "primary_concepts": top_level_dirs,
        "architectural_observations": architecture_observations,
        "notable_strengths": strengths,
        "notable_questions": questions,
        "metrics": {
            "file_count": len(files),
            "documentation_count": len(docs),
            "manifest_count": len(manifests),
        },
    }



def markdown_report(audit: dict[str, Any]) -> str:
    lines = [
        f"# Repository Audit: {audit['name']}",
        "",
        f"- Purpose: {audit.get('purpose', '') or 'Not specified'}",
        f"- Path: {audit.get('path', '')}",
        f"- Documentation Quality: {audit.get('documentation_quality', 'unknown')}",
        f"- Detected Technologies: {', '.join(audit.get('detected_technologies', [])) or 'none'}",
        "",
        "## Primary Concepts",
    ]
    lines.extend(f"- {concept}" for concept in audit.get("primary_concepts", []))
    if not audit.get("primary_concepts"):
        lines.append("- none")

    lines.append("")
    lines.append("## Architectural Observations")
    lines.extend(f"- {item}" for item in audit.get("architectural_observations", []))

    lines.append("")
    lines.append("## Notable Strengths")
    lines.extend(f"- {item}" for item in audit.get("notable_strengths", []))
    if not audit.get("notable_strengths"):
        lines.append("- none")

    lines.append("")
    lines.append("## Notable Questions")
    lines.extend(f"- {item}" for item in audit.get("notable_questions", []))
    if not audit.get("notable_questions"):
        lines.append("- none")

    return "\n".join(lines) + "\n"



def json_report(audit: dict[str, Any]) -> str:
    return json.dumps(audit, indent=2, sort_keys=True) + "\n"
