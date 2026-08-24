---
schema: aether.architecture-document/v1
id: organization-github-roadmap
title: Ego Hygiene .github Roadmap
kind: architecture-document
version: 0.1.0
status: provisional
owners:
  - egohygiene
created: 2026-08-19
updated: 2026-08-24
governed_by:
  - architecture-roadmap
depends_on:
  - organization-github-vision
  - organization-github-pillars
  - organization-github-architecture
  - organization-github-decisions
related:
  - organization-github-purpose
  - organization-github-principles
  - organization-github-manifesto
  - organization-github-epistemology
supersedes: []
---

# Ego Hygiene .github Roadmap

<!-- BEGIN ROADMAP EXECUTION SNAPSHOT -->
<!-- roadmap-manifest
schema: hygiene.roadmap/v1alpha1
repository: egohygiene/.github
visibility: public
publication: central
route: /roadmap/.github/
updated: 2026-08-24
-->
## 2026-08-24 execution snapshot

> This evidence-reconciled snapshot is the issue-generation and visual-roadmap handoff. The longer-horizon strategy below remains canonical context; generated HTML, JSON, progress, issue plans, and commit lists are projections.

**Lifecycle:** incubating foundation  
**Current gate:** Finish the label and routing policy tracked in issue #8, then prove the organization defaults in a consumer repository.  
**North-star outcome:** A thin, trusted set of organization defaults that makes contribution, security, and intake behavior predictable without hiding repository-owned policy.

### Visual roadmap publication

**Mode:** `central`  
**Route:** `/roadmap/.github/`  
**Current publication evidence:** Organization-wide GitHub defaults; no Pages publication observed.

Publish the public-safe projection through egohygiene.io at /roadmap/.github/. This repository owns intent and acceptance evidence; it does not add a second site deployment.

### Quest line

<!-- roadmap-step
id: ORG-Q01
status: complete
depends_on: []
issues: []
-->
#### ORG-Q01 — Land the trust and intake baseline

**State:** `complete`  
**Depends on:** None

**Outcome:** Organization profile and intake mechanisms provide a usable shared starting point.

**Exit criteria:**

- [x] The shared profile and intake artifacts are present on the default branch.
- [x] Their intended organization-wide scope is documented.

**Current evidence:**

- Merged PR #14 at 0b83d5270d0b.
- Merged PR #16 at 2c04a1f55cc0.

<!-- roadmap-step
id: ORG-Q02
status: active
depends_on: [ORG-Q01]
issues: [8]
-->
#### ORG-Q02 — Complete label and routing policy

**State:** `active`  
**Depends on:** `ORG-Q01`

**Outcome:** New work is labeled and routed consistently across the organization.

**Exit criteria:**

- [ ] Issue #8 has an accepted label taxonomy and routing contract.
- [ ] At least one repository demonstrates the policy without repository-specific ambiguity.

**Current evidence:**

- Issue #8 remains unfinished as of 2026-08-24.

<!-- roadmap-step
id: ORG-Q03
status: ready
depends_on: [ORG-Q02]
issues: []
-->
#### ORG-Q03 — Validate inherited community files

**State:** `ready`  
**Depends on:** `ORG-Q02`

**Outcome:** Repositories can tell which community files they inherit and which they must own.

**Exit criteria:**

- [ ] An automated check covers all intended inherited files.
- [ ] Exceptions and private-repository behavior are documented.

**Current evidence:**

- No organization-level validation workflow was observed.

<!-- roadmap-step
id: ORG-Q04
status: planned
depends_on: [ORG-Q03]
issues: []
-->
#### ORG-Q04 — Define the boundary with Hygiene

**State:** `planned`  
**Depends on:** `ORG-Q03`

**Outcome:** Human-facing defaults stay here while machine-readable portfolio policy is owned by Hygiene.

**Exit criteria:**

- [ ] Ownership is stated in both repositories.
- [ ] No policy is authoritative in two places.

**Current evidence:**

- Hygiene is the proposed canonical machine-readable organization definition.

<!-- roadmap-step
id: ORG-Q05
status: planned
depends_on: [ORG-Q03, ORG-Q04]
issues: []
-->
#### ORG-Q05 — Publish a verified organization-default release

**State:** `planned`  
**Depends on:** `ORG-Q03`, `ORG-Q04`

**Outcome:** A dated, evidence-backed checkpoint makes changes to shared defaults auditable.

**Exit criteria:**

- [ ] All lightweight validation is green.
- [ ] The checkpoint links the policy changes and consumer proof.

**Current evidence:**

- No CI or release publication was observed.

### Roadmap-to-issue handoff

- A step is complete only when its exit criteria and required evidence are satisfied; commit count never determines progress.
- Ready or planned steps without an issue are candidates for the private, duplicate-aware roadmap.issue-plan.json dry run.
- Issue creation or reconciliation requires human approval or an explicitly authorized Pace operation and returns issue references through a reviewable roadmap pull request.
- Pull requests and commits should include Roadmap-Step: <ID>; historical evidence may be linked through existing issue and pull-request relationships.
- Public rendering uses only allowlisted build-time evidence and never places a GitHub token or private issue plan in the browser artifact.

<!-- END ROADMAP EXECUTION SNAPSHOT -->

## Strategic context

This roadmap describes capability evolution, not promised dates or an issue queue. Sequence follows architecture dependencies and may change when evidence or risk changes.

## Phase 1: Clarify supported GitHub surfaces

**Outcome:** A bounded capability advances from documented intent to validated, independently usable behavior.

**Exit signals:**

- The owning contract and acceptance criteria are versioned.
- Implementation and documentation agree.
- Relevant tests and safety checks pass.
- Downstream consumers and migration impact are understood.
- Remaining uncertainty is visible.

## Phase 2: Route every concern to a canonical owner

**Outcome:** A bounded capability advances from documented intent to validated, independently usable behavior.

**Exit signals:**

- The owning contract and acceptance criteria are versioned.
- Implementation and documentation agree.
- Relevant tests and safety checks pass.
- Downstream consumers and migration impact are understood.
- Remaining uncertainty is visible.

## Phase 3: Automate safe projections

**Outcome:** A bounded capability advances from documented intent to validated, independently usable behavior.

**Exit signals:**

- The owning contract and acceptance criteria are versioned.
- Implementation and documentation agree.
- Relevant tests and safety checks pass.
- Downstream consumers and migration impact are understood.
- Remaining uncertainty is visible.

## Phase 4: Measure organization onboarding quality

**Outcome:** A bounded capability advances from documented intent to validated, independently usable behavior.

**Exit signals:**

- The owning contract and acceptance criteria are versioned.
- Implementation and documentation agree.
- Relevant tests and safety checks pass.
- Downstream consumers and migration impact are understood.
- Remaining uncertainty is visible.

## Cross-cutting tracks

- Security, privacy, accessibility, licensing, and provenance.
- Documentation, architecture portals, examples, and onboarding.
- Packaging, release, compatibility, and self-hosting.
- Organization integration through explicit contracts.
- Observatory evidence and Pace conformance when those systems exist.

## Deferred direction

Optional managed services, enterprise controls, marketplaces, and the conversational organization compiler remain later architecture work. Current choices should preserve portability and avoid foreclosing them.

## Evidence and uncertainty

- **Observed:** The repository README establishes the intended boundary as the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; significant implementation remains incomplete.
- **Decided for this draft:** The repository owns the bounded concern described here and participates through versioned contracts.
- **Proposed:** Target systems and later roadmap phases remain proposals until accepted and implemented.
- **Open question:** Which parts of this draft should become active in the first independently versioned release?
