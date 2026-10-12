import pytest
from faker import Faker
fake = Faker()

@pytest.mark.smoke
def test_open_login_page(driver):
    driver.get("https://demoqa.com/login")
    assert driver.current_url == "https://demoqa.com/login", "Invalid URL"

@pytest.mark.smoke
def test_open_books_page(driver):
    driver.get("https://demoqa.com/books")
    assert driver.current_url == "https://demoqa.com/books", "Invalid URL"

@pytest.mark.smoke
@pytest.mark.regression
def test_open_profile_page(driver):
    driver.get("https://demoqa.com/profile")
    assert driver.current_url == "https://demoqa.com/profile", "Invalid URL"

@pytest.mark.regression
def test_fake_user_data():
    user_name = fake.user_name()
    assert len(user_name) >= 2, "user_name должен содержать 2 или больше символов"
    last_name = fake.last_name()
    assert len(last_name) > 3, "last_ name должен содержать больше 3 символов"
    email = fake.email()
    assert "@" in email, "Email должен содержать символ '@'"
