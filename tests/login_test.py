import moment
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from Utils.utils import URL
from pages.login_Page import LoginPage
from pages .home_Page import HomePage
from Utils import utils as utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self,test_setup):
        try:
            driver = test_setup
            driver.get(utils.URL)
            login = LoginPage(driver)
            login.enter_username(utils.USERNAME)
            print("step 1 : user name taken")
            login.enter_password(utils.PASSWORD)
            print("step 2 : password taken")
            login.click_login()
            print("step 3 : button responded")

        except AssertionError as error:
            print("Error detected")
            print(error)
            # currtime =moment.now().strftime("%Y-%m-%d %H:%M:%S")
            # screenshotname = "screenshot" + currtime + ".png"
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("Error detected")

        else:
            print("Test passed")


    def test_logout(self,test_setup):
        try:
            driver = test_setup
            homepage = HomePage(driver)
            homepage.click_welcome()
            print("step 4 : menu button responded")
            homepage.click_logout()
            print("step 5 : log out successful")
            x=driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Error detected")
            print(error)
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise

        except Exception as e:
            print("Error detected")

        else:
            print("Test passed")
