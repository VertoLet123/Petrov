import pytest

@pytest.fixture(scope="class")
def setup_class_data(request):
    secret_key = "WEB-TOKEN-777"
    request.cls.key = secret_key
    yield

