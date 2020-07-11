import unittest
from LAMBs import stingy, lambs, generous


class StingyTests(unittest.TestCase):
    def test_stingy_1(self):
        self.assertEqual(1, stingy(1))

    def test_stingy_2(self):
        self.assertEqual(2, stingy(2))

    def test_stingy_3(self):
        self.assertEqual(2, stingy(3))

    def test_stingy_4(self):
        self.assertEqual(3, stingy(4))

    def test_stingy_10(self):
        self.assertEqual(4, stingy(10))

    def test_stingy_12(self):
        self.assertEqual(5, stingy(12))

    def test_stingy_19(self):
        self.assertEqual(5, stingy(19))

    def test_stingy_20(self):
        self.assertEqual(6, stingy(20))

    def test_stingy_231(self):
        self.assertEqual(10, stingy(231))

    def test_stingy_232(self):
        self.assertEqual(11, stingy(232))

    def test_stingy_143(self):
        self.assertEqual(10, stingy(143))


class GenerousTests(unittest.TestCase):
    def test_generous_1(self):
        self.assertEqual(1, generous(1))

    def test_generous_2(self):
        self.assertEqual(1, generous(2))

    def test_generous_3(self):
        self.assertEqual(2, generous(3))

    def test_generous_4(self):
        self.assertEqual(2, generous(4))

    def test_generous_126(self):
        self.assertEqual(6, generous(126))

    def test_generous_127(self):
        self.assertEqual(7, generous(127))

    def test_generous_128(self):
        self.assertEqual(7, generous(128))


class FullTest(unittest.TestCase):
    def test_lambs_143(self):
        self.assertEqual(3, lambs(143))

    def test_lambs_10(self):
        self.assertEqual(1, lambs(10))


if __name__ == '__main__':
    unittest.main()
