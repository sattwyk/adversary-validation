# Provenance

Upstream repository: https://github.com/hashicorp/raft.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

Issue #695 reports divergent committed values and election safety violations during partition/election and asynchronous heartbeat races. A maintainer calls the report plausible and difficult to reproduce but had not reproduced it in the cited comment. PR #701 is open and is not an accepted historical fix/control.

- [Primary source](https://github.com/hashicorp/raft/issues/695)
- [Primary source](https://github.com/hashicorp/raft/pull/701)

Reviewed source anchors: raft.go, net_transport.go, replication.go. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source report and its unresolved candidate fix were investigated separately for this corpus. No verified vulnerable/fixed pair exists for this case.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.
