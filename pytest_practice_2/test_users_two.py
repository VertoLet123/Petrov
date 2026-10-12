import pytest

def test_user_bank(generate_user):
    assert len(generate_user.number) > 10
    print(generate_user.number, generate_user.bank)