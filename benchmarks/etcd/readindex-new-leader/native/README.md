# Native baseline

Historical repository uses glide.lock rather than go.mod. A pinned GOPATH/vendor build must be prepared; the runner refuses unresolved manual baselines.

Reference command (at acquired target root):

```text
go test ./raft -run ^TestReadOnlyForNewLeader$ -count=1
```

Toolchain: Go historical GOPATH preparation pending. Availability: fixed-only. Additional build/dependency pinning remains required; no dependency solution is invented.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.

