# Research provenance

LOCAL_DST_RESEARCH is the read-only repository named adversary-research, acquired from [sattwyk/adversary-research](https://github.com/sattwyk/adversary-research). Consulted commit: `bdd898d48c77b5c55c45c7b776e8349caf56c3ca`. It was cloned into ignored `.inputs/adversary-research`; its worktree remains unchanged. No original user repository was edited. No research runtime, scheduler, storage model or experiment implementation is imported into this repository.

Consulted documents at that immutable commit:

| Document | SHA-256 |
|---|---|
| README.md | 3a01f697803b4a2123550b85eff1d9131b756ad25e267d4a140ed67ab9e190ac |
| docs/STATUS.md | 6a4015824412980bba8792b8af568047dacfa56b87021253303f856f515c3902 |
| docs/research/runtime-comparison-progress.md | 3126dbf5a446129efef2f09ceb9d5f6fab699094da7dcd8afa494b01f95f6f6e |
| docs/research/production-topology.md | 8e76d3e2ded9cdedb8d4d3a6be028f4c18787612fe3283da9567d2175c76c2b1 |
| docs/research/topology-experiment-results.md | e966bca4092331d3eb54f88819d89f754f279a86f4b6151d6e5b4a82bc69fcd3 |
| docs/research/continuation-review.md | 1d6cf6686f494dde9361238db0177ebe097e37c88364fc8a04b099766c87de5e |
| docs/history/continuation-kill-criteria.md | 6e717f12904bea88569bb7e9b74ada044c84e5f1c9f0eb24c7ba33ddb006c252 |
| docs/briefs/adversary-rfc.md | dd7e330ebf68e9493610a632f4a65bb2021249228a92ee6aee49c649d51c4fe8 |
| docs/briefs/runtime-comparison-objective.md | 1a4edfa1ace77428bc2ea648b9ab29b6c6f15f1d1bd7fed860ec7eb311b76031 |

Experiment inputs consulted: experiments/runtime-comparison/README.md, reader_boundary.rs, shared.rs, runtime_probe.rs, sync_failure.rs and manifest patches; experiments/continuations/README.md, the host/guest manifests and lockfiles, redb_probe.rs and native_fiber_probe.rs. These explain prior claims and boundaries; they are not executed in this repository.

Claims carried forward as dated external evidence:

- The runtime-comparison ledger reports matched storage-worker hosting on four viable configurations, with controller-owned scheduling; it does not establish independent runtime scheduling or a multi-node simulation. The later ledger updates the earlier topology report's unfinished comparison status, without retroactively changing earlier evidence.
- The reader-boundary experiment reports that a targeted internal checkpoint exposed the seek/read race while coarser boundaries missed it. Its Shuttle search/replay is an external historically informed experiment, not blind rediscovery here.
- A quota-four controller blocked a valid sequential producer; this is a harness-artifact negative control. [Original attack evidence](https://github.com/sattwyk/adversary-research/tree/bdd898d48c77b5c55c45c7b776e8349caf56c3ca/results/2026-09-20/checkpoint-gate).
- Production topology includes native WAL workers, bounded channels/quotas, callbacks, shared caches, snapshot/apply workers and separate file/namespace publication. These motivate capability and preservation audits.
- Continuation probes report synchronous-stack preservation for a small fixture and single-owner redb, and ordinary native fiber Drop executing application cleanup. These motivate distinct cancellation, process-death and power-loss semantics.
- Rejection criteria require narrowing or rejecting a boundary when it hides relevant concurrency, changes correctness algorithms, needs excessive OS/runtime emulation or cannot be qualified against native outcomes.

Claims explicitly not carried forward:

- No superiority, throughput, cheap integration, language neutrality, Wasm necessity, general deterministic cluster, native filesystem conformance or novel production bug discovery.
- Graceful reopen is not power loss. Manually edited recovery images do not prove a native storage outcome is admitted. A whole private-memory invocation does not preserve competing shared-memory contexts.
- Four sequential historical API/storage scenarios are not five distributed production incidents and do not prove reachability from a correct Raft core. Unfinished callback experiments and original failed builds remain failures/incomplete evidence.
- Proposed RFC profiles, SDK, WIT ABI and scheduler designs are candidate semantics, not requirements on the future implementation's architecture. Only independent invariant/environment requirements are normative here.

External historical results remain in their original repository: [reader replay](https://github.com/sattwyk/adversary-research/tree/bdd898d48c77b5c55c45c7b776e8349caf56c3ca/results/2026-09-20/reader-boundary-replay), [runtime matrix](https://github.com/sattwyk/adversary-research/tree/bdd898d48c77b5c55c45c7b776e8349caf56c3ca/results/2026-09-20/runtime-matrix-final), and [continuation probes](https://github.com/sattwyk/adversary-research/tree/bdd898d48c77b5c55c45c7b776e8349caf56c3ca/results/2026-09-19/wsl-continuations).

The ten corpus source pairs/anchors were separately inspected upstream and verified locally. `sources/verification.json` preserves the identities. HashiCorp #695 lacks an accepted fix; an open PR's merge-preview object is explicitly excluded as a fixed pin. SQLite's narrow git fix maps to the recorded Fossil origin; the published version pair is not silently substituted.

New baseline observations belong to this repository, with actual commands, dependencies, patches and stdout under results/baselines. The only copied upstream code is two small test-only regression patches, attributed with original license files in their patches directories. They are excluded from search packages. No research code was copied wholesale or relicensed.
