# Independent oracle

After an admissible interrupted manifest append, recovery must open the last durable coherent version and retain every acknowledged Sync write; complete malformed records must not be silently accepted as a legal tail.

Independent acknowledged map compared after actual Open/recovery. Require successful recovery for legal incomplete envelope states; malformed complete-record control requires detected corruption, not silent success. Preserve uncertainty for writes without observed successful Sync result.

Required witness: Version-edit record/block boundaries, WAL/SST/manifest identities and fences, flush/compaction/publication dependencies, legal crash image, recovery parser verdict and acknowledged/recovered values.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

