import unittest

from solution import solution


class MyTestCase(unittest.TestCase):
    def test_15(self):
        self.assertEqual(5, solution(15))

    def test_4(self):
        self.assertEqual(4, solution(2))


if __name__ == '__main__':
    unittest.main()
