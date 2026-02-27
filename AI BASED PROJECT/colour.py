import cv2
import numpy as np
import json
import random
import time

with open("gesture_memory.json") as f:
    gesture_db = json.load(f)
    
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
particles = []
last_time = 0
COOLDOWN = 0.4
def extract_features(cnt):
    area = cv2.contourArea(cnt)
    if area < 8000:
        return None

    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    if hull_area == 0:
        return None

    ratio = hull_area / area
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    x, y, w, h = cv2.boundingRect(cnt)
    aspect = w / h if h != 0 else 0

    defect_count = 0
    try:
        hull_idx = cv2.convexHull(cnt, returnPoints=False)
        if hull_idx is not None and len(hull_idx) > 3:
            defects = cv2.convexityDefects(cnt, hull_idx)
            if defects is not None:
                defect_count = defects.shape[0]
    except cv2.error:
        defect_count = 0

    return np.array([ratio, defect_count, aspect])
def classify(feat):
    best_label = None
    best_dist = 1e9

    for label, ref in gesture_db.items():
        dist = np.linalg.norm(feat - np.array(ref))
        if dist < best_dist:
            best_dist = dist
            best_label = label

    return best_label
def create_particles(x, y, color):
    for _ in range(35):
        particles.append(
            {
                "x": x,
                "y": y,
                "vx": random.randint(-6, 6),
                "vy": random.randint(-6, 6),
                "life": 18,
                "color": color,
            }
        )
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(
        hsv,
        np.array([0, 30, 60]),
        np.array([20, 170, 255]),
    )


    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    
    overlay = frame.copy()

    if contours:
        cnt = max(contours, key=cv2.contourArea)
        feat = extract_features(cnt)

        if feat is not None:
            gesture = classify(feat)

            color_map = {
                "FIST": (0, 0, 255),
                "TWO": (0, 255, 0),
                "THREE_FOUR": (255, 0, 255),
                "OPEN": (255, 0, 0),
            }

            color = color_map.get(gesture, (255, 255, 255))

            x, y, w, h = cv2.boundingRect(cnt)
            cx, cy = x + w // 2, y + h // 2

            now = time.time()
            if now - last_time > COOLDOWN:
                cv2.circle(
                    overlay, (cx, cy), 120, (255, 255, 255), -1
                )
                create_particles(cx, cy, color)
                last_time = now

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(
                frame,
                f"Gesture: {gesture}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                2,
            )

    for p in particles[:]:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["life"] -= 1

        if p["life"] <= 0:
            particles.remove(p)
            continue

        cv2.circle(frame, (p["x"], p["y"]), 4, p["color"], -1)

    frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)
    cv2.imshow("Gesture Recognition (Memory Based)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break   
 
cap.release()
cv2.destroyAllWindows() 