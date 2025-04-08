import subprocess
import time
import requests

BOT_TOKEN = "7988271317:AAGvKF-J6ejr0lCIDKB-b8URwsF5AylRYok"
CHAT_ID = "-1002287107269"

def get_latest_sms():
    try:
        result = subprocess.check_output(["termux-sms-list", "-l", "1"])
        return result.decode("utf-8")
    except Exception as e:
        return None

def notify_bot(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

last_sms = None

while True:
    sms = get_latest_sms()
    if sms and sms != last_sms:
        if "received" in sms.lower() or "credited" in sms.lower():  # UPI SMS keywords
            notify_bot(f"📥 UPI SMS:\n{sms}")
        last_sms = sms
    time.sleep(5)
  
