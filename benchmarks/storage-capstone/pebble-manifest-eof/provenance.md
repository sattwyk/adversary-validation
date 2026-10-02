# Provenance

Upstream repository: https://github.com/cockroachdb/pebble.git. Local full commit/tree pairs are in vulnerable.lock and fixed.lock; source acquisition and verification were performed in ignored caches. The first parent of the fixing commit is the vulnerable comparison convention, except the report-anchored unresolved class H.

Historical claim category: historical bug; no production incident claimed.

The fix distinguishes an incomplete manifest record envelope after interrupted append from malformed content inside a complete envelope. Previously recovery could reject an ordinary incomplete record or accept malformed complete content. This late-stage benchmark targets legal interrupted manifest append; malformed content is a separate detection control.

- [Primary source](https://github.com/cockroachdb/pebble/pull/4562)
- [Primary source](https://github.com/cockroachdb/pebble/issues/4561)
- [Primary source](https://github.com/cockroachdb/pebble/commit/c532754949aacd080d6f774b6d244dbcb32ac23c)

Reviewed source anchors: open.go, internal/manifest/version_edit.go, record/record.go, version_set_test.go. Source verification records, tree relationships and anchor blob IDs are in sources/verification.json. Upstream fixture behavior may construct state or use a specialized model; it is not silently a search result.

The prior research's architectural limits informed protocol design; this historical source pair was identified separately for this corpus.

Native/build/reproduction results require their own result bundles. Copies of upstream code must retain original licensing; initial specification files contain no copied upstream test code.

