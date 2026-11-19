#!/usr/bin/env bash
set -euo pipefail

readonly repository_url='https://github.com/jaysonhurd/coding-preferences.git'
usage() {
    printf '%s\n' 'Usage: install.sh [--overwrite] [--] [PROJECT_DIR]' \
        'Default: install missing files. --overwrite: replace managed files, skill links, and root AGENTS.md.'
}

overwrite=false
options=true
project_path=''
for argument in "$@"; do
    if [[ "$options" == true ]]; then
        case "$argument" in
            --overwrite) overwrite=true; continue ;;
            --help|-h) usage; exit 0 ;;
            --) options=false; continue ;;
            -*) usage >&2; exit 2 ;;
        esac
    fi
    if [[ -n "$project_path" || -z "$argument" ]]; then usage >&2; exit 2; fi
    project_path="$argument"
done

mkdir -p -- "${project_path:-.}"
target="$(cd -- "${project_path:-.}" && pwd)"
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

source_directory="$script_directory"
if [[ ! -f "$source_directory/skills/agent-help/SKILL.md" ]]; then
    git clone --depth 1 "$repository_url" "$temporary_directory/repository"
    source_directory="$temporary_directory/repository"
fi

# Walk only shipped paths. Parents precede children so all destination
# directories can be checked before any managed file is replaced.
manifest="$temporary_directory/files"
(cd "$source_directory" && find skills templates docs .agents/REPOSITORY.md \
    .agents/FILES.md AGENTS.md README.md LICENSE -print0) > "$manifest"
check_directory() {
    if [[ -L "$1" || ( -e "$1" && ! -d "$1" ) ]]; then
        printf 'Expected a directory at %s\n' "$1" >&2
        exit 1
    fi
}

check_file() {
    if [[ -e "$1" && ! -L "$1" && ! -f "$1" ]]; then
        printf 'Expected a file or link at %s\n' "$1" >&2
        exit 1
    fi
}

check_directory "$bundle/.agents"
while IFS= read -r -d '' relative; do
    if [[ -L "$source_directory/$relative" ]]; then
        printf 'Unexpected source symlink: %s\n' "$relative" >&2
        exit 1
    elif [[ -d "$source_directory/$relative" ]]; then
        check_directory "$bundle/$relative"
    else
        check_file "$bundle/$relative"
    fi
done < "$manifest"

if [[ "$overwrite" == true ]]; then
    check_file "$target/AGENTS.md"
    for skill_file in "$source_directory"/skills/*/SKILL.md; do
        skill_directory="${skill_file%/SKILL.md}"
        check_file "$target/.agents/skills/${skill_directory##*/}"
    done
fi

# Replace the directory entry itself, including dangling links or links to
# directories. Never open an existing file (or its link target) for writing.
install_entry() {
    local source="$1" destination="$2"
    if [[ -e "$destination" || -L "$destination" ]]; then
        if [[ "$overwrite" == false ]]; then return; fi
    fi
    local pending
    pending="$(mktemp -d -- "${destination%/*}/.install.XXXXXXXX")"
    if [[ "$3" == link ]]; then
        ln -s -- "$source" "$pending/entry"
    else
        cp -- "$source" "$pending/entry"
    fi
    if [[ -L "$destination" && -d "$destination" ]]; then
        unlink "$destination"
    fi
    mv -f -- "$pending/entry" "$destination"
    rmdir -- "$pending"
}

mkdir -p -- "$target/.agents/skills" "$bundle/.agents"
while IFS= read -r -d '' relative; do
    if [[ -d "$source_directory/$relative" ]]; then
        mkdir -p -- "$bundle/$relative"
    else
        install_entry "$source_directory/$relative" "$bundle/$relative" file
    fi
done < "$manifest"

for skill_file in "$source_directory"/skills/*/SKILL.md; do
    skill_directory="${skill_file%/SKILL.md}"
    skill_name="${skill_directory##*/}"
    install_entry "../coding-preferences/skills/$skill_name" "$target/.agents/skills/$skill_name" link
done

if [[ "$overwrite" == false && ( -e "$target/AGENTS.md" || -L "$target/AGENTS.md" ) ]]; then
    printf 'Preserving existing AGENTS.md.\n'
else
    cat > "$temporary_directory/AGENTS.md" <<'GUIDANCE'
# Project instructions

Use the [file guide](.agents/coding-preferences/.agents/FILES.md) to select a
workflow, preference, template, or reference for the current task. It lists
every file in the installed bundle and explains the links in `.agents/skills/`.
Follow this project's own development commands and conventions.

When adding project-specific guidance, keep it under `.agents/` and link it
here with a sentence explaining when to read it.

GUIDANCE
    sed -n '/^## Installed project task map$/,$p' "$source_directory/AGENTS.md" >> "$temporary_directory/AGENTS.md"
    install_entry "$temporary_directory/AGENTS.md" "$target/AGENTS.md" file
fi

printf 'Installed project-local workflows in %s/.agents/skills\n' "$target"
printf 'Review existing Spec Kit guidance with $agent-help apply spec-kit guidance.\n'
printf 'Existing constitution, generated Spec Kit skills, feature documents, and agent configuration files were preserved.\n'
