# Repository guidance

This repository contains reusable coding preferences and skills, not a Go service.
See [README.md](../README.md) for installation, layout, and supported chat commands.
Skills live in `skills/`, their supporting assets beside them, project templates
in `templates/`, and standard-library Python validation in `scripts/`.

Preserve existing conventions, customizations, licenses, and unrelated work.
Keep changes focused and readable; never commit secrets. Keep IDE folders,
including `.idea/`, out of `.github` content. Report changes, checks, and limits.

[Development preferences](../docs/development-preferences.md) are reusable defaults
for target projects; apply only what fits their language and requirements.

## Guidance responsibilities

Root `AGENTS.md` points to shared guidance under `.agents/`. Keep project structure, commands, and conventions in the linked project guidance.
In Spec Kit projects, `.specify/memory/constitution.md` holds durable principles
and quality standards; link to it rather than duplicating it. Generated
`.agents/skills/speckit-*` provide workflow commands: preserve them and customize
through supported presets or project-local overrides. Separate custom workflows
belong in `.agents/skills/<custom-skill>/SKILL.md`. Feature requirements, design,
and work items belong in `specs/<feature>/spec.md`, `plan.md`, and `tasks.md`.

Do not create agent or subagent definitions without a project need. Skills alone
do not require agent configuration files; use them only for actual agent settings
or Spec Kit event handlers. Inspect the existing integration before considering
an agent-neutral `none` baseline. Keep harness-generated files separate from
shared project guidance. This repository distributes setup guidance; it does not
itself have an initialized Spec Kit project or a project constitution.

## Repository validation requirements

After changing instructions, skills, documentation, scripts, or workflows, run:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/check_repository.py
```

Requires Python 3, Bash, and Git. These checks cover metadata, local Markdown
links and anchors, shell syntax, and installer behavior; they do not prove skill
behavior or remote policy enforcement. Keep local checks and CI consistent.
See [validation standards](../docs/development-preferences.md#repository-validation-requirements)
for setup in target projects. Do not invent a Go module here or change remote
settings as a side effect of local maintenance.
