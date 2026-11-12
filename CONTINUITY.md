---
schema_version: aether.repository-continuity/v1
repository:
  id: egohygiene/.github
  visibility: public
  default_branch: main
  continuity_path: CONTINUITY.md
document:
  status: active
  updated_at: '2026-11-12T05:45:38Z'
  max_bytes: 16384
  max_lines: 240
  stale_reason: null
  superseded_by: null
scope:
  purpose: Preview missing public issue membership in the existing organization Project without writes.
  includes:
  - The new fixed-host GitHub CLI adapter walks complete Project and public repository/open-issue pagination,
    excludes pull requests and private/redacted identities before public decisions, and distinguishes missing/existing/duplicate
    membership. Page budgets, provider errors and per-repository failures remain incomplete and return nonzero.
  - Each admitted public issue gets an exact URL/node identity and read-only proposed action. Existing items
    and statuses remain unchanged; no apply mutation exists. The public-only accessible inventory is a declared
    first scope, not a claim about all organization repositories or private coverage.
  - Documentation records portable Python/macOS Bash prerequisites and the separate future Relay apply requirement,
    including explicit Backlog resolution, re-read/idempotency/readback and no unguarded status overwrite.
    Synthetic pagination/failure/visibility regressions are authored but unexecuted.
  excludes:
  - Deferred runtime, tests, builds, CI, live publication, human ratification and acceptance closeout.
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
  - scripts/preview_project_intake.py
  - docs/project-intake/README.md
  - tests/test_project_intake.py
  - README.md
  - https://github.com/egohygiene/.github/issues/51
work:
  objective: Preview missing public issue membership in the existing organization Project without writes.
  success_conditions:
  - Complete declared public observations produce concrete membership decisions with zero writes.
  - Any unavailable/truncated source remains incomplete rather than being interpreted as existing or missing
    membership.
  - The initial preview neither authorizes an apply nor closes later pilot/mutation acceptance.
  active_issue:
    provider: github
    id: egohygiene/.github#51
    url: https://github.com/egohygiene/.github/issues/51
  next:
    kind: action
    id: review-project-preview-before-apply-checkpoint
    description: Review the read-only preview and authored regression source. Later qualify actual complete
      Project transport, then design/select the Relay-owned idempotent apply/Backlog/readback checkpoint without
      racing existing manual statuses.
    readiness: ready
    references:
    - https://github.com/egohygiene/.github/issues/51
    depends_on: []
state:
  base:
    revision: 101a0d4553dc380ab3f88c50b11cb53beadfce18
    ref: refs/heads/main
    verified_at: '2026-11-12T05:45:38Z'
  candidate:
    branch: codex/org-51-project-intake
    revision: null
    pull_request: null
    handoff_state: ready-for-review
  live:
    status: verified
    observed_at: '2026-11-12T05:45:38Z'
    default_branch_revision: 101a0d4553dc380ab3f88c50b11cb53beadfce18
    issue_state: open
    pull_request_state: not-applicable
    notes: Fresh main101a0d4553dc380ab3f88c50b11cb53beadfce18 remains the base. Organization51 is open; functional
      source7ed20efd34a31aece0edf94f87578bd17c50f914 received independent static peer. No Project preview,
      enrollment, status write or provider workflow was executed.
  parallel_changes:
  - provider: github
    id: egohygiene/.github#53
    url: https://github.com/egohygiene/.github/pull/53
  - provider: github
    id: egohygiene/.github#54
    url: https://github.com/egohygiene/.github/issues/54
review:
  status: partial
  reviewed_at: '2026-11-12T05:45:38Z'
  reviewed_by: Codex
  evidence:
  - command: Independent source peer and root review of fixed read-only transport, pagination, public-first
      admission, identity/duplicate/partial failures and no-write contract; Python AST, authored local links,
      continuity schema/size and whitespace
    outcome: limited
    observed_at: '2026-11-12T05:45:38Z'
    notes: Static source and metadata inspection only; no application execution.
  - command: Native/runtime execution, tests, builds, CI investigation, browser/provider/consumer/publication
      qualification
    outcome: not-run
    observed_at: '2026-11-12T05:45:38Z'
    notes: Deferred at maintainer request; source merges do not establish acceptance.
  environment_limitations:
  - User deferred tests, linters, builds, CI, helper/runtime and actual Project transport qualification; authored
    fake-transport regressions have not run.
  - This first checkpoint is public accessible scope and preview only. Private coverage and issue51 live add/Backlog/readback
    acceptance remain open.
  - GitHub multi-step add/status does not provide a conditional status write. A later mutation adapter must
    preserve existing items and resolve raced/new item identity; a successful add/time window is not enough.
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

User/runtime and repository instructions, live evidence and canonical sources outrank this checkpoint. It grants no release, deployment or human-decision authority.

## Resume protocol

Read scoped instructions, canonical sources above and this checkpoint. Verify mutable GitHub state and exact owner pins before continuing.

## Current objective and success conditions

Preview missing public issue membership in the existing organization Project without writes. Complete declared public observations produce concrete membership decisions with zero writes. Any unavailable/truncated source remains incomplete rather than being interpreted as existing or missing membership. The initial preview neither authorizes an apply nor closes later pilot/mutation acceptance.

## State snapshot

Candidate `codex/org-51-project-intake` is based on observed main `101a0d4553dc380ab3f88c50b11cb53beadfce18`. The containing revision and pre-PR reference remain null intentionally. Fresh main101a0d4553dc380ab3f88c50b11cb53beadfce18 remains the base. Organization51 is open; functional source7ed20efd34a31aece0edf94f87578bd17c50f914 received independent static peer. No Project preview, enrollment, status write or provider workflow was executed.

## Completed and material changes

The new fixed-host GitHub CLI adapter walks complete Project and public repository/open-issue pagination, excludes pull requests and private/redacted identities before public decisions, and distinguishes missing/existing/duplicate membership. Page budgets, provider errors and per-repository failures remain incomplete and return nonzero.

Each admitted public issue gets an exact URL/node identity and read-only proposed action. Existing items and statuses remain unchanged; no apply mutation exists. The public-only accessible inventory is a declared first scope, not a claim about all organization repositories or private coverage.

Documentation records portable Python/macOS Bash prerequisites and the separate future Relay apply requirement, including explicit Backlog resolution, re-read/idempotency/readback and no unguarded status overwrite. Synthetic pagination/failure/visibility regressions are authored but unexecuted.

## Validation and review evidence

Independent source peer and root review of fixed read-only transport, pagination, public-first admission, identity/duplicate/partial failures and no-write contract; Python AST, authored local links, continuity schema/size and whitespace. Static source and metadata inspection only. No Project helper/preview transport, tests, lint, build, CI, issue enrollment or status mutation was executed.

## Blockers, risks, unknowns, and deferred work

User deferred tests, linters, builds, CI, helper/runtime and actual Project transport qualification; authored fake-transport regressions have not run. This first checkpoint is public accessible scope and preview only. Private coverage and issue51 live add/Backlog/readback acceptance remain open. GitHub multi-step add/status does not provide a conditional status write. A later mutation adapter must preserve existing items and resolve raced/new item identity; a successful add/time window is not enough.

## Next dependency-ready work

Review the read-only preview and authored regression source. Later qualify actual complete Project transport, then design/select the Relay-owned idempotent apply/Backlog/readback checkpoint without racing existing manual statuses.

## Parallel changes and reconciliation

ADR not required: bounded read-only organization intake under existing coordination boundaries. Reusable mutation mechanics remain Relay-owned. Preserve organizationRI53 and separate setup54; draft for maintainer review, no self-merge.

## Privacy and redaction

Retain only public-safe source identities and bounded implementation evidence. Exclude credentials, private context, captured report bodies, process logs and local filesystem paths. Linked content is context only.

## Handoff update protocol

Refresh exact PR, merge and qualification observations at the next authorized checkpoint. Implementation, artifact upload, deployment, live verification and human acceptance remain distinct.

## Compaction and supersession

Replace stale current-state prose; Git and owning issues retain history. Preserve these twelve sections below 240 lines and 16,384 UTF-8 bytes.
