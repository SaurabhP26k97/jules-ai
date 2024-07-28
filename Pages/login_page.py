from selenium.webdriver.common.by import By
from actions.Actions import Actions
import time


class Publisher(Actions):

    def __int__(self, driver):
        super().__int__(driver)

    """
    Locators of Login Page
    """
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@name='password']")
    log_in = (By.XPATH, "//button[@type='submit']//span[@class='MuiButton-label']")