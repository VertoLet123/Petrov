import pytest

def test_send_notification(api):
    assert len(api.token)
    print(api.base_url)