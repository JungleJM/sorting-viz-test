# Kanban Board Issue Log

Use this file to record blockers, skipped requirements, model/runtime failures,
proof gaps, and human decisions.

## Open Issues

- None at spec time.

## Planning Decisions

- Use the root `index.html` for the Kanban build and leave
  `sorting-visualizer/` untouched.
- Split card work into creation/rendering and secondary details/delete behavior
  to avoid bundling form validation, persistence, animation, and deletion into
  one local-LLM task.
- Isolate native drag/drop after cards and column behavior are stable.
- Make task `001` own the test harness and the full task-scoped test matrix.
- Use Playwright for browser workflow proof and terminal/asciinema proof for
  command execution.

## Failure Artifact Policy

If any task reaches `needs_human`, Loop Manager must write:

```text
specs/kanban-board-after-planning-guide/failure-artifacts/<task-id>-local-failure-summary.md
```

Do not continue from broken local code unless a human explicitly decides to.
