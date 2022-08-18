#!/usr/bin/env python3
"""Print out the latest data on the mempool and the latest block height"""
import requests
import json

def checksite():
    """Gets latest data on the mempool"""
    response = requests.get("https://blockstream.info/api/mempool")
    jsonresponse = json.loads(response.text)
    return jsonresponse

mempool = checksite()
print(mempool)

blockheight = requests.get("https://blockstream.info/api/blocks/tip/height")
print(blockheight.text)
