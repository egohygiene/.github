# Repository Intelligence completion roadmap

Observed 2026-11-10. This is the execution queue for
[organization #30](https://github.com/egohygiene/.github/issues/30) and
[acceptance #41](https://github.com/egohygiene/.github/issues/41). It coordinates
existing owners and issues; Hygiene [#60](https://github.com/egohygiene/hygiene/issues/60)
still owns the pending organization-strategy contract.

## Finish line

Use `.github` as the daily organization entry point: what needs attention,
which evidence is current, what needs a human decision, and where to drill into
each repository's own Intelligence dashboard. Every eligible public repository
has an explicit adoption or disposition record. Real evidence feeds both levels.
The final release has inspectable integration and publication proof.

The current implementation already has ten core repository views, conditional
Hygiene/Audits/Sanity views, fleet transport, a central overview/graph and bounded
audit orchestration. See the [merged implementation index](https://github.com/egohygiene/relay/blob/73f750ef9dd1782b20d280b4c555aacd92ee5f4e/docs/repository-intelligence-audits-sanity-review.md).
Open feature issues do not mean their source implementation should be rebuilt.
Consumer adoption, real artifacts, source holds and acceptance are separate.

## Execution order

| Wave | State | Work | Exit evidence |
| --- | --- | --- | --- |
| RI-01 | Active | `.github` home, directory, explicit hosting transition and portable organization-only export | Source home/profile; dated public directory; sealed review artifact; consumer verifies exact producer/source/origin/base/files; named hosting gates |
| RI-02 | Ready after inventory | Repository adoption in bounded batches | Every admitted repository records current source, builder pin, model/artifact, declared destination and upkeep independently; existing publishers/recovery preserved |
| RI-03 | Next | Real organization audit and architecture-review feeds | Exact source revisions, repository-owned reports, explicit scope/unknowns, normalized owner models and retained artifacts; no inferred human approval |
| RI-04 | Owner dependencies | Finish the genuinely missing model chains | Typed owner contract → Observatory query → bounded renderer/intake → consumer source evidence for each chain below |
| RI-05 | After usable feeds | Finish organization attention, navigation and failure isolation | One primary home, context-preserving repository links, explicit freshness/unknowns, separate module failure states and reviewed migration aliases |
| RI-06 | Deferred qualification | Qualify, adopt and close acceptance | Privacy/failure canaries, accessible/responsive/browser/performance proof, exact deployment/rollback evidence and checklist reconciliation |

### RI-01 — Establish the organization home

Owners: `.github` [#15](https://github.com/egohygiene/.github/issues/15),
[#27](https://github.com/egohygiene/.github/issues/27),
[website #27](https://github.com/egohygiene/egohygiene.io/issues/27),
[Hygiene #25](https://github.com/egohygiene/hygiene/issues/25),
[#36](https://github.com/egohygiene/hygiene/issues/36).

1. Land this queue, the proposed [hosting decision](../decisions/ADR-0006-organization-intelligence-entrypoint.md),
   profile entry point and dated directory. Keep repository-owned evidence links.
2. Export only the existing organization Intelligence UI from its website owner.
   Bind exact source revision, explicit HTTPS origin, deployment base, route
   allowlist, public scope, model availability and every emitted file.
3. Have Relay verify the sealed export. `.github` initially produces a review
   artifact through a manual, read-only workflow. It does not deploy Pages.
4. Reconcile Hygiene's role/composition declarations and the historical hosting
   requirement in #41 before enabling a new canonical publisher. Preserve the
   website's source-compositor role and existing company/store routes.
5. Resolve the concrete `/.github/` compatibility gap in Hygiene's site-declaration
   base-path schema/validator. This is a deployment prefix, not the repository
   route profile: organization `/audits/`, `/sanity/`, `/roadmap/` and related
   canonical routes remain organization routes beneath that prefix.

The narrow compatibility source is prepared in [Hygiene PR #101](https://github.com/egohygiene/hygiene/pull/101),
functional source `96d3358c9b745af820702e0013af7380d151a6da`. It remains draft;
current consumers have not adopted it and hosting/declaration acceptance is
unchanged.

Do not copy the entire website build or pass a fleet model into the repository
renderer. The current website metadata assumes `egohygiene.io`, and its normal
build includes unrelated routes. The producer export must have an explicit
origin/base and focused entry point. No DNS, CNAME or Pages activation is implied.

### RI-02 — Make repository adoption explicit

Owners: [Pace #13](https://github.com/egohygiene/pace/issues/13) and
[#31](https://github.com/egohygiene/pace/issues/31), with each repository owning
its native publisher and [Relay #101](https://github.com/egohygiene/relay/issues/101)
owning reusable drill-down acceptance.

- Start with a fresh public-source inventory over the exact Hygiene-admitted
  roster. A dated roster is not an assertion about the organization's total.
- Batch the existing merged consumers first, then other configured Pages sites,
  then repositories requiring an explicit setup/applicability decision.
- Track source implementation, Relay version, actual model/artifact, declared
  destination, live verification and refresh ownership as different fields.
- Preserve source-held and unknown cases. A missing destination does not prove
  nonconformance; it identifies the next applicability/setup question.
- Upgrade supported current paths without changing frozen historical selectors,
  rollback bytes, existing publisher gates or retained human decisions.

The five earlier consumer upgrades select `981ddf43`; they predate the new owner
review inputs. Their source is useful baseline evidence, not full-fleet adoption
or a reason to reinstall every existing producer.

### RI-03 — Populate the audit and sanity views

Owners: [Reflector #258](https://github.com/egohygiene/reflector/issues/258),
[Pace #28](https://github.com/egohygiene/pace/issues/28),
[Observatory #20](https://github.com/egohygiene/observatory/issues/20)/[#21](https://github.com/egohygiene/observatory/issues/21),
[Relay #74](https://github.com/egohygiene/relay/issues/74)/[#76](https://github.com/egohygiene/relay/issues/76).

Refresh represented source heads before the real sweep. Resolve Aether profiles,
declare budgets and a trusted adapter/capture path, retain repository-owned
reports, and feed exact normalized models into repository builds and the fleet
home. Findings preserve defects, opportunities, experiments, positive observations
and uncertainty. Proposed backlog items retain source IDs and require review.

The existing 28-repository inventory is preparation; no organization sweep ran
in the preceding implementation batch. AI recommendations, raw JSON human
claims, successful checks and merged code cannot authenticate ratification.
Keep actual human dispositions and material-change freshness in their owners.

### RI-04 — Complete the remaining owner chains

| Domain | Ordered owning issues | Delivery boundary |
| --- | --- | --- |
| Organization roadmap | [Hygiene #60](https://github.com/egohygiene/hygiene/issues/60) → [Observatory #22](https://github.com/egohygiene/observatory/issues/22) → [organization #29](https://github.com/egohygiene/.github/issues/29); maintenance [Aether #88](https://github.com/egohygiene/aether/issues/88)/[Pace #29](https://github.com/egohygiene/pace/issues/29) | Portfolio intent/progress without replacing repository roadmaps |
| Status | [Hygiene #62](https://github.com/egohygiene/hygiene/issues/62) → [Observatory #23](https://github.com/egohygiene/observatory/issues/23) → [Relay #41](https://github.com/egohygiene/relay/issues/41) → [organization #33](https://github.com/egohygiene/.github/issues/33)/[Pace #15](https://github.com/egohygiene/pace/issues/15) | Explicit service/status evidence; source-held availability stays unknown |
| Diagnostics | [Hygiene #41](https://github.com/egohygiene/hygiene/issues/41) + [EgoLint #50](https://github.com/egohygiene/egolint/issues/50) → [Observatory #16](https://github.com/egohygiene/observatory/issues/16) → [Relay #57](https://github.com/egohygiene/relay/issues/57) | Typed diagnostic evidence; Aether #74 is already closed |
| Distribution | [Hygiene #29](https://github.com/egohygiene/hygiene/issues/29)/[Aether #63](https://github.com/egohygiene/aether/issues/63) → [Relay #48](https://github.com/egohygiene/relay/issues/48) → [Observatory #13](https://github.com/egohygiene/observatory/issues/13) → [organization #39](https://github.com/egohygiene/.github/issues/39) | Delivery and installation evidence remain distinct from releases |
| Identity adoption | [organization #37](https://github.com/egohygiene/.github/issues/37) and the owning Identity/Hygiene contracts | Actual applicability/version/adoption evidence; distinguish the Identity product `/identity/` from repository adoption `/intelligence/identity/`; approved assets alone are insufficient |

Use the same contract/query/renderer/consumer slice pattern. Existing source-
unsupported routes become implemented only when compatible owner evidence is
available. Each completed source slice gets a concrete review reference and a
next dependency-ready issue; source merges do not close acceptance automatically.

### RI-05/06 — Integrate, qualify and finish

Finish the first-screen attention queue with real blockers, stale/unknown
evidence and human-review needs. Preserve visibility before counts, identifiers,
hashes, search, links or graph expansion; publish no hidden-repository totals.
Use one canonical organization home and explicit migration aliases. Each module
fails independently and retains its own clock and provenance.

Tests, CI, application/native builds, browser/provider checks and live deployment
qualification remain deferred by the current user instruction. Keep their
acceptance unchecked in [Relay #101](https://github.com/egohygiene/relay/issues/101),
[#106](https://github.com/egohygiene/relay/issues/106) and
[organization #41](https://github.com/egohygiene/.github/issues/41).
At that final phase, exercise privacy/failure boundaries, accessibility,
performance, exact production artifacts, canaries and recovery; reconcile issue
checklists only against actual evidence.

Explicitly disposition [Relay #42](https://github.com/egohygiene/relay/issues/42),
[#130](https://github.com/egohygiene/relay/issues/130) and
[Observatory #17](https://github.com/egohygiene/observatory/issues/17) as required
release work or named later milestones. A v1 finish line cannot silently drop
them or expand forever.

## Execution rules and source holds

Work in dependency order, parallelize independent owners, keep PRs bounded and
refresh this queue and continuity at each handoff. Prefer completing the existing
implementation over creating a second collector, model, score or publisher.

Preserve [Hygiene #47](https://github.com/egohygiene/hygiene/issues/47)'s real
ADR-0001 metadata/authority hold and [Akashic #197](https://github.com/egohygiene/akashic/issues/197)'s
roadmap prerequisite. [Hygiene #69](https://github.com/egohygiene/hygiene/issues/69)
needs an explicit compatibility/authority disposition but does not block ordinary
supported consumer engineering. This queue grants no human ratification,
production activation or new domain authority.
