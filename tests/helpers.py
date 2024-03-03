def force_click(driver, element):
    driver.execute_script("arguments[0].click();", element)


def scroll_to(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
