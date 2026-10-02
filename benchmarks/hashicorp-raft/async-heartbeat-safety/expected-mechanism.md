# Reviewer-only historical mechanism

Transport-thread heartbeat handling may increase currentTerm and change role concurrently with the main Raft path creating entries or processing votes. A main-loop operation can observe inconsistent authority/term state. Preserve the native heartbeat fast path and protocol goroutines.

Primary sources: [upstream](https://github.com/hashicorp/raft/issues/695), [upstream](https://github.com/hashicorp/raft/pull/701).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

