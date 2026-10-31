# coding-preferences

Personal Codex instructions and reusable project templates. Keep general working
preferences in the root `AGENTS.md` and project starting points under `templates/`.
Reusable skill skeletons live under `skills/`.

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
no downloaded packages. External URLs are not checked. It does not replace a full
YAML parser, shell linter, or behavioral testing of skills and installer scripts.

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
install.sh                      Install or refresh a local .codex directory
AGENTS.md                       Personal defaults for Codex
skills/
  codex-help/
    SKILL.md                    Personal command help and selected-action routing
    COMMANDS.md                 Command catalog and links to source guidance
    PULL_REQUESTS.md             Branch, commit, push, PR, and merge workflows
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

## Install personal instructions

Requires Bash, Git, and curl. Run from the directory containing the `.codex`
directory you want to update (for example, run `cd ~` to update `~/.codex`):

```bash
curl -fsSL https://raw.githubusercontent.com/jaysonhurd/coding-preferences/main/install.sh -o /tmp/coding-preferences-install.sh
bash /tmp/coding-preferences-install.sh
rm /tmp/coding-preferences-install.sh
```

The installer clones this repository into a temporary directory, copies its
contents (including dotfiles, excluding `.git`) into `./.codex`, and removes the
temporary clone on exit. Matching files are overwritten to refresh them; unrelated
files, including files inside existing subdirectories, are preserved. Back up any
local edits to repository-provided files before installing.

If `./.codex` does not exist, the installer prints a warning and exits without
cloning or creating it. Create it yourself with `mkdir .codex` if needed, then
rerun the commands. The destination is relative to your current working directory;
the installer does not use `CODEX_HOME`.

## Update the installed copy

Rerun the installation commands from the same directory to refresh the installed
contents. Files absent from the latest repository copy are left in place. Start
a new Codex session after updating instructions so it loads the changes.

## Personal command help

The [codex-help skill](skills/codex-help/SKILL.md) lists the workflows in
[COMMANDS.md](skills/codex-help/COMMANDS.md), explains individual commands, and
applies selected preferences to a project. These are natural-language chat
requests, not Bash commands or registered slash commands.

### Make the skills available

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

To use the copy installed by `install.sh` instead, set
`preferences_root="$HOME/.codex"` before the loop. Link one source per skill;
existing destinations are preserved, including broken symlinks, so inspect any
"Already exists" message if a skill is missing or points to an older copy.
Keep the source directory in place: links use its absolute path. The help skill
resolves references from that source, so the sibling skills, root `AGENTS.md`,
and `templates/` must remain together.

Start a new Codex session if newly linked skills are not visible. You can also
attach `skills/codex-help/SKILL.md` directly in chat and ask it to show your
commands. In the Codex CLI, `/skills` opens the installed skill selector.

### Ask for help in chat

```text
$codex-help
$codex-help help go logging
```

The first request lists all catalog commands and examples. The second explains
one command. Neither changes files or runs the listed actions. Once the skill is
discovered, `codex help` and `list my commands` also request the catalog.

### Apply or review individual preferences

Open a session in the target project, then use `apply` to make changes or `review`
to report findings without edits. Supply a file, package, or project path to
narrow the target; otherwise the current project is used.

```text
$codex-help review go solid ./internal
$codex-help apply go logging ./internal/service
$codex-help apply go style and go docs ./internal/service
$codex-help apply go gitignore
$codex-help apply go http-tests ./internal/client
$codex-help apply project instructions /path/to/project
$codex-help verify go
$codex-help apply repository validation
$codex-help review repository validation
$codex-help verify repository
```

Available Go topics include `style`, `solid`, `effective`, `docs`, `gitignore`,
`tests`, `http-tests`, `errors`, `logging`, `tracing`, `http`, and `json`.
Selecting a topic applies only that concern; it does not run a full project
initialization or refresh reference material. JSON preferences are checked against
the supported Go toolchain, and new instrumentation dependencies are explained.
`verify go` runs build, tests, and vet from the target module root and reports
results without making code fixes.

Repository validation is a reusable preference in
[AGENTS.md](AGENTS.md#repository-validation-requirements), the Go project template,
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
$codex-help apply repository validation and configure GitHub enforcement for this repository
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
$codex-help review spec-kit principles
$codex-help apply spec-kit readme
$codex-help apply spec-kit principles
```

These selected actions preserve existing customization and do not initialize or
upgrade Spec Kit. For full setup, use `$codex-help build spec-kit` or
`$spec-kit build spec-kit`. To explicitly refresh only the local Effective Go
article, use `$codex-help refresh codex please`. That refresh does not reinstall
personal preferences. The `initialize-go` skill remains a preference guide with
unfinished full-scaffolding work; its à-la-carte commands do not imply that a
complete Go project generator exists.

### Publish changes through a pull request

From the target repository, use either chat command:

```text
$codex-help create pr
$codex-help merge pr
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
`$codex-help create pr /path/to/project`. See
[Pull-request workflows](skills/codex-help/PULL_REQUESTS.md) for scope, retry,
and merge rules. Adding these commands or asking for help does not execute them.

### Add a personal command

Add an entry to [COMMANDS.md](skills/codex-help/COMMANDS.md) with its request,
expected outcome, and source skill, template, or script. Keep the detailed rules
in that source. The help list reads the catalog each time, so new entries do not
need a second manually maintained help table. Update the help skill's routing
when adding a new action form beyond `help`, `apply`, `review`, `verify go`, or
`verify repository`, `create pr`, or `merge pr`.

## Use the Go project template

From this repository's root, copy the template to an existing project's root:

```sh
cp -i templates/go-project/AGENTS.md /path/to/project/AGENTS.md
```

Replace `/path/to/project` with the actual destination. If the project already has
an `AGENTS.md`, merge the relevant sections instead of discarding its guidance.
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
the required templates, scripts, and Codex skills. Initial setup requires network
access, Python 3.11+, uv, and Codex.

After installing this repository's skills into your Codex home, open a session in
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
specify init --here --integration codex --script sh
```

Use the bundled README section for subsequent developer setup and the chat-based
feature workflow. Keep shared `.specify/`, `.agents/skills/`, and `specs/` content
in version control, preserving generated ignores for local state. This repository's
`install.sh` installs personal preferences; it does not initialize Spec Kit in a
target project.

## How instructions interact

Codex loads global instructions from its home directory, then project instructions
from the project root down to the current working directory. More specific
instructions take precedence when guidance conflicts. In each directory,
`AGENTS.override.md` takes precedence over `AGENTS.md`; a global override can also
take precedence over the installed personal defaults. See the
[official OpenAI documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Use global instructions for personal defaults and a project's root `AGENTS.md`
for its architecture, commands, and conventions. The root instructions also apply
when working in this repository. The template is intended for copying into another
project; its presence here does not apply Go-specific guidance to unrelated projects.

These Markdown files guide Codex. They do not configure GoLand, change Go compiler
behavior, or enforce formatting or linter rules. Configure the IDE, tools, and CI
separately when enforcement is needed.
