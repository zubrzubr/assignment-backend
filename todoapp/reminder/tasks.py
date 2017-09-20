from __future__ import absolute_import, unicode_literals
from todoapp.celery import app


@app.task
def send_email_notification():
    """
    Celery task for sending email notification with reminders to users
    """
    print 'Email sent new'
