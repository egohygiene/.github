---
schema: aether.architecture-document/v1
id: organization-github-meta
title: Ego Hygiene .github Meta
kind: architecture-document
version: 0.1.0
status: provisional
owners:
  - egohygiene
created: 2026-08-19
updated: 2026-08-19
governed_by:
  - architecture-meta
depends_on:
  - organization-github-epistemology
  - organization-github-ai-constitution
related:
  - organization-github-purpose
  - organization-github-vision
  - organization-github-principles
  - organization-github-pillars
supersedes: []
---

# Ego Hygiene .github Meta Architecture

## Architecture-system overview

Ego Hygiene .github's architecture is an 18-document graph materialized from the Aether architecture specifications. Each document owns one bounded concern. This index maps ownership and relationships without replacing the documents themselves.

## Document inventory

| Artifact | Path | Category | Status | Governing specification | Upstream dependencies |
| --- | --- | --- | --- | --- | --- |
| organization-github-purpose | [PURPOSE.md](PURPOSE.md) | Identity | provisional | architecture-purpose | — |
| organization-github-vision | [VISION.md](VISION.md) | Identity | provisional | architecture-vision | organization-github-purpose |
| organization-github-principles | [PRINCIPLES.md](PRINCIPLES.md) | Identity | provisional | architecture-principles | organization-github-purpose, organization-github-vision |
| organization-github-pillars | [PILLARS.md](PILLARS.md) | Identity | provisional | architecture-pillars | organization-github-purpose, organization-github-vision, organization-github-principles |
| organization-github-manifesto | [MANIFESTO.md](MANIFESTO.md) | Identity | provisional | architecture-manifesto | organization-github-purpose, organization-github-vision, organization-github-principles, organization-github-pillars |
| organization-github-epistemology | [EPISTEMOLOGY.md](EPISTEMOLOGY.md) | Meta | provisional | architecture-epistemology | organization-github-purpose, organization-github-principles |
| organization-github-ai-constitution | [AI_CONSTITUTION.md](AI_CONSTITUTION.md) | Meta | provisional | architecture-ai-constitution | organization-github-purpose, organization-github-vision, organization-github-principles, organization-github-epistemology |
| organization-github-ontology | [ONTOLOGY.md](ONTOLOGY.md) | Domain | provisional | architecture-ontology | organization-github-purpose, organization-github-vision, organization-github-principles, organization-github-epistemology |
| organization-github-personal-model | [PERSONAL_MODEL.md](PERSONAL_MODEL.md) | Domain | provisional | architecture-personal-model | organization-github-purpose, organization-github-vision, organization-github-principles, organization-github-epistemology, organization-github-ontology |
| organization-github-foundations | [FOUNDATIONS.md](FOUNDATIONS.md) | Foundation | provisional | architecture-foundations | organization-github-purpose, organization-github-principles, organization-github-epistemology |
| organization-github-system | [SYSTEM.md](SYSTEM.md) | Foundation | provisional | architecture-system | organization-github-foundations, organization-github-ontology |
| organization-github-architecture | [ARCHITECTURE.md](ARCHITECTURE.md) | Foundation | provisional | architecture-architecture | organization-github-foundations, organization-github-system |
| organization-github-methodology | [METHODOLOGY.md](METHODOLOGY.md) | Foundation | provisional | architecture-methodology | organization-github-principles, organization-github-epistemology, organization-github-ai-constitution, organization-github-foundations, organization-github-architecture |
| organization-github-design | [DESIGN.md](DESIGN.md) | Experience | provisional | architecture-design | organization-github-purpose, organization-github-vision, organization-github-principles, organization-github-personal-model |
| organization-github-design-system | [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) | Experience | provisional | architecture-design-system | organization-github-personal-model, organization-github-design |
| organization-github-decisions | [DECISIONS.md](DECISIONS.md) | Governance | provisional | architecture-decisions | organization-github-principles, organization-github-epistemology, organization-github-foundations, organization-github-system, organization-github-architecture |
| organization-github-roadmap | [ROADMAP.md](ROADMAP.md) | Foundation | provisional | architecture-roadmap | organization-github-vision, organization-github-pillars, organization-github-architecture, organization-github-decisions |
| organization-github-meta | [META.md](META.md) | Meta | provisional | architecture-meta | organization-github-epistemology, organization-github-ai-constitution |

## Relationship graph

```mermaid
flowchart TD
  PURPOSE --> VISION --> PRINCIPLES --> PILLARS --> MANIFESTO
  PURPOSE --> EPISTEMOLOGY --> AI[AI Constitution]
  PRINCIPLES --> EPISTEMOLOGY
  EPISTEMOLOGY --> ONTOLOGY --> PERSONAL[Personal Model]
  PRINCIPLES --> FOUNDATIONS
  EPISTEMOLOGY --> FOUNDATIONS
  FOUNDATIONS --> SYSTEM --> ARCHITECTURE --> METHODOLOGY
  PERSONAL --> DESIGN --> DS[Design System]
  ARCHITECTURE --> DECISIONS --> ROADMAP
  PILLARS --> ROADMAP
  AI --> META
  EPISTEMOLOGY --> META
```

## Ownership map

- Identity documents own why the repository exists, its desired future, decision heuristics, strategic capabilities, and public commitments.
- Meta documents own knowledge integrity, AI authority, and navigation of this document system.
- Domain documents own canonical concepts and bounded human assumptions.
- Foundation documents own invariants, logical systems, structure, working method, and strategic evolution.
- Experience documents own intended experience and reusable semantic design language.
- Governance owns accepted architectural decisions and historical lineage.

## Reading order

1. PURPOSE, VISION, and PRINCIPLES.
2. EPISTEMOLOGY and ONTOLOGY.
3. FOUNDATIONS, SYSTEM, and ARCHITECTURE.
4. PERSONAL_MODEL, DESIGN, and DESIGN_SYSTEM when evaluating human-facing surfaces.
5. AI_CONSTITUTION before delegating consequential work.
6. DECISIONS and ROADMAP for accepted constraints and evolution.

## Authoring order

Follow the dependency graph from purpose through identity and evidence, then domain and foundations, experience, governance, roadmap, and finally this META index.

## Lifecycle and validation

All documents begin as provisional and require human review before becoming active. Validation covers frontmatter, stable identifiers, links, graph acyclicity, ownership boundaries, evidence labels, Markdown structure, and agreement with repository reality.

## Change propagation

A material upstream change triggers review of every downstream node. Implementation changes first update the owning specification or decision when they alter durable behavior; META changes whenever inventory or relationships change.

## Gaps and omissions

- No document in this set is intentionally omitted because Ego Hygiene .github has repository, automation, human, AI, and public or documentation surfaces that justify the complete reference set.
- Target systems remain provisional where implementation evidence is absent.
- Repository-local schemas and automated graph validation should be added or connected to Aether in a later conformance pass.

## Evidence and uncertainty

- **Observed:** The repository README establishes the intended boundary as the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; significant implementation remains incomplete.
- **Decided for this draft:** The repository owns the bounded concern described here and participates through versioned contracts.
- **Proposed:** Target systems and later roadmap phases remain proposals until accepted and implemented.
- **Open question:** Which parts of this draft should become active in the first independently versioned release?
