# Actions inventory: first public lane

Read-only snapshot collected 2026-09-25. This covers all 65 committed YAML workflows across six public repositories, pinned below. It is a bounded workflow inventory and proposed execution plan, not an organization-wide audit or a claim that every workflow passes.

No workflows, settings, schedules, budgets, secrets, or deployments were changed or executed. GitHub-generated Dependabot/Pages jobs observed in run history are outside the 65 source files and remain separately identified. Third-party action internals, effective administrative settings, and every transitive dependency were not audited.

## Snapshot and evidence boundary

| Repository | Pinned main revision | YAML workflows | Main-ref runs read | PR runs read |
|---|---|---:|---:|---:|
| relay | [`9a6315978766`](https://github.com/egohygiene/relay/commit/9a6315978766c336566b9fa7139b800fa8789ba5) | 21 | 53 of 53 | 30 of 243 |
| akashic | [`9af6e87b2c70`](https://github.com/egohygiene/akashic/commit/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b) | 8 | 100 of 420 | 30 of 479 |
| empathy | [`d160044e08f3`](https://github.com/egohygiene/empathy/commit/d160044e08f3377afdf14f4856bc470ddd53b769) | 20 | 100 of 923 | 30 of 893 |
| holon | [`660b941f9961`](https://github.com/egohygiene/holon/commit/660b941f99618806fcadd589bcdae61c519f96e4) | 1 | 15 of 15 | 22 of 22 |
| realm | [`02475f8df066`](https://github.com/egohygiene/realm/commit/02475f8df066b221c8b367d6261911f6fa5bae9b) | 1 | 2 of 2 | 2 of 2 |
| reflector | [`6b22845970a1`](https://github.com/egohygiene/reflector/commit/6b22845970a16e5f787eb944de1bf7b02cbb053e) | 14 | 100 of 669 | 30 of 153 |

Run lists are bounded to the newest 100 main-ref runs and 30 PR runs per repository, or all available if fewer. A success applies to its recorded SHA/event, not automatically to today's main. Reusable workflows often appear as jobs inside caller runs. Absence from these samples is unknown, not disabled or never executed.

## Cost and execution policy

Official [GitHub Actions billing documentation](https://docs.github.com/en/billing/concepts/product-billing/github-actions) states that standard GitHub-hosted execution in public repositories is free; larger runners are charged even for public repositories. Private hosted execution has plan allowances and the repository owner is billed. A manual GitHub workflow dispatch still uses hosted execution. Storage, external services, and AI usage require their own entitlement/retention review. A reusable workflow does not transfer its caller's costs to Relay.

No larger/custom runner labels were found in these 65 entry files. Observed labels are standard Ubuntu, Ubuntu ARM64, and macOS, including matrices. This supports keeping public hosted validation; it does not prove zero charges across all services. No billing ledger, budgets, artifact-byte totals, plan entitlements, or paid-service subscriptions were available. No sampled failure below establishes payment blockage.

Disposition key: **K** = keep existing hosted behavior pending normal fixes; **L** = candidate for native/local validation alongside hosted proof; **R** = review mutation/platform/service boundary before local execution; **R/P** = review possible pause or leave optional paid path unselected, with no pause authorized by this report. These are proposed dispositions, not configuration changes. No automatic pause is recommended for the public standard-runner lane.

Retention is the value declared in the entry workflow, in days; `input default` can be overridden by callers. `—` means no explicit retention found here, not proof that invoked actions create no artifacts. `Pages default` means the entry file omits the Pages action's retention input. SARIF/code-scanning retention is a separate service concern. Effective repository retention caps remain unverified.

## relay

| Workflow source | Triggers (cron in UTC) | Runner labels | Retention | Disposition and boundary |
|---|---|---|---|---|
| [artifact-budget.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/artifact-budget.yml) | call | ubuntu-24.04 | input default 30 | K+L: Read-only filesystem/report normalization; artifact-service adapter remains hosted. |
| [automerge-dependabot.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/automerge-dependabot.yml) | PR | ubuntu-latest | — | K+R: Dependabot-only classification then eligible approval/merge; exclude mutations from local smoke. |
| [continuity-preflight-dogfood.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/continuity-preflight-dogfood.yml) | PR | called workflow | — | K+L: Calls same-revision continuity-preflight; retention override 14d. |
| [continuity-preflight.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/continuity-preflight.yml) | call | ubuntu-24.04 | input default 14 | K+L: Pinned EgoLint/offline validation core; acquire sources separately. |
| [dependency-review.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/dependency-review.yml) | PR | ubuntu-latest | — | K: GitHub dependency-review service; preserve hosted evidence. |
| [label-sync-apply.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/label-sync-apply.yml) | call | ubuntu-24.04 | input default 30 | K+R: Default-branch apply; checksum-bound plan; deletions default false. |
| [label-sync-plan.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/label-sync-plan.yml) | call | ubuntu-24.04 | input default 7 | K+L: Read-only label plan; local fixtures before provider read. |
| [publication-pages.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/publication-pages.yml) | call | ubuntu-24.04; called workflow | input default 30; Pages default | K+R: Calls same-revision publication-review; Pages/OIDC deployment needs hosted proof. |
| [publication-review.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/publication-review.yml) | call | ubuntu-24.04 | input default 30 | K+L: Checksum and site validation core; artifact transfer stays an adapter. |
| [pull-request-label-apply.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/pull-request-label-apply.yml) | call | ubuntu-24.04 | input default 30 | K+R: Trusted planner identity and provider mutation; separate from local tests. |
| [pull-request-label-plan.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/pull-request-label-plan.yml) | call | ubuntu-24.04 | input default 7 | K+L: Read-only PR label planning. |
| [release-artifact.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/release-artifact.yml) | call | ubuntu-24.04 | input default 30 | K+R: Release/tag/alias writes; never routine local validation. |
| [release-prepare.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/release-prepare.yml) | call | ubuntu-24.04 | input default 30 | K+L: Read-only release planning/verification. |
| [release.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/release.yml) | manual | ubuntu-24.04; called workflow | 30 | K+R: Manual bundle build then same-revision semantic-release; retention 30d. |
| [repository-intelligence.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/repository-intelligence.yml) | call; manual | ubuntu-latest | validated input default 30, 30 | K+L: Read-only site generation; ordinary artifacts only; no Pages deployment. |
| [repository-journal-copilot.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/repository-journal-copilot.yml) | call | ubuntu-24.04 | input default 30 | R/P: Optional paid AI path: billing acknowledgement false and policy/permission unknown by default; no enablement proposed. |
| [repository-journal-dogfood.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/repository-journal-dogfood.yml) | cron `17 6 * * 1`; manual | ubuntu-24.04; called workflow | — | K+L: Calls local repository-journal in deterministic mode; retention 30d; no AI request. |
| [repository-journal.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/repository-journal.yml) | call | ubuntu-24.04 | input default 30 | K+L: Deterministic/manual journal; no AI billing dependency. |
| [semantic-release.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/semantic-release.yml) | call | ubuntu-24.04; called workflow | input default 30 | K+R: Calls same-revision release-prepare then release-artifact; hosted mutation boundary. |
| [stale-pull-requests.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/stale-pull-requests.yml) | call | ubuntu-24.04 | input default 14 | K+R: Advisory true; issue processing and closure false by default; preserve explicit apply gate. |
| [validate.yml](https://github.com/egohygiene/relay/blob/9a6315978766c336566b9fa7139b800fa8789ba5/.github/workflows/validate.yml) | PR; push main,master; manual | ubuntu-latest, ubuntu-24.04; called workflow | 1 | K+L: Local Python checks plus hosted reusable smoke: journal, budget, publication-review, intelligence; smoke retention 1d. |

## akashic

| Workflow source | Triggers (cron in UTC) | Runner labels | Retention | Disposition and boundary |
|---|---|---|---|---|
| [awesome-lint.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/awesome-lint.yml) | PR main (paths); push main (paths); manual | ubuntu-latest | — | K+L: Native lint candidate. |
| [freshness.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/freshness.yml) | PR main (paths); cron `17 4 * * 1`; manual | ubuntu-24.04 | 14 | K+L: Scheduled 16-shard external-link observation; review cadence/concurrency, retain bounded reads. |
| [pages.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/pages.yml) | PR; push main; manual | ubuntu-24.04; called workflow | 30; Pages default | K+R: Pinned Relay intelligence call; PR matrix current + rollback-v1.3; Pages and live verification hosted. |
| [quality.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/quality.yml) | PR main; push main; manual | ubuntu-24.04 | — | K+L: Native quality scripts candidate. |
| [repository-intelligence-failure-evidence.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/repository-intelligence-failure-evidence.yml) | manual | called workflow | — | K: Intentional invalid-depth evidence fixture; pinned Relay call, retention 30d; do not make green by weakening it. |
| [repository-intelligence-gates.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/repository-intelligence-gates.yml) | PR; push main | ubuntu-24.04 | 30 | K+L: Native gate-contract tests; retain hosted event proof. |
| [search-performance.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/search-performance.yml) | PR main (paths); push main (paths); manual | ubuntu-24.04 | — | K+L: Native performance fixture candidate. |
| [search-research.yml](https://github.com/egohygiene/akashic/blob/9af6e87b2c708dc0cb7a57a9ccf315d51e294a1b/.github/workflows/search-research.yml) | PR main (paths); push main (paths); manual | ubuntu-24.04 | — | K+L: Native research acceptance commands; preserve selected browser/toolchain parity. |

## empathy

| Workflow source | Triggers (cron in UTC) | Runner labels | Retention | Disposition and boundary |
|---|---|---|---|---|
| [automation.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/automation.yml) | PR (paths); push main (paths); manual | ubuntu-latest | — | K+L: Repair stale action-SHA policy assertion; preserve workflow validation. |
| [codeql.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/codeql.yml) | PR; push main; cron `17 5 * * 2`; manual | ubuntu-latest | — | K: Actions + Python matrix; GitHub code-scanning integration remains hosted. |
| [commitlint.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/commitlint.yml) | PR (opened,edited,synchronize,reopened) | ubuntu-latest | — | K+L: Native commit/title validation candidate. |
| [contributors.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/contributors.yml) | manual | ubuntu-latest | — | K+R: Manual documentation generation commits changes; separate read/generate from write. |
| [copilot-setup-steps.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/copilot-setup-steps.yml) | manual; push (paths); PR (paths) | ubuntu-latest | — | K+L: Environment preparation only; this file does not invoke a paid AI request. |
| [dependency-review.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/dependency-review.yml) | PR (opened,reopened,synchronize) | ubuntu-latest | — | K: GitHub dependency-review service. |
| [identity.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/identity.yml) | PR (paths); push main (paths); manual | ubuntu-24.04 | 30 | K+L: Identity validation core. |
| [lint-architecture.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/lint-architecture.yml) | PR (paths); push main (paths); cron `53 5 * * 5`; manual | ubuntu-latest | 30 | K+L: Architecture generation/validation; scheduled publication requires explicit write adapter. |
| [mantle.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/mantle.yml) | PR (paths); push main (paths); manual | ubuntu-24.04, macos-15 | — | K+L: Linux + macOS platform proof; Linux act cannot prove macOS behavior. |
| [megalinter-fix.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/megalinter-fix.yml) | manual | ubuntu-latest | 30 | K+R: Manual autofix; keep local validation separate from repository mutation. |
| [megalinter.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/megalinter.yml) | PR; push main (paths); cron `41 5 * * 3`; manual | ubuntu-latest | 30 | K+L: Lint locally where supported; security upload and curated snapshot publication remain hosted. |
| [mindgarden-pages.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/mindgarden-pages.yml) | PR; push main; workflow_run completed; manual | ubuntu-24.04 | 30; Pages default | K+R: PR current + rollback-v1.4 matrix; workflow_run after MegaLinter/Scorecard/OSV; Pages/OIDC/live proof. |
| [ossf-scorecard.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/ossf-scorecard.yml) | push main (paths); cron `23 5 * * 1`; manual | ubuntu-latest | 90 | K: Security evaluation succeeds in latest sample; summary publication fails; review 90d retention. |
| [osv-scan.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/osv-scan.yml) | push main,master (paths); PR main,master; cron `0 4 * * 3`; manual | ubuntu-latest | 30 | K+L: Native scanner candidate; latest threshold failure needs findings triage, not a skipped gate. |
| [repository-intelligence-checks.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/repository-intelligence-checks.yml) | PR; push main; manual | ubuntu-24.04 | 30 | K+L: Native consumer checks candidate. |
| [repository-intelligence-failure.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/repository-intelligence-failure.yml) | manual | called workflow | — | K: Intentional invalid-depth RIW-002 fixture; pinned Relay call; retention 30d. |
| [repository-intelligence-gates.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/repository-intelligence-gates.yml) | PR; push main | ubuntu-24.04 | 30 | K+L: Native gate-contract tests plus hosted event proof. |
| [repository-intelligence.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/repository-intelligence.yml) | PR (paths); manual | ubuntu-24.04 | 30 | K+L: Uses pinned Relay composite action, not reusable workflow; read-only evidence output. |
| [reusable-autofix.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/reusable-autofix.yml) | call | ubuntu-latest | — | K+R: Caller-controlled formatting/fixes plus autofix-ci service; validate caller checkout/service assumptions before reuse. |
| [reusable-flutter-build.yml](https://github.com/egohygiene/empathy/blob/d160044e08f3377afdf14f4856bc470ddd53b769/.github/workflows/reusable-flutter-build.yml) | call | ubuntu-latest, macos-latest | unspecified upload | K+L: Web enabled by default; Linux/Android/iOS opt-in; iOS on macOS; uploads omit retention-days. |

## holon

| Workflow source | Triggers (cron in UTC) | Runner labels | Retention | Disposition and boundary |
|---|---|---|---|---|
| [validate.yml](https://github.com/egohygiene/holon/blob/660b941f99618806fcadd589bcdae61c519f96e4/.github/workflows/validate.yml) | PR; push main | ubuntu-24.04 | — | K+L: Native Python/Node contracts and pinned-source consumer proofs. |

## realm

| Workflow source | Triggers (cron in UTC) | Runner labels | Retention | Disposition and boundary |
|---|---|---|---|---|
| [validate.yml](https://github.com/egohygiene/realm/blob/02475f8df066b221c8b367d6261911f6fa5bae9b/.github/workflows/validate.yml) | PR; push main; manual | ubuntu-24.04, ubuntu-24.04-arm | — | K+L: Native task check plus amd64/arm64 image-build proof; Docker required for image tests. |

## reflector

| Workflow source | Triggers (cron in UTC) | Runner labels | Retention | Disposition and boundary |
|---|---|---|---|---|
| [beacon-compatibility.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/beacon-compatibility.yml) | PR main (paths); push main (paths); manual | ubuntu-24.04 | 14 | K+L: Native publication compatibility proof. |
| [build-magazine.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/build-magazine.yml) | push main (paths); PR main (paths); manual | ubuntu-latest | 30, 7 | K+L: Screen/print variants; LaTeX Docker build needs matching runtime. |
| [build-paper.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/build-paper.yml) | push main (paths); PR main (paths); manual | ubuntu-latest | 30, 7 | K+L: Paper matrix; LaTeX Docker build candidate. |
| [bump-version.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/bump-version.yml) | manual | ubuntu-latest | — | K+R: Manual version mutation; dry_run defaults false. |
| [commitlint.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/commitlint.yml) | PR (opened,edited,synchronize,reopened) | ubuntu-latest | — | K+L: Native lint; latest sampled Dependabot PR failed; diagnose separately. |
| [copilot-setup-steps.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/copilot-setup-steps.yml) | manual; push (paths); PR (paths) | ubuntu-latest | — | K+L: Environment preparation only; no AI invocation in this file. |
| [pages.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/pages.yml) | PR main (paths); push main (paths); manual | ubuntu-24.04 | 14, 7; Pages default | K+R: Build succeeded, older deploy verification rejected HTTP canonical URL; confirm Pages settings before changes. |
| [paper-quality.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/paper-quality.yml) | push main (paths); PR main (paths); manual | ubuntu-latest | 30, 7 | K+L: Native metadata/LaTeX quality core. |
| [publication.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/publication.yml) | push main (paths); manual | ubuntu-latest | 30, 7 | K+R: Scope-dependent builds and automatic GitHub Release; dry_run defaults false; avoid blind act push. |
| [release-paper.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/release-paper.yml) | push tags v*.*.*,reflector-v*.*.*; manual | ubuntu-latest | 30, 7 | K+R: Tag/manual release publishing; build portion local, publication explicit. |
| [release-please.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/release-please.yml) | push main (paths); manual | ubuntu-latest | — | K+R: Release PR/provider writes. |
| [release-tag.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/release-tag.yml) | push main (paths); manual | ubuntu-latest | — | K+R: Canonical-version tag creation; provider mutation. |
| [reuse.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/reuse.yml) | push main (paths); PR main; manual | ubuntu-latest | — | K+L: Native REUSE compliance candidate. |
| [synchronization.yml](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.github/workflows/synchronization.yml) | push main (paths); PR main (paths); manual | ubuntu-latest | 30 | K+L: Repair stale deploy-pages SHA expectations; keep synchronization checks. |

## Reuse and explicit paid-service boundary

Relay's `$/.github/workflows/...` calls resolve same-revision provider workflows; `repository-journal-dogfood.yml` uses a relative local call. Akashic Pages and both consumer intentional-failure wrappers pin Relay at `9a6315978766c336566b9fa7139b800fa8789ba5`. Empathy's ordinary intelligence wrapper uses the composite action at that same pin. Local compatibility must explicitly prove these call forms; a YAML parse is insufficient.

Relay `repository-journal-copilot.yml` is the only entry file in this inventory with an explicit AI billing acknowledgement. Its `billing-acknowledged` default is false, policy and permission states default to unknown, and the selected job requests `copilot-requests: write`; it forwards these states to the journal action's preflight. No caller of this paid workflow was found in these 65 files. This does not establish usage elsewhere. The deterministic journal has no AI dependency; its “no-billing” wording should not be generalized to all private hosted compute/storage.

The two `copilot-setup-steps.yml` files prepare tools; they are not themselves evidence of an AI request. Security and autofix actions may integrate external services; workflow names and token references alone do not establish a paid subscription or actual charge. Do not copy service assumptions into private consumers without review.

## Observed passing evidence and failures

| Evidence | Observed result | Interpretation / next investigation |
|---|---|---|
| [Relay main validation](https://github.com/egohygiene/relay/actions/runs/35780510787) | Success at captured main SHA | Includes hosted reusable smoke jobs; preserve this proof while adding native entry points. |
| [Akashic Pages](https://github.com/egohygiene/akashic/actions/runs/36065226542) and [job gates](https://github.com/egohygiene/akashic/actions/runs/36065225953) | Success at captured main SHA | Keep free hosted publication and gate evidence. |
| [Empathy Mindgarden](https://github.com/egohygiene/empathy/actions/runs/35869039387) | Success at captured main SHA | A successful site publication does not erase other failed quality/security workflows. |
| [Holon validation](https://github.com/egohygiene/holon/actions/runs/35408315332), [Realm validation](https://github.com/egohygiene/realm/actions/runs/33389353578) | Success at captured main SHAs | Realm native architecture/image proof still needs Docker for local reproduction. |
| [Empathy automation](https://github.com/egohygiene/empathy/actions/runs/35867808580/job/107204071944) | Policy test expects action SHA `15e5b455...` absent from MegaLinter workflow | Reconcile pins and corresponding test expectations together; do not mute the validator. Run SHA predates captured main. |
| [Empathy Scorecard summary](https://github.com/egohygiene/empathy/actions/runs/35867808679/job/107204775594) | Security evaluation succeeds; summary fails `unknown option recursive` | Repair the Git invocation in the publication adapter; preserve security evaluation. Run SHA predates captured main. |
| [Empathy OSV](https://github.com/egohygiene/empathy/actions/runs/35867808662/job/107203973762) | Severity gate reports 85 findings at or above high | Triage actual findings and scope; count is findings, not asserted unique vulnerabilities. Curated snapshot job succeeded. Run SHA predates captured main. |
| [Empathy MegaLinter](https://github.com/egohygiene/empathy/actions/runs/35867808605) | Lint step failed; curated snapshot succeeded | Detailed lint diagnostics were not fully triaged in this inventory; keep failure visible. Run SHA predates captured main. |
| [Reflector synchronization](https://github.com/egohygiene/reflector/actions/runs/35202331002/job/105139785561) | Runtime/release-lifecycle checks fail at captured main | Tests require old `actions/deploy-pages@cd2ce8...` token; reconcile updated workflow pins and contract tests. |
| [Reflector custom Pages](https://github.com/egohygiene/reflector/actions/runs/34688866226/job/103540733284) | Build/review succeeds; deployment verification rejects HTTP canonical URL | Older run returned `http://reflector.egohygiene.io/` while HTTPS required; inspect current Pages configuration and HTTPS before changing policy. Later dynamic Pages success is not proof this custom verification passed. |
| [Reflector recent PR](https://github.com/egohygiene/reflector/actions/runs/35664317258) | Commitlint failure on dependency-update branch | Separate PR-specific diagnosis; do not infer main or billing failure. |
| [Akashic recent PR](https://github.com/egohygiene/akashic/actions/runs/35939808242) | `action_required` | A pending GitHub action/approval state; no execution or billing diagnosis established. |

[Akashic intentional failure](https://github.com/egohygiene/akashic/actions/runs/35845772724), [Empathy intentional failure](https://github.com/egohygiene/empathy/actions/runs/35855095637), and [Relay manual rejection](https://github.com/egohygiene/relay/actions/runs/35747527356) retain `RIW-002` trust/input-validation failure evidence. Both consumer fixtures explicitly submit invalid depth 21. Do not treat those consumer fixtures as broken production CI or make them pass by weakening input rejection; Relay's sampled manual rejection likewise does not establish a failed valid-input production build.

## Local execution plan

The first shared interface should be the repository's native `task check` or focused scripts, invoked by both hosted workflows and an optional `act` adapter. Relay owns reusable workflow/local compatibility contracts; Holon can materialize a pinned `.actrc` profile while preserving local overrides; Realm owns the pinned runtime and image prerequisites. Add one small profile and prove it before expanding.

[Reflector's existing `.actrc`](https://github.com/egohygiene/reflector/blob/6b22845970a16e5f787eb944de1bf7b02cbb053e/.actrc) is a seed, not a verified universal configuration: it enables `--graph`, which current [act source](https://github.com/nektos/act/blob/master/cmd/root.go) uses to draw and return without running jobs. Its documentation examples omit a `--graph=false` execution override. It maps only `ubuntu-latest` to mutable `node:16-buster-slim`; it needs version/image pinning, actual runner-label coverage, and a real execution fixture. Comment lines are not claimed as a runtime defect.

[act configuration documentation](https://nektosact.com/usage/index.html) describes XDG/home/invocation configuration layering; a reproducible wrapper must record or isolate those effective inputs. [Runner documentation](https://nektosact.com/usage/runners.html) warns that container images are incomplete relative to hosted virtual machines; Linux execution cannot establish native macOS/iOS parity. [Unsupported functionality](https://nektosact.com/not_supported.html) includes ignored permissions, concurrency, job timeout/environment semantics and missing OIDC. Therefore local success must be labeled local, and GitHub permissions, event trust, Pages, release and deployment proofs remain distinct.

This execution environment currently has no act/Docker/Podman binary or Docker socket. Native checks can be used in a later implementation checkpoint; actual act/container evidence requires an appropriate workstation or runner. No local or hosted workflow was executed for this inventory.

## Unknown settings and next checkpoint

The connector rejected the Actions workflow-state listing endpoint. Committed files therefore do not establish enabled/disabled state. Relay branch-protection retrieval returned 403; its visible ruleset list was empty, which does not establish absence of branch protection. Other repositories' effective required checks, Pages settings, organization policies, runner groups, retention caps, installed-service entitlements, and billing budgets remain unverified.

1. Review this bounded inventory and preserve the free public hosted lane. Address ordinary failures through existing ownership and linked repair checkpoints.
2. Read effective settings and budget/usage evidence when available; record unknowns explicitly. Do not pause required checks before defining how required evidence will be supplied.
3. Specify one Relay local-validation profile, its supported jobs, native commands, event fixtures, image pins, artifact output, and explicit skipped/unsupported surfaces. Exclude provider mutations and AI calls from routine local validation.
4. Prove one public provider and one separately authorized private consumer; record exact SHA, runtime, command, result and limitations. Do not publish private topology or evidence in this public report.
5. Expand in small reviewable batches. Only propose targeted pauses where actual paid usage or unsupported execution is established; preserve a documented restart path and honest checks. Local evidence does not automatically satisfy GitHub required status checks.

Completion for this checkpoint means the inventory and proposed ownership are reviewable. It does not mean universal act parity, zero cost across accounts, passing fleet CI, or completed settings migration.
