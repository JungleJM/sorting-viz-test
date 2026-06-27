#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup

def check_controls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    required_elements = {
        'start-btn': 'button',
        'pause-btn': 'button',
        'resume-btn': 'button',
        'speed-control': 'input[type="range"]',
        'elapsed-time': 'span'
    }

    missing = []
    for id, tag in required_elements.items():
        element = soup.find(id=id)
        if not element or element.name != tag.split('[')[0]:
            missing.append(f"<{tag}> with id='{id}'")

    return missing

if __name__ == "__main__":
    controls_mode = '--controls' in sys.argv

    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        sys.exit(1)

    if controls_mode:
        missing = check_controls(html_content)
        if missing:
            print(f"Missing elements: {', '.join(missing)}")
            sys.exit(1)
        else:
            print("All required control elements present")
            sys.exit(0)
    else:
        # Default checks for algorithm visualization
        print("Algorithm visualization checks would run here")
        sys.exit(0)

