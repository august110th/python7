import pytest
from main import people, shelf, people_list


class Test_buhgalter:

    def test_people(self):
        assert people("10006") == "Аристарх Павлов"
    def test_shelf(self):
        assert shelf('11-2') == '1'
    def test_people_list(self):
        assert people_list('11-2') == '1'