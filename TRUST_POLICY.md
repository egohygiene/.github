# Ego Hygiene Repository Trust Policy

| Field | Value |
| --- | --- |
| Policy ID | `ORG-05` |
| Version | `1.0.0` |
| Status | Normative policy; staged repository enforcement |
| Owner | `egohygiene/.github` |
| Effective | When the pull request adopting this version is merged |
| Review cadence | At least annually and after a material trust-boundary change |

## 1. Purpose

This policy establishes one organization-wide contract for contribution
attestation, cryptographic signing, software-bill-of-materials (SBOM) evidence,
build provenance, exceptions, and staged adoption.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**,
and **MAY** are normative. A repository is not enforcing a requirement merely
because this policy exists; enforcement begins only when that repository has an
explicit adoption state as described in section 8.

## 2. Scope and trust model

This policy applies to public and private repositories owned by Ego Hygiene and
to artifacts the organization publishes from them. It covers human and
automated contributions, source history, tags, releases, packages, containers,
and published document bundles.

The policy separates three claims:

1. **Attestation** answers who asserts authorship and licensing authority.
2. **Signing** binds an identity to a commit, tag, or artifact digest.
3. **Provenance** records how an artifact was produced from source and material
   inputs.

None substitutes for the others. A DCO sign-off is not a cryptographic
signature, a signature does not describe a build, and an SBOM does not prove
how an artifact was built.

Private keys, signing tokens, identity-provider credentials, and recovery
material MUST NOT be committed to a repository, embedded in an image, copied
into a template, printed in a log, or attached as release evidence. Automation
SHOULD prefer short-lived workload identity over long-lived signing secrets.

## 3. Contribution attestation (DCO)

### 3.1 Decision

Ego Hygiene uses the [Developer Certificate of Origin
1.1](https://developercertificate.org/) (DCO) sign-off as its contribution
attestation. Every human-authored commit introduced to a protected default
branch MUST contain a trailer in this form:

```text
Signed-off-by: Contributor Name <contributor@example.com>
```

Contributors SHOULD create it with `git commit --signoff`. The name and email
MUST identify the contributor and MUST be an identity the contributor is
authorized to use. Adding a sign-off asserts the DCO for that commit; it does
not transfer copyright and does not require publishing a private email address.

When a sign-off is absent or incorrect, the contributor MUST amend or rebase the
affected commit. Reviewers and automation MUST NOT add a trailer on someone
else's behalf. Squash, rebase, and merge strategies MUST preserve an auditable
attestation for every human contribution represented by the resulting history.

### 3.2 Automated contributions

An automated commit MAY be exempt from a DCO trailer only when all of the
following are true:

- it is authored by an approved GitHub App or unambiguously identified bot;
- it is proposed through a pull request rather than silently pushed;
- the repository adoption record names the bot class and accountable owner;
- the run records its source workflow and immutable action or tool versions; and
- required review and branch protections still apply.

Human-authored content relayed through a bot is not an automated contribution
and remains subject to DCO. A bot exemption is not a blanket exception for the
person who configured or invoked it.

### 3.3 Enforcement behavior

Relay owns the reusable DCO check. In `piloting`, the check reports every
nonconforming commit without blocking merge. In `enforcing` and `conformant`, it
MUST be a required, fail-closed check on protected branches. A transient check
failure MUST NOT be treated as a pass.

History that predates a repository's recorded effective date is not rewritten
solely to add sign-offs. New commits, cherry-picks, and substantive rewrites of
that history are evaluated as new contributions.

## 4. Signing expectations

Signatures MUST bind the signed subject to an immutable digest. Verification
instructions and the expected signer or workload identity MUST be published
without publishing secret material. Keyless workload identity is preferred for
automation; managed hardware-backed or otherwise protected keys are acceptable
when keyless signing is unavailable.

| Subject | Organization expectation |
| --- | --- |
| Commit | DCO is REQUIRED for human contributions. All maintainers SHOULD use cryptographic commit signing; it is REQUIRED for a human-created release commit in classes `R2` and `R3`. A verified GitHub App identity satisfies the signing requirement for an automation-created release commit. |
| Tag | Every public release tag in classes `R1`, `R2`, and `R3` MUST be an annotated, verifiable signed tag or have an equivalent provider-verifiable release attestation bound to the tag commit. Mutable release tags MUST NOT be reused. |
| Release | Every class `R2` or `R3` release MUST publish a digest manifest and verifiable signature or attestation covering every primary artifact. Release notes MUST identify source commit, workflow, provenance, SBOM, and verification locations. |
| Container | Every published image MUST be signed by immutable digest. A multi-architecture index and each referenced platform manifest MUST remain traceable to the same release evidence. Verification MUST reject a tag-only identity. |
| Package | Every published package or binary MUST have a digest-bound signature or attestation. Ecosystem-native trusted publishing SHOULD be used where available; it does not remove the provenance requirement. |
| Document | Source Markdown and ordinary documentation commits follow the commit rules. A published PDF, PDF/A, archive, specification bundle, or other versioned document artifact MUST appear in a signed digest manifest and carry provenance for its generator and source commit. |

An artifact MUST NOT be described as signed when only its checksum is present.
A checksum detects change but does not authenticate its publisher.

## 5. Repository classes

Every adopting repository MUST declare one or more classes. Requirements are
applied to each output; when a repository spans classes, the strongest
applicable requirement governs that output and its release path.

| Class | Description | Typical outputs |
| --- | --- | --- |
| `R0` | Organization metadata, policy, source documentation, or an unbuilt profile | Markdown, templates, policy files |
| `R1` | Source or automation without a separately distributed build artifact | applications deployed from source, reusable source, sites, non-release workflows |
| `R2` | Versioned distributable software or document bundle | packages, binaries, GitHub Actions, reusable workflow releases, archives, PDF/A bundles |
| `R3` | OCI or equivalent machine image | single-platform images, multi-architecture indexes, development or runtime images |

Repository classification describes published outputs, not perceived project
importance. A documentation repository becomes `R2` for a published PDF bundle;
a package repository that also publishes an image applies both `R2` and `R3`.

## 6. Provenance and SBOM requirements

Provenance MUST bind an artifact digest to its source repository and commit,
builder or workflow identity, build invocation, relevant material inputs, and
creation time. It MUST be generated by the build or publication path, not
reconstructed manually after release. A verifier MUST be able to establish the
expected repository, workflow, ref or tag, and signer identity. Provenance
SHOULD follow the [current approved SLSA provenance
model](https://slsa.dev/spec/v1.2/provenance) or an interoperable attestation
with equivalent subject, source, builder, invocation, and material fields.

An SBOM MUST describe the released artifact rather than only the source tree.
It MUST use an interoperable format such as [SPDX](https://spdx.dev/) or
[CycloneDX](https://cyclonedx.org/), identify its subject by digest, and include
discovered direct and transitive components with versions when available.
Missing component data MUST remain visibly unknown; generators MUST NOT invent
completeness.

| Class | Provenance | SBOM or dependency evidence |
| --- | --- | --- |
| `R0` | REQUIRED only for a generated or versioned published bundle; otherwise the reviewed Git history is the evidence. | Not required for source-only text or metadata. A generated bundle with executable dependencies MUST publish a dependency inventory. |
| `R1` | REQUIRED for deployments, generated sites, or other outputs promoted outside the repository. Source-only changes retain pull-request and commit evidence. | A locked dependency inventory is REQUIRED when executable dependencies affect the output. A full artifact SBOM SHOULD be published when a deployable artifact can be inspected. |
| `R2` | REQUIRED for every primary release artifact and MUST be digest-bound. | REQUIRED for every primary release artifact. Packages and binaries MUST include bundled and resolved runtime dependencies discoverable by the build. |
| `R3` | REQUIRED for the image index and traceable for every platform manifest. It MUST identify the build definition and base-image digests. | REQUIRED for every released image digest and MUST cover operating-system and language/runtime packages present in the image. |

Signatures, attestations, SBOMs, and provenance MUST be retained with the release
for at least as long as the primary artifact. Sensitive environment values,
tokens, private source paths, and unnecessary personal data MUST be excluded.

## 7. Verification and failure behavior

For classes `R2` and `R3`, the publication path MUST verify all required
evidence before making a release generally available. Verification MUST check:

- artifact digests and subject identity;
- the expected organization repository and source commit;
- the expected workflow or builder identity;
- the signer or workload identity;
- the presence and subject coverage of required provenance and SBOMs; and
- that no active policy exception has expired.

A verification failure MUST block publication in `enforcing` and `conformant`.
Evidence uploaded after a failed or partial publication MUST retain the failure
state; automation MUST NOT silently relabel it as a complete trusted release.
Rollback instructions MUST identify how to withdraw a bad channel or tag
without deleting the evidence required to understand it.

## 8. Staged adoption

Repositories migrate independently. Legacy repositories MUST NOT be blocked by
new organization checks until they have an explicit migration record. Absence
of a record means `legacy-unclassified`, not `conformant`.

| State | Meaning | Required behavior |
| --- | --- | --- |
| `legacy-unclassified` | No approved class or migration owner exists. | Existing work continues. Organization checks MUST NOT become required. The repository MUST NOT claim conformance. |
| `planned` | Classes, owner, gaps, and target state are recorded. | Implementation work is reviewable; checks MAY run in audit mode. |
| `piloting` | Relay profiles or equivalent controls run without blocking. | Findings and test-release evidence are retained; regressions are fixed before enforcement. |
| `enforcing` | Required checks and release gates block nonconforming changes. | Approved exceptions are the only bypass. Evidence is retained for every release. |
| `conformant` | Enforcement is active and current evidence demonstrates all applicable requirements. | The repository monitors drift and MUST return to `enforcing` or an exception state when evidence is stale or incomplete. |
| `retired` | The repository no longer accepts changes or publishes supported artifacts. | Final artifacts and verification evidence remain discoverable according to retention policy. |

An adoption record MUST contain:

- repository name and applicable classes;
- state, accountable owner, policy version, and state effective date;
- selected Relay profile and immutable version when Relay is used;
- required-check and release-evidence links;
- approved bot exemptions;
- active exception identifiers and expiry dates; and
- the last verification date for `conformant`.

The repository-local baseline contract owns the portable representation of this
record. Organization dashboards and migration ledgers are projections; they
MUST NOT silently override repository-owned state. Until that contract is
available, a repository issue or reviewed policy file MAY serve as the explicit
migration record.

Recommended rollout order is:

1. publish this policy and review repository classifications;
2. implement reusable audit-mode controls in Relay;
3. pilot the controls and release evidence in Empathy;
4. prove `R3` evidence with Realm images;
5. enable blocking checks for new or already healthy repositories; and
6. migrate legacy repositories in bounded pull requests with rollback evidence.

Policy definition is therefore not blocked on Relay or Realm implementation.
Implementation and organization adoption evidence are follow-up work.

## 9. Exceptions and emergency changes

Exceptions are repository- and requirement-specific. There are no permanent
person-level, team-level, or blanket legacy exceptions.

An exception MUST record:

- a stable identifier and affected repository, class, requirement, and artifact;
- rationale and the evidence showing why compliance is currently infeasible;
- accountable owner and approving policy owner;
- compensating controls and residual risk;
- start date, expiry date, and exit criteria; and
- a public review link unless disclosure would expose a security issue.

An exception SHOULD expire within 90 days and MUST have an explicit expiry. An
expired exception fails closed in `enforcing` and `conformant`. Renewal requires
new evidence and review; it MUST NOT be automatic. When the repository owner and
policy owner are the same person, the approval record MUST make that overlap
visible rather than implying independent review.

Emergency default-branch or publication changes MAY bypass a normal gate only
to contain an active incident when delay creates greater risk. The actor MUST
record the reason and affected evidence immediately, open a reviewable follow-up
within two business days, restore the gate, and either remediate the change or
obtain a time-bounded exception. Break-glass authority MUST NOT be used to avoid
ordinary migration work.

## 10. Responsibilities and dependency boundaries

| Owner | Responsibility |
| --- | --- |
| `.github` | Own this organization-facing policy, its public guidance, adoption coordination, and policy-exception decisions. It does not own reusable enforcement code. |
| Hygiene | Preserve the ecosystem ownership boundary, repository registry, and policy relationship in canonical architecture. It does not duplicate this organization-facing policy. |
| Relay | Implement independently versioned, least-privilege DCO, signing, verification, SBOM, provenance, reporting, and release profiles. Relay reports policy outcomes; it does not redefine them. |
| Empathy | Prove the repository-local adoption contract and act as the strict golden consumer. Incubation or experimental exemptions do not belong in Empathy. |
| Realm | Implement and prove the `R3` multi-architecture image, digest-signing, SBOM, provenance, channel, and rollback behavior. |
| Repository owners | Classify outputs, choose an adoption state, protect branches, review bot exemptions, retain evidence, and request exceptions. |
| Pace and Observatory | Future migration and evidence projections MAY consume adoption records, but MUST preserve source, freshness, and exception state. |

Reusable workflows, signing actions, policy scanners, and release mechanics MUST
remain in their owning repositories and be consumed through immutable or
versioned public contracts. This repository MUST NOT copy those implementations.

## 11. Policy changes

Editorial clarifications that do not weaken a requirement increment the patch
version. Backward-compatible additions increment the minor version. A changed
attestation rule, trust boundary, repository class, required release evidence,
or exception authority increments the major version and requires a reviewed
migration impact statement.

Repositories enforce the policy version named by their adoption record. A new
policy version does not silently change a repository from audit to blocking
mode. Security fixes MAY require an accelerated migration, but still require an
explicit reviewed state change.

## 12. Standards references

- [Developer Certificate of Origin 1.1](https://developercertificate.org/)
- [SLSA provenance model](https://slsa.dev/spec/v1.2/provenance)
- [SPDX](https://spdx.dev/)
- [CycloneDX](https://cyclonedx.org/)
