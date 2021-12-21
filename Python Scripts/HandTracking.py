import cv2 as cv
import mediapipe as mp
import math
from mediapipe.python.solutions.hands import HAND_CONNECTIONS

def rescaleFrame(frame, scale=1.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img2 = cv.imread("hand_landmarks.png")
cap = cv.VideoCapture(0)
hands = mp.solutions.hands.Hands()
Draw = mp.solutions.drawing_utils
cx1, cy1, cx2, cy2 = [0, 0, 0, 0]

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            Draw.draw_landmarks(img, handLms, HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 8 or id == 4:
                    cv.circle(img, (cx, cy), 15, (0, 255, 0), thickness=-1)
                if id == 4:
                    cx1, cy1 = cx, cy
                if id == 8:
                    cx2, cy2 = cx, cy
                cv.line(img, (cx1, cy1), (cx2, cy2), (0, 0, 255), thickness=2)
                if (math.sqrt((cx2 - cx1)**2 + (cy2 - cy2)**2)) > 120:
                    re = rescaleFrame(img2)
                    cv.imshow("Resized", re)
                if (math.sqrt((cx2 - cx1)**2 + (cy2 - cy2)**2)) < 80:
                    re = rescaleFrame(img2, scale=0.75)
                    cv.imshow("Resized", re)
    cv.imshow("Webcam", img)
    cv.waitKey(1)