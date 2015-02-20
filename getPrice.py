__author__ = 'michaelluo'


def tryGettingPrice(timesToTry, url):
    '''
    Tries getting the price x times (to account for HTTP errors and slow networks)

    '''
    from urllib2 import urlopen, HTTPError, URLError
    from json import loads
    for x in range(0, timesToTry):
        try:
            genericJSON = loads(urlopen(url).read())
            return genericJSON
        except HTTPError:
            print HTTPError
        except URLError:
            print URLError

    return None

def getBitfinexPrice():
    '''
    Gets bitfinex price (last price)

    '''
    bitfinexJSON = tryGettingPrice(10000, "https://api.bitfinex.com/v1/pubticker/BTCUSD")
    price = float(bitfinexJSON['last_price'])
    return price

def getBitstampPrice():
    bitstampJSON = tryGettingPrice(10000, "https://www.bitstamp.net/api/ticker/")
    price = float(bitstampJSON['last'])
    return price

def getBtcePrice():
    bitstampJSON = tryGettingPrice(10000, "https://btc-e.com/api/3/ticker/btc_usd")
    price = float(bitstampJSON['btc_usd']['last'])
    return price

def getCoinbaseExchangePrice():
    bitstampJSON = tryGettingPrice(10000, "https://api.exchange.coinbase.com/products/btc-usd/ticker")
    price = float(bitstampJSON['price'])
    return price

def getCoinbasePrice():
    '''
    Use HTTP GET to get the price of 1 bitcoin.

    Returns (double) price of 1 bitcoin WITHOUT any fees.
    '''
    coinbaseJSON = tryGettingPrice(10000, "https://api.coinbase.com/v1/prices/buy?qty=1")
    price = float(coinbaseJSON['subtotal']['amount'])

    return price

def getExchangePrice(exchange):
    if exchange.lower() == 'coinbase':
        return getCoinbasePrice()
    if exchange.lower() == 'bitfinex':
        return getBitfinexPrice()
    if exchange.lower() == 'bitstamp':
        return getBitstampPrice()
    if exchange.lower() == 'btc-e':
        return getBtcePrice()
    if exchange.lower() == 'coinbase exchange':
        return getCoinbaseExchangePrice()