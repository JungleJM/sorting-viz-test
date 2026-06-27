#!/usr/bin/env python3
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


def require(condition, message):
    if not condition:
        print(f"ERROR: {message}")
        return False
    return True


def check_static_contract():
    if not INDEX.exists():
        print("ERROR: index.html is missing.")
        return False

    content = INDEX.read_text(encoding="utf-8")
    lowered = content.lower()
    checks = []

    checks.append(require("<style" in lowered and "</style>" in lowered, "index.html must embed CSS."))
    checks.append(require("<script" in lowered and "</script>" in lowered, "index.html must embed JavaScript."))
    checks.append(require("script src=" not in lowered, "index.html must not load external scripts."))
    checks.append(require("algorithm.js" not in lowered, "index.html must not reference algorithm.js."))
    checks.append(require("visualization.js" not in lowered, "index.html must not reference visualization.js."))

    required_labels = [
        "Bubble Sort",
        "Insertion Sort",
        "Selection Sort",
        "Merge Sort",
        "Quick Sort",
        "Heap Sort",
    ]
    required_ids = [
        "sorting-visualization",
        "array-container",
        "speed-slider",
        "size-slider",
        "shuffle-btn",
        "start-pause-btn",
        "current-algorithm",
        "comparisons",
        "swaps",
        "time-elapsed",
    ]

    for label in required_labels:
        checks.append(require(label in content, f"Missing visible label: {label}"))

    for element_id in required_ids:
        checks.append(require(f'id="{element_id}"' in content, f"Missing required id: {element_id}"))

    size_slider = re.search(r'id="size-slider"[^>]+>', content)
    checks.append(require(size_slider is not None, "Missing size-slider input."))
    if size_slider:
        slider_markup = size_slider.group(0)
        checks.append(require('min="10"' in slider_markup, "size-slider must allow a minimum of 10."))
        checks.append(require('max="200"' in slider_markup, "size-slider must allow a maximum of 200."))

    if all(checks):
        print("Static contract check passed.")
        return True
    return False


if __name__ == "__main__":
    sys.exit(0 if check_static_contract() else 1)
