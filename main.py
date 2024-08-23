import pywhatkit as kit
from datetime import datetime, timedelta

# Define the phone number with the country code, e.g., +1234567890
phone_number = "+1234567890"

# Define the message you want to send
message = "Hello, this is an automated message sent using Python!"

# Define the time to send the message (current time + 1 minute)
now = datetime.now()
send_time = now + timedelta(minutes=1)
hours = send_time.hour
minutes = send_time.minute

# Send the message
kit.sendwhatmsg(phone_number, message, hours, minutes)

print("Message scheduled to be sent.")
