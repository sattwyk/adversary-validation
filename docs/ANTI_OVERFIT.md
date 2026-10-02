# Anti-overfitting protocol

Search may receive workload, configuration, declared fault envelope, correctness invariant and budget. It may not receive historical causal sequence, exact fault/crash location, minimal schedule, fix implementation or constructed divergent log images. Those belong to reproduction or post-hoc review.

The canonical allowed package is exported by `scripts/export-search-input.py` using an explicit allowlist from `workload.json`, `environment.json` and `oracle.json`. It contains no README, benchmark identity, source pair, upstream regression test, expected-mechanism file or native command. The coordinator separately supplies a prepared opaque target. The engine inevitably executes the target implementation; blindness concerns authorship and policy information, not pretending the target has no source.

The coordinator must build/import the artifact outside the search worker's filesystem and mount only the target and sealed package. An exporter alone is not an access-control boundary. This repository cannot grant BLIND-REDISCOVERED: its author read fixes. Require independent authors/reviewers, package hashes, access attestations, timestamped preregistration and policy digest before revealing mechanisms.

Upstream regressions that fake term/index states, target a precise failpoint, or replay a captured tape are REPRODUCTION. Label them even when an upstream random scheduler varies details. Broad random search using hand-placed historically informed checkpoints may earn REDISCOVERY with disclosure, never blindness. Site-specific weighting after reading the fix invalidates search independence.

Workloads may exercise normal snapshots, rotation, transfers, retry and multi-reader APIs. Publish why each parameter is operationally ordinary. Freeze workload/configuration, whole-class fault eligibility and budget before a campaign. Treat threshold selection informed by the bug as author knowledge and disclose it. Keep unsuccessful input revisions and all campaigns; tuning on the vulnerable revision followed by reporting only the best seed is overfitting.

Fixed sources/diffs, mechanism docs and rehearsal tapes are reviewer-only. Redact benchmark IDs from blind packages. Generic policies may use pending operation types across the whole target but must not pick the one known failing line. Test corpus splits at project/mechanism level, not merely seeds. Report any human hint or target-specific heuristic.

Per-benchmark causal witness requirements are also reviewer-only: they can mention the historical mechanism. The exporter includes the independent oracle property/method and checker controls, and excludes witness_requirements. Generic trace grammar remains available through the integration contract.

Historical replay on changed fixed code is semantic: if the old event is gone, report NOT-ADMITTED with enabling-condition evidence. Do not consume an incompatible tape and count a crash as a passed control.
