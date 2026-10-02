# Pebble manifest record/crash recovery ambiguity

Corpus class J. SOURCE-IDENTIFIED; source review only at specification creation. No local historical reproduction is implied. See benchmark.json for current status and native observations for separately scoped executed baselines.

The fix distinguishes an incomplete manifest record envelope after interrupted append from malformed content inside a complete envelope. Previously recovery could reject an ordinary incomplete record or accept malformed complete content. This late-stage benchmark targets legal interrupted manifest append; malformed content is a separate detection control.

Vulnerable: `57c482fb4e96fb89ca76cbc582354240a54f2f8c`. Fix: `c532754949aacd080d6f774b6d244dbcb32ac23c`.

The ordinary workload is in workload.json; oracle.md and assumptions.md define the independent property/envelope. expected-mechanism.md is reviewer-only. Never hand this README or upstream regression commands to search.

Acquire: `python scripts/fetch-targets.py --benchmark storage-capstone/pebble-manifest-eof`.
Verify: `python scripts/verify-pins.py --benchmark storage-capstone/pebble-manifest-eof`.
Native baseline: `python scripts/native-baseline.py --benchmark storage-capstone/pebble-manifest-eof --revision fixed` (manual/unprepared commands are refused).

Vulnerable expectation: counterexample expected under an adequate model and budget. Fixed expectation: same historical causal violation not admitted; this is not proof of correctness. Budget exhaustion does not invalidate documented history.

Remaining preparation:

- Pin toolchain, upstream go.mod/go.sum and build flags; inspect fixture compatibility on parent.
- Prepare native multi-object crash/fault qualification independently of upstream MemFS.
- Keep this benchmark late-stage; do not reduce it to one file or a record parser toy.

