import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


def test_web_form():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.selenium.dev/selenium/web/web-form.html')
    browser.maximize_window()

    text_input_field = browser.find_element(By.ID, 'my-text-id')
    text_input_field.send_keys('testuję')

    password_field = browser.find_element(By.XPATH, "//input[@name='my-password']")
    password_field.send_keys('12345')

    textarea_field = browser.find_element(By.XPATH, "//textarea[@name='my-textarea']")
    textarea_field.send_keys('uczę się pisać testy')

    dropdown_select = Select(browser.find_element(By.XPATH, "//select[@name='my-select']"))
    dropdown_select.select_by_index("3")

    dropdown_datalist = Select(browser.find_element(By.XPATH, "//input[@name='my-datalist']//following::options[contains(@value, 'Los Angeles')]"))
    dropdown_datalist.select_by_visible_text("Los Angeles")

    browser.find_element(By.ID, 'my-check-1').click()

    browser.find_element(By.XPATH, "//input[contains (@value, '#563d7c')]").click()

    browser.find_element(By.XPATH, "//input[@name='my-date']").send_keys('07/06/2023')

    actions = ActionChains(browser)
    my_range = browser.find_element(By.XPATH, "//input[@name='my-range']")
    for i in range(10):
        my_range.send_keys(Keys.RIGHT)
        time.sleep(1)

    browser.quit()
