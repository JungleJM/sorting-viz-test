from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


def read_index() -> str:
    if not INDEX.exists():
        raise AssertionError("Missing required file: index.html")
    return INDEX.read_text(encoding="utf-8")


def require_all(content: str, tokens: list[str], label: str) -> None:
    missing = [token for token in tokens if token not in content]
    if missing:
        raise AssertionError(f"Missing {label}: {', '.join(missing)}")


def check_required_controls() -> None:
    content = read_index()
    lowered = content.lower()

    require_all(
        content,
        [
            "Bubble Sort",
            "Insertion Sort",
            "Selection Sort",
            "Merge Sort",
            "Quick Sort",
            "Heap Sort",
        ],
        "algorithm button labels",
    )
    require_all(
        lowered,
        [
            'id="speed-slider"',
            'id="size-slider"',
            'id="shuffle-btn"',
            'id="start-pause-btn"',
            'id="current-algorithm"',
            'id="comparisons"',
            'id="swaps"',
            'id="time-elapsed"',
        ],
        "controls and stats ids",
    )
    if 'id="array-container"' not in lowered and 'id="sorting-visualization"' not in lowered:
        raise AssertionError("Missing visualization container id")
    if "<style" not in lowered or "background" not in lowered:
        raise AssertionError("Missing embedded visual styling")
    if "<script" not in lowered:
        raise AssertionError("Missing embedded script for direct-open app")


if __name__ == "__main__":
    check_required_controls()
    print("Static contract checks passed.")
