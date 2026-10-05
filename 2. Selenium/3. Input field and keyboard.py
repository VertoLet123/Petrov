from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
full_name = driver.find_element("xpath", "//input[@id='userName']")
full_name.clear()
assert full_name.get_attribute("value") == ""
full_name.send_keys("Sladus")
assert full_name.get_attribute("value") == "Sladus"
print(full_name.get_attribute("value"))

email = driver.find_element("xpath", "//input[@id='userEmail']")
email.send_keys(Keys.CONTROL+"A")
email.send_keys(Keys.BACKSPACE)
assert email.get_attribute("value") == ""
email.send_keys("Kosmos@quality.com")
assert email.get_attribute("value") == "Kosmos@quality.com"
print(email.get_attribute("value"))

current_address = driver.find_element("xpath","//textarea[@id='currentAddress']")
current_address.send_keys(Keys.CONTROL+"A")
current_address.send_keys(Keys.BACKSPACE)
assert current_address.get_attribute("value") == ""
current_address.send_keys("Leningrad")
assert current_address.get_attribute("value") == "Leningrad"
print(current_address.get_attribute("value"))

permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_address.send_keys(Keys.CONTROL+"A")
permanent_address.send_keys(Keys.BACKSPACE)
assert permanent_address.get_attribute("value") == ""
permanent_address.send_keys("World")
assert permanent_address.get_attribute("value") == "World"
print(permanent_address.get_attribute("value"))
driver.quit()