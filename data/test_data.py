import os

from dotenv import load_dotenv

load_dotenv()


class UkrNetCredentials:
    VALID_EMAIL = os.environ["UKRNET_EMAIL"]
    VALID_PASSWORD = os.environ["UKRNET_PASSWORD"]
    INVALID_EMAIL = '{}"{::{|/'
    DISPLAY_NAME = "Test Testing"


class MailinatorData:
    INBOX_ADDRESS = "testrwqrt@mailinator.com"
    EXPECTED_SUBJECT = "testingtheme"


class PageTitles:
    UKRNET_HOME = "UKR.NET: Всі новини України, останні новини дня в Україні та Світі"


class ErrorMessages:
    UKRNET_INVALID_LOGIN = "Неправильно вказано логін чи пароль. Спробуйте знову."
