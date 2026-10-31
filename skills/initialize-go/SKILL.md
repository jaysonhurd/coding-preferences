---
name: initialize-go
description: Scaffold for a reusable skill to initialize Go projects; not yet implemented.
---

## General
- Do not perform these refreshes on each codex request unless specifically asked to "refresh codex please".

## Initialize Go

- Depending on the project, please use this guide:
https://go.dev/doc/modules/layout
- Create a `logs/` directory in the repository root by default and write logs to
  `logs/<repo-name>.log`, substituting the actual repository name. Keep generated
  logs out of version control.

## Project preferences - General style etc.

- Generate simple, straightforward code that is easy to read and maintain.
- Use blank lines between most logical sections of code to improve readability.
- Prefer grouped `const (...)` and `var (...)` declarations at the top of each
  file (after imports) and function or method body, rather than separate
  declarations for each variable. Keep declarations in the appropriate scope.
- Apply SOLID principles pragmatically: use small, focused interfaces and explicit
  dependency injection so dependencies are easy to mock in unit tests. Avoid
  unnecessary abstractions.
- Unless otherwise specified, always add json tags to struct items.
- For public variables, constants, methods and functions, always add godoc information above each.  Private methods and functions should also have `//` Godocs but can be shorter.  Private variables and constants do not need `//` Godocs.

## .gitignore preferences
- Always update `.gitignore` to ignore the `.idea/` directory (JetBrains preferences)
- Always update `.gitignore` to ignore `.json` files.  Any required json files (fixtures, tests etc.) will be added as exclusions and should be allowed.  When updating the project please issue warnings each time with lists of these allowed .json files for awareness.
- Always update `.gitignore` to ignore `.log` files unless excluded explicitly.  Always put a `.gitkeep` file in the `/log` directory so that it exists in the Github repository.
- Always update `.gitignore` to ignore the `.codex` directory.

## Tests
- Always create unit tests where possible using Go's built in testing suite.
- Aim for 95% coverage as a minimum where possible.  Alert the developer where this is not possible.
- Make sure all error cases are tested as well.

## Go errors
- Make any error an actual error variable top of the package in vars() following the example format `ErrBadRequest` i.e.
with Err as the prefix.  Add a comment section to each top level public variable and public methods and functions for good measure.  Make reasonable attempt to add 1-2 sentence descriptions.
- Using slog, make fields this pattern:
```
logger.Error("Collection failed",
    slog.Any("error", err),
    slog.String("dealer_id", dealerID),
    slog.Int("attempt", attempt),
)
```
- Do not use `Errorf` or bulk messages built with variables like %s etc since that makes logs hard to 
read at Observability platforms.  In other words, do not build complex concatenated logs vs. separated json fields.
- Always set up OpenTelemetry tracing and metrics using `go.opentelemetry.io` libraries.

## Go Package preferences
- Use the new `encoding/json/v2` as a preference over the old `v1`.
- For HTTP services, prefer the standard library's `net/http` package and
    middleware patterns.
- For logging use Go's builtin `slog`.

## Planned resources

- `assets/templates/`: Reserved for files to copy or adapt into new Go projects.
  The `.gitkeep` file only preserves this empty directory in Git; it is not a
  project asset.

## Work remaining

Define the supported project structure, required inputs, initialization commands,
template customization, and verification steps before using this skill.
