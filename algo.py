#  Where the magic happens
from psaw import PushshiftAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime, os, smtplib
import config, contact_list, queries
import alpaca_trade_api as tradeapi
import psycopg2, psycopg2.extras

def run_logic():
    mc = queries.get_mention_counts()
    count = 0 
    temp = []
    for m in mc:
        temp.append(m)
        count += 1
        if count > 9:
            break
    
    str1 = ""
    for t in temp:
        str1 += str(t)

    hml = "<!DOCTYPE html><html><head></head><body><h1>Your Daily Algo Report</h1><h3>Today's Picks</h3><p>" + str1 + "</p><br><P>Best,</P><p>Avenue B Algo</P></body></html>"
    
    return hml

