#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Jan 29, 2015
@authors: Jose Duran, Mois��s Ackerman, Carlos Spaggiari
'''
import unittest
from marzullo import parking

class Test(unittest.TestCase):
    def testName(self):
        pass

    def testOneReservation(self): #borde
        myParking = parking(1)
        self.assertTrue(myParking.addReservation("0900", "1500"))

    def testNoSpotParking(self): #borde
        myParking = parking(0)
        self.assertFalse(myParking.addReservation("0900", "1500"))

    def testTenSpotsOneReservation(self): #malicia
        myParking = parking(10)
        self.assertTrue(myParking.addReservation("0900", "1500"))

    def testNoAceptaAdd(self): #malicia
        myParking = parking(10)
        msg = "no debe agregar"
        self.assertRaises(ValueError,myParking.addReservation,"0900","0600")

    def testAddTwoReservation(self): #malicia
        myParking = parking(10)
        myParking.addReservation("0900","1800")
        myParking.addReservation("0900","1800")
        self.assertEqual(myParking.occupation,[(900,1),(1800,-1),(900,1),(1800,-1)])

    def testAddTreeReservation(self): #malicia
        myParking = parking(10)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        self.assertEqual(myParking.occupation,[(900,1),(1800,-1),(1000,1),(1800,-1),(1200,1),(1800,-1)])

    def testFiveSpotsFiveReservation(self): #Borde
        myParking = parking(5)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1000","1800")
        self.assertTrue(myParking.addReservation("1000","1800"))

    def testFiveSpotsSixReservation(self): #borde
        myParking = parking(5)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1000","1800")
        self.assertFalse(myParking.addReservation("1000","1800"))
        self.assertFalse(myParking.addReservation("0900", "1500"))

    def testFiveSpotsSixReservationNoOverlapping(self): #esquina
        myParking = parking(5)
        myParking.addReservation("0900","1800")
        myParking.addReservation("1000","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1200","1800")
        myParking.addReservation("1000","1800")
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0900", "1200"))

    def testManyReservationsMaxOverlapping(self): #malicia
        myParking = parking(10)
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0700","1000"))
        self.assertTrue(myParking.addReservation("0800","1000"))
        self.assertTrue(myParking.addReservation("0900","1000"))
        self.assertTrue(myParking.addReservation("0700","1100"))
        self.assertTrue(myParking.addReservation("0800","1200"))
        self.assertTrue(myParking.addReservation("0900","1300"))
        self.assertTrue(myParking.addReservation("0600","0900"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))

    def testManyReservationsOneOverlap(self): #malicia y esquinas
        myParking = parking(10)
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0700","1000"))
        self.assertTrue(myParking.addReservation("0800","1000"))
        self.assertTrue(myParking.addReservation("0900","1000"))
        self.assertTrue(myParking.addReservation("0700","1100"))
        self.assertTrue(myParking.addReservation("0800","1200"))
        self.assertTrue(myParking.addReservation("0900","1300"))
        self.assertTrue(myParking.addReservation("0600","0900"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertFalse(myParking.addReservation("0900","1000"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))

    def testNoMilitaryFormat(self): #malicia
        myParking = parking(10)
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0700","1000"))
        self.assertTrue(myParking.addReservation("0800","1000"))
        self.assertTrue(myParking.addReservation("0900","1000"))
        self.assertTrue(myParking.addReservation("0700","1100"))
        self.assertTrue(myParking.addReservation("0800","1200"))
        self.assertTrue(myParking.addReservation("0900","1300"))
        self.assertTrue(myParking.addReservation("0600","0900"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertTrue(myParking.addReservation("0600","1000"))
        self.assertFalse(myParking.addReservation("0900","1000"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))
        self.assertTrue(myParking.addReservation("1000","1500"))

    def testSameHOurInOut(self):
        myParking = parking(0)
        self.assertTrue(myParking.addReservation("0600", "0600"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
