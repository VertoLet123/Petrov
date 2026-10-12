import pytest
from selenium import webdriver
from faker import Faker
from collections import namedtuple

fake = Faker()

@pytest.fixture(name="browser")
def open_browser(request):
    request.cls.driver = webdriver.Chrome()
    yield
    request.cls.driver.quit()

@pytest.fixture(name="user_data")
def fake_data():
    NewUser = namedtuple('UserData', ['user_name', 'last_name','email',])
    user_name = fake.user_name()
    last_name = fake.last_name()
    email = fake.email()
    user = NewUser(user_name=user_name, last_name=last_name,email=email)
    return user