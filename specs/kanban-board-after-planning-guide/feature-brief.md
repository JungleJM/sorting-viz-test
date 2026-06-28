# Kanban Board Feature Brief

## Source Prompt

Build a single-file personal Kanban board with drag and drop, editable columns,
cards with priority/due dates/descriptions, filtering/search, localStorage
persistence, live statistics, and a polished responsive dark glass interface.

Source file: `kanban.md`

## Product Goal

Create a self-contained root `index.html` that can be opened directly in a
browser and used as a personal task board without a server, build tooling, or
external JavaScript libraries.

## User Experience Requirements

- First screen is the usable board, not a landing page.
- Default columns are `Backlog`, `To Do`, `In Progress`, and `Done`.
- Users can add, rename, and delete empty columns.
- Users can add cards with required title, optional description, priority, and
  due date.
- Cards can move between columns using native HTML5 drag and drop.
- Moving a card to `Done` visibly marks it complete.
- Search and priority filters update immediately.
- Hidden filtered cards preserve placeholder space so columns do not jump.
- State persists automatically to `localStorage`.
- A fixed bottom statistics bar shows total, overdue, done, and completion
  rate.
- The UI remains usable on small screens with horizontal board scrolling.

## Technical Boundaries

- Single root `index.html`.
- Inline HTML, CSS, and JavaScript.
- Vanilla JavaScript only.
- Google Fonts CDN for Inter is allowed.
- No external JavaScript libraries.
- Must work by opening the file directly through `file://`.
- A temporary static server may be used only for proof automation.

## Quality Bar

- Card and column operations are discoverable and ergonomic.
- No browser `prompt()`, `alert()`, or `confirm()` workflows.
- State mutations save after each successful change.
- Drag/drop has visible feedback and deterministic drop behavior.
- Dynamic controls have accessible labels or titles.
- Tests are task-scoped and deterministic from a clean checkout.
- Browser proof includes screenshots or recordings plus console-error checks.

## Completion Definition

The feature is ready for human review when all PlanContract checks pass,
required proof artifacts exist under `specs/kanban-board-after-planning-guide/proof/`,
the final feature opens directly in a browser, and the final feature branch
remains a human merge decision.
