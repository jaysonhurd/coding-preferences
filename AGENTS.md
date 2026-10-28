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
