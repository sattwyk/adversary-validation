# Reviewer-only historical mechanism

Two readers share the same open file description. A seek is followed by another reader's seek before the first read. Wrong record bytes enter the unchanged decoder. The fix replaces cursor-based reads with positional reads. The research fixture used one targeted test-only checkpoint; this is historically informed instrumentation, not a blind input.

Primary sources: [upstream](https://github.com/drmingdrmer/raft-log/commit/707a9a2463ab215175ef9fbc8d86ea57c2aeac72).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

