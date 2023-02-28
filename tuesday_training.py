from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = r' ./Users/grapefruit/Desktop/browserdrivers/chromedriver_mac64')
driver.get("https://www.zooplus.pl/")

driver.maximize_window()
driver.implicitly_wait(3)

cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler'). click()
login_icon = driver.find_element(By.ID, 'shopHeaderAccountLink').click()
mail_log = driver.find_element(By.ID, 'login-email').click()
password = driver.find_element(By.ID, 'login-password').click()
log_in = driver.find_element(By.ID, 'loginButton').click()

driver.quit()
