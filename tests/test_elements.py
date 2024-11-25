from pages.auth_page import AuthLocators
from settings import user_config

def test_correct_auth(fixture_tools):
    fixture_tools.auth_page.input_login(AuthLocators.USERNAME, user_config.user_login)
    fixture_tools.auth_page.input_password(AuthLocators.PASSWORD, user_config.user_password)
    fixture_tools.auth_page.login_button_click(AuthLocators.LOGIN_BUTTON)
    fixture_tools.base_page.check_url("https://www.saucedemo.com/inventory.html")

# def test_auth_locked_user(fixture_tools):
#     fixture_tools.auth_page.input_login(AuthLocators.USERNAME, user_config.locked_user_login)
#     fixture_tools.auth_page.input_password(AuthLocators.PASSWORD, user_config.user_password)
#     fixture_tools.auth_page.login_button_click(AuthLocators.LOGIN_BUTTON)
#     fixture_tools.base_page.check_text(AuthLocators.ERROR_MESSAGE, "Epic sadface: \nSorry, this user has been locked out.")
