from unittest import TestCase, main
from plus import plus


class PlusTest(TestCase):
    def test_plus(self):
        self.assertEqual(plus("1+1"), 2)
        self.assertEqual(plus("10+5"), 15)
        self.assertEqual(plus("-60+100"), 40)
        self.assertEqual(plus("-50+1"), -49)


if __name__ == '__main__':
    main()
