from unittest import TestCase, main
from division import division


class DivisionTest(TestCase):
    def test_positive_nums(self):
        self.assertEqual(division('19/9'), 2)
        self.assertEqual(division('0/2'), 0)
        self.assertEqual(division('100/10'), 10)
        self.assertEqual(division('9/1'), 9)

    def test_division_error(self):
        with self.assertRaises(ZeroDivisionError) as err:
            division('9/0')
        self.assertEqual('Нихуя! На ноль делить нельзя', err.exception.args[0])


if __name__ == '__main__':
    main()
