import unittest
import ekkachai_ittihrit_hw1

class testLeap(unittest.TestCase):
    def testZero(self):
        self.assertEqual(ekkachai_ittihrit_hw1.leap(0), "Leap year!")
    def testWorkingLeapYear(self):
        self.assertEqual(ekkachai_ittihrit_hw1.leap(2000), "Leap year!")
    def testNeg(self):
        self.assertEqual(ekkachai_ittihrit_hw1.leap(-1900), "Invalid input")
    def testNonLeapYear(self):
        self.assertEqual(ekkachai_ittihrit_hw1.leap(2001), "Not a leap year!")




if __name__ == '__main__':
    unittest.main()