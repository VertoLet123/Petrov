import pytest
from selenium import webdriver


class TestMarking:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.smoke
    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Error"
    @pytest.mark.regression
    def test_open_books_page(self):
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books", "Error"

    @pytest.mark.smoke
    def test_open_profile_page(self):
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Error"

    @pytest.mark.regression
    def test_open_forms_page(self):
        self.driver.get("https://demoqa.com/forms")
        assert self.driver.current_url == "https://demoqa.com/forms", "Error"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_open_swagger_page(self):
        self.driver.get("https://demoqa.com/swagger")
        assert self.driver.current_url == "https://demoqa.com/swagger", "Error"

    def test_open_elements_page(self):
        self.driver.get("https://demoqa.com/elements")
        assert self.driver.current_url == "https://demoqa.com/elements", "Error"

    def teardown_method(self):
        self.driver.quit()