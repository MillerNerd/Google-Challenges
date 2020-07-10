import unittest
from LAMBs import stingy, lambs, generous


class MyTestCase(unittest.TestCase):
    def test_stingy_1(self):
        self.assertEqual(stingy(1), 1)

    def test_stingy_2(self):
        self.assertEqual(stingy(2), 2)

    def test_stingy_3(self):
        self.assertEqual(stingy(3), 2)

    def test_stingy_4(self):
        self.assertEqual(stingy(4), 3)

    def test_stingy_10(self):
        self.assertEqual(stingy(10), 4)

    def test_stingy_19(self):
        self.assertEqual(stingy(19), 5)

    def test_stingy_20(self):
        self.assertEqual(stingy(20), 6)

    def test_stingy_231(self):
        self.assertEqual(stingy(231), 10)

    def test_stingy_232(self):
        self.assertEqual(stingy(232), 11)

    def test_stingy_143(self):
        self.assertEqual(stingy(143), 10)

    def test_generous_1(self):
        self.assertEqual(generous(1), 1)

    def test_generous_2(self):
        self.assertEqual(generous(2), 1)

    def test_generous_3(self):
        self.assertEqual(generous(3), 2)

    def test_generous_4(self):
        self.assertEqual(generous(4), 2)

    def test_generous_126(self):
        self.assertEqual(generous(126), 6)

    def test_generous_127(self):
        self.assertEqual(generous(127), 7)

    def test_generous_128(self):
        self.assertEqual(generous(128), 7)

    def test_lambs_143(self):
        self.assertEqual(lambs(143), 3)

    def test_lambs_10(self):
        self.assertEqual(lambs(10), 1)


if __name__ == '__main__':
    unittest.main()
