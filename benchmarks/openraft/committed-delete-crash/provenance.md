# Provenance

Upstream repository: https://github.com/databendlabs/openraft.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

The fix documents committed-entry loss when AppendEntries deletes consistent entries before replacing them and a server crashes between the storage calls. It also describes possible application of an inconsistent uncommitted entry. This benchmark targets the committed-loss mechanism only.

- [Primary source](https://github.com/databendlabs/openraft/commit/9540c904da4ae005baec01868e01016f3bc76810)

Reviewed source anchors: async-raft/src/core/append_entries.rs, async-raft/src/storage.rs. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.

