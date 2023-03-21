import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Pages.hebe_page import HebePage
from Pages.main_page import MainPage
from Pages.rossman_page import RossmanPage


@pytest.fixture()
def browser():
    path = os.path.expanduser("~/Desktop/Driver/chromedriver")
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.close()


def test_check_amount_of_points_by_club_name(browser):
    tvn_sport_page = MainPage.navigate(browser, 'https://eurosport.tvn24.pl')
    title = tvn_sport_page.get_title()
    assert title == 'Sport, Wyniki meczów, Wiadomości sportowe | Eurosport w TVN24'
    points = tvn_sport_page.get_amount_of_points_by_club_name('Legia')
    assert points == '49'
    footbal_page = tvn_sport_page.go_to_football_page()
    title = footbal_page.get_title()
    assert title == 'Piłka nożna | Eurosport w TVN24'
    meteo_page = footbal_page.go_to_meteo_page()
    title = meteo_page.get_title()
    assert title == 'Prognoza pogody i wiadomości pogodowe w TVN Meteo - TVN Meteo'


def test_check_amount_of_points_by_club_name_fluent_api(browser):
    MainPage.navigate(browser, 'https://eurosport.tvn24.pl') \
        .check_title('Sport, Wyniki meczów, Wiadomości sportowe | Eurosport w TVN24') \
        .check_points('Legia', '52') \
        .go_to_football_page() \
        .check_title('Piłka nożna | Eurosport w TVN24') \
        .go_to_meteo_page() \
        .check_title('Prognoza pogody i wiadomości pogodowe w TVN Meteo - TVN Meteo')


def test_hebe_page_menu_items(browser):
    HebePage.navigate(browser, 'https://www.hebe.pl/') \
        .click_all_categories() \
        .click_sub_categories('Top składniki', 'Oleje')


def test_rossman_page_menu(browser):
    items = ['Mycie i pielęgnacja', 'Artykuły higieniczne', 'Jedzenie dla dzieci', 'Akcesoria dla dzieci',
             'Ubranka dla dzieci', 'Zabawki', 'Kobieta w ciąży', 'Karta podarunkowa']
    twarz_items = ['Oczyszczanie i demakijaż', 'Pielęgnacja twarzy', 'Pielęgnacja ust', 'Męska pielęgnacja twarzy',
                   'Karta podarunkowa']
    RossmanPage.navigate(browser, 'https://rossmann.pl') \
        .click_menu_item('Mama i Dziecko') \
        .check_sub_menu_items('Mama i Dziecko', items) \
        .click_menu_item('Twarz') \
        .check_sub_menu_items('Twarz', twarz_items)
