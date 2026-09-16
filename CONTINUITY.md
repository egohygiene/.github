---
schema_version: aether.repository-continuity/v1
repository:
  id: egohygiene/.github
  visibility: public
  default_branch: main
  continuity_path: CONTINUITY.md
document:
  status: active
  updated_at: "2026-09-16T12:32:00Z"
  max_bytes: 16384
  max_lines: 240
  stale_reason: null
  superseded_by: null
scope:
  purpose: Preserve the minimum verified state needed to continue the Ego Hygiene Repository Intelligence and Organization Intelligence visual-control-plane program across chats.
  includes:
    - Primary visual-control-plane trackers and current dependency-ready execution state.
    - Organization-roadmap source/read-model/UI dependencies.
    - Current mock-reference intent and its non-canonical status.
    - Recently merged Repository Intelligence evidence relevant to the next checkpoint.
  excludes:
    - Conversation transcripts.
    - Full issue bodies or duplicated roadmap prose.
    - Private personal context.
    - UI-local domain semantics not accepted by the canonical owner.
  precedence:
    - user-and-runtime-instructions
    - live-github-state
    - canonical-roadmap-and-architecture-sources
    - accepted-contracts-and-adrs
    - continuity-checkpoint
  canonical_sources:
    - ARCHITECTURE.md
    - DECISIONS.md
    - ROADMAP.md
    - https://github.com/egohygiene/.github/issues/30
    - https://github.com/egohygiene/.github/issues/29
    - https://github.com/egohygiene/hygiene/issues/60
    - https://github.com/egohygiene/observatory/issues/22
work:
  objective: Converge Repository Intelligence into Organization Intelligence so a human can understand current work, roadmap, dependencies, decisions, health, and next outcomes without reconstructing the organization from chat history.
  primary_tracker:
    provider: github
    id: egohygiene/.github#30
    url: https://github.com/egohygiene/.github/issues/30
  organization_roadmap:
    ui_issue: egohygiene/.github#29
    canonical_contract_issue: egohygiene/hygiene#60
    normalized_read_model_issue: egohygiene/observatory#22
  current_mock:
    path: docs/intelligence/mockups/organization-roadmap-reference.svg
    status: design-reference-only
    rule: The mock may guide information architecture and visual hierarchy but never overrides canonical roadmap state or accepted read-model semantics.
state:
  base:
    ref: refs/heads/main
    revision: b415c8029bf2fb5d474f367e7129791588ba3860
    verified_at: "2026-09-16T12:32:00Z"
  candidate:
    branch: docs/organization-roadmap-mock-reference
    pull_request: null
    handoff_state: preparing-review
  live:
    status: verified
    observed_at: "2026-09-16T12:32:00Z"
    repository_intelligence:
      relay_dependencies_pr: egohygiene/relay#78
      relay_dependencies_state: merged
      relay_dependencies_merge_commit: 2480bd307f067b7d54f7661340a0b8b41fc1c750
    organization_roadmap_dependencies:
      hygiene_60: open
      observatory_22: open
      github_29: open
      github_30: open
review:
  status: active
  reviewed_at: "2026-09-16T12:32:00Z"
  reviewed_by: ChatGPT
  evidence:
    - command: Verify egohygiene/.github main and open PR state before creating the mock-reference branch.
      outcome: passed
      notes: No competing open pull request existed in egohygiene/.github when this checkpoint started.
    - command: Re-fetch .github#29, .github#30, hygiene#60, observatory#22, and relay#78.
      outcome: passed
      notes: Relay #78 is merged; the organization-roadmap contract/read-model/UI work remains open and correctly separated by ownership.
    - command: Add a versioned SVG roadmap mock and boundary README on a focused branch.
      outcome: passed
      notes: The mock explicitly states that it is a presentation reference and not canonical roadmap state.
  environment_limitations:
    - The mock is stored as text SVG because the connected GitHub contents API accepts UTF-8 text files; the original chat-generated PNG remains a local conversational artifact.
privacy:
  classification: public-repository
  contains_sensitive_data: false
  redactions: []
---

# Ego Hygiene visual-control-plane continuity

## Current direction

The program is converging on one evidence-backed visual system:

```text
canonical repository / organization sources
        ↓
Hygiene + Aether contracts
        ↓
Egolint / Relay / specialist evidence
        ↓
Observatory normalized read models
        ↓
Repository Intelligence
        ↓
Organization Intelligence
        ↓
GitHub issues / PRs / releases for execution
```

The design goal is not “more dashboards.” It is less working-memory burden: show what is active, blocked, stale, awaiting human judgment, and meaningfully next.

## Roadmap visualization north star

The checked-in mock compresses the current direction into two readable lanes:

1. **Reusable engine:** established foundations → Repository Intelligence → Organization Intelligence → continuous control loop.
2. **Creative proof:** Flow-suite hardening → orchestration proof → real comic/media releases → reuse by Incompris LLC and future creative products.

This is a visual north star only. Canonical roadmap strategy remains in organization/repository roadmap sources and tracked GitHub work.

## Current dependency truth

- Repository `/roadmap/`, `/now/`, `/decisions/`, `/journey/`, and `/dependencies/` foundations are materially further along; Relay #78 merged the dependency-impact slice.
- Organization `/roadmap/` must consume the canonical organization-roadmap contract from Hygiene #60 through Observatory #22.
- Do not implement organization strategy semantics directly in `.github` UI while those owner contracts remain open.
- Synthetic deterministic fixtures are acceptable for UI exploration once the upstream shape is sufficiently stable, but final integration must pin the accepted contract.

## Next execution rule

For each future chat or checkpoint:

1. Re-fetch `.github#30` and `.github#29` plus their live dependencies.
2. Re-fetch current Relay Repository Intelligence state before duplicating any route.
3. Choose one smallest dependency-ready visual checkpoint.
4. Implement one bounded issue / PR.
5. Reconcile roadmap, ADR impact, generated docs, and this continuity file before handoff.
6. Do not merge review PRs unless explicitly authorized.

## Resume target

After this mock-reference PR is reviewed, continue the control-plane roadmap from live evidence. If Hygiene #60 and Observatory #22 are still open, keep pushing dependency-ready Repository Intelligence/supporting surfaces or bounded Organization Intelligence shell work that does not invent roadmap semantics. Once both roadmap owner contracts are accepted, prioritize the real organization `/roadmap/` implementation described by `.github#29`.
