import pytest
from main import people



class Test_buhgalter:
    def setup(self):
      print(1)


    def test_people(self):
        assert people(10006) == "Аристарх Павлов"

    def teardown(self):
        print(2)