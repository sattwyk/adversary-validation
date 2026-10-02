# Concurrent WAL checkpoint/reset corruption

Corpus class G. SOURCE-IDENTIFIED; source review only at specification creation. No local historical reproduction is implied. See benchmark.json for current status and native observations for separately scoped executed baselines.

SQLite documents a rare checkpointer/writer WAL reset race that can corrupt database state. The fix was shipped in 3.51.3. Local source comparison confirms live salts are checked after taking the relevant lock. This suite has not executed the published reproduction.

Vulnerable: `bae4055493c3d9549f307c20851f4b2c1e0cb5c4`. Fix: `3c7a03032f9c69feb832b96447701bee6fa3ba81`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark sqlite/wal-reset`.
Verify: `python scripts/verify-pins.py --benchmark sqlite/wal-reset`.
Native baseline: `python scripts/native-baseline.py --benchmark sqlite/wal-reset --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Pin compiler, configure flags, Tcl and thread-enabled build environment.
- Run the unmodified published native reproduction separately from diagnostic checkpoints.
- Demonstrate the window is schedulable before interpreting a search miss; exclusive/single-connection substitutes are UNSUPPORTED.

