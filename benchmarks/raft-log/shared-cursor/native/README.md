# Native baseline

The verified fully qualified test is tests::test_concurrent_read::test_concurrent_read_race_condition. Acquisition applies the hashed test-only parent patch and common frozen Cargo.lock. Both revisions were built and tested; see docs/BASELINE_OBSERVATIONS.md. The fixture is not the proposed ordinary search workload and supplies no recorded event schedule.

Reference command (at acquired target root):

```text
cargo +1.97.1 test --locked --lib tests::test_concurrent_read::test_concurrent_read_race_condition -- --exact --nocapture
```

Toolchain: 1.97.1. Availability: both after acquisition's test-only patch. The shared dependency solution is native/Cargo.lock, hashed in native/baseline.json; upstream constraints remain unchanged.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.
