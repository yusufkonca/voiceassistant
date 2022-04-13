import random
from gtts import gTTS
from playsound import playsound
import os

def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1,1000)
    file = "ses"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Merhaba efendim. Adınız nedir?")