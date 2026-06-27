# Issue Log: Sorting Viz Test

## Open issues

- Initial production attempts showed task 001 was still too large for the
  local implementers: Devstral and Qwen repeatedly produced only `index.html`
  and omitted `tests/static_contract_check.py`, so deterministic review
  correctly blocked merge to `feature/sorting-viz-test`. The plan was re-split
  so task 001 creates only the test harness and task 002 creates the app shell.
- Structured JSON reliability is still a risk for the GLM reviewer workers.
  On 2026-06-27, both Denbuntu and jmapple were reachable from Bluefin and
  could call local LM Studio, but tiny checker probes still returned malformed
  or empty JSON after model generation. This is a control-plane response issue,
  not a branch/diff handoff issue.
- Loop Manager now has an adapter-level JSON repair layer and larger GLM token
  budgets, but Denbuntu and jmapple GLM still failed the tiny checker JSON
  probe. Oracle Devstral passed the same checker probe with valid JSON.
- Worker-side branch checkout/edit/review support was added to Loop Manager,
  and worker Git access was proven for clone/review and Oracle task-branch
  push. The first managed-loop branch checkout canary still needs to run
  through Loop Manager itself.

## Resolved or mitigated issues

- The previous HantaSim attempt was archived on branch
  `failed-attempt-hanta-1` before resetting `main`.
- The repo was renamed from `hantasim-test` to `sorting-viz-test`.
- Bluefin-to-jmapple SSH was rechecked and works.
- The jmapple fallback worker script was installed at
  `/Users/jmath/ai-workers/bin/lmstudio_worker.py`.
- Denbuntu came back up and responded to Bluefin SSH and LM Studio `/v1/models`.
- Both Denbuntu and jmapple report `zai-org/glm-4.7-flash` as locally
  installed under the local-only guardrail.
- Loop Manager commit `f51e16e` added remote worker branch checkout support so
  workers can operate on task branches instead of treating copied snippets or
  diffs as the handoff.
- jmapple, Denbuntu, and Oracle can clone `feature/sorting-viz-test`.
- Oracle can push and delete a canary task branch over HTTPS using its local
  token-backed `.netrc`.

## Log entries

### 2026-06-27

- Created initial sorting-viz spec package for human review.
- Designed tasks to be smaller than the failed HantaSim attempt.
- Added explicit test expectations to every implementation task.
