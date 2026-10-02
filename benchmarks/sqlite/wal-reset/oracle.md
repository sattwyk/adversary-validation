# Independent oracle

Successful committed transactions remain present and database contents/integrity match the sequential transactional specification after concurrent checkpoint/write activity and normal reopen.

Use independently recorded transaction IDs/values and legal transactional ordering, full table comparison plus PRAGMA integrity_check after checkpoint and reopen. Integrity_check alone can miss lost logical updates.

Required witness: Checkpoint header generation, writer reset/generation, native shared-memory identities and lock transitions, checkpoint backfill publication, committed input table and recovered table mismatch.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

