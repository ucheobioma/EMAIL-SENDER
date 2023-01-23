import smtplib
from email.message import EmailMessage

email = EmailMessage()
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(sender_email, generated_key)

# message to be sent
message = "Ride on...youre doing yahoo now lol"

# sending the mail
s.sendmail(sender_email, recepient_email, message)

# terminating the session
s.quit()
