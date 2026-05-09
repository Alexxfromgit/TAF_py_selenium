from selenium.webdriver.common.by import By

from base.base_page import BasePage


class UkrNetMailPage(BasePage):
    _EMAIL_INPUT = (By.XPATH, '//input[@name="Login"]')
    _PASSWORD_INPUT = (By.XPATH, '//input[@id="id-2"]')
    _SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    _SIDEBAR_LINK = (By.XPATH, '//span[@class="sidebar__list-link-name"]')
    _COMPOSE_BUTTON = (By.XPATH, '//button[@class="default compose"]')
    _TO_INPUT = (By.XPATH, '//input[@name="toInput"]')
    _SUBJECT_INPUT = (By.XPATH, '//input[@name="subject"]')
    _SEND_BUTTON = (By.XPATH, '//button[@class="default send"]')
    _SEND_SUCCESS = (By.XPATH, '//div[@class="sendmsg__ads-ready"]')

    def login(self, email: str, password: str) -> None:
        self.type(self._EMAIL_INPUT, email)
        self.type(self._PASSWORD_INPUT, password)
        self.click(self._SUBMIT_BUTTON)

    def is_logged_in(self) -> bool:
        return self.is_element_present(self._SIDEBAR_LINK)

    def compose_and_send(self, to: str, subject: str) -> None:
        self.click(self._COMPOSE_BUTTON)
        self.type(self._TO_INPUT, to)
        self.type(self._SUBJECT_INPUT, subject)
        self.click(self._SEND_BUTTON)

    def is_email_sent(self) -> bool:
        return self.is_element_present(self._SEND_SUCCESS)
