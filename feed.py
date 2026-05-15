#!/usr/bin/env python3
"""Binance depth websocket feed -> Redis signal bus."""
import json
import os

import redis
import websocket
from dotenv import load_dotenv

load_dotenv()
r = redis.from_url(os.environ["REDIS_URL"])
WS = "wss://fstream.binance.com/ws/xauusdt@depth20@100ms"


def on_message(ws, msg):
    book = json.loads(msg)
    r.publish("depth:xauusdt", json.dumps({"b": book.get("b"), "a": book.get("a")}))


if __name__ == "__main__":
    websocket.WebSocketApp(WS, on_message=on_message).run_forever()
