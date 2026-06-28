# Kanban Board Task Breakdown

Tasks are sized for local-LLM implementation and review. Each task should be
implemented on its own task branch and reviewed against this spec.

## Feature Slug

`kanban-board-after-planning-guide`

## Sizing Rule

Each task has one primary behavior outcome and one clear verification path.
Fragile work such as validation, animation, persistence, date comparison, and
native drag/drop is isolated or given deterministic rules before implementation.

After the first local run, the original scaffold task failed twice without a
usable file bundle. The scaffold work is now split into three smaller tasks:
minimal app shell, static contract harness, and Kanban task-contract skeleton.

## Test Matrix

| Task | Check command(s) | What the check proves | What proof must cover |
|------|------------------|-----------------------|------------------------|
| 001 | `python3 -c "from pathlib import Path; html=Path('index.html').read_text(); assert 'id=\"app\"' in html; assert 'data-board' in html; assert 'data-stats-bar' in html; assert 'fonts.googleapis.com' in html"` | Minimal app shell exists with required root hooks and font. | Desktop/narrow shell screenshots. |
| 002 | `python3 tests/static_contract_check.py` | Static contract harness exists and checks the shell/project constraints. | Terminal check output and note of enforced contracts. |
| 003 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 003` | Kanban task-check harness supports task-scoped checks without failing unfinished future work. | Terminal check output and task-check matrix note. |
| 004 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 004` | State model, default columns/cards, storage key, restore/save hooks, render-from-state flow. | Default board screenshot and reload persistence proof. |
| 005 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 005` | Column add, inline rename, empty-delete guard, non-empty warning, persistence after column changes. | Add/rename/delete recording and non-empty delete warning. |
| 006 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 006` | Per-column add-card form, title validation, card schema, priority/due-date rendering, persistence after create. | Add-card workflow, empty-title validation, priority badge screenshot. |
| 007 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 007` | Description toggle, overdue comparison, warning marker, delete handler, fade-out fallback, stale-ID cleanup. | Expand/delete workflow, overdue styling, deleted-card reload proof. |
| 008 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 008` | Native drag/drop handlers, stable data attributes, deterministic move rule, Done styling, persistence after drop. | Drag recording, drop-zone highlight, Done styling, reload proof. |
| 009 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --task 009` | Search, priority filtering, placeholder gaps, stats formulas, fixed stats bar, live updates after changes. | Filter/stat workflow and fixed stats screenshot. |
| 010 | `python3 tests/static_contract_check.py`; `python3 tests/kanban_contract_check.py --all` | All contracts, accessibility labels, responsive styling, no forbidden APIs/libraries, final proof paths. | Desktop/mobile/final workflow recording. |

## Behavior-Bundling Review

| Proposal area | Bundling risk | Resulting task split |
|---------------|---------------|----------------------|
| Scaffolding/tests | The original task combined app shell, static test design, future task matrix, selectors, and proof hooks. A local model returned prose instead of a file bundle twice. | Tasks 001, 002, and 003 split shell, static checker, and Kanban task-check skeleton. |
| Cards | Original card requirement includes form, validation, schema, badges, description toggle, overdue dates, hover delete, animation, and persistence. | Task 006 creates/renders cards; task 007 handles description, overdue, and delete animation. |
| Drag/drop | Native browser drag/drop is fragile and depends on stable cards, columns, state, and persistence. | Task 008 runs after column and card behavior is complete. |
| Filtering/statistics | Filtering and stats depend on created/deleted/moved card state. | Task 009 runs after drag/drop and delete behavior. |
| Visual polish | Styling can hide broken behavior if done too early. | Task 010 is final polish and proof after all behavior exists. |

## Fragility Review

| Task | Fragility source | Mitigation in spec/checks/proof |
|------|------------------|----------------------------------|
| 001 | App shell can drift from later test selectors. | Require stable root hooks and section markers only; no behavior implementation. |
| 002 | Static tests can be shallow or too strict. | Require clear failure messages and project-wide checks only. |
| 003 | Future task checks can fail before behavior exists. | Require future contracts to be explicit but only strict when their task is run. |
| 006 | Form validation and persistence can be partial. | Require empty-title validation, stable schema, and persistence checks after create. |
| 007 | Date comparison and delete animation are timing-sensitive. | Require local-date comparison rule, visible overdue marker, bounded delete fallback, and reload proof. |
| 008 | Native drag/drop is browser-fragile. | Require stable `data-*` selectors, deterministic append/drop ordering, cleanup paths, Playwright proof, and persistence proof. |
| 009 | Filtered DOM can break stats or layout. | Require placeholder class, live stat update hooks, and proof after filtering. |
| 010 | Responsive and polish can regress behavior. | Run `--all`, require desktop/mobile screenshots, and prohibit new behavior except polish/accessibility fixes. |

## Model Routing Review

The target Loop Manager runtime exposes model inventory at `/worker-models`.
Planner-selected developer routing for this plan uses `oracle/fallback` because
the failed task showed protocol noncompliance from `oracle/normal`, while the
fallback profile is documented as the proven reliable implementation fallback
for bounded coding tasks.

| Task | Recommended worker/profile | Why this model fits | Fallback after repeated failure |
|------|----------------------------|---------------------|----------------------------------|
| 001 | `oracle/fallback` | Tiny static shell patch; needs instruction following more than deep reasoning. | Frontier re-split if no usable file bundle appears twice. |
| 002 | `oracle/fallback` | Bounded Python checker file. | Frontier narrows static contracts. |
| 003 | `oracle/fallback` | Bounded Python checker skeleton. | Frontier separates current smoke checks from future contracts. |
| 004 | `oracle/fallback` | Bounded state/persistence implementation. | Frontier reviews state-shape ambiguity or model fit. |
| 005 | `oracle/fallback` | Bounded column workflow. | Frontier splits add/rename/delete if bundled. |
| 006 | `oracle/fallback` | Bounded card creation/rendering. | Frontier splits validation from rendering/persistence. |
| 007 | `oracle/fallback` | Fragile date/animation work, but scoped after cards exist. | Frontier splits details, overdue, and delete. |
| 008 | `oracle/fallback` | Fragile drag/drop isolated after state/cards are stable. | Frontier splits drag feedback from state movement or takes over if allowed. |
| 009 | `oracle/fallback` | Bounded filtering/stat formulas. | Frontier splits filtering from stats. |
| 010 | `oracle/fallback` | Polish/proof pass with no new core behavior. | Frontier separates polish defects from proof-artifact defects. |

## Tasks

### 001 Minimal App Shell

Create only the root `index.html` skeleton.

Implementation:
- Create `index.html` with semantic app shell, top toolbar, board region, fixed
  stats bar placeholders, and inline CSS/JS placeholders.
- Add stable selectors/data attributes for app root, toolbar, board, columns
  region, stats bar, and proof hooks.
- Add comments or section markers for State, Rendering, Persistence, Column
  Actions, Card Actions, Drag and Drop, Filtering, Statistics, and Utilities.
- Load Inter from Google Fonts.
- Do not implement Kanban behavior beyond inert placeholders.

Checks:
- `python3 -c "from pathlib import Path; html=Path('index.html').read_text(); assert 'id=\"app\"' in html; assert 'data-board' in html; assert 'data-stats-bar' in html; assert 'fonts.googleapis.com' in html"`

Proof:
- Desktop screenshot of initial shell.
- Narrow viewport screenshot proving horizontal board region does not break.

### 002 Static Contract Test Harness

Create the project-wide static checker only.

Implementation:
- Add `tests/static_contract_check.py`.
- Use only Python standard library modules.
- Parse `index.html` and fail with clear messages.
- Enforce single root app target, no external JavaScript libraries, no
  `prompt()`/`alert()`/`confirm()`, required sections, Inter font, and no writes
  to `sorting-visualizer/`.
- Do not add the Kanban task-check file in this task.
- Do not implement board behavior.

Checks:
- `python3 tests/static_contract_check.py`

Proof:
- Terminal proof showing the static check passes.
- Short note describing what the static check enforces.

### 003 Kanban Task Contract Skeleton

Create the task-scoped Kanban checker without requiring unfinished behavior.

Implementation:
- Add `tests/kanban_contract_check.py`.
- Support `--task 001` through `--task 010` and `--all`.
- Use one named function per task.
- Checks for tasks 001 through 003 should pass against the current shell and
  harness.
- Future task checks should be explicit enough to guide implementation, but
  should only become strict when that task is run.
- Browser behavior that static tests cannot prove should be represented by
  stable selectors, data attributes, storage keys, named handlers, or proof
  requirements.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 003`

Proof:
- Terminal proof showing both checks pass.
- Short note mapping task numbers to contract functions.

### 004 Board State, Default Data, And Persistence

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
- `python3 tests/kanban_contract_check.py --task 004`

Proof:
- Screenshot of default cards across all four columns.
- Console-error-free reload proof showing state restored.

### 005 Column Management

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
- `python3 tests/kanban_contract_check.py --task 005`

Proof:
- Short recording: add a column, rename it, delete it.
- Screenshot or recording of non-empty column delete prevention.

### 006 Card Creation And Card Rendering

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
  behavior to task 007.
- Provide stable selectors/data attributes for forms and card fields.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 006`

Proof:
- Recording: open form, attempt empty save, add valid card, cancel another form.
- Screenshot of Low/Medium/High priority badges.

### 007 Card Details, Overdue State, And Delete

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
- `python3 tests/kanban_contract_check.py --task 007`

Proof:
- Recording: add overdue card with description, expand details, delete a card.
- Screenshot of overdue styling.
- Reload proof that the deleted card remains gone.

### 008 Native Drag And Drop

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
- `python3 tests/kanban_contract_check.py --task 008`

Proof:
- Recording: drag a card from `To Do` to `In Progress`, then to `Done`.
- Screenshot or trace frame showing drop-zone highlight.
- Screenshot showing Done styling.
- Reload proof that moved card membership/order persists.

### 009 Search, Priority Filter, And Statistics

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
- `python3 tests/kanban_contract_check.py --task 009`

Proof:
- Recording: search, apply priority filter, clear filters, observe stats.
- Screenshot of fixed stats bar after cards are filtered.

### 010 Visual Polish, Responsiveness, Accessibility, And Final Proof

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

Stop for human preview/testing after task 010 passes checks and final proof is
recorded.

## Re-Splitting Triggers

Manager should stop and re-split if:

- a task fails twice for the same behavior;
- a local worker returns no usable patch or file bundle twice;
- a local worker weakens checks or removes proof hooks;
- native drag/drop cannot be made deterministic;
- proof cannot be captured without changing the product behavior;
- task 006 or 007 expands into unrelated card features;
- task 010 introduces new behavior instead of polish/accessibility only.
