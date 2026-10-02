# Native baseline

Pinned vulnerable revision is the report's source anchor. Candidate PR is deliberately unpinned as a fix; do not call an open PR merge-preview SHA a merged fix. No fixed comparison is available.

Reference command (at acquired target root):

```text
go test -mod=readonly -race ./...
```

Toolchain: Go 1.26.4 candidate baseline. Availability: vulnerable-only. Upstream module files are immutable within the source tree; -mod=readonly rejects updates.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.

