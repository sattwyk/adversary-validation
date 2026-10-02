# Independent oracle

After a finite failed transfer and restoration of fair quorum communication, new application commands must commit within the bounded recovery interval.

After healing and transfer completion/failure, require 100 new successful commands and follower convergence within 20 maximum election timeouts. Record transfer flag only as diagnosis; progress is the independent property.

Required witness: Transfer initiation and terminal result, fair healed quorum, enabled client submissions, persistent rejection/no commit, controller enabled-set and progress deadline.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

