import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak AnyThing : ')
    audio = r.listen(source)
    query=r.recognize_google(audio)
    print(query)