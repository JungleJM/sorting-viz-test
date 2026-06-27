#!/usr/bin/env python3
import os
import sys
import json

def check_algorithm_contract():
    required_functions = [
        "generateArray",
        "bubbleSort",
        "quickSort",
        "mergeSort"
    ]

    algorithm_file = "specs/sorting-viz-test/algorithm.js"

    if not os.path.exists(algorithm_file):
        print(f"ERROR: Algorithm file '{algorithm_file}' is missing.")
        return False

    with open(algorithm_file, 'r') as f:
        content = f.read()

    for func in required_functions:
        if func not in content:
            print(f"ERROR: Required function '{func}' is missing in algorithm.js.")
            return False

    print("Algorithm contract check passed.")
    return True

if __name__ == "__main__":
    sys.exit(0 if check_algorithm_contract() else 1)
