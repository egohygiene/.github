# Foundation readiness coordination checkpoint

Observed: 2026-09-25. This is a planning checkpoint, not a new
organization roadmap, contract, registry, or completion claim. Recheck mutable
GitHub evidence before resuming work.

## Authority and intended outcome

The current focus is a dependable repository foundation with clear ownership,
applicable shared files, reproducible validation, reviewed branding, and truthful
Repository Intelligence. Repository Intelligence is the first implementation
focus; its program remains [organization issue #30](https://github.com/egohygiene/.github/issues/30).

[Hygiene #43](https://github.com/egohygiene/hygiene/issues/43) owns the reusable
platform and downstream-consumer program. This checkpoint selects a bounded
readiness focus within existing work; it does not adopt every optional capability
in that program. [Hygiene #60](https://github.com/egohygiene/hygiene/issues/60)
still owns the pending canonical organization-roadmap and inheritance contract.
[Pace #25](https://github.com/egohygiene/pace/issues/25) owns the execution-focus
projection. Organization strategy, repository roadmaps, executable issues, and
observed delivery evidence keep their existing authority.

This document composes owner issues by reference. It does not duplicate their
acceptance criteria or declare a new schema. The current sequence is maintainer
preference, not an assertion that every later chunk is technically blocked by
every earlier chunk.

## Agreed chunks and current authorization

| Order | Chunk | Boundary and current state |
| --- | --- | --- |
| 1 | Reconcile roadmaps and handoffs | Authorized now. Refresh stale Intelligence parent/checkpoint claims and expose ownership conflicts; present documentation and tracker changes for review. |
| 2 | Inventory Actions execution | Authorized now, read-only. Record representative public workflow triggers, runner choices, local entry points, missing evidence, and cost uncertainty in the [execution inventory](actions-execution-inventory.md). |
| 3 | [Relay #106](https://github.com/egohygiene/relay/issues/106) | Proposed after review. Reconcile publication acceptance from exact canary evidence; preserve any unsatisfied criterion and the existing portability limitation. |
| 4 | [Relay #109](https://github.com/egohygiene/relay/issues/109) | Proposed after review. Repair checkout-name dependence and prove reproduction across differently named checkouts at identical declared inputs. |
| 5 | Local CI pilot | Proposed after review and environment inspection. Select a small applicable workflow and prove its documented local commands and supported `act` path. |

Stop after chunks 1 and 2 for maintainer review. This authorization does not
include workflow disabling, workflow dispatch, deployment, implementation of
chunks 3–5, consumer upgrades, or fleet changes.

After that review, the next three candidate actions are Relay #106, Relay #109,
and the local CI pilot in that order. Recheck readiness before each. Relay #106
must not report portability as proven while #109 remains unresolved; a limitation
is not automatically a new prerequisite or a satisfied acceptance criterion.

## Readiness boundaries

- Product features, speculative research, optional integrations, and unrelated
  product polish stay outside this foundation focus. Necessary infrastructure
  implementation remains with its owning platform repository.
- Apply a shared minimum plus repository-specific profiles and exceptions.
  File presence, meaningful conformance, released tooling, and fleet adoption
  are separate stages; no repository must adopt every available capability.
- Identity artwork is a manual creative lane. The maintainer generates and
  approves source assets; consumers adopt the existing Identity contracts and
  generated packages. Missing artwork remains explicit and does not block
  unrelated infrastructure work or become an invented approval.
- The Actions objective is no additional GitHub spending. Inventory eligibility,
  runner classes, usage/storage implications, and local alternatives before
  proposing execution changes. Public visibility alone is not a cost guarantee.
- Direct local checks, `act` execution, hosted checks, deployment, and live
  verification are distinct evidence stages. An unsupported or unavailable
  stage stays explicit; local success is not hosted-platform parity.
- The local pilot requires an inspected compatible runtime, Docker access where
  needed, a supported runner/action path, and safe credential boundaries. If
  unavailable, record the limitation and the runnable handoff without claiming
  that the workflow was exercised.
- Downstream organizations retain their own identity, intent, private inventory,
  and adoption decisions. Public coordination must not reveal private repository
  names, counts, identifiers, relationships, or private tracking links.

## Existing programs to reuse

| Concern | Existing owner and tracker |
| --- | --- |
| Repository Intelligence delivery | [Organization #30](https://github.com/egohygiene/.github/issues/30), [Relay #27](https://github.com/egohygiene/relay/issues/27), [Relay #33](https://github.com/egohygiene/relay/issues/33) |
| File contracts and pilot process | [Organization #32](https://github.com/egohygiene/.github/issues/32) |
| Intelligence fleet adoption | [Pace #13](https://github.com/egohygiene/pace/issues/13) |
| README presentation and approved assets | [Pace #14](https://github.com/egohygiene/pace/issues/14) |
| Continuity and agent guidance adoption | [Pace #26](https://github.com/egohygiene/pace/issues/26) |
| Accepted gitignore fleet adoption | [Pace #30](https://github.com/egohygiene/pace/issues/30) |
| Portable organization contract | [Hygiene #42](https://github.com/egohygiene/hygiene/issues/42) |
| Reusable platform and downstream proof | [Hygiene #43](https://github.com/egohygiene/hygiene/issues/43) |

These are coordination links, not additional prerequisites for every
Intelligence issue. Each owning program retains its scope and completion test.

## Unresolved registry ownership conflict

[Organization #42](https://github.com/egohygiene/.github/issues/42) proposes a
canonical registry, relationships, and organization roadmap under `.github`.
That proposal conflicts with accepted [local ADR-001](../DECISIONS.md),
[Hygiene ADR-0001](https://github.com/egohygiene/hygiene/blob/main/docs/decisions/ADR-0001-holistic-architecture-v0.1.md),
the existing Hygiene catalog, and Hygiene #60's roadmap boundary.

Preserve the useful requirements and reconcile them with the existing owners
before implementation. Do not create a competing registry or silently treat a
newer issue as superseding an accepted decision. Any intentional ownership move
requires a reviewed architectural decision. No such move is made here.

## Current handoff acceptance

The present checkpoint is ready for review when stale claims are tied to current
evidence, unresolved gates remain explicit, changed documentation passes its
applicable checks, and the bounded Actions inventory distinguishes observations
from unknowns. Report documentation, tracker updates, and validation separately.
This does not close the Intelligence program, declare fleet conformance, or
authorize the next implementation chunk. Resume through [CONTINUITY.md](../CONTINUITY.md).
