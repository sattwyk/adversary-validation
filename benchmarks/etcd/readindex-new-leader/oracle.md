# Independent oracle

Completed reads are linearizable: a read beginning after a write completes must observe that write or a later valid write, respecting concurrent and unknown operations.

Check invocation/response histories against an independent register model; reads wait for application through the returned index. A protocol ReadIndex certificate alone is not a completed application read.

Required witness: Predecessor write success, later read invocation/response, prior commitment evidence, new leader/election and read certificate, applied index and returned value.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

