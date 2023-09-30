#!/usr/bin/python3

from winsound import PlaySound
import speech_recognition
import pyautogui
import webbrowser
from plyer import notification
import requests
import cv2
import numpy as np
import imutils
import datetime
import os
import random
from gtts import gTTS
from playsound import playsound
from winsound import PlaySound

class main_function :
    def speak(string):
        tts = gTTS(text=string, lang="tr", slow=False)
        file = f"soundfile {random.randint(0, 100)}.mp3"
        tts.save(file)
        playsound("Olive.mp3")
        playsound(file)
        os.remove(file)

    def listen(ask=False):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            if ask:
                print(ask)
            q = r.listen(source)
            audio = ""
            try:
                audio = r.recognize_google(q, language="tr-TR")
                return audio
            except speech_recognition.UnknownValueError:
                print("anlamadım")
            except speech_recognition.RequestError:
                main_function.speak("System arızası")
            return audio

    def notification():
        notification.notify(title='Asistan açıldı',
                        message='hi!?',
                        )

    def response(audio):
        if"Merhaba" in audio:
            selection = ["sanada merhaba" ,"merhaba" ]
            answer=random.choice(selection)
            main_function.speak(answer)
            print(answer)

        elif"ne haber"  in audio :
            selection = ["iyi sen" ,"iyi" , "idare eder" , "sende nasıl" , "güzel gidiyor"]
            answer=random.choice(selection)
            main_function.speak(answer)
            print(answer)
            
        elif"Selam" in audio :
            selection = ["sanada selam" ,"selam" ]
            answer=random.choice(selection)
            main_function.speak(answer)
            print(answer)
        
        elif"Kahve içelim" in audio :
            main_function.speak("neden olmasın ancak yusufla içmeni öneririm")
            print("neden olmasın ancak yusufla içmeni öneririm")
            
        elif"kapan" in audio :
            main_function.speak("kapanıyor")
            print("kapanıyor")
            exit()

        elif"Uygulama aç" in audio :
            function.open_app()
        
        elif"Google'da ara" in audio :
            function.open_google()

        elif "Not et" in audio :
            function.write_note()
        
        elif"telefona bağlan" in audio :
            function.phonecam_connect()
    
        elif"Bugün ne" in audio :
            function.get_today()
            
        elif"saat kaç" in audio :
            function.get_time()
        
        elif"Sesi yükselt" in audio :
            function.volume_up()

        elif"Sesi kıs" in audio :
            function.volume_down()

        elif"Sesi kapat" in audio :
            function.volume_mute()

        elif "kapat" in audio :
            function.close()

        elif"sesi aç" in audio:
            function.volume_mute()

        elif"Enter" in audio :
            function.enter()

        elif"Ekran görüntüsü al" in audio :
            function.printscreen()
            
        elif"Numlock aç"in audio :
            function.numlock()

        elif "Numlock kapa" in audio:
            function.numlock()

        elif"caps lock aç" in audio :
            function.capslock()

        elif"caps lock kapa" in audio:
            function.capslock()

        elif"oynat"in audio :
            function.play_pause()

        elif "durdur" in audio:
            function.play_pause()
            
        elif"temizle"in audio :
            function.clear()
            
        elif"Gmail aç" in audio :
            function.open_gmail()   

        elif"sekme değiştir" in audio :
            function.change_tab()
            
class function :
    def open_app():
        main_function.speak("hangi uygulama")
        app = main_function.listen()
        print(app)
        if(app=="Firefox"):
            pyautogui.hotkey('win')
            pyautogui.write('Firefox')
            pyautogui.press('enter')
        elif(app == "Vs code") :
            pyautogui.hotkey('win')
            pyautogui.write('vs code')
            pyautogui.press('enter')
        elif(app == 'ayarlar'):
            pyautogui.hotkey('win')
            pyautogui.write('settings')
            pyautogui.press('enter')
        elif(app == 'cmd'):
            pyautogui.hotkey('win')
            pyautogui.write('cmd')
            pyautogui.press('enter')
        elif(app == 'v8'):
            pyautogui.hotkey('win')
            pyautogui.write('v8')
            pyautogui.press('enter')
        elif(app == 'led keyboard'):
            pyautogui.hotkey('win')
            pyautogui.write('led keyboard')
            pyautogui.press('enter')
        elif(app == 'control center'):
            pyautogui.hotkey('win')
            pyautogui.write('control center')
            pyautogui.press('enter')
        elif(app == 'fan speed settingc'):
            pyautogui.hotkey('win')
            pyautogui.write('fan speed setting')
            pyautogui.press('enter')
        elif (app == 'Spotify'):
            pyautogui.hotkey('win')
            pyautogui.write('spotify')
            pyautogui.press('enter')
        elif(app == 'opera'):
            pyautogui.hotkey('win')
            pyautogui.write('opera')
            pyautogui.press('enter')
        elif(app == 'brave'):
            pyautogui.hotkey('win')
            pyautogui.write('brave')
            pyautogui.press('enter')
        elif(app == 'pycharm'):
            pyautogui.hotkey('win')
            pyautogui.write('settings')
            pyautogui.press('pycharm')
        elif(app == 'bluetooth'):
            pyautogui.hotkey('win')
            pyautogui.write('blueteooth')
            pyautogui.press('enter')
        elif(app == 'revo uninstaller'):
            pyautogui.hotkey('win')
            pyautogui.write('revo uninstaller')
            pyautogui.press('enter')
        elif(app == 'telefon'):
            pyautogui.hotkey('win')
            pyautogui.write('phone link')
            pyautogui.press('enter')
        elif(app == 'WhatsApp'):
            pyautogui.hotkey('win')
            pyautogui.write('whatsapp')
            pyautogui.press('enter')
        elif(app == 'instagram'):
            pyautogui.hotkey('win')
            pyautogui.write('instagram')
            pyautogui.press('enter')

    def open_google():
        main_function.speak("ne arayayım")
        search = main_function.listen()
        url = f"https://www.google.com/search?q={search}"
        webbrowser.open_new_tab(url)

    def open_youtube():
        main_function.speak("ne arayayım")
        search = main_function.listen()
        url = f"https://www.youtube.com/search?q={search}"
        webbrowser.open_new_tab(url)

    def write_note():
        main_function.speak("dosya adı ne olsun")
        file = main_function.listen()+".txt"
        main_function.speak("ne yazayım")
        text = main_function.listen()
        f = open(file , "w+" ,encoding="utf-8")
        f.writelines(text)
        f.close()
        main_function.speak("kaydedildi")

    def phonecam_connect():
        main_function.speak("telefonunda IP webcam açık olduğundan emin ol")
        # Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
        url = "http://192.168.0.101:8080/shot.jpg"

        # While loop to continuously fetching data from the Url
        while True:
            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=1000, height=1800)
            cv2.imshow("Android_cam", img)

            # Press Esc key to exit
            if cv2.waitKey(1) == 27:
                break

        cv2.destroyAllWindows()

    def get_today():
        bugun = datetime.datetime.now()
        print(bugun.strftime('%d/%m/%Y'))
        main_function.speak(bugun.strftime('%d/%m/%Y'))

    def get_time():
        bugun = datetime.datetime.now()
        print(bugun.strftime('%H:%M:%S'))
        main_function.speak(bugun.strftime('%H:%M:%S'))

    def volume_up():
        x=0
        while x<10 :
            pyautogui.hotkey('volumeup')
            x+=1

    def volume_down():
        x=0
        while x<10 :
            pyautogui.hotkey('volumedown')
            x+=1

    def change_tab():
        pyautogui.hotkey('alt','tab')

    def close():
        pyautogui.hotkey('alt','f4')

    def volume_mute():
        pyautogui.hotkey('volumemute')

    def enter():
        pyautogui.hotkey('enter')

    def printscreen():
        pyautogui.hotkey('win','printscreen')

    def numlock():
        pyautogui.hotkey('numlock')

    def capslock():
        pyautogui.hotkey('capslock')

    def play_pause():
        pyautogui.hotkey('playpause')

    def clear():
        pyautogui.hotkey('clear')

    def open_gmail():
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")



class main :
    main_function.notification()
    main_function.speak("asistan açıldı")
    while True :
     audio = main_function.listen()
     print(audio)
     main_function.response(audio)
     
    



