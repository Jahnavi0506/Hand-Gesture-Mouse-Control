# Hand-Gesture-Mouse-Control
Hand Gesture Mouse Control using OpenCV, MediaPipe, PyAutoGUI 
This project implements a virtual mouse that can be controlled using hand gestures in real-time. It leverages MediaPipe for hand tracking and PyAutoGUI for system-level mouse control. The index fingertip (ID 8) is used to move the cursor, and a mouse click is triggered when the thumb (ID 4) comes close to it.

🧠 How It Works
Captures video feed from webcam.

Detects hand landmarks using MediaPipe Hands.

Extracts the positions of:

Index finger tip (landmark ID 8) → to control mouse position.

Thumb tip (landmark ID 4) → to detect click gesture.

Computes vertical distance between them.

If distance < threshold (30 pixels), it triggers a mouse click.

Draws:

Circles at key finger points.

Landmark connections.

📷 Visualization
Pink circle → index fingertip

Yellow circle → thumb tip

"Clicking" text appears when fingers are close

Live preview window shows landmarks and motion

🧩 Project Structure
bash
Copy code
hand-gesture-mouse-control/
├── hand_mouse_control.py
├── README.md
