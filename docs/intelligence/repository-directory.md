# Reviewed repository navigation

[Directory JSON](repository-directory.json) supplies repository links even when
the organization Core model is unavailable. Its
[versioned schema](repository-directory.schema.json) is a presentation input;
it does not create Core rows, health scores, model coverage or fleet evidence.
The website owns loading, rendering and export. This repository owns the reviewed
input and organization publication selection, with separate authority boundaries.

## Source ownership and scope

Hygiene remains the canonical catalog and ecosystem architecture owner under
[accepted ADR-0001](https://github.com/egohygiene/hygiene/blob/49639c1845cdfd08fbd5a768261a8b3cf515f80f/docs/decisions/ADR-0001-holistic-architecture-v0.1.md)
and [the local decision](../../DECISIONS.md). This is a projection of the existing
[dated source inventory](repositories.source.json), whose reviewed public roster
is pinned to Hygiene `49639c1845cdfd08fbd5a768261a8b3cf515f80f`,
`catalog/public-repositories.json`, SHA-256
`af9c7186ded0bb57b18741eaa5905314b96d6adb03736946c868e0fc4aa50b26`.

The inventory's original SHA-256 is
`c4e41df201500c5a00aa7b0e5e30cc4d8054f33eb39c842718266c70530175a9`.
All 28 admitted entries retain their original identities and source observations.
This is a fixed reviewed public scope, not a current organization total. The
projection adds no repository roles, lifecycle, relationships or adoption claims.
[Issue #42](https://github.com/egohygiene/.github/issues/42) remains open for its
broader canonical registry and relationship coordination.

## Link and publication states

| Link state | Meaning | Publication state |
| --- | --- | --- |
| `publication-recorded` | A retained reviewed packet records publication at its stated source/run and observation time. | `recorded`, with pinned evidence. |
| `source-declared` | Inspected source declares both Intelligence Pages composition and a destination. | `unknown`; no successful run or live probe is inferred. |
| `unknown` | The inspected inputs do not establish a dashboard destination. | `unknown`; the repository link remains available. |

The first projection has two publication records: the
[organization hub](../reviews/2026-11-13-organization-live-publication.json) and
[Empathy](../reviews/2026-11-14-foundation-selected-ten.json). Akashic, Hygiene
and Identity retain source-declared dashboard destinations with unknown
publication. The other 23 destinations remain unknown; preview references and
composition declarations without an origin do not become dashboard URLs.

Recorded publication means dated evidence exists. It does not promise current
availability, unchanged content, complete collectors, clean scanners, current
models or human approval. Organization Core stays unavailable. Existing partial
and unreviewed organization models are unchanged. Empathy's native scanner and
layout findings remain in its linked packet.

The organization observation uses the actual hosted receipt's
`2026-11-13T05:32:30Z` verification clock. Empathy uses the containing packet's
`2026-11-14T06:35:35.745Z` observation clock; it is not a new live verification
time. Catalog, inspected source and each publication keep separate clocks.
No projection-generation clock refreshes them.

## Consumer contract

Consumers pin the containing `.github` commit and exact directory payload
SHA-256. In-payload source references identify the earlier immutable input
revision; they are not a self-checksum or the directory's containing revision.
The initial projection's payload SHA-256 is
`d29435982560531d31e7698c31fb40e55cfc0849615f4d094be6cb4342ee04fd`.

Load this as an optional navigation capability, separately from Core model
admission, module availability, coverage and aggregate health. If absent or
rejected, render the existing model state and an explicit unavailable directory.
Do not substitute catalog entries into historical `repositories` model rows.
Show a dated publication record or source declaration as such; avoid a current
"healthy", "live" or "available" badge inferred from either.

Validate the schema, unique repository names/provider IDs, matching repository
links, run ownership and link states before rendering. Accept only canonical
public HTTPS URLs: `github.com/egohygiene/` for repository/evidence links and
organization-owned `egohygiene.io` subdomains or `egohygiene.github.io` for
dashboard destinations. Reject credentials, ports, queries, fragments, control
characters, encoded aliases and parent-path traversal. Render labels as text.
The structural schema is supplemented by the native semantic validator;
structural validity alone does not authenticate publication evidence. The native
validator binds the complete admitted roster, source observations, declared
destinations and named publication records to the pinned original inputs. A
plausible new link or syntactically valid replacement receipt is rejected.

## Review and update

Run the offline deterministic projector and its focused contract controls:

```sh
python3 scripts/project_repository_directory.py --check
python3 -m unittest discover --start-directory tests --pattern test_repository_directory.py
```

The projector reads only digest-pinned source inventory and two existing public
review packets. It never fetches URLs, discovers repositories, executes consumer
code or writes provider state. `--check` compares the committed complete output
to those exact inputs, including admission, identity, state and clock bindings.
Without `--check`, it regenerates only the local JSON projection.

To add or retire a repository, update and review Hygiene's canonical catalog
first, then explicitly review the admitted public inventory and projection pin.
Do not silently rewrite the roster from provider discovery. To add a publication
record, retain a dated source/run-bound public proof packet, review its pinned
adapter and regenerate the projection. Unknown publication is a useful state;
do not replace it with an assumed workflow success.

No polling results or high-frequency CI state belong in these default-branch
inputs. Future live observations use retained artifacts or another separately
reviewed generated-state surface. Website loader/export integration and actual
organization publication remain separate, reviewed steps.
