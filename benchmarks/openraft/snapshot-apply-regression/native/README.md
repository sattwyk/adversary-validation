# Native baseline

Existing baseline exercises snapshot behavior but does not force or demonstrate the historical interleaving.

Reference command (at acquired target root):

```text
cargo +1.97.1 test --locked -p async-raft --test snapshot_overrides_membership -- --nocapture
```

Toolchain: 1.97.1. Availability: both. Additional build/dependency pinning remains required; no dependency solution is invented.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.

