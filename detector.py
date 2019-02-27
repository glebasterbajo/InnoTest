# Standard Modules
import os
from collections import deque

# Vendor Modules
import cv2
import numpy as np


class Detector:
    def __init__(self):
        self.__cup_lower = np.array([90, 30, 30])
        self.__cup_upper = np.array([130, 255, 255])

    def find_cup(self, frame):
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
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

                cup = frame[y: y + h, x: x + w]
                self.__find_title(cup)

    def __find_title(self, cup):
        height, weight = cup.shape[:2]
        if weight > 10 and height > 40:
            cup = cup[40:height * 70 // 100, 10:weight * 75 // 100]
        else:
            cup = cup[0:height * 70 // 100, 0:weight * 75 // 100]

        gray = cv2.cvtColor(cup, cv2.COLOR_BGR2GRAY)
        grad_x = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
        grad_y = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
        gradient = cv2.subtract(grad_x, grad_y)
        gradient = cv2.convertScaleAbs(gradient)

        blurred = cv2.blur(gradient, (11, 11))

        _, thresh = cv2.threshold(blurred, 70, 100, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        contours = cv2.findContours(
            closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )[1]

        if len(contours) > 0:
            contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(cup, (x, y), (x + w, y + h), (0, 255, 0), 2)
