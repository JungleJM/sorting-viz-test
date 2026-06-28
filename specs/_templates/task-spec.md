# Task Spec: <NNN task title>

## Task slug

`<short-task-slug>`

## Parent feature

`<feature-slug>`

## Branches

- Base branch: `feature/<feature-slug>`
- Task branch: `task/<feature-slug>-NNN-<task-slug>`
- Task PR target: `feature/<feature-slug>`

## Manager intent

State the specific outcome the development node must produce.

## Scope

### In scope

- <bounded implementation item>

### Out of scope

- <explicit non-goal>

## Expected files or areas

- `<path or area>` — <expected change>

## Implementation requirements

- <requirement>

## Fragility and split rationale

- Fragility level: low/medium/high
- Fragility sources: `<drag/drop/storage/date/responsive/animation/API/etc.>`
- Why this task is small enough: `<one primary behavior and one verification path>`
- Deferred behavior: `<related behavior intentionally left to another task>`
- Deterministic rules:
  - `<rule that removes ambiguity for local workers>`

## Tests to add or update

- <test file or command> — <behavior to prove>

## Test design notes

- Task-scoped check: `<command such as python3 tests/contract.py --task NNN>`
- This check should prove:
  - `<observable structure or behavior>`
- This check should not require:
  - `<future task behavior or unavailable service>`
- If behavior is hard to test deterministically, expose stable selectors,
  command hooks, data attributes, logs, storage keys, or fixtures for proof.

## Verification commands

```sh
<project test command>
```

## Proof requirement

Choose one:

- `playwright_required`: browser/UI behavior must be proven against the preview URL.
- `asciinema_required`: terminal/API/server/deploy behavior must be proven.
- `both_required`: both browser and terminal proof are needed.
- `not_applicable`: explain why proof is not meaningful for this tiny task.

Reason:

## Proof design

Fill this before implementation. The breakdown/frontier model should decide this
from the task scope:

- Proof folder: `specs/<feature-slug>/proof/tasks/NNN-<task-slug>/`
- Browser console:
  - `must be error-free`: yes/no/not applicable
- Required screenshots:
  - `<name>` — <state/layout to show>
- Required video:
  - `<name>` — <interaction/workflow to show>
- Required reload/persistence proof:
  - `<state to prove after reload>` or not applicable
- Click visibility:
  - `required`: yes/no
  - Method: visible click ripple, mouse trace overlay, or not applicable reason
- Required command logs:
  - `<command>` — <behavior proven>
- Gitea PR posting:
  - [ ] proof artifacts linked in task PR body
  - [ ] proof summary posted as task PR comment

Use proof type `not_applicable` only for tasks where visual/interactive proof
would add no information beyond deterministic tests. Explain why.

## Acceptance criteria

- [ ] <criterion>

## Auto-merge eligibility

Task PR may auto-merge into the feature branch only when:

- [ ] tests passed
- [ ] secret scan passed
- [ ] code review node decision is `approve`
- [ ] Codex/OpenAI PR review decision is `approve`
- [ ] local PR-Agent decision is `approve`
- [ ] no blocking findings remain
- [ ] required proof is recorded or explicitly not applicable
- [ ] task acceptance criteria are satisfied

If both local PR-Agent and Codex/OpenAI PR-Agent cannot run, do not auto-merge
by default. Prefer obtaining the Codex/OpenAI PR review first because it is the
higher-quality independent reviewer. Record exactly why local PR-Agent was
unable to run, including missing model, worker timeout, malformed output,
authentication failure, or unavailable host.

## Needs-human failure artifact

If this task reaches `needs_human`, Loop Manager must write:

`specs/<feature-slug>/failure-artifacts/<task-id>-local-failure-summary.md`

That artifact is required even when no Codex fallback is allowed. If Codex
fallback is allowed for developer or code-review, the fallback must restart from
a clean base and use the artifact as memory rather than continuing from the
failed local code.

## Notes for code review node

Focus review on spec compliance, edge cases, tests, secret handling, and integration risk.

## Notes for PR agents

Local PR-Agent and Codex PR-Agent review the opened task PR against the whole
repo, not only the files mentioned in the task. They should look for integration
breakage, missing tests, brittle proof, secret leaks, and regressions outside
the task's narrow acceptance criteria.

When only one PR-Agent path is available, use Codex/OpenAI first. Local PR-Agent
is useful as an additional independent pass, but it must not block getting a
frontier review unless the project explicitly requires local-only review.
