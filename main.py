# send_full.py
import os
import smtplib
import csv, smtplib, ssl, os

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""

SMTP_HOST = os.environ.get(SMTP_HOST)
SMTP_PASSWORD = os.environ.get(SMTP_PASS)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(SMTP_HOST, SMTP_PASSWORD)
    with open("incfo.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )