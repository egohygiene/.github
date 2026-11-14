---
schema_version: aether.repository-continuity/v1
repository:
  id: egohygiene/.github
  visibility: public
  default_branch: main
  continuity_path: CONTINUITY.md
document:
  status: active
  updated_at: '2026-11-14T04:19:35Z'
  max_bytes: 16384
  max_lines: 240
  stale_reason: null
  superseded_by: null
scope:
  purpose: Prepare supported organization community defaults and shared issue forms without claiming
    consumer enrollment.
  includes:
  - Add concise contribution, support, security and pull-request fallback guidance; record explicit
    supported-file adoption/deferral decisions.
  - Move the original funding bytes to the platform-required .github/FUNDING.yml path; canonical labels/titles
    remain unchanged.
  - Seven type/checkpoint forms and API examples share required fields. No historical issue migration,
    label provisioning, contact invention or governance approval occurs.
  excludes:
  - Actual provider label reads found only type:feature among required type labels; remaining labels
    need Relay-owned enrollment before activation. Hosted fallback and consumer discovery remain unverified.
    Code of conduct, accessibility, private vulnerability forms and Discussions are explicitly deferred.
  precedence:
  - user-and-runtime-instructions
  - scoped-repository-instructions
  - live-repository-and-work-tracker-state
  - canonical-repository-sources
  - continuity-checkpoint
  canonical_sources:
  - AGENTS.md
  - docs/community-health.md
  - docs/issue-authoring.md
  - .github/issues/authoring.v1.json
  - .github/ISSUE_TEMPLATE/organization-work.yml
  - .github/FUNDING.yml
  - https://github.com/egohygiene/.github/issues/24
work:
  objective: Prepare supported organization community defaults and shared issue forms without claiming
    consumer enrollment.
  success_conditions:
  - 33 tests pass; title/body/form consistency, funding identity, local links, defaults and existing
    contract suites pass. Official supported-file documentation was inspected.
  - Keep source checks distinct from provider, publication and human acceptance.
  active_issue:
    provider: github
    id: egohygiene/.github#24
    url: https://github.com/egohygiene/.github/issues/24
  next:
    kind: action
    id: review-24-checkpoint
    description: Review the bounded draft and exact evidence; preserve outstanding owner/provider gates
      before broader issue closeout.
    readiness: ready
    references:
    - https://github.com/egohygiene/.github/issues/24
    depends_on: []
state:
  base:
    revision: 876bae3d92e3a28b6d3b4e9d4ef4a640cef0a44f
    ref: refs/heads/main
    verified_at: '2026-11-14T04:19:35Z'
  candidate:
    branch: fix/24-community-defaults
    revision: null
    pull_request: null
    handoff_state: ready-for-review
  live:
    status: verified
    observed_at: '2026-11-14T04:19:35Z'
    default_branch_revision: 876bae3d92e3a28b6d3b4e9d4ef4a640cef0a44f
    issue_state: open
    pull_request_state: not-applicable
    notes: Live main and owner issue were inspected before implementation. This pre-PR candidate leaves
      its containing revision and provider reference null intentionally.
  parallel_changes: []
review:
  status: partial
  reviewed_at: '2026-11-14T04:19:35Z'
  reviewed_by: Codex
  evidence:
  - command: python3 -m unittest discover -s tests -v; python3 scripts/validate_labels.py
    outcome: passed
    observed_at: '2026-11-14T04:19:35Z'
    notes: 33 tests pass; title/body/form consistency, funding identity, local links, defaults and existing
      contract suites pass. Official supported-file documentation was inspected.
  environment_limitations:
  - Actual provider label reads found only type:feature among required type labels; remaining labels
    need Relay-owned enrollment before activation. Hosted fallback and consumer discovery remain unverified.
    Code of conduct, accessibility, private vulnerability forms and Discussions are explicitly deferred.
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

# org-community continuity

## Purpose and precedence

User/runtime and scoped instructions, live provider evidence and canonical sources outrank this snapshot. No additional authority is granted.

## Resume protocol

Read AGENTS, the linked owner issue and current target branch before continuing. Verify all mutable issue/PR claims.

## Current objective and success conditions

Prepare supported organization community defaults and shared issue forms without claiming consumer enrollment.

## State snapshot

Candidate `fix/24-community-defaults` starts at main `876bae3d92e3a28b6d3b4e9d4ef4a640cef0a44f`. Containing revision and pre-PR reference stay null intentionally.

## Completed and material changes

Add concise contribution, support, security and pull-request fallback guidance; record explicit supported-file adoption/deferral decisions.

Move the original funding bytes to the platform-required .github/FUNDING.yml path; canonical labels/titles remain unchanged.

Seven type/checkpoint forms and API examples share required fields. No historical issue migration, label provisioning, contact invention or governance approval occurs.

## Validation and review evidence

33 tests pass; title/body/form consistency, funding identity, local links, defaults and existing contract suites pass. Official supported-file documentation was inspected.

## Blockers, risks, unknowns, and deferred work

Actual provider label reads found only type:feature among required type labels; remaining labels need Relay-owned enrollment before activation. Hosted fallback and consumer discovery remain unverified. Code of conduct, accessibility, private vulnerability forms and Discussions are explicitly deferred.

## Next dependency-ready work

Independently review the draft, reconcile any new target changes and retain remaining gates in the owning issue.

## Parallel changes and reconciliation

Known native-v1 or publication work remains separately owned; this change neither merges nor activates another candidate.

## Privacy and redaction

Public source facts and synthetic fixtures only. No private exports, credentials, personal content or raw private paths belong in this handoff.

## Handoff update protocol

Record exact tested heads, actual checks, reviewer findings and provider outcomes before integration. Do not infer acceptance from source presence.

## Compaction and supersession

This replaces the previous active snapshot. Historical release/adoption evidence remains available through Git and its owning work records.
