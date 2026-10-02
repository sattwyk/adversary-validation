# ReadIndex before current-term commitment

Corpus class E. SOURCE-IDENTIFIED; source review only at specification creation. No local historical reproduction is implied. See benchmark.json for current status and native observations for separately scoped executed baselines.

Issue #7331 reports a newly elected leader returning an older committed index before it commits a current-term entry, admitting stale ReadIndex results. The issue is closed by #7332. This is not the later duplicated-context defect; retry/duplicate attempts are workload dimensions, not claimed as this fix's cause.

Vulnerable: `ad1b754e020b6ab55d431e198d29932cd140c3e2`. Fix: `9342647e0c9b9a2a12e4bc5ee76d28d5b9f29f83`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark etcd/readindex-new-leader`.
Verify: `python scripts/verify-pins.py --benchmark etcd/readindex-new-leader`.
Native baseline: `python scripts/native-baseline.py --benchmark etcd/readindex-new-leader --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Acquire glide.lock dependencies with checksums in an isolated GOPATH.
- Transplant the upstream regression test as test-only reproduction input.
- Supply real history/state-machine integration above the protocol module.

