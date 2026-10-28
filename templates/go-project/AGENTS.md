# Go project instructions

This is a starting point. Replace every `[TODO: ...]` placeholder and remove
inapplicable guidance before using it in a project. Placeholders are documentation,
not commands to execute. Follow the project's established conventions.

## Project overview

- Purpose: [TODO: Describe the service or application and its users.]
- Go version: [TODO: Specify the supported version, consistent with go.mod.]
- Module: [TODO: Specify the module path from go.mod.]

## Architecture

- Entry points: [TODO: Identify executable packages and startup flow.]
- Package layout: [TODO: Describe package responsibilities and dependency boundaries.]
- External systems: [TODO: List databases, APIs, queues, and other integrations.]
- Design references: [TODO: Link relevant architecture documentation.]

Keep changes within established package boundaries; avoid new layers without a
clear need.

## Build and local development

Run these commands from the module root after completing project-specific setup:

```sh
go build ./...
```

- Prerequisites: [TODO: Document required tools and local services.]
- Setup: [TODO: Document configuration and dependency startup commands.]
- Run locally: [TODO: Provide the actual command, such as go run ./cmd/server.]
- Development workflow: [TODO: Document migrations, fixtures, and cleanup as needed.]

Do not assume an example entry point or undocumented service exists.

## Formatting and verification

- Format changed Go files with `gofmt -w path/to/changed.go`, using actual file paths.
- Run tests with `go test ./...`.
- Prefer Go's standard `testing` package and native test tooling over third-party
  testing frameworks.
- Run static checks with `go vet ./...`.
- Add or update tests for changed behavior using existing test conventions.
- Report checks run, results, and any checks blocked by missing prerequisites.
- Additional checks: [TODO: Document project-specific integration tests, build tags,
  race checks, or CI requirements.]

## Go conventions

- Write idiomatic Go following the guidance in Effective Go.
- Layout: Use blank lines between most logical sections of code to improve
  readability. Prefer grouped `const (...)` and `var (...)` declarations at the
  top of each file (after imports) and function or method body, rather than
  separate declarations for each variable. Keep declarations in the appropriate
  scope.
- Readability: Prefer simple, straightforward code that is easy to read and
  maintain. Apply SOLID principles pragmatically, using small, focused interfaces
  and explicit dependency injection so dependencies are easy to mock in unit
  tests. Avoid unnecessary abstractions.
- Logging: Prefer the standard library's `log/slog` package. Use named constants
  for most fixed log message text and structured attributes for changing values.
  By default, create `logs/` in the repository root and write logs to
  `logs/<repo-name>.log`, substituting the actual repository name. Keep generated
  logs out of version control.
- HTTP: Prefer the standard library's `net/http` package and middleware patterns
  for HTTP services.
- Errors: Return errors to callers and handle them explicitly. Add useful context
  with `fmt.Errorf("operation: %w", err)` when wrapping. Use `errors.Is` or
  `errors.As` where appropriate; avoid string comparisons and logging the same
  error at every layer. Reserve panics for truly unrecoverable programmer errors.
- Contexts: Accept `context.Context` as the first parameter for operations that
  may block or perform I/O. Propagate caller contexts, honor cancellation and
  deadlines, and call cancel functions for derived contexts. Do not store contexts
  in structs or replace request contexts with `context.Background()`.
- Configuration: Load and validate configuration at startup, then pass explicit
  configuration or dependencies to the code that needs them. Follow existing
  environment-variable, flag, and configuration-file conventions.
- Secrets: Never hardcode or commit credentials, tokens, or other secrets. Use the
  project's environment or secret manager, redact sensitive logs, and use dummy
  values in examples. Keep local secret files out of version control.
- Dependencies: Prefer the standard library when it meets the need. Explain new
  production dependencies and significant design tradeoffs.

## Project-specific instructions

- Configuration reference: [TODO: List required variables and safe defaults.]
- Security requirements: [TODO: Document authorization, sensitive data, and logging rules.]
- API and compatibility requirements: [TODO: Describe compatibility commitments.]
- Operational constraints: [TODO: Document timeouts, shutdown, and deployment requirements.]
- Other conventions or exceptions: [TODO: Add instructions specific to this project.]
