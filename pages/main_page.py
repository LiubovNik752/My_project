from pages.base_page import BasePage

class MainPage(BasePage):
    """ Описание локаторов главной страницы"""

    def main_page_links(self):
        return self.get_elements(locator='//div[@class="card mt-4 top-card"]')