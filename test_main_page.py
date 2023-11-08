from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.test_go_to_login_page()

    def test_go_to_login_page(self, browser):
        browser.get(link)
        login_link = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login_link")))
        login_link.click()

