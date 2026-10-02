# Native baseline observations — 2 October 2026

These are newly executed local tests, not imported research results. Every retained standard result remains INCONCLUSIVE about a full benchmark counterexample: no engine decision trace, qualified replay or search occurred. Raw stdout, exact environment and result candidates are in results/baselines. Tests ran on Linux/WSL2 x86_64, Rust 1.97.1 or Go 1.26.4 with the recorded nodwarf5 build variant. This is not cross-platform qualification.

| Target/fixture | Vulnerable observation | Fixed observation | Interpretation |
|---|---|---|---|
| raft-log upstream concurrent reader | 1 test failed: 39 read errors, 0 payload mismatches, 24 caught reader panics | 1 test passed with all three counters zero | Native historical reader regression symptoms were demonstrated with unchanged reader algorithms; no event tape or replay claim |
| OpenRaft upstream constructed divergent logs | 1 test failed waiting for node 2 to become leader, before checking follower replication | 1 test passed | Inconclusive about the documented replication-conflict mechanism; do not count this as liveness reproduction/discovery |
| HashiCorp surrounding transfer tests | 3 tests passed | Same 3 tests passed | Baseline/toolchain compatibility; the selected tests did not demonstrate the transfer-flag regression |

Retained run IDs:

- A vulnerable: results/baselines/20261002T102015Z-1f4bfb36; fixed: results/baselines/20261002T102016Z-30ae29cd.
- B vulnerable: results/baselines/20261002T105218Z-d3fc90bb; fixed: results/baselines/20261002T105220Z-95cfd739.
- I fixed: results/baselines/20261002T101123Z-c6f2c8e0; vulnerable: results/baselines/20261002T101123Z-f2f4ce38.

A and B parent fixtures are exact upstream test-only additions. Their production algorithms are unchanged; dependency solutions are shared within each pair. Patch hashes/postimages are validated before execution. The A fixture's payload check is weaker than the independent specification's full requested-range oracle; decode/identity failures still demonstrate the observed native symptoms. It supplies neither a complete causal event chain nor a production service correspondence claim.

B's early election timeout is a real failed attempt and is preserved. The fix also changed adjacent timeout/vote behavior; source similarity and a failing parent fixture do not establish that the expected replication condition was reached. Additional fixture/upstream investigation is required before S1/S5 for B. Do not repair the vulnerable consensus algorithm to make the fixture progress.

Source/build preparation for A/B/I is established by the executed compiler/test logs. No FIXED-CONTROL-PASSED, SEARCH-REDISCOVERED, BLIND-REDISCOVERED, NATIVE-CONFIRMED or S2–S8 success is inferred. Stronger NATIVE-REPRODUCED claims require the repository's complete counterexample/reviewer evidence, not just these assertion logs. The native runner deliberately does not award evidence levels automatically.

For BASELINE records, number_of_executions counts executed upstream tests, not engine explorations or distinct schedules. The revised runner was checked again on I fixed (results/local/20261002T111036Z-6e57edb9): all three tests passed and the archived native configuration validated. Fresh A acquisition, test-only patch/lock application, pin verification and repeated acquisition also passed in an isolated temporary directory. These checks establish infrastructure behavior, not stronger target evidence.

Earlier fixed-only A/B build attempts also passed and remain in ignored results/local. No failed target run was replaced. Acquisition initially failed when serving a partial-clone cache; the acquisition script now fetches canonical pinned commits directly and resumes only its own empty initialization. That infrastructure failure is not attributed to etcd.
