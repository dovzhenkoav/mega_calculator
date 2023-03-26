from unittest import TestCase, main
from calculator import calculate


class CalculateTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculate("1+1"), 2)
        self.assertEqual(calculate("5+10"), 15)
        # self.assertEqual(calculate("-10+5"), -5)
        self.assertEqual(calculate("0+100"), 100)

    def test_minus(self):
        self.assertEqual(calculate("5-1"), 4)
        self.assertEqual(calculate("100-50"), 50)
        self.assertEqual(calculate("15-50"), -35)
        self.assertEqual(calculate("4-0"), 4)

    def test_multiply(self):
        self.assertEqual(calculate("4*2"), 8)
        self.assertEqual(calculate("30*4"), 120)
        self.assertEqual(calculate("15*3"), 45)
        self.assertEqual(calculate("4*0"), 0)

    def test_division(self):
        self.assertEqual(calculate("75/25"), 3)
        self.assertEqual(calculate("1000/50"), 20)
        self.assertEqual(calculate("10/5"), 2)
        self.assertEqual(calculate("4/1"), 4)

    def test_division_error(self):
        with self.assertRaises(ZeroDivisionError) as err:
            calculate("5/0")
        self.assertEqual('Нихуя! На ноль делить нельзя', err.exception.args[0])

    def test_value_error(self):
        with self.assertRaises(ValueError):
            calculate("1++1")

    def test_no_signs(self):
        with self.assertRaises(ValueError):
            calculate("11")


if __name__ == '__main__':
    main()

