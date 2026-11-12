# Organization home: source and review path

The profile and repository README are the initial organization entry point.
They link the [completion queue](DELIVERY_ROADMAP.md),
[repository directory](repositories.md) and existing organization views.
The proposed [hosting decision](../decisions/ADR-0006-organization-intelligence-entrypoint.md)
keeps every repository's own dashboard and existing domain owners.

## First artifact path

1. The website source owner exports a focused organization application through
   its manual `.github/workflows/intelligence-static-export.yml` workflow. It
   requires an explicit intended HTTPS origin and base and excludes the company
   site/store build. The ordinary artifact is
   `organization-intelligence-static-v1-<run-id>-<attempt>`.
2. Supply its exact public producer source commit, run/attempt, artifact ID,
   raw ZIP SHA-256, manifest SHA-256 and intended origin/base to this repository's
   manual [review workflow](../../.github/workflows/organization-intelligence-review.yml).
   Only a successful manual run on the producer's canonical main is eligible.
3. The workflow verifies GitHub transport metadata and raw archive digest, then
   invokes Relay's pinned static-export intake. Relay verifies the producer-owned
   manifest, public scope, complete file inventory, routes and source/origin/base
   bindings without executing the application.
4. Retain only Relay's verified review directory and receipt as an ordinary
   artifact. Raw provider metadata, transport captures and credentials are not
   uploaded. Review the artifact before any publisher activation.

Source reviews: [website #139](https://github.com/egohygiene/egohygiene.io/pull/139),
[Relay #180](https://github.com/egohygiene/relay/pull/180), and
[Hygiene #101](https://github.com/egohygiene/hygiene/pull/101). The workflow selects
Relay `d15cacd987ef1f98a6b94b051a42925eb91f8cc7`; its producer-owned schema/route
lock selects website `54e0b6e66b9b028bad382bbbc4bc6ba588cee665`.

The workflow has only contents/actions read permissions. It has no Pages job,
OIDC permission, DNS/CNAME mutation, schedule or automatic deployment. It is
manual-only on this repository's main. The proposed project target is origin
`https://egohygiene.github.io` with base `/.github/`; those values are review
intent, not proof that Pages is configured or live.

## Retained-model producer profile

The default `static` producer profile retains the original workflow and input
contract. The optional `retained-models` profile selects the website's manual
`.github/workflows/intelligence-model-artifacts-export.yml` producer. That path
selects exact existing core/Audits/Sanity model bundles, preserving each module's
own observation clock and failure state before invoking the same sealed exporter.
It does not assemble another fleet or fabricate reports, artifact IDs or hashes.

For this profile supply the additional exact companion artifact ID, raw companion
ZIP SHA-256 and `model-selection-receipt.json` SHA-256. Its expected name is
`organization-intelligence-model-selection-v1-<run-id>-<attempt>`. Both ordinary
artifacts must belong to the same admitted public producer revision/run/attempt.
The consumer checks the companion against the exact Relay-verified export
manifest, admitted presentation identities, intended project target and module
clocks before retaining it. The companion is outside the static ZIP; it does not
expand Relay's sealed site format or publication inventory.

`scripts/verify_intelligence_model_selection.py` reads the exact dated public
source inventory already checked in here to admit provenance repository names.
That is a pinned observation projection, not a new registry or a claim about
current organization totals. Refreshing it requires a separately reviewed source
and digest change. Raw model packets, provider captures, rejected source names,
credentials and their acquisition-only checksums are not uploaded.

Each module may remain unavailable, incompatible, stale or partial. A source
artifact being accessible does not make the underlying audit complete, a
repository conformant or an architecture human-ratified. The companion binds
producer declarations to admitted presentation; it does not replay upstream
normalization or authenticate human claims. The workflow remains review-only.
Its input `state` and literal native `presentation_state` are separate: a
compatible file can still present stale evidence or no authored records.

GitHub may require a read credential for another repository's retained artifact.
The workflow uses `INTELLIGENCE_ARTIFACT_READ_TOKEN` from repository secrets when
configured, otherwise its normal GitHub token. An inaccessible artifact fails
admission; it does not enable a weaker download path. Configure credentials only
through GitHub settings, never in source files or issue text. Actual API/token
and artifact transport qualification remains separate.

## Activation gates

- Review the proposed hosting transition and reconcile Hygiene's catalog,
  compositor/publication declarations and #41's older host criterion.
- Select the exact compatible `/.github/` schema/helper correction merged in
  [Hygiene #101](https://github.com/egohygiene/hygiene/pull/101). Existing pinned
  selections do not gain that admission automatically.
- Retain the organization route profile beneath the deployment prefix; use
  redirects for aliases and one canonical publisher after cutover.
- Supply actual admitted owner models and qualify the export, intake, base-path,
  source/Pages provenance, failure behavior and rollback before publication.

Source implementation alone does not establish site-declaration admission,
successful application execution, live publication, human ratification or
full-fleet adoption. The next authorized checkpoint is the
[one real report canary](real-report-canary.md), using the existing producer,
exporter and review consumer. Its focused execution is separate from broad CI,
browser qualification, live publication and a full organization sanity sweep.
