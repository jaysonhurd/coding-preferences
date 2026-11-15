# Personal Codex defaults

- Prefer Go for new backend services unless project requirements suggest otherwise.
- Write idiomatic Go following the guidance in Effective Go.
- Follow existing project architecture, naming, and formatting conventions.
- Keep changes focused on the requested task.
- Favor simple, maintainable solutions and straightforward, easy-to-read code.
- Use blank lines between most logical sections of code to improve readability.
- In Go, prefer grouped `const (...)` and `var (...)` declarations at the top of
  each file (after imports) and function or method body, rather than separate
  declarations for each variable. Keep declarations in the appropriate scope.
- Prefer Go's standard `testing` package and native test tooling over third-party
  testing frameworks.
- For Go logging, prefer the standard library's `log/slog` package and named
  constants for most fixed log message text; use structured attributes for values
  that change.
- By default, create a `logs/` directory in the repository root and write logs to
  `logs/<repo-name>.log`, replacing `<repo-name>` with the repository name.
- For Go HTTP services, prefer the standard library's `net/http` package and
  middleware patterns.
- Apply SOLID design principles pragmatically. Favor small, focused interfaces
  and explicit dependency injection so dependencies are easy to mock in unit
  tests; avoid unnecessary abstractions.
- Explain significant tradeoffs and new production dependencies.
- Never place credentials or secrets in source code.
- Run formatting and relevant tests after code changes.
- Report what changed, what was verified, and any unresolved issues.
- Keep communication concise and practical.
- Proceed autonomously with routine, reversible work within the requested scope.
- .github should always exclude IDE folders, including, but not limited to, .idea (for JetBrains)

## Repository validation requirements

- During project initialization or an explicit validation-setup request, create
  repeatable local checks and CI for the project's actual contents. Extend
  existing checks rather than adding a parallel validation system. For routine
  changes, maintain and run the relevant checks without unrelated setup.
- Validate skill metadata when skills exist, local Markdown links and anchors
  when documentation exists, and shell syntax when shell scripts exist. For Go
  modules, also check formatting, build, tests, and `go vet` using the supported
  Go version and documented build tags. Do not invent a Go module for a
  documentation-only repository.
- Keep local and CI commands consistent and document their prerequisites,
  coverage, and limitations in the README. Test meaningful failure cases when
  adding or changing a validation script. Prefer existing tooling and avoid
  dependencies when standard tools suffice.
- On GitHub, run CI on pull requests to and pushes to the actual default branch.
  Use stable check names, read-only workflow permissions, timeouts, full commit
  SHA pins for external Actions, and checkout without persisted credentials.
  Exclude IDE folders from `.github` content and preserve existing ignores.
- Require successful CI checks before merging when remote configuration is part
  of the authorized task. Register the real check name and provider after a
  successful run, keep the branch up to date, and preserve existing protections.
  Do not weaken checks or use an administrator bypass to make a merge succeed.
- When configuring a public GitHub repository, enable secret scanning and push
  protection where available, restrict Actions to reviewed dependencies, and
  retain read-only token defaults with PR approval by workflows disabled. Keep
  the allowed Actions policy aligned with workflow pins. Report plan, permission,
  authentication, or feature limitations instead of claiming enforcement.
- Creating local validation files does not itself authorize publishing, remote
  settings changes, or merging. Follow the user's task scope. Preserve chosen
  licenses and third-party notices; do not choose or replace a license as a side
  effect of validation setup.
- For this repository, run `python3 -m unittest discover -s scripts -p 'test_*.py'`
  and `python3 scripts/check_repository.py` after changing instructions, skills,
  documentation, scripts, or workflows. These checks validate structure and
  syntax; they do not prove a skill's behavior or a remote setting is enforced.
