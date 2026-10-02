# Provenance

Upstream repository: https://github.com/databendlabs/openraft.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

The fixing commit reports replication remaining blocked when long inconsistent suffixes cause conflict responses to repeat a non-progressing position. Its upstream test constructs divergent logs directly. That test is a historical regression fixture, not an ordinary search workload.

- [Primary source](https://github.com/databendlabs/openraft/commit/6d53aa12f66ecd08e81bcb055eb17387b835e2eb)

Reviewed source anchors: async-raft/src/core/append_entries.rs, async-raft/src/replication/mod.rs, async-raft/tests/append_inconsistent_log.rs. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

The small upstream regression-test patch is copied with original MIT/Apache licenses and hashed postimages. Native build/test logs for both revisions are retained in results/baselines; see docs/BASELINE_OBSERVATIONS.md. The vulnerable fixture failed before the replication condition, so these logs establish build preparation, not historical replication reproduction.
