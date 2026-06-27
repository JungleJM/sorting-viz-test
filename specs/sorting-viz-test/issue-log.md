# Sorting Viz Test Issue Log

## Managed Loop Results

- Initial production attempts showed task 001 was too large for the local
  implementers: Devstral and Qwen repeatedly produced only `index.html` and
  omitted `tests/static_contract_check.py`, so deterministic review correctly
  blocked merge to `feature/sorting-viz-test`.
- The plan was re-split so task 001 created only the test harness and task 002
  created the app shell.
- After re-splitting, task 001 passed and merged into `feature/sorting-viz-test`.
- Task 002 produced a usable scaffold, but its generated harness was too
  brittle: it expected exact strings and a select-based UI even though the spec
  called for algorithm buttons. Codex manually merged the worker's task-002
  branch into `feature/sorting-viz-test` and corrected the harness to semantic
  checks at feature commit `468e853`.
- Tasks 003 through 007 passed local worker review and were merged into
  `feature/sorting-viz-test`.
- Task 007 regressed the original single-file requirement by moving runtime
  code into `specs/sorting-viz-test/algorithm.js` and
  `specs/sorting-viz-test/visualization.js`.

## Worker Reliability Notes

- Structured JSON reliability is still a risk for GLM reviewer workers.
- On 2026-06-27, both Denbuntu and jmapple were reachable from Bluefin and
  could call local LM Studio, but tiny checker probes still returned malformed
  or empty JSON after model generation. This is a control-plane response issue,
  not a branch/diff handoff issue.
- Loop Manager now has an adapter-level JSON repair layer and larger GLM token
  budgets, but Denbuntu and jmapple GLM still failed the tiny checker JSON
  probe. Oracle Devstral passed the same checker probe with valid JSON.
- Worker-side branch checkout/edit/review support was added to Loop Manager,
  and worker Git access was proven for clone/review and Oracle task-branch
  push.

## Final Manual Hardening

- Restored the app to a self-contained `index.html` that can be opened directly
  in a browser.
- Removed external runtime JavaScript files from the spec folder.
- Replaced static and algorithm contract tests so they check the single-file
  contract, required controls, six sorting algorithms, rendering hooks, and
  stats hooks.
- Captured final desktop, running-state, mobile, and short video proof artifacts
  in `specs/sorting-viz-test/proof/`.

## Residual Risks

- The UI proof is browser-smoke level, not a full visual regression suite.
- The app is intentionally small and educational; it does not attempt to
  benchmark algorithm performance.
