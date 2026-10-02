# Reviewer-only historical mechanism

A leader re-sends a suffix containing an already committed matching entry. The follower deletes after the predecessor, then dies before append restores the entry. With the prior leader unavailable, a new quorum can elect a node missing the committed value. The fix skips consistent entries and orders commit-index advancement after append.

Primary sources: [upstream](https://github.com/databendlabs/openraft/commit/9540c904da4ae005baec01868e01016f3bc76810).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

