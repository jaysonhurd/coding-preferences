# Pull-request workflows

Use this source for `create pr` and `merge pr` in the personal command catalog.
These are GitHub workflows for the current task's changes, targeting the current
repository unless a repository path is supplied. An invocation authorizes branch
creation, staging, committing, pushing, and PR creation. Only `merge pr` authorizes
merging. Describing, documenting, or asking for help with these commands does not
execute them. Proceed with authorized actions without redundant confirmation.

## Prepare and publish

1. Read the target's instructions and inspect status, staged and unstaged diffs,
   untracked files, current branch, remotes, and recent commits. Establish the
   intended changes, GitHub repository, and base branch from the task and project
   conventions; otherwise use the remote's actual default branch. Ask only if
   change scope or remote/base selection remains ambiguous. Do not include
   unrelated local edits or commits, credentials, generated logs, or IDE files.
2. Verify Git and authenticated GitHub access, using an available connector or
   `gh` CLI, plus push and PR permissions. Report missing tools or access without
   installing tools or changing remote settings. Fetch the relevant base so the
   branch and PR diff can be checked against current remote state. Stop for
   unresolved Git operations or conflicts; preserve local changes.
3. Create a uniquely named descriptive branch with `git switch -c`. Choose its
   starting point so the PR contains only the intended task changes, preserving
   existing task commits when appropriate. Do not reset, discard unrelated work,
   rewrite shared history, or force-push. On a retry, inspect and reuse the branch
   and PR already created by this invocation instead of duplicating them.
4. Run the target's relevant formatting and documented checks. Resolve failures
   within the task's scope and rerun affected checks; report other blockers before
   publishing. Inspect the final diff, then use explicit paths with `git add`
   (or select hunks for mixed files). Inspect the entire staged diff before
   committing, including previously staged content. Preserve unrelated staged
   changes and never silently include them. Commit with a descriptive message
   following repository conventions. Do not create an empty commit: if intended
   changes are already committed, use those commits; if there is no task diff
   against the base, report that there is nothing to publish.
5. Push the branch with upstream tracking, for example `git push -u REMOTE BRANCH`.
   Check the complete base-to-head diff and commit list before opening the PR.
   Use explicit base and head branches and a descriptive title. Follow the
   repository's PR template and include the Markdown content below. With `gh`,
   write the body to a temporary Markdown file and pass `--body-file` to
   `gh pr create`; use a structured body argument with a connector. Preserve
   literal Markdown and newlines without shell interpolation, and remove the
   temporary file afterward. The PR body is the requested Markdown document;
   do not add a redundant document to the repository unless requested.

## PR Markdown document

Lead with a brief summary of the concrete problem and resulting behavior, then
provide details proportional to the change:

- **Summary:** short overview and motivation, with a before/after example if useful.
- **Changes:** implementation details, affected components, and significant
  design decisions or dependencies that help a reviewer assess the final diff.
- **Validation:** actual checks and outcomes, including checks not run and why.
  Never present unrun or pending checks as successful.
- **Risks and follow-up:** material limitations, compatibility, migration, or
  rollout concerns; state when none are known rather than inventing concerns.

Honor existing template sections and checkboxes. Describe the final implementation
for a reviewer who has not seen the conversation; omit abandoned approaches and
conversation history. Include both the concise summary and detailed explanation
in the same Markdown PR description.

## Finish according to the command

For `create pr`, return the branch, commit, PR URL, validation results, and any
pending checks. Leave the PR open. Do not merge or enable auto-merge, even if all
checks pass.

For `merge pr`:

1. Inspect the resulting PR's current head SHA, base, draft status, checks,
   mergeability, required reviews, and unresolved conversations. Wait for checks
   with bounded polling and brief progress updates. Required checks and local
   validation must pass for the exact head being merged. If no CI checks exist,
   report that limitation and rely on the documented local validation and actual
   repository rules; do not claim CI passed.
2. Keep the branch up to date as required by repository policy, using its accepted
   update strategy without force-pushing. If an update changes the head, rerun
   affected validation and wait for checks on that head. Stop on conflicts,
   failed checks, missing approvals, or other unresolved protections that cannot
   be resolved within scope. Report the PR URL and concrete blocker; never weaken
   protections, dismiss reviews, approve your own PR, or use an administrator
   bypass. Do not change repository settings as part of this command.
3. Merge using a method allowed by the repository and consistent with its history
   requirements (prefer squash if no convention exists). With `gh pr merge`, use
   `--match-head-commit` with the verified head SHA to avoid merging unverified
   changes. With another tool, use its equivalent head guard; if unavailable,
   use a supported method that enforces the verified head. A changed head requires
   revalidation. Do not substitute auto-merge for a completed merge.
4. Verify GitHub reports the PR as merged, then return the PR URL, branch, source
   commit, merge commit, and validation outcomes. Do not delete local or remote
   branches unless separately requested.

If publishing or merging fails, inspect the actual branch/PR state before any
retry. Stop when further progress requires new authorization, credentials,
external reviews, or resolving an out-of-scope failure. Report completed actions
and the next needed action without claiming success.
