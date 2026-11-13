---
schema: egohygiene.architecture-decision/v1
id: ADR-0006
title: Make the organization GitHub repository the primary Intelligence entry point
status: proposed
date: "2026-11-10"
decision_scope: repository
visibility: public
owners: [egohygiene/.github]
issue: https://github.com/egohygiene/.github/issues/27
pull_request: null
related: [ADR-0001, ADR-0002, ADR-0003]
supersedes: []
superseded_by: []
affected_repositories:
  - egohygiene/.github
  - egohygiene/egohygiene.io
  - egohygiene/hygiene
  - egohygiene/relay
  - egohygiene/observatory
  - egohygiene/pace
affected_contracts:
  - egohygiene.public-site-surface-registry/v1
  - egohygiene.public-site-surface-declaration/v1
implementation_status: in_progress
evidence:
  - type: issue
    url: https://github.com/egohygiene/.github/issues/27
    description: Organization-facing Intelligence home and modular navigation.
  - type: issue
    url: https://github.com/egohygiene/.github/issues/41
    description: Existing acceptance still names the earlier egohygiene.io host and requires explicit reconciliation.
  - type: documentation
    url: https://github.com/egohygiene/relay/blob/73f750ef9dd1782b20d280b4c555aacd92ee5f4e/docs/repository-intelligence-audits-sanity-review.md
    description: Merged evidence/model/rendering foundations retained rather than reimplemented.
exceptions: []
approval: null
extensions: {}
---

# ADR-0006: Make the organization GitHub repository the primary Intelligence entry point

## Context

The maintainer selected `egohygiene/.github` as the daily organization perspective:
high-level insights, attention and links into repository-owned Intelligence.
Earlier roadmap and acceptance text assumes the portal is hosted by
`egohygiene.io`. The current website already owns a substantial organization UI;
Hygiene retains canonical architecture, catalog and surface semantics, and
Observatory retains normalized evidence. A second independent model or copied
website would create maintenance and authority conflicts.

## Decision

Propose this repository as the primary organization entry point. Its profile and
README provide a useful source home immediately; a future single Pages publisher
consumes an Intelligence-only export from the website source owner. Relay
verifies that export through a versioned transport contract. The website remains
the source compositor and company-site owner; each repository retains its own
Pages publisher and detailed dashboard. Hygiene/Observatory/Aether/Reflector
retain their existing policy, model, methodology and orchestration boundaries.

The consumer starts with a manual review-artifact path. It receives exact producer
source, origin, deployment prefix, canonical organization routes, public scope
and a complete hash-bound file inventory. It does not deploy Pages, activate DNS,
change CNAME or infer published/live status. A reviewed deployment is a later
explicit action; this proposal does not claim architecture ratification.

### Route and compatibility boundaries

The proposed GitHub project Pages mount has HTTPS origin
`https://egohygiene.github.io` and base `/.github/`. That is intended
configuration, not observed enabled hosting. A reviewed custom origin remains
possible. The base is a deployment prefix; the organization route profile keeps
`/intelligence/`, `/audits/`, `/sanity/`, `/roadmap/` and the registry's other
organization bindings beneath it. Repository detail routes stay nested under
their own `/intelligence/` roots.

Current Hygiene site declarations reject `/.github/` because base-path segments
start with an alphanumeric character. A narrow owner schema/helper compatibility
proposal is required; old pins cannot admit the new prefix. The export transport
may represent that intended review target without claiming an admitted site
declaration. Reconcile canonical role/composition/publication declarations and
the older #41 hosting criterion before activating the new canonical publisher.
No accepted role or declaration is overwritten here.

## Alternatives considered and rejected

- Keep the website as the only daily entry point: retains the existing host but
  does not match the maintainer's chosen organization workflow.
- Copy its entire output into this repository: carries unrelated store/routes
  and the current `egohygiene.io` canonical/asset assumptions; rejected.
- Feed fleet JSON to the repository renderer: violates its repository/commit
  binding and route profile; rejected.
- Export a focused organization application: reuses the UI and models while
  requiring explicit base-path, metadata, transport and migration contracts.

## Consequences and tradeoffs

There will be a deliberate interval with source navigation here and the earlier
website route still linked. The transition must not publish two canonical copies.
The future cutover needs reviewed route aliases and declared publication evidence.

## Implementation and evidence links

Source checkpoint, 2026-11-13: the real report-to-review-artifact canary passed,
and the maintainer explicitly requested work toward live project Pages. The
[publisher preparation](../intelligence/organization-pages.md) selects the
actual retained review artifact and Hygiene's explicit organization-export
declaration profile. The website remains source compositor; `.github` owns the
selected publisher/recovery boundary. Existing review receipts and this
proposal's null approval remain unchanged. Publication authorization does not
ratify this ADR; actual provider/live evidence is recorded separately.

Source checkpoint, 2026-11-12: the narrow `/.github/` compatibility correction
described in the original context was merged in
[Hygiene #101](https://github.com/egohygiene/hygiene/pull/101). Consumers must
select those compatible owner resources explicitly; an older pin retains its
original behavior. The focused export, typed review feed and retained-model
intake are now source-integrated. The
[real report canary](../intelligence/real-report-canary.md) tracks the next
artifact proof. These implementation observations do not accept this proposed
decision, enable a publisher or satisfy hosting/declaration acceptance.

This proposal records source implementation and the user's requested direction;
approval remains null. This is a local consumption/publisher proposal; Hygiene
retains organization-level policy and declaration authority. The selected
authoring reference is Hygiene policy 1.2.0 at
`a05b14f8b9e2772124f879f818e09a911e996ad8`. This new record does not install a
whole-repository policy reference or migrate the older inline ADR set. The
[completion roadmap](../intelligence/DELIVERY_ROADMAP.md)
owns the bounded execution queue. Required work includes the focused export,
Relay verifier, dated repository directory, Hygiene compatibility/declarations,
explicit publisher cutover, consumer adoption and final qualification. Tests,
CI, builds, browser/provider and live publication qualification remain deferred.

## Replacement or exit strategy

Rollback retains the earlier compatible host/artifact and original repository
publishers. Source, model, artifact, preview, deployment and human approval remain
separate observations. No migration requires rewriting historical evidence.

## Follow-up work

Complete the source export/intake and review artifact, reconcile Hygiene's
declaration/base-path/host boundaries, then separately qualify and activate a
single publisher. Reconcile the old issue hosting text and consumer navigation
against that reviewed outcome; keep acceptance and human disposition explicit.
