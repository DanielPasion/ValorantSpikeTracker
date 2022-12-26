import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time

while True:

    #Giving time to switch into valorant
    time.sleep(10)

    #Loading the image of the screen to cap. 1st parameter = Left, 2nd = Top, 3rd = Right, 4th = Bottom. Only is looking at the spike area
    cap = ImageGrab.grab(bbox=(916,8,1004,95)) 

    #Loading cap into an array in order to show it into imshow
    cap_arr = np.array(cap)
    cv2.imshow("",cap_arr)

    #If Presses Escape Key
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()