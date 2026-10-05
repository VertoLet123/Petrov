from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

ADD_ELEMENT = ("xpath", "//button[@onclick='addElement()']")
DELETE_BUTTON = ("xpath", "//button[@onclick='deleteElement()']")

wait.until(EC.element_to_be_clickable(ADD_ELEMENT)) # Ждем пока кнопка станет кликабельной
driver.find_element(*ADD_ELEMENT).click() # Кликаем на кнопку
wait.until(EC.visibility_of_element_located(DELETE_BUTTON)) # Ждем пока элемент станет видимым
driver.find_element(*DELETE_BUTTON).click()
driver.quit()