import pytest


@pytest.mark.usefixtures("browser")
class TestPages:

    @pytest.mark.smoke
    def test_login_page(self):
       self.driver.get("https://demoqa.com/login")


    @pytest.mark.regression
    def test_books_page(self):
        self.driver.get("https://demoqa.com/books")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_profile_page(self):
        self.driver.get("https://demoqa.com/profile")


class TestUserData:

    @pytest.mark.regression
    def test_user_data(self, user_data):
        assert len(user_data.user_name) > 0, "Строка пустая"
        assert len(user_data.last_name) > 0, "Строка пустая"
        assert '@' in user_data.email