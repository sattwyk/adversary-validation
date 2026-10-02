# Native baseline

Ordinary close/reopen is a baseline only. SIGKILL does not test missing directory persistence; a qualified VM/block-device or native failpoint experiment is required.

Reference command (at acquired target root):

```text
go test ./wal -run ^TestRecoverAfterCut$ -count=1
```

Toolchain: Go historical GOPATH and qualified crash stack pending. Availability: both. Additional build/dependency pinning remains required; no dependency solution is invented.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.

