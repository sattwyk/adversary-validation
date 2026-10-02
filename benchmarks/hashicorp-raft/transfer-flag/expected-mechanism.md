# Reviewer-only historical mechanism

Leadership transfer exits via failure without clearing the in-progress flag, so the existing leader can continue rejecting work. The fix resets the flag on all goroutine exits. A future liveness witness must show fair healthy progress and continuing rejection, not just one rejected request.

Primary sources: [upstream](https://github.com/hashicorp/raft/pull/493), [upstream](https://github.com/hashicorp/raft/commit/f2fdbd651e1d824151bfb0f73aa297b8903632ac).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

