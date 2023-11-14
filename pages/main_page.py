from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    link = "http://selenium1py.pythonanywhere.com"

    def __init__(self, browser):
        super().__init__(browser, MainPage.link)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        time.sleep(5)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

