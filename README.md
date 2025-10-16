# Automation-HRMS
Kasturi HRMS Automation Tests

## Overview
This repository contains automation test scripts for the HRMS application.  
The objective is to automate **happy-path scenarios** for core HRMS modules and ensure faster, more reliable regression testing.

## Tech Stack
- **Python 3.10+**
- **Pytest** (test framework)
- **Selenium** (automation tool)
- **Webdriver-Manager** (auto-manages drivers)

## Project Structure
```
Automation-HRMS/
│
├── data/
│   └── logindata.json          # Test data (credentials, input values)
│
├── pages/
│   └── homepage.py             # Page Object files
│
├── tests/
│   ├── login/
│   │   └── test_login_logout.py  # Login & Logout test cases
│   └── conftest.py              # Fixtures and browser setup
│
├── requirements.txt             # Dependencies list
└── README.md                    # Project documentation
```

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/jatins1028/Automation-HRMS.git
cd Automation-HRMS

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run Test Cases
You can execute all test cases using:
pytest --browser_name=chrome

Or run a specific test file:
pytest tests/login/test_login_logout.py -v --browser_name=chrome

## Author
**Jatin Saini**  
Automation Engineer

