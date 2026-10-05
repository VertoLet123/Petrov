import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
time.sleep(5)
page_url = driver.current_url  # Сохраняем текущий URL в переменную
print(page_url)  # Выводим значение переменной в консоль
PAGE_TITLE = driver.title  # Сохраняем заголовок страницы
print(f"Заголовок страницы: {PAGE_TITLE}")  # Выводим значение
title = driver.title
if "Swag Labs" in title:
    print("Страница авторизации успешно загружена")
else:
    print("Ошибка: открыта неверная страница")
# Проверяем заголовок страницы
