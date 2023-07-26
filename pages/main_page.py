from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from conftest import browser


class MainPage(BasePage):
    SearchInputWrapper = (By.CSS_SELECTOR, "input.search-input")
    SearchButton = (By.CSS_SELECTOR, "#__layout div.app-toolbar button.btn.search-input-submit.info.small")
    FavoritesButton = (By.CSS_SELECTOR, "favorites_button")
    SearchResult = (By.CSS_SELECTOR, "#search-page > div > div > div > div > div > div.category-page-header > div > span")


    # локаторы

