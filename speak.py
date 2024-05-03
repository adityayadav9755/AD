# Importing
import pyttsx3

# Setup & Variables
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)
engine.setProperty('voice', voices[1].id)


# Class
class Speech:

    def speak(self, speech):
        engine.say(speech)
        engine.runAndWait()



