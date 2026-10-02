# Independent oracle

After faults stop and all three voters have fair communication and execution, a stable leader's committed prefix must propagate to every running follower within the declared recovery bound.

Require at least 100 successful post-heal commits and convergence of each follower's committed/applied prefix to the stable leader. Validate fair delivery before interpreting timeout.

Required witness: Divergent prefixes reached through ordinary operations, conflict responses, unchanged next replication position, healthy-period deliveries, timer progress and convergence deadline.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

