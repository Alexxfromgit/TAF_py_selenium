import unittest

from base.driver_factory import DriverFactory
from config.config import IMPLICIT_WAIT


class BaseTest(unittest.TestCase):
    url: str = ""

    def setUp(self) -> None:
        self.driver = DriverFactory.get_driver()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(IMPLICIT_WAIT)

    def tearDown(self) -> None:
        self.driver.quit()
