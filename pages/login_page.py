from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


class LoginPage(BasePage):
    link = "http://selenium1py.pythonanywhere.com"

    def __init__(self, browser):
        super().__init__(browser, LoginPage.link)

    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        current_url = browser.current_url
        assert "login" in str(current_url), f"Substring 'login' is not in url. Current URL: {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"


