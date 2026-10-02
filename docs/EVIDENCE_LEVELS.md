# Evidence and outcomes

Evidence labels are independent assertions requiring explicit review and artifact references; they are not an ordinal ladder.

| Label | Meaning |
|---|---|
| DOCUMENTED | Primary source documents the stated defect; no local execution implied. |
| SOURCE-VERIFIED | Local pinned source and patch support the stated mechanism. |
| BUILD-VERIFIED | The exact source, lock and toolchain built successfully; no violation demonstrated. |
| NATIVE-REPRODUCED | Real native target execution demonstrated the historical violation in the declared local environment. |
| SCRIPTED-REPRODUCED | An explicitly supplied schedule/fault location or constructed state demonstrated it. Can coexist with native reproduction. |
| SEARCH-REDISCOVERED | Generic search found it without the known event tape or fault point. |
| BLIND-REDISCOVERED | Independent search authors had no mechanism/fix access, sealed input and audit confirm that separation. |
| FIXED-CONTROL-PASSED | Corresponding fixed control actually executed with matched admissible inputs and no historical violation; scope/budget recorded. |
| NATIVE-CONFIRMED | Native execution independently admits a model-discovered condition. |
| UNSUPPORTED | Required capability absent; no target pass/fail inference. |
| INCONCLUSIVE | Missing evidence, incomplete campaign, oracle budget or unmet fairness assumption. |
| HARNESS-FAILURE | Infrastructure, recorder, controller or build failure. |

Outcomes: COUNTEREXAMPLE FOUND, NO FAILURE FOUND, MODEL CANNOT REPRESENT REQUIRED BEHAVIOR, BENCHMARK INVALID, INCONCLUSIVE, HARNESS FAILURE. Outcome and evidence are separate axes. NO FAILURE FOUND requires completed admissible executions, a reached oracle and satisfied coverage requirements; it cannot stand in for unsupported behavior. A build failure is HARNESS FAILURE, never a bug finding. A liveness timeout is INCONCLUSIVE until fair progress and harness independence are demonstrated.

Existing research logs stay external, dated evidence. Their labels are not copied into this repository's result ledger. Metadata CI cannot award any execution evidence.

