# Loop Manager Project Scripts

## `verify-spec-planning.sh`

Run this at the end of spec-making:

```sh
.loop-manager/scripts/verify-spec-planning.sh
```

It finds the Loop Manager source checkout and runs its test suite through `uv`.
This is a preflight check. It does not submit a plan.

## `submit-plan.sh`

Run this when the spec is ready to start in Loop Manager:

```sh
.loop-manager/scripts/submit-plan.sh --feature <feature-slug> -v
```

Use `--feature` for the normal layout:

```text
specs/<feature-slug>/plan-contract.bluefin.yaml
```

Use `--plan` when you want to submit one exact YAML file:

```sh
.loop-manager/scripts/submit-plan.sh --plan specs/<feature-slug>/plan-contract.bluefin.yaml -v
```

Rule of thumb:

- `--feature`: run the standard plan for a feature folder.
- `--plan`: run this exact PlanContract file.

Useful options:

- `--dry-run`: discover, verify, and parse the plan without posting to Bluefin.
- `--latest`: if multiple plans exist, choose the newest one.
- `--skip-verify`: submit without running the spec-planning preflight.
- `-v`: print selected plan and monitoring URLs.
- `-vv`: also print a detailed response summary.

Before submission, the script:

- runs `.loop-manager/scripts/verify-spec-planning.sh` unless `--skip-verify`
  is passed;
- checks Loop Manager health at `/health`;
- queries `/worker-models` so the runtime exposes the valid worker/model
  profile names used by frontier-generated PlanContracts.

After submission, the script prints the Loop Manager dashboard URL, Paperclip
dashboard URL, Paperclip events URL, and the plan dashboard URL.
