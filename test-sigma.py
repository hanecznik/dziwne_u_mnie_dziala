from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://travel.testsigma.com/")
driver.maximize_window()
time.sleep(5)
x = driver.find_element(By.XPATH, '//*[@id="dropdownMenuButton"]')
x.click()
y = driver.find_element(By.CSS_SELECTOR, ".text-muted.text-center.mt-1")
y.click()
driver.close()
