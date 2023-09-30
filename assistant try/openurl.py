import webbrowser
import time

url = "http://docs.python.org/"

webbrowser.open_new_tab(url)

open_browser = webbrowser.get('windows-default').open('https://google.com')

open_browser = webbrowser.open('https://www.youtube.com/watch?v=google')
time.sleep(10)