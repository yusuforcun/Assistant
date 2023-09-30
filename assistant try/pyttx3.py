import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 140) #ses hızı
engine.setProperty('volume',1) # ses seviyesini 0 ile 1 arasında ayarlama
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #indeks değiştirme, sesleri değiştirir. 0 kadın için
#engine.save_to_file('Hello World' , 'test.mp3')
engine.say("hello sir , how can help you")
engine.runAndWait()

