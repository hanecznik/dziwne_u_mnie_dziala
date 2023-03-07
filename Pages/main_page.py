from Pages.pagebase import PageBase


class MainPage(PageBase):

    def get_amount_of_points_by_club_name(self, name):
        selector = f"//td[contains(text(),'{name}')]/parent::tr/td[@class='points']"
        element = self.find_element(locator=selector)
        return element
