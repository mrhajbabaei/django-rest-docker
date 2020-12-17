from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 5), 8)

    def test_subtract_numbers(self):
        """Test that values are subtracted correctly"""
        self.assertEqual(subtract(4, 17), 13)
