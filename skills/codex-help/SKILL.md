---
name: codex-help
description: List or explain personal coding-preferences commands when asked for codex help, and apply or review selected Go preferences, repository validation, project instructions, Spec Kit documentation, or GitHub pull-request workflows. Use for this personal command catalog, not general Codex troubleshooting.
---

# Personal command catalog

Read [COMMANDS.md](COMMANDS.md) for the supported commands and their sources.
Resolve relative source paths from this skill's real directory (follow symlinks),
not from the project being changed. The target is the current project unless the
user names another target. Read the target's instructions before changing it.

## Help

- `$codex-help`, `codex help`, and `list my commands`: display the catalog's
  command names, purposes, and invocation examples. Do not execute the commands.
- `$codex-help help COMMAND`: explain that command, its scope, source guidance,
  prerequisites, and an example. Help requests never change files or install tools.
- Unknown commands: explain the available choices; do not guess an action.

## Selected actions

- `$codex-help apply COMMAND [TARGET]`: perform only the selected catalog action
  on the named target, or the current project when omitted.
- `$codex-help review COMMAND [TARGET]`: inspect the selected concern and report
  findings with file locations; do not edit files or install tools.
- `$codex-help verify go [TARGET]`: run the catalog's Go checks and report results.
- `$codex-help apply repository validation [TARGET]`: follow the
  [repository-validation skill](../repository-validation/SKILL.md) to create or
  extend local checks and matching CI. Configure remote enforcement only when
  the user also requests remote setup.
- `$codex-help review repository validation [TARGET]`: use that skill to inspect
  local/CI coverage and accessible remote settings without making changes.
- `$codex-help verify repository [TARGET]`: run the target's documented existing
  repository checks and report results; do not create checks, install missing
  tools, change remote settings, or repair failures as part of verification.
- `$codex-help create pr [TARGET]`: follow [Pull-request workflows](PULL_REQUESTS.md)
  to create a branch, stage and commit scoped changes, push, and open a PR with
  a Markdown summary and detailed description. Leave it open; never merge.
- `$codex-help merge pr [TARGET]`: follow the same workflow, then merge only
  after validation and required GitHub checks and reviews pass.
- Recognize the catalog's existing `build spec-kit` and `refresh codex please`
  requests as their explicitly documented workflows. They are separate actions;
  applying another preference does not trigger them.

Read only the source sections needed for the selected action. General target
instructions still apply, but selecting one preference does not authorize a full
initialization, source refresh, dependency upgrade, or unrelated cleanup. Accept
several explicitly named commands together. Ask for missing information only
when needed to perform the chosen action correctly.

Preserve established project requirements. Explain conflicts or unsupported
toolchain features instead of silently replacing them. If a source is missing,
report it; do not reconstruct its rules from memory. For changes, run appropriate
formatting and relevant checks and report changes, results, and unresolved issues.
