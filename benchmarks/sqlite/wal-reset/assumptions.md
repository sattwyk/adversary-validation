# Environmental assumptions

- Native connections share the same database, WAL and mapped WAL-index locks/state. Normal writer/reset and checkpoint progress may overlap. No process crash or media error in this race envelope.

Required capabilities: shared-memory-scheduling, shared-wal-index, storage-ordering, multi-object-recovery. Preserve source behavior even when the adapter returns UNSUPPORTED. environment.json is the versioned search envelope. Numeric budgets are workload.json parameters and must be identical for both revisions.

Exclusions: Byzantine behavior; weak-memory exploration; unqualified native filesystem/device power-loss correspondence; full production service transport/framing outside the stated module boundary. Model conformance is unqualified until independently executed. An in-memory test store is not production durable-storage correspondence. A timeout is not target liveness evidence until healthy/fair progress and controller independence are shown.

