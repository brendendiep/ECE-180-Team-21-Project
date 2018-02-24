import json
import re
def loadAndDump(filename, coin_name):
    ## Loading coin data and encode the data in json file
    coin = {}
    coin["description"] = coin_name +" data from coinmarketcap"
    coin["column_names"] = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']
    coin["data"] = []    
    with open(filename,"rb") as f:
        for l in f:
            l = re.sub(',', '',l[:-1])
            l = re.sub('-', '0',l)
            d = l.split('\t')
            d[1:] = map(float,d[1:])
            coin["data"].append(d)
    with open(filename+'.json', 'wb') as fp:
        json.dump(coin, fp,sort_keys=True,indent=4, separators=(',', ': '))

## Loading BTC data and encode the data in json file
loadAndDump("BTC_USD(coinmarketcap)", "Bit Coin")
## Loading BTC data and encode the data in json file
loadAndDump("ETH_USD(coinmarketcap)", "Ethereum")
## Loading Ripple data and encode the data in json file
loadAndDump("RIPPLE_USD(coinmarketcap)", "Ripple")