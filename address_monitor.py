#!/usr/bin/env python3
"""Print out the latest data on the mempool and the latest block height"""
import requests
import json
import smsalert
import secrets
import time
import sys

def checksite():
    """Gets latest data on the mempool"""
    response = requests.get("https://blockstream.info/api/mempool")
    jsonresponse = json.loads(response.text)
    return jsonresponse

mempool = checksite()
print(mempool)

blockheight = requests.get("https://blockstream.info/api/blocks/tip/height")
print(blockheight.text)

def checkaddress():
    """Get the latest tx count of address"""
    response = requests.get("https://blockstream.info/api/address/bc1qs7gd29ptzvyc8s9etpcp07xny6v6krz3jhklya")
    jsonresponse = json.loads(response.text)
    return jsonresponse

address_info = checkaddress()
print(address_info["chain_stats"])
print(address_info["chain_stats"]["tx_count"])
tx_count = (address_info["chain_stats"]["tx_count"])

# https://blockstream.info/api/address/bc1qs7gd29ptzvyc8s9etpcp07xny6v6krz3jhklya

def is_tx_count_different(threshold):
    """Returns whether the tx count is above a certain threshold or not, boolean"""
    if tx_count > threshold:
        result = True
    else: result = False
    return result

def send_sms():
    print("Sending SMS")
    message = smsalert.client.messages \
                    .create(
                         body="There has been a transaction at your address",
                     from_= secrets.twilio_phone,
                     to= secrets.my_phone
                 )

    return(message.sid)

while True:
  print("Checking transactions at address")
  time.sleep(5)
  if is_tx_count_different(506) == True:
      send_sms()
      sys.exit()
  else: print("No new transactions at this address")

