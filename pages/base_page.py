import logging

from playwright.sync_api import Page, Locator, TimeoutError as PlaywrightTimeoutError, expect
from configs.constants import SHORT_TIMEOUT
from wait_helper import WaitHelper
from typing import List, Optional


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.timeout = SHORT_TIMEOUT
        self.wait = WaitHelper(page)
        self.logger = logging.getLogger(__name__)

    def goto(self, url: str):
        """ Переход по-указанному URL. """
        try:
            self.page.goto(url, timeout=self.timeout)
            self.logger.debug(f"Переход на указанный {url} успешный")
        except PlaywrightTimeoutError as e:
            self.logger.error(f"Тайм-аут при переходе к {url}: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Произошла ошибка при переходе к {url}: {e}")
            raise None

    def get_element(self, locator: str, state="visible", for_visible: bool = True) -> Optional[Locator]:
        """ Получение одного элемента по селектору. """
        try:
            element = self.page.locator(locator)
            if for_visible:
                self.wait.wait_for_selector_visible(locator=locator, state=state)
            return element
        except Exception as e:
            self.logger.debug(f"Произошла ошибка при получении элемента с селектором: {locator}: {e}")
            return None

    def get_elements(self, locator: str) -> List[Locator]:
        """ Получение списка элементов по селектору. """
        try:
            elements = self.page.locator(locator)
            self.wait.wait_for_selector_visible(locator=locator, state="visible")
            all_elements = elements.all()
            if all_elements:
                self.logger.debug(f"Элементы найдены: {locator}")
            else:
                self.logger.warning(f"Элементы не найдены: {locator}")
            return all_elements
        except Exception as e:
            self.logger.error(f"Произошла ошибка при получении элемента с селектором: {locator}: {e}")
            raise []

    def check_url(self, url):
        """ Проверка текущего url. """
        expect(self.page).to_have_url(url)

    def check_text(self, locator, text):
        """ Проверка текста элемента. """
        elem = self.get_element(locator)
        self.logger.debug(f"Element with text '{elem.text_content()}' was found")
        expect(elem).to_contain_text(text)