# Counterexample requirements

A valid failure bundle reconstructs application/client action → submitted operation → environmental effect → completion/persistence order → fault or competing operation → observable incorrect result → violated invariant.

Retain lossless events with event ID, sequence, actor/incarnation/task, request/logical-client/resource identity, input/output bytes or content-addressed blobs, enabled alternatives, chosen decision, logical/native clock and causal predecessor IDs. File identity must survive rename/handle aliases; incarnations must change on restart. Replay verifies enabling conditions and operation/result digests, and rejects unexpected operations as divergence.

The bundle includes initial state, target/build/lock/patch identities, workload, fault-model/oracle/policy versions and hashes, explicit decisions, client history/state observations, final recovery image where relevant, checker witness, limitations and replay measurements. Event records follow schema/trace.schema.json. Observation payload schemas and property-specific witnesses are defined by each oracle.

A seed, assertion, stack trace or final corrupted value alone is insufficient. A generic panic must be attributed to an invariant and legitimate target path; recorder errors are harness failures. Histories have unique invocation IDs with one invocation and at most one terminal result, preserve session and real-time order, and allow unknown operations to commit where legal.

Do not infer causality from adjacent timestamps. Attach dependencies and independent observations: client success to applied command, command to log bytes, byte effects to durability fences, recovered state to durable image. A post-hoc mechanism reviewer signs its assessment; schema validation cannot prove the assessment true.

Fixed controls rerun the workload/envelope/policy and separately challenge the original causal condition. A removed enabling condition can establish that this counterexample is not admitted; it cannot prove the fixed revision correct.

