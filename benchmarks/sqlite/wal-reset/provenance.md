# Provenance

Upstream repository: https://github.com/sqlite/sqlite.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

SQLite documents a rare checkpointer/writer WAL reset race that can corrupt database state. The fix was shipped in 3.51.3. Local source comparison confirms live salts are checked after taking the relevant lock. This suite has not executed the published reproduction.

- [Primary source](https://sqlite.org/wal.html#walreset)
- [Primary source](https://sqlite.org/src/info/5aadfbbdd83b051b)
- [Primary source](https://github.com/sqlite/sqlite/commit/3c7a03032f9c69feb832b96447701bee6fa3ba81)

Reviewed source anchors: src/wal.c, test/walrestart.test. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.

