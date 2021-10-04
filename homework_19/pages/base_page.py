from selenium.webdriver.chrome.webdriver import WebDriver

from homework_19.core.cookie import Cookie
from homework_19.core.local_storage import LocalStorage


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._base_url = "https://linkedin.com"
        self._cookie = Cookie(self._driver)
        self._local_storage = LocalStorage(self._driver)
