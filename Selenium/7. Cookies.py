import json
import time
import os.path
from selenium import webdriver
from cookies_manager import CookieManager

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")
cookie_manager = CookieManager(driver)

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

if os.path.exists("cookies.json"):
    cookie_manager.load()
else:
    driver.find_element(*LOGIN_FIELD).send_keys("Dasdfghnm@gmail.com")
    driver.find_element(*PASSWORD_FIELD).send_keys("12345678")
    driver.find_element(*SUBMIT_BUTTON).click()
    cookie_manager.save()
time.sleep(5)