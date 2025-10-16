from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    textbox_username_xpath = "//input[@id='email']"
    textbox_password_xpath = "//input[@id='password']"
    button_login_xpath = "//button[@id='btn-login']"
    error_blankEmail_xpath = "//span[text()='Please enter your email address']"
    error_blankPassword_xpath = "//span[text()='Please enter password']"
    toast_error1_xpath = "//div[text()='The user name or password you entered does not match our records. Please try again or reset your password using Forgot Password.']"
    toast_error2_xpath = "//div[text()='The user name or password you entered does not match our records. Please try again or reset your password using Forgot Password.']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def getTitle(self):
        self.wait.until(EC.title_contains("Login - HRMS Admin"))
        page_title = self.driver.title
        return page_title

    def verifyTitle(self):
        assert "Login - HRMS Admin" == self.getTitle()

    def readUserName(self):
        prefilled_username = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_username_xpath))).text
        return prefilled_username 

    def setUserName(self, username):
        username_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_username_xpath)))
        username_input.click()
        username_input.clear()
        username_input.send_keys(username)

    def setPassword(self,password):
        password_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_password_xpath)))
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))).click()

    def blankEmailandPassword(self):
        blankEmailError = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.error_blankEmail_xpath))).text
        blankPasswordError = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.error_blankPassword_xpath))).text
        return blankEmailError, blankPasswordError

    def blankPassword(self):
        blankPasswordError = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.error_blankPassword_xpath))).text
        return blankPasswordError
    
    def toastError1(self):
        toastErrorMessage = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.toast_error1_xpath))).text
        return toastErrorMessage

    def toastError2(self):
        toastErrorMessage = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.toast_error2_xpath))).text
        return toastErrorMessage