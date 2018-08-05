"""User resource workflows"""

from __future__ import annotations

from app import q
from app.models import Task, User
from app.tasks.email import send_welcome_message


def process_new_user(db, user: User) -> User:
    db.session.add(user)
    db.session.commit()

    # send welcome email
    send_welcome_message(user.id)
    job = q.enqueue(send_welcome_message, user.id)
    welcome_email_task = Task(id=job.id, user=user, name="welcome_email")
    db.session.add(welcome_email_task)
    db.session.commit()

    # add task to send email in 10 days

    return user
