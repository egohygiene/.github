# Real-report review artifact proof — 2026-11-13

One real, explicitly partial audit completed the hosted path from typed report
to repository models and dashboard, retained website export, and the organization
review artifact. The artifacts were downloaded and their bytes independently
checked. This is a narrow integration result, not organization-wide acceptance.

The [five-source integration record](2026-11-12-ri-convergence.md) records the
preceding merges. The [canary guide](../intelligence/real-report-canary.md)
describes the selected report and the existing producer and consumer interfaces.

## Successful stages

All runs below used attempt **1**. Artifact links open GitHub's artifact UI.

| Stage | Run and immutable source | Downloaded artifacts and observed result |
| --- | --- | --- |
| Repository feed and dashboard | [.github run 43333273329](https://github.com/egohygiene/.github/actions/runs/43333273329), source `b1539be1ab718de2db3da4b1eaa6827e36d4753f` | [Models 13996296082](https://github.com/egohygiene/.github/actions/runs/43333273329/artifacts/13996296082): exactly five model/receipt files, one audit run and one finding. [Dashboard 13996695693](https://github.com/egohygiene/.github/actions/runs/43333273329/artifacts/13996695693): actual Audits HTML renders the finding and partial label. |
| Retained website export | [Website run 43338700534](https://github.com/egohygiene/egohygiene.io/actions/runs/43338700534), source `3672c05323b348edba8720998e735668c5d4a3a9` | [Export 13997279164](https://github.com/egohygiene/egohygiene.io/actions/runs/43338700534/artifacts/13997279164) and [companion 13997503599](https://github.com/egohygiene/egohygiene.io/actions/runs/43338700534/artifacts/13997503599): Audits input and native presentation available; 39 routes and 43 declared files, all file hashes verified. |
| Organization review intake | [.github run 43339209486](https://github.com/egohygiene/.github/actions/runs/43339209486), consumer `b1539be1ab718de2db3da4b1eaa6827e36d4753f` | [Final review 13998892236](https://github.com/egohygiene/.github/actions/runs/43339209486/artifacts/13998892236): downloaded producer export preserves all 44 files, including its manifest, byte-for-byte; companion receipt also preserved byte-for-byte. Final Audits HTML retains the finding anchor, title and partial label. |

The rendered finding is `AUDIT-001`, “Organization review workflow preserves the
documented artifact-only boundary.” It is an observed positive source finding,
not a defect or evidence that the whole repository passed an audit.

## Scope, clocks and identity

The admitted public scope is exactly **`egohygiene/.github`**. The report assesses
historical source `8aef67662f3cf832cc1457ac24ed88f9bf9d2ae7` at
**2026-11-12T23:46:41Z**. Models honestly retain report revision status `different`
from their represented source. The captured model clock remains
**2026-11-12T23:58:44Z** through retained export. The selection/export evaluation
boundary is **2026-11-13T00:04:12Z**, which the intake receipt preserves; the
later intake run time does not refresh either source observation.

The exercised Relay source remains the valid immutable functional pin
`5d27be5ce1599df883e31f14cd894eb18622c18c`. Its later source integration did not
invalidate that pin or require rewriting historical receipts.

These SHA-256 values identify the admitted public artifacts and projections:

| Object | SHA-256 |
| --- | --- |
| Typed audit sidecar | `fba14958748b573ce9045417452de470c2054f028aa9100be4eadaf659aefa92` |
| Five-file model archive | `1192d4c86ccb449d6f40762785a47022235dc0160831e04d6f4354f394d9668d` |
| Repository Audits model | `5270b13b30270862e7006bb910e9df7018099aacb1d6045e48fa124df0c7468b` |
| Fleet Audits model | `cc815114ca2064eb697d7ee6ba7dc3b6970d330fdcd154751f6317d398fdb41a` |
| Feed receipt | `0ec4e83d1c381eabc7450a69c762cc894a8b8a3568d6fbeea7afdf0ce090c651` |
| Repository dashboard archive | `159cdef735638c21fa8dc6f0fadbef4fa7800649b9912b95bc9254d92fb11d56` |
| Website static export archive | `26029b63e41ab34824d124e629a1d67ebafc3297b41402161db055757efa77c6` |
| Export manifest | `55016315151ff9cc47889c0729abbf6966cedbe917fa1b698ddcf2e5ee0020cf` |
| Native Audits presentation | `bfbc3e0eca8c20fa75b9ef640305850d45b294dad4265bed9952d43349addaf3` |
| Companion selection archive | `dc845b2b5a568b80fd3043defe9b665fb82050ada0109070be2f10a2d9fd1765` |
| Companion selection receipt | `8c990b8e93610fb12872c58b1f0d8f6d3de5bbc310d80c5eff6fa548f8b88f81` |
| Intake receipt | `db7e8f7072224b2c1370db05adadb9047636d370f03eba49eb6d4190dd5db00c` |
| Final organization review archive | `d23cb76f235f473a5955e0aaade6c7e6afd493d80eb873ea241e4ba1f9caeb96` |

## Repairs observed during the canary

[Pace #37](https://github.com/egohygiene/pace/pull/37) corrected boolean/integer
canonical equality. Website [#141](https://github.com/egohygiene/egohygiene.io/pull/141)
added the required `contains` schema handling;
[#142](https://github.com/egohygiene/egohygiene.io/pull/142) added bounded source
diagnostics; [#143](https://github.com/egohygiene/egohygiene.io/pull/143) confined
GitHub CLI state outside the source checkout.

The earlier website runs [43335344355](https://github.com/egohygiene/egohygiene.io/actions/runs/43335344355)
and [43337872934](https://github.com/egohygiene/egohygiene.io/actions/runs/43337872934)
failed before producing export artifacts. In the successful run, the checkout,
acquisition and install checkpoints all reported the expected source HEAD,
successful status reads, no truncation and empty changed-path lists (`[]`).
Export, finalization and both artifact uploads then succeeded.

## Review window and limits

The final review artifact expires **2026-11-20T00:42:47Z (UTC)** under the existing
seven-day consumer retention. Download it before that time to retain a copy.

This proof covers **one partial audit**. Core and Sanity remain unavailable.
It does not establish a fresh organization sweep, Pages publication, human
ratification, broad CI qualification or browser qualification. No issue
acceptance checklist or lifecycle state is advanced by this record.

Native intake verified the manifest, exact byte inventory and admitted scope;
it labels model derivation **`producer-declared-not-replayed`** and did not
execute browser scripts. The separate upstream feed/model proof and actual
rendered HTML checks above provide evidence for this selected report; they do
not expand the intake verifier's claim.
