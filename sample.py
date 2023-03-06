import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
    points = tvn_sport_page.get_amount_of_points_by_club_name('Legia')
    assert points == '46'
