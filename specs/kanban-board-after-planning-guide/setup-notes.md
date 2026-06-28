# Kanban Board Setup Notes

## Repo Layout

- Source prompt: `kanban.md`
- Build target: root `index.html`
- Tests target: root `tests/`
- Spec directory: `specs/kanban-board-after-planning-guide/`
- Completed sorting visualizer archive: `sorting-visualizer/`

## Loop Manager Expectations

- Feature branch should be `feature/kanban-board-after-planning-guide` if this
  comparison spec is run as a separate feature.
- Task branches should use
  `task/kanban-board-after-planning-guide-<NNN>-<slug>`.
- In Bluefin live mode, PlanContract `repo_url` should be the allowlisted local
  checkout path:

```text
/var/home/j/code/sorting-viz-test
```

- Remote worker clone/push handoff should continue to use
  `LOOP_MANAGER_WORKER_REPO_URL` from Bluefin's environment.
- Developer and code-review nodes should be local LLM workers.
- Local PR-Agent should run before task-branch merge.
- Codex PR-Agent should run before task-branch merge when integrated; if it is
  unavailable, record the reason and allow final feature review to catch issues
  before any merge to `main`.
- Final feature merge to `main` remains a human decision.

## Checks

The build should create these root-level checks:

```sh
python3 tests/static_contract_check.py
python3 tests/kanban_contract_check.py --all
```

Task specs use narrower checks such as:

```sh
python3 tests/kanban_contract_check.py --task 004
```

## Preview

The app is static and must work by directly opening `index.html`. For Playwright
proof convenience, a temporary static server may be used:

```sh
python3 -m http.server 4173
```

Proof must note whether it ran through `file://` or the temporary server.

## Spec Finalization Check

After this spec was drafted, the project-local wrapper was run:

```sh
.loop-manager/scripts/verify-spec-planning.sh
```

Result: passed, running the Loop Manager source tests through `uv`
(`103 passed, 1 warning`).

## Runtime Adjustment

- 2026-06-28: Oracle implementer timeout should be `900` seconds for this
  quality-first scaffold run.
- Task 001 uses `max_attempts: 2` so two implementation timeouts stop at
  `needs_human`; at that point, a frontier model should assess whether task 001
  is too broad or ambiguous and propose a narrower split before another run.

## Post-Failure Re-Split

- 2026-06-28: The first local run reached `needs_human` after two attempts on
  the original scaffold task. The rerun no longer hit the 300-second timeout,
  but Oracle returned prose instead of a usable file bundle/diff.
- The original scaffold task was split into:
  - `001` minimal app shell;
  - `002` static contract harness;
  - `003` Kanban task contract skeleton.
- The remaining behavior tasks were renumbered to `004` through `010`.
- Developer routing now recommends `oracle/fallback` for each task because the
  fallback profile is documented as the reliable bounded implementation model,
  while `oracle/normal` showed protocol noncompliance on this scaffold work.
