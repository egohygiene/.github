# Organization Label Governance

The versioned label contract under [`.github/labels`](../.github/labels) is the
canonical source for Ego Hygiene label names, descriptions, colors, and
repository overlay assignments. Human-facing documentation explains the
contract; it does not redefine it.

Colors use GitHub's provider-ready form: exactly six lowercase hexadecimal
digits without a leading `#`.

## Ownership

- `.github` owns the organization taxonomy, overlay definitions, and repository
  assignments.
- Relay consumes an immutable revision of this contract and owns previewing and
  applying provider mutations.
- Repository owners may request overlays and add genuinely local labels through
  the assignment document. They may not redefine canonical names.
- Pace may later report adoption and drift. It does not mutate labels without a
  separately reviewed Relay plan.

The contract contains no credentials and grants no mutation authority.

## Contract files

| File | Purpose |
| --- | --- |
| `catalog.v1.json` | Universal labels, approved overlays, lifecycle policy, and catalog version. |
| `repositories.v1.json` | Explicit repository adoption and overlay selections. |
| `schema/*.schema.json` | Provider-neutral document shapes for consumers. |

Universal labels are required for every configured repository. Overlays are
opt-in. A repository may add labels only when their names do not collide with a
universal or overlay label.

## Precedence and collision rules

1. Universal definitions always win and cannot be disabled or overridden.
2. Overlay definitions are canonical and cannot be changed by a repository.
3. Repository additions must use unique names and remain owned by that
   repository.
4. Selecting multiple overlays produces their union. Duplicate canonical names
   are invalid rather than resolved by order.
5. An unknown overlay or catalog-version mismatch fails closed before planning
   any provider mutation.

Similar concepts may intentionally have separate universal and expressive
labels—for example, `type:bug` is machine-oriented while `🐛 bug` belongs to the
opt-in engineering overlay. Their distinct names prevent accidental semantic
replacement.

## Lifecycle

Changes follow semantic versioning at the catalog level:

- patch: spelling or clarification that does not change matching semantics;
- minor: additive labels, overlays, or repository assignments;
- major: rename, semantic change, removal, or incompatible schema behavior.

A rename is modeled as an addition plus a deprecation. Deprecations must name a
replacement when one exists and provide a review date. Relay must preview
renames and removals separately from additive synchronization.

Deletion is never inferred from absence. The catalog's default removal policy
is `retain`; destructive removal requires an explicit future contract change,
a generated preview, and human approval. Unrelated manually applied labels on
issues and pull requests remain outside taxonomy synchronization.

## Adoption and rollback

To adopt a repository:

1. Add one entry to `repositories.v1.json` and select only relevant overlays.
2. Run `python scripts/validate_labels.py`.
3. Preview the exact provider-neutral projection:

   ```shell
   python scripts/project_labels.py --repository "egohygiene/example"
   ```

4. Review and merge the contract change.
5. Have Relay consume the merged commit immutably and preview provider changes
   before applying them.

Rollback means reverting the assignment or catalog commit and generating a new
preview. Because the default is retain, rollback does not delete labels or
remove labels already attached to work items.

## Local issue templates

The organization work form is the fallback for organization-level or unowned
work. Repositories should still materialize their own issue templates and
`config.yml`: GitHub inheritance varies by repository visibility and a local
template can express repository-owned policy more accurately. A local template
must retain owner, dependency, acceptance, and security fields when it accepts
cross-repository work.
