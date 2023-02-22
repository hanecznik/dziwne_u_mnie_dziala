from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:/Users/grapefruit/Desktop/browserdrivers/chromedriver_mac64')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.pl")

# # driver = webdriver.Chrome (ChromeDriverManager().install())
# driver.get("https://www.tvn24.pl")
# driver.maximize_window()
# element=WebDriverWait(driver,30)
# # drive.manage().timeouts()implicitlyWait(10, TimeUnit.SECONDS)
# driver.find_element("onetrust-accept-btn-handler").click()
# element=WebDriverWait(driver,15)
# # driver.find_elements("//*[@id="__next"]/div/header/nav/ul/li[2]/ul/li[3]/div/div[1]/button/svg/path")
# driver.close()
#
