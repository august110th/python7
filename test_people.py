import pytest
from main import people



class Test_buhgalter:

     def test_people(self):
        assert people("10006") == "Аристарх Павлов"
