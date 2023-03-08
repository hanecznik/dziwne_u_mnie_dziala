from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

import time


# TODO - I'll be back!
# import pytest
# @pytest.fixture(scope='web')
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.close()

def test_demo_page():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://mdlr-shop.webflow.io/')
    browser.maximize_window()
    browser.implicitly_wait(4)

    web_title = browser.find_element(By.CSS_SELECTOR, "h1[class='logo']").text
    assert web_title == 'MDLR'

    procucts_at_store = browser.find_element(By.LINK_TEXT, 'Tops').click()

    browser.find_element(By.CSS_SELECTOR, 'a[data-node-type="commerce-cart-open-link"]').click()
    browser.find_element(By.CSS_SELECTOR, 'a[data-node-type="commerce-cart-close-link"]').click()

    Subscribe_time = browser.find_element(By.ID, 'name-2')
    Subscribe_time.send_keys('Andrzej')

    Subscribe_last_name = browser.find_element(By.ID, 'email-3')
    Subscribe_last_name.send_keys('Dudek')

    Subscribe_email = browser.find_element(By.ID, 'email-2')
    Subscribe_email.send_keys('noname@noname.pl')

    browser.find_element(By.XPATH, '//input[@type="submit"]').click()
    time.sleep(3)
    Subscribe_information = browser.find_element(By.ID, 'wf-form-Subscribe').submit()
    time.sleep(2)
    register_confirmation = browser.find_element(By.CSS_SELECTOR, "div[class='w-form-done'] > div").text
    assert register_confirmation == "Thank you! Your submission has been received!"
    browser.save_screenshot("image.png")
