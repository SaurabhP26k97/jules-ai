import pytest
from Pages.login_page import Login
from Test.test_base import BaseTest


class Test_Login(BaseTest, Login):

    def test_login_with_valid_details(self):
        self.do_login()

    def test_login_with_invalid_creds(self):
        pass

    def test_login_with_empty_field(self):
        pass

    def test_length_of_email_password_field(self):
        pass


