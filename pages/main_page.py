from pages.base_page import BasePage
from allure import step


class MainLocators:
    """ Описание локаторов главной страницы """

    ADDTOCART_BUTTONS = '//button[text()="Add to cart"]'
    QUANTITY_PRODUCTS = '.shopping_cart_badge'
    REMOVE_BUTTONS = '//button[text()="Remove"]'
    PRODUCT_TITLES = '.inventory_item_name'
    PRODUCT_PRICES = '.inventory_item_price'
    CART_LINK = '//a[contains(@class, "shopping_cart")]'

class MainPage(BasePage):
    """ Описание методов главной страницы """

    @step("Нажимаем на кнопку Add to cart")
    def click_add_to_cart_button(self, locator, num):
        add_button = self.get_elements(locator)[num]
        self.logger.debug("Add to cart button was found")
        add_button.click()
        self.logger.debug("Add to cart button was clicked")

    @step("Получаем значение количества товаров в корзине")
    def get_quantity_of_products(self, locator):
        element = self.get_element(locator)
        self.logger.debug(f"Element with locator {locator} was found")
        value = element.text_content()
        self.logger.debug(f"Element value is {value}")
        return value

    @step("Нажимаем на кнопку Remove")
    def click_remove_button(self, locator, num):
        remove_button = self.get_elements(locator)[num]
        self.logger.debug("Remove button was found")
        remove_button.click()
        self.logger.debug("Remove button was clicked")

    @step("Нажимаем на кнопку Remove")
    def click_remove_button(self, locator, num):
        remove_button = self.get_elements(locator)[num]
        self.logger.debug("Remove button was found")
        remove_button.click()
        self.logger.debug("Remove button was clicked")

    @step("Нажимаем на иконку корзины")
    def click_cart_button(self, locator):
        cart_icon = self.get_element(locator)
        self.logger.debug("Cart icon link was found")
        cart_icon.click()
        self.logger.debug("Cart icon link was clicked")