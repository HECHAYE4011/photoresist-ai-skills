# Research Supervision Protocol

## 1. Research contract gate

Pass only when all are explicit:

- problem and affected stakeholder;
- target application and why present solutions are insufficient;
- measurable scientific or engineering value;
- two or three answerable research questions;
- constraints, existing assets, excluded scope, and completion criteria.

If the application cannot be translated into a measurable requirement, lower its priority rather than decorating the story.

## 2. Landscape and novelty gate

Use primary papers, patents, official documentation, code, data, and supplementary material. Search multiple perspectives and record retrieval dates and queries. For every central citation verify identity and support for the claim.

Compare the candidate with the closest works on explicit axes:

- research object and setting;
- mechanism and information used;
- data, compute, energy, area, bandwidth, latency, and supervision budget;
- causal versus noncausal context;
- validation conditions and evidence level;
- application benefit and deployment cost.

`Not found` is not proof of novelty. A novelty claim passes only when a specific difference remains after adversarial prior-art search and that difference matters scientifically or practically.

## 3. Innovation gate

A surviving idea must have:

1. one-sentence mechanism claim;
2. the hidden assumption it changes;
3. the nearest alternatives and exact difference axes;
4. a falsifier and cheap kill test;
5. a reason the expected gain is not merely more data, parameters, compute, bits, area, future context, or favorable samples;
6. a credible route to application value;
7. a feasible doctoral contribution chain.

Prefer mechanism-level or measurement-level changes. Parameter tuning, ordinary module stacking, renaming, and downstream denoising alone are not high innovation.

## 4. Experiment protocol gate

Freeze before confirmatory results are inspected:

- primary hypothesis and metric;
- practical-significance threshold, not only statistical significance;
- strongest fair baselines and an intentionally simple baseline;
- shared data, stimuli, splits, preprocessing, budgets, and stopping rules;
- seeds, repetitions, uncertainty method, and exclusion rules;
- mechanism-isolating ablations and negative controls;
- stress tests and out-of-distribution conditions;
- commands, configs, environment, expected artifact paths, and protocol hash.

Exploration may be adaptive but must be labelled exploratory. It cannot be renamed confirmatory after seeing the outcome.

## 5. Execution and evidence gate

An experiment is executed only when raw artifacts, exact configuration, log or command, and a parseable result exist. Preserve failures and negative results. Do not replace a missing run with an estimate or prose.

Evidence maturity uses the global levels:

- 炼气: concept and minimum check;
- 筑基: reproducible baseline;
- 结丹: core mechanism passes fair confirmatory comparison;
- 元婴: reusable system passes independent audit;
- 化神: scalable platform with stable governance.

For analog or mixed-signal work, distinguish hand calculation, behavioral model, representative SPICE, transistor-level nominal, PVT/Monte Carlo, post-layout, PCB prototype, and measurement. For ML work, distinguish synthetic, held-out simulated, public measured, and newly measured data. Never collapse these into one word such as "validated".

## 6. Decision gate

Choose one:

- **Continue**: evidence crossed the predefined threshold and remaining risk is bounded.
- **Revise**: mechanism is plausible but attribution, robustness, or feasibility is unresolved.
- **Pivot**: core mechanism is refuted, dominated, or too costly for its value.
- **Stop with a negative result**: the tested space is informative and properly documented.

Record the decision, evidence, rejected alternatives, and conditions that would reopen it.

## 7. Delivery gate

Deliver a compact supervisor brief with:

1. what conclusion changed;
2. strongest evidence and comparison result;
3. failures and their impact;
4. current recommendation;
5. next milestone and missing evidence;
6. links to detailed artifacts;
7. one consolidated user decision, only if necessary;
8. a separate `你要做什么：` line.

Do not make the user read raw logs or every candidate. Detailed methods and tables remain in workspace artifacts.

