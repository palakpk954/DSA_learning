import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_frame)
        gesture = None

        if result.multi_hand_landmarks:
            landmarks = result.multi_hand_landmarks[0]
            self.drawer.draw_landmarks(frame, landmarks, mp.solutions.hands.HAND_CONNECTIONS)

            fingers = self._count_fingers(landmarks)
            if fingers == 1:
                gesture = "ONE"
            elif fingers == 2:
                gesture = "TWO"
            elif fingers == 5:
                gesture = "FIVE"

        return gesture

    def _count_fingers(self, landmarks):
        tip_ids = [4, 8, 12, 16, 20]
        fingers = 0

        for i in range(1, 5):
            if landmarks.landmark[tip_ids[i]].y < landmarks.landmark[tip_ids[i] - 2].y:
                fingers += 1
        return fingers

    def display(self, frame):
        return frame
