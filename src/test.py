import unittest
from Calculator import *
from read_data import *


class test(unittest.TestCase):

    # def setUp(self):
    #     print("do something befor test.prepare environment")

    # def tearDown(self):
    #     print("do something after test.Clean up")

    def test_add(self):
        df = read_data(AdditionPath)
        for i in range(len(df)):
            a=df.iat[i,0]
            b=df.iat[i,1]
            c=df.iat[i,2]
            self.assertEqual(c,add(a,b))

    def test_minus(self):
        df = read_data(SubtractionPath)
        for i in range(len(df)):
            a=df.iat[i,0]
            b=df.iat[i,1]
            c=df.iat[i,2]
            self.assertEqual(c,minus(b,a))

    def test_Multi(self):
        df = read_data(MultiplicationPath)
        for i in range(len(df)):
            a=df.iat[i,0]
            b=df.iat[i,1]
            c=df.iat[i,2]
            self.assertEqual(c,multi(a,b))

    def test_divide(self):
        df = read_data(DivisionPath)
        for i in range(len(df)):
            a=df.iat[i,0]
            b=df.iat[i,1]
            c=df.iat[i,2]
            self.assertAlmostEqual(c,divide(b,a))

    def test_square(self):
        df = read_square(SquarePath)
        for i in range(len(df)):
            a=df.iat[0,0]
            b=df.iat[0,1]
            self.assertEqual(b,square(a))

    def test_squreRoot(self):
        df = read_square(SquareRootPath)
        for i in range(len(df)):
            a=df.iat[0,0]
            b=df.iat[0,1]
            self.assertAlmostEqual(b,squareRoot(a))

if __name__ == '__main__':
    unittest.main()
