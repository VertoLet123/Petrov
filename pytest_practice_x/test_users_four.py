import pytest

@pytest.mark.usefixtures("setup_class_data")
class TestAdminZone():


    def test_check_access(self):
        assert self.key == "WEB-TOKEN-777"
        print(self.key)