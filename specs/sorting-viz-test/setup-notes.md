# Setup Notes: Sorting Viz Test

## 2026-06-27

- Renamed Gitea repo to `gitea_admin/sorting-viz-test`.
- Updated local `origin` to:

```text
ssh://git@appliedsci.tail90eacc.ts.net:411/gitea_admin/sorting-viz-test.git
```

- Intended Bluefin checkout path:

```text
/var/home/j/code/sorting-viz-test
```

- Intended feature branch:

```text
feature/sorting-viz-test
```

- Loop Manager should use branch handoff mode from the updated Loop Manager
  commit `f51e16e` or later.
- Denbuntu should remain the preferred checker when reachable.
- jmapple should be the checker fallback when Denbuntu has an infrastructure
  failure.

## Worker readiness

- Bluefin can SSH to jmapple as `jmath`.
- jmapple has `/Users/jmath/ai-workers/bin/lmstudio_worker.py`.
- Bluefin can SSH to Denbuntu as `j`.
- Denbuntu has `/home/j/ai-workers/bin/lmstudio_worker.py`.
- Both Denbuntu and jmapple responded to `http://127.0.0.1:1234/v1/models`
  from their own machines via Bluefin SSH.
- Both report `zai-org/glm-4.7-flash` as locally installed, not only
  LM Link-advertised.
- Structured JSON response reliability remains unproven for GLM reviewer calls.

## Runtime mode

Use `LOOP_MANAGER_RUNTIME_MODE=dry_run` for the first managed canary. Move to
`live` only after worker connectivity and the first task branch handoff are
verified.

Bluefin should also export:

```text
LOOP_MANAGER_WORKER_REPO_URL=https://appliedsci.tail90eacc.ts.net:3000/gitea_admin/sorting-viz-test.git
LOOP_MANAGER_PUSH_BRANCH_BEFORE_WORKER=true
```
