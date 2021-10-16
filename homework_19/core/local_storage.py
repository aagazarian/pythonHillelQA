from selenium.webdriver.chrome.webdriver import WebDriver


class LocalStorage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def set(self, name, value):
        print(f"save to local storage: 'name:' {name}, 'value:' {value}")
        self.__driver.execute_script(f"window.localStorage['{name}'] = '{value}'")

    def get(self, name) -> str:
        print(f"get argument from local storage '{name}'")
        return self.__driver.execute_script(f"return window.localStorage['{name}']")

    def items(self):
        return self.__driver.execute_script("let ls = window.localStorage, items = {};"
                                            "for (let i = 0, k; i < ls.length; ++i)"
                                            "items[k = ls.key(i)] = ls.getItem(k);"
                                            "return items;")
