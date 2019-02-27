# Standard Modules
import os
from collections import deque

# Vendor Modules
import cv2
import numpy as np

# Django Modules
from django.conf import settings


def create_screenshots():
    print("Start creating screenshots...")
    detector = ScreenSaver()
    video = cv2.VideoCapture(
        os.path.join(settings.BASE_DIR, os.pardir, "2018-02-2715_03_24.ogv")
    )
    grabbed, frame = video.read()

    while grabbed:
        if cv2.waitKey(1) & 0xFF == 27:
            break

        detector.find_cup(frame)

        grabbed, frame = video.read()

    video.release()
    print("Done creating screenshots")


class ScreenSaver:
    def __init__(self, num_frames=5):
        self.__counter = 0
        self.__detected = False
        self.__appearing = deque(maxlen=num_frames)
        self.__disappearing = deque(maxlen=num_frames)

        self.__font = cv2.FONT_HERSHEY_SIMPLEX
        self.__cup_lower = np.array([90, 30, 30])
        self.__cup_upper = np.array([130, 255, 255])

    def find_cup(self, frame):
        self.__counter += 1
        blurred = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.__cup_lower, self.__cup_upper)

        contours = [
            contour
            for contour in cv2.findContours(
                mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )[1]
            if cv2.contourArea(contour) > 5000
        ]

        if len(contours) > 0:
            self.__cup_appear(frame)
        else:
            self.__cup_disappear(frame)

    def __cup_disappear(self, frame):
        self.__detected = False
        self.__appearing.append({self.__counter: frame})
        for item in self.__disappearing:
            for key, value in item.items():
                cv2.imwrite(
                    os.path.join(
                        settings.BASE_DIR, "viewer",
                        "static", "viewer", "images", f"d_{key}.jpg"
                    ),
                    value
                )
        self.__disappearing = deque(maxlen=5)

    def __cup_appear(self, frame):
        self.__detected = True
        self.__disappearing.append({self.__counter: frame})
        for item in self.__appearing:
            for key, value in item.items():
                cv2.imwrite(
                    os.path.join(
                        settings.BASE_DIR, "viewer",
                        "static", "viewer", "images", f"a_{key}.jpg"
                    ),
                    value
                )
        self.__appearing = deque(maxlen=5)


def scan(char):
    return int(char) if char.isdigit() else char


def cut(text):
    return scan(text[text.find("_") + 1:text.rfind(".")])
