import win32file
import win32con
import time
import requests

TELEGRAM_BOT_TOKEN = '7542385960:AAGQrOg0IX4rOjN4xwj9pIE9-FSe9tC5KWU'
CHAT_ID = '7013139280'



def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_drives():
    drives = []
    bitmask = win32file.GetLogicalDrives()
    for letter in range(26):
        if bitmask & 1:
            drives.append(chr(65 + letter) + ':\\')
        bitmask >>= 1
    return drives



def monitor_usb():
    previous_drives = set(get_drives())
    print("Monitoring USB devices. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
            current_drives = set(get_drives())
            added = current_drives - previous_drives
            removed = previous_drives - current_drives

            for drive in added:
                print(f"USB device added: {drive}")
                send_telegram_message(f"USB device added: {drive}")
                

            for drive in removed:
                print(f"USB device removed: {drive}")

            previous_drives = current_drives
    except KeyboardInterrupt:
        print("Monitoring stopped.")




if __name__ == "__main__":
    monitor_usb()