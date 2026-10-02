# adversary-validation

A laboratory for judging a future deterministic-testing implementation. This repository implements acquisition, metadata validation, native baseline capture and search-input packaging. It implements no Adversary runtime, scheduler, simulator, SDK or exploration algorithm.

Ten historical specifications span shared cursors, replication, crash recovery, snapshots, stale reads, namespace durability, WAL concurrency, distributed safety, leadership transfer and production storage recovery. Each has an independent oracle and an ordinary workload. Historical mechanisms are reviewer-only. An unsupported benchmark stays in the denominator.

Start with [the validation plan](docs/VALIDATION_PLAN.md), [success criteria](docs/SUCCESS_CRITERIA.md), [protocol](docs/BENCHMARK_PROTOCOL.md) and [capability matrix](docs/CAPABILITY_MATRIX.md). Status is recorded in manifests; source verification does not imply reproduction.

## Local commands

Python 3.14.5 is the reference metadata environment; Python 3.11+ supports the tools. Git is required for acquisition. Enabled native baselines additionally require Go 1.26.4 or Rust 1.97.1 as declared in each native/baseline.json; they are not installed by acquisition.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.lock
.venv/bin/python scripts/validate-metadata.py
.venv/bin/python scripts/fetch-targets.py --benchmark raft-log/shared-cursor
.venv/bin/python scripts/verify-pins.py --benchmark raft-log/shared-cursor
.venv/bin/python controls/run.py
.venv/bin/python scripts/fetch-targets.py --benchmark hashicorp-raft/transfer-flag
.venv/bin/python scripts/verify-pins.py --benchmark hashicorp-raft/transfer-flag
.venv/bin/python scripts/native-baseline.py --benchmark hashicorp-raft/transfer-flag --revision fixed
.venv/bin/python scripts/export-search-input.py --benchmark openraft/divergent-log-liveness --output .work/search-input
.venv/bin/python scripts/report.py --check
```

Acquisition creates detached pinned checkouts under `.work/targets/`; it allows only declared, hashed test-only patches and dependency overlays and refuses other source changes. No upstream algorithms are modified. Baselines are upstream tests, not search campaigns; historically constructed state remains reproduction-only input. Missing tests, tools or locks are errors, never passing controls. Native result records remain INCONCLUSIVE about historical bugs until reviewed evidence establishes more.

JSON manifests are used instead of TOML so the same objects are checked directly by JSON Schema. `sources/` contains small verification records, not upstream repositories. `.inputs/adversary-research` is ignored and is unnecessary to use the suite. Consult [provenance](docs/PROVENANCE.md) for immutable research references and limitations.

No project-wide license is assigned here; do not infer relicensing of upstream material. See [third-party provenance](THIRD_PARTY.md).
