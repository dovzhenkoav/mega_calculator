from unittest import TestCase, main
from calculator import minus


class Calculator(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Начали тесты")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Тесты закончили")

    def setUp(self) -> None:
        print("Тест начался")

    def tearDown(self) -> None:
        print("Тест закончен")

    def test_minus(self):
        self.assertEqual(minus("5-1"), 4)
        self.assertEqual(minus("100-50"), 50)
        self.assertEqual(minus("15-50"), -35)
        self.assertEqual(minus("4-1"), 3)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            minus("1--1")

    def test_no_signs(self):
        with self.assertRaises(ValueError):
            minus("1 1")


if __name__ == '__main__':
    main()