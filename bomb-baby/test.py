import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(0, solution(1, 1))

    def test_2_1(self):
        self.assertEqual(1, solution(2, 1))

    def test_1_2(self):
        self.assertEqual(1, solution(1, 2))

    def test_1_100(self):
        self.assertEqual(99, solution(1, 100))

    def test_100_1(self):
        self.assertEqual(99, solution(100, 1))

    def test_4_7(self):
        self.assertEqual(4, solution(4, 7))

    def test_7_4(self):
        self.assertEqual(4, solution(7, 4))

    def test_5_8(self):
        self.assertEqual(4, solution(5, 8))

    def test_8_5(self):
        self.assertEqual(4, solution(8, 5))

    def test_2_7(self):
        self.assertEqual(4, solution(2, 7))

    def test_7_2(self):
        self.assertEqual(4, solution(7, 2))


if __name__ == '__main__':
    unittest.main()
