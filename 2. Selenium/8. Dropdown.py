import time
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN_ELEMENT = ("xpath","//select[@id='dropdown']")

dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))
dropdown.select_by_visible_text("Option 2")
time.sleep(1)
dropdown.select_by_index(1)
time.sleep(1)
dropdown.select_by_value("2")
time.sleep(1)

