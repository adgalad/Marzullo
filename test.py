#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
        myParking = parking(1)
        self.assertTrue(myParking.fits("0900", "1500"))

    def testNoSpotParking(self):
        myParking = parking(0)
        self.assertFalse(myParking.fits("0900", "1500"))

    def testTenSpotsOneReservation(self):
        myParking = parking(10)
        myParking.addReservation("0900","1800")
        self.assertTrue(myParking.fits("0900", "1500"))

    def testNoAceptaAdd(self):
        myParking = parking(10)
        msg = "no debe agregar"
        self.assertRaises(ValueError,myParking.addReservation,"0900","0600")

    def testAddTwoReservation(self):
        myParking = parking(10)
        myParking.addReservation("0900","1800")
        myParking.addReservation("0900","1800")
        self.assertEqual(myParking.occupation,[(900,1),(1800,-1),(900,1),(1800,-1)])

    def testAddTreeReservation(self):
        myParking = parking(10)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        self.assertEqual(myParking.occupation,[(900,1),(1800,-1),(1000,1),(1800,-1),(1200,1),(1800,-1)])

    def testFiveSpotsFiveReservation(self):
        myParking = parking(5)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1000","1800")
        self.assertFalse(myParking.fits("0900", "1500"))

    def testFiveSpotsSixReservation(self):
        myParking = parking(5)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1000","1800")
        self.assertFalse(myParking.fits("0900", "1500"))

    def testFiveSpotsSixReservationNoOverlapping(self):
        myParking = parking(5)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("0600","1000")
        self.assertFalse(myParking.fits("0900", "1500"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
