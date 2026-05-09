from selenium.webdriver.common.by import By

from base.base_page import BasePage
from data.test_data import ErrorMessages


class UkrNetHomePage(BasePage):
    _EMAIL_INPUT = (By.XPATH, '//input[@name="Login"]')
    _PASSWORD_INPUT = (By.XPATH, '//input[@name="Password"]')
    _SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    _LOGOUT_BUTTON = (By.XPATH, '//div[@class="top-bar__logout"]')
    _ERROR_MESSAGE = (By.XPATH, f"//div[@class='error-text' and .= '{ErrorMessages.UKRNET_INVALID_LOGIN}']")

    def login(self, email: str, password: str) -> None:
        self.type(self._EMAIL_INPUT, email)
        self.type(self._PASSWORD_INPUT, password)
        self.click(self._SUBMIT_BUTTON)

    def is_logged_in(self) -> bool:
        return self.is_element_present(self._LOGOUT_BUTTON)

    def has_login_error(self) -> bool:
        return self.is_element_present(self._ERROR_MESSAGE)
