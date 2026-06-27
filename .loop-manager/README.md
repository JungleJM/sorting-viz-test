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
