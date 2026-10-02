# Reviewer-only historical mechanism

Apply completes separately, snapshot publication advances last_applied, then RaftCore consumes the older apply completion and publishes its lower position. The fix serializes state-machine mutation. Do not add serialization to the vulnerable target.

Primary sources: [upstream](https://github.com/databendlabs/openraft/commit/eed681d57950fc58b6ca71a45814b8f6d2bb1223).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

