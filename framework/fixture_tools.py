from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from wait_helper import WaitHelper


class FixtureTools:
    """
        Класс FixtureTools используется для инициализации и управления различными страницами веб-приложения.
        Он служит контейнером для страниц и обеспечивает легкий доступ к ним.
    """

    def __init__(self, page):
        self.wait = WaitHelper(page)
        self.base_page = BasePage(page)
        self.main_page = MainPage(page)
        self.auth_page = AuthPage(page)