# Independent oracle

For every completed range read, each returned log identity and payload equals the requested immutable record; valid prewritten records do not produce decode/EOF errors due to other readers.

Compare (term,index,payload) tuples against an independent prewritten input table. On immutable valid data, unexpected decoding error/panic is a violation after harness causes are excluded.

Required witness: Requested range, exact stored input, returned identity/bytes, file identity, both reader operations and their causal overlap.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

