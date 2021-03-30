import unittest
import chops


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(-1, chops.chop(3, []))

    def test1(self):
        self.assertEqual(-1, chops.chop(3, [1]))

    def test2(self):
        self.assertEqual(0, chops.chop(1, [1]))

    def test3(self):
        self.assertEqual(0, chops.chop(1, [1, 3, 5]))

    def test4(self):
        self.assertEqual(1, chops.chop(3, [1, 3, 5]))

    def test5(self):
        self.assertEqual(2, chops.chop(5, [1, 3, 5]))

    def test6(self):
        self.assertEqual(-1, chops.chop(0, [1, 3, 5]))

    def test7(self):
        self.assertEqual(-1, chops.chop(2, [1, 3, 5]))

    def test8(self):
        self.assertEqual(-1, chops.chop(4, [1, 3, 5]))

    def test9(self):
        self.assertEqual(-1, chops.chop(6, [1, 3, 5]))

    def test10(self):
        self.assertEqual(-1, chops.chop(0, [1, 3, 5, 7]))

    def test11(self):
        self.assertEqual(-1, chops.chop(2, [1, 3, 5, 7]))

    def test12(self):
        self.assertEqual(-1, chops.chop(6, [1, 3, 5, 7]))


if __name__ == '__main__':
    unittest.main()
