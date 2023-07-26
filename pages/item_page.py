from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
from pages.base_page import BasePage
from config.test_data import TestData
from pages.search_page import SearchPage

class ItemPage(BasePage):
    favourite_title = (By.CLASS_NAME, "product-card-title")
    item_page_title = (By.CLASS_NAME, "desc-name")
    favourite_button = (By.CSS_SELECTOR, "#product-page > div > div > div.product-wrap > div.product-desc > div > button.btn.product-buttons-favorite.filled.giant > svg > use")


