from pages.base_page import BasePage
from allure import step


class AuthLocators:
    USERNAME = '#user-name'
    PASSWORD = '#password'
    LOGIN_BUTTON = '#login-button'
    ERROR_MESSAGE = '//h3[@data-test="error"]'

class AuthPage(BasePage):
    @step("Вводим логин")
    def input_login(self, locator, username):
        login = self.get_element(locator)
        self.logger.debug("Login field was found")
        login.fill(username)
        self.logger.debug("Login was added")

    @step("Вводим пароль")
    def input_password(self, locator, password):
        passw = self.get_element(locator)
        self.logger.debug("Password field was found")
        passw.fill(password)
        self.logger.debug("Password was added")

    @step("Нажимаем кнопку логин")
    def login_button_click(self, locator):
        login_button = self.get_element(locator)
        self.logger.debug(f"Login button with locator {locator} was found")
        login_button.click()
        self.logger.debug("Login button was clicked")
