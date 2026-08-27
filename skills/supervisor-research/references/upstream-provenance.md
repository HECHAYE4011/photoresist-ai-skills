# Upstream Provenance

- Project: `HKUSTDial/Supervisor-Skills`
- URL: https://github.com/HKUSTDial/Supervisor-Skills
- Fixed commit: `aff5de9e5b902df0ef51e955d4c78b22793d763a`
- Commit date: 2026-07-16T15:09:59Z
- Audit date: 2026-07-28
- Repository snapshot at audit: 4,455 stars, 309 forks
- Root license: CC BY-NC-SA 4.0
- Local use: non-commercial doctoral research

Installed upstream skill directories:

- `idea-evaluator`
- `deep-research`
- `vibe-research-workflow`
- `tech-paper-template`
- `intro-drafter`
- `paper-writer`
- `benchmark-paper-template`
- `paper-polish`
- `pre-submission-reviewer`
- `figure-designer`
- `drawio-reconstruction`

The upstream directories were installed from the fixed commit. `supervisor-research` is a local adaptation and orchestration layer, not an upstream file. It adds doctoral-research execution gates, domain-skill handoffs, evidence maturity, and a low-burden user interface. This adaptation remains under CC BY-NC-SA 4.0. The upstream authors do not endorse the adaptation.

Security review: the package is predominantly Markdown. The Draw.io skill contains local Python helpers for manifests, XML/layout checks, image cropping, and invoking a locally installed Draw.io executable. At the audited commit, no helper uploaded project data, accessed credentials, deleted user files, or performed hidden network calls. Optional dependencies are PyYAML for repository linting and Pillow for crop assistance.

