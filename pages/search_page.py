from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from conftest import browser


class SearchPage(BasePage):
    productcard_on_search_page = (By.CSS_SELECTOR, "#search-page > div > div > div > div > div > div.category-page-products > div:nth-child(1) > a")
    product_name_on_productcard = (By.CSS_SELECTOR, "#product-page > div > div > div.product-wrap > div.product-desc > section > h1")

    #локаторы






