import pytest
from Pages.login_page import Login
from Test.test_base import BaseTest


class Test_Login(BaseTest, Login):


    '''
    This class contains all generic function which will be used to interact with web-element
    '''

    #Negative test case
    def test_login_with_invalid_creds(self):
        assert self.login_with_invalid_creds() == "Your email and/or password are incorrects"

    def test_login_with_empty_field(self):
        assert self.login_with_empty_field() == "Required"
    
    def test_microsoft_login_link(self):
        assert self.ms_login_link() == "Sign in to your account"

    def test_login_with_google_link(self):
        assert self.google_login_link() == "Sign in - Google Accounts"

    # Positive test case that will check login
    def test_login_with_valid_details(self):
        assert self.do_login() == "https://demo.haroldwaste.com/"