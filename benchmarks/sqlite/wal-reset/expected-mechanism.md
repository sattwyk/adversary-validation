# Reviewer-only historical mechanism

A checkpoint captures stale header state, a writer resets the WAL generation, then checkpoint work proceeds using the old view and may advance backfill incorrectly. A later checkpoint can skip data. Fix checks live generation salts under the lock. Whole SQLite calls treated atomically cannot represent this.

Primary sources: [upstream](https://sqlite.org/wal.html#walreset), [upstream](https://sqlite.org/src/info/5aadfbbdd83b051b), [upstream](https://github.com/sqlite/sqlite/commit/3c7a03032f9c69feb832b96447701bee6fa3ba81).

This file is prohibited search input. Use it only for explicit reproduction setup or post-hoc S5 review. Matching a final symptom does not establish the causal mechanism. No execution was performed merely by writing this specification.

