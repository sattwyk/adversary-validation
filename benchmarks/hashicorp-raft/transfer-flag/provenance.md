# Provenance

Upstream repository: https://github.com/hashicorp/raft.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

The fix states that 1.3.4 reset the leadership-transfer flag only on success, leaving it set after failed transfer and breaking callers that require it cleared. No production incident is asserted.

- [Primary source](https://github.com/hashicorp/raft/pull/493)
- [Primary source](https://github.com/hashicorp/raft/commit/f2fdbd651e1d824151bfb0f73aa297b8903632ac)

Reviewed source anchors: raft.go, raft_test.go. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.

