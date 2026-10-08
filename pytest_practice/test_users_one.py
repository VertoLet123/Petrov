import pytest

def test_user_email(generate_user):
    assert "@" in generate_user.email
    print(generate_user.email)
