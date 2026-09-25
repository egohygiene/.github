---
schema: aether.architecture-document/v1
id: organization-github-roadmap
title: Ego Hygiene .github Roadmap
kind: architecture-document
version: 0.1.1
status: provisional
owners:
  - egohygiene
created: 2026-08-19
updated: 2026-09-25
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

This is the roadmap for the `.github` repository's own defaults, intake, and
coordination responsibilities. Hygiene is the accepted owner of ecosystem
architecture and the repository catalog; [Hygiene #60](https://github.com/egohygiene/hygiene/issues/60)
owns the pending canonical organization-roadmap contract. The proposed
[foundation checkpoint](docs/foundation-readiness-checkpoint.md) records the
current bounded execution focus by reference, while
[organization #30](https://github.com/egohygiene/.github/issues/30) coordinates
Intelligence delivery. Neither replaces organization or repository strategy.

<!-- BEGIN ROADMAP EXECUTION SNAPSHOT -->
<!-- roadmap-manifest
schema: hygiene.roadmap/v1alpha1
repository: egohygiene/.github
visibility: public
publication: central
route: /roadmap/.github/
updated: 2026-09-25
-->
## 2026-09-25 execution reconciliation

> This evidence-reconciled snapshot is the issue-generation and visual-roadmap handoff. The longer-horizon strategy below remains canonical context; generated HTML, JSON, progress, issue plans, and commit lists are projections.

**Lifecycle:** incubating foundation  
**Current gate:** Review the bounded foundation reconciliation and read-only Actions inventory. The label contract in #8 is merged; legacy consumer and inherited-default acceptance still require their own evidence.

**North-star outcome:** A thin, trusted set of organization defaults that makes contribution, security, and intake behavior predictable without hiding repository-owned policy.

### Visual roadmap publication

**Mode:** `central`  
**Route:** `/roadmap/.github/`  
**Current publication evidence:** Organization-wide GitHub defaults are present. No new live Pages or stable-release verification is claimed by this documentation reconciliation.

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

- [x] Issue #8 has an accepted label taxonomy and routing contract.
- [ ] At least one repository demonstrates the policy without repository-specific ambiguity.

**Current evidence:**

- [Issue #8](https://github.com/egohygiene/.github/issues/8) is closed as completed.
- [PR #21](https://github.com/egohygiene/.github/pull/21) merged on 2026-09-02 as
  `b415c8029bf2fb5d474f367e7129791588ba3860`, delivering the versioned label
  catalog, overlay assignments, routing guidance, validators, and workflow.
- The committed assignment document and reference projection cover `.github`.
  This inspection has not established the intended adoption evidence for the
  remaining criterion; reconcile it explicitly rather than inferring this
  step's completion from issue closure. Its active state is retained.

<!-- roadmap-step
id: ORG-Q03
status: planned
depends_on: [ORG-Q02]
issues: []
-->
#### ORG-Q03 — Validate inherited community files

**State:** `planned`

**Depends on:** `ORG-Q02`

**Outcome:** Repositories can tell which community files they inherit and which they must own.

**Exit criteria:**

- [ ] An automated check covers all intended inherited files.
- [ ] Exceptions and private-repository behavior are documented.

**Current evidence:**

- The repository has a path-filtered [label-contract workflow](.github/workflows/validate-label-contract.yml)
  for pull requests, `main` pushes, and manual dispatch. That workflow validates
  labels; it does not prove all inherited community files.
- Its historical [PR #21 run 33573965859](https://github.com/egohygiene/.github/actions/runs/33573965859)
  completed successfully on the label-contract candidate. This is historical
  execution evidence, not a check of the present documentation candidate.
- Inherited-file coverage and consumer/visibility exceptions remain unverified.
  This step is planned until its own evidence and ORG-Q02's remaining criterion
  are reconciled; the old ready label was not supported by those records.

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

- [x] Ownership is stated in both repositories.
- [ ] No policy is authoritative in two places.

**Current evidence:**

- [Local ADR-001](DECISIONS.md) and accepted
  [Hygiene ADR-0001](https://github.com/egohygiene/hygiene/blob/main/docs/decisions/ADR-0001-holistic-architecture-v0.1.md)
  assign ecosystem architecture and the repository catalog to Hygiene.
- [Organization #42](https://github.com/egohygiene/.github/issues/42) proposes a
  conflicting canonical registry/roadmap location. Reconcile that proposal with
  existing owners before implementation; no ownership move or duplicate
  registry is accepted by this checkpoint. The second criterion remains open.

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

- Label-contract CI exists and has the historical successful execution linked
  under ORG-Q03. That focused evidence does not establish a verified release of
  every organization default.
- Stable organization-default release evidence and the full consumer checkpoint
  have not been verified by this reconciliation; both exit criteria remain open.

### Roadmap-to-issue handoff

- A step is complete only when its exit criteria and required evidence are satisfied; commit count never determines progress.
- Ready steps without an issue are candidates for the private, duplicate-aware roadmap.issue-plan.json dry run. Planned steps remain preview-only unless a reviewer explicitly opts them in with issue_policy: propose.
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
