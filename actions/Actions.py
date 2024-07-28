import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import os

"""
This class contains all the generic methods and utilities for all the pages
"""


class Actions:

    def __int__(self, driver):
        self.driver = driver

    def do_click(self, element):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(element)).click()

    def do_send_keys(self, element, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).send_keys(value)

    def get_text(self, element):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).text

    def get_rows(self, element):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(element))

    def get_alert(self):
        alert = Alert(self.driver)
        print(alert.text)
        return alert.text

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def switching_between_window(self):
        p = self.driver.current_window_handle
        win = self.driver.window_handles
        for i in win:
            if i != p:
                self.driver.switch_to.window(i)
                break

    def upload_file(self, locator, file):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elem.send_keys(os.getcwd()+file)
