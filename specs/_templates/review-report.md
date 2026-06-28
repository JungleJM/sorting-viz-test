# Local LLM Review Report

## Metadata

- Feature: `<feature-slug>`
- Task: `<NNN-task-slug>`
- PR: `<gitea-pr-url>`
- Reviewer role: code review node
- Reviewer node alias: `<node-alias>`
- Reviewer model: `<model-name-or-hint>`
- Developer node alias: `<node-alias>`
- Developer model: `<model-name-or-hint>`
- Review independence: `normal | degraded`
- Degraded reason, if any: `<same physical node, alternate model used, fallback reason>`

## Decision

`approve | revise | blocked`

## Blocking findings

1. `<finding id>` — <description>
   - Evidence:
   - Required change:

## Non-blocking findings

1. <description>

## Spec coverage

- [ ] Task acceptance criteria satisfied
- [ ] Tests match task requirements
- [ ] Proof requirement handled or justified
- [ ] Secret handling is safe
- [ ] Implementation fits project architecture

## Verification run

```sh
<commands run by reviewer>
```

Result:

## Residual risks

- <risk>

## Required next action

- `merge_task_pr`
- `request_development_revision`
- `manager_resplit_task`
- `stop_for_human`
