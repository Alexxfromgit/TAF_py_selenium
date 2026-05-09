# proj_sel

Selenium-based UI test automation framework for email services, built with Python and the Page Object Model (POM) design pattern.

## What It Tests

| Test Class | Target | Scenario |
|---|---|---|
| `TestALoginPage` | ukr.net | Login with invalid credentials, login with valid credentials |
| `TestBSendingEmail` | mail.ukr.net | Compose and send an email to a Mailinator inbox |
| `TestCEmailinatorInbox` | mailinator.com | Verify the received email's sender and subject |

## Prerequisites

- Python 3.6+
- Google Chrome
- ChromeDriver matching your Chrome version, placed at `C:/webdrivers/chromedriver.exe`
- Selenium installed in your environment:

```bash
pip install selenium
```

## Project Structure

```
proj_sel/
├── base/
│   └── selenium_driver.py      # WebDriver factory (Chrome)
├── pages/
│   └── Login/
│       └── login_page.py       # Page Object — login, email, inbox actions
└── tests/
    └── login_test.py           # Test suite (3 classes, 5 test methods)
```

## Running Tests

Run the full suite from the project root:

```bash
python -m unittest tests/login_test.py
```

Run a single test class:

```bash
python -m unittest tests.login_test.TestALoginPage
```

Run a single test method:

```bash
python -m unittest tests.login_test.TestALoginPage.test_login_valid
```

> **Note:** Test classes are prefixed `A`, `B`, `C` to enforce execution order — `TestB` depends on `TestA` having sent the email that `TestC` then verifies.

## Configuration

The ChromeDriver path is hardcoded in `base/selenium_driver.py`. Update it if your driver lives elsewhere:

```python
driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
```

Test credentials and target addresses are defined in `tests/login_test.py`.
