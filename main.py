#importing libraries
import os
from dotenv import load_dotenv
load_dotenv() 
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Load environment variables
load_dotenv()

# Get credentials from .env
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
my_phone = os.getenv("MY_PHONE")
client = Client(account_sid, auth_token)

# Function with exception handling for sending message
def sendMessage(reciepent_number, message_body):
    try:
        message = client.messages.create(
            from_=f'{twilio_phone}',
            body=message_body,
            to=f'whatsapp:{reciepent_number}'
        )
        print("Message Sent Successfully")
    except Exception as e:
        print("An Error Occurred:", e)

name = input("Enter recipient name: ")
reciepent_number = input("Enter WhatsApp Number with country code: ")
message_body = input(f"Enter the message for {name}: ")
dateStr = input("Enter the date to send (YYYY-MM-DD): ")
timeStr = input("Enter the time to send (HH:MM): ")

schedule_datetime = datetime.strptime(f'{dateStr} {timeStr}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("Scheduled time is already past.")
else:
    print(f"Message scheduled to send to {name} at {schedule_datetime}")
    time.sleep(delay_seconds)
    # Calling function
    sendMessage(reciepent_number, message_body)
