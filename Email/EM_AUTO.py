#!/usr/bin/env python3

import ssl, smtplib


def read_cred():
    user = password = ''
    with open("cred.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        password = file[1].strip()

    return user, password


sender, password = read_cred()

receiver = ""

port = 465

message ="""\
Subject: Welcome To Secure Chat

This is a test mail from python!

Thank you
"""

context = ssl.create_default_context()

print("-----------------Starting to send-----------------")

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as serv:
    serv.login(sender, password)
    serv.sendmail(sender, receiver, message)

print("------------------Email Sent----------------------")
