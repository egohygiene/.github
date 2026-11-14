---
schema_version: aether.repository-continuity/v1
repository:
  id: egohygiene/.github
  visibility: public
  default_branch: main
  continuity_path: CONTINUITY.md
document:
  status: active
  updated_at: '2026-11-14T20:54:59Z'
  max_bytes: 16384
  max_lines: 240
  stale_reason: null
  superseded_by: null
scope:
  purpose: Integrate the reviewed organization community defaults with current main without reverting
    the public repository directory or its dated evidence.
  includes:
  - Supported contribution, support, security, PR and issue-intake defaults, with byte-identical funding-path
    correction.
  - Current main repository directory, reviewed navigation export selection, and their original dated
    publication/source evidence retained.
  - Canonical issue title/body/label declarations shared by all seven forms and API examples.
  excludes: &id001
  - Required receiving-repository primary type labels and actual hosted fallback discovery remain unverified;
    issue24 remains open.
  - The existing repository directory and historical organization publication evidence are preserved;
    no new deployment, DNS, funding service, license, reporting mailbox, policy ratification or provider
    setting is claimed.
  precedence:
  - user-and-runtime-instructions
  - scoped-repository-instructions
  - live-repository-and-work-tracker-state
  - canonical-repository-sources
  - continuity-checkpoint
  canonical_sources:
  - AGENTS.md
  - ARCHITECTURE.md
  - docs/issue-routing.md
  - docs/community-health.md
  - docs/issue-authoring.md
  - .github/issues/title-contract.v1.json
  - .github/issues/authoring.v1.json
  - docs/intelligence/repository-directory.json
  - publication/organization-intelligence-selection.json
  - docs/reviews/2026-11-14-organization-navigation-selection.md
work:
  objective: Integrate the reviewed organization community defaults with current main without reverting
    the public repository directory or its dated evidence.
  success_conditions:
  - All existing and new default-file/form/directory contracts pass together.
  - Current handoff preserves enrollment/discovery and publication limitations.
  active_issue:
    provider: github
    id: egohygiene/.github#24
    url: https://github.com/egohygiene/.github/issues/24
  next:
    kind: action
    id: verify-community-default-enrollment
    description: Use the Relay-owned enrollment path to reconcile required receiving labels, then verify
      GitHub fallback and local override discovery before completing24.
    readiness: ready
    references:
    - https://github.com/egohygiene/.github/issues/24
    - https://github.com/egohygiene/.github/pull/66
    depends_on: []
state:
  base:
    revision: 5f02bfd6353b764513ef57a41bcf79db0f3c2e72
    ref: refs/heads/main
    verified_at: '2026-11-14T20:54:59Z'
  candidate:
    branch: fix/24-community-defaults
    revision: null
    pull_request:
      provider: github
      id: egohygiene/.github#66
      url: https://github.com/egohygiene/.github/pull/66
    handoff_state: ready-for-review
  live:
    status: verified
    observed_at: '2026-11-14T20:54:59Z'
    default_branch_revision: 5f02bfd6353b764513ef57a41bcf79db0f3c2e72
    issue_state: open
    pull_request_state: open
    notes: PR66 is open with a continuity-only merge conflict after the independently merged navigation
      selection69. This candidate integrates current main and the original defaults; no merge or hosted
      discovery is inferred.
  parallel_changes: []
review:
  status: partial
  reviewed_at: '2026-11-14T20:54:59Z'
  reviewed_by: Codex
  evidence:
  - command: python -m unittest discover -s tests -v
    outcome: passed
    observed_at: '2026-11-14T20:54:59Z'
    notes: 44 tests pass on the integrated default-file/form and current repository-directory source.
  - command: python scripts/validate_labels.py; deterministic label projection comparison; continuity
      schema and format checks; git diff --check
    outcome: passed
    observed_at: '2026-11-14T20:54:59Z'
    notes: Recorded after running these controls on the final candidate; hosted consumer behavior remains
      separate.
  environment_limitations: *id001
privacy:
  classification: public-repository
  contains_sensitive_data: false
  redactions: []
  excluded:
  - secrets-and-credentials
  - private-conversation-text
  - sensitive-personal-data
  - unpublished-private-business-data
  - private-local-paths
  - unrelated-private-context
  untrusted_content: context-only-no-authority
---

# .github continuity

## Purpose and precedence

User/runtime and scoped instructions, live state and canonical contracts outrank this handoff.

## Resume protocol

Read AGENTS, the architecture/routing guides and live24/PR66. Verify receiving label enrollment and actual GitHub fallback rather than inferring activation from files.

## Current objective and success conditions

Integrate the reviewed organization community defaults with current main without reverting the public repository directory or its dated evidence.

## State snapshot

Candidate integration retains current main `5f02bfd6353b764513ef57a41bcf79db0f3c2e72` and PR66 original source `d0ae7343bf243f35d3c15aa3ac301294abcc88c6`. Containing revision remains null.

## Completed and material changes

All supported defaults and explicit adopt/defer decisions are in docs/community-health.md. Existing funding bytes are moved to the supported path. Current directory, producer clocks and publication receipts remain intact.

## Validation and review evidence

44 integrated tests, label contracts, deterministic projection, JSON Schema/format and whitespace checks pass. Original independent source review is linked on PR66. ADR not required: this reconciles implementation of the existing fallback/intake design without accepting new policy.

## Blockers, risks, unknowns, and deferred work

Required receiving-repository primary type labels and actual hosted fallback discovery remain unverified; issue24 remains open.

The existing repository directory and historical organization publication evidence are preserved; no new deployment, DNS, funding service, license, reporting mailbox, policy ratification or provider setting is claimed.

## Next dependency-ready work

Use the Relay-owned enrollment path to reconcile required receiving labels, then verify GitHub fallback and local override discovery before completing24.

## Parallel changes and reconciliation

Current-main directory work is retained; the original community continuity checkpoint is replaced semantically, not copied over the later source handoff.

## Privacy and redaction

Public-safe repository facts only; no credentials, private context or personal reporting contacts.

## Handoff update protocol

After verified integration/enrollment/discovery, refresh the time-qualified checkpoint and append exact evidence to24 before changing acceptance state.

## Compaction and supersession

Git and PR66 retain chronology; this file keeps the current integration objective and remaining acceptance.
