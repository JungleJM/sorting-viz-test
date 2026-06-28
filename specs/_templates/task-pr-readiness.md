# Task PR Readiness

## Task PR

- Feature: `<feature-slug>`
- Task: `<NNN-task-slug>`
- PR URL: `<gitea-pr-url>`
- Base: `feature/<feature-slug>`
- Head: `task/<feature-slug>-NNN-<task-slug>`

## Required gates

- [ ] Implementation committed and pushed
- [ ] Task tests passed
- [ ] Build/typecheck/lint passed as applicable
- [ ] Secret scan passed
- [ ] Local-LLM code review decision: `approve`
- [ ] Codex/OpenAI PR review decision: `approve`
- [ ] Blocking findings: none
- [ ] Proof artifact recorded or not-applicable reason accepted
- [ ] PR body includes summary, verification, and secret-handling statement

## Auto-merge decision

`eligible | not_eligible`

Reason:

## Merge action

Task PR may merge into the feature branch only if eligible. Feature branch must not merge into `main` automatically.
