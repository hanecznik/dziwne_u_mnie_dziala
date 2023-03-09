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
    tvn_sport_page = MainPage.navigate(browser, 'https://eurosport.tvn24.pl')
    title = tvn_sport_page.get_title()
    assert title == 'Sport, Wyniki meczów, Wiadomości sportowe | Eurosport w TVN24'
    points = tvn_sport_page.get_amount_of_points_by_club_name('Legia')
    assert points == '46'
    footbal_page = tvn_sport_page.go_to_football_page()
    title = footbal_page.get_title()
    assert title == 'Piłka nożna | Eurosport w TVN24'
    meteo_page = footbal_page.go_to_meteo_page()
    title = meteo_page.get_title()
    assert title == 'Prognoza pogody i wiadomości pogodowe w TVN Meteo - TVN Meteo'
