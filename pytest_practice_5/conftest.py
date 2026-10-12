import pytest
from selenium import webdriver

@pytest.fixture(name="driver")
def open_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()