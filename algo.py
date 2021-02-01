#  Where the magic happens
from psaw import PushshiftAPI
import datetime
import config
import queries
import alpaca_trade_api as tradeapi
import psycopg2
import psycopg2.extras


mc = queries.get_mention_counts()



