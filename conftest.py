import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect

from configs.constants import DEFAULT_TIMEOUT
from framework.fixture_tools import FixtureTools
from settings import user_config


@pytest.fixture(scope="function")
def browser():
    """
        Фикстура для создания браузера.
        После выполнения тестов браузер закрывается.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """
        Фикстура для создания новой страницы в браузере.
    """
    context = browser.new_context(no_viewport=True)
    page: Page = context.new_page()
    page.goto(user_config.base_url)
    page.set_default_timeout(DEFAULT_TIMEOUT)
    yield page
    context.close()


@pytest.fixture
def fixture_tools(page: Page) -> FixtureTools:
    """
        Фикстура для создания экземпляра `FixtureTools`, используя объект страницы `page`
    """
    return FixtureTools(page)