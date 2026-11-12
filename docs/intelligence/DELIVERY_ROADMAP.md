# Repository Intelligence completion roadmap

Observed 2026-11-11. This is the execution queue for
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
| RI-01 | First source wave merged; artifacts/hosting unqualified | `.github` home, directory, explicit hosting transition and portable organization-only export | Source home/profile; dated public directory; sealed review artifact; consumer verifies exact producer/source/origin/base/files; named hosting gates |
| RI-02 | First five-slice adoption batch in draft | Repository adoption in bounded batches | Every admitted repository records current source, builder pin, model/artifact, declared destination and upkeep independently; existing publishers/recovery preserved |
| RI-03 | Feed source in draft; actual sweep pending | Real organization audit and architecture-review feeds | Exact source revisions, repository-owned reports, explicit scope/unknowns, normalized owner models and retained artifacts; no inferred human approval |
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

The first four source slices were merged after maintainer approval. These are
observed source merges, not successful exports, deployments or hosting acceptance:

| Owner | Merged source | Merge revision |
| --- | --- | --- |
| `.github` | [PR #52](https://github.com/egohygiene/.github/pull/52): home/profile, directory, roadmap and manual review consumer | `101a0d4553dc380ab3f88c50b11cb53beadfce18` |
| Website | [PR #139](https://github.com/egohygiene/egohygiene.io/pull/139): focused organization export and manual producer | `c35932b77fe3623cad19f1f1b890e51ec16f38a8` |
| Relay | [PR #180](https://github.com/egohygiene/relay/pull/180): sealed-byte review intake | `a3d87ab48d92d10f74d8d0df8a6106b66cce0dac` |
| Hygiene | [PR #101](https://github.com/egohygiene/hygiene/pull/101): exact `/.github/` compatibility | `31ae6fb78757502e7474e5518904fc568840c1ee` |

The review consumer selects Relay functional source
`d15cacd987ef1f98a6b94b051a42925eb91f8cc7`. Its unchanged producer schema/route
lock selects website `54e0b6e66b9b028bad382bbbc4bc6ba588cee665`. The Hygiene
correction is merged source; old pinned consumers do not gain it automatically.
Canonical hosting/declaration reconciliation and actual pipeline qualification
remain pending.

The next five slices are now implemented for review across seven draft PRs:
Pace's actionable adoption ledger, shared typed review feed, Identity/Empathy
feed adoption, Civics onboarding and retained-model organization export/intake.
See the [current review packet](2026-11-11-adoption-review.md) for exact references,
source pins, dependency order and deferred acceptance. This new batch is not
merged; it activates no publisher.

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

[Pace PR #37](https://github.com/egohygiene/pace/pull/37) now provides the
source-backed ledger over the fixed 28-entry public roster. Source, builder,
destination, artifact/live verification and refresh ownership remain independent;
eligibility is unassessed and missing runtime evidence stays unknown. Its
projection clock cannot refresh the original source observations.

[Identity #144](https://github.com/egohygiene/identity/pull/144),
[Empathy #125](https://github.com/egohygiene/empathy/pull/125) and
[Civics #9](https://github.com/egohygiene/civics/pull/9) add or upgrade supported
current paths to the exact shared feed. Existing publishers, product bytes and
frozen recovery stay protected; no report or publication result is supplied.

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

[Relay PR #181](https://github.com/egohygiene/relay/pull/181), functional source
`5d27be5ce1599df883e31f14cd894eb18622c18c`, supplies the checked-in Git report
profile and existing repository/singleton-fleet owner models. Empty selections
are unavailable; historical report subjects and clocks stay historical. A
captured-current report source profile and actual organization sweep remain
separate future work. [Website #140](https://github.com/egohygiene/egohygiene.io/pull/140)
and this companion consumer can select retained owner bundles for the primary
organization overview, preserving independent module clocks and failure states.
There is no new semantic fleet assembler or automatic latest-artifact selection.

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

## Proposed next batch — awaiting maintainer review

Live issue/default-branch source triage on 2026-11-11 supports these five slices.
They are a proposal; this handoff does not start or approve them.

| Order | Owning issue / source slice | Concrete next change and boundary |
| --- | --- | --- |
| 1 | [Pace #13](https://github.com/egohygiene/pace/issues/13): OptiFlow adoption | Upgrade the existing current `981ddf43` path to the reviewed typed feed, same-frame owner inputs and separate receipt artifact. Keep native publisher/tool ordering. Declared `https://optiflow.egohygiene.io` is source intent; publication qualification remains [Flow #88](https://github.com/egohygiene/flow/issues/88). OptiFlow #60 is closed as superseded, not qualified. |
| 2 | [Pace #13](https://github.com/egohygiene/pace/issues/13): Akashic adoption | Reuse one exact feed/model/clock pair across both current deterministic builds; update current receipt/profile admission. Preserve [Akashic #197](https://github.com/egohygiene/akashic/issues/197), disabled unsupported collectors and frozen recovery bytes. |
| 3 | [Pace #13](https://github.com/egohygiene/pace/issues/13): Hygiene evidence | Add optional read-only retained review evidence independently of the existing publication hold. Preserve [Hygiene #47](https://github.com/egohygiene/hygiene/issues/47); do not admit held ADRs or enable its gated publisher. |
| 4 | [Hygiene #60](https://github.com/egohygiene/hygiene/issues/60): organization initiative contract | Propose the canonical owner contract/path, repository membership by reference, state and disclosure semantics. No invented strategic priorities. Enables [Observatory #22](https://github.com/egohygiene/observatory/issues/22) then [organization #29](https://github.com/egohygiene/.github/issues/29); remains distinct from this execution queue and repository roadmaps. |
| 5 | [Hygiene #62](https://github.com/egohygiene/hygiene/issues/62): status contract | Propose provider-neutral service/incident, applicability, freshness and disclosure semantics. Enables [Observatory #23](https://github.com/egohygiene/observatory/issues/23), [Relay #41](https://github.com/egohygiene/relay/issues/41), [organization #33](https://github.com/egohygiene/.github/issues/33) and [Pace #15](https://github.com/egohygiene/pace/issues/15). No monitors, incident writes or inference that successful CI means healthy service. |

The three consumers depend on review/adoption of Relay #181's exact shared
functional source. Their current `981ddf43` paths lack typed feed wiring; this is
bounded adoption work, not a reason to rebuild existing renderers. The two
Hygiene owner contracts and corresponding Observatory model chains have no
implementation on the refreshed main sources; draft semantics precede models
and renderers. Contract proposals remain proposed pending actual human review.
Tests/CI/runtime/publication qualification stays in RI-06 unless the maintainer
changes the deferral.

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
