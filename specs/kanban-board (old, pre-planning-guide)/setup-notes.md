# Kanban Board Setup Notes

## Repo Layout

- New Kanban prompt: `kanban.md`
- New build target: root `index.html`
- New tests target: root `tests/`
- Kanban specs: `specs/kanban-board/`
- Completed sorting visualizer archive: `sorting-visualizer/`

## Loop Manager Expectations

- The feature branch should be `feature/kanban-board`.
- Task branches should use `task/kanban-board-<NNN>-<slug>`.
- Developer and code-review nodes should be local LLM workers.
- Codex should be used for PR-Agent review, not developer or code-review roles,
  unless a future run explicitly changes `codex_role_policy`.
- Local PR-Agent should run before task-branch merge.
- Codex PR-Agent should run when integrated/configured.
- Final feature merge to `main` remains a human decision.

## Checks

The build should create these root-level checks:

```sh
python3 tests/static_contract_check.py
python3 tests/kanban_contract_check.py --all
```

Task specs use narrower `--task NNN` checks where useful.

## Preview

The app is static and should work by directly opening `index.html`. For proof
automation, a temporary static server may be used:

```sh
python3 -m http.server 4173
```
