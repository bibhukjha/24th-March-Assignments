import unittest
def ero(x):
    if x%2==0:
        return "Even"
    else:
        return "Odd"

def prn(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return "Is not a prime number"
            else:
                return "Is a prime number"

def divseven(x):
    if x%7==0:
        return "Is Divisible"
    else:
        return "Is not Divisible"

class EROapp(unittest.TestCase):
     def test_case1(self):
         x = 4
         r = ero(x)
         self.assertEqual("Even", r)

     def test_case2(self):
         x = 5
         r = ero(x)
         self.assertEqual("Odd", r)
class primeapp(unittest.TestCase):

     def test_case3(self):
         x = 3
         r = prn(x)
         self.assertEqual("Is a prime number", r)
     def test_case4(self):
         x = 10
         r = prn(x)
         self.assertEqual("Is not a prime number", r)
class sevenapp(unittest.TestCase):
    def test_case5(self):
        x = 14
        r = divseven(x)
        self.assertEqual("Is Divisible", r)
    def test_case6(self):
        x = 15
        r = divseven(x)
        self.assertEqual("Is not Divisible", r)
if __name__=="__main__":
    unittest.main()