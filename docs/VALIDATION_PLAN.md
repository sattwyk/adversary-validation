# Validation plan

This repository can falsify bounded claims about a future engine's represented behavior, replay, search and preservation. It cannot currently certify Adversary: no implementation or search campaign exists here. Nine historical fix/parent pairs and one unresolved safety report are pinned; all ten have ordinary workload, oracle, fault-envelope and capability specifications.

## 1. Exact claims this suite can test

Whether a chosen boundary admits the historical mechanism; whether an explicit failing execution is reproducible; whether generic search finds it; whether the fixed pair rejects it under matched conditions; whether trace and native evidence support the same cause. Each assertion maps to S0–S8 with independent artifact requirements. The suite may establish an engine's insufficiency without establishing a bug in the target.

## 2. Claims it cannot test

Universal correctness, complete state-space coverage, weak-memory correctness, all operating systems/filesystems/devices, full native service transport from module-only RPC tests, runtime economic superiority, or novel discovery from rediscovering a known bug. Finite fixed-version success is not a proof. S9 is optional and unearned.

## 3–5. Preparation status and upstream gaps

| Class | Source identity | Prepared executable pieces | Remaining work |
|---|---|---|---|
| A raft-log shared cursor | Verified fix/parent/tree; native reader code retained | Same upstream reader fixture on both revisions, test-only parent patch, shared frozen dependency lock and native command | Internal event trace/replay, independent full range oracle and ordinary search driver |
| B OpenRaft divergent logs | Verified 2021 async-raft fix/parent/tree | Both revisions built/tested; test-only parent transplant and common frozen dependency lock | Investigate early vulnerable election timeout; historical replication witness, ordinary API-created divergence, fair search and replay |
| C OpenRaft committed delete/crash | Verified fix/parent/tree and documented storage sequence | Acquisition and surrounding native test instructions | Historical dependency freeze, durable storage adapter, abrupt crash/restart fixture, commit/history witness |
| D OpenRaft snapshot/apply | Verified fix/parent/tree and separate publication paths | Acquisition and surrounding snapshot test instructions | Dependency freeze, observational publication hooks, multiple-continuation fixture |
| E etcd ReadIndex | Verified #7331/#7332 fix/parent/tree | Acquisition and exact historical test identity | Historical GOPATH/glide dependency build, test-only parent fixture, application history integration |
| F etcd WAL directory sync | Verified #6368/#6381 fix/parent/tree | Acquisition and rotation/reopen baseline instructions | Frozen GOPATH dependencies; concrete native filesystem/power-cut qualification; namespace/fence observations |
| G SQLite WAL reset | Verified narrow git fix/parent and Fossil identity | Acquisition; native threaded/VFS assumptions retained | Compiler/Tcl/configure pins, published native reproducer execution, shared-index schedulability audit |
| H HashiCorp async heartbeat | Report-anchored source verified; no accepted fixed control | Acquisition; native source/transport audit | Upstream accepted fix, independently demonstrated full safety witness; open #701 is not promoted |
| I HashiCorp transfer flag | Verified #493 fix/parent/tree | Native module pins and same three surrounding transfer tests on both revisions | Exact continuing-progress failure fixture, fair recovery oracle and trace |
| J Pebble manifest EOF | Verified mainline fix/parent/tree | Acquisition, module pins and upstream fixed fixture identified | Late-stage multi-object native crash qualification, parent fixture compatibility, independent acknowledged-map oracle |

Fully prepared means a stated workflow is executable, not that every gate is earned. A/B/I have acquisition and native baseline preparation; no benchmark is fully prepared for blind search, qualified power-loss validation or all S0–S8 gates. Other paired rows are source-identified specifications with explicit preparation gaps. H needs additional upstream investigation. Do not convert these gaps into passing results. Consult BASELINE_OBSERVATIONS.md for what actually ran; this table describes laboratory readiness, not results.

## 6. Repeated capabilities

Message ordering and timers recur in B/C/D/E/H/I. Shared-memory or publication scheduling recurs in A/D/G/H/J. Storage/recovery recurs in C/F/G/J, while F specifically requires namespace durability and J multiple object identities. Histories are essential to C/E/H; internal assertions alone cannot support their external safety claims. See CAPABILITY_MATRIX.md for source-justified selections rather than assumptions based on project branding.

## 7. Lower-level model requirements

A needs a split between real file cursor operations. G requires native shared WAL-index memory and locking across connections; whole-call or private-memory serialization hides it. H requires transport and main protocol concurrency. F must retain rename, file identities and directory synchronization; a single byte vector erases the defect. J retains real WAL/table/manifest codecs and recovery dependencies. C needs actual storage calls plus process recovery and later elections; a consensus-only model misses the storage transition.

## 8. Scripted reproduction

An upstream regression with constructed log state, a precise failpoint, targeted event tape or known internal checkpoint is explicitly REPRODUCTION. B's constructed divergent suffix fixture is such input. A's native stress fixture is historically authored regression input; an observed failure has no automatic deterministic schedule or causal trace. Scripted fixtures stay outside the search package and require their own result evidence.

## 9. Genuine rediscovery

A frozen generic policy receives only normal workload, configuration, whole-class fault envelope, independent oracle and budget. It discovers a violation, emits the complete bundle, and passes independent causal/replay review. A blind claim additionally requires independent policy authors with no mechanism/fix access and auditable isolation. This repository's author is not blind.

## 10. Overfitting

Supplying the known crash point, minimal schedule, divergent initial log image, site-specific weight based on the fix, or selectively reporting successful seeds. Internal checkpoints justified from a known race must be disclosed. Avoid dropping unsupported rows from a headline denominator or changing the fixed run's budget/faults to obtain green results.

## 11. Fair vulnerable/fixed comparison

Exact pair SHAs, identical dependency solution where possible, toolchain/flags, source-preserving instrumentation, workload, envelope, oracle, seeds, policy and budget. Build both from fresh state. Preserve failures and censored searches. Test original counterexample admission separately from fresh exploration: changed fixed code may remove a choice site and require semantic correspondence instead of literal tape consumption. Report such divergence explicitly.

## 12. Harness-induced failures

Metadata/trace grammar controls, known-valid and planted-invalid oracle histories, unsupported capability declarations, zero-test rejection and artifact hashes run before target judgment. Inspect enabled tasks/operations and healthy progress when liveness fails. Compare instrumentation disabled/passive/active and sequential/pipelined clients. The historical four-request gate is a required controller artifact control. Compilation, recorder and watchdog failures cannot be target discoveries.

## 13. Evidence before production correspondence

Audit correctness-sensitive functions and their actual exercised paths, original worker ownership/locks/queues, callback timing, codecs, durability fences, transport boundary and restart recovery. Save full diffs/patch hashes and dependency identities. Qualify model contracts against named native kernel/filesystem/mount/device environments; independently validate the causal condition with native execution where feasible. Neither unchanged LOC nor a passing in-memory storage test is enough.

## 14. Minimum subset before implementing Adversary

Finish reviewer-approved S0 and baseline/checker preparation on A/B/C/F, retaining G as an architectural boundary control. These cover intrafunction native concurrency, distributed liveness, crash/committed safety and namespace durability. Demonstrate S1 on A and one persistence case, validate checker controls, freeze ordinary inputs and fault budgets, and inventory production escape points. I supplies a cheap additional liveness control; J is late-stage. H's unresolved fix should not block the smaller initial decision, but must remain visible.

## 15. Evidence justifying boundary changes

A reproduced historical condition excluded by a coarse atomic region; a necessary shared-memory/native worker absent from the guest; a native allowed recovery image excluded by the persistence contract; repeated unexplained replay divergence; or cheaper matched existing-tool integration preserving more relevant behavior. Measure the missing semantic distinction and integration cost before adding a new subsystem. Narrow or reject a capability claim when qualification fails; do not weaken the historical workload.
