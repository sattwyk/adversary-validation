# Native baseline

Build Unix threaded shared-memory configuration; inspect test/walrestart.test for upstream scripted fault-sim regression. Retain original wal.c and native VFS/mapped state. Historical git parent/fix are the narrow pair; published 3.51.2/3.51.3 versions are additional future controls.

Reference command (at acquired target root):

```text
make test
```

Toolchain: C compiler/Tcl/make preparation pending. Availability: both. Additional build/dependency pinning remains required; no dependency solution is invented.

A baseline pass checks only the selected upstream fixture. It does not demonstrate S1–S5, a production incident or a discovered bug. The native runner records actual test count and refuses zero-test success. For a parent lacking the regression, retain a test-only compatibility patch/hash and exact original license before execution. Upstream algorithms must stay untouched.

