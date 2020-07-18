import unittest

from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, solution(1))

    def test_2(self):
        self.assertEqual(1, solution(2))

    def test_3(self):
        self.assertEqual(2, solution(3))

    def test_4(self):
        self.assertEqual(2, solution(4))

    def test_5(self):
        self.assertEqual(3, solution(5))

    def test_6(self):
        self.assertEqual(3, solution(6))

    def test_7(self):
        self.assertEqual(4, solution(7))

    def test_8(self):
        self.assertEqual(3, solution(8))

    def test_9(self):
        self.assertEqual(4, solution(9))

    def test_15(self):
        self.assertEqual(5, solution(15))

    def test_16(self):
        self.assertEqual(4, solution(16))


if __name__ == '__main__':
    unittest.main()
