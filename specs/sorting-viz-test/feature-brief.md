# Feature Brief: Sorting Viz Test

## Feature slug

`sorting-viz-test`

## Original request

Create a single self-contained `index.html` file with a real-time sorting
algorithm visualizer. It should include Bubble Sort, Insertion Sort, Selection
Sort, Merge Sort, Quick Sort, and Heap Sort; animated vertical bars; algorithm
selection buttons; animation speed and array-size sliders; shuffle/reset; a
start/pause toggle; and a live stats panel for algorithm, comparisons, swaps,
and elapsed time. The UI should be modern, polished, dark, and vibrant. It must
run by simply opening the file in a browser.

## Product goal

Build a polished educational sorting visualizer that makes each algorithm feel
observable and understandable without requiring users to know algorithm jargon.

## Priorities

1. Keep the deliverable as one self-contained `index.html`.
2. Make the animation reliable before adding polish.
3. Keep every algorithm instrumented with comparisons, swaps/writes, highlighted
   active bars, and sorted-state marking.
4. Include concrete tests for each task so local workers and reviewers can
   evaluate behavior consistently.
5. Keep task size small enough for local LLM implementation and review.

## In scope

- Single-file browser app in `index.html`.
- Plain HTML/CSS/JavaScript, with no build step.
- Optional CDN dependency only if it materially improves the UI and does not
  prevent opening the file directly.
- Six sorting algorithms: Bubble, Insertion, Selection, Merge, Quick, Heap.
- Live animation controls and live stats.
- Static and browser-smoke tests stored outside the app for evaluation.

## Out of scope

- Framework setup, bundlers, transpilers, or package-heavy app structure.
- Backend services.
- Persistent saved arrays or user accounts.
- Benchmark-grade performance claims.
- Exact educational narration for every algorithm step.

## Architecture constraints

- App implementation must remain in `index.html`.
- Test files may live under `tests/` for evaluation, but production app code
  must not be split into separate source files.
- Sorting logic should produce step events that the renderer can animate.
- UI controls should be disabled or guarded while a running sort would make a
  control unsafe.
- The array-size slider must support 10 to 200 elements.
- The speed slider must cover very slow to very fast animation.

## Branches and PRs

- Feature branch: `feature/sorting-viz-test`
- Draft feature PR target: `main`
- Task PR target: `feature/sorting-viz-test`

## Feature acceptance criteria

- [ ] Opening `index.html` directly in a browser shows the visualizer.
- [ ] Users can select all six required algorithms.
- [ ] Bars animate smoothly and visually distinguish default, comparing, and
      sorted states.
- [ ] Start/Pause can pause and resume an in-progress sort.
- [ ] Shuffle & Reset creates a new randomized array and clears stats.
- [ ] Speed and array-size sliders visibly affect the app.
- [ ] Stats update live for algorithm name, comparisons, swaps/writes, and
      elapsed time.
- [ ] Sorting completes correctly for array sizes from 10 through 200.
- [ ] The UI remains polished and readable on common desktop browser sizes.

## Planner notes

The HantaSim attempt failed partly because tasks were too broad and because
worker handoff/review mechanics were not yet branch-centered. This project is
intentionally smaller. Keep each task narrow, require tests with each task, and
stop/re-split if a local model fails twice for the same reason.
