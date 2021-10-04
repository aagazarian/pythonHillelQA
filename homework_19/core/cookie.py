from selenium.webdriver.chrome.webdriver import WebDriver


class Cookie:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def save_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        print(f"save cookie: {cookie}")
        self.__driver.add_cookie(cookie)

    def get_cookie(self, name) -> str:
        print(f"get cookie '{name}'")
        cookie = self.__driver.get_cookie(name)
        if cookie is None:
            return None
        print(f"cookie_dict: {cookie}")
        return cookie.get('value')

    def get_all_cookies(self) -> list:
        print(f"get all cookies")
        cookies = self.__driver.get_cookies()
        print(f"cookie_list: {cookies}")
        return cookies
