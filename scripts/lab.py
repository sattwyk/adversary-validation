"""Laboratory metadata/acquisition tools. No execution engine or fault model."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import signal
import shutil
import subprocess
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ROOT / ".work/targets"
CAPABILITIES = {
    "message-ordering", "timers", "process-crash", "power-loss",
    "storage-ordering", "directory-durability", "shared-memory-scheduling",
    "shared-wal-index", "client-history", "multi-object-recovery",
    "concurrent-publication", "fair-progress",
}


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")


def within(base, relative):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()) or Path(relative).is_absolute():
        raise ValueError(f"path outside artifact scope: {relative}")
    return path


def checked(argv, cwd=None):
    return subprocess.check_output(argv, cwd=cwd, text=True).strip()


def git(path, *args):
    return checked(["git", "-C", str(path), *args])


def schema_check(name, value):
    from jsonschema import Draft202012Validator
    schema = read(ROOT / "schema" / name)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(value)


def manifests(selected=None):
    paths = sorted((ROOT / "benchmarks").glob("*/*/benchmark.json"))
    if selected:
        paths = [p for p in paths if read(p)["id"] == selected]
        if not paths:
            raise ValueError(f"unknown benchmark: {selected}")
    return [(p.parent, read(p)) for p in paths]


def validate_metadata():
    seen = set()
    for base, m in manifests():
        schema_check("benchmark.schema.json", m)
        assert m["id"] == base.relative_to(ROOT / "benchmarks").as_posix()
        assert m["class"] not in seen, "duplicate corpus class"
        seen.add(m["class"])
        assert set(m["required_capabilities"]) <= CAPABILITIES
        assert set(m["inputs"]) == {"workload", "environment", "oracle"}
        for name, rel in m["inputs"].items():
            assert rel == name + ".json", "search input routing must remain canonical"
            value = read(within(base, rel))
            assert value["version"].endswith("/1")
        env = read(base / "environment.json")
        assert env["required_capabilities"] == m["required_capabilities"]
        assert env["behaviors"] and all(b["semantics"] for b in env["behaviors"])
        assert env["exclusions"]
        wl = read(base / "workload.json")
        assert wl["configuration"] and wl["budget"]["max_executions_per_seed"] > 0
        assert len(wl["budget"]["seeds"]) == len(set(wl["budget"]["seeds"]))
        oracle = read(base / "oracle.json")
        assert oracle["property"] and oracle["method"] and oracle["witness_requirements"]
        for role in ("vulnerable", "fixed"):
            lock = read(base / (role + ".lock"))
            schema_check("target-lock.schema.json", lock)
            assert lock["role"] == role and lock["upstream"] == m["upstream"]
            assert (lock["commit"] is None) == (lock["tree"] is None)
            assert (lock["status"] == "unresolved") == (lock["commit"] is None)
        assert (m["targets"]["fixed"] is None) == (read(base / "fixed.lock")["commit"] is None)
        for p in m["patches"]:
            assert digest(within(base, p["path"])) == p["sha256"]
        for rel in m["reviewer_only"] + [m["native"], "README.md", "oracle.md", "assumptions.md", "expected-mechanism.md", "provenance.md"]:
            assert within(base, rel).is_file(), rel
        native = read(base / m["native"])
        assert native["argv"] and native["toolchain"] and native["coverage"]
        for dep, overlay in native.get("dependency_overlays", {}).items():
            assert digest(within(base, overlay["path"])) == overlay["sha256"]
            assert dep in native["dependency_files"]
    assert seen == set("ABCDEFGHIJ"), "initial corpus incomplete"
    for p in (ROOT / "schema").glob("*.json"):
        from jsonschema import Draft202012Validator
        Draft202012Validator.check_schema(read(p))
    for p in sorted((ROOT / "results/baselines").glob("*/result.json")):
        check_result(p)
    print("Validated ten specifications, locks, input routing and schemas; no execution evidence awarded.")


def target_dir(m, role):
    return TARGETS / m["id"] / role


def clean_target(path, lock, patches=(), overlays=None):
    assert git(path, "rev-parse", "HEAD") == lock["commit"], "wrong commit"
    assert git(path, "rev-parse", "HEAD^{tree}") == lock["tree"], "wrong tree"
    # Generated ignored build products are allowed; tracked or untracked source changes are not.
    status = git(path, "status", "--porcelain", "--untracked-files=all")
    allowed_paths = set()
    for dep, overlay in (overlays or {}).items():
        assert digest(within(path, dep)) == overlay["sha256"], "dependency overlay drift"
        allowed_paths.add(dep)
    for patch in patches:
        if lock["role"] not in patch["roles"]:
            continue
        for relative, blob in patch["postimages"].items():
            assert git(path, "hash-object", str(within(path, relative))) == blob, "patched source drift"
            allowed_paths.add(relative)
    for line in status.splitlines():
        assert line.strip().split(maxsplit=1)[1] in allowed_paths, f"dirty target: {status}"


def prepare_dependencies(base, m, dest):
    cfg = read(base / m["native"])
    for dep, overlay in cfg.get("dependency_overlays", {}).items():
        source = within(base, overlay["path"])
        assert digest(source) == overlay["sha256"]
        target = within(dest, dep)
        if target.exists():
            assert digest(target) == overlay["sha256"], "existing dependency solution differs; preserve it and use a fresh target"
        else:
            assert not git(dest, "ls-files", "--", dep), "cannot overwrite upstream dependency pin"
            shutil.copyfile(source, target)
    return cfg.get("dependency_overlays", {})


def prepare_patches(base, m, dest, role):
    for patch in m["patches"]:
        if role not in patch["roles"]:
            continue
        source = within(base, patch["path"])
        assert digest(source) == patch["sha256"]
        # Idempotent only when every patched source matches the reviewed postimage.
        if all(within(dest, p).is_file() and git(dest, "hash-object", str(within(dest, p))) == h for p, h in patch["postimages"].items()):
            continue
        assert not git(dest, "status", "--porcelain"), "refuse patching dirty source"
        git(dest, "apply", "--check", str(source))
        git(dest, "apply", str(source))


def fetch(selected):
    for base, m in manifests(selected):
        for role in ("vulnerable", "fixed"):
            lock = read(base / (role + ".lock"))
            if lock["commit"] is None:
                print(f"{m['id']} {role}: unresolved, acquisition skipped")
                continue
            dest = target_dir(m, role)
            if dest.exists():
                head = subprocess.run(["git", "-C", str(dest), "rev-parse", "--verify", "HEAD"], capture_output=True)
                if head.returncode == 0:
                    prepare_patches(base, m, dest, role)
                    overlays = prepare_dependencies(base, m, dest)
                    clean_target(dest, lock, m["patches"], overlays)
                    print(f"{m['id']} {role}: existing clean pinned checkout")
                    continue
                # Resume only a failed empty initialization belonging to this acquisition.
                assert sorted(p.name for p in dest.iterdir()) == [".git"], "unexpected partial checkout"
                assert git(dest, "remote", "get-url", "origin") == lock["upstream"]
            else:
                dest.mkdir(parents=True)
                git(dest, "init", "-q")
                git(dest, "remote", "add", "origin", lock["upstream"])
            git(dest, "fetch", "--quiet", "--depth=1", "origin", lock["commit"])
            git(dest, "checkout", "--quiet", "--detach", lock["commit"])
            prepare_patches(base, m, dest, role)
            overlays = prepare_dependencies(base, m, dest)
            clean_target(dest, lock, m["patches"], overlays)
            print(f"{m['id']} {role}: {lock['commit']}")


def verify(selected):
    registry = read(ROOT / "sources/verification.json")
    for base, m in manifests(selected):
        for role in ("vulnerable", "fixed"):
            lock = read(base / (role + ".lock"))
            if lock["commit"] is None:
                print(f"{m['id']} {role}: unresolved")
                continue
            path = target_dir(m, role)
            overlays = read(base / m["native"]).get("dependency_overlays", {})
            clean_target(path, lock, m["patches"], overlays)
            for anchor, blob in registry[m["id"]][role]["anchors"].items():
                assert git(path, "rev-parse", f"HEAD:{anchor}") == blob
            if role == "fixed":
                parents = [line[7:] for line in git(path, "cat-file", "-p", "HEAD").splitlines() if line.startswith("parent ")]
                assert parents[0] == read(base / "vulnerable.lock")["commit"]
            print(f"{m['id']} {role}: commit/tree/source anchors verified")


def export_search(selected, output):
    base, m = manifests(selected)[0]
    output = Path(output).resolve()
    if output.exists():
        raise ValueError("search package destination must be new")
    # Strict field construction: never dump the manifest or reviewer-owned metadata.
    workload, env, oracle = [read(base / m["inputs"][key]) for key in ("workload", "environment", "oracle")]
    package = {
        "schema_version": 1,
        "workload": {key: workload[key] for key in ("version", "description", "configuration", "budget")},
        "environment": {key: env[key] for key in ("version", "required_capabilities", "behaviors", "recovery", "exclusions")},
        "oracle": {key: oracle[key] for key in ("version", "property", "method", "control_requirements")},
    }
    write(output / "input.json", package)
    write(output / "seal.json", {"sha256": digest(output / "input.json"), "protocol": "search-input/1"})
    print("Exported ordinary inputs only. Blindness still requires independent authors and isolated access.")


def check_trace(trace):
    schema_check("trace.schema.json", trace)
    seen = set()
    sequence = -1
    for e in trace["events"]:
        assert e["id"] not in seen and e["sequence"] > sequence
        assert set(e["predecessors"]) <= seen, "dangling or future causal predecessor"
        if e["kind"] in {"submit", "effect", "complete", "persist"}:
            assert e["operation"], "IO event lacks operation identity"
        if e["kind"] in {"effect", "persist"}:
            assert e["resource"], "effect lacks storage/network identity"
        seen.add(e["id"])
        sequence = e["sequence"]


def check_counterexample_trace(trace):
    """Require a connected witness skeleton; causal truth still needs review."""
    check_trace(trace)
    ancestor_kinds = {}
    required = {"client-action", "submit", "effect", "observe", "violation"}
    for event in trace["events"]:
        kinds = {event["kind"]}
        for predecessor in event["predecessors"]:
            kinds.update(ancestor_kinds[predecessor])
        ancestor_kinds[event["id"]] = kinds
        if event["kind"] == "violation" and required <= kinds:
            if kinds & {"complete", "persist"} and kinds & {"fault", "compete"}:
                return
    raise AssertionError("no violation has a complete connected causal witness")


def check_result(path):
    path = Path(path).resolve()
    r = read(path)
    schema_check("result.schema.json", r)
    base, m = manifests(r["benchmark"])[0]
    lock = read(base / (r["target_revision"] + ".lock"))
    assert lock["commit"] == r["source_commit"] and lock["tree"] == r["source_hash"]
    if r["mode"] == "BASELINE":
        config_path = path.parent / "native-config.json"
        assert r["workload"] == {"version": "upstream-baseline/1", "sha256": digest(config_path)}
        assert r["build_environment"]["argv"] == read(config_path)["argv"]
        assert r["fault_model_version"] == "upstream-fixture/1"
        assert r["oracle_version"] == "upstream-assertions/1"
    else:
        assert r["workload"]["sha256"] == digest(base / "workload.json")
        assert r["workload"]["version"] == read(base / "workload.json")["version"]
        assert r["fault_model_version"] == read(base / "environment.json")["version"]
        assert r["oracle_version"] == read(base / "oracle.json")["version"]
    assert r["replay_result"]["matching"] <= r["replay_result"]["attempts"]
    assert set(r["missing_capabilities"]) <= set(m["required_capabilities"])
    refs = r["artifacts"] + [r[key] for key in ("trace", "witness") if r[key]]
    refs += [r[key]["artifact"] for key in ("review", "historical_mechanism_match", "replay_result") if r[key] and r[key]["artifact"]]
    for ref in refs:
        assert digest(within(path.parent, ref["path"])) == ref["sha256"], "artifact hash mismatch"
    labels = set(r["evidence"])
    for label, outcome in {
        "UNSUPPORTED": "MODEL CANNOT REPRESENT REQUIRED BEHAVIOR",
        "INCONCLUSIVE": "INCONCLUSIVE",
        "HARNESS-FAILURE": "HARNESS FAILURE",
    }.items():
        if label in labels:
            assert r["outcome"] == outcome, "evidence/outcome contradiction"
    execution_labels = {"NATIVE-REPRODUCED", "SCRIPTED-REPRODUCED", "SEARCH-REDISCOVERED", "BLIND-REDISCOVERED", "NATIVE-CONFIRMED", "FIXED-CONTROL-PASSED", "BUILD-VERIFIED"}
    if labels & execution_labels:
        assert r["review"] is not None, "execution evidence requires explicit review"
    if r["outcome"] == "COUNTEREXAMPLE FOUND":
        assert r["oracle_reached"] and not r["missing_capabilities"]
        trace = read(within(path.parent, r["trace"]["path"]))
        check_counterexample_trace(trace)
        assert r["review"], "counterexample requires independent causal/evidence review"
        assert r["invariant_violated"] == read(base / "oracle.json")["property"]
    else:
        assert r["counterexample_identifier"] is None and r["invariant_violated"] is None
    if r["outcome"] == "NO FAILURE FOUND":
        assert r["mode"] != "BASELINE", "baseline cannot discharge the benchmark oracle"
        if "timers" in m["required_capabilities"]:
            assert r["fairness_validated"], "no-failure campaign lacks fairness qualification"
    if labels & {"SEARCH-REDISCOVERED", "BLIND-REDISCOVERED"}:
        assert r["mode"] in {"REDISCOVERY", "BLIND REDISCOVERY"} and r["search_strategy"]
        assert r["outcome"] == "COUNTEREXAMPLE FOUND"
        assert "sealed-input" in r["review"]["attestations"]
    if "BLIND-REDISCOVERED" in labels:
        assert r["mode"] == "BLIND REDISCOVERY"
        assert "independent-blind-authorship" in r["review"]["attestations"]
    if "SCRIPTED-REPRODUCED" in labels:
        assert r["mode"] == "REPRODUCTION" and r["outcome"] == "COUNTEREXAMPLE FOUND"
    if "NATIVE-REPRODUCED" in labels:
        assert r["mode"] != "BASELINE" and r["outcome"] == "COUNTEREXAMPLE FOUND"
    if "NATIVE-CONFIRMED" in labels:
        assert r["native_confirmation_status"] == "CONFIRMED"
    if "FIXED-CONTROL-PASSED" in labels:
        assert r["target_revision"] == "fixed" and r["outcome"] == "NO FAILURE FOUND"
        assert "matched-vulnerable-control" in r["review"]["attestations"]
    if r["historical_mechanism_match"]["status"] == "MATCH":
        assert r["historical_mechanism_match"]["reviewer"] and r["historical_mechanism_match"]["artifact"]
    if r["replay_result"]["status"] == "MATCHED":
        assert r["replay_result"]["attempts"] > 0 and r["replay_result"]["artifact"]
        assert r["replay_result"]["matching"] == r["replay_result"]["attempts"]
    print(f"Evidence structure valid: {r['run_id']}; substantive review remains required.")


def native(selected, role):
    base, m = manifests(selected)[0]
    cfg = read(base / m["native"])
    lock = read(base / (role + ".lock"))
    if lock["commit"] is None:
        raise ValueError("unresolved target")
    if cfg["kind"] == "manual" or cfg["dependency_status"] == "needs-lock-preparation":
        raise ValueError("baseline unprepared: follow native/README.md; no test was executed")
    if cfg["availability"] == "fixed-only" and role != "fixed":
        raise ValueError("test absent on vulnerable revision; test-only preparation required")
    target = target_dir(m, role)
    clean_target(target, lock, m["patches"], cfg.get("dependency_overlays", {}))
    for dep in cfg["dependency_files"]:
        assert (target / dep).is_file(), f"missing dependency pin: {dep}"
    if cfg["kind"] == "go":
        tool = checked(["go", "version"])
        assert tool.split()[2].split("-X:")[0] == cfg["toolchain"], "wrong Go toolchain"
    elif cfg["kind"] == "cargo":
        tool = checked(["rustc", "+" + cfg["toolchain"], "--version"])
    else:
        raise ValueError("unsupported baseline command kind")
    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "-" + uuid.uuid4().hex[:8]
    output = ROOT / "results/local" / run_id
    output.mkdir(parents=True)
    shutil.copyfile(base / m["native"], output / "native-config.json")
    env = dict(os.environ)
    env["GOTOOLCHAIN"] = "local"
    if cfg["kind"] == "cargo":
        env["CARGO_TARGET_DIR"] = str(ROOT / ".work/build" / m["id"] / role)
    build_env = {
        "platform": platform.platform(), "machine": platform.machine(),
        "python": platform.python_version(), "toolchain": tool,
        "git": checked(["git", "--version"]), "argv": cfg["argv"],
        "source_patches": [p for p in m["patches"] if role in p["roles"]],
        "dependency_hashes": {p: digest(target / p) for p in cfg["dependency_files"]},
        "compiler_flags": {k: env.get(k, "") for k in ("RUSTFLAGS", "GOFLAGS", "GOEXPERIMENT", "CGO_ENABLED", "CC", "CFLAGS")},
        "storage_qualification": "not performed; baseline only",
    }
    write(output / "environment.json", build_env)
    start = time.monotonic()
    with (output / "stdout.log").open("w") as log:
        proc = subprocess.Popen(cfg["argv"], cwd=target, env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code = proc.wait(timeout=cfg["timeout_seconds"])
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait()
            code = 124
    log_text = (output / "stdout.log").read_text()
    if cfg["kind"] == "cargo":
        executed = sum(int(n) for n in re.findall(r"(?:^|\n)running (\d+) tests?", log_text))
    else:
        executed = len(re.findall(r"^=== RUN\s+", log_text, re.MULTILINE))
    passed = code == 0 and executed > 0
    infrastructure_failure = executed == 0 or code == 124
    outcome = "HARNESS FAILURE" if infrastructure_failure else "INCONCLUSIVE"
    record = {
        "schema_version": 1, "run_id": run_id, "benchmark": m["id"],
        "target_revision": role, "source_commit": lock["commit"], "source_hash": lock["tree"],
        "mode": "BASELINE", "outcome": outcome,
        "evidence": ["HARNESS-FAILURE" if infrastructure_failure else "INCONCLUSIVE"],
        "build_environment": build_env,
        "workload": {"version": "upstream-baseline/1", "sha256": digest(base / m["native"])},
        "fault_model_version": "upstream-fixture/1",
        "oracle_version": "upstream-assertions/1",
        "search_strategy": None, "search_budget": {"baseline_timeout_seconds": cfg["timeout_seconds"]},
        "random_seed": None, "number_of_executions": executed,
        "time_to_first_failure": None, "events_to_first_failure": None,
        "counterexample_identifier": None,
        "replay_result": {"status": "NOT-RUN", "attempts": 0, "matching": 0, "artifact": None},
        "invariant_violated": None,
        "historical_mechanism_match": {"status": "NOT-REVIEWED", "reviewer": None, "artifact": None},
        "native_confirmation_status": "NOT-RUN", "model_limitations": [cfg["coverage"]],
        "missing_capabilities": [], "oracle_reached": False, "fairness_validated": False,
        "coverage_validated": False, "completed_budget": False,
        "artifacts": [{"path": name, "sha256": digest(output / name)} for name in ("stdout.log", "environment.json", "native-config.json")],
        "trace": None, "witness": None, "review": None,
        "native_baseline_status": "PASSED" if passed else "ZERO-TESTS" if code == 0 else "FAILED",
        "notes": f"Exit {code}; wall {time.monotonic()-start:.3f}s. Executed upstream fixtures only. No automatic evidence promotion.",
    }
    write(output / "result.json", record)
    check_result(output / "result.json")
    print(f"Baseline {'passed' if passed else 'failed'}: {output}")
    if not passed:
        raise ValueError("baseline failed; retained for review with raw evidence")


def matrix():
    groups = {
        "network": {"message-ordering"}, "storage": {"storage-ordering", "directory-durability", "shared-wal-index", "multi-object-recovery"},
        "time": {"timers"}, "crash": {"process-crash", "power-loss"},
        "concurrency": {"shared-memory-scheduling", "concurrent-publication"}, "history": {"client-history"},
    }
    lines = ["# Capability matrix", "", "Source-justified requirements, not implemented capabilities or passing results. A dash is outside this benchmark envelope, not a project-wide absence.", "", "| Benchmark | network | storage | time | crash | concurrency | history |", "|---|---|---|---|---|---|---|"]
    for _, m in manifests():
        caps = set(m["required_capabilities"])
        marks = ["✓" if caps & required else "—" for required in groups.values()]
        lines.append("| " + m["id"] + " | " + " | ".join(marks) + " |")
    lines += ["", "A's native file cursor is a concurrency requirement, not a storage-fault model. C includes elections/messages because the documented crash mechanism requires a later quorum. G does not need crash injection to expose its race. H requires concurrency plus network/election; process crashes are optional and excluded from this initial envelope. J's upstream crash clone is a model, not native power-loss qualification.", "", "Required capability details are in each environment.json and docs/MODEL_REQUIREMENTS.md.", ""]
    return "\n".join(lines)


def main(action=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark")
    parser.add_argument("--revision", choices=["vulnerable", "fixed"], default="fixed")
    parser.add_argument("--output")
    parser.add_argument("--result")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if action == "validate":
        validate_metadata()
    elif action == "fetch":
        fetch(args.benchmark)
    elif action == "verify":
        verify(args.benchmark)
    elif action == "export":
        if not args.benchmark or not args.output:
            parser.error("--benchmark and --output required")
        export_search(args.benchmark, args.output)
    elif action == "native":
        if not args.benchmark:
            parser.error("--benchmark required")
        native(args.benchmark, args.revision)
    elif action == "result":
        if not args.result:
            parser.error("--result required")
        check_result(args.result)
    elif action == "report":
        path = ROOT / "docs/CAPABILITY_MATRIX.md"
        if args.check:
            assert path.read_text() == matrix(), "matrix is stale"
            print("Capability matrix matches source-backed manifests.")
        else:
            print(matrix(), end="")
    else:
        parser.error("use a named entrypoint")


def entry(action):
    try:
        main(action)
    except (AssertionError, ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Laboratory error: {error}", file=sys.stderr)
        raise SystemExit(1)
