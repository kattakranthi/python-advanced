import smtplib
from email.mime.text import MIMEText

def send_email_notification(subject, body):
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_username"
    smtp_password = "your_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, [receiver_email], msg.as_string())
        print("Email notification sent.")
    except Exception as e:
        print("Error sending email notification:", str(e))

# Usage
error_message = "Something went wrong in the application."
send_email_notification("Error Alert", error_message)

import re

log_file_path = "path/to/your/logfile.log"
pattern = r"ERROR: (.*)"

with open(log_file_path, "r") as log_file:
    for line in log_file:
        match = re.search(pattern, line)
        if match:
            error_message = match.group(1)
            print("Found error:", error_message)
            # Send notifications here
            send_email_notification("Error that should come to your notice ", error_message):

            
