from django.core import mail
from django.test import TestCase


class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings(
                EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
        ):
            self.assertEqual(len(mail.outbox), 1)
            # Send message
            mail.send_mail(
                subject="TestSubject here",
                message="Test Here is the message.",
                from_email="stanislav.osipov89@gmail.com",
                recipient_list=["badlolpro@gmail.com"],
                # fail_silently=False,
            )
            # Test that one message has been sent
            self.assertEqual(len(mail.outbox), 1)
            # Verify that the subject of the first message is correct
            self.assertEqual(mail.outbox[0].subject, "Test Subject here")
