---
name: repository-validation
description: Create or maintain local repository validations and matching CI during project initialization or explicit validation setup, or review existing validation coverage. Use for skill metadata, Markdown links, shell syntax, Go checks, and authorized GitHub enforcement; not unrelated application changes.
---

# Repository validation

## Inspect and scope

Read the target project's instructions, README, existing scripts and workflows,
supported toolchains, default branch, and relevant remote settings when accessible.
Preserve existing checks, stronger protections, licenses, and unrelated work.
Use the current project unless the user supplies another target. A review is
read-only; report findings and missing prerequisites without creating files,
installing tools, or changing settings.

Follow [Repository validation requirements](../../AGENTS.md#repository-validation-requirements).
Resolve this skill's source links from its real directory, following symlinks.
Its sibling repository scripts and templates must remain available together; if
they are missing, report that and inspect the target's existing tooling first.

## Create or update local checks

- Cover applicable content: skill names and required metadata; local Markdown
  links and anchors; shell syntax; and Go formatting, build, tests, and vet where
  real Go modules exist. Respect existing build tags, module boundaries, generated
  content, and vendored files. Document skipped checks and their reasons.
- Prefer the target's existing tools. For a repository shaped like
  coding-preferences, adapt [check_repository.py](../../scripts/check_repository.py)
  and [its regression tests](../../scripts/test_check_repository.py) into the
  target's scripts directory. Inspect both before adapting; do not overwrite
  customized files or copy hardcoded assumptions without checking them.
- That checker uses Python 3.9+, Git, and Bash. It checks basic single-line skill
  metadata and inline local Markdown links, not complete YAML or every Markdown
  construct. Use the target's fuller validators when required. Do not describe
  structural checks as behavioral verification of a skill.
- Keep scripts runnable locally without CI-only paths. Test valid inputs and
  relevant failures, such as broken links and anchors, invalid metadata, and
  shell syntax errors. Preserve tests that protect existing behavior.

## Create or update CI

Adapt [the repository workflow](../../.github/workflows/validate.yml) to the
target's actual commands and default branch. Merge into an existing suitable
workflow rather than adding duplicate checks. Include:

- Pull-request and default-branch push triggers, with no path filters that leave
  required checks permanently pending for unrelated changes.
- Stable job/check names, read-only token permissions, a timeout, full commit SHA
  pins for reviewed external Actions, and checkout with credential persistence
  disabled. Match runtime versions to the target's requirements.
- The same checks documented for local use. For Go projects, fail on unformatted
  project Go files and run the supported build/test/vet commands. Do not format
  and silently pass in CI.
- IDE ignore rules covering `.idea/`, `.vscode/`, and applicable IDE files under
  `.github`, without removing the target's existing ignore rules.

Document setup, local commands, validation limits, and check names in the README.
Preserve the selected license and all third-party notices.

## GitHub enforcement

Only configure the remote when the user's task includes remote setup. Local
validation setup or a review alone does not authorize remote changes or merging.
Inspect current settings and current official GitHub documentation before writes.

- After a successful CI run, require the actual check name from its expected
  provider and an up-to-date branch. Preserve stronger existing required checks,
  review rules, and other branch protections. Do not bypass them to merge.
- For public repositories, enable secret scanning and push protection when
  supported. Limit allowed Actions to the reviewed workflow dependencies, require
  SHA pinning where supported, use read-only token defaults, and disable workflow
  PR approvals. Update allowlists together with any changed action pins.
- Preserve visibility, collaborator permissions, and PR access policy unless the
  user requested changes. Report unsupported features, missing authentication,
  insufficient permissions, and paid-plan requirements explicitly.
- Verify remote settings with read-back requests. Inspect alert summaries without
  printing secret values. An empty alert list is not proof that history has no
  sensitive data.

## Verify and report

Run the documented commands and checker regression tests from the target root.
Inspect the diff, validate workflow syntax with available tooling, and confirm
referenced scripts and action pins exist. When publishing is authorized, verify
the real CI result before claiming CI enforcement works. Report local changes,
commands and results, remote settings actually verified, and remaining gaps.
