---
name: spec-kit
description: Initialize a GitHub Spec Kit skeleton in a new or existing project, customize its constitution, and document setup and the feature workflow in the project's README. Use when the user requests "build spec-kit" or asks to add or set up Spec Kit, not for routine feature implementation or automatic refreshes.
---

# Set up GitHub Spec Kit

Create a working Spec Kit scaffold using the official Specify CLI. This skill
bundles project-specific starter assets; upstream supplies the executable helper
scripts, templates, and agent skills. Initial setup requires network access.
Do not substitute empty directories or handwritten agent commands for a working
installation. Do not initialize or refresh Spec Kit on unrelated requests.

## Request command

Treat `build spec-kit` in agent chat as a request to run this skill's setup
workflow in the current project: inspect, generate missing infrastructure,
customize the constitution, update the project's README, and verify the result.
Use an explicitly named target directory when supplied. This is a natural-language
request, not a Bash command. For an existing scaffold, preserve customizations and
complete missing setup rather than forcing a refresh or implementing a feature.

## Inspect the target

- Identify the requested project root and read its `AGENTS.md`, README, ignore
  rules, and existing `.specify` and agent configuration. Preserve unrelated work.
- Use the requested agent integration; default to `codex` for Codex projects.
  Examples below use Codex on Bash. Adapt the integration and script type when
  the target environment differs.
- If a working scaffold already exists, complete only missing customization and
  documentation. Do not reinitialize it merely because this skill was invoked.
  For an explicitly requested upgrade, follow upstream's upgrade instructions.

## Generate the scaffold

Requires Python 3.11+, `uv`, and the chosen agent. Check existing tools first;
install the CLI only if missing. If prerequisites cannot be installed, report
what is missing rather than claiming that setup is complete.

```bash
uv tool install specify-cli

# Run from the target project root, not from this skill's directory.
specify init --here --integration codex --script sh
```

For a new project directory, use
`specify init PROJECT_NAME --integration codex --script sh` instead. Replace
`PROJECT_NAME` with the actual name. An existing nonempty directory may require
merge confirmation. Review possible overlaps first; use `--force` only after
determining that the merge will preserve required customizations. Never blanket
replace an existing constitution, README, AGENTS.md, or agent configuration.

If `.specify` is already initialized but lacks the requested integration, use
`specify integration install codex` instead of initializing again. Check the
installed CLI's `--help` and official documentation if its flags differ.

Expected core output (additional managed files may vary by release):

```text
.specify/
  memory/constitution.md
  scripts/
  templates/
.agents/skills/speckit-*/SKILL.md    # Codex integration
specs/                            # Feature documents created during the workflow
```

Do not invent a feature or generate implementation tasks merely to populate
`specs/`. Create `specs/.gitkeep` if an empty tracked feature directory is useful.
Git branch automation is optional; install `specify extension add git` only when
the project requests that workflow.

## Customize and document

1. Read [assets/constitution-principles.md](assets/constitution-principles.md).
   Use it as input to the generated constitution workflow, adapting it to the
   project's existing requirements. Retain upstream's constitution structure,
   version/date metadata, and template synchronization behavior. For an existing
   constitution, merge only applicable missing principles. Do not copy the asset
   verbatim over `.specify/memory/constitution.md`.
2. For Go projects, incorporate the project's Go preferences (including an
   invoked `initialize-go` skill when available). Keep implementation choices in
   plans and engineering rules in the constitution; feature specifications should
   describe user needs and acceptance criteria. This skill does not scaffold Go
   source code or add application dependencies.
3. Read [assets/readme-section.md](assets/readme-section.md) and merge its setup,
   layout, and workflow guidance into the target project's `README.md`. Create
   that file if absent; otherwise preserve existing content and update an existing
   Spec Kit section rather than appending duplicates. Adapt commands to the actual
   integration and record the installed CLI version with `specify version`.
4. Keep shared `.specify` infrastructure, generated agent skills, and feature
   documents available for version control. Preserve upstream's ignores for local
   state. If the project ignores all `*.json`, inspect generated files and add
   narrow exceptions for required shared JSON configuration. Report the actual
   exception paths; do not allow all JSON or commit machine-local feature state.
   If `.codex/` is ignored, inspect generated changes there and explain any shared
   configuration that needs an explicit exception; never commit credentials or
   session data. Preserve `.idea/` and other existing IDE ignores.

## Verify and report

- During initial setup, create or extend repeatable validation for generated
  skill metadata, local documentation links and anchors, and helper-shell syntax
  following [repository-validation](../repository-validation/SKILL.md). Integrate
  with existing CI and document the same local commands; include the project's
  native checks where applicable. Preserve upstream-managed files and extend
  surrounding tooling rather than rewriting generated helpers. A documentation-
  only update should maintain relevant checks without triggering full CI setup.
- Record these validation expectations in the constitution and README using the
  bundled principles. Remote required checks and public-repository security
  settings need task scope that includes remote setup; report that distinction
  and any missing capabilities rather than claiming files enforce remote policy.

- Run `specify check` from the target root and inspect the generated diff.
- Confirm the constitution, core templates, helper scripts, and selected agent
  skills exist and are nonempty. Check that the README's commands match the
  generated integration. For Codex, current skills use `$speckit-...` in chat.
- Check relevant generated shared files with `git check-ignore -v -- PATH`;
  distinguish intentional local-state ignores from accidentally ignored assets.
- Confirm there are no unresolved constitution placeholders introduced by setup,
  and that unrelated files and existing specifications remain intact.
- Report generated/customized files, CLI version, checks performed, and any
  prerequisite or agent-reload steps still required. Scaffold setup stops before
  feature implementation unless the user also requested that work.

## Official references

Consult these when installing or resolving version differences:

- [Spec Kit installation and prerequisites](https://github.com/github/spec-kit#get-started)
- [Core initialization commands](https://github.github.io/spec-kit/reference/core.html)
- [Codex integration and skill invocation](https://github.com/github/spec-kit/blob/main/docs/integrations/codex.md)
- [Upgrade existing infrastructure](https://github.github.io/spec-kit/upgrade.html)
