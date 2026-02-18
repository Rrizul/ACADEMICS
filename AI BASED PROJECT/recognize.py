import cv2
import mediapipe as mp
import numpy as np
import json

# Load saved gesture memory
with open("gesture_memory.json", "r") as f:
    memory = json.load(f)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
)

cap = cv2.VideoCapture(0)

def extract_vector(hand):
    return np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()

def classify(vec):
    best_gesture = None
    best_dist = float("inf")

    for gesture, samples in memory.items():
        mean_vec = np.mean(np.array(samples), axis=0)
        dist = np.linalg.norm(vec - mean_vec)
        if dist < best_dist:
            best_dist = dist
            best_gesture = gesture

    return best_gesture, best_dist

history = []
STABLE_FRAMES = 6

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
        gesture, dist = classify(vec)

        history.append(gesture)
        if len(history) > STABLE_FRAMES:
            history.pop(0)

        final = max(set(history), key=history.count)

        cv2.putText(
            frame,
            f"{final}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.3,
            (0, 255, 0),
            3,
        )

        mp.solutions.drawing_utils.draw_landmarks(
            frame, hand, mp_hands.HAND_CONNECTIONS
        )



    cv2.imshow("Gesture Recognition (Memory + Stable)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()