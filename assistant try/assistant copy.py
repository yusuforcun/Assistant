import speech_recognition
import pyttsx3
import pyautogui
import webbrowser
from plyer import notification
import requests
import cv2
import numpy as np
import imutils
import datetime

class main_function :
    def speak(string):
        engine = pyttsx3.init()
        engine.setProperty("rate",120) #sound speed
        engine.setProperty("volume",1) #sound level
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id) # 0=woman sound 1=man sound
        engine.say(string)
        engine.runAndWait()

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
                main_function.speak("i didn't understand you , can you repeat")
            except speech_recognition.RequestError:
                main_function.speak("System error")
            return audio


class function :
    def open_app(app):
        if (app=="firefox"):
            pyautogui.hotkey('win')
            pyautogui.write('Firefox')
            pyautogui.press('enter')
        elif (app == "vs code") :
            pyautogui.hotkey('win')
            pyautogui.write('vs code')
            pyautogui.press('enter')
        elif(app == 'settings'):
            pyautogui.hotkey('win')
            pyautogui.write('settings')
            pyautogui.press('enter')
        elif (app == 'cmd'):
            pyautogui.hotkey('win')
            pyautogui.write('cmd')
            pyautogui.press('enter')
        elif (app == 'v8'):
            pyautogui.hotkey('win')
            pyautogui.write('v8')
            pyautogui.press('enter')
        elif (app == 'led keyboard'):
            pyautogui.hotkey('win')
            pyautogui.write('led keyboard')
            pyautogui.press('enter')
        elif (app == 'control center'):
            pyautogui.hotkey('win')
            pyautogui.write('control center')
            pyautogui.press('enter')
        elif (app == 'fan speed settingc'):
            pyautogui.hotkey('win')
            pyautogui.write('fan speed setting')
            pyautogui.press('enter')
        elif (app == 'opera'):
            pyautogui.hotkey('win')
            pyautogui.write('opera')
            pyautogui.press('enter')
        elif (app == 'brave'):
            pyautogui.hotkey('win')
            pyautogui.write('brave')
            pyautogui.press('enter')
        elif (app == 'pycharm'):
            pyautogui.hotkey('win')
            pyautogui.write('settings')
            pyautogui.press('pycharm')
        elif (app == 'bluetooth'):
            pyautogui.hotkey('win')
            pyautogui.write('blueteooth')
            pyautogui.press('enter')
        elif (app == 'revo uninstaller'):
            pyautogui.hotkey('win')
            pyautogui.write('revo uninstaller')
            pyautogui.press('enter')
        elif (app == 'phone'):
            pyautogui.hotkey('win')
            pyautogui.write('phone link')
            pyautogui.press('enter')
        elif (app == 'whatsapp'):
            pyautogui.hotkey('win')
            pyautogui.write('whatsapp')
            pyautogui.press('enter')
        elif (app == 'instagram'):
            pyautogui.hotkey('win')
            pyautogui.write('instagram')
            pyautogui.press('enter')

    def open_url():
        main_function.speak("what should i look for")
        search = main_function.response()
        url = f"https://www.google.com/search?q={search}"
        webbrowser.open_new_tab(url)

    def open_youtube():
        main_function.speak("what should i look for")
        search = main_function.listen()
        url = f"https://www.youtube.com/search?q={search}"
        webbrowser.open_new_tab(url)

    def write_note():
        main_function.speak("whats file name")
        file = main_function.listen()+"txt"
        main_function.speak("what do you want write")
        text = main_function.listen()
        f = open(file , "w+" ,encoding="utf-8")
        f.writelines(text)
        f.close()
        main_function.speak("saved")

    def phonecam_connect():
        main_function.speak("you should  open the IP webcam ")
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
        print(bugun.strftime('%d/%m/%Y'))
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
    notification.notify(title='Asistan açıldı',
                        message='hi!?',
                        )
    main_function.speak("hello friend")





























