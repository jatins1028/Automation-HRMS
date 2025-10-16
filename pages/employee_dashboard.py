import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class DropdownMenu:
    button_dropdown_xpath = "(//a[@id='dropdownMenuButton1'])[2]"
    button_logout_xpath = "(//a[text()='Logout'])[2]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click_dropdown(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_dropdown_xpath))).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_logout_xpath))).click()