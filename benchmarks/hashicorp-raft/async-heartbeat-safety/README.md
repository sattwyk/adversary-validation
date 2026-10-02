# Async heartbeat changes term concurrently with protocol path

Corpus class H. NEEDS-UPSTREAM-INVESTIGATION; source review only at specification creation. No local historical reproduction is implied. See benchmark.json for current status and native observations for separately scoped executed baselines.

Issue #695 reports divergent committed values and election safety violations during partition/election and asynchronous heartbeat races. A maintainer calls the report plausible and difficult to reproduce but had not reproduced it in the cited comment. PR #701 is open and is not an accepted historical fix/control.

Vulnerable: `4c8f61ac9255bb95fb3b8319dfcf0ae53ab325b6`. Fixed revision: unresolved; PR #701 is not a verified control.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark hashicorp-raft/async-heartbeat-safety`.
Verify: `python scripts/verify-pins.py --benchmark hashicorp-raft/async-heartbeat-safety`.
Native baseline: `python scripts/native-baseline.py --benchmark hashicorp-raft/async-heartbeat-safety --revision vulnerable` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Obtain an accepted reviewed upstream fix and exact parent pair, or independently validate a separately labeled candidate control.
- Execute the documented mechanism locally.
- Audit whether term access instrumentation itself serializes the race.

