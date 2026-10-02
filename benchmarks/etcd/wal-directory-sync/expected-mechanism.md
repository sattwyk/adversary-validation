# Reviewer-only historical mechanism

A newly synced temporary WAL is renamed; additional acknowledged records are synced through the same file identity but the rename may remain volatile. After power loss recovery sees a temporary rather than recognized segment name and can discard it. The fix syncs the directory after rename.

Primary sources: [upstream](https://github.com/etcd-io/etcd/issues/6368), [upstream](https://github.com/etcd-io/etcd/pull/6381), [upstream](https://github.com/etcd-io/etcd/commit/bd7107bd4bf26219ba9852aa6c4c817ccde0191c).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

