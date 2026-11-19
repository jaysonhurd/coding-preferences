# coding-preferences

Reusable project guidance, optional workflows, and project templates. Root
[AGENTS.md](AGENTS.md) points to [repository guidance](.agents/REPOSITORY.md) and the [file guide](.agents/FILES.md); reusable personal defaults
live in [development preferences](docs/development-preferences.md). Project
starting points live under `templates/` and custom workflows under `skills/`.

## Install in a project

Open a terminal **in the root of the repository you want to update**. Run
`pwd` to check the directory. The final `.` on each `bash` line selects that
directory as the installation target. Choose **one** of the two commands below.
Both require Bash, Git, curl, standard Unix tools, and network access.

### Replace the project's existing AGENTS.md

Use this command to **update an existing `AGENTS.md`**. Save any local edits
you want to keep first. The `--overwrite` flag on the **bash line** replaces
the root instructions and refreshes the bundled files and four managed skill links.

```bash
installer=$(mktemp) &&
curl -fsSL https://raw.githubusercontent.com/jaysonhurd/coding-preferences/main/install.sh -o "$installer" &&
bash "$installer" --overwrite . &&
rm "$installer"
```

Verify the installed instructions from the same directory:

```bash
grep -Fx '## Installed project task map' AGENTS.md
```

The command should print the heading. If the installer printed
`Preserving existing AGENTS.md.`, you ran in the default mode. Run the
overwrite block above to replace that file.

### Install missing files and keep an existing AGENTS.md

Use this command for a first install or to fill in missing files and links.
It creates `AGENTS.md` if absent and preserves it if it already exists.

```bash
installer=$(mktemp) &&
curl -fsSL https://raw.githubusercontent.com/jaysonhurd/coding-preferences/main/install.sh -o "$installer" &&
bash "$installer" . &&
rm "$installer"
```

The installer puts reusable sources and their references in
`.agents/coding-preferences/` and links custom skills into `.agents/skills/`.
It copies skills, templates, docs, README, license, the root pointer, and its two linked guides;
it does not copy Git metadata, CI, or harness configuration. It creates a small
root `AGENTS.md` with a task-by-task map of installed paths and a link to the full file guide. By default it fills gaps in the bundle and preserves existing files and skill links. Destination directory symlinks are rejected.
No agent-specific configuration or agent definitions are created.

Review the installed workflows and adapt root guidance to actual project commands.
For an existing Spec Kit setup, request `$agent-help apply spec-kit guidance`
to organize guidance using the guidance responsibilities below; `build spec-kit` also reviews existing setup before filling
missing pieces. The installer does not run an agent, merge constitution principles,
initialize or migrate Spec Kit, change remote settings, or publish files.

## Update an installed copy

For a downloaded installer, follow [Replace the project's existing AGENTS.md](#replace-the-projects-existing-agentsmd).
From a local coding-preferences checkout, use the same modes without a download.
Replace `/path/to/project` with your target repository and choose one command:

| Desired result | Command from the coding-preferences checkout |
| --- | --- |
| Replace the target's `AGENTS.md` and refresh managed files and links | `bash install.sh --overwrite /path/to/project` |
| Add missing files and links while keeping local edits | `bash install.sh /path/to/project` |
| Show usage | `bash install.sh --help` |

The target defaults to the current directory. Use `--` before a path that starts
with a dash. Extra project files and obsolete skills stay in place. If a real
directory occupies a managed skill link, move it aside before overwriting.
Restart the agent session after changing skills.

## Install for user-wide discovery

For user-wide discovery, link these skills into `~/.agents/skills/`. From this
repository's root, run:

```bash
preferences_root="$PWD"
mkdir -p "$HOME/.agents/skills"
for skill_file in "$preferences_root"/skills/*/SKILL.md; do
    skill_directory="$(dirname "$skill_file")"
    skill_name="$(basename "$skill_directory")"
    skill_link="$HOME/.agents/skills/$skill_name"
    if [[ -e "$skill_link" || -L "$skill_link" ]]; then
        printf 'Already exists; leaving unchanged: %s\n' "$skill_link"
    else
        ln -s "$skill_directory" "$skill_link"
    fi
done
```

For project-local discovery, `install.sh` creates the links automatically. To
link its bundle user-wide instead, set
`preferences_root="/path/to/project/.agents/coding-preferences"` before the loop. Link one source per skill;
existing destinations are preserved, including broken symlinks, so inspect any
"Already exists" message if a skill is missing or points to an older copy.
Keep the source directory in place: links use its absolute path. The help skill
resolves references from that source, so the sibling skills, root `AGENTS.md`,
`docs/`, and `templates/` must remain together.

Start a new agent session if newly linked skills are not visible. You can also
attach `skills/agent-help/SKILL.md` directly in chat and ask it to show your
commands. Use your agent's skill discovery mechanism to select installed skills.

## Guidance responsibilities

| Location in a target project | Responsibility |
| --- | --- |
| `AGENTS.md` | Pointers to shared project guidance under `.agents/`, with when to read each file |
| `.specify/memory/constitution.md` | Durable project principles and quality standards |
| `.agents/skills/speckit-*` | Spec Kit-generated workflow commands; preserve managed files |
| `.agents/skills/<custom-skill>/SKILL.md` | Optional separate reusable project workflows |
| `specs/<feature>/spec.md`, `plan.md`, `tasks.md` | Feature requirements, design, and work items |

Inspect existing Spec Kit integration, presets, overrides, and customizations before
editing. Use supported presets or project-local overrides for managed commands.
Consider the agent-neutral `none` integration when the team needs a shared baseline;
keep harness-specific files separate. Follow the
[official integration workflow](https://github.com/github/spec-kit/blob/main/docs/integrations/index.md)
and the installed CLI's help. Do not silently migrate an existing integration.
Agent/subagent definitions need an actual project use; skills alone do not require
agent configuration files. These files are relevant for agent settings or event handlers.

This repository distributes guidance and setup workflows; it has no initialized
Spec Kit scaffold. Installation does not create a constitution or feature documents.

## License

Original repository content is licensed under the [BSD Zero Clause license
(0BSD)](LICENSE). You may use, modify, and redistribute it, including commercially,
without an attribution requirement.

The copied [Effective Go article](skills/initialize-go/EFFECTIVE_GO.md#source-license)
retains the Go Authors' separate license and notices. The repository's 0BSD
license does not replace those terms.

## Repository checks and public security

Run the same checks as CI from the repository root with Python 3 and Bash:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/check_repository.py
```

The checker validates skill names and required metadata, local Markdown links
and anchors, and shell-script syntax. It uses the standard library and requires
no downloaded packages. External URLs are not checked. Installer tests also exercise preservation, repeat runs, and rejected destinations.
Checks do not replace a full YAML parser, shell linter, or behavioral skill testing.

The `Repository validation` GitHub Actions check runs for pull requests to `main`
and pushes to `main`. It must pass before merging. Pull requests are restricted
to collaborators; `main` also requires resolved conversations and linear history,
with force pushes and deletion disabled, including for administrators. A solo
maintainer can merge their own PR without another person's approval.

Secret scanning and push protection are enabled in GitHub settings. Review
security alerts when changing historical content or adding credentials to local
tooling; never commit secrets. Push protection detects supported secret patterns
and is not a guarantee that all sensitive content will be caught.

Actions are limited to the explicitly allowed checkout commit used by the
workflow, with full commit SHA pinning required. Workflow tokens default to
read-only and cannot approve PRs. When upgrading checkout or adding another
action, review its source and update both the repository's allowed Actions policy
and the workflow's pinned SHA before merging.

## Directory structure

```text
README.md                       Usage and maintenance instructions
install.sh                      Install project-local custom skills safely
AGENTS.md                       Entry point for any harness
.agents/REPOSITORY.md           Repository maintenance rules and checks
.agents/FILES.md                File-by-file guide for the preference bundle
docs/development-preferences.md Reusable personal defaults
skills/
  agent-help/
    SKILL.md                    Personal command help and selected-action routing
    COMMANDS.md                 Command catalog and links to source guidance
    PULL_REQUESTS.md             Branch, commit, push, PR, and merge workflows
    UPDATE_ALL.md               Apply all applicable preferences to a project
  initialize-go/
    SKILL.md                    Go initialization skill skeleton (not implemented)
    EFFECTIVE_GO.md              Complete local Effective Go article
    assets/
      templates/                Reserved for generated project templates
  repository-validation/
    SKILL.md                    Set up or review local checks and matching CI
  spec-kit/
    SKILL.md                    Initialize and document GitHub Spec Kit
    assets/                     Constitution principles and README section
templates/
  go-project/
    AGENTS.md                   Starting point for Go project instructions
```

## Command rename

Personal commands now use `agent` naming: `$agent-help`, `agent help`,
`agent update all`, and `refresh agent please`. Command topics and scope stay the
same. Rerun the installer to add the renamed `agent-help` skill. Review obsolete
help-skill links before removing them manually. Agent integration identifiers and configuration paths must match the selected tool.

## Personal command help

The [agent-help skill](skills/agent-help/SKILL.md) lists the workflows in
[COMMANDS.md](skills/agent-help/COMMANDS.md), explains individual commands, and
applies selected preferences to a project. These are natural-language chat
requests, not Bash commands or registered slash commands.

### Ask for help in chat

```text
$agent-help
$agent-help help go logging
```

The first request lists all catalog commands and examples. The second explains
one command. Neither changes files or runs the listed actions. Once the skill is
discovered, `agent help` and `list my commands` also request the catalog.

### Apply all preferences

In the target project, request:

```text
agent update all
agent update all /path/to/project
$agent-help update all
```

This applies all applicable guidance from the available coding-preferences copy:
Go preferences, project instructions, repository validation, and documentation
and constitution principles for existing Spec Kit projects. It preserves project
requirements and customization, runs relevant checks, and reports changes,
unchanged items, skips, and blockers. Non-Go projects receive applicable general
instructions and validation without Go scaffolding. Repeated runs should leave
already compliant content unchanged.

See [Update all preferences](skills/agent-help/UPDATE_ALL.md) for the workflow.
Like the other personal commands, this is a chat request. It does not download
new preferences, initialize or upgrade Spec Kit, refresh the Effective Go source,
change remote settings, or publish changes. Refresh an installed source copy
using the installation instructions above before invoking it when needed.

### Apply or review individual preferences

Open a session in the target project, then use `apply` to make changes or `review`
to report findings without edits. Supply a file, package, or project path to
narrow the target; otherwise the current project is used.

```text
$agent-help review go solid ./internal
$agent-help apply go logging ./internal/service
$agent-help apply go style and go docs ./internal/service
$agent-help apply go gitignore
$agent-help apply go http-tests ./internal/client
$agent-help apply project instructions /path/to/project
$agent-help verify go
$agent-help apply repository validation
$agent-help review repository validation
$agent-help verify repository
```

Available Go topics include `style`, `solid`, `effective`, `docs`, `gitignore`,
`tests`, `http-tests`, `errors`, `logging`, `tracing`, `http`, and `json`.
Selecting a topic applies only that concern; it does not run a full project
initialization or refresh reference material. JSON preferences are checked against
the supported Go toolchain, and new instrumentation dependencies are explained.
`verify go` runs build, tests, and vet from the target module root and reports
results without making code fixes.

Repository validation is a reusable preference in
[development preferences](docs/development-preferences.md#repository-validation-requirements), the Go project template,
and the Go and Spec Kit setup skills. The
[repository-validation skill](skills/repository-validation/SKILL.md) creates or
extends checks for the target's actual content: skill metadata, local Markdown
links and anchors, shell syntax, and native language checks such as Go formatting,
build, tests, and vet. It reuses the target's tooling where available and documents
the same local commands used by CI.

`apply repository validation` creates local scripts, CI configuration, and usage
instructions. `review repository validation` reports gaps without edits;
`verify repository` runs existing documented checks. To also configure remote
enforcement, include that scope explicitly, for example:

```text
$agent-help apply repository validation and configure GitHub enforcement for this repository
```

Remote setup verifies passing required check names and providers, branch
protections, secret scanning, push protection, and allowed SHA-pinned Actions
where supported. It preserves existing protections and license choices and
reports authentication, permission, or plan limits. Instructions express the
policy; scripts, CI, and verified GitHub settings provide the corresponding
enforcement. Applying an unrelated preference does not trigger validation setup.

For an existing Spec Kit project, documentation and principles can be updated
independently:

```text
$agent-help review spec-kit guidance
$agent-help apply spec-kit guidance
$agent-help review spec-kit principles
$agent-help apply spec-kit readme
$agent-help apply spec-kit principles
```

These selected actions preserve existing customization and do not initialize or
upgrade Spec Kit. For full setup, use `$agent-help build spec-kit` or
`$spec-kit build spec-kit`. To explicitly refresh only the local Effective Go
article, use `$agent-help refresh agent please`. That refresh does not reinstall
personal preferences. The `initialize-go` skill remains a preference guide with
unfinished full-scaffolding work; its à-la-carte commands do not imply that a
complete Go project generator exists.

### Publish changes through a pull request

From the target repository, use either chat command:

```text
$agent-help create pr
$agent-help merge pr
```

Both commands create a branch, stage the current task's changes with `git add`,
commit, push, and open a GitHub pull request. The PR description is a Markdown
document containing a short summary and detailed changes, validation results,
and risks. `create pr` leaves it open and does not enable auto-merge. `merge pr`
also merges after validation and required checks, reviews, and protections pass;
it stops and reports blockers if they cannot be satisfied.

These workflows require Git, authenticated GitHub access (for example, the `gh`
CLI), and push/PR permissions; merging also requires merge permission. An optional
repository path selects another target, for example
`$agent-help create pr /path/to/project`. See
[Pull-request workflows](skills/agent-help/PULL_REQUESTS.md) for scope, retry,
and merge rules. Adding these commands or asking for help does not execute them.

### Add a personal command

Add an entry to [COMMANDS.md](skills/agent-help/COMMANDS.md) with its request,
expected outcome, and source skill, template, or script. Keep the detailed rules
in that source. The help list reads the catalog each time, so new entries do not
need a second manually maintained help table. Update the help skill's routing
when adding a new action form beyond `help`, `apply`, `review`, `verify go`, or
`verify repository`, `update all`, `create pr`, or `merge pr`.

## Use the Go project template

From this repository's root, copy the template into the project's shared guidance directory:

```sh
mkdir -p /path/to/project/.agents
cp -i templates/go-project/AGENTS.md /path/to/project/.agents/project.md
```

Replace `/path/to/project` with the actual destination. Add a link to `.agents/project.md` in the project’s root `AGENTS.md` and explain
that it applies to Go development. Preserve any existing project instructions.
Replace all `[TODO: ...]` placeholders, supply the actual local development
commands, and remove sections that do not apply. The template does not create a Go
module, source files, or development services. Copies are independent; review and
merge future template changes manually.

## Set up Spec Kit in a project

The [spec-kit skill](skills/spec-kit/SKILL.md) creates a GitHub Spec Kit skeleton
using the official Specify CLI, adapts a constitution to the project, and adds
setup and feature-workflow instructions to that project's `README.md`. It bundles
[constitution principles](skills/spec-kit/assets/constitution-principles.md) and
a [README section](skills/spec-kit/assets/readme-section.md); upstream generates
the required templates, scripts, and agent skills. Initial setup requires network
access, Python 3.11+, uv, and your chosen agent.

After installing this repository's project-local skills, open a session in
the target project and request:

```text
build spec-kit
```

This chat request runs the skill's setup workflow in the current project,
including its README instructions. It is not a Bash command. You can explicitly
invoke the same workflow with `$spec-kit build spec-kit`.

You can also explicitly reference `skills/spec-kit/SKILL.md` from this repository.
The skill preserves existing project content and does not implement a feature or
refresh Spec Kit on ordinary requests. For manual initial setup from the target
project root:

```bash
uv tool install specify-cli
specify init --here --integration INTEGRATION --script sh
```

Replace `INTEGRATION` with the selected agent integration key from the installed CLI.

Use the bundled README section for subsequent developer setup and the chat-based
feature workflow. Keep shared `.specify/`, `.agents/skills/`, and `specs/` content
in version control, preserving generated ignores for local state. This repository's
`install.sh` installs project-local custom workflows; it does not initialize Spec Kit in a
target project.

## How instructions interact

Check your agent's documentation for instruction discovery and precedence,
including support for global defaults, project `AGENTS.md` files, and local
overrides. Keep tool-specific configuration separate from shared guidance.

Use optional global instructions for personal defaults and link project architecture, commands,
and conventions from the project's root `AGENTS.md`. The root instructions also apply
when working in this repository. The template is intended for copying into another
project; its presence here does not apply Go-specific guidance to unrelated projects.

These Markdown files guide compatible agents. They do not configure GoLand, change Go compiler
behavior, or enforce formatting or linter rules. Configure the IDE, tools, and CI
separately when enforcement is needed.
