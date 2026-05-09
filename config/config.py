import os


CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "C:/webdrivers/chromedriver.exe")
IMPLICIT_WAIT = 3


class URLs:
    UKRNET_HOME = "https://www.ukr.net"
    UKRNET_MAIL = "https://mail.ukr.net"
    MAILINATOR = "https://www.mailinator.com"
