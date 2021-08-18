#!/usr/bin/env python3

import requests
import json
import smsalert
import secrets
# import importlib

# importlib.import_module(smsalert)

def checksite():
    response = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    jsonresponse = json.loads(response.text)
    return jsonresponse
print("The price is",checksite()["mid"])

message = smsalert.client.messages \
                .create(
                     body="The Bitcoin price is now....",
                     from_= secrets.twilio_phone,
                     to= secrets.my_phone
                 )

print(message.sid)
