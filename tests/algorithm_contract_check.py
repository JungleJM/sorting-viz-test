#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path

def check_stats_panel():
    index_path = Path('index.html')
    if not index_path.exists():
        print("ERROR: index.html does not exist.")
        return False

    content = index_path.read_text()
    required_elements = [
        'id="algorithm-name"',
        'id="comparisons"',
        'id="swaps-writes"',
        'id="elapsed-time"'
    ]

    for element in required_elements:
        if element not in content:
            print(f"ERROR: Required stats panel element '{element}' not found.")
            return False

    return True

def check_algorithm_selector():
    index_path = Path('index.html')
    if not index_path.exists():
        print("ERROR: index.html does not exist.")
        return False

    content = index_path.read_text()
    required_algorithms = [
        'bubble-sort',
        'selection-sort',
        'insertion-sort'
    ]

    for algorithm in required_algorithms:
        if f'value="{algorithm}"' not in content:
            print(f"ERROR: Required algorithm '{algorithm}' not found in selector.")
            return False

    return True

def check_sorting_logic():
    index_path = Path('index.html')
    if not index_path.exists():
        print("ERROR: index.html does not exist.")
        return False

    content = index_path.read_text()
    required_functions = [
        'bubbleSort()',
        'selectionSort()',
        'insertionSort()'
    ]

    for func in required_functions:
        if f'{func}(' not in content:
            print(f"ERROR: Required sorting function '{func}' not found.")
            return False

    return True

def check_stats_updates():
    index_path = Path('index.html')
    if not index_path.exists():
        print("ERROR: index.html does not exist.")
        return False

    content = index_path.read_text()
    required_updates = [
        'comparisons++',
        'swapsWrites++',
        'startTime = Date.now()'
    ]

    for update in required_updates:
        if update not in content:
            print(f"ERROR: Required stats update '{update}' not found.")
            return False

    return True

def check_completion_handling():
    index_path = Path('index.html')
    if not index_path.exists():
        print("ERROR: index.html does not exist.")
        return False

    content = index_path.read_text()
    required_elements = [
        'markAllSorted()',
        '.sorted'
    ]

    for element in required_elements:
        if element not in content:
            print(f"ERROR: Required completion handling element '{element}' not found.")
            return False

    return True

def main():
    parser = argparse.ArgumentParser(description='Check algorithm contracts')
    parser.add_argument('--stats', action='store_true', help='Check stats-related contracts')

    args = parser.parse_args()

    if not check_stats_panel():
        sys.exit(1)

    if not check_algorithm_selector():
        sys.exit(1)

    if not check_sorting_logic():
        sys.exit(1)

    if args.stats:
        if not check_stats_updates():
            sys.exit(1)
        if not check_completion_handling():
            sys.exit(1)

    print("All algorithm contract checks passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
