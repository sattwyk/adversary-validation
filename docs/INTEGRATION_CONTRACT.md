# Future engine contract, version 1

No engine dependency is present. A future adapter supplies these operations through CLI, JSONL RPC or another documented binding:

| Operation | Required input and output |
|---|---|
| prepare | Opaque acquired target + toolchain/lock/patch manifest → source/build hashes, audited preservation record, artifact identity. |
| capabilities | Versioned capability declarations + unsupported reasons → complete match/missing set before running. |
| run | Prepared target + sealed ordinary input package + frozen generic policy + budget → execution histories, explicit decisions, losses/coverage, standard result candidate. |
| reproduce | Separately labeled reviewer-owned constructed schedule → trace and invariant witness. |
| replay | Complete failure bundle and identical artifacts → consumed decisions, replay trace hashes, divergence or matching violation. |
| observe | Lossless histories/state/effect events using stable actor/incarnation/request/object identities → validated evidence. |

The adapter owns environmental control. The target owns consensus, retry, state-machine, storage codecs, batching, snapshots and recovery. The laboratory owns workload/oracle definitions and result review. No SDK, runtime or environment simulator is supplied here.

Capability negotiation is exact set inclusion over required capabilities. A claim such as “storage supported” does not satisfy directory-durability or shared-wal-index. Report missing semantics, not just missing API names. Capabilities are assertions requiring conformance evidence, not self-certifying flags.

Search cannot consume manifest/provenance/expected mechanism or known regression scripts. The exported package is the only ordinary input; target artifact preparation is coordinator-owned. All result fields may be null only where the schema permits it; explain unperformed operations and limitations. Engine-specific details go into versioned extensions, never replace the independent invariant.

Adapter failures, unhandled ambient effects, trace loss, unmatched oracle inputs and resource exhaustion are HARNESS FAILURE or INCONCLUSIVE. An engine may return unsupported without executing. It must never silently downgrade concurrency, crash or file identity semantics.

