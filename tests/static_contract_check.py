#!/usr/bin/env python3

import os
import sys

def check_static_contracts():
    required_files = ['index.html']
    missing_files = []

    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print(f"Missing files: {', '.join(missing_files)}")
        return False

    return True

if __name__ == "__main__":
    sys.exit(0 if check_static_contracts() else 1)
