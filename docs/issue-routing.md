# Organization Issue Routing

The `egohygiene/.github` repository is the organization-level intake and coordination surface. It is not the default implementation repository for work that already has a durable owner.

## Routing rule

Route work to the narrowest durable owner that can complete it without copying another repository's implementation.

Use `.github` when work is genuinely organization-facing or when ownership is not yet known. Once an owner is established, keep the umbrella issue here only when cross-repository coordination remains useful and link to the implementation issue instead of duplicating its checklist.

## Intake states

| State | Meaning | Next action |
| --- | --- | --- |
| `needs-routing` | No durable owner is established yet. | Identify the capability and candidate owners. |
| `routed` | An implementation owner is known. | Link the owning issue/repository. |
| `cross-repo` | Multiple repositories must coordinate through explicit contracts. | Keep an umbrella issue and link bounded implementation issues. |
| `blocked` | A dependency prevents useful implementation. | Record the dependency and unblock condition. |
| `ready` | Scope, owner, dependencies, and acceptance criteria are sufficient for implementation. | Execute in the owning repository. |

These names describe the intended taxonomy. Label creation/synchronization should be performed by the organization automation owned by Relay rather than hand-maintained independently in every repository.

## Stable label taxonomy

The organization taxonomy should remain deliberately small.

### Priority

- `priority:p0` — correctness, security, or data-integrity blocker.
- `priority:p1` — required foundation or near-term release work.
- `priority:p2` — important planned capability.
- `priority:p3` — research, exploration, or later direction.

### Type

- `type:architecture`
- `type:feature`
- `type:bug`
- `type:documentation`
- `type:research`
- `type:maintenance`

### Area

Use `area:<domain>` only for stable domains that improve filtering. Do not create a label for every component or repository.

### Coordination

- `cross-repo`
- `needs-routing`
- `blocked`
- `ready`

Repository-specific overlays may add labels, but must not redefine organization label semantics.

## Umbrella issues

An umbrella issue owns coordination, not duplicated implementation.

It should contain:

- the organization-level outcome;
- the owning repositories;
- dependency edges;
- links to implementation issues;
- integration acceptance criteria.

Implementation details belong in the repository that owns them. Closing an implementation issue does not automatically close the umbrella issue until the cross-repository outcome is verified.

## Routing examples

| Request | Owner |
| --- | --- |
| Organization profile/community defaults | `.github` |
| Canonical architecture/policy/catalog | `hygiene` |
| Repository baseline/template contract | `empathy` |
| Repository materialization | `holon` |
| AI artifacts and provider projections | `aether` |
| Reusable GitHub Actions | `relay` |
| Lint semantics | `egolint` |
| Development environments | `realm` |
| Portable shell/workstation behavior | `mantle` |
| Fleet convergence | `pace` |
| Fleet visibility/evidence | `observatory` |
| Unknown experimental capability | `.github` for routing, then `sanctuary` when incubation is appropriate and available |

## Security and destructive work

Issues involving secrets, signing, production infrastructure, billing, destructive migration, personal/private data, or external publication must state the trust boundary and required human approval. Do not place credentials or sensitive values in issues.
