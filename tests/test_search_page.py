import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
from pages.base_page import BasePage
from config.test_data import TestData
from pages.search_page import SearchPage


#Найти продукт "iPhone 14 Pro 128 Deep Purple" среди результатов поиска.
#Проверить, что название продукта соответствует "iPhone 14 Pro 128 Deep Purple".
def test_search_iphone_among_result(browser):
    search_page = SearchPage(browser)
    search_page.get(TestData.SEARCH_PAGE_URL)
    element = browser.find_element(By.CSS_SELECTOR, "#search-page > div > div > div > div > div > div.category-page-products > div:nth-child(1) > a")
    assert element.is_displayed()


#5) Кликнуть на продукт "Смартфон Apple iPhone 14 Pro 128 Deep Purple", чтобы открыть его страницу, подождать пока страница загрузится, Проверить, что название продукта на странице соответствует "iPhone 14 Pro 128 Deep Purple
def test_product_card_name(browser):
    search_page = SearchPage(browser)
    search_page.get(TestData.SEARCH_PAGE_URL)
    search_page.do_click(SearchPage.productcard_on_search_page)
    time.sleep(5)
    element = browser.find_element(By.CLASS_NAME, value="desc-name")
    assert element.is_displayed()
    assert TestData.PRODUCT_NAME in element.text















