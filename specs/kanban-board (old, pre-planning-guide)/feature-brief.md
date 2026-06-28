# Kanban Board Feature Brief

## Source Prompt

Build a single-file personal Kanban board with drag and drop, editable columns,
cards with priority/due dates/descriptions, filtering/search, localStorage
persistence, live statistics, and a polished responsive dark glass interface.

Source file: `kanban.md`

## Product Goal

Create a self-contained `index.html` that can be opened directly in a browser
and used as a personal task board without a server, build tooling, or external
JavaScript libraries.

## User Experience Requirements

- The first screen is the usable board, not a landing page.
- Default columns are `Backlog`, `To Do`, `In Progress`, and `Done`.
- Users can add, rename, and delete empty columns.
- Users can add cards with title, optional description, priority, and due date.
- Cards can move between columns using native HTML5 drag and drop.
- Search and priority filters update the board immediately.
- State persists automatically to `localStorage`.
- A fixed bottom statistics bar always shows total cards, overdue cards, done
  cards, and completion rate.
- The UI must remain usable on small screens with horizontal board scrolling.

## Technical Boundaries

- Single root `index.html`.
- Vanilla JavaScript only.
- Inline HTML, CSS, and JavaScript.
- Google Fonts CDN for Inter is allowed.
- No external JavaScript libraries.
- Must work by opening the file directly in a browser.

## Quality Bar

- Card and column operations should be discoverable and ergonomic.
- Drag/drop should provide clear visual feedback.
- Hidden filtered cards should preserve placeholder space to avoid column height
  jumps.
- LocalStorage writes should happen after every state change.
- Tests should inspect structure and behavior contracts without requiring a
  server.
- Proof should include screenshots and short interaction recordings with visible
  click feedback.

## Completion Definition

The feature is ready for human review when `index.html` implements all prompt
requirements, automated contract checks pass, proof artifacts exist under
`specs/kanban-board/proof/`, and the final feature can be opened directly in a
browser.
