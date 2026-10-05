import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 1)
action = ActionChains(driver)

driver.get("https://demoqa.com/menu#")

STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

# 1. Находим первый элемент (он виден сразу)
STEP10 = driver.find_element(*STEP_1_LOCATOR)
action.move_to_element(STEP_1).pause(1).perform()   # Раскрываем первое подменю

# 2. Теперь второй элемент стал видимым — находим его
STEP20 = driver.find_element(*STEP_2_LOCATOR)
action.move_to_element(STEP_2).pause(1).perform()

# 3. Теперь третий элемент стал видимым — находим его и кликаем
STEP30 = driver.find_element(*STEP_3_LOCATOR)
action.move_to_element(STEP_3).pause(1).click().perform()

time.sleep(3)
