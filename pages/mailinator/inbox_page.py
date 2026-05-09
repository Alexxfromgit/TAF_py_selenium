from selenium.webdriver.common.by import By

from base.base_page import BasePage


class MailinatorInboxPage(BasePage):
    _SEARCH_INPUT = (By.XPATH, '//input[@class="form-control"]')
    _GO_BUTTON = (By.XPATH, '//button[@class="btn btn-dark"]')

    def search_inbox(self, address: str) -> None:
        self.type(self._SEARCH_INPUT, address)
        self.click(self._GO_BUTTON)

    def has_email_from(self, sender_name: str) -> bool:
        locator = (By.XPATH, f"//td[@title='FROM' and .= '{sender_name}']")
        return self.is_element_present(locator)

    def has_email_with_subject(self, subject: str) -> bool:
        locator = (By.XPATH, f"//div[@class='all_message-min_text' and .= '{subject}']")
        return self.is_element_present(locator)
