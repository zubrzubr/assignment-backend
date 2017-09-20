from __future__ import absolute_import, unicode_literals

from django.core.mail import send_mail
from django.conf import settings

from todoapp.celery import app


@app.task
def send_email_notification(email, message):
    """
    Celery task for sending email notification with reminders to users
    """
    send_mail(
        settings.EMAIL_TEST_SUBJECT,
        message,
        settings.EMAIL_SENDER,
        [email],
        fail_silently=False,
    )
