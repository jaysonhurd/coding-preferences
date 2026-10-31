## Spec Kit

This project uses [GitHub Spec Kit](https://github.com/github/spec-kit) to carry
feature requirements through planning, tasks, implementation, and verification.

If the `spec-kit` setup skill from `coding-preferences` is installed, request
`build spec-kit` in agent chat to create or complete this project's skeleton and
README setup instructions. Use `$spec-kit build spec-kit` to invoke it explicitly.
This is a chat request, not a Bash command; it preserves existing customizations.

### Developer setup

Install Python 3.11+, [uv](https://docs.astral.sh/uv/), and Codex. Then install the
Specify CLI:

```bash
uv tool install specify-cli
specify version
specify check
```

Run the last two commands from the project root. Shared Spec Kit files are checked
into the repository, so a fresh checkout normally does not require initialization.
The project setup notes should record the CLI version used to generate them;
install that version with `uv tool install 'specify-cli==VERSION'` when reproducing
the setup, replacing `VERSION` with that recorded version.

For the initial setup of a project that does not yet contain `.specify/`, run:

```bash
specify init --here --integration codex --script sh
```

Review merge prompts in an existing directory. Do not rerun initialization as a
routine refresh. Follow the [upgrade guide](https://github.github.io/spec-kit/upgrade.html)
when intentionally updating managed files. Open a new agent session if generated
skills are not visible in the current session.

### Project layout

```text
.specify/memory/constitution.md   Project principles and governance
.specify/templates/              Templates for feature artifacts
.specify/scripts/                Spec Kit workflow helpers
.agents/skills/speckit-*/         Generated Codex skills
specs/                          Feature specifications, plans, and tasks
```

The `specs/` directory gains feature subdirectories during specification work;
initial setup does not create a sample application or feature.

### Feature workflow

Run these in Codex chat, one step at a time, reviewing each result. Establish the
constitution once per project and amend it when project principles change:

```text
$speckit-constitution Establish or update this project's engineering principles.
```

For each feature:

```text
$speckit-specify Describe the intended users, behavior, and acceptance criteria.
$speckit-clarify
$speckit-plan Describe the project's stack, architecture, and technical constraints.
$speckit-tasks
$speckit-analyze
$speckit-implement
$speckit-converge
```

Replace the descriptive text with actual requirements. Clarification and analysis
help resolve ambiguity and inconsistencies before implementation. Repeat
implementation and convergence as needed until the feature is verified. These are
agent skills, not Bash commands.

Commit shared constitution, templates, scripts, agent skills, and feature
documents. Preserve the generated ignores for machine-local state and keep
credentials and session data out of version control.
