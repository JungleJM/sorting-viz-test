import sys
import argparse

def check_control_elements():
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
            print(f"Missing control element: {element}")
            return False

    print("All required control elements present")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--controls', action='store_true')
    args = parser.parse_args()

    if args.controls:
        sys.exit(0 if check_control_elements() else 1)
