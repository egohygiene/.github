# Organization community defaults

Tracking: [#24](https://github.com/egohygiene/.github/issues/24).
The [GitHub supported default-file model](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
is the platform reference. A public `.github` repository supplies supported
fallback files to repositories owned by the same account; repository-local
files take precedence. These are GitHub discovery rules, not filesystem
inheritance or an automatic agent installation.

| Supported surface | Decision and source |
| --- | --- |
| Contribution guidance | Adopt root [CONTRIBUTING.md](../CONTRIBUTING.md); local build, attestations and contribution policy remain authoritative. |
| Security policy | Adopt root [SECURITY.md](../SECURITY.md); no invented mailbox, response guarantee or supported-version window. |
| Support guidance | Adopt root [SUPPORT.md](../SUPPORT.md); use receiving-repository facilities only when available. |
| Issue forms/configuration | Adopt the existing `.github/ISSUE_TEMPLATE/` intake with canonical type prefixes and shared required fields. |
| Pull request template | Adopt `.github/PULL_REQUEST_TEMPLATE.md`; receiving-repository requirements extend or replace it. |
| Funding | Move the existing [FUNDING.yml](../.github/FUNDING.yml) byte-for-byte to GitHub's required `.github` directory. Repository-local funding overrides it. Sponsor-button/provider availability remains external. |
| Code of conduct | Defer until the maintainer selects an enforcement contact and process; do not invent a mailbox or reporting promise. |
| Accessibility policy | Defer `ACCESSIBILITY.md` until the owning products provide their goals, known barriers and reporting process; no organization-wide conformance claim. |
| Private vulnerability form | Defer `VULNERABILITY_REPORT.yml` until the receiving reporting path and required intake fields are selected; this does not enable private reporting. |
| Discussion category forms | Defer until categories and enablement are selected; no default discussion configuration is assumed. |

Licenses remain repository-owned; this change adds no fallback license. The
existing license for this source repository is not an organization-wide grant.
`GOVERNANCE.md`, `AGENTS.md`, architecture documents, release declarations and
lint configuration are not GitHub-supported inherited community-health files.

A local community file wins even when it is shorter than this default. A valid
local issue template or configuration in `.github/ISSUE_TEMPLATE` prevents use
of **all** default contents from that directory; GitHub does not merge default
and local forms. Pull request templates likewise follow the receiving
repository's selected configuration. Test discovery on each intended consumer;
the source files alone do not prove hosted inheritance.

Forms reference the existing label taxonomy and
[shared authoring contract](issue-authoring.md). Missing receiving-repository
labels remain an explicit enrollment gap. Ordinary feature and checkpoint
fixtures demonstrate UI/API consistency without creating provider issues.
Historical issues remain unchanged. No discussion, private-reporting setting,
funding service, license or enforcement mode is activated by these files.
