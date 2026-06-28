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
- `project.yaml` branch handoff fields: whether workers must checkout and
  review task branches rather than receiving file snippets

The installer also creates `specs/_templates/` with reusable feature, task,
proof, review, readiness, and PlanContract templates. For a production Loop
Manager run:

1. Fill in this repo's `.loop-manager/project.yaml`.
2. Replace placeholder checks in `.loop-manager/checks.yaml` with commands that
   work from a clean checkout.
3. Set `.loop-manager/preview.yaml` to the real proof mode for the project.
4. Draft a feature directory under `specs/<feature-slug>/`.
5. Convert the feature task list into a PlanContract and submit it to Bluefin.

For real-worker runs, the manager should create and push a task branch before
developer/reviewer activation. Workers should checkout that branch locally,
perform their implementation or review there, and report branch status back to
Loop Manager. Diffs may be internal worker artifacts, but the branch is the
handoff unit.

Runtime worker routing, model selection, Gitea tokens, and Paperclip settings
belong in the Loop Manager repo and Bluefin environment, not in this target repo.

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

Current jmapple preference is Qwen3-Coder through LM Studio MLX when available,
with direct MLX as fallback. LM Studio must use MLX runtime `1.8.5` for this
model family; runtime `1.9.1` fails on the embedded Python filesystem codec.
The preferred loaded API identifier is `qwen3-coder-30b-a3b-instruct`; direct
MLX remains the fallback if LM Studio cannot keep that model loaded.

For real Gitea task PRs, Loop Manager now runs local PR-Agent review before
task-branch merge. The task branch merges into the feature branch only after the
local PR-Agent decision is `approve`.

If a task stops at `needs_human`, Loop Manager must create a failure artifact
summarizing the local attempts, worker results, checks, attempted files, and
restart guidance. Codex may create that artifact only when deterministic
artifact creation fails and Codex is explicitly configured as `fallback` for the
developer or code-review role.
