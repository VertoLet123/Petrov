import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")
time.sleep(3)

USERNAME = ("xpath", "//input[@data-test='username']")
PASSWORD = ("xpath", "//input[@data-test='password']")
LOGIN = ("xpath", "//input[@data-test='login-button']")
JACKET_BUTTON = ("xpath", "//button[@data-test='add-to-cart-sauce-labs-fleece-jacket']")
BASKET = ("xpath", "//a[@data-test='shopping-cart-link']")
CHECKOUT_BUTTON = ("xpath", "//button[@data-test='checkout']")
FIRST_NAME = ("xpath", "//input[@data-test='firstName']")
LAST_NAME = ("xpath", "//input[@data-test='lastName']")
POSTAL_CODE = ("xpath", "//input[@data-test='postalCode']")
CONTINUE_BUTTON  = ("xpath", "//input[@data-test='continue']")
FINISH_BUTTON = ("xpath", "//button[@data-test='finish']")

input_username = driver.find_element(*USERNAME)
input_username.send_keys("standard_user")
input_password = driver.find_element(*PASSWORD)
input_password.send_keys("secret_sauce")
login = driver.find_element(*LOGIN)
login.click()
time.sleep(3)
assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Error. Открыта неверная страница"

add_jacket = driver.find_element(*JACKET_BUTTON)
add_jacket.click()
time.sleep(3)

click_basket = driver.find_element(*BASKET)
click_basket.click()
time.sleep(3)
assert driver.current_url == "https://www.saucedemo.com/cart.html", "Error. Открыта неверная страница"

checkout_button = driver.find_element(*CHECKOUT_BUTTON)
checkout_button.click()
time.sleep(3)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Error. Открыта неверная страница"

first_name = driver.find_element(*FIRST_NAME)
first_name.send_keys("Dmitry")
last_name = driver.find_element(*LAST_NAME)
last_name.send_keys("Petrov")
postal = driver.find_element(*POSTAL_CODE)
postal.send_keys("StaryOskol")
time.sleep(3)
continue_button = driver.find_element(*CONTINUE_BUTTON)
continue_button.click()
time.sleep(3)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Error. Открыта неверная страница"

finish = driver.find_element(*FINISH_BUTTON)
finish.click()

time.sleep(3)