#!/usr/bin/env python3
import os
import sys

def check_static_contract():
    required_files = [
        "index.html",
        "specs/sorting-viz-test/algorithm.js",
        "specs/sorting-viz-test/visualization.js"
    ]

    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"ERROR: Required file '{file_path}' is missing.")
            return False

    print("Static contract check passed.")
    return True

if __name__ == "__main__":
    sys.exit(0 if check_static_contract() else 1)
