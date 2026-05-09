from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple) -> None:
        self.find(locator).click()

    def type(self, locator: tuple, text: str) -> None:
        self.find(locator).send_keys(text)

    def is_element_present(self, locator: tuple) -> bool:
        return len(self.find_all(locator)) > 0

    @property
    def title(self) -> str:
        return self.driver.title
