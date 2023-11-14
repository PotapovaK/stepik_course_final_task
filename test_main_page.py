from .pages.main_page import MainPage
from .pages.login_page import LoginPage


class TestMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_login_page(browser)

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()


