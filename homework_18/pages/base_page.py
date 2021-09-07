from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._base_url = "https://www.oneskyapp.com"
        self.__wait = WebDriverWait(self._driver, 5)

    def _fill_input_field(self, locator: Tuple[By, str], value: str) -> None:
        element = self.__wait_for_element(locator)
        element.click()
        element.clear()
        element.send_keys(value)

    def _is_element_present(self, locator: Tuple[By, str]) -> bool:
        try:
            element = self.__wait_for_element(locator)
        except TimeoutException as e:
            print(e.msg)
            return False
        return element.is_displayed()

    def _get_element_text(self, locator: Tuple[By, str]) -> str:
        element = self.__wait_for_element(locator)
        return element.text

    def __wait_for_element(self, locator: Tuple[By, str]) -> WebElement:
        return self.__wait.until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def _click_on_element(self, locator: Tuple[By, str]) -> None:
        element = self.__wait_for_element(locator)
        element.click()

    def _scroll_to_element(self, locator: Tuple[By, str]):
        element = self.__wait_for_element(locator)
        action = ActionChains(self._driver)
        action \
            .move_to_element(element) \
            .perform()
