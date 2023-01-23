import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('template.html').read_text())
# we want to read the text contained in the html file
email = EmailMessage()  # create an email object
email['from'] = #name
email['to'] = #receipient email
email['subject'] = 'YOU CAN NOW SPAM PEOPLE'
email.set_content(html.substitute({'name': name}), 'html')


# email.set_content('Ride on ...youre doing yahoo now lol')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # to alert the sever and establish connection
    smtp.starttls()  # this is an encryption mechanism for connecting securely
    smtp.login('sender_email', generated_key_from_emailing_service)
    smtp.send_message(email)
    print('looks good')

