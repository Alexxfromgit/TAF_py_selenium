from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config.config import CHROMEDRIVER_PATH


class DriverFactory:
    @staticmethod
    def get_driver(browser: str = "chrome") -> webdriver.Chrome:
        if browser.lower() == "chrome":
            service = Service(executable_path=CHROMEDRIVER_PATH)
            return webdriver.Chrome(service=service)
        raise ValueError(f"Unsupported browser: {browser}")
