import random
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr

def record():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        voice = r.listen(source)
        try:
            audio = r.recognize_google(voice, language="tr-TR")
        except sr.UnknownValueError:
            speak("Üzgünüm anlayamadım seni. Lütfen tekrar söyler misin?")
            return record()
        except sr.Recognizer:
            speak("Üzgünüm sistem çalışmıyor.")
            return record()
        except sr.WaitTimeoutError:
            speak("Üzgünüm seni duyamadım.")
            return record()
        return audio

def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1,1000)
    file = "ses"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Merhaba efendim. Adınız nedir?")
isim = record()
print(isim)