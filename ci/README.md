# CI contract

.github/workflows/validation.yml runs metadata schemas, controls, matrix freshness, pinned source acquisition/verification and buildable native baseline pieces. It does not run Adversary or claim search coverage. Vulnerable native regression failures are retained for reviewed local comparison; stochastic failure is not made a required green CI outcome.

Actions are pinned by SHA, Python dependencies/toolchain and Go/Rust toolchains are pinned. The Ubuntu hosted runner image can change: baseline environment artifacts record the actual environment, and hosted CI is not filesystem/power-loss qualification or bitwise host reproducibility. Source/test/dependency hashes remain immutable.

Local equivalent: create the documented venv, run validate-metadata.py, controls/run.py, report.py --check, fetch/verify a selected target, then native-baseline.py. Missing dependencies or zero matched tests fail the job. Raw artifacts upload even on failure; result evidence is never promoted by CI.
