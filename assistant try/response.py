import speech_recognition
import pyttsx3
import pyautogui
pyautogui.hotkey("alt", "tab")


def speak(string):
    engine = pyttsx3.init()
    engine.setProperty("rate", 140) #ses hızı
    engine.setProperty('volume',1) # ses seviyesini 0 ile 1 arasında ayarlama
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #indeks değiştirme, sesleri değiştirir. 0 kadın için
    #engine.save_to_file('Hello World' , 'test.mp3')
    engine.say(string)
    engine.runAndWait()


def transform():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        said = r.listen(source)

        try:
            q = r.recognize_google(said, language='en-in')
            print(f"You said:{q}\n")

        except speech_recognition.UnknownValueError:
            print("Didn't catch that")
            return "Waiting for input"

        except speech_recognition.RequestError:
            print('server down')
            return "Waiting for input"

        except:
            return "Waiting for input"
    return q

voice=transform()
if("hello" in voice):
        voice = str(voice).lower()
        print(voice)
        speak("hello woman")
elif ("what's up" in voice):
    voice = str(voice).lower()
    print(voice)
    speak("fine,you")