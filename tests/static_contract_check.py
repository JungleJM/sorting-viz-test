#!/usr/bin/env python3

import os
from bs4 import BeautifulSoup

def check_static_contracts(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    errors = []

    # Check for required elements
    if not soup.find(id='array'):
        errors.append("Missing array container element")

    # Check for script presence
    if not soup.find('script'):
        errors.append("Missing script section")

    return errors

if __name__ == "__main__":
    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        sys.exit(1)

    errors = check_static_contracts(html_content)
    if errors:
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("All static contracts passed")
        sys.exit(0)

