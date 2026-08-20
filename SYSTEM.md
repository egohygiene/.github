---
schema: aether.architecture-document/v1
id: organization-github-system
title: Ego Hygiene .github System
kind: architecture-document
version: 0.1.0
status: provisional
owners:
  - egohygiene
created: 2026-08-19
updated: 2026-08-19
governed_by:
  - architecture-system
depends_on:
  - organization-github-foundations
  - organization-github-ontology
related:
  - organization-github-purpose
  - organization-github-vision
  - organization-github-principles
  - organization-github-pillars
supersedes: []
---

# Ego Hygiene .github System

## Purpose and scope

This document identifies Ego Hygiene .github's logical systems and responsibilities. It answers what the major systems do; [ARCHITECTURE.md](ARCHITECTURE.md) owns their structural organization and dependency rules.

## System inventory

| System | State | Responsibility |
| --- | --- | --- |
| Organization profile | Target | Owns its bounded portion of the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; exposes explicit inputs, outputs, failure states, and evidence. |
| Community health defaults | Target | Owns its bounded portion of the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; exposes explicit inputs, outputs, failure states, and evidence. |
| Issue and pull-request intake | Target | Owns its bounded portion of the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; exposes explicit inputs, outputs, failure states, and evidence. |
| Agent instruction projection | Target | Owns its bounded portion of the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; exposes explicit inputs, outputs, failure states, and evidence. |
| Coordination queue | Target | Owns its bounded portion of the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; exposes explicit inputs, outputs, failure states, and evidence. |

## External systems

- Hygiene control plane
- Empathy baseline
- Relay workflows
- Aether agent contracts

External systems are integrations, not hidden implementation units. Each requires version, authentication, availability, data, error, and replacement boundaries appropriate to its risk.

## System interactions

Inputs enter through an adapter or validated contract, move through domain systems, produce artifacts and diagnostics, and leave through a stable interface. Evidence flows back to validation, review, and future decisions.

## Failure model

Systems fail closed at destructive, publication, privacy, and security boundaries. Partial results identify coverage and remain distinguishable from complete success.

## Evidence and uncertainty

- **Observed:** The repository README establishes the intended boundary as the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; significant implementation remains incomplete.
- **Decided for this draft:** The repository owns the bounded concern described here and participates through versioned contracts.
- **Proposed:** Target systems and later roadmap phases remain proposals until accepted and implemented.
- **Open question:** Which parts of this draft should become active in the first independently versioned release?
