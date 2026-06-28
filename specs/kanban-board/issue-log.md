# Kanban Board Issue Log

Use this file to record blockers, skipped requirements, model/runtime failures,
proof gaps, and human decisions.

## Open Issues

- None at spec time.

## Decisions

- 2026-06-27: Preserve the completed sorting visualizer under
  `sorting-visualizer/` and use the repo root for the new Kanban build.
- 2026-06-27: Keep the existing Gitea repo URL for now even though the project
  id is `kanban-board-test`.

## Failure Artifact Policy

If any task reaches `needs_human`, the mandatory failure artifact should be
created under:

```text
specs/kanban-board/failure-artifacts/
```

Do not continue from broken local code unless a human explicitly decides to.
