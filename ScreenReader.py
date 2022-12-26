import pyautogui
import cv2
import time
import threading
import tkinter as tk
import pyglet
from win10toast import ToastNotifier
from playsound import playsound
from PIL import Image, ImageTk
from threading import Timer



########################
###Setting Up THe Gui###
########################

#Nessecary Variables
global spikeOn
spikeOn = False
currentRound = 0
global detOrClock
detOrClock = "clock"

#Prompts
awaitingSpikePrompt ="Current Status: Awaiting Spike To Be Planted" #Prompt for when spike hasnt been planted in the round
spikePlantedPrompt = "Current Status: Spike Has Been Planted" #Prompt for when spike has been planted
spikeDefusedPrompt = "Current Status: Spike Has Been Defused, restarting" #Prompt for When Spike has been defused
spikeDetonatedPrompt = "Current Status: Spike has been Detonated: restarting" #Prompt for when spike has been detonated

#Button Functions
def awaitClock():
    global detOrClock
    detOrClock = "clock"
    print("now clock")

def awaitDetonation():
    global detOrClock
    detOrClock = "detonation"
    print("now detonation")
#Loading the valorant font
pyglet.font.add_file(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\valorant\ValFont.ttf')

#Setting up the window
root = tk.Tk()
root.geometry("450x400")
root.title("Spike Timer")
background = tk.Frame(root,bg="black")
background.place(relx=0,rely=0,relwidth=1,relheight=1)
root.resizable(False, False)

#Setting the valorant logo as the title
logo = Image.open(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\valorant\ValLogo.jpg')
photoImage = ImageTk.PhotoImage(logo)
title_label = tk.Label(root,image=photoImage)
title_label.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

#Saying the description of the app
description_label = tk.Label(root, font=('VALORANT',10), text = "spike countdown extension", fg = "#fa4454")
description_label.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#Initializing Timer
time_label = tk.Label(root, font=("VALORANT",30), text = "Time: 45:00") #Setting up the label
time_label.grid(row=3,column=0,columnspan=2,padx=5,pady=5) #Location of the label

#Setting up the status prompt
status_label = tk.Label(root, font=('VALORANT',10), text = awaitingSpikePrompt, fg = "#fa4454",)
status_label.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

#Setting Up Status for full defusal
fullDefuse_label = tk.Label(root, font=('VALORANT',10), text = "Full Defuse -> Possible", bg = "black",bd="10",)
fullDefuse_label.grid(row=5,column=0,columnspan=2,padx=5,pady=5)

#Setting Up Status for half defusal
halfDefuse_label = tk.Label(root, font=('VALORANT',10), text = "Half Defuse -> Possible", bg = "black", bd="10",)
halfDefuse_label.grid(row=6,column=0,columnspan=2,padx=5,pady=5)

#Detonate Option label
detonation_button = tk.Button(root, font=('VALORANT',10), text = "Click If You Want Program To Restart On Detonation", bg = "#364966", bd="6",command=awaitDetonation)
detonation_button.grid(row=7,column=0,columnspan=2,padx=5,pady=5)

#Clock Option Label
clock_button = tk.Button(root, font=('VALORANT',10), text = "Click If You Want Program To Have A GUI Clock ", bg = "#b38c8f", bd="6",command=awaitClock)
clock_button.grid(row=8,column=0,columnspan=2,padx=5,pady=5)

#Current Functions
def clock():
    #Setting the Timer and figuring out when it ends
    seconds = 45
    afterSeconds = 0
    while (69 != 420):

        #Clock Countdown
        if afterSeconds == 0:
            afterSeconds = 5
            seconds -= 1
        else:
            afterSeconds-=5
    
        if (seconds==7 and afterSeconds==5):
            fullDefuse_label.config(text = "RUN",bg="#fa4454")

        
        if (seconds == 3 and afterSeconds == 5):
            halfDefuse_label.config(text = "RUN",bg="#fa4454")


        time_label.config(text=f"Time: {seconds:02d}:{afterSeconds}0")
        root.update()
        if (seconds == 0 and afterSeconds == 0):
            break
        time.sleep(.5)

def detonation(sc):
    while(sc != None):
        global spikeOn
        sc = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\valorant\Spike.png', grayscale=True, confidence = .35)
        print (sc)
        
    spikeOn = False

def spikeVoiceOverDetonation():

    #Beginning
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\SpikePlantedStartingTimer.wav')
    time.sleep(14)

    if (spikeOn == False):
        exit

    #Twenty
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\TwentySeconds.wav')
    time.sleep(8)
    if (spikeOn == False):
        exit
    
    #Ten
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\TenSeconds.wav')
    time.sleep(2)
    if (spikeOn == False):
        exit

    #Five
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\Five.wav')
    time.sleep(.5)
    if (spikeOn == False):
        exit

    #Four
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\Four.wav')
    time.sleep(.5)
    if (spikeOn == False):
        exit

    #Three
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\Three.wav')
    time.sleep(.5)
    if (spikeOn == False):
        exit

    #Two
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\Two.wav')
    time.sleep(.5)
    if (spikeOn == False):
        exit
    
    #One
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\One.wav')
    time.sleep(.5)
    if (spikeOn == False):
        exit

    #Full Defuse Gone
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\FullDefuseGone.wav')
    if (spikeOn == False):
        exit

    #Two (Half)
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\One.wav')
    time.sleep(.5)
    if (spikeOn == False):
        exit
    
    #One (Half)
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\Two.wav')
    time.sleep(.5)
    if (spikeOn == False):
        exit

    #Half Defuse Gone
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\HalfDefuseGone.wav')
    time.sleep(5)
    if (spikeOn == False):
        exit
    
    #Restarting Prompt"
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\RestartingProgram.wav')

def spikeVoiceOverClock():
    #Playing the Plankton Sound
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\SpikeAudioFile.mp3')

    #Restarting Prompt"
    playsound(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\audiofilesplankton\RestartingProgram.wav')


#Main Program
while(True):#Infinite Loop

    #Initalizing/Resettign the Timer
    sc = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\valorant\Spike.png', grayscale=True, confidence = .7)#image recognition
    defusedOrDetonated = "Neither" #Checking to see if the spike was defused or detonated
    status_label.config(text = awaitingSpikePrompt, bg="white") #Status of spike at the moment
    root.update()
    print(f"Succseful Launch, Current Round: {currentRound}")#System Message To Show the Current round

    #Waiting For Spike to be planted
    while (sc == None):
        sc = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\PersonalProjects\ValorantSpikeTracker\valorant\Spike.png', grayscale=True, confidence = .7)
        root.update()

    #Changing the interface because spike has been planted
    status_label.config(text = spikePlantedPrompt,bg = "#fa4454",fg="black")
    fullDefuse_label.config(bg = "#042e27")
    halfDefuse_label.config(bg = "#042e27")
    defusedOrDetonated = "defused"
    root.update()

    #Starting the timer while threading it
    if (detOrClock == "detonation"):
        time_label.config(text="Time: N/A")
        ongoingSpike_thread = threading.Thread(target=spikeVoiceOverDetonation)
        ongoingSpike_thread.start()
        detonation(sc)

    else:
        ongoingSpike_thread = threading.Thread(target=spikeVoiceOverClock)
        ongoingSpike_thread.start()
        clock()

    status_label.config(text="Restarting Program")
    fullDefuse_label.config(bg = "black")
    halfDefuse_label.config(bg = "black")
    defusedOrDetonated = "neither"
    time_label.config(text="Time: 45:00")
    currentRound += 1
    time.sleep(3)


#countdown_thread = threading.Thread(target = countdown)

#countdown_thread.start()
