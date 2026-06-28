# Kanban Board Proof Plan

## Feature

`kanban-board-after-planning-guide`

## Preview Target

The app must work through `file://` by opening root `index.html` directly. For
Playwright convenience, proof may use:

```sh
python3 -m http.server 4173
```

If a static server is used, proof notes must still confirm direct-file browser
compatibility.

## Proof Policy

- Use Playwright screenshots or Playwright trace/video for browser workflow
  proof where possible.
- Use asciinema or terminal logs for command/check proof.
- Do not rely on terminal recordings alone for visual browser behavior.
- Browser proof should include a console-error-free check unless the task is not
  browser-facing.
- Clicks in recordings should be visible through a click ripple, mouse trace, or
  Playwright trace indicator.
- Post or link task proof artifacts on the task PR before merge.

## Task Proof Entries

| Task | Proof type | Command/script | Behavior proven | Artifact path/link | Required? | Status |
|------|------------|----------------|-----------------|--------------------|-----------|--------|
| 001 | Playwright/screenshot | inline `python3 -c` shell smoke | Minimal shell layout and narrow viewport. | `specs/kanban-board-after-planning-guide/proof/tasks/001-app-shell/` | yes | pending |
| 002 | Terminal | `python3 tests/static_contract_check.py` | Static contract checker runs and enforces project constraints. | `specs/kanban-board-after-planning-guide/proof/tasks/002-static-harness/` | yes | pending |
| 003 | Terminal | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 003` | Task-scoped Kanban harness exists and current contracts pass. | `specs/kanban-board-after-planning-guide/proof/tasks/003-kanban-contract-skeleton/` | yes | pending |
| 004 | Playwright | `python3 tests/kanban_contract_check.py --task 004` | Default data renders and reload persistence works. | `specs/kanban-board-after-planning-guide/proof/tasks/004-state-persistence/` | yes | pending |
| 005 | Playwright video | `python3 tests/kanban_contract_check.py --task 005` | Add, rename, delete empty column, prevent non-empty delete. | `specs/kanban-board-after-planning-guide/proof/tasks/005-columns/` | yes | pending |
| 006 | Playwright video/screenshots | `python3 tests/kanban_contract_check.py --task 006` | Add-card form, empty validation, valid create, badges. | `specs/kanban-board-after-planning-guide/proof/tasks/006-card-create-render/` | yes | pending |
| 007 | Playwright video/screenshots | `python3 tests/kanban_contract_check.py --task 007` | Description toggle, overdue marker, delete fade, reload deletion. | `specs/kanban-board-after-planning-guide/proof/tasks/007-card-details-delete/` | yes | pending |
| 008 | Playwright trace/video | `python3 tests/kanban_contract_check.py --task 008` | Drag/drop feedback, Done styling, persisted movement. | `specs/kanban-board-after-planning-guide/proof/tasks/008-drag-drop/` | yes | pending |
| 009 | Playwright video/screenshots | `python3 tests/kanban_contract_check.py --task 009` | Search, priority filter, placeholder gaps, stats updates. | `specs/kanban-board-after-planning-guide/proof/tasks/009-filter-stats/` | yes | pending |
| 010 | Playwright + terminal | `python3 tests/kanban_contract_check.py --all` | Final desktop/mobile/workflow proof and all checks. | `specs/kanban-board-after-planning-guide/proof/feature-final/` | yes | pending |

## Task Details

### 001 Minimal App Shell

- Desktop screenshot of initial shell.
- Narrow viewport screenshot proving horizontal board region does not break.
- Terminal log showing the inline shell smoke check passes.

### 002 Static Contract Harness

- Terminal log showing `python3 tests/static_contract_check.py` passes.
- Short note describing what the static check enforces.

### 003 Kanban Task Contract Skeleton

- Terminal log showing static check and `--task 003` pass.
- Short note mapping task numbers to contract functions.

### 004 State And Persistence

- Screenshot of default cards across all four columns.
- Reload proof showing localStorage state restored.
- Console-error-free browser proof.

### 005 Column Management

- Recording: add column, rename column, delete empty column.
- Screenshot or recording of non-empty column delete prevention.
- Console-error-free browser proof.

### 006 Card Creation And Rendering

- Recording: open add-card form, attempt empty save, add valid card with
  priority/due date, cancel another form.
- Screenshot showing Low/Medium/High badges.
- Console-error-free browser proof.

### 007 Card Details, Overdue State, And Delete

- Recording: add overdue card with description, expand details, delete card.
- Screenshot of overdue styling.
- Reload proof that deleted card remains gone.
- Console-error-free browser proof.

### 008 Drag And Drop

- Recording: drag card from `To Do` to `In Progress`, then to `Done`.
- Screenshot or trace frame showing drop-zone highlight.
- Screenshot showing Done styling.
- Reload proof that moved card membership/order persists.
- Console-error-free browser proof.

### 009 Filtering And Stats

- Recording: search by title, filter by priority, clear filters.
- Screenshot of stats bar with non-zero total, overdue, done, and completion.
- Screenshot or trace frame showing placeholder gaps for hidden filtered cards.
- Console-error-free browser proof.

### 010 Final Feature Proof

- Desktop screenshot.
- Narrow/mobile screenshot.
- Final recording covering add card, filter, drag to Done, stats update, and
  persistence after reload.
- Terminal log showing all checks pass.

## Failure Proof

If any task reaches `needs_human`, Loop Manager must write:

```text
specs/kanban-board-after-planning-guide/failure-artifacts/<task-id>-local-failure-summary.md
```

That artifact should be attached or linked to the task PR or issue log.
