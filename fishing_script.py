# Approach 1: Using subtitles
# version: v0.1
import pydirectinput
import time
import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab

def getTextFromScreen():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # ImageGrab captures the screen image. 
    # Bbox will be used to capture a specific area.  
    cap = ImageGrab.grab()

    # Convert the image to monochrome for it to be easily 
    # read by the OCR.
    screen_text = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
            lang ='eng')

    # Output result to the console for testing purposes
    print(screen_text)
    return screen_text


def search_for_bob(screen_text):
    # Searches the given data for the subtitle that represents the fishing rod bobbing down
    bob_string = "fishing bobber splashes"
    screen_text = screen_text.lower()

    if bob_string in screen_text:
        # Right click to reel in
        pydirectinput.click(button="right")
        time.sleep(1.5) # Delay before casting rod again
        pydirectinput.click(button="right")


time.sleep(10)
pydirectinput.click(button="right") # first cast
while True:
    screen_text = getTextFromScreen()
    search_for_bob(screen_text)