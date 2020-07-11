import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_2(self):
        expectation = ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
        given = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
        self.assertEqual(expectation, solution(given))

    def test_1(self):
        expectation = ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
        given = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
        self.assertEqual(expectation, solution(given))


if __name__ == '__main__':
    unittest.main()
