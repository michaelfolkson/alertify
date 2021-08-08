#!/usr/bin/env python3

import requests
import json
def checksite():
    response = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    jsonresponse = json.loads(response.text)
    return jsonresponse
print("The price is",checksite()["mid"])
