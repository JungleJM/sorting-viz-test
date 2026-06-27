import os

def check_index_html_exists():
    """Verify index.html exists in the project root."""
    if not os.path.exists("index.html"):
        raise AssertionError("Missing required file: index.html")

def check_required_controls():
    """Check for presence of required controls in index.html."""
    with open("index.html", "r") as f:
        content = f.read()

    required_controls = [
        "<div id='sorting-visualization'>",
        "<button id='start-sort'>",
        "<select id='algorithm-select'>"
    ]

    for control in required_controls:
        if control not in content:
            raise AssertionError(f"Missing required control: {control}")

if __name__ == "__main__":
    check_index_html_exists()
    check_required_controls()
    print("Static contract checks passed!")
