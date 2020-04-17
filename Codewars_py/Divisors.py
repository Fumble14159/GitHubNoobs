import unittest
#Given an Integer, return an array of its divisors
#If it´s prime, return 'integer is prime'

def divisors(integer):
    res = []

    for x in range(2,integer):
        if(integer%x)==0:
            res.append(x)
    
    if len(res)==0:
        return '%d is prime' % (integer)
    else:
        return res
        

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(divisors(15), [3, 5])
    def test2(self):
        self.assertEqual(divisors(12), [2, 3, 4, 6])
    def test3(self):
        self.assertEquals(divisors(13), "13 is prime")
