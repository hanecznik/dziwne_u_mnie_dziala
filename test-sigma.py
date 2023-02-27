from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui
import time

driver.get("https://travel.testsigma.com/")
driver.maximize.window()
time.sleep(7)
myPageTitle=driver.title
print(myPageTitle)
time.sleep(4)
print("Printed after 4")
def screenshot():
    image = pyautogui.screenshot()
    screenshot.save ('picture_from_pycharm.png')
driver.close()
