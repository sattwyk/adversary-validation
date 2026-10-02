# Snapshot/application publication regresses last-applied

Corpus class D. SOURCE-IDENTIFIED; source review only at specification creation. No local historical reproduction is implied. See benchmark.json for current status and native observations for separately scoped executed baselines.

The commit documents last_applied being reset to an earlier position by completion of an apply task after snapshot installation. State-machine changes had run in separate continuations. It does not document power-loss data loss.

Vulnerable: `4d58a51e41189acba06c1d2a0e8466759d9eb785`. Fix: `eed681d57950fc58b6ca71a45814b8f6d2bb1223`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark openraft/snapshot-apply-regression`.
Verify: `python scripts/verify-pins.py --benchmark openraft/snapshot-apply-regression`.
Native baseline: `python scripts/native-baseline.py --benchmark openraft/snapshot-apply-regression --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Freeze historical dependencies.
- Add observational publication instrumentation without moving synchronization.
- Prepare a separately labeled scripted concurrency execution; preserve multiple vulnerable continuations.

