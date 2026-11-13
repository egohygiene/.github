# One real report through Organization Intelligence

This bounded checkpoint implements the next step of organization
[#41](https://github.com/egohygiene/.github/issues/41). It uses the existing
Aether report contract, Observatory models, Relay builder, website export and
organization intake. Repository publishers retain their owners.

The first full hosted trace is now
[verified](../reviews/2026-11-13-real-report-proof.md), including the real finding
in the retained organization review site. The instructions below describe its
repeatable path; source merge, actual artifact proof and live publication remain
distinct.

## Actual source assessment

The [canonical report](../../audits/ri-review-boundary-20261112T234641Z.md) and
its [typed sidecar](../../audits/ri-review-boundary-20261112T234641Z.json) record
an actual inspection of two files at organization source
`8aef67662f3cf832cc1457ac24ed88f9bf9d2ae7`:

- the organization review workflow is manual, read-only and restricted to main;
- the source guide documents the same artifact-only boundary.

The selected `contract-drift@1.0.0` profile is explicitly **partial**. There is
one observed positive finding. This is a source assessment, with no whole-repo
conformance, fresh organization sweep, human approval or publication claim.
The original report and clock remain immutable when the canary is rebuilt.

The plan at `.config/repository-intelligence/review-plan.json` selects the
exact raw sidecar hash. Sanity has no selected report and remains unavailable.
The report represents the earlier inspected source; later model receipt source
revisions correctly show that historical context rather than retiming it.

## Review artifact producer

Run the manual
[`repository-intelligence-canary.yml`](../../.github/workflows/repository-intelligence-canary.yml)
workflow on this repository's canonical main. It checks out the exact source
with full history, captures one evaluation boundary and supplies the same
revision/clock to the typed feed and existing dashboard builder. Both select
Relay functional source `5d27be5ce1599df883e31f14cd894eb18622c18c`.

It retains two separate ordinary artifacts:

- `repository-intelligence-real-review-v1-<run-id>-<attempt>`: exactly the four
  repository/fleet models and `review-feed-receipt.json`. It is retained before
  building the dashboard, so a later failure does not erase this partial result.
- `repository-intelligence-real-dashboard-v1-<run-id>-<attempt>`: only the
  generated repository dashboard, including the Audits route.

The run summary records actual source, evaluation boundary, feed receipt hash,
artifact IDs and archive digests. A model upload, successful dashboard and
organization export remain separate observations. A failed producer run is not
eligible for the website's success-only retained-artifact admission.

## Continue through the existing export and intake

1. Verify the exact successful canary run/attempt and download its actual model
   artifact. Recompute the raw ZIP and `review-feed-receipt.json` hashes.
2. In the website owner, check in one explicit model selection binding that
   public producer revision, workflow path, run/attempt, artifact name/ID and
   hashes. Select the Audits fleet model; other modules may remain unavailable.
   Preserve each original module and report clock.
3. Run the website's existing manual retained-model export. Verify the exact
   static export and separate model-selection companion artifacts from that
   same producer run/attempt. No capture replay can substitute for real
   provider acquisition or mint the final public selection receipt.
4. Supply those exact artifact identities and hashes to this repository's
   existing organization review workflow using `producer_profile: retained-models`.
   Retain the sealed review directory and selection receipt.

The intended review target remains `https://egohygiene.github.io/.github/`.
ADR-0006 remains proposed and approval remains null. The older website host
stays a migration reference; one canonical publisher still needs declaration,
host/base-path, navigation and rollback qualification before cutover.

## Evidence and remaining acceptance

The pinned Aether owner validator and actual local typed feed were executed
for the initial committed candidate. They produced one partial audit run and
one finding; the report revision is `different`, while Sanity is unavailable.
These checks establish local normalization of this report, not provider
transport, application execution or publication.

The [dated proof](../reviews/2026-11-13-real-report-proof.md) now records actual
producer/export/intake runs, exact artifacts and original clocks. Required
steps executed, the audit input and presentation are available, all declared
export bytes were verified, and the final retained site preserves the real
finding and its partial label. A green preparation step alone is insufficient:
it can intentionally return unavailable module inputs.

Subsequent refreshes need their own exact run/attempt, artifact IDs, hashes and
inspected content. Broad CI, browser qualification, live Pages activation and
a full organization sanity sweep remain separate work. The original partial
report and source observations must not be retimed to manufacture freshness.
