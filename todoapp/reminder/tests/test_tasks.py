import mock

from django.conf import settings

from reminder.tasks import send_email_notification


class TestReminderTasks(object):
    def test_task_should_call_email_send(self):

        with mock.patch('reminder.tasks.send_mail') as email_send_mock:
            message = 'Hello'
            email = 't@t.com'
            send_email_notification(email, message)
            email_send_mock.assert_called_once_with(
                settings.EMAIL_TEST_SUBJECT,
                message,
                settings.EMAIL_SENDER,
                [email],
                fail_silently=False,
            )
