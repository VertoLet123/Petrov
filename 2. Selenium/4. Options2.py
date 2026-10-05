from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get("https://ya.ru")

Основные опции:
1. Безголовый режим (--headless и --headless=new)
options.add_argument("--headless=new") - улучшенная версия с более стабильной работой (Chrome 109+)
Преимущества:
Работает в фоне без GUI
Экономит ресурсы системы
Ускоряет выполнение тестов

2. Режим инкогнито (--incognito)
options.add_argument("--incognito")

Особенности:
Не использует кэш и cookies
Создает чистую сессию
Автоматически очищается после закрытия
Ограничения:
Сбрасывает настройки загрузок
Не сохраняет историю

3. Игнорирование SSL-ошибок (--ignore-certificate-errors)
options.add_argument("--ignore-certificate-errors")
Применение:
Тестирование на тестовых/staging окружениях
Работа с само подписанными сертификатами

4. Установка размера окна (--window-size=X,Y)
options.add_argument("--window-size=1920,1080")
Рекомендации:
Используйте стандартные разрешения (1920x1080, 1366x768)
Важно для тестирования адаптивности
Особенность:
Влияет на отображение элементов (может менять layout)

5. Отключение кэширования (--disable-cache)
options.add_argument("--disable-cache")
Когда использовать:
Тестирование свежего контента
Проверка обновлений ресурсов
Отладка проблем с кэшированием
Дополнительные полезные опции:
# Для CI/CD окружений
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Оптимизация производительности
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

# Управление поведением
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
Пример комплексной настройки:
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-cache")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)