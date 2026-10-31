# Update all preferences

Use this workflow for `codex update all [TARGET]` or
`$codex-help update all [TARGET]`. The target is the current project when omitted.
This invocation authorizes applying all applicable project preferences together;
asking for help or adding the command does not execute it.

## Inspect and apply

Read the target's instructions, working-tree status, architecture, supported
language versions, existing validation, and any Spec Kit infrastructure. Use the
available coding-preferences source copy resolved from this skill's real directory.
Read [personal defaults](../../AGENTS.md) and the current
[command catalog](COMMANDS.md), following each applicable action's source and
compatibility rules. Preserve unrelated local work and established project
requirements. Do not overwrite custom instructions or replace licenses.

Apply these concerns as one coherent update:

- Merge applicable personal defaults into the target's project instructions.
  For Go projects, adapt [the Go template](../../templates/go-project/AGENTS.md)
  using inspected facts and preserve existing architecture and commands.
  For other projects, retain their language and tooling; omit Go-only rules.
- Apply every applicable Go preference in the catalog, including style, SOLID,
  Effective Go, documentation, ignores, tests, HTTP client tests, errors, logging,
  tracing, HTTP, and JSON. Read [initialize-go](../initialize-go/SKILL.md) and
  its referenced guidance. Skip Go work when no Go code exists; do not invent a
  module. Preserve API and wire-format contracts, explain new dependencies, and
  report unsupported toolchain features rather than upgrading Go implicitly.
- Follow [repository-validation](../repository-validation/SKILL.md) to extend
  existing local checks and matching CI for the target's actual contents, and
  document prerequisites, coverage, and limitations. Include IDE ignores while
  preserving existing exceptions and tracked files. Configure no remote settings
  unless the user separately authorizes that scope.
- For existing Spec Kit projects, apply the catalog's `spec-kit readme` and
  `spec-kit principles` actions from their bundled sources. Preserve custom
  content and follow constitution amendment rules. Report missing infrastructure
  as skipped; do not initialize or upgrade Spec Kit.

Use the current catalog so newly added project preference actions are considered
on future runs. Help, review, verification, publishing, source-refresh, installer,
and initialization commands are not additional project preferences to execute.
In particular, this command does not run `build spec-kit`, `refresh codex please`,
`install.sh`, `create pr`, or `merge pr`. Separately requested actions retain their
own scope and authorization.

## Verify and report

Run relevant formatting and the target's documented checks, including checks
added by this update. For Go modules include formatting, build, tests, and vet
with supported versions and documented tags. Resolve failures caused by the
update and report unrelated failures or missing prerequisites accurately.

Keep already compliant content unchanged on repeated runs. Report the target and
source copy, changes made, preferences already satisfied, inapplicable items,
blocked items with reasons, checks and outcomes, and unresolved issues. Continue
independent applicable work when a concern is blocked; do not claim completion
for skipped checks or unsupported preferences.
