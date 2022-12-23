import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

while True:

    cap = ImageGrab.grab(bbox=(None))


    #Breaks on Escape Key
    if cv2.waitkey(1) == 27:
        break

cv2.destroyAllWindows()