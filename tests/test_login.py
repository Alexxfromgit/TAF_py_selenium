import unittest

from tests.base_test import BaseTest
from pages.ukrnet.home_page import UkrNetHomePage
from data.test_data import UkrNetCredentials, PageTitles
from config.config import URLs


class TestLogin(BaseTest):
    url = URLs.UKRNET_HOME

    def setUp(self) -> None:
        super().setUp()
        self.login_page = UkrNetHomePage(self.driver)

    def test_invalid_credentials_show_error(self) -> None:
        self.assertEqual(self.login_page.title, PageTitles.UKRNET_HOME)
        self.login_page.login(UkrNetCredentials.INVALID_EMAIL, UkrNetCredentials.VALID_PASSWORD)
        self.assertTrue(self.login_page.has_login_error())

    def test_valid_credentials_log_in(self) -> None:
        self.assertEqual(self.login_page.title, PageTitles.UKRNET_HOME)
        self.login_page.login(UkrNetCredentials.VALID_EMAIL, UkrNetCredentials.VALID_PASSWORD)
        self.assertTrue(self.login_page.is_logged_in())


if __name__ == "__main__":
    unittest.main()
