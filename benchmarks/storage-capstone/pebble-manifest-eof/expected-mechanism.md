# Reviewer-only historical mechanism

Large version edits span record blocks. A crash leaves a partial envelope which some parsing paths recategorize as corruption. Conversely, a complete envelope with a truncated version-edit body can be silently treated as a trailing interrupted record. Cross-object WAL/SST/manifest state and the real record parser matter.

Primary sources: [upstream](https://github.com/cockroachdb/pebble/pull/4562), [upstream](https://github.com/cockroachdb/pebble/issues/4561), [upstream](https://github.com/cockroachdb/pebble/commit/c532754949aacd080d6f774b6d244dbcb32ac23c).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

