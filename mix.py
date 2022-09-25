import speech_recognition as sr
import pyttsx3 as pt

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak AnyThing : ')
    audio = r.listen(source)
    query=r.recognize_google(audio)
    print(query)

text_speech=pt.init()

answer=query
text_speech.say(answer)
text_speech.runAndWait()