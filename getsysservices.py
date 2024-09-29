import psutil, time, requests


url = "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"

while True:
    for service in psutil.win_service_iter():
        data = {
        "content":service.name()
        }
        requests.post(url=url, data=data)
    time.sleep(1800)
