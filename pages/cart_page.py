from pages.base_page import BasePage
from allure import step


class CartLocators:
    """ Описание локаторов страницы корзины """

    PAGE_TITLE = '.title'
    PRODUCT_NAMES = '.inventory_item_name'
    PRODUCT_PRICES = '.inventory_item_price'


class MainPage(BasePage):
    """ Описание методов страницы корзины """

    pass
