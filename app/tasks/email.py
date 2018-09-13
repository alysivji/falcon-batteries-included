"""Email tasks

Adapted from https://alysivji.github.io/sending-emails-from-python.html
"""

from email.headerregistry import Address
from email.message import EmailMessage
import smtplib

from .. import db
from ..config import OUTBOUND_EMAIL_ADDRESS, OUTBOUND_EMAIL_PASSWORD, IN_PRODUCTION
from ..models import User
from ..utilities import find_by_id


def _send_email(msg):
    if not IN_PRODUCTION:
        return

    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(OUTBOUND_EMAIL_ADDRESS, OUTBOUND_EMAIL_PASSWORD)
        smtp_server.send_message(msg)

    # TODO should probably log this
    print("Email sent successfully")


def send_welcome_message(user_id):
    subject = "[MovieRecommendation] New User Account Created"
    body = "You have created a new user account."

    user = find_by_id(db=db, model=User, id=user_id, worker_task=True)

    msg = EmailMessage()
    msg["From"] = OUTBOUND_EMAIL_ADDRESS
    msg["To"] = Address(
        display_name=user.full_name,
        username=user.email_username,
        domain=user.email_domain,
    )
    msg["Subject"] = subject
    msg.set_content(body, subtype="html")

    _send_email(msg)

    return f"Welcome email sent for {user.email}"
