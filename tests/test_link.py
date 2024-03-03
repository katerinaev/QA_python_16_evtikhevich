import pytest
from selenium.webdriver.common.by import By

from tests.helpers import force_click, scroll_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.frontlineeducation.com/"

navigation_links = [
    {"locator": (By.LINK_TEXT, "Contact Us"), "expected_title": "Contact Us Today With Questions | Frontline Education"},
    {"locator": (By.LINK_TEXT, "Sign In"), "expected_title": "Sign in to your Frontline Education Application | Frontline Education"},
]

left_links = [
    {"locator": (By.XPATH, "//*[@id='fe-nav-item-solutions']"), "dropdown_locator": (By.XPATH, "//*[@id='solutions-dropdown-menu']")},
    {"locator": (By.XPATH, "//*[@id='fe-nav-item-resources']"), "dropdown_locator": (By.XPATH, "//*[@id='resources-dropdown-menu']")},
    {"locator": (By.XPATH, "//*[@id='fe-nav-item-about']"), "dropdown_locator": (By.XPATH, "//*[@id='about-dropdown-menu']")},
]

product_links = [
    {"locator": (By.XPATH, "//li[@rel='tab0']"), "expected_title": (By.XPATH, "//h1[text()='Frontline Analytics']")},
    {"locator": (By.XPATH, "//li[@rel='tab1']"), "expected_title": (By.XPATH, "//h1[text()='Frontline HRMS']")},
    {"locator": (By.XPATH, "//li[@rel='tab2']"), "expected_title": (By.XPATH, "//h1[text()='Frontline Recruiting & Hiring']")},
]

hcm_links = [
    {"loc": (By.XPATH, "//h2[text()='Absence & Time']"), "curr_url": "https://www.frontlineeducation.com/solutions/absence-time/"},
    {"loc": (By.XPATH, "//h2[text()='Frontline Central']"), "curr_url": "https://www.frontlineeducation.com/solutions/central/"},
    {"loc": (By.XPATH, "//h2[text()='HRMS']"), "curr_url": "https://www.frontlineeducation.com/solutions/hrms/"},
    {"loc": (By.XPATH, "//h2[text()='Professional Growth']"), "curr_url": "https://www.frontlineeducation.com/solutions/professional-growth/"},
    {"loc": (By.XPATH, "//h2[text()='Recruiting & Hiring']"), "curr_url": "https://www.frontlineeducation.com/solutions/recruiting-hiring/"},
]

social_links = [
    {"locator": (By.XPATH, "//a[@title='Facebook']"), "media_url": "https://www.facebook.com/FrontlineEd"},
    {"locator": (By.XPATH, "//a[@title='Twitter']"), "media_url": "https://twitter.com/i/flow/login?redirect_after_login=%2FFrontlineEdu"},
    {"locator": (By.XPATH, "//a[@title='LinkedIn']"), "media_url": "https://www.linkedin.com/company/frontline-education"},
    {"locator": (By.XPATH, "//a[@title='Instagram']"), "media_url": "https://www.instagram.com/frontlineed/"},
    {"locator": (By.XPATH, "//a[@title='YouTube']"), "media_url": "https://www.youtube.com/c/FrontlineEducation"},
]

@pytest.mark.regression
@pytest.mark.parametrize("link_data", navigation_links)
def test_navigation_links(driver_chrome, link_data):
    driver_chrome.get(url)

    link_element = driver_chrome.find_element(*link_data["locator"])

    link_element.click()

    assert link_data["expected_title"] in driver_chrome.title


@pytest.mark.only
@pytest.mark.parametrize("hcm_data", hcm_links)
def test_solutions_links(driver_chrome, hcm_data):
    driver_chrome.get(url)

    element = driver_chrome.find_element(*hcm_data["loc"])
    driver_chrome.execute_script("arguments[0].scrollIntoView(true);", element)
    force_click(driver_chrome, element)

    WebDriverWait(driver_chrome, 10).until(EC.url_to_be(hcm_data["curr_url"]))

    assert driver_chrome.current_url == hcm_data["curr_url"]


@pytest.mark.regression
@pytest.mark.parametrize("link_data", left_links)
def test_left_bar(driver_chrome, link_data):
    driver_chrome.get(url)

    element = driver_chrome.find_element(*link_data["locator"])
    # WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable(link_data["locator"]))
    element.click()

    dropdowm_menu = driver_chrome.find_element(*link_data["dropdown_locator"])
    assert dropdowm_menu.is_displayed()


@pytest.mark.smoke
@pytest.mark.parametrize("link_data", product_links)
def test_product_tab(driver_chrome, link_data):
    driver_chrome.get(url)

    element = driver_chrome.find_element(*link_data["locator"])
    driver_chrome.execute_script("arguments[0].scrollIntoView(true);", element)
    WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable(link_data["locator"]))
    force_click(driver_chrome, element)

    h1_element = driver_chrome.find_element(*link_data["expected_title"])
    assert h1_element.is_displayed()


@pytest.mark.smoke
@pytest.mark.parametrize("link_data", social_links)
def test_media_links(driver_chrome, link_data):
    driver_chrome.get(url)

    initial_window_handle = driver_chrome.current_window_handle

    element = driver_chrome.find_element(*link_data["locator"])
    scroll_to(driver_chrome)
    force_click(driver_chrome, element)

    WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(2))

    new_window_handle = [handle for handle in driver_chrome.window_handles if handle != initial_window_handle][0]
    driver_chrome.switch_to.window(new_window_handle)

    WebDriverWait(driver_chrome, 10).until(EC.url_to_be(link_data["media_url"]))

    assert driver_chrome.current_url == link_data["media_url"]

    driver_chrome.switch_to.window(initial_window_handle)

