import unittest
import ekkachai_ittihrit_hw1

class testLeap(unittest.TestCase):
    def testZero(self):
        self.assertEqual(ekkachai_ittihrit_hw1.leap(0), "Leap year!")




if __name__ == '__main__':
    unittest.main()