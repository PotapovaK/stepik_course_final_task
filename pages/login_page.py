from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser, timeout=10):
        try:
            WebDriverWait(browser, timeout).until(EC.url_contains("login"))
            assert True, f"Substring 'login' in url"
        except TimeoutException:
            assert False, f"Substring 'login' is not in url"

    def should_be_login_form(self, browser, timeout=10):
        try:
            WebDriverWait(browser, timeout).until(EC.presence_of_element_located(*LoginPageLocators.LOGIN_FORM))
            assert self.should_be_login_form(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self, browser, timeout=10):
        try:
            WebDriverWait(browser, timeout).until(EC.presence_of_element_located(*LoginPageLocators.REGISTER_FORM))
            assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
