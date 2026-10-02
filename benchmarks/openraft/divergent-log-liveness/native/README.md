# Native baseline

The upstream fixture constructs initial divergence and is reproduction-only input, never search input. Acquisition supplies the exact test-only parent patch and the shared frozen native/Cargo.lock. Both builds executed locally: the vulnerable fixture failed early during election setup, so the historical replication mechanism remains unconfirmed.

Reference command (at acquired target root):

```text
cargo +1.97.1 test --locked -p async-raft --test append_inconsistent_log -- --nocapture
```

Toolchain: 1.97.1. Availability: both after acquisition's test-only patch. Dependency and patch hashes are recorded in native/baseline.json and benchmark.json. See docs/BASELINE_OBSERVATIONS.md for the exact observations.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.
