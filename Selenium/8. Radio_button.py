from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

YES_RADIO_LABEL = ("xpath","//label[@for='yesRadio']")
YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")

driver.find_element(*YES_RADIO_LABEL).click()
print(driver.find_element(*YES_RADIO_BUTTON).is_selected())

driver.find_element(*IMPRESSIVE_RADIO_BUTTON).click()
print(driver.find_element(*IMPRESSIVE_RADIO_BUTTON).is_selected())

assert not driver.find_element(*NO_RADIO_BUTTON).is_enabled()
print(driver.find_element(*NO_RADIO_BUTTON).is_enabled())