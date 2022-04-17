import cv2
import numpy as np
import os
import glob
cap = cv2.VideoCapture('Task2/video.mp4')
def load_images():
    images = [cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2GRAY) for file in glob.glob('Task2/images/*')]
    return images


while True:

    ret, frame = cap.read()
    if not ret:
        break
    images = load_images()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    w, h = frame.shape[:2]
    for im in images:
        match = 0
        match = cv2.matchTemplate(grayframe, im, method=cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(frame, top_left, bottom_right, 255, 2)
        frame = cv2.resize(frame, (500,500))
        cv2.imshow("show", frame)
        if match.any():
            print("found something idk")
        print("image changed")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break