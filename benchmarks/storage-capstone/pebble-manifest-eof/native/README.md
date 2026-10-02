# Native baseline

Upstream fixture uses CrashableMemFS and manifest-specific random crash sampling. It is an upstream model/regression baseline, not native power-loss confirmation or blind search. Parent lacks the added test.

Reference command (at acquired target root):

```text
go test -v -mod=readonly -run '^TestCrashDuringManifestWrite_LargeKeys$' -count=1 -timeout=120s .
```

Toolchain: go1.26.4. Availability: fixed-only. Upstream module files are immutable within the source tree; -mod=readonly rejects updates.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.
