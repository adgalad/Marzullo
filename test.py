#!/usr/bin/env python3
'''
Created on Jan 29, 2015
@authors: Jose Duran, Moisés Ackerman, Carlos Spaggiari
'''
import unittest
from Marzullo import parking

class Test(unittest.TestCase):
    def testName(self):
        pass

    def testNoReservations(self):
        myParking = parking(0)
        self.assertTrue(myParking.fits())

    def testFirstReservation(self):
        myParking = parking(10)
        self.assertTrue(myParking.fits())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()