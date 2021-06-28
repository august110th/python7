import pytest
from main import people, shelf, add_command


class Test_buhgalter:

    def test_people(self):
        assert people("10006") == "Аристарх Павлов"
    def test_shelf(self):
        assert shelf('11-2') == '1'
    def test_add_command(self):
        assert add_command("zagran_passport", "1548 356426", "Василий Тупкин", '3') ==