import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://dzen.ru/")
print(driver.current_url)
time.sleep(5)
page_title = driver.title
print(page_title)
assert driver.current_url == "https://dzen.ru/", "Открыта неверная страница"
assert page_title == "Дзен — главная новостная информационная платформа, которая помогает миллионам людей узнавать, что происходит в мире.", "Неверный заголовок"

first_search = driver.find_element(By.XPATH, "//input[@name='text' or @type='search']")
time.sleep(10)
first_search.send_keys("Пайтон")
time.sleep(10)
