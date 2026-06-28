# Kanban Board Task Breakdown

Tasks are sized for local-LLM implementation and review. Each task should be
implemented on its own task branch and reviewed against this spec.

## 001 Scaffold Single-File App And Test Harness

Create the root `index.html` skeleton and the test harness files.

Implementation:
- Create `index.html` with semantic app shell, top toolbar, board region, and
  fixed stats bar placeholders.
- Add inline CSS/JS sections with clear comments for State, Rendering,
  Persistence, Drag and Drop, Filtering, and Statistics.
- Load Inter from Google Fonts.
- Add `tests/static_contract_check.py`.
- Add `tests/kanban_contract_check.py`.
- The tests should be real contract checks, not placeholders. They should parse
  `index.html` and fail with clear messages when required IDs/classes,
  accessible labels, state keys, event hooks, or required text are missing.
- `tests/static_contract_check.py` should check project-wide constraints:
  single root `index.html`, no external JavaScript libraries, no browser
  `prompt()`/`alert()`/`confirm()` workflows, required inline CSS/JS sections,
  Inter font loading, and no writes to `sorting-visualizer/`.
- `tests/kanban_contract_check.py` should support `--task NNN` and `--all`.
  Each task check should verify only behavior or structure introduced up to
  that task, so later incomplete work does not fail earlier branches.
- Where browser behavior cannot be proven from static parsing, the contract test
  should check for named hooks, data attributes, storage keys, and event
  listeners that make Playwright proof straightforward.
- Tests should be deterministic and runnable from a clean checkout with only
  Python standard library.

Test design:
- `static_contract_check.py` should expose small helper assertions such as
  `require_text`, `require_regex`, `forbid_regex`, and `require_count_at_least`
  so failures name the missing contract plainly.
- `kanban_contract_check.py` should define one function per task, for example
  `check_task_001(html)`, `check_task_002(html)`, and so on. `--all` should run
  the task checks in numeric order and report every failure it can, not just the
  first avoidable failure.
- Task 001 checks should verify the shell: top toolbar, search input placeholder
  or label, priority filter control, board container, stats bar, add-column
  placeholder/control, inline CSS/JS, and section comments.
- Task 002 checks should verify state/persistence names: default column labels,
  example-card data, stable ID generation, a single localStorage key, restore
  path, save path, and render-from-state flow.
- Task 003 checks should verify column action hooks: add column handler, inline
  rename editor, empty-column delete guard, non-empty delete message, and
  persistence after column changes.
- Task 004 checks should verify card creation hooks: per-column add-card form,
  required title validation, priority options, due date input, description
  textarea, stable card schema, priority badge markup, due-date markup, and
  persistence after create.
- Task 005 checks should verify card secondary behavior: description toggle,
  overdue comparison against today's date, visible overdue marker, delete
  handler, fade-out class or animation, bounded removal fallback, and stale-ID
  cleanup.
- Task 006 checks should verify drag/drop hooks: `draggable`, `dragstart`,
  `dragover`, `dragleave`, `drop`, stable card/column data attributes,
  drop-zone class, state movement function, Done styling rule, and persistence
  after drop.
- Task 007 checks should verify filter/stats behavior: case-insensitive search,
  priority dropdown values, hidden-card placeholder class, total/overdue/done
  counters, completion-rate calculation, fixed stats bar, and updates after
  create/delete/drop/filter events.
- Task 008 checks should verify final constraints: no external JavaScript,
  no browser prompt/alert/confirm, responsive board scrolling styles,
  accessible labels/titles for icon controls, required proof artifact paths
  referenced in the spec, and all prior checks passing.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 001`

Proof:
- Screenshot of initial shell at desktop width.
- Screenshot of horizontal-scroll board area at narrow width.
- Terminal proof showing both test commands fail before the expected structures
  exist and pass after the task implementation.

## 002 Board State, Default Data, And Persistence

Implement initial state, example cards, localStorage restore/save, and rendering
of the four default columns.

Implementation:
- Define state with columns and cards including stable IDs and card order.
- Populate example cards spread across all four default columns when storage is
  empty.
- Restore full board state from localStorage on load.
- Save after every state-changing action introduced in this task.
- Render columns and cards from state.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 002`

Proof:
- Screenshot of default cards across all four columns.
- Browser-console-free proof log showing reload persistence.

## 003 Column Management

Implement adding, renaming, and deleting empty columns.

Implementation:
- Add the end-of-board `+ Add Column` button.
- Add custom columns with sensible default names.
- Rename any column by double-clicking its header using an inline editor.
- Show a trash icon on column hover.
- Allow deletion only when the column is empty; empty-column deletion updates
  state and localStorage.
- Prevent deletion of non-empty columns with a visible non-blocking message.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 003`

Proof:
- Short recording: add a column, rename it, delete it.
- Screenshot of non-empty column delete prevention.

## 004 Card Creation And Card Rendering

Implement inline card creation and the basic card display contract.

Implementation:
- Add `+ Add card` at the bottom of every column.
- Show an inline mini-form, not `prompt()`.
- Form fields: required title, priority selector, due date picker, optional
  description textarea, Save, Cancel.
- Validate title before saving and keep the form open with a visible inline
  message when title is empty.
- Create cards with stable IDs, column membership, priority, due date,
  description, and creation/update timestamps if the local state shape already
  uses timestamps.
- Save state to localStorage after each successful card create.
- Render priority badges with distinct Low/Medium/High colors.
- Render due dates in a consistent card metadata area.
- Render optional descriptions collapsed by default, but do not implement the
  expand/collapse behavior until task 005.
- Keep card controls keyboard reachable and labels/titles present for icon-only
  controls.

Test harness expectations:
- `--task 004` should verify add-card controls/forms exist for columns, form
  fields use stable selectors or data attributes, title validation is present,
  the card object schema includes the required fields, save paths call
  persistence, and priority/due-date markup exists.
- Static checks should still reject browser `prompt()` usage.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 004`

Proof:
- Short recording: open add-card form, attempt empty save, add a valid card
  with priority and due date, cancel another form.
- Screenshot of Low/Medium/High priority badge styling.

## 005 Card Details, Overdue State, And Delete

Implement secondary card behavior after cards can already be created and shown.

Implementation:
- Make optional descriptions expandable/collapsible below the title.
- Description toggle state should be clear visually and accessible by keyboard.
- Render optional description as collapsible detail below the title.
- Mark overdue due dates in red with a warning icon or clear warning marker.
- Show card delete button on hover and remove cards with a fade-out animation.
- Delete should update state, persist to localStorage, and not leave card IDs in
  any column order arrays.
- Fade-out should not make tests flaky: remove the card after a bounded timeout
  or after the animation end, with a fallback.
- Empty cards area should remain visually stable after deleting the last card in
  a column.

Test harness expectations:
- `--task 005` should verify description toggle wiring, overdue date comparison
  logic, warning markup, delete event handling, persistence after delete, and
  animation/fallback removal paths.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 005`

Proof:
- Short recording: add a high-priority overdue card with description, expand
  details, then delete a card.
- Screenshot of priority badges and overdue styling.

## 006 Native Drag And Drop

Implement native HTML5 drag/drop movement between columns and Done styling.

Implementation:
- Make cards draggable with the native HTML5 Drag and Drop API.
- Highlight target columns with a visible drop-zone indicator while dragging.
- Support dropping into empty columns and columns with existing cards.
- Move cards between columns and preserve order within the destination column.
- Define a simple deterministic ordering rule for drops. If precise insertion
  between cards is too risky for local workers, append to the destination column
  first and make that behavior explicit in code/tests.
- Moving a card to `Done` applies muted styling and strikethrough title.
- Moving a card out of `Done` removes done styling.
- Persist order and column membership after each drop.
- Drag state should clean up after successful drop, cancelled drag, and invalid
  drop target.
- Drag/drop selectors and data attributes should make Playwright proof possible
  without relying on fragile visual text matching.

Test harness expectations:
- `--task 006` should verify native drag/drop handlers exist, draggable
  attributes are applied to cards, drop targets have stable selectors, state
  movement updates both source and destination columns, Done styling is derived
  from column membership, and persistence is called after drop.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 006`

Proof:
- Short recording: drag a card from `To Do` to `In Progress`, then to `Done`.
- Screenshot showing drop-zone highlight and done card styling.

## 007 Search, Priority Filter, And Statistics

Implement filtering and the fixed bottom statistics bar.

Implementation:
- Search bar filters cards by title, case-insensitive.
- Priority dropdown supports All, Low, Medium, High.
- Filtered-out cards are hidden but leave a placeholder gap so column height
  does not jump.
- Statistics update live: total cards, overdue cards, done cards, completion
  rate.
- Statistics stay fixed at the bottom of the viewport and do not hide controls.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 007`

Proof:
- Short recording: search, apply priority filter, clear filters, observe stats.
- Screenshot of fixed stats bar after cards are filtered.

## 008 Visual Polish, Responsiveness, And Final Proof

Finalize dark glassmorphism styling, responsive behavior, accessibility labels,
and feature proof.

Implementation:
- Dark charcoal/slate theme.
- Frosted-glass column panels with subtle borders and shadow.
- Smooth transitions for hover lift, drag opacity, drop pulse, and delete
  fade-out.
- Horizontal board scrolling on small screens without layout breakage.
- Buttons and icon-only controls have accessible labels or titles.
- No browser `prompt()` usage.
- No external JavaScript libraries.
- Final cleanup of comments and structure.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --all`

Proof:
- Desktop screenshot.
- Mobile/narrow screenshot.
- Final short recording covering add card, filter, drag to Done, stats update,
  and persistence after reload.
