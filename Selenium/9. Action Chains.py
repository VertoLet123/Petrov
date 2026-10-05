import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options = options)
wait = WebDriverWait(driver, 10, 1)
action = ActionChains(driver)
driver.get("https://demoqa.com/buttons")
time.sleep(3)

DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
LEFT_CLICK_BUTTON = ("xpath", "//button[text()='Click Me']")

BUTTON = driver.find_element(*DOUBLE_CLICK_BUTTON)
RIGHT_BUTTON = driver.find_element(*RIGHT_CLICK_BUTTON)
LAST_BUTTON = driver.find_element(*LEFT_CLICK_BUTTON)

action.double_click(BUTTON ).context_click(RIGHT_BUTTON).click(LAST_BUTTON).perform()
time.sleep(3)
