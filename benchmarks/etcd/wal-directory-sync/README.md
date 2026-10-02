# WAL rename missing directory durability

Corpus class F. SOURCE-IDENTIFIED; source review only at specification creation. No local historical reproduction is implied. See benchmark.json for current status and native observations for separately scoped executed baselines.

The reporter describes and reports reproducing possible WAL data loss after file sync and rename without syncing the parent directory; a maintainer agrees it appears to be a bug. The report permits correlated crashes. No production incident or local reproduction by this suite is claimed.

Vulnerable: `c449da6ff9cb64d7f980e6f5deed4f6f82b70e39`. Fix: `bd7107bd4bf26219ba9852aa6c4c817ccde0191c`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark etcd/wal-directory-sync`.
Verify: `python scripts/verify-pins.py --benchmark etcd/wal-directory-sync`.
Native baseline: `python scripts/native-baseline.py --benchmark etcd/wal-directory-sync --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Pin GOPATH dependencies and build flags.
- Define a concrete Linux/filesystem/device qualification and disposable VM procedure.
- Validate that any synthetic namespace image is legally admitted; keep image fixtures labeled scripted.

