# Shared issue authoring

The existing [title contract](../.github/issues/title-contract.v1.json),
[title semantics](issue-titles.md) and [label catalog](../.github/labels/catalog.v1.json)
own the emoji/type mapping, subject rules and universal labels. The small
[body contract](../.github/issues/authoring.v1.json) is the draft shared field
definition for UI forms and API/agent authoring; it creates no second taxonomy.

Choose exactly one primary type. Forms provide a matching title prefix and
primary label; replace the empty subject with a concrete action. Other labels
and the native GitHub issue type remain independent. Keep stable IDs and links
in the body; a decorated title does not establish parentage or completion.

Every path supplies an outcome, owner or routing state, bounded scope,
dependencies (or explicit none), reviewable acceptance/validation, and trust
boundary. A checkpoint additionally supplies its parent URL/native identity and
its stable checkpoint ID. The checkpoint form uses maintenance as its initial
type; change the prefix and primary label together if another type is correct.
The [API examples](../fixtures/issue-authoring/examples.v1.json) demonstrate the
same fields. Aether's portable issue-authoring guidance consumes the pinned
contract; these source files do not install that skill in every clone.

Repository extensions may add domain fields. Preserve the universal meanings
and required fields; do not redefine a primary label. A local form directory
must carry its own complete selected forms because GitHub replaces the default
directory as a unit, rather than merging its files.

Before adopting a form, verify all referenced labels exist in that receiving
repository. The source catalog is not evidence of provider availability.
Missing labels require the existing Relay-owned enrollment path, not an invented
classification or a claim of enforcement. These candidate forms are not proof
that every consumer is enrolled. See [community fallback decisions](community-health.md).

The form files use the JSON subset of YAML, so the existing dependency-free
checks can parse their complete structure and compare UI/API fields without
introducing a separate YAML runtime. GitHub still discovers them as `.yml`
issue forms.

Editing templates affects new issue entry only. Historical normalization stays
under [#23](https://github.com/egohygiene/.github/issues/23) and the existing
Relay preview/apply/recovery work. Preview preserves authored subjects, bodies,
IDs and relationships; conformant repeats do nothing, and changed source values
become conflicts. No rename, label provisioning or migration runs in this change.
