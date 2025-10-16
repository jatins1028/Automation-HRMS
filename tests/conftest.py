import time
import pytest
import logging
import os
import sys
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--headless", action="store_true", help="Run browser in headless mode"
    )

@pytest.fixture()
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")

    if browser_name == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")  # or "--headless" for older versions
        driver = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)

    elif browser_name == 'edge':
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)

    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def slow_down_each_step():
    time.sleep(3)

@pytest.fixture()
def login_data():
    # with open('../data/loginData.json') as f:
    #     return json.load(f)
    data_path = os.path.join(os.path.dirname(__file__), "../data/logindata.json")
    with open(os.path.abspath(data_path)) as f:
        return json.load(f)
