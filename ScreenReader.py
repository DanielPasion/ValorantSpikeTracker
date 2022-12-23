import pyautogui
import cv2

#By Taking A Screen Shot of What Area of the screen you want, you can load the png into locateOnScreen and it will tell you what it is
img = cv2.imread(r"C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\Spike.png")
res = pyautogui.locateOnScreen(img)
print(res)

#In coordinate Form
#edit_but = pyautogui.center(res)

#pyautogui.moveTo(edit_but)
