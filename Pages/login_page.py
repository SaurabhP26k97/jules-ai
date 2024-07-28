from selenium.webdriver.common.by import By
from actions.Actions import Actions
from Config.config import BasicData
import time
from selenium.webdriver.support.ui import WebDriverWait

class Login(Actions,BasicData):

    def __int__(self, driver):
        super().__int__(driver)

    """
    Locators of Login Page
    """
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@name='password']")
    log_in = (By.XPATH, "//button[@type='submit']//span[@class='MuiButton-label']")
    microsoft_login = (By.XPATH, '//*[@id="root"]/div/div[2]/button[1]/span[1]/span')
    google_login = (By.XPATH, '//*[@id="root"]/div/div[2]/button[2]/span[1]/span')
    email_field_required = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div/div[1]/div[3]')
    incoorect_creds = (By.XPATH, '//*[@id="notistack-snackbar"]/div')

    def do_login(self):
        self.do_send_keys(self.email, self.EMAIL)
        self.do_send_keys(self.password, self.PASSWORD)
        self.do_click(self.log_in)
        time.sleep(3)
        return self.get_url()

    def login_with_invalid_creds(self):
        self.do_send_keys(self.email, self.EMAIL)
        self.do_send_keys(self.password, "anything")
        self.do_click(self.log_in)
        time.sleep(5)
        return self.get_text(self.incoorect_creds)

    def ms_login_link(self):
        self.do_click(self.microsoft_login)
        time.sleep(5)
        return self.get_title()

    def google_login_link(self):
        self.do_click(self.google_login)
        time.sleep(5)
        return self.get_title()

    def login_with_empty_field(self):
        self.do_click(self.log_in)
        return self.get_text(self.email_field_required)


