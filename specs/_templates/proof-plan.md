# Proof Plan

## Feature

`<feature-slug>`

## Preview URL under test

`https://<feature-slug>.<preview-domain>`

## Proof policy

Proof should run against the same preview URL the human will test. Use dev/test backend resources defined by the project preview data policy.

## Decision matrix

Use Playwright when browser UI behavior, visual/touch behavior, screenshots, video, or preview URL behavior matter.

Use asciinema when CLI/API/server/deploy behavior, terminal setup, logs, or commands matter.

Use both when both browser behavior and terminal/API behavior matter.

Do not rely on terminal recordings alone to prove visual browser behavior.

Browser proof should include a console-error-free check unless the task is
explicitly not browser-facing.

## Task proof entries

| Task | Proof type | Command/script | Behavior proven | Artifact path/link | Required? | Status |
|------|------------|----------------|-----------------|--------------------|-----------|--------|
| 001 | playwright/asciinema/both/N/A | `<command>` | `<behavior>` | `specs/<feature-slug>/proof/tasks/001-<task-slug>/...` | yes/no | pending |

Each task with UI, interaction, visual layout, media generation, frontend state,
or user-facing workflow changes must define proof before implementation starts.
Use task-scoped folders:

```text
specs/<feature-slug>/proof/tasks/NNN-<task-slug>/
  screenshots/
  videos/
  logs/
  proof-result.md
```

For interactive UI proof, include an obvious click indicator in recordings when
possible, such as a visible ripple/circle at click coordinates or Playwright
mouse-trace overlay.

High-fragility tasks should include targeted proof:

- drag/drop or gestures: video or trace showing source, target, drop feedback,
  final state, and persistence if applicable;
- storage or reload behavior: before/after reload proof;
- date/time behavior: visible boundary case and the date used for the proof;
- responsive layout: desktop and narrow/mobile screenshots;
- animation/removal behavior: proof of both transition and final state;
- async/API behavior: success, failure, and loading/empty states when in scope.

Task PR proof artifacts must be linked from the Gitea task PR body or posted as
a task PR comment before the task can auto-merge into the feature branch.

## Feature-level recording

Describe the end-to-end feature behavior to record for human review. Store
feature-level proof separately from task proof:

```text
specs/<feature-slug>/proof/feature-final/
```

## Not-applicable exceptions

Record any tasks where proof is not applicable and explain why.
