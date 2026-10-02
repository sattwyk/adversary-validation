"""Executable infrastructure controls; not historical target evidence."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lab import ROOT, check_counterexample_trace, check_result, check_trace, digest, export_search, manifests, read, schema_check, write


def sequential_register(history):
    """A deliberately narrow oracle: complete, nonoverlapping single-register actions."""
    value = 0
    for action in history:
        if action["op"] == "write":
            value = action["value"]
        elif action["op"] == "read":
            if action["value"] != value:
                return False
        else:
            raise ValueError("outside sequential fixture contract")
    return True


def unsupported_fixture():
    base, m = manifests("sqlite/wal-reset")[0]
    lock = read(base / "vulnerable.lock")
    return {
        "schema_version": 1, "run_id": "CONTROL-FIXTURE-NOT-A-TARGET-RUN", "benchmark": m["id"],
        "target_revision": "vulnerable", "source_commit": lock["commit"], "source_hash": lock["tree"],
        "mode": "REDISCOVERY", "outcome": "MODEL CANNOT REPRESENT REQUIRED BEHAVIOR", "evidence": ["UNSUPPORTED"],
        "build_environment": {"fixture": "metadata control only; no target execution"},
        "workload": {"version": "workload/1", "sha256": digest(base / "workload.json")},
        "fault_model_version": "envelope/1", "oracle_version": "oracle/1", "search_strategy": None,
        "search_budget": {"fixture": 0}, "random_seed": None, "number_of_executions": 0,
        "time_to_first_failure": None, "events_to_first_failure": None, "counterexample_identifier": None,
        "replay_result": {"status": "NOT-RUN", "attempts": 0, "matching": 0, "artifact": None},
        "invariant_violated": None, "historical_mechanism_match": {"status": "NOT-REVIEWED", "reviewer": None, "artifact": None},
        "native_confirmation_status": "NOT-RUN", "model_limitations": ["no shared WAL-index"],
        "missing_capabilities": ["shared-wal-index"], "oracle_reached": False, "fairness_validated": False,
        "coverage_validated": False, "completed_budget": False, "artifacts": [], "trace": None,
        "witness": None, "review": None, "native_baseline_status": "NOT-RUN", "notes": "Control fixture only.",
    }


class Controls(unittest.TestCase):
    def test_correct_toy_and_stale_read(self):
        register = 0
        history = []
        for value in (7, 11, 42):
            register = value
            history += [{"op": "write", "value": value}, {"op": "read", "value": register}]
        self.assertTrue(sequential_register(history))
        planted = copy.deepcopy(history)
        planted[-1]["value"] = 11
        self.assertFalse(sequential_register(planted))

    def test_unsupported_cannot_be_no_failure(self):
        with tempfile.TemporaryDirectory(prefix="adversary-metadata-control-") as temp:
            path = Path(temp) / "fixture.json"
            fixture = unsupported_fixture()
            write(path, fixture)
            check_result(path)
            fixture["outcome"] = "NO FAILURE FOUND"
            write(path, fixture)
            with self.assertRaises(Exception):
                check_result(path)

    def test_seed_only_counterexample_rejected(self):
        fixture = unsupported_fixture()
        fixture.update(outcome="COUNTEREXAMPLE FOUND", random_seed=7, number_of_executions=1, counterexample_identifier="seed-7")
        with self.assertRaises(Exception):
            schema_check("result.schema.json", fixture)

    def test_zero_execution_pass_rejected(self):
        fixture = unsupported_fixture()
        fixture.update(outcome="NO FAILURE FOUND", oracle_reached=True, coverage_validated=True, completed_budget=True, missing_capabilities=[])
        with self.assertRaises(Exception):
            schema_check("result.schema.json", fixture)

    def test_causal_dangling_reference_rejected(self):
        event = {"id": "e1", "sequence": 0, "kind": "client-action", "actor": "client", "incarnation": 1,
                 "task": None, "operation": None, "resource": None, "predecessors": [], "payload": {}}
        trace = {"schema_version": 1, "events": [event]}
        check_trace(trace)
        event["predecessors"] = ["future-event"]
        with self.assertRaises(AssertionError):
            check_trace(trace)

    def test_search_label_not_awarded_by_fixture(self):
        fixture = unsupported_fixture()
        fixture["evidence"] += ["SEARCH-REDISCOVERED"]
        with tempfile.TemporaryDirectory(prefix="adversary-label-control-") as temp:
            path = Path(temp) / "fixture.json"
            write(path, fixture)
            with self.assertRaises(AssertionError):
                check_result(path)

    def test_disconnected_counterexample_rejected(self):
        # A trace-grammar fixture only; not evidence of any target failure.
        events = []
        for sequence, kind in enumerate(("client-action", "submit", "effect", "complete", "compete", "observe", "violation")):
            events.append({"id": f"e{sequence}", "sequence": sequence, "kind": kind,
                           "actor": "fixture", "incarnation": 1, "task": "fixture-task",
                           "operation": "fixture-operation", "resource": "fixture-resource",
                           "predecessors": [], "payload": {"fixture_only": True}})
        trace = {"schema_version": 1, "events": events}
        with self.assertRaises(AssertionError):
            check_counterexample_trace(trace)
        for sequence, event in enumerate(events[1:], 1):
            event["predecessors"] = [f"e{sequence - 1}"]
        check_counterexample_trace(trace)

    def test_search_export_contains_only_allowed_inputs(self):
        with tempfile.TemporaryDirectory(prefix="adversary-package-control-") as temp:
            dest = Path(temp) / "package"
            export_search("raft-log/shared-cursor", dest)
            package = read(dest / "input.json")
            self.assertEqual(set(package), {"schema_version", "workload", "environment", "oracle"})
            self.assertNotIn("witness_requirements", package["oracle"])
            self.assertEqual(sorted(p.name for p in dest.iterdir()), ["input.json", "seal.json"])
            serialized = json.dumps(package)
            for prohibited in ("707a9a2", "expected-mechanism", "pread", "native/baseline", "Shuttle"):
                self.assertNotIn(prohibited, serialized)
            self.assertEqual(read(dest / "seal.json")["sha256"], digest(dest / "input.json"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
