# Provenance

Upstream repository: https://github.com/databendlabs/openraft.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

The commit documents last_applied being reset to an earlier position by completion of an apply task after snapshot installation. State-machine changes had run in separate continuations. It does not document power-loss data loss.

- [Primary source](https://github.com/databendlabs/openraft/commit/eed681d57950fc58b6ca71a45814b8f6d2bb1223)

Reviewed source anchors: async-raft/src/core/install_snapshot.rs, async-raft/src/core/append_entries.rs, async-raft/src/core/mod.rs. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.

