from selenium.webdriver.common.by import By

from Pages.foot_page1 import FootballPage
from Pages.meteo_page1 import MeteoPage
from Pages.pagebase import PageBase


class MainPage(PageBase):
    @staticmethod
    def navigate(driver, url):
        page = MainPage(driver, url)
        page.navigate_to()
        page.click_on((By.XPATH, '//button[@id="onetrust-accept-btn-handler"]'), 360)
        return page

    def get_amount_of_points_by_club_name(self, name):
        selector = f"//td[contains(text(),'{name}')]/parent::tr/td[@class='points']"
        element = self.find_element((By.XPATH, selector))
        return element.text

    def go_to_football_page(self):
        self.click_on((By.XPATH, "//*[@title='Piłka nożna']"), 60)
        return FootballPage(self.driver, self.base_url)

    def go_to_meteo_page(self):
        self.click_on((By.LINK_TEXT, "TVN METEO"))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return MeteoPage(self.driver, self.base_url)

    def check_points(self, teamname, point):
        points = self.get_amount_of_points_by_club_name(teamname)
        assert points == point
        return self
