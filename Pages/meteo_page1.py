from selenium.webdriver.common.by import By

from Pages.pagebase import PageBase


class MeteoPage(PageBase):
    def go_to_football_page(self):
        self.click_on((By.LINK_TEXT, 'Piłka nożna'), 60)
        from Pages.foot_page1 import FootballPage
        return FootballPage(self.driver)
