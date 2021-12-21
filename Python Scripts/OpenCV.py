import cv2 as cv

img = cv.imread("hand_landmarks.png")

cv.imshow("Image", img)
cv.waitKey(0)