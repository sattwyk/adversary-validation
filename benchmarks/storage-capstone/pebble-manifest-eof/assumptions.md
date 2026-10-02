# Environmental assumptions

- Up to two power cuts over all objects in one volume. Completed successful sync fences survive. Unsynced append tails may be incomplete at declared record/block units; legal filesystem namespace states and cross-object dependencies must be qualified. No spontaneous corruption.
- Independently runnable native implementation tasks retain shared state and real synchronization; observation must not add serialization.

Required capabilities: storage-ordering, power-loss, multi-object-recovery, shared-memory-scheduling. Preserve source behavior even when the adapter returns UNSUPPORTED. environment.json is the versioned search envelope. Numeric budgets are workload.json parameters and must be identical for both revisions.

Exclusions: Byzantine behavior; weak-memory exploration; unqualified native filesystem/device power-loss correspondence; full production service transport/framing outside the stated module boundary. Model conformance is unqualified until independently executed. An in-memory test store is not production durable-storage correspondence. A timeout is not target liveness evidence until healthy/fair progress and controller independence are shown.

