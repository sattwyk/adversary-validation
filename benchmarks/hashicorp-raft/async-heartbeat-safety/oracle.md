# Independent oracle

No two replicas apply different commands at the same committed index; at most one elected leader may have valid election authority in a term.

Compare independent committed/apply witnesses at matching indices and vote/election evidence; distinguish a candidate's belief from quorum-certified election. Client histories supplement the internal witness.

Required witness: Term/role observation with task/thread identity, asynchronous incoming heartbeat, overlapping main protocol operation, emitted log identity/value, commit quorums and conflicting applied values.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

