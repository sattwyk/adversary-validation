# Independent oracle

Every committed command remains represented in the committed history after admissible crash/restart and later elections; no later successful read or applied history may omit or replace it.

Record committed identities from quorum evidence and completed client writes; after recovery require the corresponding immutable committed prefix and linearizable sequential final reads. Storage effects must meet RaftStorage's documented contract.

Required witness: Commit quorum for the lost command, real delete and append calls, durable storage snapshots before/after death, fresh recovery/election evidence, recovered/applied prefix and client observation.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

