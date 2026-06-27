import os

def check_algorithm_modes():
    """Verify algorithm modes are defined in index.html."""
    with open("index.html", "r") as f:
        content = f.read()

    required_modes = [
        "data-bubble-sort",
        "data-quick-sort",
        "data-merge-sort"
    ]

    for mode in required_modes:
        if mode not in content:
            raise AssertionError(f"Missing algorithm mode: {mode}")

if __name__ == "__main__":
    check_algorithm_modes()
    print("Algorithm contract checks passed!")
