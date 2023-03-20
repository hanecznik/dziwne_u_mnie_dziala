from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.pagebase import PageBase


class HebePage(PageBase):
    @staticmethod
    def navigate(driver, url):
        page = HebePage(driver, url)
        page.navigate_to()
        return page

    def click_all_categories(self):
        self.click_on((By.CSS_SELECTOR, "span[class='header-expander__label'"), 360)
        return self

    def click_sub_categories(self, categoryName, subcategory):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element((By.XPATH, f"//span[contains(text(),'{categoryName}')]"), 360))
        action.perform()

        action.move_to_element(self.find_element((By.XPATH, f"//span[contains(text(),'{subcategory}')]"), 360))
        action.perform()
        menu_items = self.find_elements((By.XPATH,
                                         "//div[@class='header-l2__list']//a/span[contains(text(),'Olej') and @class='header-l2-item__label']"),
                                        360)
        text = set()
        for value in menu_items:
            text.add(value.text)
        print(text)
