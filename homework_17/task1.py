from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains


class TestEmail:
    driver = None
    expected_error_message = "Please enter a valid email address"

    email_input_xpath = "//div[@class='input-group']/input[@name='email']"
    submit_button_xpath = "//span/button[@type='submit']"
    error_message_xpath = "//label[@id='email-error']"

    def setup_class(self):
        print("Initialize driver")
        self.driver = Chrome("./drivers/chromedriver")

    def teardown_class(self):
        print("Close driver")
        self.driver.close()

    def test_button(self):
        self.driver.get("https://www.oneskyapp.com")

        email_input = self.driver.find_element_by_xpath(self.email_input_xpath)
        get_started_for_free_button = self.driver.find_element_by_xpath(self.submit_button_xpath)

        action = ActionChains(self.driver)
        action \
            .move_to_element(email_input) \
            .perform()

        email_input.send_keys("uyfhigfgfuttflhfu")
        get_started_for_free_button.click()

        actual_error_message = self.driver.find_element_by_xpath(self.error_message_xpath)
        assert actual_error_message.is_displayed() is True
        assert actual_error_message.text == self.expected_error_message
