import sys

def check_static_contracts():
    # Check that all required elements exist in index.html
    with open('index.html', 'r') as f:
        content = f.read()

    required_elements = [
        '<button id="startBtn">Start</button>',
        '<button id="pauseBtn" disabled>Pause</button>',
        '<button id="resumeBtn" disabled>Resume</button>',
        '<span id="elapsedTime">0s</span>',
        '<input type="range" id="speedSlider" min="1" max="10" value="5">'
    ]

    for element in required_elements:
        if element not in content:
            print(f"Missing required element: {element}")
            return False

    print("All static contracts passed")
    return True

if __name__ == "__main__":
    sys.exit(0 if check_static_contracts() else 1)
