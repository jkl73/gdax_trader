# Requires python-requests. Install with pip:
#
#   pip install requests
#
# or, with easy-install:
#
#   easy_install requests

import json, hmac, hashlib, time, requests, base64
import datetime
import gdax_comm
from decimal import Decimal

# MAIN START
# AUTH Head Info
with open('config.json') as api_secret:
    api_credential = json.load(api_secret)

API_KEY = api_credential['api_key']
API_SECRET = api_credential['api_secret']
API_PASS = api_credential['api_pass']
auth = gdax_comm.CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)

# Get accounts
r = gdax_comm.getAccount(auth)
print ("* * * * * *")
print ("* Available Funds: " + r.json()[0]['available'])
print ("* Total Balance: " + r.json()[0]['balance'])
print ("* * * * * *")

# Constants
mainLoopPeroid = 1

# Vars
prevPrc = Decimal(gdax_comm.getLatestPrice('ETH-USD').json()['price'])

# Main Loop
while True:
    time.sleep(mainLoopPeroid)

    print("@" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    gdax_comm.placeLimit('limit', 0.01, 10, 'buy', 'GTC', True, 'ETH-USD')

    curPrc = Decimal(gdax_comm.getLatestPrice('ETH-USD').json()['price'])

    print curPrc

    if (prevPrc > curPrc):
        print "vvv " + str(prevPrc - curPrc)
        prevPrc = curPrc
    elif (prevPrc < curPrc):
        print "^^^ " + str(curPrc - prevPrc)
        prevPrc = curPrc
    else:
        print "---"

    #listOrders('open', 'ETH-USD')

    #cancelAllOrders('ETH-USD')

    gdax_comm.bidsAsksDiff('ETH-USD')

    print "-----------------------------------------------"

