import unittest
from shifts import solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        data = [1, 2, 3]
        n = 0
        expected = []
        self.assertEqual(solution(data, n), expected)

    def test_2(self):
        data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
        n = 1
        expected = [1, 4]
        self.assertEqual(solution(data, n), expected)

    def test_3(self):
        data = [5, 10, 15, 10, 7]
        n = 1
        expected = [5, 15, 7]
        self.assertEqual(solution(data, n), expected)


if __name__ == "__main__":
    unittest.main()
