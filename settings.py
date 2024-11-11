import os
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class TestUserConfig(BaseSettings):
    """
        Класс для хранения конфигурации тестового пользователя.

        Атрибуты:
            base_url (str): Базовый URL.
            user_login (str): Логин пользователя.
            user_password (str): Пароль пользователя.
    """
    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding='utf-8', extra="ignore")

    base_url: str = ""
    user_login: str = ""
    user_password: str = ""
    locked_user_login: str = ""



user_config = TestUserConfig()