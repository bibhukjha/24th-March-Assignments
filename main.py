import unittest

def add(x,y):
    return x+y

def add2(x,y,z):
    return x+y+z

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

class myCalapp(unittest.TestCase):
    def test_case1(self):
         a = 10
         b = 20
         result = add(a, b)
         self.assertEqual(a+b, result)
    def test_case2(self):
         a=10
         b=20
         c=30
         result = add2(a, b, c)
         self.assertEqual(a+b+c, result)

    def test_case3(self):
        a = 10
        b = 20
        result = sub(a, b)
        self.assertEqual(a - b, result)

    def test_case4(self):
        a = 10
        b = 20
        result = mul(a, b)
        self.assertEqual(a * b, result)

    def test_case5(self):
        a = 10
        b = 20
        result = div(a, b)
        self.assertEqual(a / b, result)

if __name__ == "__main__":
    unittest.main()