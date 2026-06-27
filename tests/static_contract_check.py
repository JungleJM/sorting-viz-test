#!/usr/bin/env python3

import sys
from pathlib import Path

def check_index_html_exists():
    """Verify index.html exists."""
    if not Path('index.html').exists():
        print("ERROR: Required file 'index.html' not found.")
        return False
    return True

def main():
    if not check_index_html_exists():
        sys.exit(1)
    print("All static contract checks passed.")

if __name__ == "__main__":
    main()
