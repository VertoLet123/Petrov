from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

BUTTON = ("xpath", "//button[@id='visibleAfter']")

wait.until(EC.visibility_of_element_located(BUTTON))



#Неявные_ожидания - Implicit_Waits:
#from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(6)
# driver.get("https://demoqa.com/dynamic-properties")
# VISIBLE_AFTER_5_SECOND_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# driver.find_element(*VISIBLE_AFTER_5_SECOND_BUTTON).click()



