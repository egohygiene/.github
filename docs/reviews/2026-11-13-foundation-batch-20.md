# Foundation batch: 20 selected issues

This review packet retains the original selection: six Empathy, eight Holon and
six Hygiene issues. The work combines implementation repairs with qualification
of previously merged behavior. **Selection, PR merge, executed checks and issue
closure are different observations.** No all-20 completion claim is made.

The [provider snapshot](2026-11-13-foundation-batch-20.json) at
**2026-11-13T04:08:19Z** records **15 closed and five open issues**. All selected
scopes have merged source across 18 distinct PRs; Holon #99 covers three issues.
The five open issues are Empathy #92/#98/#109/#112 and Hygiene #76. The remaining
criteria below are retained even where a narrower issue is completed.

This packet aggregates owning qualification evidence and actual provider facts;
it does not rerun tests, change policy, waive source holds or approve promotion.

## Per-issue review

| Issue | Selected scope | Source PR at checkpoint | Recorded outcome | Remaining criteria or separate acceptance |
| --- | --- | --- | --- | --- |
| [empathy #117](https://github.com/egohygiene/empathy/issues/117) — closed | Narrow unsupported attribution fallback and retain explicit unresolved provenance. | [PR #133](https://github.com/egohygiene/empathy/pull/133) — merged | REUSE attribution fallback restricted; four source samples preserved; three regression tests passed. | Corpus rights/origin review and promotion remain under #79/#51; no legal or full-scan acceptance. |
| [empathy #109](https://github.com/egohygiene/empathy/issues/109) — open | Repair real baseline fixture drift and qualify canonical validation without duplicating runners. | [PR #136](https://github.com/egohygiene/empathy/pull/136) — merged | 224 equipped repository tests passed without skips; independent 31-test embedded suite retained one runtime/catalog failure. Six-file Python checks passed. | Aggregate remains failed; #110 runtime/catalog, #79 root Rust membership, staging diagnostic debt and broad holistic qualification remain. |
| [empathy #112](https://github.com/egohygiene/empathy/issues/112) — open | Qualify staging preimage/removal receipts and read-only scheduled gate. | [PR #134](https://github.com/egohygiene/empathy/pull/134) — merged | 27 staging tests and exact base/head gate passed. Actual staging job passed; independent baseline job and whole hosted workflow failed with retained results. | Actual PR-event proof and canonical staging diagnostics remain; no source deletion, destination proof or human approval. |
| [empathy #92](https://github.com/egohygiene/empathy/issues/92) — open | Prove inherited ignore exceptions through current immutable Holon/EgoLint inputs. | [PR #138](https://github.com/egohygiene/empathy/pull/138) — merged | 19 gitignore tests and two accepted Holon/EgoLint disposable consumer lifecycles passed, including no-op/update/guarded rollback and semantic checks. | Three inherited-policy deviations still need owner correction or accepted exception; current 2.0 adapter compatibility is a separate adoption limit. |
| [empathy #98](https://github.com/egohygiene/empathy/issues/98) — open | Repair Scorecard publication command and represented-revision evidence. | [PR #135](https://github.com/egohygiene/empathy/pull/135) — merged | Unsupported Git cleanup flag repaired; 11 exact Relay report tests and seven policy tests passed. Actual historical SARIF replay preserves stale/mismatch/absence. | Snapshot HEAD/source cycle, fresh producer and composed preview/live proof remain open; no report retiming or new publication. |
| [empathy #113](https://github.com/egohygiene/empathy/issues/113) — closed | Refresh dependency triage, suppression expiry and updater evidence. | [PR #137](https://github.com/egohygiene/empathy/pull/137) — merged | Fresh seven-root OSV triage maps 663 grouped advisory occurrences, including 320 blocking; four obsolete suppression identifiers removed and root updater package-manager proof passed. | Bounded triage is accepted; residual owner/investigation work, retained filters, unresolved versions and hosted updater behavior remain explicit. No clean scan or exploitability claim. |
| [holon #68](https://github.com/egohygiene/holon/issues/68) — closed | Replace predictable temporary writes with guarded lifecycle primitives. | [PR #94](https://github.com/egohygiene/holon/pull/94) — merged | 15 presentation tests plus fixture validation passed: alias/symlink/special-file denial and ordinary paired-write compensation. | Issue-specific repair completed; broader platform/crash/concurrency limits remain below. |
| [holon #74](https://github.com/egohygiene/holon/issues/74) — closed | Preserve exact bytes and recovery state through initialize/noop/upgrade/rollback. | [PR #95](https://github.com/egohygiene/holon/pull/95) — merged | 20 presentation tests plus fixture validation passed: byte-exact no-op, authored UTF-8/line endings and one-level rollback ownership. | Issue-specific repair completed; broader platform/crash/concurrency limits remain below. |
| [holon #71](https://github.com/egohygiene/holon/issues/71) — closed | Align render overlay output with the closed public schema. | [PR #96](https://github.com/egohygiene/holon/pull/96) — merged | 31 materialization tests passed with real Draft202012 instances, ordered descriptors and legacy omission controls. | No issue-scoped gate reported by owner; broader qualification stays separate. |
| [holon #69](https://github.com/egohygiene/holon/issues/69) — closed | Compensate earlier restores when a later rollback write fails. | [PR #97](https://github.com/egohygiene/holon/pull/97) — merged | Late write/unlink/state failures compensate; final-main missing/corrupt recovery inputs reject before mutation with byte-identical fixtures. | No issue-scoped gate reported by owner; persistent storage/crash/concurrency guarantees remain outside the qualified behavior. |
| [holon #63](https://github.com/egohygiene/holon/issues/63) — closed | Align ADR scaffold pins/provenance and qualify native upgrade and rollback. | [PR #98](https://github.com/egohygiene/holon/pull/98) — merged | Nine focused tests and blueprint validation passed; exact native EgoLint empty/proposed consumers passed. Historical pack upgrade/rollback and authored conflict were exercised. | No issue-scoped gate reported by owner; downstream adoption, release declaration, policy-owner mode and human approval remain separate. |
| [holon #77](https://github.com/egohygiene/holon/issues/77) — closed | Qualify safe-integer and escaping behavior in Intelligence rendering. | [PR #99](https://github.com/egohygiene/holon/pull/99) — merged | Shared 32-test RI suite passed: safe integer/escaping denials and pinned owner golden through pure, mounted and static CLI paths. | No issue-scoped gate reported by owner; browser accessibility and broader hosted/fleet qualification remain separate. |
| [holon #78](https://github.com/egohygiene/holon/issues/78) — closed | Qualify absent/null theme inputs and component reconnect/update behavior. | [PR #99](https://github.com/egohygiene/holon/pull/99) — merged | The same 32-test RI suite passed optional/null theme, update/disconnect/reconnect and minimal-DOM listener/navigation controls. | No issue-scoped gate reported by owner; minimal-DOM checks are not real-browser accessibility qualification. |
| [holon #79](https://github.com/egohygiene/holon/issues/79) — closed | Qualify semantic release ordering and date precision/tie behavior. | [PR #99](https://github.com/egohygiene/holon/pull/99) — merged | The same 32-test RI suite passed timestamp ordering, ties/offsets/fractions, permutations and matching pure/mount/static summaries. | No issue-scoped gate reported by owner; actual provider freshness and publication remain separate. |
| [hygiene #76](https://github.com/egohygiene/hygiene/issues/76) — open | Fix duplicate presentation evidence, rebind documentation composition and reconcile current validation checkpoints; retain broader parent gates. | [PR #109](https://github.com/egohygiene/hygiene/pull/109) — merged | Duplicate/documentation repair: 44 focused tests passed. Context correction merged; final clean-main gate passed 24 checks, but unit-tests hit the 60-second cap with no complete count. | Parent remains open: unit-suite timeout, hosted/ruleset, exact native EgoLint, #47 historical authority/publication and human gates remain. |
| [hygiene #82](https://github.com/egohygiene/hygiene/issues/82) — closed | Make ADR reference schema/helper full-string matching agree. | [PR #112](https://github.com/egohygiene/hygiene/pull/112) — merged | 29 ADR tests, 72 reference CLI calls and 36 Node grammar cases passed; schema/helper use complete reference strings. | Decoded-reference acceptance does not replace exact native Markdown/source admission or #47 human/authority evidence. |
| [hygiene #83](https://github.com/egohygiene/hygiene/issues/83) — closed | Qualify shared HTTPS/origin validation through actual owner CLIs. | [PR #113](https://github.com/egohygiene/hygiene/pull/113) — merged | 44 Web and 43 surface tests plus public profile/fixture/registry CLIs passed; no network or secret echo. | Proposed profile remains proposed; site certification, browser/live conformance and #95 human lifecycle review are separate. |
| [hygiene #84](https://github.com/egohygiene/hygiene/issues/84) — closed | Qualify exact pinned release composition and safe prepare/verify; no release publication. | [PR #114](https://github.com/egohygiene/hygiene/pull/114) — merged | 16 release-policy tests and exact owner/declaration/profile CLIs passed; actual Task plan/prepare/verify passed after YAML handoff repair. | No release:publish, tag, release, deployment or credential action; proposed ADR-0015 and successor #65 remain separate. |
| [hygiene #80](https://github.com/egohygiene/hygiene/issues/80) — closed | Qualify explicit/current UTC assessment and expiry behavior. | [PR #110](https://github.com/egohygiene/hygiene/pull/110) — merged | 22 continuity tests and five public CLI invocations passed UTC assessment, expiry boundaries, explicit determinism and unavailable-clock denial. | No authentic exception approval, policy ratification, consumer activation or hosted CI claim. |
| [hygiene #81](https://github.com/egohygiene/hygiene/issues/81) — closed | Qualify current-witness, stale-evidence and duplicate-record semantics. | [PR #111](https://github.com/egohygiene/hygiene/pull/111) — merged | 24 presentation tests and public CLI controls passed current witnesses, stale/duplicate evidence and schema-order parity. | Live facts, reachability, policy promotion and parent #76 combined acceptance remain separate. |

The 32-test Holon RI suite is shared by #77/#78/#79; it is not three independent
32-test executions. Other overlapping suites are also not summed into a batch
score. Recorded focused passes do not overwrite an aggregate failure.

## Source evidence

The linked PRs retain exact prepared heads and merge commits. These selected
qualification records are pinned to their actual source rather than a mutable
latest branch:

- [Empathy attribution samples](https://github.com/egohygiene/empathy/blob/ffbbf2e5411a1e279b25ba4adeb22b0015448f0f/docs/security/data/attribution-2026-11-13.json).
- [Empathy baseline qualification](https://github.com/egohygiene/empathy/blob/43ad939a82471a842d85d96dcb2dc532867a6529/docs/evidence/2026-11-13-baseline-validation.json).
- [Empathy staging qualification](https://github.com/egohygiene/empathy/blob/4706296662f52520c67434c9935cffa40ad90202/docs/migration/STAGING_RECEIPTS_QUALIFICATION.json).
- [Empathy actual Scorecard source replay](https://github.com/egohygiene/empathy/blob/c4c92e58a41eb426b05df4010f965cb53a849541/docs/integrations/evidence/scorecard-source-boundary-2026-11-13.json).
- [Holon exact native ADR qualification](https://github.com/egohygiene/holon/blob/cb56c4a1aeb7363507926d97eb29862a6d063455/docs/evidence/2026-11-13-adr-native.json)
  and [shared RI qualification](https://github.com/egohygiene/holon/blob/44dbe04188b3e85a76d412c57cbbf250bbd83180/docs/evidence/2026-11-13-repository-intelligence-qualification.md).
- [Empathy accepted gitignore integration proof](https://github.com/egohygiene/empathy/blob/74795473aeda4b5a7712124bce7160d573781145/docs/foundation/gitignore/data/shared-integration-20261113.json).
- [Empathy current dependency ledger](https://github.com/egohygiene/empathy/blob/4d27e691684d078e76d823c1bcca231994e693cc/docs/security/data/dependency-findings-2026-11-13.csv).

The [final Hygiene reference-gate summary](https://github.com/egohygiene/hygiene/blob/6cc9c63d2804f518fb2e078b6cc55d9251e365cf/docs/evidence/2026-11-13-reference-gate.json)
retains the clean-source, exact runtime, 24 passed checks and timed-out unit suite.
Its public JSON SHA-256 is `da0f7363c0e974d4c6cda64ef9c64b85724e95178565f7d55c8cf3e8b47618c8`.

Hygiene records one dated evidence report per selected issue at its linked PR.
Their focused source/check clocks remain separate from a later composed gate.
Raw process logs, captures, temporary paths and credentials are excluded here.

## Retained holds

Empathy's independent runtime/catalog failure remains under #110. Its root Rust
membership/source-ownership question and unresolved intake provenance remain
under #79/#51. No source hold, staging approval, receipt, rights assertion or
publisher gate was removed to obtain a pass. The actual staging job succeeded
inside an overall failed workflow; the failed baseline results remain retained.

Empathy #113 completed its bounded ledger/updater triage acceptance while the
configured scanner still blocks: 663 grouped advisory occurrences across seven
result roots include 320 high/critical occurrences. These are not counts of
unique exploitable production defects. Named owner investigations/remediation,
retained filters, unresolved version expressions, optional-source coverage and
hosted updater behavior remain explicit in its evidence. Closing the triage
issue does not close those residual tasks or manufacture a clean scan.

Hygiene's initial full gate exposed context/index mapping failures. The owner
correction is now merged. A separate final gate on clean main
`a28fb6207889d4368228d537b5fb2308cca49d2b` used the exact configured release
owner/runtime: 24 of 25 checks passed, including repaired context/generated and
release-owner checks. The unit suite was killed at its unchanged 60-second cap
(60.003 seconds, exit -9); it has no complete test count. The aggregate remains
failed and parent #76 stays open. No deadline waiver or clean-suite claim
replaces that result. Exact native EgoLint admission, hosted/ruleset proof,
historical authority/source/publication work under #47 and human lifecycle
under #95 remain separate. Proposed policy/ADRs retain their dispositions.

Holon's focused local Linux/Node controls do not claim Windows, crash-transaction,
concurrent-writer, browser accessibility, release/distribution or fleet-adoption
qualification. Its parent #66 and independent owner/adoption issues remain
separate from individual repair acceptance.

## Actual organization source sweep and hosted handoff

The [canonical source sweep](../intelligence/organization-source-sweep.md)
assesses all 28 repositories admitted by the reviewed public catalog at exact
historical source heads. It remains partial, with eight concerns and 28 narrower
source positives. It does not establish the organization total or whole-code
conformance. Native capture omissions and the narrower semantic source review
are disclosed separately; later foundation merges do not retime that evidence.

The actual manual [canary 43358630670/1](https://github.com/egohygiene/.github/actions/runs/43358630670)
ran successfully on main `281c3827378ae08bb44cde810ad6467fdb0c8adc` with evaluation
boundary `2026-11-13T03:23:31Z`. The [hosted proof](2026-11-13-organization-source-sweep.hosted-proof.json)
binds model artifact `14007481492`, dashboard artifact `14007341969`, raw archive
hashes and the exact feed receipt. All four owner models validate. Downloaded
native HTML shows both domains: one partial Audit run with the one `.github`
finding, and one partial organization Sanity review with 28 components, eight
concerns, 28 strengths and 17 dimensions. All eight concern summaries are present
in the actual Sanity page; human state stays unavailable.

The canonical organization Audit retains all 36 findings. The repository Audits
projection and each fleet model still target one `.github` consumer row. This producer success alone establishes no additional fleet rows or human
approval. The separate [combined export/intake proof](2026-11-13-organization-export-intake.json)
now records actual website run `43361706555/1` at source
`342673b110915f4a29ada01625a77416a1e105d7`, export `14008422802`, companion
`14008148910`, and organization intake `43362027530/1` at source `281c`.
The final review artifact is `14008223697`, raw archive SHA-256
`45a128195fe10c53b518c903fc800d69c786595b9a329897ba364d9255fcaea7`.
Both review domains and all eight concern summaries survived the 39-route,
43-file sealed export and byte-exact intake. Model clock `03:23:31Z`, partial
execution and unreviewed governance remain unchanged. Review-only intake still
has `deployment_authorized: false`; live Pages and human acceptance remain
separate. This packet changes no publisher inputs.

## Actual read-only publication preparation

After publisher refresh [PR #62](https://github.com/egohygiene/.github/pull/62)
merged, actual main `f3e90df69710492fe55d0d5fb0f5f203a5804bc9` ran the existing
publisher with `publish: false`. [Run 43363401173/1](https://github.com/egohygiene/.github/actions/runs/43363401173)
passed preparation and skipped deployment. The [separate preparation proof](2026-11-13-organization-publication-prepare.json)
binds artifact `14008693427`, raw archive SHA-256
`66588a1e98fd7d2480ba7b11653fc15217b73b524e0ff2f0143af5bd174afa14`
and publication metadata SHA-256
`ee446df191be95b2acdc728d8fb4e783f4183d36ce7648093c1900dcdeb39627`.

All 43 producer files and the sealed manifest remain byte-exact. The public
site has 44 files, adding only consumer provenance; it contains no private
acquisition captures or CLI state. Both review domains remain available with
the original partial/unreviewed scope, while Core remains unavailable. The
source guard and downloaded native byte check passed. No Pages setting,
deployment, live HTTPS or recovery success is claimed. The administrator's
Pages Actions setting remains the named next capability.

## Bounded browser replay

The actual [hosted export](https://github.com/egohygiene/egohygiene.io/actions/runs/43361706555)
was replayed locally in a browser from `03:55:00Z` to `03:55:39Z`. Its manifest
and all 43 site files matched the downloaded archive before and after the
checks. Twelve focused checks passed, with zero failed checks and a retained
finding: Audits and Sanity detail pages had a 402-pixel scroll width at a
390-pixel viewport. The result is **passed with findings**.

This is local replay of the exact hosted artifact. No canonical live HTTPS,
physical-device matrix, complete accessibility or production Pages acceptance
is supplied by it. The replay made no provider writes and changed no producer
files. The [canonical export/intake proof](2026-11-13-organization-export-intake.json)
provides its source and artifact binding; raw browser diagnostics and temporary
preview paths remain outside this public packet.

## Closeout protocol

Refresh the exact source heads, merge receipts and issue dispositions before
publishing a final tally. Close only the issue-scoped criteria supported by
actual evidence; retain parent, external-source, platform and human gates by
name. The original selection and dated source/qualification clocks remain
inspectable even when the coordinator later closes a subset of issues.
