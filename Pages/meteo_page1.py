from Pages.pagebase import PageBase


class MeteoPage(PageBase):
    def go_to_football_page(self):
        pass
        # TODO: investigate why cannot import name 'FootballPage'
        # self.click_on((By.LINK_TEXT, 'Piłka nożna'), 60)
        # return FootballPage(self.driver)
