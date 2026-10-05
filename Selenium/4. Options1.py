import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--incognito") # работает, но инкогнито выкл в браузере
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options = options)

driver.get("https://demoqa.com/automation-practice-form")
print(driver.current_url)
first_search = driver.find_element("xpath","//input[@id='firstName']")
assert first_search.get_attribute("value") == ""
print(first_search.get_attribute)
time.sleep(2)
first_search.send_keys("Sladus")
time.sleep(2)
first_search_1 = first_search.get_attribute("value") == "Sladus"
print(first_search_1)
time.sleep(2)
first_search.clear()
time.sleep(2)
first_search.send_keys("Perdus")
time.sleep(2)
first_search.send_keys(Keys.CONTROL+"A")
time.sleep(2)
first_search.send_keys(Keys.BACKSPACE)
time.sleep(2)
first_search.send_keys("Sladus")
time.sleep(2)
print(first_search.get_attribute("value"))
assert first_search.get_attribute("value") == "Sladus", "Error, неправильное имя"
driver.get("https://demoqa.com/upload-download")
time.sleep(2)
File_Upload_Field = ("xpath", "//input[@label='Select a File']")
upload_file_field = driver.find_element(*File_Upload_Field) # распаковка строки выше, команда звездочка
upload_file_field.send_keys(r"C:\Users\Karam\OneDrive\Рабочий стол\Obey.png")
time.sleep(2)
