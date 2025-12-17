import cowsay
import pyttsx3
this = input("What's this? ")
engine = pyttsx3.init()
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
