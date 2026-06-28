# Task Breakdown: <feature title>

## Feature slug

`<feature-slug>`

## Sizing rule

Prefer boringly small tasks. A task should normally be implementable and reviewable by a local LLM in one focused session. If a task spans multiple architectural layers, split it unless those layers are inseparable for verification.

Before finalizing the task list, read `spec-planning-guide.md` and complete the
test matrix, behavior-bundling review, and fragility review below. The task
breakdown should make the split understandable to a human reviewer and concrete
enough for Bluefin to execute without product judgment.

## Test matrix

If the repo does not already have a strong test harness, task `001` should
normally create one. Define task-scoped checks before implementation starts.

| Task | Check command(s) | What the check proves | What proof must cover |
|------|------------------|-----------------------|------------------------|
| 001 | `<command>` | `<structure/behavior>` | `<Playwright/asciinema/N/A>` |

Test matrix rules:

- Project-wide static checks should enforce broad constraints such as forbidden
  APIs, dependency limits, required files, and generated/protected paths.
- Task-scoped checks should verify only behavior introduced up to that task, so
  unfinished later work does not fail earlier branches.
- Final aggregate checks should run all task checks.
- Any browser, visual, gesture, responsive, persistence, or workflow behavior
  that deterministic tests cannot prove must be assigned to proof.

## Behavior-bundling review

List any proposal areas that were split because they bundled too much behavior.

| Proposal area | Bundling risk | Resulting task split |
|---------------|---------------|----------------------|
| `<area>` | `<why one task is risky>` | `<tasks>` |

Split or narrow a task when it combines:

- form creation, validation, persistence, and deletion;
- animation plus state mutation;
- drag/drop plus filtering, statistics, or unrelated rendering;
- visual polish plus new behavior;
- multiple independent create/update/delete workflows;
- core implementation plus test harness creation, except for a scaffold task.

## Fragility review

Identify high-fragility tasks and the extra rules that make them local-LLM safe.

| Task | Fragility source | Mitigation in spec/checks/proof |
|------|------------------|----------------------------------|
| `<NNN>` | `<drag/drop/storage/date/etc.>` | `<deterministic rule/proof/check>` |

Treat these as high-fragility by default: drag/drop, gestures, animation timing,
browser storage, reload persistence, date/time comparison, responsive layout,
canvas/WebGL/media/file APIs, async network behavior, auth, migrations, secrets,
production data, and generated assets.

## Task list

| N | Task | Branch | PR target | Proof | Auto-merge eligible |
|---|------|--------|-----------|-------|---------------------|
| 001 | <task title> | `task/<feature-slug>-001-<task-slug>` | `feature/<feature-slug>` | Playwright/asciinema/N/A | yes/no |

## Human-test checkpoint

Stop for human preview testing when these tasks are merged into the feature branch:

- [ ] 001 <task title>

## Dedicated test tasks

Use this section only when separate test-focused tasks are useful.

- <test task>

## Re-splitting triggers

Manager should re-split or narrow a task if:

- review fails twice for related reasons;
- the development node repeats the same error;
- the task touches too many unrelated areas;
- verification cannot be run deterministically.
- the task needs more than one main proof video;
- the task contains multiple state machines or independent user workflows;
- a fragile browser/API/storage/date/animation task lacks deterministic rules,
  stable selectors/hooks, or explicit proof.
