# Divergent logs permanently block replication

Corpus class B. BASELINE-PREPARED: both pinned revisions build and execute the upstream constructed-log fixture. The vulnerable run timed out during election setup, before the historical replication condition; the fixed run passed. Historical mechanism reproduction remains unestablished. See docs/BASELINE_OBSERVATIONS.md and benchmark.json.

The fixing commit reports replication remaining blocked when long inconsistent suffixes cause conflict responses to repeat a non-progressing position. Its upstream test constructs divergent logs directly. That test is a historical regression fixture, not an ordinary search workload.

Vulnerable: `ab6689d951954e3adbe8eb427364cf9062da1425`. Fix: `6d53aa12f66ecd08e81bcb055eb17387b835e2eb`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark openraft/divergent-log-liveness`.
Verify: `python scripts/verify-pins.py --benchmark openraft/divergent-log-liveness`.
Native baseline: `python scripts/native-baseline.py --benchmark openraft/divergent-log-liveness --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Freeze compatible Cargo.lock for both revisions.
- Transplant only regression test after checking fixture/API differences.
- Prepare an ordinary API workload adapter that creates divergence without supplied log images.
