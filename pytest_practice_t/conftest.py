import pytest
from collections import namedtuple
from faker import Faker

@pytest.fixture
def generate_user():
    fake = Faker()
    holder = fake.name()
    number = fake.credit_card_number()
    bank = fake.bank()
    user = namedtuple('BankCard', ['holder','number','bank'])
    user_bank = user(holder=holder, number=number, bank=bank)
    yield user_bank
    print("\n[Teardown] Данные карты стерты из памяти")