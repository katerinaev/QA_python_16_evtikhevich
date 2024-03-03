# find_element(By.XPATH, "xpath")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from selenium import webdriver


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_by_name(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    name = 'yandex-tableau-widget'
    assert driver_chrome.find_element(By.NAME, name)


def test_by_id(driver_chrome):
    driver_chrome.get('https://www.wildberries.by/')
    id = 'route-content'
    assert driver_chrome.find_element(By.ID, id)


def test_by_link_text(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    text = 'Научпоп'
    assert driver_chrome.find_element(By.LINK_TEXT, text)


def test_by_partial_link_text(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    text = 'готовилась'
    assert driver_chrome.find_element(By.PARTIAL_LINK_TEXT, text)


def test_by_tag_name(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    tag = 'span'
    driver_chrome.find_element(By.TAG_NAME, tag)


def test_by_class_name(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    class_name = 'tm-adfox-banner__container'
    elements = driver_chrome.find_elements(By.CLASS_NAME, class_name)
    assert len(elements) == 4

    # ---------


def test_by_name_css(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    css = "[name='yandex-tableau-widget']"
    assert driver_chrome.find_element(By.CSS_SELECTOR, css)


def test_by_id_css(driver_chrome):
    driver_chrome.get('https://www.wildberries.by/')
    id = '#route-content'
    assert driver_chrome.find_element(By.CSS_SELECTOR, id)


def test_by_class_name_css(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    class_name = '.da9c.dac2'
    elements = driver_chrome.find_elements(By.CSS_SELECTOR, class_name)
    assert len(elements) == 4


def get_by_class_css(selector):
    return f'[class={selector}]'


def get_locator_by_class(driver, selector):
    selector = get_by_class_css(selector)
    return driver.find_elements(By.CSS_SELECTOR, selector)


def test_by_class_name_cssw(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    assert get_locator_by_class(driver_chrome, 'da9c dac2')


def test_by_xpath(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    xpath = '//form/button/div'
    assert driver_chrome.find_element(By.XPATH, xpath)

def test_by_xpath_attr(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    xpath = '//*[@class="ag15-a"]'
    assert driver_chrome.find_element(By.XPATH, xpath)

def test_by_xpath_text(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    xpath = '//*[text()="Детские товары"] '
    assert driver_chrome.find_element(By.XPATH, xpath)


def test_by_xpath_text_by_contains(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    xpath = '//*[contains(text(),"Детские")]'
    assert driver_chrome.find_element(By.XPATH, xpath)


def get_by_data_id(data_id):
    return f"//*[data-id={data_id}]"

def test_by_data_id(driver_chrome):
    driver_chrome.get('https://www.avito.ru/')
    assert driver_chrome.find_element(get_by_data_id('1838'))
