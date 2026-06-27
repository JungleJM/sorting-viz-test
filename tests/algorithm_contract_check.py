from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


def read_index() -> str:
    if not INDEX.exists():
        raise AssertionError("Missing required file: index.html")
    return INDEX.read_text(encoding="utf-8")


def require_any(content: str, tokens: list[str], label: str) -> None:
    if not any(token in content for token in tokens):
        raise AssertionError(f"Missing {label}: expected one of {tokens}")


def require_all(content: str, tokens: list[str], label: str) -> None:
    missing = [token for token in tokens if token not in content]
    if missing:
        raise AssertionError(f"Missing {label}: {', '.join(missing)}")


def check_rendering() -> None:
    content = read_index()
    lowered = content.lower()
    require_all(
        lowered,
        [
            'id="size-slider"',
            'min="10"',
            'max="200"',
            "createelement",
            "class",
            "bar",
            "appendchild",
        ],
        "rendering hooks",
    )
    require_any(content, ["generateRandomArray", "resetArray", "renderBars"], "array lifecycle functions")


def check_controls() -> None:
    content = read_index()
    require_all(
        content,
        ["startPauseBtn", "isSorting", "speedSlider", "speedDelay"],
        "animation control hooks",
    )


def check_algorithm_names(names: list[str]) -> None:
    content = read_index().lower()
    for name in names:
        label = name.strip().lower()
        if not label:
            continue
        compact = re.sub(r"[^a-z]", "", label)
        candidates = {
            label,
            compact,
            f"{label} sort",
            f"{compact}sort",
            f"{compact}-btn",
        }
        if not any(candidate in content for candidate in candidates):
            raise AssertionError(f"Missing algorithm hook or label: {name}")


def check_stats() -> None:
    content = read_index()
    require_all(
        content,
        ["current-algorithm", "comparisons", "swaps", "time-elapsed"],
        "stats fields",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rendering", action="store_true")
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--algorithms", default="")
    args = parser.parse_args()

    if args.rendering or args.all:
        check_rendering()
    if args.controls or args.all:
        check_controls()
    if args.stats or args.all:
        check_stats()
    if args.algorithms or args.all:
        names = args.algorithms.split(",") if args.algorithms else [
            "bubble",
            "insertion",
            "selection",
            "merge",
            "quick",
            "heap",
        ]
        check_algorithm_names(names)
    print("Algorithm contract checks passed.")


if __name__ == "__main__":
    main()
