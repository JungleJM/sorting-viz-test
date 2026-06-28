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

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 001`

Proof:
- Screenshot of initial shell at desktop width.
- Screenshot of horizontal-scroll board area at narrow width.

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

## 004 Card Creation, Details, Priority, Due Date, And Delete

Implement card add forms and complete card rendering behavior.

Implementation:
- Add `+ Add card` at the bottom of every column.
- Show an inline mini-form, not `prompt()`.
- Form fields: required title, priority selector, due date picker, optional
  description textarea, Save, Cancel.
- Render priority badges with distinct Low/Medium/High colors.
- Render optional description as collapsible detail below the title.
- Mark overdue due dates in red with a warning icon or clear warning marker.
- Show card delete button on hover and remove cards with a fade-out animation.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 004`

Proof:
- Short recording: add a high-priority overdue card with description, expand
  details, then delete a card.
- Screenshot of priority badges and overdue styling.

## 005 Native Drag And Drop

Implement native HTML5 drag/drop movement between columns and Done styling.

Implementation:
- Make cards draggable with the native HTML5 Drag and Drop API.
- Highlight target columns with a visible drop-zone indicator while dragging.
- Move cards between columns and preserve order.
- Moving a card to `Done` applies muted styling and strikethrough title.
- Moving a card out of `Done` removes done styling.
- Persist order and column membership after each drop.

Checks:
- `python3 tests/static_contract_check.py`
- `python3 tests/kanban_contract_check.py --task 005`

Proof:
- Short recording: drag a card from `To Do` to `In Progress`, then to `Done`.
- Screenshot showing drop-zone highlight and done card styling.

## 006 Search, Priority Filter, And Statistics

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
- `python3 tests/kanban_contract_check.py --task 006`

Proof:
- Short recording: search, apply priority filter, clear filters, observe stats.
- Screenshot of fixed stats bar after cards are filtered.

## 007 Visual Polish, Responsiveness, And Final Proof

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
