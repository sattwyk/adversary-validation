# Committed entry deletion across crash

Corpus class C. SOURCE-IDENTIFIED; source review only at specification creation. No local historical reproduction is implied. See benchmark.json for current status and native observations for separately scoped executed baselines.

The fix documents committed-entry loss when AppendEntries deletes consistent entries before replacing them and a server crashes between the storage calls. It also describes possible application of an inconsistent uncommitted entry. This benchmark targets the committed-loss mechanism only.

Vulnerable: `05ecf7efab1cf7399eea5ede589d86878eb73d42`. Fix: `9540c904da4ae005baec01868e01016f3bc76810`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark openraft/committed-delete-crash`.
Verify: `python scripts/verify-pins.py --benchmark openraft/committed-delete-crash`.
Native baseline: `python scripts/native-baseline.py --benchmark openraft/committed-delete-crash --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Prepare a local storage implementation satisfying this historical RaftStorage contract without changing the Raft algorithm.
- Audit delete/append persistence and abrupt restart semantics.
- Execute the historical fixture before claiming S1 or production storage correspondence.

