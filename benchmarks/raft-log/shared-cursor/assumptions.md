# Environmental assumptions

- Independent native readers share original file handles; schedule runnable readers inside operations where the target permits. No synthetic byte corruption or concurrent writes.

Required capabilities: shared-memory-scheduling. Preserve source behavior even when the adapter returns UNSUPPORTED. environment.json is the versioned search envelope. Numeric budgets are workload.json parameters and must be identical for both revisions.

Exclusions: Byzantine behavior; weak-memory exploration; unqualified native filesystem/device power-loss correspondence; full production service transport/framing outside the stated module boundary. Model conformance is unqualified until independently executed. An in-memory test store is not production durable-storage correspondence. A timeout is not target liveness evidence until healthy/fair progress and controller independence are shown.

