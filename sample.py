import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Pages.main_page import MainPage


@pytest.fixture()
def browser():
    path = os.path.expanduser("~/Desktop/drivers/chromedriver")
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.close()


def test_check_amount_of_points_by_club_name(browser):
    tvn_sport_page = MainPage(browser, 'https://eurosport.tvn24.pl')
    tvn_sport_page.navigate_to()
    tvn_sport_page.click_on((By.XPATH, '//button[@id="onetrust-accept-btn-handler"]'), 360)
    name = 'Legia'
    selector = f"//td[contains(text(),'{name}')]/parent::tr/td[@class='points']"
    # points = browser.find_element(By.XPATH, selector).text
    # TODO:investigate base page methods
    points = tvn_sport_page.get_amount_of_points_by_club_name('Legia')
    assert points == '46'
    title = tvn_sport_page.get_title()
    assert title == 'Sport, Wyniki meczów, Wiadomości sportowe | Eurosport w TVN24'
