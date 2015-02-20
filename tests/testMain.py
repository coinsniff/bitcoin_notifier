__author__ = 'michaelluo'

import unittest
import main

class TestMainFunctions(unittest.TestCase):

    def test_checkArgs(self):
        self.assertTrue(main.checkValidArgs([1,2]))
        self.assertFalse(main.checkValidArgs(['.py', '340.00', '>=', 'test@test.com', '1', 'coinbase']))
        self.assertFalse(main.checkValidArgs(['.py', '340', '>=', 'test@test.com', '1', 'bitfinex']))
        self.assertTrue(main.checkValidArgs(['.py', '340', 'blah', 'test@test.com', '1', 'coinbase']))
        self.assertTrue(main.checkValidArgs(['.py', '340', 'blah', 'asdf@', '1','coinbase']))
        self.assertTrue(main.checkValidArgs(['.py', '340', 'blah', 'asdf.', '1','coinbase']))
        self.assertTrue(main.checkValidArgs(['.py', '340', 'blah', 'asdf@', 'asdf,','coinbase']))
        self.assertTrue(main.checkValidArgs(['.py', '340.00', '>=', 'test@test.com', '1', 'not an exchange']))

    def test_comparePrices(self):
        self.assertFalse(main.comparePrices(500, 200, '<'))
        self.assertTrue(main.comparePrices(500, 200, '>'))
        self.assertFalse(main.comparePrices(200, 500, '>'))
        self.assertTrue(main.comparePrices(200, 500, '<'))

if __name__ == '__main__':
    unittest.main()