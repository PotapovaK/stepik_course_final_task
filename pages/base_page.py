from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


