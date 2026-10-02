# Shared file cursor race

Corpus class A. BASELINE-PREPARED: both pinned revisions build and execute the same upstream reader fixture. The vulnerable fixture failed and the fixed fixture passed locally. These are native assertion observations, not deterministic replay or search evidence; see docs/BASELINE_OBSERVATIONS.md and benchmark.json for the exact scope and remaining gaps.

The fix describes concurrent readers overwriting a shared seek position before another reader consumes a record, causing reads at incorrect offsets. It adds a concurrent-reader regression. No production incident is claimed.

Vulnerable: `9e61000ca32474aa0ece9917b6cf52c99518da78`. Fix: `707a9a2463ab215175ef9fbc8d86ea57c2aeac72`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark raft-log/shared-cursor`.
Verify: `python scripts/verify-pins.py --benchmark raft-log/shared-cursor`.
Native baseline: `python scripts/native-baseline.py --benchmark raft-log/shared-cursor --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Prepare and hash a test-only fixture that compiles on both revisions without reader algorithm edits.
- Disclose any targeted internal checkpoint; do not label it blind.
- Run ordinary native stress and distinguish probabilistic reproduction from deterministic replay.
