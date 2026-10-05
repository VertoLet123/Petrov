import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 1)
action = ActionChains(driver)

driver.get("https://demoqa.com/droppable")

SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")

SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)

time.sleep(2)

action.drag_and_drop(SOURCE, TARGET).perform()

time.sleep(5)

