import requests, json
from config import *
from psaw import PushshiftAPI
import datetime
import config
import psycopg2
import psycopg2.extras

HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET}
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL) 

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

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
    print("Placing order: " + symbol + " " + qty + " Shares")
    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)

def get_reddit_mentions():
    cursor.execute("""
        SELECT * FROM mention
    """)

    mentions = cursor.fetchall()

    return mentions

def get_mention_counts():
    cursor.execute("""
        SELECT COUNT(*) AS num_mentions, stock_id, symbol
        FROM mention JOIN stock ON stock.id = mention.stock_id
        GROUP BY stock_id, symbol
        ORDER BY num_mentions DESC
    """)
    mention_counts = cursor.fetchall()

    return mention_counts
