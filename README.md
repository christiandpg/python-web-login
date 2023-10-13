# Test Automation - Web - Python, Pytest, Selenium
The purpose of this project is to implement automated login tests using python for https://www.saucedemo.com/.

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



## Running Tests
### Run All Tests
```pytest -s tests/login_tests.py tests/logout_tests.py```

### Run Specific Tests
#### Login Tests
```pytest -s tests/login_tests.py```

#### Logout Tests
```pytest -s tests/logout_tests.py```

## IDE Integration
This project is configured to work seamlessly with PyCharm. Make sure to set up your IDE following the project's configurations.
