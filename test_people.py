from main import people, shelf, add_command
import unittest

class TestBuhgalter(unittest.TestCase):

    def test_people(self):
        self.assertEqual(people('10006'), "Аристарх Павлов")

    def test_shelf(self):
        self.assertEqual(shelf('11-2'), "1")

    def test_add_command(self):
        self.assertEqual(add_command("zagran_passport", "1548 356426", "Василий Тупкин", "4"), "Введенной полки не существует")

# if __name__ == '__main__':
#     TestBuhgalter()