# Proof Plan: Sorting Viz Test

## Feature preview target

Open the repository file directly:

```sh
open index.html
```

No build step should be required.

## Proof standards

- Command proof must include the command, machine, commit SHA, and output.
- UI proof should include screenshots or a short recording showing the relevant
  controls and bars.
- Any failed worker attempt, malformed response, skipped check, or scope
  reduction must be recorded in `specs/sorting-viz-test/issue-log.md`.

## Required feature-level proof

- Static/test proof:
  - `python3 tests/static_contract_check.py`
  - `python3 tests/algorithm_contract_check.py --all`
- Browser proof:
  - screenshot of initial loaded page;
  - screenshot or short recording of at least one algorithm running;
  - screenshot after completion showing sorted bars;
  - evidence that array size and speed controls work.

Feature-level proof artifacts are stored in:

```text
specs/sorting-viz-test/proof/feature-final/
```

## Task proof entries

Each task in `task-breakdown.md` lists its required tests. Reviewers should not
approve a task unless the task-specific tests either pass or the issue log
explains why proof could not be collected.

Future task proof should use task-scoped folders:

```text
specs/sorting-viz-test/proof/tasks/NNN-<task-slug>/
  screenshots/
  videos/
  logs/
  proof-result.md
```

This completed sorting-viz run has feature-level proof only. Per-task proof was
not captured because Loop Manager was still in dry-run PR mode and proof posting
was not yet a first-class task PR gate.
