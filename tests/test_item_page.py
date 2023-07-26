import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
from pages.base_page import BasePage
from config.test_data import TestData
from pages.item_page import ItemPage

#пункт 7

def test_title_itempage_favouritespage(browser):
    item_page = ItemPage(browser)
    item_page.get(TestData.PRODUCT_PAGE_URL)
    favourite_button = browser.find_element(By.CSS_SELECTOR, "#product-page > div > div > div.product-wrap > div.product-desc > div > button.btn.product-buttons-favorite.filled.giant > svg > use")
    favourite_button.click()
    item_page_title = browser.find_element(By.CLASS_NAME, value="desc-name")
    element_1 = item_page_title.text
    item_page.get(TestData.FAVOURITES_URL)
    favourite_title = browser.find_element(By.CLASS_NAME, value="product-card-title")
    element_2 = favourite_title.text
    assert element_1 == element_2

#8
def test_price_itempage_favourites_search(browser):
    item_page = ItemPage(browser)
    item_page.get(TestData.PRODUCT_PAGE_URL)
    favourite_button = browser.find_element(By.CSS_SELECTOR, "#product-page > div > div > div.product-wrap > div.product-desc > div > button.btn.product-buttons-favorite.filled.giant > svg > use")
    favourite_button.click()

    item_page_price = browser.find_element(By.CSS_SELECTOR, "#product-page > div > div > div.product-wrap > div.product-desc > section > div.desc-price-wrap > div:nth-child(1) > div.desc-price-value")
    element_1 = item_page_price.text
    processed_text = element_1.replace("от 510 900 ₸", "510 900 ₸")

    item_page.get(TestData.FAVOURITES_URL)

    favourites_page_price = browser.find_element(By.CSS_SELECTOR, "#__layout > div > main > div > div > div.favorite-body > div > div > div > div.product-card-content > div.product-card-pay > span")
    element_2 = favourites_page_price.text

    item_page.get(TestData.SEARCH_PAGE_URL)

    search_page_price = browser.find_element(By.CSS_SELECTOR, "#search-page > div > div > div > div > div > div.category-page-products > div:nth-child(1) > div > div.product-card-content > div.product-card-pay > span")
    element_3 = search_page_price.text

    assert processed_text == element_2 == element_3



