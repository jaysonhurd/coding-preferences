# Constitution starter principles

Adapt these principles to the target project through the generated constitution
workflow. Preserve existing requirements and supply actual project metadata.

## Scope and maintainability

Keep changes focused on agreed requirements. Favor straightforward code, existing
architecture, small interfaces, and explicit dependencies. Explain significant
tradeoffs and new production dependencies.

## Requirements and planning

Define user-visible behavior and measurable acceptance criteria before planning
implementation. Record technical decisions and unresolved questions in the plan.
Keep specifications, plans, and tasks consistent when scope changes.

## Verification

Verify acceptance criteria and meaningful failure cases with appropriate tests.
Run formatting and relevant checks after code changes. Record results and any
unresolved limitations; do not claim unperformed checks passed.

During project setup, create or extend repeatable local validation and matching CI
for applicable skill metadata, Markdown links and anchors, shell syntax, and native
build/test/static checks. Use stable required check names, PR/default-branch
triggers, read-only tokens, timeouts, and reviewed SHA-pinned Actions. Test
meaningful failures in new validation scripts and document commands and limits.
Configure required checks only within authorized remote setup and verify the
actual passing check and provider before claiming enforcement.

## Security and configuration

Keep credentials, secrets, generated logs, IDE settings, and machine-local agent
state out of version control. Document required configuration without embedding
secret values. Track shared specification tooling and project rules.

When public GitHub security setup is authorized, enable supported secret scanning
and push protection, restrict allowed Actions to reviewed dependencies, and disable
workflow PR approvals. Preserve stronger protections, licenses, and third-party
notices. Report missing permissions or unsupported features explicitly.

## Go projects only

Prefer idiomatic Go, standard-library HTTP handlers and testing, structured
`log/slog` logging, and small interfaces with explicit dependency injection.
Use the project's supported Go version and established package layout. Incorporate
additional project-specific Go rules from its instructions without silently
changing existing architecture or introducing dependencies during Spec Kit setup.

## Governance

Document amendments and their reasons. Review affected templates and active
feature plans after a rule changes. Record the actual constitution version,
ratification date, and amendment date in the generated constitution format.
