# Success criteria, protocol version 1

Report each gate separately, with reviewed artifact links. No automatic promotion. S0–S8 are validation objectives; S9 is optional. These gates test bounded claims, never universal correctness.

| Gate | Required evidence |
|---|---|
| S0 benchmark validity | Primary historical claim, full vulnerable/fix SHAs, local source and diff review, parent/ancestry verification, scope of upstream claim, reachable workload, oracle independently specified. A candidate fix or an unvalidated storage adapter prevents a full S0 claim. |
| S1 mechanism reproduction | Executed explicitly constructed execution with observable violation and causal witness; known initial log images, failpoints and event tapes make this REPRODUCTION. Source review alone fails this gate. |
| S2 deterministic replay | Original failure plus 100 fresh executions of its complete choice/evidence bundle, 100 matching violations and relevant trace digests, zero unexplained divergences under identical pinned artifacts. Cross-host claims require separate qualification. |
| S3 search rediscovery | Frozen generic policy receives only the sealed allowed input package; declared budgets and all attempts including misses retained; an executed failure is independently checked. A targeted checkpoint derived from the historical race must be disclosed and cannot earn blindness. |
| S4 vulnerable/fixed discrimination | Identical workload, fault envelope, oracle, policy, seeds and budgets on both revisions. Vulnerable failure, absence of the historical violation on fixed, and valid coverage. Report fixed historical replay separately from fresh search; incompatibility is not a passing control. |
| S5 causal correspondence | Reviewer matches the complete failure chain against upstream mechanism after search. Same final symptom or a target panic alone is insufficient. |
| S6 cross-class generality | S0–S5 and S7 across at least shared-memory scheduling, network/timer liveness, and crash/persistence safety; at least three projects. Publish misses and unsupported rows with the selected denominator. |
| S7 production correspondence | Correctness-sensitive algorithms, threads/tasks, ownership, storage identities, recovery and required transport remain; audited build and patch diffs plus native/model contract evidence. Unchanged LOC or compilation alone is insufficient. |
| S8 native confirmation | An independently executed native trace/fault experiment admits the discovered causal condition, checked by the same property, with platform and injection provenance. Synthetic recovery images alone cannot establish power-failure correspondence. |
| S9 novel discovery | Previously unknown upstream correctness issue, independent native validation and external review. Not an initial project requirement. |

Initial research decision: do not implement Adversary until A, B, C and F have reviewer-approved S0, executable baseline plans, sealed ordinary inputs, checker controls and preservation audits, with G retained as a boundary test. Historical native/scripted reproduction should establish S1 for at least A and one persistence case before interpreting search misses. Candidate H must remain unresolved until a reviewed fix exists.

An initial future-engine acceptance is S0–S5 and S7 on A/B/C/F, S2 on all discovered failures, truthful capability rejection on G, and S8 wherever native fault infrastructure is available. This is a predeclared engineering gate, not a statistical theorem. Strengthen to S6 before cross-project/general-platform claims. Missing production qualification limits S7/S8 claims even when model tests succeed.

Budgets in workload packages are initial fixed laboratory budgets. Compare paired discovery rates over seeds 0–29, retain censored time-to-failure and zero-execution runs, report confidence intervals without pooling unlike models. Never treat budget exhaustion as proof of correctness.

