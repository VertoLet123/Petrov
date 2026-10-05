import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

# Клик на кнопку, которая вызывает alert
driver.find_element("xpath", "//button[@id='alertButton']").click()
print("Клик на кнопку, которая вызывает alert")
alert = wait.until(EC.alert_is_present())
time.sleep(3)
print(alert)
alert.accept()

или ввод нужных значений в Alert

driver.find_element("xpath", "//button[@id='promtButton']").click()
alert = wait.until(EC.alert_is_present())
alert.send_keys("Alex")
time.sleep(3)
alert.accept()



HomeWork:
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 1)

driver.get("https://demoqa.com/alerts")


CLICK_BUTTON_TO_SEE_LOCATOR = ("xpath", "//button[@id='alertButton']")
BUTTON_AFTER_5_SECONDS_LOCATOR = ("xpath", "//button[@id='timerAlertButton']")
APPEAR_BUTTON_LOCATOR = ("xpath", "//button[@id='confirmButton']")
INPUT_BUTTON_LOCATOR = ("xpath", "//button[@id='promtButton']")

BUTTON1 = driver.find_element(*CLICK_BUTTON_TO_SEE_LOCATOR)
BUTTON2 = driver.find_element(*BUTTON_AFTER_5_SECONDS_LOCATOR)
BUTTON3 = driver.find_element(*APPEAR_BUTTON_LOCATOR)
BUTTON4 = driver.find_element(*INPUT_BUTTON_LOCATOR)

BUTTON1.click()
time.sleep(3)
alert = wait.until(EC.alert_is_present())
alert.accept()
time.sleep(3)

BUTTON2.click()
alert = wait.until(EC.alert_is_present())
time.sleep(3)
alert.accept()

BUTTON3.click()
alert = wait.until(EC.alert_is_present())
time.sleep(3)
alert.dismiss()
time.sleep(3)

BUTTON4.click()
alert = wait.until(EC.alert_is_present())
time.sleep(3)
alert.send_keys("Hello")
alert.accept()
time.sleep(3)