# Test Automation - Web - Python, Pytest, Selenium
The purpose of this project is to implement automated login tests using python for https://www.saucedemo.com/.
There are positive and negative scenarios and the possibility to run tests in parallel.

## Prerequisites
Ensure you have the following installed before running the project:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Poetry**: [Poetry Installation Guide](https://python-poetry.org/docs/#installation)
- **Web browser driver** for Selenium (e.g., ChromeDriver)

## Setup
1. Clone the repository:
``````
git clone https://github.com/christiandpg/python-web-login.git
cd python-web-login
``````

2. Install dependencies using Poetry:
```poetry install```

3. Install web browser driver (e.g., ChromeDriver) and update the driver path in the configuration if needed.

## PROJECT STRUCTURE
<pre>
project-root
│
├── config
│   └── config.py            # test data - URL, username, password
│   
├── data
│   └── messages.py          # login error messages for validation 
│
├── fixtures
│   └── setup.py             # webdriver configuration / teardown 
│
├── helpers
│   └── selenium_helpers.py  # webDriverWait methods
│
├── pages
│   ├── inventory_page.py    # inventory page object
│   └── login_page.py        # login page object
│
├── tests
│   ├── login_tests.py      # login test scenarios
│   └── logout_tests.py     # logout test scenarios
│
</pre>

## Running Tests
### Run All Tests
```pytest -s tests/login_tests.py tests/logout_tests.py```

### Run All Tests - in parallel
It will run 2 tests in parallel
```pytest -s tests/*_tests.py --verbose -n=2```

It will run 4 tests in parallel
```pytest -s tests/*_tests.py --verbose -n=4```

### Run Specific Tests
#### Login Tests
```pytest -s tests/login_tests.py```

#### Logout Tests
```pytest -s tests/logout_tests.py```

## IDE Integration
This project is configured to work seamlessly with PyCharm. Make sure to set up your IDE following the project's configurations.
