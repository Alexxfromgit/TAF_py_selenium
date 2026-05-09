# proj_sel

Selenium-based UI test automation framework for email services, built with Python and the Page Object Model (POM) design pattern.

## What It Tests

| Test Class | Target | Scenario |
|---|---|---|
| `TestLogin` | ukr.net | Login with invalid credentials, login with valid credentials |
| `TestSendEmail` | mail.ukr.net | Compose and send an email to a Mailinator inbox |
| `TestMailinatorInbox` | mailinator.com | Verify the received email's sender and subject |

## Prerequisites

- Python 3.6+
- Google Chrome
- ChromeDriver matching your Chrome version, placed at `C:/webdrivers/chromedriver.exe`

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

```
UKRNET_EMAIL=your_email@ukr.net
UKRNET_PASSWORD=your_password
```

## Project Structure

```
proj_sel/
├── config/
│   └── config.py               # URLs, timeouts, chromedriver path
├── data/
│   └── test_data.py            # Expected values and env-loaded credentials
├── base/
│   ├── driver_factory.py       # WebDriver factory (Chrome)
│   └── base_page.py            # Shared Selenium helpers
├── pages/
│   ├── ukrnet/
│   │   ├── home_page.py        # UKR.NET homepage — login & error detection
│   │   └── mail_page.py        # UKR.NET mail — compose & send
│   └── mailinator/
│       └── inbox_page.py       # Mailinator — inbox search & assertions
└── tests/
    ├── base_test.py            # Base test class with driver lifecycle
    ├── test_login.py           # Login validation tests
    └── test_email_flow.py      # Email send + inbox verification
```

## Running Tests

Run the full suite from the project root:

```bash
pytest
```

Run a single file:

```bash
pytest tests/test_login.py
pytest tests/test_email_flow.py
```

Run a single test:

```bash
pytest tests/test_login.py::TestLogin::test_valid_credentials_log_in
```

## Configuration

| What | How |
|---|---|
| ChromeDriver path | Set `CHROMEDRIVER_PATH` env var, or edit `config/config.py` |
| Test credentials | Set `UKRNET_EMAIL` and `UKRNET_PASSWORD` in `.env` |
| Implicit wait | Edit `IMPLICIT_WAIT` in `config/config.py` |

> **Note:** `TestMailinatorInbox` depends on `TestSendEmail` having delivered an email. Run `test_email_flow.py` as a whole, not in isolation.
