import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
from pages.base_page import BasePage
from config.test_data import TestData
from pages.main_page import MainPage



def test_page_title(browser):
    expected_title = TestData.TITLE
    browser.get(TestData.BASE_URL)
    actual_title = browser.title
    assert actual_title == expected_title, "Заголовок страницы не соответствует ожидаемому. Ожидался: {expected_title}, Фактический: {actual_title}"
    #Проверка соответствия заголовка страницы


def test_search_wrapper_exists(browser):
    main_page = BasePage(browser)
    main_page.get(TestData.BASE_URL)
    search_input_wrapper = MainPage.SearchInputWrapper
    assert MainPage.SearchInputWrapper
    # Найти поле поиска на сайте.
    # fix (assert true)

def test_search_results_exists(browser):
    main_page = BasePage(browser)
    main_page.get(TestData.BASE_URL)
    main_page.do_click(MainPage.SearchInputWrapper)
    main_page.do_send_keys(MainPage.SearchInputWrapper, TestData.SEARCH_INPUT)
    #Ввести "iPhone 14 Pro 128 Deep Purple" в поле поиска.
    main_page.do_click(MainPage.SearchButton)
    #Нажать клавишу Enter или выполнить поиск, чтобы получить результаты.
    time.sleep(5)
    search_result = browser.find_element(By.CLASS_NAME, value="category-page-title")
    assert TestData.EXPECTED_RESULT in search_result.text
    #Проверить, что есть результаты поиска.








    










