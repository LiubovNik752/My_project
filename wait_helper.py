import logging

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from configs.constants import LONG_TIMEOUT


class WaitHelper:
    def __init__(self, page: Page):
        """ Инициализация WaitHelper с экземпляром страницы. """

        self.page = page
        self.timeout = LONG_TIMEOUT
        self.logger = logging.getLogger(__name__)
        # self.logger = logger_config.setup_logger(self.__class__.__name__)

    def wait_for_selector_visible(self, locator: str, state=None):
        """ Ожидание появления элемента на странице по локатору. """
        try:
            self.page.wait_for_selector(locator, state=state, timeout=self.timeout)
        except PlaywrightTimeoutError as e:
            if self.logger:
                self.logger.error(f"Тайм-аут при ожидании элемента {locator}: {e}")
        except Exception as e:
            if self.logger:
                self.logger.error(f"Ошибка при ожидании элемента {locator}: {e}")
                raise None