# send_full.py
import os
import smtplib
import csv, smtplib, ssl, os

def mentorEmail(name: str):
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        Check out the new post on the Mailtrap blog:</p>
        <p><a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p>
        <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p>
    </body>
    </html>
    """
    return html

def menteeEmail(name: str):
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        Check out the new post on the Mailtrap blog:</p>
        <p><a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p>
        <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p>
    </body>
    </html>
    """
    return html

SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PASSWORD = os.environ.get("SMTP_PASS")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(SMTP_HOST, SMTP_PASSWORD)
    with open("incfo.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for name, email, grade in reader:
            server.sendmail(
                from_addr=from_address,
                to_addrs=email,
                msg=message.format(name=name,grade=grade),
            )