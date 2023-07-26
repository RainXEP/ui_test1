from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser

class BasePage(object):
    def __init__(self, browser):
        self.browser = browser


    def get(self, url):
        self.browser.get(url)


    def refresh(self):
        self.browser.refresh()


    def do_click(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        element.click()


    def get_title(self, title):
        WebDriverWait(self.browser, 10).until(EC.title_is(title))
        return self.browser.title

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)

    def is_exist(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_element_text(self, by_locator):
        item_page_title = self.browser.find_element(by_locator)
        return item_page_title.text









