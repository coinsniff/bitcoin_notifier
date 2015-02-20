__author__ = 'michaelluo'

import unittest
import getPrice

class TestPriceFunctions(unittest.TestCase):

    def test_tryGettingPrice(self):
        priceJSON = getPrice.tryGettingPrice(2, "https://api.coinbase.com/v1/prices/buy?qty=1")
        self.assertIsNotNone(priceJSON)
        self.assertTrue(priceJSON.has_key('subtotal'))
        self.assertTrue(priceJSON['subtotal'].has_key('amount'))

        priceJSON = getPrice.tryGettingPrice(2, "https://api.bitfinex.com/v1/pubticker/BTCUSD")
        self.assertIsNotNone(priceJSON)
        self.assertTrue(priceJSON.has_key('last_price'))

    def test_getCoinbasePrice(self):
        price = getPrice.getCoinbasePrice()
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)

    def test_getBitfinexPrice(self):
        price = getPrice.getBitfinexPrice()
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)

    def test_getBitstampPrice(self):
        price = getPrice.getBitstampPrice()
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)

    def test_getBtcePrice(self):
        price = getPrice.getBtcePrice()
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)

    def test_getCoinbaseExchangePrice(self):
        price = getPrice.getCoinbaseExchangePrice()
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)

    def test_getExchangePrice(self):
        price = getPrice.getBitfinexPrice()
        exchangePrice = getPrice.getExchangePrice('bitfinex')
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)
        self.assertIsNotNone(exchangePrice)
        self.assertIsInstance(exchangePrice, float)
        self.assertEquals(price, exchangePrice)

        price = getPrice.getCoinbasePrice()
        exchangePrice = getPrice.getExchangePrice('coinbase')
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)
        self.assertIsNotNone(exchangePrice)
        self.assertIsInstance(exchangePrice, float)
        self.assertEquals(price, exchangePrice)



if __name__ == '__main__':
    unittest.main()