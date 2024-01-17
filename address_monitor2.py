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
# print(mempool)

# blockheight = requests.get("https://blockstream.info/api/blocks/tip/height")
# print(blockheight.text)


url = "https://mempool.space/signet/api/address/"

# or "https://mempool.space/api/address/"
# or "https://blockstream.info/api/address/"

addresses = ["tb1qusjgdyt0d6rw0lh0xdqevpa3aste4j9n4cj4y6", "tb1qdfnge99t2p7a3hpeg43v26wex799jea92fyspn", "tb1qewg2v9pm4sdh98lmzx0fpzalg8ktuq4mf0c50m"]
thresholds = [0, -1, 0]

thresholds_dict = dict(zip(addresses, thresholds))
print(thresholds_dict)

def checkaddress(url, address):
    """Get the latest tx count of address"""
    response = requests.get(url + address)
    jsonresponse = json.loads(response.text)
    return jsonresponse

tx_counts = []

for address in addresses:
	address_info = checkaddress(url, address)
	tx_count = (address_info["chain_stats"]["tx_count"])
	tx_counts.append(tx_count)

print(tx_counts)

tx_count_dict = dict(zip(addresses, tx_counts))

z = []
if tx_count_dict == thresholds_dict:
	print("There hasn't been a transaction")
else:
# Comparing two dictionaries
    set_1 = set(tx_count_dict.items())
    set_2 = set(thresholds_dict.items())
    x = set_1 - set_2
    y = dict(x)
    z = list(y)
    print(z)

# def is_tx_count_different(threshold):
#    """Returns whether the tx count is above a certain threshold or not, boolean"""
#    if tx_count > threshold`
#
#        result = True
#    else: result = False
#    return result

i = ""

def send_sms(i):
    print("Sending SMS")
    message = smsalert.client.messages \
                    .create(
                         body="There has been a transaction at " + i,
                    from_= secrets.twilio_phone,
                    to= secrets.my_phone
                 )

    return(message.sid)

while True:
  print("Checking transactions at addresses")
  time.sleep(5)
  if len(z) != 0:
      j=0
      while j < len(z):
          send_sms(z[j])
          j = j+1
      sys.exit()
  else: print("No new transactions at addresses")

