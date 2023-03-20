from selenium.webdriver.common.by import By

from Pages.pagebase import PageBase


class RossmanPage(PageBase):
    @staticmethod
    def navigate(driver, url):
        page = RossmanPage(driver, url)
        page.navigate_to()
        # page.click_on((By.XPATH, '//button[@id="onetrust-accept-btn-handler"]'), 360)
        return page

    def click_menu_item(self, item):
        self.click_on((By.XPATH, f"//a[text()='{item}']"), 360)
        return self

    def check_sub_menu_items(self, item, menu_items):
        items = self.find_elements(
            (By.XPATH, f"//*[text()='{item}']/following-sibling::div//*[@class='mega-menu__categories']/div/a[text()]"),
            360)
        text = []
        for item in items:
            text.append(item.text)
        print(text)
        print(menu_items)
        assert text == menu_items
