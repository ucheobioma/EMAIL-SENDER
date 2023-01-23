import smtplib
from email.message import EmailMessage

email = EmailMessage()
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("viculstudio@gmail.com", "oymzyxcewmscgjal")

# message to be sent
message = "Ride on uche...youre doing yahoo now lol"

# sending the mail
s.sendmail("viculstudio@gmail.com", "ucheobioma45@gmail.com", message)

# terminating the session
s.quit()