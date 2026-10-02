# Capability matrix

Source-justified requirements, not implemented capabilities or passing results. A dash is outside this benchmark envelope, not a project-wide absence.

| Benchmark | network | storage | time | crash | concurrency | history |
|---|---|---|---|---|---|---|
| etcd/readindex-new-leader | ✓ | — | ✓ | — | — | ✓ |
| etcd/wal-directory-sync | — | ✓ | — | ✓ | — | — |
| hashicorp-raft/async-heartbeat-safety | ✓ | — | ✓ | — | ✓ | ✓ |
| hashicorp-raft/transfer-flag | ✓ | — | ✓ | — | — | — |
| openraft/committed-delete-crash | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| openraft/divergent-log-liveness | ✓ | — | ✓ | — | — | — |
| openraft/snapshot-apply-regression | ✓ | — | ✓ | — | ✓ | — |
| raft-log/shared-cursor | — | — | — | — | ✓ | — |
| sqlite/wal-reset | — | ✓ | — | — | ✓ | — |
| storage-capstone/pebble-manifest-eof | — | ✓ | — | ✓ | ✓ | — |

A's native file cursor is a concurrency requirement, not a storage-fault model. C includes elections/messages because the documented crash mechanism requires a later quorum. G does not need crash injection to expose its race. H requires concurrency plus network/election; process crashes are optional and excluded from this initial envelope. J's upstream crash clone is a model, not native power-loss qualification.

Required capability details are in each environment.json and docs/MODEL_REQUIREMENTS.md.
