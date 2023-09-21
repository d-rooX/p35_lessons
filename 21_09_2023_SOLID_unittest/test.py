import unittest



def add(a, b):
    return a + b


def div(a, b):
    return a / b


class Fraction:
    ...

class TestFraction(unittest.TestCase):
    ...


class TestCalc(unittest.TestCase):
    # def test_add(self):
    #     self.assertEqual(add(10, 15), 25)
    #     self.assertEqual(add(0, 0), 0)
    #     self.assertEqual(add(1, -1), 0)
    #     self.assertEqual(add(-10, -1000), -1010)

    # def test_add(self):
    #     self.assertEqual((d1 + d2).value, 0.5)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(1, 1), 1)
        self.assertEqual(div(15, 2), 7.5)

        self.assertRaises(ZeroDivisionError, div, 5, 0)


if __name__ == '__main__':
    unittest.main()
