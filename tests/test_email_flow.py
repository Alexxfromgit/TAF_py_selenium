import unittest

from tests.base_test import BaseTest
from pages.ukrnet.mail_page import UkrNetMailPage
from pages.mailinator.inbox_page import MailinatorInboxPage
from data.test_data import UkrNetCredentials, MailinatorData
from config.config import URLs


class TestSendEmail(BaseTest):
    url = URLs.UKRNET_MAIL

    def setUp(self) -> None:
        super().setUp()
        self.mail_page = UkrNetMailPage(self.driver)

    def test_send_email_to_mailinator(self) -> None:
        self.mail_page.login(UkrNetCredentials.VALID_EMAIL, UkrNetCredentials.VALID_PASSWORD)
        self.mail_page.compose_and_send(MailinatorData.INBOX_ADDRESS, MailinatorData.EXPECTED_SUBJECT)
        self.assertTrue(self.mail_page.is_email_sent())


# TestMailinatorInbox depends on TestSendEmail having delivered an email.
# Run the full suite together: pytest tests/test_email_flow.py
class TestMailinatorInbox(BaseTest):
    url = URLs.MAILINATOR

    def setUp(self) -> None:
        super().setUp()
        self.inbox_page = MailinatorInboxPage(self.driver)

    def test_inbox_shows_sender(self) -> None:
        self.inbox_page.search_inbox(MailinatorData.INBOX_ADDRESS)
        self.assertTrue(self.inbox_page.has_email_from(UkrNetCredentials.DISPLAY_NAME))

    def test_inbox_shows_subject(self) -> None:
        self.inbox_page.search_inbox(MailinatorData.INBOX_ADDRESS)
        self.assertTrue(self.inbox_page.has_email_with_subject(MailinatorData.EXPECTED_SUBJECT))


if __name__ == "__main__":
    unittest.main()
