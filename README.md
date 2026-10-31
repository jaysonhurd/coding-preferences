# coding-preferences

Personal Codex instructions and reusable project templates. Keep general working
preferences in the root `AGENTS.md` and project starting points under `templates/`.
Reusable skill skeletons live under `skills/`.

## Directory structure

```text
README.md                       Usage and maintenance instructions
install.sh                      Install or refresh a local .codex directory
AGENTS.md                       Personal defaults for Codex
skills/
  initialize-go/
    SKILL.md                    Go initialization skill skeleton (not implemented)
    assets/
      templates/                Reserved for generated project templates
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
