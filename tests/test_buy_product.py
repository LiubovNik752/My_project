from allure import step, title
from pages.cart_page import CartLocators
from pages.main_page import MainLocators

@title('Добавление и удаление товаров в (из) корзину')
def test_add_product_to_cart(fixture_tools, auth):
    with step("Добавляем в корзину товар Sauce Labs Backpack и проверяем, что значение счетчика = 1"):
        fixture_tools.main_page.click_add_to_cart_button(MainLocators.ADDTOCART_BUTTONS, num=0)
        fixture_tools.base_page.check_text(MainLocators.QUANTITY_PRODUCTS, '1')

    with step("Добавляем в корзину товар Sauce Labs Bolt T-Shirt и проверяем, что значение счетчика = 2"):
        fixture_tools.main_page.click_add_to_cart_button(MainLocators.ADDTOCART_BUTTONS, num=1)
        fixture_tools.base_page.check_text(MainLocators.QUANTITY_PRODUCTS, '2')

    with step("Удаляем товары из корзины, нажатием на кнопку Remove"):
        fixture_tools.main_page.click_remove_button(MainLocators.REMOVE_BUTTONS, num=1)
        fixture_tools.main_page.click_remove_button(MainLocators.REMOVE_BUTTONS, num=0)
        quantity_element = fixture_tools.base_page.get_element(MainLocators.QUANTITY_PRODUCTS)
        assert quantity_element.count() == 0

@title('Проверка страницы корзины')
def test_cart_page(fixture_tools, auth):
    with step("Добавляем товар в корзину и переходим на страницу корзины"):
        num = 2
        product_name = fixture_tools.base_page.get_text_element(MainLocators.PRODUCT_TITLES, num)
        product_price = fixture_tools.base_page.get_text_element(MainLocators.PRODUCT_PRICES, num)
        fixture_tools.main_page.click_add_to_cart_button(MainLocators.ADDTOCART_BUTTONS, num)
        fixture_tools.main_page.click_cart_button(MainLocators.CART_LINK)
        fixture_tools.base_page.check_text(CartLocators.PAGE_TITLE, 'Your Cart')

    with step("Проверяем на соответствие название и цену добавленного товара"):
        cart_product_name = fixture_tools.base_page.get_text_element(CartLocators.PRODUCT_NAMES, num=0)
        cart_product_price = fixture_tools.base_page.get_text_element(CartLocators.PRODUCT_PRICES, num=0)
        assert cart_product_name == product_name
        assert cart_product_price == product_price
