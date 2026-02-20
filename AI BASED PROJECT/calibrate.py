import cv2
import mediapipe as mp
import json
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
)
cap = cv2.VideoCapture(0)
GESTURES = {
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "OPEN",
}

memory = {}

def extract_vector(hand):
    return np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()

print("Hold gesture steady and press 1–5 to record. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        vec = extract_vector(hand)

        key = cv2.waitKey(1) & 0xFF
        if chr(key) in GESTURES:
            name = GESTURES[chr(key)]
            memory.setdefault(name, []).append(vec.tolist())
            print(f"Saved sample for {name}")

        mp.solutions.drawing_utils.draw_landmarks(
            frame, hand, mp_hands.HAND_CONNECTIONS
        )

    cv2.imshow("Calibration (MediaPipe)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

with open("gesture_memory.json", "w") as f:
    json.dump(memory, f)
cap.release()
cv2.destroyAllWindows()