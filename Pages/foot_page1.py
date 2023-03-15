from selenium.webdriver.common.by import By

from Pages.meteo_page1 import MeteoPage
from Pages.pagebase import PageBase


class FootballPage(PageBase):
    def go_to_meteo_page(self):
        self.click_on((By.LINK_TEXT, "TVN METEO"), 60)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return MeteoPage(self.driver, self.base_url)


