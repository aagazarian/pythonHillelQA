from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__email_input_xpath = (By.XPATH, "//div[@class='input-group']/input[@name='email']")
        self.__submit_button_xpath = (By.XPATH, "//span/button[@type='submit']")
        self.__error_message_xpath = (By.XPATH, "//label[@id='email-error ']")

    def open(self) -> None:
        self._driver.get(self._base_url)

    def fill_email(self, value: str) -> None:
        self._scroll_to_element(self.__email_input_xpath)
        self._fill_input_field(self.__email_input_xpath, value)

    def click_get_started_button(self):
        self._click_on_element(self.__submit_button_xpath)

    def is_error_message_displayed(self) -> bool:
        return self._is_element_present(self.__error_message_xpath)

    def get_error_message_text(self) -> str:
        return self._get_element_text(self.__error_message_xpath)
