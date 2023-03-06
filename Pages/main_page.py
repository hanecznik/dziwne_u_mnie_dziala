from Pages.pagebase import PageBase


class MainPage(PageBase):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def get_amount_of_points_by_club_name(self, name):
        selector = f"//td[text()='{name}']/parent::tr/td[@class='points']"
        element = self.find_element(self, selector)
        return element
