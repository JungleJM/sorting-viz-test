#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

ALGORITHMS = {
    "bubble": "bubbleSort",
    "insertion": "insertionSort",
    "selection": "selectionSort",
    "merge": "mergeSort",
    "quick": "quickSort",
    "heap": "heapSort",
}


def require(content, token, label):
    if token not in content:
        print(f"ERROR: Missing {label}: {token}")
        return False
    return True


def check_algorithms(content, selected):
    ok = True
    for name in selected:
        if name not in ALGORITHMS:
            print(f"ERROR: Unknown algorithm requested: {name}")
            ok = False
            continue
        ok = require(content, f"function* {ALGORITHMS[name]}", f"{name} generator") and ok
        ok = require(content, f'data-algorithm="{name}"', f"{name} control") and ok
    return ok


def check_rendering(content):
    required = [
        "function generateArray",
        "function renderBars",
        "document.createElement",
        'className = "bar"',
        "appendChild",
    ]
    return all(require(content, token, "rendering hook") for token in required)


def check_controls(content):
    required = [
        "startPauseBtn",
        "isRunning",
        "isPaused",
        "speedSlider",
        "speedDelay",
        "sizeSlider",
        "animationTimer",
        "addEventListener",
    ]
    return all(require(content, token, "control hook") for token in required)


def check_stats(content):
    required = [
        "currentAlgorithm",
        "comparisons",
        "swaps",
        "timeElapsed",
        "stats.comparisons",
        "stats.swaps",
        "updateElapsed",
    ]
    return all(require(content, token, "stats hook") for token in required)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algorithms", default=",".join(ALGORITHMS))
    parser.add_argument("--rendering", action="store_true")
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if not INDEX.exists():
        print("ERROR: index.html is missing.")
        return 1

    content = INDEX.read_text(encoding="utf-8")
    selected = [item.strip() for item in args.algorithms.split(",") if item.strip()]
    ok = check_algorithms(content, selected)

    if args.all or args.rendering:
      ok = check_rendering(content) and ok
    if args.all or args.controls:
      ok = check_controls(content) and ok
    if args.all or args.stats:
      ok = check_stats(content) and ok

    if ok:
        print("Algorithm contract check passed.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
