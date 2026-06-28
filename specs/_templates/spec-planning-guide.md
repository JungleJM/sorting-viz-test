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

Before assigning task models, query the Loop Manager runtime that will execute
the plan:

```sh
curl -fsS "$LOOP_MANAGER_API_URL/worker-models"
```

Use only worker/profile names from that inventory when writing
`recommended_worker` and `recommended_model_profile` in the PlanContract. If the
runtime cannot provide the inventory, stop and record the issue instead of
guessing a model name.

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

## Model Routing Rule

The frontier planner should recommend the developer worker/model profile for
each task. This is a planning judgment, not a hardcoded algorithm. Match the
task type to the available inventory:

- small, bounded code patches: prefer the proven reliable implementer profile;
- broad scaffolding or protocol-sensitive edits: prefer the most
  instruction-following coding profile, or split the task before assigning it;
- deep reasoning tasks: use a deeper model only when latency is acceptable and
  the task is already narrow;
- UI-heavy or experimental work: route only when the inventory marks that model
  suitable, and add stronger proof/check requirements.

Each PlanContract task should include:

- `recommended_worker`: the worker name from `/worker-models`;
- `recommended_model_profile`: the profile key from that worker;
- `fallback_policy`: what to do after repeated failure.

If a frontier developer fallback is available and allowed by policy, the
fallback policy may say to hand the task to the frontier model after local
attempts are exhausted. If a frontier developer fallback is not available, the
policy should say to return the failed task and failure artifact to frontier
planning for reassessment. The reassessment must choose one of:

- split the task into smaller tasks;
- keep the task but route it to a different available worker/model profile;
- stop for human review because the acceptance criteria or proof requirement is
  ambiguous.

Repeated protocol failures, such as no usable patch/file bundle, count as a
model-fit failure even when the task did not time out.

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
- `recommended_worker` and `recommended_model_profile`: planner-selected
  implementation route from `/worker-models`;
- `fallback_policy`: retry/re-route/frontier-reassessment rule after repeated
  failure;
- `risk_flags`: high-fragility or human-stop markers.

Do not ask Bluefin to make product decisions. Encode decisions in the task spec
or stop for human review.
