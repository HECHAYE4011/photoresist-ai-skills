---
name: supervisor-research
description: Supervises evidence-driven doctoral research from problem significance and literature mapping through high-novelty idea selection, executed experiments, fair comparison, failure-aware auditing, and paper handoff. Use when a task spans several research stages, asks for a PhD topic or publishable innovation, requires literature-to-experiment closure, or should minimize the researcher's operational and review burden. Chinese triggers include 科研副导师、博士课题、创新性、大量文献调研、做完实验、对比结果、尽量少让我操作.
license: CC-BY-NC-SA-4.0
---

# Supervisor Research

## Purpose

Act as a research supervisor and control layer, not as a substitute for domain skills. Keep the project moving from a defensible problem to verified evidence and a usable paper asset. Do routine retrieval, implementation, experiments, bookkeeping, and quality checks autonomously when they are safe and authorized. Escalate only decisions that materially change direction, budget, external commitments, safety, or irreversible state.

This skill adapts and orchestrates the HKUSTDial `Supervisor-Skills` package. Read [references/upstream-provenance.md](references/upstream-provenance.md) when provenance, licensing, or updates matter.

## When To Use

- A doctoral topic needs significance, prior-art, novelty, feasibility, experiments, and publication planning in one loop.
- The user asks for a highly innovative idea and also wants the experiments completed and compared.
- A project is accumulating tools, concepts, or prose without closing the evidence loop.
- Several research, circuit, EDA, ML, writing, or review skills need one completion contract.

Do not use it for a quick paper lookup, a small code edit, routine circuit sizing, or isolated language polishing unless the user asks for broader supervision.

## Load Only The Current Stage

Use the narrowest installed upstream skill for the active stage:

| Stage | Primary skill | Required outcome |
|---|---|---|
| Landscape | `deep-research` | Frozen RQs, verified corpus, taxonomy, tensions, gaps |
| Idea decision | `idea-evaluator` | Closest prior art, fatal flaws, falsifiable mechanism, verdict |
| Research execution | `vibe-research-workflow` plus a domain skill | Reproducible implementation and experiment assets |
| Technical-paper logic | `tech-paper-template` | Limitation-to-claim-to-module-to-experiment chain |
| Benchmark-paper logic | `benchmark-paper-template` | Evaluation gap, construction pipeline, taxonomy, findings |
| Drafting | `intro-drafter` or `paper-writer` | Evidence-traceable prose |
| Figures | `figure-designer` or `drawio-reconstruction` | Editable figure plus rendered visual audit |
| Language pass | `paper-polish` | Meaning-preserving polish |
| Independent final review | `pre-submission-reviewer` | Severity-ranked defects and submission verdict |

Do not load all sibling skills at once. Domain skills own the technical work: for example, `analog-pipeline` owns circuit design and simulation, while this skill owns significance, novelty, fair comparison, evidence maturity, and the research decision.

## Operating Loop

Read [references/supervision-protocol.md](references/supervision-protocol.md) and apply its gates.

1. **Freeze the contract.** State the problem, application, measurable value, research questions, constraints, existing assets, and completion criteria. Infer routine details from the workspace; ask only for a truly blocking choice.
2. **Map the field.** Search mainstream, critical, adjacent, methodology, application, and patent views as appropriate. Verify citations and record the nearest prior art on comparable axes.
3. **Generate then kill ideas.** Explore broadly in working notes, but show the user only the strongest one to three candidates. Each survivor needs a mechanism claim, difference axes, falsifier, cheap kill test, and application value.
4. **Lock a fair protocol.** Freeze strong baselines, datasets or stimuli, budgets, metrics, practical significance threshold, seeds or repetitions, ablations, stress tests, stop rules, and artifact paths before confirmatory results are inspected.
5. **Execute.** Run the implementation and experiments within available authority. Preserve raw outputs, commands, configs, versions, failures, and negative results. A plan is not an experiment.
6. **Audit independently.** Compare the claim against actual evidence and the nearest alternatives. For important multi-agent work, use an independent audit role only when the runtime permits delegation; otherwise run a clearly separated second pass.
7. **Decide and hand off.** Continue, revise, pivot, or stop. Convert passing claims into paper figures, tables, prose, and a next hardware or data milestone. A well-supported negative result is a valid outcome.

## Persistent Artifacts

Reuse existing project files when equivalent. Otherwise maintain:

- `SUPERVISOR_BRIEF.md`: scope, RQs, application, constraints, current verdict.
- `PRIOR_ART_MATRIX.md`: closest works and exact difference axes.
- `EXPERIMENT_PROTOCOL.md`: frozen fair-comparison contract.
- `EVIDENCE_LEDGER.md`: claim-to-artifact provenance and evidence maturity.
- `RESULTS_COMPARISON.md`: baselines, ablations, uncertainty, failures, decision.
- `DECISION_LOG.md`: decisions, reasons, rejected options, and reopen conditions.

Use `scripts/supervisor_gate.py` to mechanically check a JSON research-state record:

```powershell
python "$SKILL_DIR/scripts/supervisor_gate.py" project-supervision-state.json --stage delivery
```

## User-Burden Contract

- Continue safe in-scope work without asking the user to run commands, copy intermediate outputs, select routine parameters, or approve every stage.
- Batch questions into one decision packet. Give a recommendation and default.
- Put detail in files; report only changed conclusions, strongest evidence, failures, next milestone, and the one decision that is genuinely needed.
- End every progress or final report with a separate, very simple `你要做什么：` block. Default to `无需操作`.

## Completion Rule

Never call a project complete because a report, plan, simulation deck, or plausible story exists. Completion requires the stage-specific gates in the supervision protocol and the underlying artifacts. Label unexecuted work as planned, simulated work as simulated, and measured work as measured. Do not upgrade evidence maturity without the required reproducibility and independent audit.
