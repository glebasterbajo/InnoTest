# Standard Modules
import os

# Vendor Modules
import cv2

# Project Modules
from detector import Detector

detector = Detector()
video = cv2.VideoCapture(os.path.join(os.curdir, "2018-02-2715_03_24.ogv"))
cv2.namedWindow("Test", flags=cv2.WINDOW_NORMAL)
grabbed, frame = video.read()

while grabbed:
    if cv2.waitKey(1) & 0xFF == 27:
        break

    detector.find_cup(frame)
    cv2.imshow("Test", frame)

    grabbed, frame = video.read()

video.release()
cv2.destroyAllWindows()
