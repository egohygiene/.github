---
schema: aether.architecture-document/v1
id: organization-github-decisions
title: Ego Hygiene .github Decisions
kind: architecture-document
version: 0.2.0
status: provisional
owners:
  - egohygiene
created: 2026-08-19
updated: 2026-08-21
governed_by:
  - architecture-decisions
depends_on:
  - organization-github-principles
  - organization-github-epistemology
  - organization-github-foundations
  - organization-github-system
  - organization-github-architecture
related:
  - organization-github-purpose
  - organization-github-vision
  - organization-github-pillars
  - organization-github-manifesto
supersedes: []
---

# Ego Hygiene .github Decisions

## Purpose

This document preserves significant accepted architectural choices and their rationale. Issues coordinate work, proposals explore alternatives, and this file records decisions that constrain future implementation.

## Governance

Do not rewrite historical context to fit current understanding. Amend a record for corrections that do not change meaning; supersede it with a new record when the decision changes materially.

## Index

- ADR-0001: Keep ecosystem architecture canonical in Hygiene
- ADR-0002: Use this repository as the organization-facing inbox and defaults surface
- ADR-0003: Avoid duplicating implementation libraries
- ADR-0004: Define trust policy before reusable enforcement
- ADR-0005: Keep organization label meaning canonical in `.github`

## ADR-0001: Keep ecosystem architecture canonical in Hygiene

- **Status:** Accepted as the current architectural direction
- **Date:** 2026-08-19
- **Context:** Repository evidence and ecosystem ownership require an explicit durable boundary.
- **Decision:** Keep ecosystem architecture canonical in Hygiene.
- **Consequences:** The choice improves ownership and predictability while requiring maintained contracts, validation, and migration discipline.
- **Reconsider when:** New evidence shows that the boundary prevents standalone usefulness, safety, portability, or maintainability.

## ADR-0002: Use this repository as the organization-facing inbox and defaults surface

- **Status:** Accepted as the current architectural direction
- **Date:** 2026-08-19
- **Context:** Repository evidence and ecosystem ownership require an explicit durable boundary.
- **Decision:** Use this repository as the organization-facing inbox and defaults surface.
- **Consequences:** The choice improves ownership and predictability while requiring maintained contracts, validation, and migration discipline.
- **Reconsider when:** New evidence shows that the boundary prevents standalone usefulness, safety, portability, or maintainability.

## ADR-0003: Avoid duplicating implementation libraries

- **Status:** Accepted as the current architectural direction
- **Date:** 2026-08-19
- **Context:** Repository evidence and ecosystem ownership require an explicit durable boundary.
- **Decision:** Avoid duplicating implementation libraries.
- **Consequences:** The choice improves ownership and predictability while requiring maintained contracts, validation, and migration discipline.
- **Reconsider when:** New evidence shows that the boundary prevents standalone usefulness, safety, portability, or maintainability.

## ADR-0004: Define trust policy before reusable enforcement

- **Status:** Accepted as the current architectural direction
- **Date:** 2026-08-21
- **Context:** Trust-policy issue `ORG-05` and the Relay and Realm implementation
  issues depend on one another when policy adoption and implementation evidence
  are treated as one step.
- **Decision:** The organization-facing [repository trust
  policy](TRUST_POLICY.md) defines DCO, signing, provenance, SBOM, exception,
  and staged-adoption requirements first. Relay and artifact-producing
  repositories implement those requirements through versioned contracts;
  adoption evidence follows without reopening the policy decision.
- **Consequences:** Policy requirements can be reviewed without copied workflow
  code or false implementation claims. Repositories remain non-blocking until
  an explicit migration state enables enforcement.
- **Reconsider when:** The ownership boundary prevents independent policy
  review, reusable implementation, or accurate conformance evidence.

## ADR-0005: Keep organization label meaning canonical in `.github`

- **Status:** Accepted as the current architectural direction
- **Date:** 2026-09-02
- **Context:** Organization intake requires stable label meaning while provider
  synchronization, path labeling, and contributor automation belong to Relay.
- **Decision:** Keep the versioned organization label catalog, overlay model,
  and repository assignments in `.github`. Relay consumes the contract and owns
  provider mutations; repository additions cannot redefine canonical labels.
- **Consequences:** Human-facing defaults and their machine-readable meaning
  share one owner. Synchronization remains reusable and independently released.
  Every consumer must bind to an immutable catalog revision and fail closed on
  incompatible versions.
- **Reconsider when:** GitHub-specific representation leaks into the canonical
  domain contract or the boundary prevents safe non-GitHub consumers.

## Open decisions

- Release and compatibility policy for the first stable version.
- Exact self-hosted, managed, and organization-integrated deployment boundaries.
- Which target systems must exist before the architecture status may become active.

## Evidence and uncertainty

- **Observed:** The repository README establishes the intended boundary as the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; significant implementation remains incomplete.
- **Decided for this draft:** The repository owns the bounded concern described here and participates through versioned contracts.
- **Proposed:** Target systems and later roadmap phases remain proposals until accepted and implemented.
- **Open question:** Which parts of this draft should become active in the first independently versioned release?

## Identifier format migration (2026-10-18)

The maintainer selected four-digit numbering in [Hygiene #73](https://github.com/egohygiene/hygiene/issues/73). This padding-only migration changes current labels and anchors; logical numbers, decision content, dates and disposition remain unchanged. Git retains prior versions. New canonical records use `ADR-NNNN` under Hygiene policy v1.2.0.

| Previous ID | Current ID | Record |
| --- | --- | --- |
| `ADR-001` | `ADR-0001` | [DECISIONS.md](DECISIONS.md#adr-0001-keep-ecosystem-architecture-canonical-in-hygiene) |
| `ADR-002` | `ADR-0002` | [DECISIONS.md](DECISIONS.md#adr-0002-use-this-repository-as-the-organization-facing-inbox-and-defaults-surface) |
| `ADR-003` | `ADR-0003` | [DECISIONS.md](DECISIONS.md#adr-0003-avoid-duplicating-implementation-libraries) |
| `ADR-004` | `ADR-0004` | [DECISIONS.md](DECISIONS.md#adr-0004-define-trust-policy-before-reusable-enforcement) |
| `ADR-005` | `ADR-0005` | [DECISIONS.md](DECISIONS.md#adr-0005-keep-organization-label-meaning-canonical-in-github) |
