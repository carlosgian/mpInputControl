from test import handDetector
from pynput.keyboard import Key,Controller
import pyautogui
import pydirectinput as pdi
import cv2
import time

keyboard = Controller()

def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        _,img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) > 0:
            pdi.press('z')
            #keyboard.release('z')
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()