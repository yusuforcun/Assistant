 
import os 
import random
from winsound import PlaySound
from tts import gTTS

def speak(string):
    tts=gTTS(text=string ,lang="tr",slow=False)
    file=f"soundfile {random.randint(0,100) }.mp3"
    tts.save(file)
    PlaySound("Olive.mp3")
    PlaySound(file)
    os.remove(file)

speak("merhaba")