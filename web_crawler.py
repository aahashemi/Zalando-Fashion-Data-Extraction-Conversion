from selenium import webdriver
import time

PATH = 'PATH TO YOUR CHROME DRIVER'

def initiate_driver(headless = False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')

    prefs = {
        "translate_whitelists": {"": "en"},
        "translate": {"enabled": "True"}
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(PATH, options=options)
    return driver

def scroll_down_the_page(driver, page ,speed=5):
    y = 10000
    for timer in range(0, speed):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 5000
        time.sleep(1)






