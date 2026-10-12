import pytest
import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType


@allure.epic("Аккаунт")
@allure.feature("Авторизация")
@allure.story("Страницы")
class TestPages:

    @pytest.mark.smoke
    @allure.title("Открыть страницу авторизации")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://www.toolsqa.com/selenium-training/", name="Documentation")
    def test_login_page(self, driver):
       with allure.step("Переход на страницу"):
           driver.get("https://demoqa.com/login")
           allure.attach(
               body=driver.get_screenshot_as_png(),
               name="Страница авторизации",
               attachment_type=AttachmentType.PNG
           )
       with allure.step("Проверка текущего адреса страницы"):
           assert driver.current_url == "https://demoqa.com/login", "Error"



    @pytest.mark.regression
    @allure.title("Открыть страницу книг")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://www.toolsqa.com/selenium-training/", name="Documentation")
    def test_books_page(self, driver):
        with allure.step("Переход на страницу"):
            driver.get("https://demoqa.com/books")
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name="Страница книги",
                attachment_type=AttachmentType.PNG
            )
        with allure.step("Проверка текущего адреса страницы"):
            assert driver.current_url == "https://demoqa.com/books", "Error"

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Открыть страницу профиля")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://www.toolsqa.com/selenium-training/", name="Documentation")
    def test_profile_page(self, driver):
        with allure.step("Переход на страницу"):
            driver.get("https://demoqa.com/profile")
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name="Страница профиля",
                attachment_type=AttachmentType.PNG
            )
        with allure.step("Проверка текущего адреса страницы"):
            assert driver.current_url == "https://demoqa.com/profile", "Error"


class TestUserData:

    @pytest.mark.regression
    @allure.title("Проверка валидации")
    @allure.severity(Severity.NORMAL)
    def test_user_data(self, user_data):
        with allure.step("Проверка имени"):
            assert len(user_data.user_name) > 0, "Строка пустая"
        with allure.step("Проверка фамилии"):
            assert len(user_data.last_name) > 0, "Строка пустая"
        with allure.step("Проверка почты"):
             assert '@' in user_data.email