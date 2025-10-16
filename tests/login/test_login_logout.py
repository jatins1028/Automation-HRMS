import time

import json
import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conftest import browserInstance
from pages.homepage import SignIn
from pages.loginpage import Login
from pages.employee_dashboard import DropdownMenu

class TestLogin:
    
    # @pytest.mark.skip
    # @pytest.mark.morning
    def test_login_logout_email(self, browserInstance, login_data):
        self.driver = browserInstance
        self.driver.implicitly_wait(10)
        self.driver.get(login_data["baseURLs"]["main"])
        self.driver.maximize_window()

        self.sp = SignIn(self.driver)
        self.sp.signin()
        self.sp.setUserName(login_data["users"]["employee1"]["email"])
        self.sp.continueSignIn()

        self.lp = Login(self.driver)
        self.lp.getTitle()
        self.lp.verifyTitle()
        self.lp.setUserName(login_data["users"]["employee1"]["email"])
        self.lp.setPassword(login_data["users"]["employee1"]["password"])
        self.lp.clickLogin()

        self.dp = DropdownMenu(self.driver)
        self.dp.click_dropdown()
        self.dp.logout()

    # @pytest.mark.skip
    # @pytest.mark.morning
    def test_login_logout_ID(self, browserInstance, login_data):
        self.driver = browserInstance
        self.driver.implicitly_wait(10)
        self.driver.get(login_data["baseURLs"]["main"])
        self.driver.maximize_window()

        self.sp = SignIn(self.driver)
        self.sp.signin()
        self.sp.setUserName(login_data["users"]["employee1"]["employeeID"])
        self.sp.continueSignIn()

        self.lp = Login(self.driver)
        self.lp.getTitle()
        self.lp.verifyTitle()
        self.lp.setUserName(login_data["users"]["employee1"]["employeeID"])
        self.lp.setPassword(login_data["users"]["employee1"]["password"])
        self.lp.clickLogin()

        self.dp = DropdownMenu(self.driver)
        self.dp.click_dropdown()
        self.dp.logout()

    # @pytest.mark.skip
    # @pytest.mark.morning
    def test_login_logout_Phone(self, browserInstance, login_data):
        self.driver = browserInstance
        self.driver.implicitly_wait(10)
        self.driver.get(login_data["baseURLs"]["main"])
        self.driver.maximize_window()

        self.sp = SignIn(self.driver)
        self.sp.signin()
        self.sp.setUserName(login_data["users"]["employee1"]["phone"])
        self.sp.continueSignIn()

        self.lp = Login(self.driver)
        self.lp.getTitle()
        self.lp.verifyTitle()
        self.lp.setUserName(login_data["users"]["employee1"]["phone"])
        self.lp.setPassword(login_data["users"]["employee1"]["password"])
        self.lp.clickLogin()

        self.dp = DropdownMenu(self.driver)
        self.dp.click_dropdown()
        self.dp.logout()

class TestNegativeLogin:
    # @pytest.mark.skip
    # @pytest.mark.morning
    def test_negative_login(self, browserInstance, login_data):
        self.driver = browserInstance
        self.driver.implicitly_wait(10)
        self.driver.get(login_data["baseURLs"]["main"])
        self.driver.maximize_window()

        self.sp = SignIn(self.driver)
        self.sp.signin()
        #Testing signin without passing email in the input box
        self.sp.continueSignIn()
        assert self.sp.noEmailErrorValidation() == "The email field is required."
        #Testing signin using wrong email
        self.sp.setUserName(login_data["negativeCases"]["invalidEmail"])
        self.sp.continueSignIn()
        assert self.sp.wrongEmailErrorValidation() == "You have entered invalid credentials. Please check and try again."
        #Continue test using valid email
        self.sp.setUserName(login_data["users"]["employee1"]["email"])
        self.sp.continueSignIn()

        self.lp = Login(self.driver)
        #Verifying the page title
        self.lp.getTitle()
        self.lp.verifyTitle()
        # Testing login with blank password
        self.lp.clickLogin()
        blankPasswordError = self.lp.blankPassword()
        assert blankPasswordError == "Please enter password"
        time.sleep(6)
        #Testing login page incorrect username and password
        self.lp.setUserName(login_data["negativeCases"]["invalidEmail"])
        self.lp.setPassword(login_data["negativeCases"]["invalidPassword"])
        self.lp.clickLogin()
        assert self.lp.toastError1() == "The user name or password you entered does not match our records. Please try again or reset your password using Forgot Password."
        time.sleep(6)
        #Testing login with correct username and incorrect password
        self.lp.setUserName(login_data["users"]["employee1"]["email"])
        self.lp.setPassword(login_data["negativeCases"]["invalidPassword"])
        self.lp.clickLogin()
        assert self.lp.toastError2() == "The user name or password you entered does not match our records. Please try again or reset your password using Forgot Password."
        time.sleep(6)
        #Testing login with incorrect username and correct password
        self.lp.setUserName(login_data["negativeCases"]["invalidEmail"])
        self.lp.setPassword(login_data["users"]["employee1"]["password"])
        self.lp.clickLogin()
        assert self.lp.toastError1() == "The user name or password you entered does not match our records. Please try again or reset your password using Forgot Password."
        time.sleep(3)

