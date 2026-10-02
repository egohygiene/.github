# Repository agent guidance

This repository owns organization-facing GitHub policy, defaults, and intake.
Read [ARCHITECTURE.md](ARCHITECTURE.md),
[issue routing](docs/issue-routing.md), and root
[CONTINUITY.md](CONTINUITY.md) before repository changes. Verify mutable
issue and pull-request state before resuming work.

## GitHub issue titles

Before creating or changing an issue, read the
[issue-title contract](.github/issues/title-contract.v1.json) and its
[semantics and examples](docs/issue-titles.md).

- Select exactly one primary type from the existing label catalog.
- Use the contract's emoji, type token, and title format.
- Verify provider labels exist; report missing or inaccessible label state.
- Preserve subject wording, tracking identifiers, and native relationships.
- Preview legacy normalization using an explicit reviewed subject.
- Do not claim automatic conformance from these instructions alone.

This is the source repository's entry point. Other repositories consume a
pinned revision through their local guidance; this file is not automatically
inherited across GitHub. Aether owns reusable agent projections, Egolint owns
conformance code, and Relay owns GitHub mutations.

Refresh CONTINUITY.md in an authorized repository change, recording exact
validation, limitations, and the next checkpoint. Proposed work is delivered
through a draft PR for maintainer review; do not self-merge.
