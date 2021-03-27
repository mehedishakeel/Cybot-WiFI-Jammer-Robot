import cv2 
import os 
cap=cv2.VideoCapture(0) #for Web cam
print("captureing Image") 
for i in range(10): #for 10 Image 
frame=cap.read() # variable of image 
print("Saving Image") # 
cv2.imwrite("text.jpg",frame) 
print("image Save") 
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #CONVERT IMAGE GRAY 
try: 
from PIL import Image 
except ImportError: 
import Image 
import pytesseract 
print("Reading Image") 
text=pytesseract.image_to_string(frame) 
#text = pytesseract.image_to_string(Image.open("ocr_example_1.png")) 
print(text) 
import pyttsx3 
engine = pyttsx3. init() # object creation
rate = engine.getProperty('rate') # getting details of current speaking rate 
print (rate) #printing current voice rate 
engine.setProperty('rate', 125) # setting up new voice rate 
"""VOLUME""" 
volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1) 
print (volume) #printing current volume level 
engine.setProperty('volume',1.0) # setting up volume level between 0 and 1
voices = engine.getProperty('voices') #getting details of current voice 
#engine.setProperty('voice', voices[0].id) #changing index, changes voices. o for male 
engine.setProperty('voice', voices[1].id) #changing index, changes voices. 1 for female 
from gtts import gTTS 
tts = gTTS(text) 
tts.save('output.mp3')
cmd='play ./output.mp3' 
engine.say("Hello World!") 
engine.runAndWait() 
osplay=os.system(cmd) 
#engine.say(text) 
#engine.runAndWait() 
#engine.stop
