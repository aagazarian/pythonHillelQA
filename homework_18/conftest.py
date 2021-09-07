from pathlib import Path

import pytest
from selenium.webdriver import Chrome

from homework_18.pages.home_page import HomePage


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver_folder = Path(__file__).parent / "drivers"
    driver_path = driver_folder / "chromedriver"
    driver = Chrome(driver_path)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture
def homepage(driver) -> HomePage:
    yield HomePage(driver)
