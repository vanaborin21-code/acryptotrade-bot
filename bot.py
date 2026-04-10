#!/usr/bin/env python3
"""ACryptoTrade — live scalping bot (XAU-USDT, 20x isolated margin)."""
import os
import time

import yaml
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
cfg = yaml.safe_load(open("config.yaml"))
client = Client(os.environ["BINANCE_API_KEY"], os.environ["BINANCE_API_SECRET"])

SYMBOL = cfg["strategy"]["pair"].replace("-", "")
LEVERAGE = cfg["strategy"]["leverage"]
THRESHOLD = cfg["strategy"]["spread_threshold"]


def run():
    client.futures_change_leverage(symbol=SYMBOL, leverage=LEVERAGE)
    while True:
        ob = client.futures_order_book(symbol=SYMBOL, limit=20)
        bid, ask = float(ob["bids"][0][0]), float(ob["asks"][0][0])
        if (ask - bid) / bid < THRESHOLD:
            client.futures_create_order(symbol=SYMBOL, side="BUY",
                                        type="MARKET", quantity=0.02)
        time.sleep(0.2)


if __name__ == "__main__":
    run()
