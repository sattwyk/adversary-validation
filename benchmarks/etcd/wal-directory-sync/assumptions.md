# Environmental assumptions

- Up to two power cuts over the local target volume. Writes/file-sync and rename/directory-sync remain distinct; a successful directory fence persists earlier namespace operations. Unsynced rename can recover old/new legally; handles retain inode identity. No loss of successfully fenced untouched bytes.

Required capabilities: storage-ordering, directory-durability, power-loss, multi-object-recovery. Preserve source behavior even when the adapter returns UNSUPPORTED. environment.json is the versioned search envelope. Numeric budgets are workload.json parameters and must be identical for both revisions.

Exclusions: Byzantine behavior; weak-memory exploration; unqualified native filesystem/device power-loss correspondence; full production service transport/framing outside the stated module boundary. Model conformance is unqualified until independently executed. An in-memory test store is not production durable-storage correspondence. A timeout is not target liveness evidence until healthy/fair progress and controller independence are shown.

