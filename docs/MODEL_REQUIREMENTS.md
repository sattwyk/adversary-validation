# Required semantics, envelope version 1

These are requirements on future adapters, not model implementations.

| Capability | Required meaning |
|---|---|
| message-ordering | Delay/drop independently sent protocol RPCs and their replies, asymmetric partitions and later healing. A decoded-RPC boundary excludes production byte-stream behavior; record it. |
| timers | Monotonic clocks advance; expiry occurs at/after deadlines; eligible timeout and message handlers may race. No early expiry or implicit election notification. |
| process-crash | Abrupt termination of all process continuations without application cleanup; restart runs ordinary recovery. Kernel cache and issued IO are not automatically erased. |
| power-loss | Loss of explicitly volatile storage under a named qualified profile; successful fences survive absent declared media fault. Distinct from SIGKILL. |
| storage-ordering | Submission, live effect, completion and persistence are distinct; failed operations may have partial effects; later sync covers its declared preceding fence. |
| directory-durability | File contents/length and namespace durability differ; same-filesystem rename is atomic live, not automatically durable. Open handles alias file identity across rename. Directory sync covers prior namespace effects. |
| shared-memory-scheduling | Real independently runnable threads/tasks, original sharing/locks and schedulable relevant internal operations. Whole-call atomicity is insufficient for A/G/H. Weak memory requires separate qualification. |
| shared-wal-index | Native SQLite connections share coherent mapped WAL-index metadata and real lock semantics. Private-memory instances or exclusive mode do not qualify. |
| client-history | Invocation, response, logical ID, attempt ID, unknown outcome, term/index/value where observed, and real-time precedence. Retries are new attempts, not rollback. |
| multi-object-recovery | Separate WAL, manifest, table, database and temporary objects, identities, deletion/publication and actual recovery parsers. No single durable key/value surrogate. |
| concurrent-publication | Application and snapshot continuations can both progress; observation records publication and completion order without moving locks or inventing dependencies. |
| fair-progress | After healing, continuously enabled tasks, IO and messages run within a declared bound; no required future producer input is invented by the controller. |

Ordinary storage profile excludes spontaneous corruption of previously fenced untouched bytes. A separate opt-in malformed-record control may test rejection, with scope clearly recorded. Short writes accept a positive prefix, loop behavior remains upstream; error/unsynced persistence does not imply rollback. Failed sync may have persisted data, but successful sync is trustworthy within the profile.

No universal ext4/XFS/NVMe mapping is claimed. Native conformance records syscall/effect histories and recovery images on exact deployments; power-loss claims require a controlled disposable VM/block/device test, not graceful close or a manually edited file. Future implementations may use native checkpoints, existing runtimes, Wasm or combinations. Architecture names confer no capability.

Byte-stream framing is a separate production qualification: within a connected direction accepted bytes arrive as an ordered prefix, never arbitrarily reordered/duplicated application frames. Application retry across reconnections may duplicate requests. This initial protocol-module corpus does not establish full service transport coverage.

