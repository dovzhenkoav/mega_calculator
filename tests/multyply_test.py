from unittest import TestCase
from multiply import multiply


class CalculateTest(TestCase):

    def test_multiply(self):
        self.assertEqual(multiply("4*2"), 8)
        self.assertEqual(multiply("30*4"), 120)
        self.assertEqual(multiply("15*3"), 45)
        self.assertEqual(multiply("4*0"), 0)