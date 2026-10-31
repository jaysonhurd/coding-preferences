# Personal commands

These are chat requests interpreted by the `codex-help` skill, not native slash
commands or Bash commands. Replace `TARGET` with a project, package, or file path;
omit it to use the current project. Help lists this catalog without executing it.

```text
$codex-help
codex update all
codex update all /path/to/project
$codex-help help go logging
$codex-help review go solid ./internal
$codex-help apply go logging ./internal/service
$codex-help apply go style and go docs ./internal/service
$codex-help verify go
$codex-help apply repository validation
$codex-help review repository validation
$codex-help verify repository
$codex-help create pr
$codex-help merge pr
```

## Apply all preferences

| Request | Behavior and source |
| --- | --- |
| `codex update all TARGET` | Apply all applicable coding-preferences guidance to the target project using [Update all preferences](UPDATE_ALL.md), then run relevant checks. Includes Go preferences, project instructions, repository validation, and existing Spec Kit documentation and principles where applicable. Report applied, unchanged, skipped, and blocked items. |

`$codex-help update all TARGET` is the explicit skill invocation. Omit `TARGET`
to use the current project. This updates the project from the available source
copy; it does not fetch or reinstall coding-preferences, initialize or upgrade
Spec Kit, refresh Effective Go, publish changes, or configure remote settings.

## Go preferences à la carte

Use `apply` to make changes or `review` to report findings. Read the indicated
sections of [initialize-go](../initialize-go/SKILL.md); that file is a preference
guide with unfinished full-scaffolding work, not an implemented project generator.
These commands use its existing guidance without running full initialization.

| Command | Scope and source sections |
| --- | --- |
| `go style` | Apply readability, blank-line, and grouped-declaration preferences from **Project preferences - General style etc.**, then format changed Go files. |
| `go solid` | Apply or review all five principles from **General → SOLID principles**, using small consumer interfaces, composition, and explicit dependencies where useful. |
| `go effective` | Use relevant sections of [EFFECTIVE_GO.md](../initialize-go/EFFECTIVE_GO.md) to improve or review idiomatic Go. Preserve its historical examples and check compatibility with the project's Go version. Do not refresh the reference. |
| `go docs` | Add or review declaration comments and JSON field tags from **Project preferences - General style etc.** Preserve intentional wire formats and excluded fields. |
| `go gitignore` | Apply **.gitignore preferences**, including IDE folders, local Codex state, generated logs, and narrow exceptions for required JSON. Report allowed JSON paths. Use the canonical `logs/` directory from **Initialize Go**; interpret the older `/log` mention consistently as `logs/.gitkeep`. Do not untrack existing files automatically. |
| `go tests` | Apply **Tests** using native Go testing, meaningful success and error cases, and a 95% coverage goal where practical. Report measured coverage and limitations; do not create tests just to inflate coverage. |
| `go http-tests` | Apply the HTTP client testing preference in **Tests**, using an injectable `ClientDoer` with `Do(*http.Request) (*http.Response, error)`. Preserve appropriate server-handler tests. |
| `go errors` | Apply the error-variable guidance in **Go errors** and comments for exported sentinel errors. Preserve error identity and existing caller contracts. If dynamic wrapping is needed, reconcile with the target project's error conventions. |
| `go logging` | Apply structured `log/slog` guidance from **Go errors**, **Go Package preferences**, and [personal defaults](../../AGENTS.md). Use structured attributes, fixed message constants where appropriate, and `logs/<repo-name>.log`; keep generated logs ignored. |
| `go tracing` | Apply the OpenTelemetry tracing and metrics preference in **Go errors**. Inspect existing instrumentation and configuration first; integrate with the current lifecycle, explain new dependencies, and avoid inventing collector endpoints or credentials. |
| `go http` | Apply the standard-library `net/http` and middleware preference from **Go Package preferences** within the requested scope, preserving API behavior and established requirements. |
| `go json` | Evaluate the `encoding/json/v2` preference in **Go Package preferences** against the project's supported toolchain and wire-format requirements. Apply it only when supported; report prerequisites or incompatibilities instead of silently upgrading Go or enabling experiments. |

## Project instructions and verification

| Request | Behavior and source |
| --- | --- |
| `apply repository validation TARGET` | Use [repository-validation](../repository-validation/SKILL.md) to create or extend applicable skill, Markdown, shell, and native-language checks with matching CI and README instructions. Local setup does not change remote settings; include an explicit request for GitHub enforcement to configure and verify required checks, reviewed Actions, secret scanning, and push protection. |
| `review repository validation TARGET` | Review local checks, CI, and accessible remote settings against [validation requirements](../../AGENTS.md#repository-validation-requirements), reporting gaps without edits or setup. |
| `verify repository TARGET` | Run the target's documented existing checks. In coding-preferences, run `python3 -m unittest discover -s scripts -p 'test_*.py'` and `python3 scripts/check_repository.py`. Report failures or missing commands; do not add tooling, repair files, or change remote settings. |
| `apply project instructions TARGET` | Adapt [templates/go-project/AGENTS.md](../../templates/go-project/AGENTS.md) to the target Go project. Fill placeholders from inspected project facts, merge existing instructions, and flag facts that cannot be determined. Do not create a module or application. |
| `review project instructions TARGET` | Compare project instructions with that template and [personal defaults](../../AGENTS.md), reporting missing or conflicting guidance without editing. |
| `verify go TARGET` | From the target Go module root, run `go build ./...`, `go test ./...`, and `go vet ./...` as described in the template. Respect documented build tags and prerequisites. Report failures and missing prerequisites; do not rewrite code or install tools as part of verification. Ask which module to use if a multi-module target is ambiguous. |
| `refresh codex please` | Explicitly refresh the local Effective Go copy using **General → Effective Go** in [initialize-go](../initialize-go/SKILL.md). Preserve the article, examples, links, license, and retrieval date. This does not reinstall personal preferences or upgrade Spec Kit. |

## GitHub pull requests

Read [Pull-request workflows](PULL_REQUESTS.md) for prerequisites, change scope,
Markdown content, and merge requirements. Invoking a command authorizes its
listed Git and GitHub actions for the selected changes. Help requests and requests
to add or edit these commands do not authorize executing them.

| Request | Behavior and source |
| --- | --- |
| `create pr TARGET` | Create a branch, use `git add` for scoped changes, commit, push the branch, and open a GitHub PR with a Markdown summary, implementation details, validation, and risks. Leave the PR open without enabling auto-merge. Follow [Pull-request workflows](PULL_REQUESTS.md). |
| `merge pr TARGET` | Perform the same branch, stage, commit, push, and documented PR workflow, then merge the resulting PR after validation, required checks, reviews, and other repository protections are satisfied. Never bypass protections. Follow [Pull-request workflows](PULL_REQUESTS.md). |

`TARGET` is a repository path for these two commands. The current task determines
which changes belong in the PR; unrelated working-tree changes stay untouched.

## Spec Kit

| Request | Behavior and source |
| --- | --- |
| `build spec-kit` | Run the full [spec-kit](../spec-kit/SKILL.md) setup workflow, including prerequisite checks, generated infrastructure, constitution customization, README instructions, and verification. Network access and additional tools may be required. Stop before feature implementation. |
| `apply spec-kit readme TARGET` | Adapt only [the README section](../spec-kit/assets/readme-section.md) to an existing project's actual Spec Kit setup. Merge its existing section and verify documented commands against installed tooling. Do not initialize or upgrade Spec Kit; report missing infrastructure. |
| `apply spec-kit principles TARGET` | Merge applicable [constitution principles](../spec-kit/assets/constitution-principles.md) into an existing constitution, preserving its structure and governance metadata. Follow the existing amendment process. Do not initialize Spec Kit or generate feature work; report a missing constitution. |
| `review spec-kit readme TARGET` | Check the README against the bundled section and actual project infrastructure, without edits or setup. |
| `review spec-kit principles TARGET` | Compare the existing constitution with the bundled principles and report gaps, without edits or setup. |

After Spec Kit is initialized, its generated `$speckit-...` skills implement the
feature workflow. See [the bundled workflow instructions](../spec-kit/assets/readme-section.md#feature-workflow);
those skills must exist in the target project before they can be used.

## Maintaining this catalog

Add a row when adding a supported workflow. Give each command a source and a
bounded outcome; keep detailed engineering rules in their existing source files.
Update [SKILL.md](SKILL.md) if a new action needs different routing. Keep examples
in the repository README aligned with these invocation forms.
