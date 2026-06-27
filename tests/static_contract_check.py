#!/usr/bin/env python3

import os
import sys

def check_files_exist():
    required_files = ['index.html']
    for file in required_files:
        if not os.path.exists(file):
            print(f"ERROR: Required file '{file}' does not exist.")
            return False
    return True

if __name__ == "__main__":
    if check_files_exist():
        print("Static contract check passed.")
        sys.exit(0)
    else:
        print("Static contract check failed.")
        sys.exit(1)
