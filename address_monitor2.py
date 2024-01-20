#!/usr/bin/env python3
"""Print out the latest data on the mempool and the latest block height"""
import requests
import json
import smsalert
import secrets
import time
import sys

url = "https://mempool.space/signet/api/address/"

# or "https://mempool.space/api/address/"
# or "https://blockstream.info/api/address/"

addresses = ["tb1qusjgdyt0d6rw0lh0xdqevpa3aste4j9n4cj4y6", "tb1qdfnge99t2p7a3hpeg43v26wex799jea92fyspn", "tb1qewg2v9pm4sdh98lmzx0fpzalg8ktuq4mf0c50m"]
thresholds = [1, 0, 0]

thresholds_dict = dict(zip(addresses, thresholds))
print(thresholds_dict)

tx_counts = []

def checkaddresses(url, addresses):
        i=0
        while i < len(addresses):
            response = requests.get(url + addresses[i])
            jsonresponse = json.loads(response.text)
            tx_count = jsonresponse["chain_stats"]["tx_count"]
            tx_counts.append(tx_count)
            i = i+1
        return tx_counts

tx_count_list = checkaddresses(url, addresses)

def is_tx_count_different(addresses, tx_count_list, thresholds_dict):
    tx_count_dict = dict(zip(addresses, tx_count_list))
# Comparing two dictionaries
    set_1 = set(tx_count_dict.items())
    set_2 = set(thresholds_dict.items())
    x = set_1 - set_2
    y = dict(x)
    z = list(y)
    return(z)

address_diff_list = is_tx_count_different(addresses, tx_count_list, thresholds_dict)
print(address_diff_list)

j = ""

def send_sms(j):
    print("Sending SMS")
    message = smsalert.client.messages \
                    .create(
                         body="There has been a transaction at " + j,
                    from_= secrets.twilio_phone,
                    to= secrets.my_phone
                 )

    return(message.sid)

while True:
  time.sleep(5)
  print("Checking transactions at addresses")
  tx_count_list = checkaddresses(url, addresses)
  address_diff_list = is_tx_count_different(addresses, tx_count_list, thresholds_dict)
  if len(address_diff_list) != 0:
      k=0
      while k < len(address_diff_list):
          send_sms(address_diff_list[k])
          k = k+1
      sys.exit()
  else: print("No new transactions at addresses")

