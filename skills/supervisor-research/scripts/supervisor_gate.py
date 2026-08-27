#!/usr/bin/env python3
"""Validate a compact doctoral-research supervision state record.

The checker does not judge scientific truth. It detects missing evidence fields so
an agent cannot call a stage complete while only a plan or narrative exists.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


STAGES = ("brief", "landscape", "idea", "experiment-plan", "results", "delivery")
LEVELS = (
    "炼气",
    "筑基",
    "结丹",
    "元婴",
    "化神",
    "concept",
    "baseline",
    "mechanism",
    "audited-system",
    "platform",
)


def load_state(path: str) -> dict:
    if path == "-":
        raw = sys.stdin.buffer.read()
        data = json.loads(raw.decode("utf-8-sig"))
    else:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("state root must be a JSON object")
    return data


def present(value: object) -> bool:
    if value is None or value is False:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def require(state: dict, dotted: str, failures: list[str]) -> None:
    value: object = state
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            failures.append(dotted)
            return
        value = value[part]
    if not present(value):
        failures.append(dotted)


def validate(state: dict, stage: str) -> list[str]:
    failures: list[str] = []
    order = STAGES.index(stage)

    for field in ("project", "significance.problem", "significance.application", "significance.measurable_value"):
        require(state, field, failures)

    if order >= STAGES.index("landscape"):
        for field in ("landscape.research_questions", "landscape.verified_sources", "landscape.nearest_prior_art"):
            require(state, field, failures)
        verified_sources = state.get("landscape", {}).get("verified_sources")
        if not isinstance(verified_sources, int) or isinstance(verified_sources, bool) or verified_sources < 1:
            failures.append("landscape.verified_sources (must be a positive integer)")

    if order >= STAGES.index("idea"):
        for field in ("innovation.claim", "innovation.difference_axes", "innovation.falsifier", "innovation.cheap_kill_test"):
            require(state, field, failures)

    if order >= STAGES.index("experiment-plan"):
        for field in (
            "experiment.primary_metric",
            "experiment.practical_threshold",
            "experiment.baselines",
            "experiment.fairness_contract",
            "experiment.ablations",
            "experiment.stop_rule",
        ):
            require(state, field, failures)

    if order >= STAGES.index("results"):
        if state.get("experiment", {}).get("executed") is not True:
            failures.append("experiment.executed (must be true)")
        for field in ("experiment.raw_artifacts", "experiment.result_table", "experiment.commands_or_logs"):
            require(state, field, failures)

    if order >= STAGES.index("delivery"):
        for field in ("audit.decision", "audit.negative_results_recorded", "audit.reproducible", "audit.evidence_level"):
            require(state, field, failures)
        level = state.get("audit", {}).get("evidence_level")
        if present(level) and level not in LEVELS:
            failures.append("audit.evidence_level (unknown level)")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check required evidence for a supervised research stage.")
    parser.add_argument("state", help="JSON state path, or - for stdin")
    parser.add_argument("--stage", choices=STAGES, help="Stage to validate; defaults to state.stage")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output")
    args = parser.parse_args()

    try:
        state = load_state(args.state)
        stage = args.stage or state.get("stage")
        if stage not in STAGES:
            raise ValueError(f"stage must be one of: {', '.join(STAGES)}")
        failures = validate(state, stage)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"supervisor-gate: error: {exc}", file=sys.stderr)
        return 2

    result = {"status": "PASS" if not failures else "FAIL", "stage": stage, "missing_or_invalid": failures}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"supervisor-gate: {result['status']} stage={stage}")
        for failure in failures:
            print(f"- {failure}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
