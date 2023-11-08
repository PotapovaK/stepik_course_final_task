from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver.common.by import By
import pytest
import time


class MainPage(BasePage):
    def test_go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        time.sleep(5)
        login_link.click()
