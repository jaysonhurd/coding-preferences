---
name: codex-help
description: List or explain personal coding-preferences commands when asked for codex help, and apply or review explicitly selected Go preferences, project instructions, or Spec Kit documentation. Use for this personal command catalog, not general Codex troubleshooting.
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
