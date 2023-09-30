import random
import os
import time
import speech_recognition
from playsound import playsound
from gtts import gTTS
import webbrowser
from plyer import notification



def speak(string):
    tts=gTTS(text=string ,lang="tr",slow=False)
    file=f"soundfile {random.randint(0,10) }.mp3"
    tts.save(file)
    playsound("Olive.mp3")
    playsound(file)
    os.remove(file)


def record(ask=False):
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except speech_recognition.UnknownValueError:
            speak("anlamadım")
        except speech_recognition.RequestError:
            speak("System error")
        return voice


def response(voice):
    # if "hey " in voice:
        if "merhaba" in voice :
            selection= ["sanada merhaba ","merhaba "]
            speak(random.choice(selection))
            
        if "selam" in voice :
            selection= ["sanada selam ","selam "]
            speak(random.choice(selection))
            
        if "nasılsın" in voice :
            selection=["iyiyim sen nasılsın","iyi sen","iyidir","iyi","aynı","iyiyim siz nasılsınız"]
            speak(random.choice(selection))
     
        if "ne yapıyorsun" in voice:
            speak("hiçbirşey çünkü buna ihtiyacım yok")
            
        if "naber" in voice :
            speak("iyi senden ")
        
        if "kapan" in voice:
            speak("kapanıyor")
            exit()
      
        if "google'da ara" in voice :
            speak("ne arayayım")
            search=record()
            url=f"https://www.google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f"{search} için google'da bulduklarım")
            
        if "youtube'da ara" in voice :
            speak("ne aramamı istersin")
            search=record()
            url=f"https://www.youtube.com/results?search_query={search}"
            webbrowser.get().open(url)
            speak(f"{search} için youtubeda bulunanlar")
          
        if "not et" in voice:
            speak("dosya adı ne ")
            txtfile = record()+".txt"
            speak("ne kaydetmek istiyorsun ")
            text=record()
            f=open(txtfile,"w+",encoding="utf-8")
            f.writelines(text)
            f.close()
            speak("kaydettim")
            speak("rica ederim")
            exit()
            
        if "sadece aç" in voice :
          
            speak("ne açayım")
            app=record()
            apps=["Spotify","Google Chrome","Firefox","opera","visual studio code","pycharm"]
            while True:
                app = str(app)
                app.lower()
                x=apps.index(app)
                if app in apps:
                    os.startfile(app)
                    time.sleep(5)
                    exit()
                else:
                    speak("açmak istediğin uygulamayı tekrar söylermisin") 
                    app=record()    
             
notification.notify(
title='Asistan açıldı',
    message='hi!?',
    app_name='not python',
)
playsound("Olive.mp3")
speak("merhaba")
while True:
    voice = record()
    if voice != '' :
        voice = str(voice).lower()
        print(voice)
        response(voice)
        
        

# import speech_recognition

# import pyttsx3 as pyttsx3

# class main_function :
#     def speak(string):
#         engine = pyttsx3.init()
#         engine.setProperty("rate",140) #sound speed
#         engine.setProperty("volume",1) #sound level
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice',voices[1].id) # 0=woman sound 1=man sound
#         engine.say(string)
#         engine.runAndWait()

#     def response():
#         r=speech_recognition.Recognizer()
#         with speech_recognition.Microphone() as source :
#             q = r.listen(source)
#         try :
#             audio=r.recognize_google(q,language='en-in')
#             print(f"you said :{audio}\n")
#         except speech_recognition.UnknownValueError :
#             print("i didn't understand you , can you repeat")
#             main_function.speak("i didn't understand you , can you repeat")
#         except speech_recognition.RequestError :
#             print("server down")
#             main_function.speak("server down")

# ses = main_function.response()
# if ("hello" in ses):
#     main_function.speak("hello to you")