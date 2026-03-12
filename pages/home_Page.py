from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.menu_button_id = "react-burger-menu-btn"
        self.logout_button_id = "logout_sidebar_link"

    def click_welcome(self):
        self.driver.find_element(By.ID, self.menu_button_id).click()

    def click_logout(self):
        self.driver.find_element(By.ID, self.logout_button_id).click()