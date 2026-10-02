# Reviewer-only historical mechanism

A new leader's local committed index lags the prior cluster commitment. Without a committed current-term entry its ReadIndex path can certify an index preceding a completed write. The fix gates safe reads on current-term commitment.

Primary sources: [upstream](https://github.com/etcd-io/etcd/issues/7331), [upstream](https://github.com/etcd-io/etcd/pull/7332), [upstream](https://github.com/etcd-io/etcd/commit/9342647e0c9b9a2a12e4bc5ee76d28d5b9f29f83).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

