#!/usr/bin/env python3

import os
import sys

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

    for root, dirs, files in os.walk('.'):
        for file in files:
            for pattern in forbidden_patterns:
                if pattern.endswith('/**'):
                    base_path = pattern[:-3]
                    if file.startswith(base_path):
                        print(f"ERROR: Forbidden path detected: {os.path.join(root, file)}")
                        return False
                elif pattern in file:
                    print(f"ERROR: Forbidden file detected: {os.path.join(root, file)}")
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
