#!/usr/bin/env python3

import sys
import json
from pathlib import Path

def check_bubble_sort():
    """Verify bubbleSort function exists and has correct signature."""
    try:
        with open('index.html', 'r') as f:
            content = f.read()

        if 'function bubbleSort()' not in content:
            print("ERROR: Required sorting function 'bubbleSort()' not found.")
            return False

        return True
    except Exception as e:
        print(f"ERROR: Failed to check bubble sort implementation: {e}")
        return False

def main():
    if '--stats' in sys.argv:
        if not check_bubble_sort():
            sys.exit(1)
        print("All algorithm contract checks passed.")
    else:
        print("Algorithm contract checks completed.")

if __name__ == "__main__":
    main()
