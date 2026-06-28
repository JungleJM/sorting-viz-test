# Kanban Board Proof Plan

Proof artifacts should be stored under:

```text
specs/kanban-board/proof/tasks/<task-id>/
specs/kanban-board/proof/feature-final/
```

## General Proof Rules

- Capture proof against the root `index.html`.
- Opening the file directly in a browser must work.
- If using a local static server for Playwright convenience, note that the app
  still works through `file://`.
- Clicks in recordings should be visible through a click ripple, mouse trace,
  or Playwright trace indicator.
- Post or link task proof artifacts on the task PR before merge.

## Task Proof

### 001 Scaffold

- Desktop screenshot of initial shell.
- Narrow viewport screenshot proving horizontal board region does not break.

### 002 State And Persistence

- Screenshot of default cards in all four columns.
- Short reload proof showing localStorage state restored.

### 003 Column Management

- Short recording: add column, rename column, delete empty column.
- Screenshot or recording of non-empty delete prevention.

### 004 Card Operations

- Short recording: open inline add-card form, save a card, expand description,
  delete a card.
- Screenshot of Low/Medium/High badges and overdue styling.

### 005 Drag And Drop

- Short recording: drag card between columns and into Done.
- Screenshot showing done styling.
- Screenshot or trace frame showing drop-zone highlight.

### 006 Filtering And Stats

- Short recording: search by title, filter by priority, clear filters.
- Screenshot of stats bar with non-zero total, overdue, done, and completion.

### 007 Final Feature Proof

- Desktop screenshot.
- Narrow/mobile screenshot.
- Short recording covering:
  - add card
  - filter
  - drag to Done
  - stats update
  - reload persistence

## Failure Proof

If any task reaches `needs_human`, Loop Manager must write:

```text
specs/kanban-board/failure-artifacts/<task-id>-local-failure-summary.md
```

That artifact should be attached or linked to the task PR or issue log.
