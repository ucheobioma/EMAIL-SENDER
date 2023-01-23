import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('template.html').read_text())
# we want to read the text contained in the html file
email = EmailMessage()  # create an email object
email['from'] = 'uche'
email['to'] = 'ucheobioma45@gmail.com'
email['subject'] = 'YOU CAN NOW SPAM PEOPLE'
email.set_content(html.substitute({'name': "uche"}), 'html')


# email.set_content('Ride on uche...youre doing yahoo now lol')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # to alert the sever and establish connection
    smtp.starttls()  # this is an encryption mechanism for connecting securely
    smtp.login('viculstudio@gmail.com', 'oymzyxcewmscgjal')
    smtp.send_message(email)
    print('looks good')

