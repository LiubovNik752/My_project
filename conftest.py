import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect

from configs.constants import DEFAULT_TIMEOUT
from framework.fixture_tools import FixtureTools
from pages.auth_page import AuthLocators
from settings import user_config


@pytest.fixture(scope="function")
def browser():
    """
        Фикстура для создания браузера.
        После выполнения тестов браузер закрывается.
    """
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """ Фикстура для создания новой страницы в браузере. """
    context = browser.new_context(no_viewport=True)
    page: Page = context.new_page()
    page.goto(user_config.base_url)
    page.set_default_timeout(DEFAULT_TIMEOUT)
    yield page
    context.close()


@pytest.fixture
def fixture_tools(page: Page) -> FixtureTools:
    """ Фикстура для создания экземпляра `FixtureTools`, используя объект страницы `page` """
    return FixtureTools(page)

@pytest.fixture
def auth(fixture_tools, page):
    """ Фикстура для авторизации в системе """
    fixture_tools.auth_page.input_login(AuthLocators.USERNAME, user_config.user_login)
    fixture_tools.auth_page.input_password(AuthLocators.PASSWORD, user_config.user_password)
    fixture_tools.auth_page.login_button_click(AuthLocators.LOGIN_BUTTON)