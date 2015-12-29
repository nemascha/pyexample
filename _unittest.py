# coding=utf-8
'''
assertEqual(a, b
assertNotEqual(a, b)
assertTrue(x
assertFalse(x)
assertIs(a, b)
assertIsNot(a, b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertNotIn(a, b)
assertIsInstance(a, b)
assertNotIsInstance(a, b)
'''
import unittest

x = range(10)
element = 4

class TestFunction(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(x, range(10), 'My own comment.')
        self.assertNotEqual(x, range(11, 14))

    def test_in(self):
        self.assertTrue(element in x, 'The second comment')
        self.assertFalse(element not in x)



if __name__ == '__main__':

    test_equal(__main__.TestFunction)
    test_in(__main__.TestFunction)

    #unittest.main()
