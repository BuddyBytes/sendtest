import smtplib
from email.message import EmailMessage
import schedule
import time

# Sender email address and password
sender_email = "bigot.louis@mail.ru"
password = "xCz6mVbw2TdmZcggjJrn"

# Recipient email address
recipient_email = "ncljescn@hldrive.com"

# SMTP server configuration
smtp_server = "smtp.mail.ru"
port = 465  # Port number for the SMTP server (465 for SSL)

# Email content
message = EmailMessage()
message.set_content("test email")
message["Subject"] = "test email"
message["From"] = sender_email
message["To"] = recipient_email

def send_email():
    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(sender_email, password)
        server.send_message(message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Schedule the send_email function to run every 10 seconds
schedule.every(10).seconds.do(send_email)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        break
