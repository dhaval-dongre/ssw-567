# -*- coding: utf-8 -*-
"""

@author: Dhaval Dongre
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    if (a <= 0 or b<=0 or c<=0) or ((a > b + c) or (b > a + c) or (c > a + b)):
        return 'NotATriangle'
    
    if a == b and b == c: # Equilateral Triangle
        return 'Equilateral Triangle'

    if a != b and  b != c and a != c: # Scalene Triangle
        if checkRight(a,b,c): # Right Scalene Triangle
            return 'Right Scalene Triangle'
        else:
            return 'Scalene Triangle'

    if (a == b) or (a == c) or (b == c): # Isoceles TRIANGLE
        if checkRight(a,b,c): # Right Isoceles Triangle
            return 'Right Isoceles Triangle'
        else:
            return 'Isoceles Triangle'

        
def checkRight(a,b,c):
    if (a**2 + b**2 == c**2) or  (c**2 + b**2 == a**2) or (a**2 + c**2 == b**2):# Right Triangle
        return True

#def runClassifyTriangle(a, b, c):
#    """ invoke classifyTriangle with the specified arguments and print the result """
#    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    # with 'test'.  Each function may include multiple tests

    def testRightTriangle(self):
        assert classifyTriangle(3, 4, 5) == 'Right Scalene Triangle'
        assert classifyTriangle(6, 8, 10) == 'Right Scalene Triangle'

    def testEquilateralTriangle(self):
        assert classifyTriangle(1, 1, 1) == 'Equilateral Triangle'
        assert classifyTriangle(100, 100, 100) == 'Equilateral Triangle'
        assert classifyTriangle(101, 100, 100) != 'Equilateral Triangle'

    def testIsocelesTriangle(self):
        assert classifyTriangle(10, 10, 10) != 'Isoceles Triangle'
        assert classifyTriangle(5, 5, 3) == 'Isoceles Triangle'

    def testScaleneTriangle(self):
        assert classifyTriangle(11, 9, 14) == 'Scalene Triangle'
        assert classifyTriangle(5.7, 7.4, 9) == 'Scalene Triangle'

    def testNotATriangle(self):
        assert classifyTriangle(100, 1, 1) == 'NotATriangle'
        assert classifyTriangle(-1, -1, -1) == 'NotATriangle'
        assert classifyTriangle(0, 0, 0) == 'NotATriangle'

if __name__ == '__main__':
    # examples of running the code
    #runClassifyTriangle(1,2,3)
    #runClassifyTriangle(1,1,1)
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
        
       
       