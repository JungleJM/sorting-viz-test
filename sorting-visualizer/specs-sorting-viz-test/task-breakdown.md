# Task Breakdown: Sorting Viz Test

## Feature slug

`sorting-viz-test`

## Sizing rule

Each task should be small enough for a local LLM to implement and for another
local LLM to review. Prefer one behavior layer per task. The app code must stay
in `index.html`; tests and proof files may be separate.

## Task list

| N | Task | Branch | Tests to perform | Proof | Auto-merge eligible |
|---|------|--------|------------------|-------|---------------------|
| 000 | Codex spec breakdown | `task/sorting-viz-test-000-spec-breakdown` | Human review of this spec package | markdown review | no |
| 001 | Create lightweight test harness | `task/sorting-viz-test-001-scaffold` | Python compile check for harness scripts | command output | yes |
| 002 | Scaffold app layout, controls, and array rendering | `task/sorting-viz-test-002-array-rendering` | Static/browser check for required controls, 10/200 sizes, bar count, reset behavior | screenshot + command output | yes |
| 003 | Animation controller, speed, start/pause, elapsed time | `task/sorting-viz-test-003-animation-controls` | Browser check for start, pause, resume, speed slider, elapsed stat | short recording or screenshot sequence | yes |
| 004 | Bubble, insertion, and selection sort step generators | `task/sorting-viz-test-004-simple-sorts` | Unit/browser checks that three algorithms sort fixed arrays and update comparisons/swaps | command output | yes |
| 005 | Merge, quick, and heap sort step generators | `task/sorting-viz-test-005-advanced-sorts` | Unit/browser checks that three algorithms sort fixed arrays and update comparisons/swaps | command output | yes |
| 006 | Live stats, sorted highlighting, and completion states | `task/sorting-viz-test-006-stats-completion` | Browser check for algorithm label, comparisons, swaps, elapsed, final sorted colors | screenshot + command output | yes |
| 007 | Final UI polish, responsiveness, and cross-browser smoke | `task/sorting-viz-test-007-polish-hardening` | Static checks, browser smoke at desktop/mobile-ish widths, manual visual inspection | screenshot + short recording | no |

## Task details

### 000 Codex spec breakdown

Goal: produce this spec package for human review before the managed loop starts.

Acceptance criteria:

- `feature-brief.md`, `task-breakdown.md`, `proof/proof-plan.md`,
  `issue-log.md`, `setup-notes.md`, and `plan-contract.bluefin.yaml` exist.
- Every implementation task includes tests to perform.
- Tasks are small enough for local LLMs.

Tests to perform:

- Human review of the markdown and YAML.
- Confirm Bluefin paths and branch names match the renamed repo.

### 001 Create lightweight test harness

Goal: create lightweight Python test harness files under `tests/` before asking
local workers to build the app UI.

Acceptance criteria:

- `tests/static_contract_check.py` exists and is valid Python.
- `tests/algorithm_contract_check.py` exists and is valid Python.
- Test scripts use clear assertion messages suitable for local-LLM review.
- Test scripts do not move app code out of `index.html`.

Tests to perform:

- `python3 -m py_compile tests/static_contract_check.py tests/algorithm_contract_check.py`

### 002 Scaffold app layout, controls, and array rendering

Goal: create `index.html` with the full visual layout, controls, stats panel,
and randomized bar rendering.

Acceptance criteria:

- `index.html` opens directly in a browser.
- The page contains algorithm buttons for all six algorithms.
- The page contains speed and array-size sliders, Shuffle & Reset, Start/Pause,
  and the stats panel.
- The visual style is dark, modern, and not a bare unstyled prototype.
- Array-size slider supports 10 through 200.
- Shuffle & Reset regenerates values and resets visual state.
- Bar count matches the selected array size.
- Bars use a default unsorted color and animate value/height changes smoothly.

Tests to perform:

- `python3 tests/static_contract_check.py`
- `python3 tests/algorithm_contract_check.py --rendering`
- Browser check: set size to 10 and 200 and verify bar counts visually or via
  test output.

### 003 Animation controller, speed, start/pause, elapsed time

Goal: implement the animation loop and control state needed by all algorithms.

Acceptance criteria:

- Start begins playback for the selected algorithm.
- Pause stops progress without resetting.
- Resume continues from the same step.
- Speed slider changes delay between steps.
- Elapsed time updates while running and stops when paused/completed.

Tests to perform:

- `python3 tests/static_contract_check.py`
- `python3 tests/algorithm_contract_check.py --controls`
- Browser check: start, pause, resume, and change speed during a run.

### 004 Bubble, insertion, and selection sort step generators

Goal: implement instrumented step generators for the simpler iterative sorts.

Acceptance criteria:

- Bubble Sort, Insertion Sort, and Selection Sort produce sorted output.
- Comparisons increment for meaningful element comparisons.
- Swaps/writes increment when values are moved.
- The currently compared bars are highlighted during playback.
- Completed regions are marked sorted where the algorithm can know that.

Tests to perform:

- `python3 tests/static_contract_check.py`
- `python3 tests/algorithm_contract_check.py --algorithms bubble,insertion,selection`
- Browser check each of the three algorithms on a small array.

### 005 Merge, quick, and heap sort step generators

Goal: implement instrumented step generators for the remaining more complex
sorts without destabilizing the renderer.

Acceptance criteria:

- Merge Sort, Quick Sort, and Heap Sort produce sorted output.
- Comparisons and swaps/writes update during each algorithm.
- Active comparisons and writes are highlighted.
- Each algorithm completes without freezing at array size 200.

Tests to perform:

- `python3 tests/static_contract_check.py`
- `python3 tests/algorithm_contract_check.py --algorithms merge,quick,heap`
- Browser check each of the three algorithms on a medium array.

### 006 Live stats, sorted highlighting, and completion states

Goal: finish the live stats panel and final visual states.

Acceptance criteria:

- Stats panel always shows selected algorithm name.
- Comparisons, swaps/writes, and elapsed time update live.
- On completion, all bars are marked sorted.
- Starting a new algorithm resets stats cleanly.
- Controls cannot corrupt state mid-sort.

Tests to perform:

- `python3 tests/static_contract_check.py`
- `python3 tests/algorithm_contract_check.py --stats`
- Browser check one short run through completion and screenshot final state.

### 007 Final UI polish, responsiveness, and cross-browser smoke

Goal: make the app feel finished and harden the direct-open browser experience.

Acceptance criteria:

- Layout is readable and polished on common desktop widths.
- Controls do not overlap or resize awkwardly.
- Text is plain and understandable.
- Color contrast makes default, comparing, and sorted states obvious.
- All feature acceptance criteria pass.
- Known issues are recorded in `specs/sorting-viz-test/issue-log.md`.

Tests to perform:

- `python3 tests/static_contract_check.py`
- `python3 tests/algorithm_contract_check.py --all`
- Browser smoke in at least one Chromium-family browser by opening
  `index.html` directly.
- Screenshot at desktop width and a narrower responsive width.

## Re-splitting triggers

Manager should stop and re-split if:

- a worker fails twice with malformed JSON or unusable diffs;
- a task tries to move app code out of `index.html`;
- animation, sorting logic, and final polish are mixed in one oversized PR;
- tests are skipped or weakened to make a task pass;
- the app cannot be opened directly from the filesystem.
