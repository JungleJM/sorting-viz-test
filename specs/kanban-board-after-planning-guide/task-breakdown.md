# Kanban Board Task Breakdown

Tasks are sized for local-LLM implementation and review. Each task should be
implemented on its own task branch and reviewed against this spec.

## Feature Slug

`kanban-board-after-planning-guide`

## Sizing Rule

Each task has one primary behavior outcome and one clear verification path.
Fragile work such as validation, animation, persistence, date comparison, and
native drag/drop is isolated or given deterministic rules before implementation.

## Test Matrix

| Task | Check command(s) | What the check proves | What proof must cover |
|------|------------------|-----------------------|------------------------|
| 001 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 001` | App shell, required sections, project constraints, and task-check harness exist. | Desktop/narrow shell screenshots and terminal check output. |
| 002 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 002` | State model, default columns/cards, storage key, restore/save hooks, render-from-state flow. | Default board screenshot and reload persistence proof. |
| 003 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 003` | Column add, inline rename, empty-delete guard, non-empty warning, persistence after column changes. | Add/rename/delete recording and non-empty delete warning. |
| 004 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 004` | Per-column add-card form, title validation, card schema, priority/due-date rendering, persistence after create. | Add-card workflow, empty-title validation, priority badge screenshot. |
| 005 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 005` | Description toggle, overdue comparison, warning marker, delete handler, fade-out fallback, stale-ID cleanup. | Expand/delete workflow, overdue styling, deleted-card reload proof. |
| 006 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 006` | Native drag/drop handlers, stable data attributes, deterministic move rule, Done styling, persistence after drop. | Drag recording, drop-zone highlight, Done styling, reload proof. |
| 007 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 007` | Search, priority filtering, placeholder gaps, stats formulas, fixed stats bar, live updates after changes. | Filter/stat workflow and fixed stats screenshot. |
| 008 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --all` | All contracts, accessibility labels, responsive styling, no forbidden APIs/libraries, final proof paths. | Desktop/mobile/final workflow recording. |

## Behavior-Bundling Review

| Proposal area | Bundling risk | Resulting task split |
|---------------|---------------|----------------------|
| Cards | Original card requirement includes form, validation, schema, badges, description toggle, overdue dates, hover delete, animation, and persistence. | Task 004 creates/renders cards; task 005 handles description, overdue, and delete animation. |
| Drag/drop | Native browser drag/drop is fragile and depends on stable cards, columns, state, and persistence. | Task 006 runs after column and card behavior is complete. |
| Filtering/statistics | Filtering and stats depend on created/deleted/moved card state. | Task 007 runs after drag/drop and delete behavior. |
| Visual polish | Styling can hide broken behavior if done too early. | Task 008 is final polish and proof after all behavior exists. |
| Tests | Later workers need stable contracts before implementation. | Task 001 creates the harness and full task-scoped test matrix. |

## Fragility Review

| Task | Fragility source | Mitigation in spec/checks/proof |
|------|------------------|----------------------------------|
| 001 | Tests could be shallow or overfit to early HTML. | Require real helper assertions, task functions, clear failures, and checks for selectors/hooks used by later proof. |
| 004 | Form validation and persistence can be partial. | Require empty-title validation, stable schema, and persistence checks after create. |
| 005 | Date comparison and delete animation are timing-sensitive. | Require local-date comparison rule, visible overdue marker, bounded delete fallback, and reload proof. |
| 006 | Native drag/drop is browser-fragile. | Require stable `data-*` selectors, deterministic append/drop ordering, cleanup paths, Playwright proof, and persistence proof. |
| 007 | Filtered DOM can break stats or layout. | Require placeholder class, live stat update hooks, and proof after filtering. |
| 008 | Responsive and polish can regress behavior. | Run `--all`, require desktop/mobile screenshots, and prohibit new behavior except polish/accessibility fixes. |

## Tasks

### 001 Scaffold Single-File App And Test Harness

Create the root `index.html` skeleton and deterministic test harness.

Implementation:
- Create `index.html` with semantic app shell, top toolbar, board region, fixed
  stats bar placeholders, and inline CSS/JS.
- Add comments or section markers for State, Rendering, Persistence, Column
  Actions, Card Actions, Drag and Drop, Filtering, Statistics, and Utilities.
- Load Inter from Google Fonts.
- Add `tests/static_contract_check.py`.
- Add `tests/kanban_contract_check.py`.
- Tests must parse `index.html` and fail with clear messages.
- Static checks must enforce single root app target, no external JavaScript
  libraries, no `prompt()`/`alert()`/`confirm()`, required sections, Inter font,
  and no writes to `sorting-visualizer/`.
- Kanban checks must support `--task 001` through `--task 008` and `--all`,
  with one function per task.
- Browser behavior that static tests cannot prove should be represented by
  stable selectors, data attributes, storage keys, named handlers, or proof
  requirements.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 001`

Proof:
- Desktop screenshot of initial shell.
- Narrow viewport screenshot proving horizontal board region does not break.
- Terminal proof showing the task checks pass.

### 002 Board State, Default Data, And Persistence

Implement initial state, default columns/cards, localStorage restore/save, and
state-driven rendering.

Implementation:
- Define a state object with columns, card records, and card order by column.
- Use stable IDs for columns and cards.
- Populate example cards across all four default columns when storage is empty.
- Use one documented localStorage key.
- Restore full board state on load.
- Save after every state-changing action introduced in this task.
- Render columns and cards from state only.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 002`

Proof:
- Screenshot of default cards across all four columns.
- Console-error-free reload proof showing state restored.

### 003 Column Management

Implement adding, renaming, and deleting empty columns.

Implementation:
- Add the end-of-board `+ Add Column` control.
- Create custom columns with stable IDs and sensible default names.
- Rename any column by double-clicking its header using an inline editor.
- Show a trash icon/control on column hover.
- Delete only empty columns.
- Show a visible non-blocking message when deleting a non-empty column is
  attempted.
- Save state after add, rename, and successful delete.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 003`

Proof:
- Short recording: add a column, rename it, delete it.
- Screenshot or recording of non-empty column delete prevention.

### 004 Card Creation And Card Rendering

Implement inline card creation and basic card display.

Implementation:
- Add `+ Add card` at the bottom of every column.
- Show an inline mini-form with required title, priority selector, due date
  picker, optional description textarea, Save, and Cancel.
- Validate title before saving; keep the form open and show an inline message
  when title is empty.
- Create card records with stable ID, column ID, title, priority, due date,
  description, and ordering.
- Save to localStorage after successful create.
- Render Low/Medium/High priority badges with distinct colors.
- Render due date in a consistent metadata area.
- Render description content collapsed by default, but defer expand/collapse
  behavior to task 005.
- Provide stable selectors/data attributes for forms and card fields.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 004`

Proof:
- Recording: open form, attempt empty save, add valid card, cancel another form.
- Screenshot of Low/Medium/High priority badges.

### 005 Card Details, Overdue State, And Delete

Implement secondary card behavior after cards can already be created.

Implementation:
- Make optional descriptions expandable/collapsible below the title.
- Description toggles must be keyboard reachable and clearly labelled.
- Compare due dates against today's local date using date-only comparison.
- Mark overdue due dates in red with a warning icon or clear warning marker.
- Show card delete control on hover/focus.
- Delete removes the card with a fade-out animation.
- Delete must update state, remove stale card IDs from column order, save to
  localStorage, and have a bounded fallback if animation events do not fire.
- Empty card areas remain visually stable after deleting the last card.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 005`

Proof:
- Recording: add overdue card with description, expand details, delete a card.
- Screenshot of overdue styling.
- Reload proof that the deleted card remains gone.

### 006 Native Drag And Drop

Implement native HTML5 drag/drop movement between columns and Done styling.

Implementation:
- Make cards draggable with native HTML5 Drag and Drop API.
- Add stable `data-card-id` and `data-column-id` attributes.
- Highlight target columns with a visible drop-zone indicator while dragging.
- Support dropping into empty and populated columns.
- Use deterministic append-to-destination ordering for drops unless a later
  human-approved task asks for precise between-card insertion.
- Moving to `Done` applies muted styling and strikethrough title.
- Moving out of `Done` removes Done styling.
- Persist column membership and order after each drop.
- Clean up drag state after successful drop, cancelled drag, and invalid target.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 006`

Proof:
- Recording: drag a card from `To Do` to `In Progress`, then to `Done`.
- Screenshot or trace frame showing drop-zone highlight.
- Screenshot showing Done styling.
- Reload proof that moved card membership/order persists.

### 007 Search, Priority Filter, And Statistics

Implement filtering and the fixed bottom statistics bar.

Implementation:
- Search filters cards by title, case-insensitive.
- Priority dropdown supports All, Low, Medium, High.
- Filtered-out cards are hidden but leave placeholder space so column height
  does not jump.
- Statistics update live: total cards, overdue cards, done cards, completion
  rate.
- Completion rate is `Done / Total * 100`, with zero-card handling.
- Stats bar remains fixed at the bottom and does not hide controls/content.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 007`

Proof:
- Recording: search, apply priority filter, clear filters, observe stats.
- Screenshot of fixed stats bar after cards are filtered.

### 008 Visual Polish, Responsiveness, Accessibility, And Final Proof

Finalize styling, responsive behavior, accessibility labels, and full proof.

Implementation:
- Dark charcoal/slate theme.
- Frosted-glass column panels with subtle borders and shadow.
- Smooth transitions for card hover lift, drag opacity, drop pulse, and delete
  fade-out.
- Horizontal board scrolling on small screens without layout breakage.
- Buttons and icon-only controls have accessible labels or titles.
- No browser `prompt()`/`alert()`/`confirm()` usage.
- No external JavaScript libraries.
- Final cleanup of comments and structure without changing core behavior.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --all`

Proof:
- Desktop screenshot.
- Mobile/narrow screenshot.
- Final recording covering add card, filter, drag to Done, stats update, and
  persistence after reload.

## Human-Test Checkpoint

Stop for human preview/testing after task 008 passes checks and final proof is
recorded.

## Re-Splitting Triggers

Manager should stop and re-split if:

- a task fails twice for the same behavior;
- a local worker weakens checks or removes proof hooks;
- native drag/drop cannot be made deterministic;
- proof cannot be captured without changing the product behavior;
- task 004 or 005 expands into unrelated card features;
- task 008 introduces new behavior instead of polish/accessibility only.
