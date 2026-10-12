import pytest
from collections import namedtuple

@pytest.fixture
def generate_user():
    newUser = namedtuple('User',['username', 'email'])
    user = newUser(username="tester", email="test@test.com")
    yield user
    print("\n[Teardown] Тестовый пользователь удален из базы данных")