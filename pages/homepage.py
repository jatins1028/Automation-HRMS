import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SignIn:
    button_signin_xpath = "//a[contains(@href,'find-company')]"
    textbox_username_xpath = "(//input[@name='email'])[2]"
    button_continue_xpath = "//button[@id='button-find']"
    email_errorMessage1_xpath = "//div[text()='The email field is required.']"
    email_errorMessage2_xpath = "//div[text()='You have entered invalid credentials. Please check and try again.']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def signin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_signin_xpath))).click()

    def setUserName(self,username):
        username_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_username_xpath)))
        username_input.click()
        username_input.clear()
        username_input.send_keys(username)

    def continueSignIn(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_continue_xpath))).click()

    def noEmailErrorValidation(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.email_errorMessage1_xpath))).text

    def wrongEmailErrorValidation(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.email_errorMessage2_xpath))).text