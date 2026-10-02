# Independent oracle

Within a process incarnation, accepted state-machine progress never publishes a lower last-applied index after a later prefix has become visible. Its applied values must remain consistent with that prefix.

Observe serialized publication events for process-incarnation last_applied and state digests. Reject any decrease without an explicitly declared restart; independently compare values against committed prefix.

Required witness: Earlier apply completion, later snapshot prefix, publication events, task identities, same incarnation and observed regression. Normal monotonic metric sampling alone may miss a transient regression.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

