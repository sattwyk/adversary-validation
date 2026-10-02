# Environmental assumptions

- Protocol-module RPC sends/replies may be delayed, dropped or delivered in different orders across independent sends. Message payloads are not changed. Same-connection TCP ordering is not claimed at this boundary.
- At most one node is isolated at a time during the fault phase; directional edges may stop progress. Every edge heals before recovery; no immediate membership notification.
- Election/heartbeat timers expire at or after actual configured deadlines; eligible RPC and timeout handlers can run in either order. Clocks advance during recovery.
- A timeout leaves an unknown result. Up to three ordinary retries use recorded logical and attempt IDs. Duplicates arise through application attempts, not arbitrary TCP byte duplication.

Required capabilities: message-ordering, timers, client-history. Preserve source behavior even when the adapter returns UNSUPPORTED. environment.json is the versioned search envelope. Numeric budgets are workload.json parameters and must be identical for both revisions.

Exclusions: Byzantine behavior; weak-memory exploration; unqualified native filesystem/device power-loss correspondence; full production service transport/framing outside the stated module boundary. Model conformance is unqualified until independently executed. An in-memory test store is not production durable-storage correspondence. A timeout is not target liveness evidence until healthy/fair progress and controller independence are shown.

