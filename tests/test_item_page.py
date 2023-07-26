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
    favourite_title = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div/div")
    element_2 = favourite_title.text
    print(element_2)
    assert element_1 == element_2



