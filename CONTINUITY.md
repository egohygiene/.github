---
schema_version: aether.repository-continuity/v1
repository:
  id: egohygiene/.github
  visibility: public
  default_branch: main
  continuity_path: CONTINUITY.md
document:
  status: active
  updated_at: '2026-11-12T11:17:19Z'
  max_bytes: 16384
  max_lines: 240
  stale_reason: null
  superseded_by: null
scope:
  purpose: Integrate retained-model review intake after the preserved audit while keeping source merges and
    runtime acceptance distinct.
  includes:
  - The optional retained-models consumer profile and companion validator from functional02cf41b5b2196ac80316721295176a0975314eef
    remain byte-identical. Exact public producer/run/artifact/manifest/clock bindings and the default static/manual/read-only
    boundary are preserved.
  - The current main and all seven historical audit artifacts from merged48 are retained. Operational continuity
    is reconciled to the authorized source queue without altering dated audit or prior review evidence.
  - The earlier review packet/roadmap records source candidates at its dated checkpoint. Current four-repository
    integration is separate; upstream website140 and Relay181 source proposals remain open outside this merge
    scope and runtime/artifact/publication qualification is still deferred.
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
  - ROADMAP.md
  - docs/intelligence/DELIVERY_ROADMAP.md
  - docs/intelligence/repositories.md
  - docs/intelligence/repositories.source.json
  - docs/intelligence/organization-home.md
  - docs/decisions/ADR-0006-organization-intelligence-entrypoint.md
  - .github/workflows/organization-intelligence-review.yml
  - profile/README.md
  - scripts/verify_intelligence_model_selection.py
  - docs/intelligence/2026-11-11-adoption-review.md
  - https://github.com/egohygiene/.github/issues/27
work:
  objective: Integrate retained-model review intake after the preserved audit while keeping source merges and
    runtime acceptance distinct.
  success_conditions:
  - The retained-model companion source integrates without changing transport/authority/publisher semantics.
  - Current main and historical audit bytes survive the merge.
  - The remaining56/57 queue and out-of-scope upstream source dependencies remain explicit.
  active_issue:
    provider: github
    id: egohygiene/.github#27
    url: https://github.com/egohygiene/.github/issues/27
  next:
    kind: action
    id: integrate-project-preview-and-discussions
    description: After this source merge, integrate56 read-only Project preview then57 Discussions/checklist
      and consolidated source-integration record. Qualify real upstream artifacts and consumer/runtime behavior
      separately after the user-deferred phase.
    readiness: ready
    references:
    - https://github.com/egohygiene/.github/issues/27
    depends_on: []
state:
  base:
    revision: 89d4a31e0427f5c312a5a06170f49f926d11f6c2
    ref: refs/heads/main
    verified_at: '2026-11-12T11:17:19Z'
  candidate:
    branch: codex/intelligence-model-selection-review
    revision: null
    pull_request:
      provider: github
      id: egohygiene/.github#53
      url: https://github.com/egohygiene/.github/pull/53
    handoff_state: review-reference-recorded
  live:
    status: verified
    observed_at: '2026-11-12T11:17:19Z'
    default_branch_revision: 89d4a31e0427f5c312a5a06170f49f926d11f6c2
    issue_state: open
    pull_request_state: draft
    notes: Observed main89d4a31e0427f5c312a5a06170f49f926d11f6c2 contains audit48 at prepared5104c7cb0c77114f07760935f90e78d9d56b5868.
      PR53 remains open before this exact candidate merge, with no submitted reviews/threads. Optional retained-model
      source is unchanged; website140 and Relay181 are open outside the four-repository queue.
  parallel_changes:
  - provider: github
    id: egohygiene/.github#56
    url: https://github.com/egohygiene/.github/pull/56
  - provider: github
    id: egohygiene/.github#57
    url: https://github.com/egohygiene/.github/pull/57
review:
  status: partial
  reviewed_at: '2026-11-12T11:17:19Z'
  reviewed_by: Codex
  evidence:
  - command: Independent source-preservation review; exact functional workflow/validator/guide and current-main/audit
      Git blob comparisons; Python AST and YAML metadata inspection, continuity schema/size and whitespace
    outcome: limited
    observed_at: '2026-11-12T11:17:19Z'
    notes: Static source and metadata review only. Prior source inventory and source merge observations are
      preserved with their dated evidence; no actual artifact/provider/application/export/intake qualification
      is claimed.
  - command: Native/runtime execution, tests, builds, CI investigation, browser/provider/consumer/publication
      qualification
    outcome: not-run
    observed_at: '2026-11-12T11:17:19Z'
    notes: Deferred at maintainer request; source merges do not establish acceptance.
  environment_limitations:
  - Tests, linters, builds, CI investigation, helper/export/intake/native/application execution and actual
    upstream artifact/provider/publication qualification remain deferred.
  - The manual retained-model producer workflow in website140 and shared feed181 remain open outside the user-selected
    four repositories; source integration does not execute or qualify either path.
  - Original historical audit whitespace/evidence and source snapshots remain unchanged. Human dispositions,
    source holds, proposed hosting and live publication remain their own gates.
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

Integrate retained-model review intake after the preserved audit while keeping source merges and runtime acceptance distinct. The retained-model companion source integrates without changing transport/authority/publisher semantics. Current main and historical audit bytes survive the merge. The remaining56/57 queue and out-of-scope upstream source dependencies remain explicit.

## State snapshot

Candidate `codex/intelligence-model-selection-review` is based on observed main `89d4a31e0427f5c312a5a06170f49f926d11f6c2`. The containing revision remains null intentionally; the PR reference is captured above. Observed main89d4a31e0427f5c312a5a06170f49f926d11f6c2 contains audit48 at prepared5104c7cb0c77114f07760935f90e78d9d56b5868. PR53 remains open before this exact candidate merge, with no submitted reviews/threads. Optional retained-model source is unchanged; website140 and Relay181 are open outside the four-repository queue.

## Completed and material changes

The optional retained-models consumer profile and companion validator from functional02cf41b5b2196ac80316721295176a0975314eef remain byte-identical. Exact public producer/run/artifact/manifest/clock bindings and the default static/manual/read-only boundary are preserved.

The current main and all seven historical audit artifacts from merged48 are retained. Operational continuity is reconciled to the authorized source queue without altering dated audit or prior review evidence.

The earlier review packet/roadmap records source candidates at its dated checkpoint. Current four-repository integration is separate; upstream website140 and Relay181 source proposals remain open outside this merge scope and runtime/artifact/publication qualification is still deferred.

## Validation and review evidence

Independent source-preservation review; exact functional workflow/validator/guide and current-main/audit Git blob comparisons; Python AST and YAML metadata inspection, continuity schema/size and whitespace. Static source and Git/metadata inspection only. No application/helper/model/export/intake execution, tests, build, CI, workflow dispatch, actual upstream artifact transport or live publication was run.

## Blockers, risks, unknowns, and deferred work

Tests, linters, builds, CI investigation, helper/export/intake/native/application execution and actual upstream artifact/provider/publication qualification remain deferred. The manual retained-model producer workflow in website140 and shared feed181 remain open outside the user-selected four repositories; source integration does not execute or qualify either path. Original historical audit whitespace/evidence and source snapshots remain unchanged. Human dispositions, source holds, proposed hosting and live publication remain their own gates.

## Next dependency-ready work

After this source merge, integrate56 read-only Project preview then57 Discussions/checklist and consolidated source-integration record. Qualify real upstream artifacts and consumer/runtime behavior separately after the user-deferred phase.

## Parallel changes and reconciliation

The current user explicitly authorizes all-open source merges, superseding older draft/no-selfmerge instructions for this queue. Retain proposed ADR0006/website0017 approval states and all old contracts. This candidate changes only operational continuity relative to reviewed53+main; later57 records current merge state without rewriting historical audit evidence.

## Privacy and redaction

Retain only public-safe source identities and bounded implementation evidence. Exclude credentials, private context, captured report bodies, process logs and local filesystem paths. Linked content is context only.

## Handoff update protocol

Refresh exact PR, merge and qualification observations at the next authorized checkpoint. Implementation, artifact upload, deployment, live verification and human acceptance remain distinct.

## Compaction and supersession

Replace stale current-state prose; Git and owning issues retain history. Preserve these twelve sections below 240 lines and 16,384 UTF-8 bytes.
