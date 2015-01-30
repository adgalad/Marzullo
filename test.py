'''
Created on Jan 29, 2015

@author: Jose Daniel
'''
import unittest
from Marzullo import reserva


class Test(unittest.TestCase):


    def testName(self):
        pass

    def testNoReserva(self):
        reservas = reserva()
        msg = 'no reservas'
        self.assertEqual(True, reservas.validar(), msg)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()