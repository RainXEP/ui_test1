from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
from pages.base_page import BasePage
from config.test_data import TestData
from pages.favorites_page import FavoritePage

#пункт 6
def test_add_to_favorites(browser):
    favorite_page = FavoritePage(browser)
    favorite_page.get(TestData.PRODUCT_PAGE_URL)
    favourite_button = browser.find_element(By.CSS_SELECTOR, "#product-page > div > div > div.product-wrap > div.product-desc > div > button.btn.product-buttons-favorite.filled.giant > svg > use")
    favourite_button.click()
    favorite_page.get(TestData.FAVOURITES_URL)
    favourites_item = browser.find_element(By.CLASS_NAME, value="product-card-title")
    assert TestData.PRODUCT_NAME in favourites_item.text
