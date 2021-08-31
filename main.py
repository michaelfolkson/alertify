#!/usr/bin/env python3
"""Sends a text message when the Bitcoin price hits a certain threshold"""
import requests
import json
import smsalert
import secrets
import time
import sys

def checksite():
    """Requests various Bitcoin price data from Bitfinex"""
    response = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    jsonresponse = json.loads(response.text)
    return jsonresponse

def is_price_too_high(threshold):
    """Returns whether the price is above a certain threshold or not, boolean"""
    price=checksite()["mid"]
    price=float(price)
    if price > threshold:
        result = True
    else: result = False
    return result

def send_sms():
    print("Sending SMS")
    message = smsalert.client.messages \
                    .create(
                         body="The Bitcoin price is now....",
                     from_= secrets.twilio_phone,
                     to= secrets.my_phone
                 )

    return(message.sid)

while True:
  print("Checking prices")
  time.sleep(5)
  if is_price_too_high(40000) == True:
      send_sms()
      sys.exit()
  else: print("The price is not too high")

# check price, if lower than limit, sleep and then check again
# if higher than limit send message and exit loop


