# Provenance

Upstream repository: https://github.com/etcd-io/etcd.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

Issue #7331 reports a newly elected leader returning an older committed index before it commits a current-term entry, admitting stale ReadIndex results. The issue is closed by #7332. This is not the later duplicated-context defect; retry/duplicate attempts are workload dimensions, not claimed as this fix's cause.

- [Primary source](https://github.com/etcd-io/etcd/issues/7331)
- [Primary source](https://github.com/etcd-io/etcd/pull/7332)
- [Primary source](https://github.com/etcd-io/etcd/commit/9342647e0c9b9a2a12e4bc5ee76d28d5b9f29f83)

Reviewed source anchors: raft/raft.go, raft/raft_test.go, raft/read_only.go. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.

