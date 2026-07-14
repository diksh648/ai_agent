import os
import subprocess

import pywhatkit

from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
twilio_number = "+1234567890"

client = Client(account_sid, auth_token)


def make_call(phone_number):
    try:
        call = client.calls.create(
            to=phone_number,
            from_=twilio_number,
            url="http://demo.twilio.com/docs/voice.xml"
        )

        return f"Calling {phone_number}...\nCall SID: {call.sid}"

    except Exception as e:
        return f"Error: {e}"

def create_folder(folder_name):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return f"Folder '{folder_name}' created successfully on Desktop."
    else:
        return f"Folder '{folder_name}' already exists."


def open_chrome():
    try:
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Chrome opened successfully."
    except:
        return "Chrome not found. Check the installation path."