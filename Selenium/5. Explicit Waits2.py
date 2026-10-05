from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 30, 1)
driver.get("https://demoqa.com/dynamic-properties")

CLICK_AFTER_5_SEC = ("xpath", "//button[@id='enableAfter']")
COLOR_CHANGE_BUTTON = ("xpath", "//button[@id='colorChange']")
TEXT_WITH_RANDOM_ID = ("xpath", "//p[contains(text(),'This text has random Id')]")

# 1. Нажимаем на первую кнопку
wait.until(EC.element_to_be_clickable(CLICK_AFTER_5_SEC))
driver.find_element(*CLICK_AFTER_5_SEC).click()
print("✅ Нажата кнопка 'Will enable 5 seconds'")
# 2. Работа с кнопкой, которая меняет цвет
color_button_element = driver.find_element(*COLOR_CHANGE_BUTTON)
print("⏳ Ожидание изменения цвета на красный...")
def color_became_red(element):
    current_color = element.value_of_css_property("color")
    print(f"Текущий цвет: {current_color}")  # Для отладки
    return current_color == "rgba(220, 53, 69, 1)"  # Исправленный цвет!

wait.until(lambda d: color_became_red(color_button_element))
color_button_element.click()
print("✅ Нажата кнопка 'Color Change' после изменения цвета")

# 3. Работа с текстом "random Id"
wait.until(EC.visibility_of_element_located(TEXT_WITH_RANDOM_ID))
random_text_element = driver.find_element(*TEXT_WITH_RANDOM_ID)
random_text = random_text_element.text
print(random_text)
print(f"✅ Текст с random Id появился: '{random_text}'")

driver.quit()