#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def check_files_exist():
    required_files = [
        'index.html',
        'tests/algorithm_contract_check.py'
    ]

    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"ERROR: Required file '{file_path}' does not exist.")
            return False

    return True

def check_forbidden_paths():
    forbidden_patterns = [
        '.env',
        '.env.*',
        'secrets/**',
        'private/**',
        'credentials/**'
    ]

    for pattern in forbidden_patterns:
        matches = list(Path('.').glob(pattern))
        if matches:
            print(f"ERROR: Forbidden path found: {matches}")
            return False

    return True

def main():
    if not check_files_exist():
        sys.exit(1)

    if not check_forbidden_paths():
        sys.exit(1)

    print("All static contract checks passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
