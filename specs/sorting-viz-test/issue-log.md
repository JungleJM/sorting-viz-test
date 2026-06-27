# Issue Log: Sorting Viz Test

## Open issues

- Structured JSON reliability is still a risk for the GLM reviewer workers.
  On 2026-06-27, both Denbuntu and jmapple were reachable from Bluefin and
  could call local LM Studio, but tiny checker probes still returned malformed
  or empty JSON after model generation. This is a control-plane response issue,
  not a branch/diff handoff issue.
- Worker-side branch checkout/edit/review support was added to Loop Manager,
  but the first live branch checkout canary still needs to prove worker Git
  credentials can clone and, for implementers, push task branches.

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

## Log entries

### 2026-06-27

- Created initial sorting-viz spec package for human review.
- Designed tasks to be smaller than the failed HantaSim attempt.
- Added explicit test expectations to every implementation task.
