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
