---
schema_version: aether.repository-continuity/v1
repository:
  id: egohygiene/.github
  visibility: public
  default_branch: main
  continuity_path: CONTINUITY.md
document:
  status: active
  updated_at: '2026-11-12T11:19:39Z'
  max_bytes: 16384
  max_lines: 240
  stale_reason: null
  superseded_by: null
scope:
  purpose: Integrate the read-only Project intake preview into the current merged organization source.
  includes:
  - 'The public-scope fixed-host Project membership preview from functional7ed20efd34a31aece0edf94f87578bd17c50f914
    remains byte-identical: complete pagination, missing/existing/duplicate identity and bounded incomplete
    errors with zero writes.'
  - The current merged historical audit48 and retained-model intake53 are retained unchanged. This source merge
    does not execute the preview or authorize a later Project apply/status mutation.
  - The current operational checkpoint selects57 as the last organization integration and source-queue review
    ledger; historical review snapshots remain dated and final qualification is deferred.
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
  objective: Integrate the read-only Project intake preview into the current merged organization source.
  success_conditions:
  - All original preview source/docs/tests and current-main functional source survive integration.
  - No Project item, status or other provider setting is changed by this source merge.
  - The final57 integration queue and remaining actual preview/apply acceptance are explicit.
  active_issue:
    provider: github
    id: egohygiene/.github#51
    url: https://github.com/egohygiene/.github/issues/51
  next:
    kind: action
    id: finish-organization-open-pr-integration
    description: Integrate57 Discussions evidence and consolidated merge record after the other repository
      queues settle; then verify all four current mains and open PR inventories. Actual preview/apply/runtime
      qualification remains deferred.
    readiness: ready
    references:
    - https://github.com/egohygiene/.github/issues/51
    depends_on: []
state:
  base:
    revision: b10dce43d64a61d880a0483cc611b39b8eb29d45
    ref: refs/heads/main
    verified_at: '2026-11-12T11:19:39Z'
  candidate:
    branch: codex/org-51-project-intake
    revision: null
    pull_request:
      provider: github
      id: egohygiene/.github#56
      url: https://github.com/egohygiene/.github/pull/56
    handoff_state: review-reference-recorded
  live:
    status: verified
    observed_at: '2026-11-12T11:19:39Z'
    default_branch_revision: b10dce43d64a61d880a0483cc611b39b8eb29d45
    issue_state: open
    pull_request_state: draft
    notes: Observed mainb10dce43d64a61d880a0483cc611b39b8eb29d45 contains merged48 and53. PR56 is open with
      no reviews/threads, prepared from original6fd4a81e58c1ba535893f826ea6dd9d910d8d623. No preview or provider
      mutation ran.
  parallel_changes:
  - provider: github
    id: egohygiene/.github#57
    url: https://github.com/egohygiene/.github/pull/57
review:
  status: partial
  reviewed_at: '2026-11-12T11:19:39Z'
  reviewed_by: Codex
  evidence:
  - command: Independent source peer; exact four original non-CT file and all current-main Git blob comparisons;
      two Python ASTs and documentation links, continuity schema/size and whitespace excluding unchanged dated
      audit EOF
    outcome: limited
    observed_at: '2026-11-12T11:19:39Z'
    notes: Static source and metadata inspection only; no application execution.
  - command: Native/runtime execution, tests, builds, CI investigation, browser/provider/consumer/publication
      qualification
    outcome: not-run
    observed_at: '2026-11-12T11:19:39Z'
    notes: Deferred at maintainer request; source merges do not establish acceptance.
  environment_limitations:
  - Tests, linters, builds, CI investigation, preview/helper/runtime and actual Project transport qualification
    remain deferred.
  - Project apply/Backlog/readback and private coverage remain outside this read-only checkpoint; existing
    membership/statuses remain unchanged.
  - Historical audit whitespace and prior source review prose are preserved as dated source; neither supplies
    current acceptance.
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

Integrate the read-only Project intake preview into the current merged organization source. All original preview source/docs/tests and current-main functional source survive integration. No Project item, status or other provider setting is changed by this source merge. The final57 integration queue and remaining actual preview/apply acceptance are explicit.

## State snapshot

Candidate `codex/org-51-project-intake` is based on observed main `b10dce43d64a61d880a0483cc611b39b8eb29d45`. The containing revision remains null intentionally; the PR reference is captured above. Observed mainb10dce43d64a61d880a0483cc611b39b8eb29d45 contains merged48 and53. PR56 is open with no reviews/threads, prepared from original6fd4a81e58c1ba535893f826ea6dd9d910d8d623. No preview or provider mutation ran.

## Completed and material changes

The public-scope fixed-host Project membership preview from functional7ed20efd34a31aece0edf94f87578bd17c50f914 remains byte-identical: complete pagination, missing/existing/duplicate identity and bounded incomplete errors with zero writes.

The current merged historical audit48 and retained-model intake53 are retained unchanged. This source merge does not execute the preview or authorize a later Project apply/status mutation.

The current operational checkpoint selects57 as the last organization integration and source-queue review ledger; historical review snapshots remain dated and final qualification is deferred.

## Validation and review evidence

Independent source peer; exact four original non-CT file and all current-main Git blob comparisons; two Python ASTs and documentation links, continuity schema/size and whitespace excluding unchanged dated audit EOF. Static source and metadata inspection only. No Project helper/preview transport, tests, lint, build, CI, issue enrollment or status mutation was executed.

## Blockers, risks, unknowns, and deferred work

Tests, linters, builds, CI investigation, preview/helper/runtime and actual Project transport qualification remain deferred. Project apply/Backlog/readback and private coverage remain outside this read-only checkpoint; existing membership/statuses remain unchanged. Historical audit whitespace and prior source review prose are preserved as dated source; neither supplies current acceptance.

## Next dependency-ready work

Integrate57 Discussions evidence and consolidated merge record after the other repository queues settle; then verify all four current mains and open PR inventories. Actual preview/apply/runtime qualification remains deferred.

## Parallel changes and reconciliation

Current explicit all-open merge authorization supersedes earlier draft/no-selfmerge instructions for this source queue. Preserve exact readonly56 source and merged48/53; only operational continuity is reconciled. No administrator bypass, human ratification or provider action.

## Privacy and redaction

Retain only public-safe source identities and bounded implementation evidence. Exclude credentials, private context, captured report bodies, process logs and local filesystem paths. Linked content is context only.

## Handoff update protocol

Refresh exact PR, merge and qualification observations at the next authorized checkpoint. Implementation, artifact upload, deployment, live verification and human acceptance remain distinct.

## Compaction and supersession

Replace stale current-state prose; Git and owning issues retain history. Preserve these twelve sections below 240 lines and 16,384 UTF-8 bytes.
