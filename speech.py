import speech_recognition as sr
from pygame import mixer
mixer.init()
r = sr.Recognizer()
while 1:
 with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source,phrase_time_limit=3)
        response = r.recognize_google(audio)
        print(response)
        words = [i.lower() for i in response.split()]
        key = ['help', 'help me', 'save']
        if any([(word in key) for word in words]):
             print("Someone needs help")
