#!/usr/bin/env bash
set -euo pipefail

readonly repository_url='https://github.com/jaysonhurd/coding-preferences.git'
mkdir -p -- "${1:-.}"
target="$(cd -- "${1:-.}" && pwd)"
readonly target
script_directory="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
readonly script_directory
readonly bundle="$target/.agents/coding-preferences"

# Never follow an existing .agents symlink into another project or user home.
for directory in "$target/.agents" "$target/.agents/skills" "$bundle"; do
    if [[ -L "$directory" || ( -e "$directory" && ! -d "$directory" ) ]]; then
        printf 'Refusing non-directory or symlink destination: %s\n' "$directory" >&2
        exit 1
    fi
done

temporary_directory=$(mktemp -d)
trap 'rm -rf -- "$temporary_directory"' EXIT

if [[ ! -e "$bundle" ]]; then
    source_directory="$script_directory"
    if [[ ! -f "$source_directory/skills/agent-help/SKILL.md" ]]; then
        git clone --depth 1 "$repository_url" "$temporary_directory/repository"
        source_directory="$temporary_directory/repository"
    fi

    mkdir -p "$target/.agents/skills"
    mkdir "$bundle"
    # Copy only reusable sources and their references, never harness configuration.
    cp -R "$source_directory/skills" "$source_directory/templates" \
        "$source_directory/docs" "$bundle/"
    cp "$source_directory/AGENTS.md" "$source_directory/README.md" \
        "$source_directory/LICENSE" "$bundle/"
else
    printf 'Preserving installed source bundle: %s\n' "$bundle"
    mkdir -p "$target/.agents/skills"
fi

for skill_file in "$bundle"/skills/*/SKILL.md; do
    [[ -f "$skill_file" ]] || continue
    skill_directory="$(dirname -- "$skill_file")"
    skill_name="$(basename -- "$skill_directory")"
    destination="$target/.agents/skills/$skill_name"
    if [[ -e "$destination" || -L "$destination" ]]; then
        printf 'Preserving existing skill: %s\n' "$destination"
    else
        ln -s "../coding-preferences/skills/$skill_name" "$destination"
    fi
done

if [[ -e "$target/AGENTS.md" || -L "$target/AGENTS.md" ]]; then
    printf 'Preserving existing AGENTS.md; merge guidance after review.\n'
else
    cat > "$target/AGENTS.md" <<'GUIDANCE'
# Project guidance

Follow this project's existing structure, commands, and development conventions.
Review and fill in project-specific build and test commands before development.
Keep changes focused, preserve customizations, and report checks and limitations.

Reusable workflows and optional development defaults are available in
[the preference bundle](.agents/coding-preferences/README.md).
Apply only preferences appropriate to this project.

For Spec Kit projects, use `.specify/memory/constitution.md` for durable principles
and quality standards; link to it here after verifying it exists. Keep generated
`.agents/skills/speckit-*` intact and manage customization through supported presets
or project-local overrides. Separate custom skills from generated workflow skills.
Feature requirements, design, and work items belong in `specs/<feature>/spec.md`,
`plan.md`, and `tasks.md`. Skills alone need no agent/subagent definitions or
`.codex/config.toml`. Inspect the integration before considering a `none` baseline.
GUIDANCE
fi

printf 'Installed project-local workflows in %s/.agents/skills\n' "$target"
printf 'Review existing Spec Kit guidance with $agent-help apply spec-kit guidance.\n'
printf 'Existing constitution, generated Spec Kit skills, feature documents, and .codex files were preserved.\n'
