# Provenance

Upstream repository: https://github.com/etcd-io/etcd.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

The reporter describes and reports reproducing possible WAL data loss after file sync and rename without syncing the parent directory; a maintainer agrees it appears to be a bug. The report permits correlated crashes. No production incident or local reproduction by this suite is claimed.

- [Primary source](https://github.com/etcd-io/etcd/issues/6368)
- [Primary source](https://github.com/etcd-io/etcd/pull/6381)
- [Primary source](https://github.com/etcd-io/etcd/commit/bd7107bd4bf26219ba9852aa6c4c817ccde0191c)

Reviewed source anchors: wal/wal.go, wal/wal_unix.go. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.

