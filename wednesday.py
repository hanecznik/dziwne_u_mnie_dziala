from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time
# import pytest

# @pytest.fixture(scope='web')
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.close()

def test_demo_page():
    service = Service(executable_path = './Users/grapefruit/Desktop/browserdrivers/chromedriver_mac64')
    browser = webdriver.Chrome(service=service)

  # driver = Chrome(executable_path=ChromeDriverManager().install())

    browser.get('https://mdlr-shop.webflow.io/')
    browser.maximize_window()
    browser.implicitly_wait(10)

    web_title = browser.find_element(By.CSS_SELECTOR, "h1[class='logo']").text
    assert web_title == 'MDLR'

    procucts_at_store = browser.find_element(By.LINK_TEXT, 'Tops').click()

    commerce_card = browser.find_element(By.CSS_SELECTOR, 'a[data-node-type="commerce-cart-open-link"]').click()
    browser.implicitly_wait(3)
    closing_comerce_card = browser.find_element(By.CSS_SELECTOR, 'a[data-node-type="commerce-cart-close-link"]').click()

    Subscribe_time = browser.find_element(By.ID, 'name-2')
    Subscribe_time.send_keys('Andrzej')
    browser.implicitly_wait(3)

    Subscribe_last_name = browser.find_element(By.ID, 'email-3')
    Subscribe_last_name.send_keys('Dudek')
    browser.implicitly_wait(3)

    Subscribe_email = browser.find_element(By.ID, 'email-2')
    Subscribe_email.send_keys('noname@noname.pl')

    Click_subsribe_button = browser.find_element(By.XPATH, '//input[@type="submit"]').click()




