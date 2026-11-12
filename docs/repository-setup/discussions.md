# Discussions setup checkpoint

Refs [organization #54](https://github.com/egohygiene/.github/issues/54),
[community health #24](https://github.com/egohygiene/.github/issues/24) and
[repository setup #32](https://github.com/egohygiene/.github/issues/32).

The [organization checklist](../../checklists/organization-discussions.json)
records two distinct results: the provider's actual `enabled` setting and the
actual `starter_discussion_url` with category and dated verification. A local
form, README link, authored draft, successful source check or merged PR cannot
satisfy either result. This is proposed organization setup evidence, not a new
universal Hygiene profile or an accepted fleet requirement.

## Canary observation

A read-only GitHub REST/GraphQL inventory of public `egohygiene/.github` is
retained in the [dated observation](../evidence/discussions/2026-11-12-organization.json).
At its exact recorded time, Discussions was disabled and the complete returned
category/discussion connections were empty. The checklist therefore says
`enabled: false`, has no category or starter URL, and remains **blocked**. This
is an observed configuration state, not a failed canary post or evidence that
other repositories lack Discussions.

The [purpose-aware starter](organization-discussion-draft.md) is a reviewable
content draft. Its emoji follows the existing organization README's brain
prefix. It neither creates a discussion nor selects a nonexistent category.
Provider enablement, category selection, posting and readback are later selected
execution steps; this first checkpoint performs none of those mutations.

## Shared profile and owner references

The record pins Hygiene's proposed repository-presentation contract and
Empathy's existing `community-health` foundation profile by exact revision/file
hash. They retain their own lifecycle, schemas, composition and applicability.
The checklist is a companion record: do not add unsupported fields directly to
those closed manifests or treat this JSON as proof that their contracts already
include a Discussions rule. A future compatible common-profile amendment and
consumer adoption belong to those owners. Hygiene #64 retains documentation
navigation policy; this guide does not select or migrate its layout.

- Hygiene owns universal applicability and policy; exceptions remain explicit.
- Empathy owns baseline/profile composition and setup slots.
- Holon owns materialization; files alone cannot configure GitHub.
- Relay owns reusable provider setup/readback mechanics.
- Pace owns reviewed repository-scoped rollout.
- `.github` owns this organization setup checklist and reviewed starter prose.

## Resume without duplicates

1. Select one repository and verify public/private boundaries and archived state.
2. Inventory its actual enabled setting, all categories and all existing
   discussions with complete pagination. An incomplete/error response is unknown.
3. Reuse an existing suitable starter. Preserve conversations and categories;
   title matching alone cannot prove identical purpose or justify a second post.
4. If configuration/content is missing, retain a blocker and review the exact
   settings/category/content plan. Unsupported, archived or differently governed
   repositories need explicit applicability/exception evidence.
5. When a later selected execution step occurs, record the actual discussion URL,
   category and readback timestamp. Re-read the existing starter before posting;
   retries after ambiguous failures must inventory/read back rather than repost.
6. Mark completion verified only after enabled/category/starter purpose and URL
   have actual provider evidence. Retain the original observation; a schema pass
   is only structural validation and does not authenticate the provider claim.

The schema validates fields and requires a true enabled value, actual starter
URL/category/date and no blocker for a `verified` record. It cannot authenticate
content, human review or a live provider. No credentials, private source bodies
or generic fleet totals belong in public examples.

## Review boundary

Only the public canary inventory was executed. Source/schema/reference checks
are distinct from tests, CI, provider mutations, a canary post and live rollout
qualification, which remain deferred or outside this checkpoint. Issue #54's
real enabled-and-posted canary criterion remains open.

ADR not required: this adds bounded organization checklist evidence and a draft
under existing profile/owner boundaries, without changing policy or provider
configuration.
