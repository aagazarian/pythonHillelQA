from selenium.webdriver.chrome.webdriver import WebDriver

from homework_19.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self) -> None:
        self._driver.get(self._base_url)
