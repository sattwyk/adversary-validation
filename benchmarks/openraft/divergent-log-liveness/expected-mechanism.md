# Reviewer-only historical mechanism

The follower searches a bounded suffix forward and keeps reporting its last log as conflict, so the leader retries the same predecessor. The upstream fixture synthesizes suffixes exceeding the historical scan limit. Future search must create divergence through normal writes, partitions and elections, not import those synthetic initial images.

Primary sources: [upstream](https://github.com/databendlabs/openraft/commit/6d53aa12f66ecd08e81bcb055eb17387b835e2eb).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

