import unittest
from RomanNumeral import convertToRomanNumerals

class RomanNumeralTestMethods(unittest.TestCase):
    def testFirstDigit(self):
        self.assetEqual(convertToRomanNumerals(1),'I')


if __name__ == '__main__':
    unittest.main()