# Approach 1: Using subtitles
import pydirectinput
import time
import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab

#pydirectinput.click(button="right")

def getTextFromScreen():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # ImageGrab captures the screen image. 
    # Bbox will be used to capture a specific area.  
    cap = ImageGrab.grab()

    # Convert the image to monochrome for it to be easily 
    # read by the OCR.
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
            lang ='eng')

    # Output result to the console for testing purposes
    print(tesstr)


time.sleep(10)
getTextFromScreen()