# Organization Intelligence Pages publisher

The organization publisher consumes an existing sealed review artifact. The
website remains the UI/export owner; Hygiene owns declarations and Relay owns
static-export validation. This publisher adds no renderer, model assembler,
company-site deployment, custom domain or repository-dashboard publisher.

The target is `https://egohygiene.github.io/.github/`. The source change and a
successful preparation are distinct from Pages configuration, deployment and
live verification. ADR-0006 and Hygiene ADR-0020 remain proposed with null
approval. Explicit repository-owner publication authorization and a manual
publish dispatch are separate from those human decision records.

## Reviewed selection and owner sources

The checked-in [selection](../../publication/organization-intelligence-selection.json)
binds actual successful organization review run `43339209486`, attempt `1`,
source `b1539be1ab718de2db3da4b1eaa6827e36d4753f`, artifact `13998892236` and
raw archive SHA-256
`d23cb76f235f473a5955e0aaade6c7e6afd493d80eb873ea241e4ba1f9caeb96`.
It also binds the original producer, sealed manifest, intake receipt and model
selection receipt. The original review receipt stays `review-only`, with
`deployment_authorized: false`; it is not edited into publication permission.

The exact selected owner sources are:

- Relay `d15cacd987ef1f98a6b94b051a42925eb91f8cc7`, retaining the native
  sealed-export and public-admission checks already exercised by the review.
- Hygiene `6aa97ae2bf44abacb83e698281c1fffdba8eaf49`, selecting the explicit
  organization export hosting dialect, unchanged v1 state/route/privacy rules,
  and canonical compositor/publication ownership reconciliation.

The selection includes their required raw source/resource hashes. Git identity,
clean owner checkouts and hashes must all agree before owner code is loaded.
No source is loaded from a candidate artifact or a mutable branch.

The [complete declaration](../../publication/organization-site-surfaces.json)
uses the narrowly scoped v2 hosting profile and the same 36-surface registry.
It names the actual website renderer and exact producer commit. Its semantic
source is this repository's immutable
[composition reference](../../publication/organization-intelligence-source.json),
which points to upstream evidence without claiming ownership of its models.
Twenty UI surfaces are implemented but unpublished; the other sixteen retain
evidence-backed unknown applicability and delivery state. Unavailable model
inputs do not imply that a rendered UI is unimplemented or that an audit passed.
This is a dated prepublication assessment; later live evidence is separate.

## Manual preparation and publication

Use `.github/workflows/organization-intelligence-pages.yml` on canonical main.
Supply the raw selection SHA-256:

```text
36eae53d26e6387b7ff8ec2203aced90318994148867e15dde3ea9b961ed535c
```

`publish: false` is the default. The read-only preparation authenticates the
public repository, exact successful manual review run/attempt/source, artifact
identity/name/digest, lifetime and archive bytes. It then revalidates the sealed
export through Relay and the complete declaration through Hygiene. Any missing
artifact, failed owner check or malformed input blocks the handoff. There is
no degraded or unverified publishing fallback.

Every producer site file remains byte-identical. A separate consumer-owned
`organization-intelligence-publication.json` records source/provenance, the
selected declaration digest and complete producer inventory. Its `export_as_of`
is the export evaluation clock; it does not refresh the original model/report
clocks. Raw provider captures, CLI device state and the original receipts are
outside the public site. The ordinary prepared artifact retains the public site
and selected source evidence, excluding acquisition packets and process state.

`publish: true` additionally permits the separate deployment job. Only that job
has Pages write/OIDC permissions and the `github-pages` environment. It downloads
this run's exact prepared artifact ID, binds its publication hash and consumer
revision, and checks every byte again. Runs serialize without cancellation.

Pages must already be configured to use GitHub Actions. The workflow explicitly
disables automatic enablement and requires the provider's exact project base
URL. It never writes DNS, CNAME, a custom origin, company hosting or another
repository's settings. Configuration/activation belongs to the coordinated
operator action after source and necessary qualification are reviewed.

## Recovery and live evidence

Before deployment, the publisher checks the canonical HTTPS publication
manifest. Both that manifest and the root must return 404 to establish the
first-deployment condition. A root without an admitted manifest is rejected.
For a replacement, every prior public file is downloaded and hash/size-checked
before it is retained as a recovery artifact. Redirects, TLS/network errors,
unmanifested existing content and incomplete recovery block deployment.

The recovery artifact is uploaded before `deploy-pages`. A first deployment has
no fictional previous revision: its recovery action is to unpublish through
the repository's Pages settings, then publish a reviewed successor. A later
replacement retains the prior site bytes for a separately controlled restore;
no automatic rollback is installed or claimed exercised. Recovery and live
evidence artifacts retain available evidence for 90 days; preserve a required
recovery point before expiry.

After the provider deploys, verification compares the publication manifest and
every public producer file over verified HTTPS. Directory routes use their
declared URLs; `.nojekyll` is checked locally as a GitHub control file. Custom
404 content must match even when served with HTTP 404. Only complete equality
writes a success receipt binding source, publication digest, selected review,
actual workflow run/attempt, verification time and recovery condition. A failed
deployment or verification retains available recovery evidence but never writes
a success receipt. Provider failure does not prove the prior deployment stayed
unchanged.

## Executed preparation evidence

At functional source `77a04f800a398ee1971b6d069b5d7846a969609b`, eight focused
publisher tests passed. They cover exact hash/source binding, changed/missing/
extra/symlink files, local-replay denial, CNAME denial, first-deployment checks,
complete prior-site recovery, live drift without a success receipt, redirects,
custom 404 handling and unsafe/duplicate metadata. These tests use synthetic
local data and mocked HTTPS, with no provider write or real credential.

The actual downloaded 46-file review archive was also revalidated offline
through the exact Relay and Hygiene helpers. The native v2 declaration schema
passed. All 39 routes and 43 producer site files retained exact bytes, with only
the separate consumer provenance file added. Acquisition was explicitly marked
`local-unverified`; the deploy boundary correctly rejected that replay. It
cannot mint provider acquisition, deployment or publication proof.

An actual main-workflow preparation/publication, browser qualification and
canonical live/recovery evidence remain separate next checks. The selected
report remains one partial historical audit; Core/Sanity are unavailable.
The organization-wide sanity sweep is a separate source-backed collection task,
not a result of publishing this artifact.
