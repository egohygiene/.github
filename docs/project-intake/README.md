# Organization Project intake preview

Refs [#51](https://github.com/egohygiene/.github/issues/51).

```sh
python3 scripts/preview_project_intake.py --output /path/to/new-local-preview.json
```

Python 3.10+ and an authenticated GitHub CLI are required. The wrapper works from
stock macOS Bash 3.2; it uses no Bash arrays, `mapfile` or GNU command flags.
GitHub authentication needs read access to public repository issues and the
organization's existing Project 1. Configure credentials outside source.

This first checkpoint implements a read-only preview. The utility cannot add a
Project item or change a field: its REST requests are GETs and its GraphQL
operation is a fixed query. It does not create, close, reopen, relabel or assign
an issue. There is no schedule or automatic rollout.

## Exact declared scope

The preview selects accessible **public** repositories owned by `egohygiene`,
then every open issue, excluding pull requests. Archived repositories remain
in scope when the provider returns them. Private/inaccessible repository
coverage is not inferred, counted or claimed. The public-only default is an
explicit first profile; a private intake needs a separately reviewed output
and access boundary.

REST and Project connections paginate to an explicit end. `--max-pages` bounds
each connection (default 1000, supported 1–10000); reaching the budget before
an end is incomplete, never an empty or fully reconciled result. Invalid,
duplicate or failed provider responses fail closed. Repository errors are
reported independently; a global Project/access error prevents an actionable
preview. Any incomplete result exits nonzero. Access, transport and rate-limit
failures are failures, never evidence of existing membership.

Each public issue has one membership decision: `missing`, `existing`, or
`duplicate`. Existing/duplicate items, including archived Project items, are
left unchanged. The output contains no issue bodies or titles, private item
identities, or hidden-item totals. Summary counts describe only admitted public
issues actually observed. The API is not a transaction: concurrent edits can
invalidate any preview, so no saved preview authorizes a later write.

## Apply checkpoint remains open

The issue's live add/Backlog/readback outcome is separate from this preview.
A future Relay-owned apply adapter must resolve the current Project, Status
field and Backlog option dynamically, re-read membership, and distinguish a
new item from a raced/pre-existing item. It must preserve every existing field,
return partial results, and retain actual readback evidence. GitHub's separate
add/status mutations do not supply a conditional status write; a time window
or successful add alone does not prove that overwriting status is safe. Do not
implement an unconditional status reset or reinterpret any provider error as
"already exists."

The existing [issue-routing policy](../issue-routing.md) retains triage and
ownership. This utility does not complete backlog normalization #23. Later
owner mappings and a private/public profile remain outside this initial scope.

## Source review

The committed fake-transport cases cover pagination, missing/existing/duplicate
membership, PR exclusion, private admission, per-repository failure and page
budget exhaustion. On 2026-11-15 the complete local 44-test contract suite passes
with zero skips. The same suite and deterministic projection also pass in
[hosted run 43662602146](https://github.com/egohygiene/.github/actions/runs/43662602146).

The actual read-only provider preview was attempted separately; its [dated access receipt](../evidence/project-intake-access-2026-11-15.json) retains the failed preview and an independent minimal Project query. Its Project
transport is incomplete, with no actionable membership result: a minimal
Project 1 query returns GraphQL FORBIDDEN, "Resource not accessible by
integration." This is missing provider access, not evidence of an empty board
or existing membership. No add/status mutation, Backlog pilot or board change
occurred. Actual Project access and the Relay-owned safe apply/readback path
remain open under #51.

ADR not required: this is a read-only initial intake adapter under the existing
organization coordination boundary. Reusable provider mutation belongs to Relay.
