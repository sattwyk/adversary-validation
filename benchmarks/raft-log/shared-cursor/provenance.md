# Provenance

Upstream repository: https://github.com/drmingdrmer/raft-log.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

The fix describes concurrent readers overwriting a shared seek position before another reader consumes a record, causing reads at incorrect offsets. It adds a concurrent-reader regression. No production incident is claimed.

- [Primary source](https://github.com/drmingdrmer/raft-log/commit/707a9a2463ab215175ef9fbc8d86ea57c2aeac72)

Reviewed source anchors: src/chunk/mod.rs, src/tests/test_concurrent_read.rs. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

External research reference: [dated research evidence](https://github.com/sattwyk/adversary-research/blob/bdd898d48c77b5c55c45c7b776e8349caf56c3ca/docs/research/runtime-comparison-progress.md#historical-shared-cursor-race). This repository has not rerun or imported that fixture.

The small upstream test-only patch is copied with its original Apache license and hashed postimages. Native build/test logs for both revisions are retained separately in results/baselines; see docs/BASELINE_OBSERVATIONS.md. They do not rerun or import the external research scheduler fixture, and no search/replay evidence is claimed.
