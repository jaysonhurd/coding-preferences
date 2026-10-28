---
name: initialize-go
description: Scaffold for a reusable skill to initialize Go projects; not yet implemented.
---

# Initialize Go

Depending on the project, please use this guide:

https://go.dev/doc/modules/layout

## Project preferences

- Generate simple, straightforward code that is easy to read and maintain.
- Use blank lines between most logical sections of code to improve readability.
- Prefer grouped `const (...)` and `var (...)` declarations at the top of each
  file (after imports) and function or method body, rather than separate
  declarations for each variable. Keep declarations in the appropriate scope.
- Prefer Go's standard `testing` package and native test tooling over third-party
  testing frameworks; run tests with `go test ./...`.
- Prefer the standard library's `log/slog` package for logging. Use named constants
  for most fixed log message text and structured attributes for changing values.
- Create a `logs/` directory in the repository root by default and write logs to
  `logs/<repo-name>.log`, substituting the actual repository name. Keep generated
  logs out of version control.
- For HTTP services, prefer the standard library's `net/http` package and
  middleware patterns.
- Apply SOLID principles pragmatically: use small, focused interfaces and explicit
  dependency injection so dependencies are easy to mock in unit tests. Avoid
  unnecessary abstractions.
- Unless otherwise specified, always add json tags to struct items.

## Go errors
- Use slog
- Make any error an actual error variable top of the package in vars() following the example format `ErrBadRequest` i.e.
with Err as the prefix.  
- Using slog, make fields this pattern:
```go
logger.Error("Collection failed",
    slog.Any("error", err),
    slog.String("dealer_id", dealerID),
    slog.Int("attempt", attempt),
)
```
- Do not use `Errorf` or bulk messages built with variables like %s etc since that makes logs hard to 
read at Observability platforms.


## Planned resources

- `assets/templates/`: Reserved for files to copy or adapt into new Go projects.
  The `.gitkeep` file only preserves this empty directory in Git; it is not a
  project asset.

## Work remaining

Define the supported project structure, required inputs, initialization commands,
template customization, and verification steps before using this skill.
