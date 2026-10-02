# Failed leadership transfer leaves progress blocked

Corpus class I. BASELINE-PREPARED: the same three surrounding transfer tests passed on both revisions. They did not demonstrate the historical continuing-progress failure. See docs/BASELINE_OBSERVATIONS.md and benchmark.json for remaining fixture/oracle work.

The fix states that 1.3.4 reset the leadership-transfer flag only on success, leaving it set after failed transfer and breaking callers that require it cleared. No production incident is asserted.

Vulnerable: `38cb18695192d910bd774e2442d198fdc2c691a0`. Fix: `f2fdbd651e1d824151bfb0f73aa297b8903632ac`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark hashicorp-raft/transfer-flag`.
Verify: `python scripts/verify-pins.py --benchmark hashicorp-raft/transfer-flag`.
Native baseline: `python scripts/native-baseline.py --benchmark hashicorp-raft/transfer-flag --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Add a test-only ordinary transfer-failure fixture that demonstrates continuing progress failure and fixed discrimination.
- Compare fair enabled sets to exclude controller stalls.
- Retain race-enabled/native multi-node follow-up before production claims.
