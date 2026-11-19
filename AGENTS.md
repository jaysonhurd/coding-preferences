# Repository instructions

- Read [repository guidance](.agents/REPOSITORY.md) before working on this repository. It describes the layout, editing conventions, and checks to run after changes.
- Use the [file guide](.agents/FILES.md) when selecting a skill, reference, or template. It lists every file shipped in the preference bundle and explains when each applies.

Any harness can follow these Markdown links directly.

## Installed project task map

Paths below start at the target project root after running `install.sh`. Open the file for the task at hand. The installer links the four skill directories under `.agents/skills/` and copies the supporting documents into `.agents/coding-preferences/`.

| When working on… | Open this installed path |
| --- | --- |
| Go language, style, testing, logging, or other Go conventions | `.agents/skills/initialize-go/SKILL.md` |
| Effective Go examples or the article’s license | `.agents/skills/initialize-go/EFFECTIVE_GO.md` |
| Go scaffolding assets | `.agents/skills/initialize-go/assets/templates/.gitkeep` only marks a reserved directory. |
| Help selecting or invoking a workflow | `.agents/skills/agent-help/SKILL.md` |
| A named command or preference | `.agents/skills/agent-help/COMMANDS.md` for its syntax and scope |
| Applying all applicable preferences | `.agents/skills/agent-help/UPDATE_ALL.md` |
| Creating or merging a pull request | `.agents/skills/agent-help/PULL_REQUESTS.md` |
| Setting up or reviewing repository checks and CI | `.agents/skills/repository-validation/SKILL.md` |
| Setting up Spec Kit or reviewing existing Spec Kit guidance | `.agents/skills/spec-kit/SKILL.md` |
| Writing or amending a Spec Kit constitution | `.agents/skills/spec-kit/assets/constitution-principles.md` |
| Documenting the project's Spec Kit workflow | `.agents/skills/spec-kit/assets/readme-section.md` |
| Choosing development defaults for a project | `.agents/coding-preferences/docs/development-preferences.md` |
| Drafting project-specific Go instructions | `.agents/coding-preferences/templates/go-project/AGENTS.md` |
| Installation, updates, or command examples | `.agents/coding-preferences/README.md` |
| Checking terms for reuse or redistribution | `.agents/coding-preferences/LICENSE` |
| Looking up any file in the installed bundle | `.agents/coding-preferences/.agents/FILES.md` |
| Maintaining the preference sources | `.agents/coding-preferences/AGENTS.md` is the source entry point. Read `.agents/coding-preferences/.agents/REPOSITORY.md` for editing rules and checks. |

If a project already has a skill at one of these paths, consult that skill's own instructions. The bundled version is available at the same relative path under `.agents/coding-preferences/skills/`. For project-specific instructions, follow the project's root guidance.
