import cv2
import mediapipe as mp
import time
import pyautogui
import math

print("\nHand Mouse Gesture Control with Smooth Zoom")

# Screen dimensions
screen_w, screen_h = pyautogui.size()

# Click / cursor variables
last_click_time = 0
double_click_threshold = 0.35
click_cooldown = 0.6
freeze_cursor = False

# Zoom smoothing variables
prev_zoom_dist = None
smoothed_zoom_dist = None
alpha = 0.2                # smoothing factor for zoom
zoom_accumulator = 0.0
zoom_step_threshold = 0.015
zoom_cooldown = 0.12
last_zoom_time = 0

# MediaPipe hands
mp_hands = mp.solutions.hands  # type: ignore
mp_drawing = mp.solutions.drawing_utils  # type: ignore
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Camera
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        # ------------------ TWO HAND SMOOTH ZOOM ------------------
        if len(result.multi_hand_landmarks) == 2:
            hand1 = result.multi_hand_landmarks[0]
            hand2 = result.multi_hand_landmarks[1]

            index1 = hand1.landmark[8]
            index2 = hand2.landmark[8]

            raw_dist = math.hypot(
                index1.x - index2.x,
                index1.y - index2.y
            )

            # Initialize smoothing
            if smoothed_zoom_dist is None:
                smoothed_zoom_dist = raw_dist
                prev_zoom_dist = raw_dist
            else:
                # Exponential Moving Average
                smoothed_zoom_dist = alpha * raw_dist + (1 - alpha) * smoothed_zoom_dist

            delta = smoothed_zoom_dist - prev_zoom_dist  # type: ignore
            prev_zoom_dist = smoothed_zoom_dist

            zoom_accumulator += delta
            current_time = time.time()

            if abs(zoom_accumulator) > zoom_step_threshold:
                if current_time - last_zoom_time > zoom_cooldown:
                    if zoom_accumulator > 0:
                        pyautogui.hotkey('ctrl', '+')
                        cv2.putText(frame, "Zoom In", (10, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else:
                        pyautogui.hotkey('ctrl', '-')
                        cv2.putText(frame, "Zoom Out", (10, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    zoom_accumulator = 0
                    last_zoom_time = current_time

        else:
            # Reset zoom variables if only one hand
            prev_zoom_dist = None
            smoothed_zoom_dist = None
            zoom_accumulator = 0

            # ------------------ SINGLE HAND CONTROL ------------------
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]

                # Finger distance for click
                dist = math.hypot(
                    thumb_tip.x - index_tip.x,
                    thumb_tip.y - index_tip.y
                )

                current_time = time.time()

                # Single / double click
                if dist < 0.05:
                    if current_time - last_click_time < double_click_threshold:
                        pyautogui.doubleClick()
                        last_click_time = 0
                        cv2.putText(frame, "Double Click", (10, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    elif current_time - last_click_time > click_cooldown:
                        pyautogui.click()
                        last_click_time = current_time
                        cv2.putText(frame, "Single Click", (10, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    freeze_cursor = False

                # Move cursor by index finger
                if not freeze_cursor:
                    screen_x = int(index_tip.x * screen_w)
                    screen_y = int(index_tip.y * screen_h)
                    pyautogui.moveTo(screen_x, screen_y, duration=0.0)

    # Show frame
    cv2.imshow("Hand Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
