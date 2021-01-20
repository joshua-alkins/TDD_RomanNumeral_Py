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
    

    def testLXXX(self):
        self.assertEquals(convertToRomanNumerals(80),'LXXX')
        self.assertEquals(convertToRomanNumerals(84),'LXXXIV')
        self.assertEquals(convertToRomanNumerals(89),'LXXXIX')

    def testXL(self):
        self.assertEquals(convertToRomanNumerals(90),'XC')
        self.assertEquals(convertToRomanNumerals(94),'XCIV')
        self.assertEquals(convertToRomanNumerals(97),'XCVII')
        self.assertEquals(convertToRomanNumerals(99),'XCIX')

    def testC(self):
        self.assertEquals(convertToRomanNumerals(100),'C')
        self.assertEquals(convertToRomanNumerals(155),'CLV')
        self.assertEquals(convertToRomanNumerals(209),'CCIX')
        self.assertEquals(convertToRomanNumerals(344),'CCCXLIV')
        self.assertEquals(convertToRomanNumerals(391),'CCCXLI')

    def testCD(self):
        self.assertEquals(convertToRomanNumerals(400),'CD')
        self.assertEquals(convertToRomanNumerals(444),'CDXLIV')

    def testD(self):
        self.assertEquals(convertToRomanNumerals(500),'D')
        self.assertEquals(convertToRomanNumerals(744),'DCCXLIV')
        self.assertEquals(convertToRomanNumerals(899),'DCCCXCIX')

    def testCM(self):
        self.assertEquals(convertToRomanNumerals(900),'CM')
        
    def testM(self):
        self.assertEquals(convertToRomanNumerals(1000),'M')
        self.assertEquals(convertToRomanNumerals(1744),'MDCCXLIV')
        self.assertEquals(convertToRomanNumerals(1899),'MDCCCXCIX')
        self.assertEquals(convertToRomanNumerals(2000),'MM')
        self.assertEquals(convertToRomanNumerals(3994),'MMMCMXCIV')
        self.assertEquals(convertToRomanNumerals(3744),'MMMDCCXLIV')

if __name__ == '__main__':
    unittest.main()