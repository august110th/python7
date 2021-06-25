import pytest
from main import people, shelf


class Test_buhgalter:

    def test_people(self):
        assert people("10006") == "Аристарх Павлов"
    def test_shelf(self):
        assert shelf('11-2') == '1'
    def test_(self):
        assert shelf('11-2') == '1'