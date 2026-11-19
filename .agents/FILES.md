# File guide

Use this index to choose the file for the current task. Open the Markdown links directly in any editor or agent. In an installed project the links resolve inside `.agents/coding-preferences/`. The project's own requirements and conventions take precedence over reusable defaults.

| File | When to use it |
| --- | --- |
| [AGENTS.md](../AGENTS.md) | Start here when maintaining the coding-preferences source repository. |
| [.agents/REPOSITORY.md](REPOSITORY.md) | Read before editing the source repository. It defines layout, maintenance rules, and required checks. In a target project, consult its guidance responsibilities section when organizing Spec Kit files. |
| [.agents/FILES.md](FILES.md) | Use this index when selecting a workflow or identifying an installed file. |
| [README.md](../README.md) | Consult for install, update, skill discovery, and examples of chat requests. |
| [LICENSE](../LICENSE) | Consult before reusing or redistributing the bundle. The Effective Go article carries its own notice. |
| [docs/development-preferences.md](../docs/development-preferences.md) | Consult when applying development defaults or setting up validation in a target project. |
| [skills/agent-help/SKILL.md](../skills/agent-help/SKILL.md) | Open for help, command lookup, or routing a selected request. |
| [skills/agent-help/COMMANDS.md](../skills/agent-help/COMMANDS.md) | Look up a command's spelling, scope, and source before applying or reviewing a preference. |
| [skills/agent-help/UPDATE_ALL.md](../skills/agent-help/UPDATE_ALL.md) | Follow when asked to apply all applicable preferences to a project. |
| [skills/agent-help/PULL_REQUESTS.md](../skills/agent-help/PULL_REQUESTS.md) | Follow for a requested pull request. Merge only when requested. |
| [skills/initialize-go/SKILL.md](../skills/initialize-go/SKILL.md) | Consult for Go conventions or a selected Go topic. Full project scaffolding is unfinished. |
| [skills/initialize-go/EFFECTIVE_GO.md](../skills/initialize-go/EFFECTIVE_GO.md) | Use the local article for Effective Go guidance. Consult its notice before redistribution. |
| [skills/initialize-go/assets/templates/.gitkeep](../skills/initialize-go/assets/templates/.gitkeep) | Empty placeholder that preserves the templates directory in Git. It contains no instructions. |
| [skills/repository-validation/SKILL.md](../skills/repository-validation/SKILL.md) | Open when setting up, reviewing, or running project validation and matching CI. |
| [skills/spec-kit/SKILL.md](../skills/spec-kit/SKILL.md) | Open for requested Spec Kit setup or a selected review of existing guidance. Follow the scope of the request. |
| [skills/spec-kit/assets/constitution-principles.md](../skills/spec-kit/assets/constitution-principles.md) | Adapt applicable principles when creating or amending a project's Spec Kit constitution. |
| [skills/spec-kit/assets/readme-section.md](../skills/spec-kit/assets/readme-section.md) | Adapt when documenting a project's Spec Kit setup and feature workflow. |
| [templates/go-project/AGENTS.md](../templates/go-project/AGENTS.md) | Use when drafting Go project guidance. Fill in the project's actual commands and conventions before linking to it. |

In an installed project, `.agents/skills/agent-help/`, `initialize-go/`, `repository-validation/`, and `spec-kit/` under the same skills directory normally link to the corresponding bundle directories above. Each file through a link has the same use as its source. If a project already supplied a skill at that location, read its own SKILL.md for its scope. For generated `speckit-*` workflows, follow the installed integration's instructions for the requested feature stage.

When adding a project-owned file under `.agents/`, add its path and when to use it to the project's root pointer or a linked project index. Keep shared project guidance accessible by path to every harness.
