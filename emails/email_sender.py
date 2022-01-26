# -*- coding: utf-8 -*-
"""
Sends email with a personal message as html file.

Created on Wed Jan 26 18:45:54 2022

@author: Farid
"""
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Farid Mo'
email['to'] = 'farid.fm.mohammadi@gmail.com'
email['subject'] = 'Salute from the prince of Nigeria'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('faridmohammadi69@gmail.com', '*****')
    smtp.send_message(email)
    print('Email sent successfully.')
