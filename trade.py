import requests, json
from config import *

HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    
    return json.loads(r.content)

def create_order(symbol, qty, side, type1, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type1,
        "time_in_force": time_in_force
    }
    
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    print("Placing order: " + "AAPL" + " " + "100" + " Shares")
    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)

