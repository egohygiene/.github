---
schema: aether.architecture-document/v1
id: organization-github-ontology
title: Ego Hygiene .github Ontology
kind: architecture-document
version: 0.1.0
status: provisional
owners:
  - egohygiene
created: 2026-08-19
updated: 2026-08-19
governed_by:
  - architecture-ontology
depends_on:
  - organization-github-purpose
  - organization-github-vision
  - organization-github-principles
  - organization-github-epistemology
related:
  - organization-github-pillars
  - organization-github-manifesto
  - organization-github-ai-constitution
  - organization-github-personal-model
supersedes: []
---

# Ego Hygiene .github Ontology

## Domain scope

Ego Hygiene .github models the concepts needed for give every GitHub visitor and contributor a coherent, discoverable entrance into the Ego Hygiene organization. The ontology names conceptual entities and relationships; it is not a source-code class model, API schema, or database design.

## Canonical concepts

| Concept | Meaning |
| --- | --- |
| Organization profile | A canonical concept in the Ego Hygiene .github domain whose exact fields belong to specifications or schemas, not this ontology. |
| Community health file | A canonical concept in the Ego Hygiene .github domain whose exact fields belong to specifications or schemas, not this ontology. |
| Issue template | A canonical concept in the Ego Hygiene .github domain whose exact fields belong to specifications or schemas, not this ontology. |
| Pull Request template | A canonical concept in the Ego Hygiene .github domain whose exact fields belong to specifications or schemas, not this ontology. |
| Public default | A canonical concept in the Ego Hygiene .github domain whose exact fields belong to specifications or schemas, not this ontology. |
| Coordination issue | A canonical concept in the Ego Hygiene .github domain whose exact fields belong to specifications or schemas, not this ontology. |
| Canonical link | A canonical concept in the Ego Hygiene .github domain whose exact fields belong to specifications or schemas, not this ontology. |

## Core relationships

- A repository or person provides source context to one or more domain artifacts.
- A specification constrains how an artifact is interpreted or produced.
- A plan separates proposed action from execution.
- Evidence supports a claim; a decision authorizes a durable direction.
- Provenance connects derived artifacts to their inputs and processing context.
- A consumer integrates through an explicit interface rather than internal structure.

## Boundaries

- Conceptual identity is distinct from filesystem path, database identifier, or display label.
- Observed state is distinct from desired state.
- Proposed relationships are not accepted facts.
- Neighboring repositories retain ownership of their domain concepts.

## Evidence and uncertainty

- **Observed:** The repository README establishes the intended boundary as the organization-facing GitHub profile, public defaults, contribution entry points, and fallback coordination surface; significant implementation remains incomplete.
- **Decided for this draft:** The repository owns the bounded concern described here and participates through versioned contracts.
- **Proposed:** Target systems and later roadmap phases remain proposals until accepted and implemented.
- **Open question:** Which parts of this draft should become active in the first independently versioned release?
