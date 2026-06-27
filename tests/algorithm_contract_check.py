#!/usr/bin/env python3

import argparse
import os
import sys

def check_algorithms(algorithms):
    required_files = {
        'bubble': ['index.html'],
        'insertion': ['index.html'],
        'selection': ['index.html']
    }

    for algo in algorithms:
        if algo not in required_files:
            print(f"ERROR: Unknown algorithm '{algo}'.")
            return False

        for file in required_files[algo]:
            if not os.path.exists(file):
                print(f"ERROR: Required file '{file}' for algorithm '{algo}' does not exist.")
                return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check sorting algorithms implementation.')
    parser.add_argument('--algorithms', required=True, help='Comma-separated list of algorithms to check')
    args = parser.parse_args()

    algorithms = [algo.strip() for algo in args.algorithms.split(',')]

    if check_algorithms(algorithms):
        print(f"Algorithm contract check passed for: {', '.join(algorithms)}")
        sys.exit(0)
    else:
        print(f"Algorithm contract check failed for: {', '.join(algorithms)}")
        sys.exit(1)
