# Loop Manager Project Files

These files describe what this project needs from Loop Manager. They do not
contain machine tokens, model secrets, Paperclip secrets, or Gitea tokens.

Bluefin owns runtime secrets and routing through:

```text
/var/home/j/.config/loop-manager/loop-manager.env
```

Edit these files for project-specific behavior:

- `project.yaml`: repo identity and branch policy
- `checks.yaml`: build, test, lint, and typecheck commands
- `preview.yaml`: preview server and proof expectations

Proof artifacts should be organized under:

```text
specs/<feature-slug>/proof/tasks/NNN-<task-slug>/
specs/<feature-slug>/proof/feature-final/
```

For future managed runs, task proof should be linked or posted on the Gitea task
PR before the task branch merges into the feature branch.

Task PRs should include the rendered task spec in the PR body. That makes Gitea
the central review surface for the code-review node, local PR-Agent,
Codex/OpenAI PR-Agent, and human review.

If local PR-Agent cannot run, record the reason on the task PR and prioritize
Codex/OpenAI PR review. If both PR-Agent paths are unavailable, leave the task
blocked for human review unless the project explicitly marks PR-Agent review
optional.
