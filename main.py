import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from helpers import force_click, scroll_to


@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.minimize_window()
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_chrome(driver_chrome):
    driver_chrome.get('https://pypi.org/project/pytest/')
    time.sleep(5)


def test_firefox(driver_firefox):
    driver_firefox.get('https://www.frontlineeducation.com/')
    time.sleep(5)

def test_navigate_to_absense(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/solutions/absence-time/')
    assert driver_chrome.title == 'K-12 Absence Management Software | Frontline Absence & Time'

def test_navigate_to_contact_us_from_main(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/')

    css = '.fe-navbar-right li:nth-child(3)'
    element = driver_chrome.find_element(By.CSS_SELECTOR, css)

    element.click()
    time.sleep(5)

    assert driver_chrome.title == 'School Administration Software for K-12 | Frontline Education' or '(1) New Messages!'
    assert driver_chrome.current_url == 'https://www.frontlineeducation.com/contact-us/'

def test_cookies(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/')
    cookie = {'name': 'test', 'value': 'value'}
    driver_chrome.add_cookie(cookie)
    test_cookie = driver_chrome.get_cookie('test')
    driver_chrome.delete_cookie(cookie)

    assert cookie['name'] == test_cookie['name']

def test_get_attribute(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/')

    xpath = "//div[@class='fe-navbar-right']//a[contains(@title, 'Contact')]"
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert element.get_attribute('href') == 'https://www.frontlineeducation.com/contact-us'


def test_get_text(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/')

    xpath = "//div[@class='fe-navbar-right']//a[contains(@title, 'Contact')]"
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert element.text == 'Contact Us'

def test_scroll_to(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/')

    scroll_to(driver_chrome)

    time.sleep(10)

def test_send_keys(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/')

    xpath = '//a[@id="fe-nav-search-btn"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()

    css = '#fe-search-box'
    el = driver_chrome.find_element(By.CSS_SELECTOR, css)
    el.send_keys('school administration')
    el.submit()
    assert 'school administration' in driver_chrome.title

def test_is_displayed(driver_chrome):
    driver_chrome.get('https://www.frontlineeducation.com/#')

    xpath = '//a[@id="fe-nav-search-btn"]'
    el = driver_chrome.find_element(By.XPATH, xpath)
    el.click()

    css = '#fe-search-box'
    element = driver_chrome.find_element(By.CSS_SELECTOR, css)

    assert element.is_displayed()

def test_is_displayed_ps(driver_chrome):
    driver_chrome.get('https://www.purestorage.com/')
    time.sleep(5)
    xpath = '//a[@data-an-id="Services & Support"]'
    element = driver_chrome.find_element(By.XPATH, xpath)

    force_click(driver_chrome, element)
    time.sleep(5)
    css = '[class="mt-help mt-inputredirect-input ui-dform-input"]'
    element = driver_chrome.find_element(By.CSS_SELECTOR, css)
    # time.sleep(5)
    assert element.is_displayed()

def test_add_user(driver_chrome):
    driver_chrome.get('http://arquivofosgo.awardspace.info/addauser.php')

    xpath = '//input[@name="username"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('user_114')

    xpath = '//input[@name="password"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('pass_114')

    xpath = '//input[@type="button"]'
    element = driver_chrome.find_element(By.XPATH, xpath)

    element.submit()

def test_login(driver_chrome):
    driver_chrome.get('http://arquivofosgo.awardspace.info/login.php')

    xpath = '//input[@name="username"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('user_114')

    xpath = '//input[@name="password"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('pass_114')

    xpath = '//input[@type="button"]'
    element = driver_chrome.find_element(By.XPATH, xpath)

    element.submit()

    xpath = '//center/b[text()="**Successful Login**"]'
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert element.text == '**Successful Login**'

def test_form(driver_chrome):
    driver_chrome.get('https://demo.guru99.com/test/newtours/register.php')

    xpath = '//input[@name="firstName"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('Dagny')

    xpath = '//input[@name="lastName"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('Taggart')

    xpath = '//input[@name="phone"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('800-423-1273')

    xpath = '//input[@id="userName"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('d.taggart@gmail.com')

    xpath = '//input[@name="address1"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('Pilgrim Lane')

    xpath = '//input[@name="city"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('New York')

    xpath = '//input[@name="state"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('NY')

    xpath = '//input[@name="postalCode"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('11372')

    xpath = '//select[@name="country"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    select = Select(element)
    select.select_by_visible_text('UNITED STATES')

    xpath = '//input[@id="email"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('d.taggart@gmail.com')

    xpath = '//input[@name="password"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('DTaggart123')

    xpath = '//input[@name="confirmPassword"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('DTaggart123')

    xpath = '//input[@name="submit"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    force_click(driver_chrome, element)


    xpath = "//tr//table//font/b"
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert 'Dagny Taggart' in element.text


    xpath = "//tr//table//font/b[contains(text(), 'user name')]"
    el = driver_chrome.find_element(By.XPATH, xpath)

    assert 'd.taggart@gmail.com' in el.text
