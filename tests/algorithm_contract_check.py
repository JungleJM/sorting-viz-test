#!/usr/bin/env python3

import os
import sys
import argparse

def check_algorithm_controls():
    # Check for animation controls in index.html
    with open('index.html', 'r') as f:
        content = f.read()

    required_elements = [
        '<button id="start-btn">',
        '<button id="pause-btn">',
        '<button id="resume-btn">',
        '<input type="range" id="speed-control">',
        'Elapsed Time'
    ]

    missing_elements = []
    for element in required_elements:
        if element not in content:
            missing_elements.append(element)

    if missing_elements:
        print(f"Missing elements: {', '.join(missing_elements)}")
        return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--controls', action='store_true')
    args = parser.parse_args()

    if args.controls:
        sys.exit(0 if check_algorithm_controls() else 1)
    else:
        print("No checks specified")
        sys.exit(1)
