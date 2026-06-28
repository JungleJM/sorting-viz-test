# Spec Planning Guide

Use this guide before converting a proposal into task specs or a PlanContract.
The goal is to produce work units that local LLM workers can implement,
reviewers can verify, and Loop Manager can gate without guessing.

## Required Planner Outputs

Every feature plan should include:

- `feature-brief.md` describing the product goal, user-facing behavior,
  technical boundaries, quality bar, and completion definition.
- `task-breakdown.md` with small task slices, task split rationale,
  behavior-bundling review, fragility review, and task-scoped checks.
- `proof/proof-plan.md` describing browser, terminal, and final feature proof
  before implementation starts.
- `plan-contract.bluefin.yaml` or equivalent PlanContract with bounded goals,
  observable acceptance criteria, checks, allowed paths, forbidden paths, and
  risk flags.

At the end of spec-making, run:

```sh
.loop-manager/scripts/verify-spec-planning.sh
```

Record the result in `setup-notes.md` or the issue log. If this check fails,
fix the Loop Manager/templates issue before submitting the PlanContract to
Bluefin.

When the spec is ready to start, submit it with:

```sh
.loop-manager/scripts/submit-plan.sh --feature <feature-slug> -v
```

This discovers the PlanContract, runs verification, posts to Bluefin, and prints
dashboard/Paperclip URLs.

## Test Matrix Rule

If the target repo does not already have a strong test harness, task `001`
should normally create it before feature behavior starts.

Task `001` should define the whole feature's test matrix:

- project-wide static checks;
- task-scoped checks such as `--task NNN`;
- final aggregate checks such as `--all`;
- what each task check proves;
- what cannot be proven deterministically and must be covered by Playwright,
  asciinema, manual proof, or human review.

Tests should be deterministic from a clean checkout. They should fail with clear
messages naming the missing contract. Avoid placeholder tests and vague lines
like "add tests" unless a separate task defines exactly what those tests cover.

## Behavior-Bundling Review

Split by user behavior and risk, not by broad product nouns.

A task is probably too bundled if it combines:

- form creation, validation, persistence, and deletion;
- animation plus state mutation;
- drag/drop plus filtering or statistics;
- visual polish plus new business behavior;
- data model changes plus unrelated UI changes;
- multiple independent create/update/delete workflows;
- core implementation plus test harness creation, except for a scaffold task.

When in doubt, split the task so each branch has one primary user-visible
outcome and one clear verification path.

## Fragility Review

Mark tasks as higher-fragility when they involve:

- drag/drop, gestures, keyboard shortcuts, or pointer events;
- animation timing or delayed removal;
- browser storage, reload persistence, or offline behavior;
- date/time comparison;
- responsive layout, scrolling, or viewport-specific behavior;
- canvas, WebGL, media, files, clipboard, service workers, or browser APIs;
- async network calls, retries, cancellation, or partial failure;
- migrations, auth, permissions, secrets, or production data;
- generated assets or output that is hard to inspect with plain tests.

High-fragility tasks should be isolated. They should define deterministic
behavior rules, stable selectors or hooks for proof, edge cases, and explicit
Playwright/asciinema proof.

## Task Size Heuristics

A local-LLM-sized task should usually:

- be implementable and reviewable in one focused session;
- touch a small number of files or one coherent area;
- have one primary behavior outcome;
- have explicit out-of-scope items;
- include at least one edge case;
- include checks that can run on a clean checkout;
- include proof requirements when behavior is visual, interactive, or workflow
  based.

Re-split before implementation if the task needs more than one main proof video,
more than one state machine, or more than one independent reviewer question.

## Proof Planning Rule

Proof should be designed before implementation.

Use Playwright for browser UI behavior, visual/touch behavior, screenshots,
video, console checks, responsive layout, and preview URL behavior.

Use asciinema or terminal logs for CLI/API/server/deploy behavior, setup,
command execution, and check output.

Use both when a task has both browser behavior and terminal proof requirements.
Do not rely on terminal recordings alone to prove visual browser workflows.

## PlanContract Guidance

Keep the PlanContract small and executable. Put the most important planning
decisions into existing fields:

- `goal`: the bounded implementation outcome and explicit non-goals;
- `acceptance_criteria`: observable behavior and important edge cases;
- `checks`: deterministic commands Loop Manager can run;
- `allowed_paths` and `forbidden_paths`: scope boundaries;
- `risk_flags`: high-fragility or human-stop markers.

Do not ask Bluefin to make product decisions. Encode decisions in the task spec
or stop for human review.
