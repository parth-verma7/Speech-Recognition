import pyttsx3 as pt

text_speech=pt.init()

answer=input("What is your name buddy ? ")
text_speech.say(answer)
text_speech.runAndWait()