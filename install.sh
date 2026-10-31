#!/usr/bin/env bash
set -euo pipefail

readonly repository_url='https://github.com/jaysonhurd/coding-preferences.git'
readonly destination="${PWD}/.codex"

if [[ ! -d "$destination" ]]; then
    printf 'Warning: no .codex directory exists in %s; nothing was installed.\n' "$PWD" >&2
    exit 1
fi

temporary_directory=$(mktemp -d)
trap 'rm -rf -- "$temporary_directory"' EXIT

git clone --depth 1 "$repository_url" "$temporary_directory/repository"

# Install repository contents, including dotfiles, without Git metadata.
rm -rf -- "$temporary_directory/repository/.git"
cp -R "$temporary_directory/repository/." "$destination/"

printf 'Installed coding preferences into %s\n' "$destination"
