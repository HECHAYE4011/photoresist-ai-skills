# Photoresist AI Skills

Reusable Codex skills for evidence-driven photoresist metrology planning.

## Included skills

- `supervisor-research`: research supervision, evidence gates, experiment protocol, and audit.
- `deep-research`: survey-grade literature investigation and citation verification.

The domain-specific `photoresist-metrology-design` skill is planned but is not included until its technical rules are validated.

## Install from GitHub

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo HECHAYE4011/photoresist-ai-skills `
  --path skills/supervisor-research skills/deep-research
```

Restart or start a new Codex task after installation.

## Scope

These skills help structure research and measurement planning. They do not replace optical safety review, instrument calibration, or laboratory validation.
