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
binds actual successful organization review run `43371630627`, attempt `1`,
source `460bd07960a1dfa85614874e2daa0c29fc2eab48`, artifact `14011999855` and
raw archive SHA-256
`818b8ded0abb5ede0f36c967f6235e06c29be488b691ed6c4dda4046de6cd316`.
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
[composition reference](../../publication/sources/organization-theme-2026-11-13.json),
which points to upstream evidence without claiming ownership of its models.
Twenty UI surfaces are implemented in the selected theme candidate but not yet
deployed; the prior version is live under the separate proof below. The other
sixteen retain
evidence-backed unknown applicability and delivery state. Unavailable model
inputs do not imply that a rendered UI is unimplemented or that an audit passed.
This is an assessment of the selected candidate; live evidence is separate.

## Manual preparation and publication

Use `.github/workflows/organization-intelligence-pages.yml` on canonical main.
Supply the raw selection SHA-256:

```text
0f83a0fc255bb505df7472740e38f3611f28310adb65b48d10672f10875aaae5
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

## Initial publisher qualification — historical 2026-11-13 checkpoint

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

At that initial checkpoint the selected report was one partial historical audit,
and Core/Sanity were unavailable. Its source and receipts remain historical
evidence. Actual prepare-only run `43356501268/1` later passed for that initial
selection; it did not configure or deploy Pages.


## Prior Audit and Sanity selection — historical 2026-11-13 checkpoint

The [actual export/intake evidence](../reviews/2026-11-13-organization-export-intake.json)
records the full retained-artifact chain:

- Public model run [43358630670/1](https://github.com/egohygiene/.github/actions/runs/43358630670)
  retained the actual Audit and Sanity bundle at source `281c3827378ae08bb44cde810ad6467fdb0c8adc`.
- Graph-fixed website export [43361706555/1](https://github.com/egohygiene/egohygiene.io/actions/runs/43361706555)
  succeeded at `342673b110915f4a29ada01625a77416a1e105d7`. All three source
  checkpoints were clean with that exact HEAD. Both native input and admitted
  presentation states are available; Core remains unavailable.
- Organization review [43362027530/1](https://github.com/egohygiene/.github/actions/runs/43362027530)
  admitted the exact static and companion artifacts. Its downloaded retained
  artifact preserves all 43 producer files, the manifest and the companion
  byte-for-byte. The intake receipt remains review-only and deployment-unauthorized.

The original model frame is `2026-11-13T03:23:31Z`; export evaluation is
`03:36:14Z`. There is one `.github` fleet target, containing a Sanity review of
28 components, eight concerns, 28 strengths and 17 dimensions. All eight concern
summaries appear in retained HTML. Execution remains partial, governance
not-reviewed and human evidence unavailable. The canonical Audit has 36 findings;
its target projection retains one positive finding. Neither source clocks nor
these independent scopes are expanded by publication.

The new source pointer was committed first at
`7550df88a67d62de1704105b27556cb6fb723236`; the complete declaration references
that immutable existing blob. It binds the actual website exporter revision,
20 implemented/unpublished surfaces and 16 unresolved applicability assessments.
The original composition pointer and earlier review receipts remain unchanged.

At functional source `8ce7d4501e0fa599b31096974582f72a04e61805`, the unchanged
publisher revalidated the actual 46-member review archive through the pinned
Relay and Hygiene owners. The v2 schema passed. All 43 producer files remained
exact, with only the separate consumer metadata added; no private captures or
CLI state enter the 44-file public site. This local replay is explicitly
`local-unverified`, and the deployable check correctly rejects it.

Independent Chromium replay of these exact hosted 43 site files passes all
12 focused checks: route traversal, pointer and keyboard navigation, first-touch
Sanity concern selection and original partial/human states. No console/page or
response errors were observed. Audit/Sanity detail pages retain a 402px width
at a 390px viewport; the graph hub fits. This is local browser replay, not live
HTTPS or full accessibility acceptance.

At this historical checkpoint, source integration and a later actual
`publish: false` preparation remained ahead, and Pages awaited the administrator's
GitHub Actions source setting after an integration 403. This checkpoint itself
claimed no deployment, live verification or human ratification. The actual later
publication and current candidate are recorded separately below.


## Actual live publication and theme replacement

The administrator configured the project to use GitHub Actions. Actual manual
[publish run 43369556651/1](https://github.com/egohygiene/.github/actions/runs/43369556651)
at `460bd07960a1dfa85614874e2daa0c29fc2eab48` then published the prior 43-file
producer export. The [bounded live evidence](../reviews/2026-11-13-organization-live-publication.json)
records canonical HTTPS equality for every producer file, the separate consumer
provenance, actual first-deployment recovery and live browser navigation through
the root, Audits and Sanity. The canonical entry point is
[Organization Intelligence](https://egohygiene.github.io/.github/intelligence/).
The browser's automatic origin-root favicon request returned 404; no selected
project resource or producer byte mismatch was observed.

Website [PR #147](https://github.com/egohygiene/egohygiene.io/pull/147) added
System, Light and Dark appearance using the existing shared preference.
Actual retained-model export
[43371316736/1](https://github.com/egohygiene/egohygiene.io/actions/runs/43371316736)
at `d8f9a7c706ef4cc477b0cf7201dd6c9f128d985a` produced 44 sealed files for the
same 39 routes. The new file is `assets/theme-preference.js`; all 40 HTML files
load it before content and any stylesheet. Original Audit/Sanity source and
presentation hashes, model clocks, partial scope and unavailable Core remain
unchanged. All three actual source observers were clean at that exact producer.

Organization review
[43371630627/1](https://github.com/egohygiene/.github/actions/runs/43371630627)
admitted the exact static and companion archives. Its 47 retained members
preserve the producer bytes and both review receipts. The new immutable
composition pointer was committed at `82e4ba749daebc05377e456a87833ea03cb19c54`;
the declaration and selection above reference that candidate without rewriting
the historical sweep pointer or promoting review-only receipts.

After this candidate is reviewed and integrated, the existing manually
authorized publisher can replace the current site. It must capture and verify
the actual prior publication `63e3f2e57cd261ceea4dbb3bf6cb0b92a4df88d91cfa4a0ebd93ccfb14c89322`
and all 44 previous public files before deployment. The new public inventory
will be 44 producer files plus separate consumer provenance. Replacement live
bytes and actual appearance behavior remain the next checkpoint; this candidate
does not claim them. The company publisher and repository-specific publishers
retain their ownership, and neither hosting ADR is ratified by publication.
