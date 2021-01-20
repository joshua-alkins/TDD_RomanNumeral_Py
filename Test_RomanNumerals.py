import unittest
from RomanNumeral import convertToRomanNumerals
import math

class RomanNumeralTestMethods(unittest.TestCase):
    def testTypeError(self):
        self.assertRaises(TypeError,convertToRomanNumerals,'I')
        self.assertRaises(TypeError,convertToRomanNumerals,0.11)
        self.assertRaises(TypeError,convertToRomanNumerals,1j)

    def testZero(self):
        self.assertEquals(convertToRomanNumerals(0),'')

    def testI(self):
        self.assertEquals(convertToRomanNumerals(1),'I')
        self.assertEquals(convertToRomanNumerals(2),'II')

    def testIV(self):
        self.assertEquals(convertToRomanNumerals(4),'IV')

    def testV(self):
        self.assertEquals(convertToRomanNumerals(5),'V')
        self.assertEquals(convertToRomanNumerals(8),'VIII')

    def testIX(self):
        self.assertEquals(convertToRomanNumerals(9),'IX')

    def testX(self):
        self.assertEquals(convertToRomanNumerals(10),'X')
        self.assertEquals(convertToRomanNumerals(13),'XIII')
        self.assertEquals(convertToRomanNumerals(14),'XIV')
        self.assertEquals(convertToRomanNumerals(15),'XV')
        self.assertEquals(convertToRomanNumerals(18),'XVIII')
        self.assertEquals(convertToRomanNumerals(19),'XIX')
    
    def testXX(self):
        self.assertEquals(convertToRomanNumerals(20),'XX')
        self.assertEquals(convertToRomanNumerals(24),'XXIV')
        self.assertEquals(convertToRomanNumerals(25),'XXV')
        self.assertEquals(convertToRomanNumerals(28),'XXVIII')
        self.assertEquals(convertToRomanNumerals(29),'XXIX')
        self.assertEquals(convertToRomanNumerals(30),'XXX')

    def testXL(self):
        self.assertEquals(convertToRomanNumerals(40),'XL')
        self.assertEquals(convertToRomanNumerals(41),'XLI')
        self.assertEquals(convertToRomanNumerals(44),'XLIV')
        self.assertEquals(convertToRomanNumerals(49),'XLIX')


    def testL(self):
        self.assertEquals(convertToRomanNumerals(50),'L')
        self.assertEquals(convertToRomanNumerals(52),'LII')
        self.assertEquals(convertToRomanNumerals(54),'LIV')
        self.assertEquals(convertToRomanNumerals(55),'LV')
        self.assertEquals(convertToRomanNumerals(57),'LVII')
        self.assertEquals(convertToRomanNumerals(59),'LIX')
    
if __name__ == '__main__':
    unittest.main()