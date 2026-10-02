# Native baseline

Existing upstream native tests are surrounding transfer baselines, not proof of the exact historical flag mechanism. Go module files are pinned by each tree; runtime/compiler differs from historical release and is disclosed.

Reference command (at acquired target root):

```text
go test -v -mod=readonly -run '^TestRaft_LeadershipTransfer(ToInvalidID|LeaderReplicationTimeout|StopRightAway)$' -count=1 -timeout=60s .
```

Toolchain: go1.26.4. Availability: both. Upstream module files are immutable within the source tree; -mod=readonly rejects updates.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.
