# Independent oracle

A successfully saved-and-synced WAL entry survives the declared ordinary power loss and remains recoverable under its segment identity; namespace publication cannot invalidate that durability acknowledgement.

Compare recoverable saved entries and hard state with successful Save fences. Allow valid unacknowledged suffixes, reject missing acknowledged prefixes or unexpected recovery errors. Correlated node failure is unnecessary for this local WAL property.

Required witness: File/inode identity through temp creation and rename, writes, file sync fences, namespace/root sync, Save success, legal crash image and exact recovery enumeration/decoded entries.

Use oracle.json as the sealed versioned definition. Record implementation/hash of any future checker separately. These documents define the checker but do not claim an executable full-project checker exists. Safety applies to every admissible prefix; liveness requires the healthy fairness phase. Invalid/missing observations, unexpected recovery errors and checker resource exhaustion are never accepted as a recovered old state.

