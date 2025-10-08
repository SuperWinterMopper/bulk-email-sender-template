# send_full.py
import os
import smtplib
from email.message import EmailMessage
from mimetypes import guess_type

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

def add_attachment(msg: EmailMessage, filepath: str):
    ctype, encoding = guess_type(filepath)
    if ctype is None:
        ctype = "application/octet-stream"
    maintype, subtype = ctype.split("/", 1)
    with open(filepath, "rb") as f:
        data = f.read()
    msg.add_attachment(data, maintype=maintype, subtype=subtype, filename=os.path.basename(filepath))

def send_email(to_addrs, subject, plain_text, html=None, attachments=None, from_addr=None):
    msg = EmailMessage()
    msg["From"] = from_addr or SMTP_USER
    msg["To"] = ", ".join(to_addrs) if isinstance(to_addrs, (list, tuple)) else to_addrs
    msg["Subject"] = subject
    msg.set_content(plain_text)
    if html:
        msg.add_alternative(html, subtype="html")
    attachments = attachments or []
    for path in attachments:
        add_attachment(msg, path)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)

if __name__ == "__main__":
    html_body = """\
    <html>
      <body>
        <p>Hi!<br>
           This is a <b>HTML</b> email sent from Python.
        </p>
      </body>
    </html>
    """
    send_email(
        ["recipient@example.com"],
        "Fancy email with attachment",
        "This is the plain-text fallback.",
        html=html_body,
        attachments=["/path/to/file.pdf"]
    )
    print("Sent")
