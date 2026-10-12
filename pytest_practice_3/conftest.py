import pytest
from collections import namedtuple
from faker import Faker

@pytest.fixture(autouse=True)
def clear_notification_history():
    print("\n[Autouse Setup] История уведомлений очищена")
    yield
    print("\n[Autouse Teardown] Логи отправки сохранены")

@pytest.fixture(name="api")
def connect_to_api_service():
    site = namedtuple('ApiService',['base_url','token'])
    api = site(base_url = 'https://test.com',token = 'wqrethyjkmbcvxddw4234r323rfscsv')
    return api
