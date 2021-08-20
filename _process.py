import os
import sys
from gtts import gTTS
import pygame
import pyttsx3
import speech_recognition as sr

engine = sr.Recognizer()
def greet():
        _era_greet = "Hi there. i am ERA. What i can do for you?"
        language = 'en'
        voice_obj = gTTS(text=_era_greet, lang=language)
        voice_obj.save("greet.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("greet.mp3")
        pygame.mixer.music.play()

def say(_era):
    language = 'en'
    voice_obj = gTTS(text=_era, lang=language)
    voice_obj.save("temp\\say.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp\\say.mp3")
    pygame.mixer.music.play()


def listen():
    while(1):
        try:
            with sr.Microphone() as source:
                engine.adjust_for_ambient_noise(source, duration=0.5)
                user = engine.listen(source)
                r_text = r.recognize_google(audio2)
                r_text = t_text.lower()

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
          
        except sr.UnknownValueError:
            print("unknown error occured")

    return r_text

def tellMe(get_file_name):
    filename = get_file_name
    print("Era: Opps! I have no idea about that what you're saying... :(")
    _count = 0
    while _count <= 3:
        ans = input('Please tell me anwer of that [4 Ans] : ')
        file = open("_data\\" + filename + ".er", "a+")
        file.writelines(ans + "\n")
        _count += 1

