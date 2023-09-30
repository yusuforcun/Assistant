import speech_recognition

r=speech_recognition.Recognizer()
def record(ask=False):
    with speech_recognition.Microphone() as source:
        if ask :
            print(ask)
        audio = r.listen(source)
        voice=""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except speech_recognition.UnknownValueError :
            print("anlamadım")
        except speech_recognition.RequestError:
            print("System error")
        return voice 
record()