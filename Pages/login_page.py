from selenium.webdriver.common.by import By
from actions.Actions import Actions
from Config.config import BasicData
import time


class Login(Actions,BasicData):

    def __int__(self, driver):
        super().__int__(driver)

    """
    Locators of Login Page
    """
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@name='password']")
    log_in = (By.XPATH, "//button[@type='submit']//span[@class='MuiButton-label']")

    def do_login(self):
        self.do_send_keys(self.email, self.EMAIL)
        self.do_send_keys(self.password, self.PASSWORD)
        self.do_click(self.log_in)
        return self.get_title()